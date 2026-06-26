import torch
import torch.distributed as dist
import torch.nn as nn
from .wrap import _FSDPPolicy
from _typeshed import Incomplete
from enum import Enum
from torch.distributed.fsdp._common_utils import _FSDPState
from torch.distributed.fsdp._init_utils import ProcessGroupType
from torch.distributed.fsdp.api import BackwardPrefetch, CPUOffload, MixedPrecision, OptimStateDictConfig, ShardingStrategy, StateDictConfig, StateDictSettings, StateDictType
from typing import Any, Callable, Dict, Generator, Iterable, Iterator, List, Tuple

__all__ = ['FullyShardedDataParallel', 'OptimStateKeyType']

class OptimStateKeyType(Enum):
    PARAM_NAME: Incomplete
    PARAM_ID: Incomplete

class FullyShardedDataParallel(nn.Module, _FSDPState):
    '''
    A wrapper for sharding Module parameters across data parallel workers. This
    is inspired by `Xu et al.`_ as well as the ZeRO Stage 3 from DeepSpeed_.
    FullyShardedDataParallel is commonly shortened to FSDP.

    .. _`Xu et al.`: https://arxiv.org/abs/2004.13336
    .. _DeepSpeed: https://www.deepspeed.ai/

    Example::

        >>> # xdoctest: +SKIP("undefined variables")
        >>> import torch
        >>> from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
        >>> torch.cuda.set_device(device_id)
        >>> sharded_module = FSDP(my_module)
        >>> optim = torch.optim.Adam(sharded_module.parameters(), lr=0.0001)
        >>> x = sharded_module(x, y=3, z=torch.Tensor([1]))
        >>> loss = x.sum()
        >>> loss.backward()
        >>> optim.step()

    .. warning::
        The optimizer must be initialized *after* the module has been wrapped,
        since FSDP will shard parameters in-place and this will break any
        previously initialized optimizers.

    .. warning::
        If the destination CUDA device has ID ``dev_id``, either (1)
        ``module`` should already be placed on that device, (2) the device
        should be set using ``torch.cuda.set_device(dev_id)``, or (3)
        ``dev_id`` should be passed into the ``device_id`` constructor
        argument. This FSDP instance\'s compute device will be that destination
        device. For (1) and (3), the FSDP initialization always occurs on GPU.
        For (2), the FSDP initialization happens on ``module`` \'s current
        device, which may be CPU.

    .. warning::
        FSDP currently does not support gradient accumulation outside
        ``no_sync()`` when using CPU offloading. Trying to do so yields
        incorrect results since FSDP will use the newly-reduced gradient
        instead of accumulating with any existing gradient.

    .. warning::
        Changing the original parameter variable names after construction will
        lead to undefined behavior.

    .. warning::
        Passing in `sync_module_states=True` flag requires module to be put
        on GPU, or to use ``device_id`` argument to specify a CUDA device that
        FSDP will move module to. This is because ``sync_module_states=True``
        requires GPU communication.

    .. warning::
        As of PyTorch 1.12, FSDP only offers limited support for shared parameters
        (for example, setting one ``Linear`` layer\'s weight to another\'s). In
        particular, modules that share parameters must be wrapped as part of the
        same FSDP unit. If enhanced shared parameter support is needed for your
        use case, please ping https://github.com/pytorch/pytorch/issues/77724

    .. note:
        Attempting to run the forward pass of a submodule that is contained in an
        FSDP instance is not supported and will result in errors. This is because the
        submodule\'s parameters will be sharded, but it itself is not an FSDP instance,
        so its forward pass will not all-gather the full parameters appropriately.
        This could potentially happen when attempting to run only the encoder of a
        encoder-decoder model, and the encoder is not wrapped in its own FSDP instance. To
        resolve this, please wrap the submodule in its own FSDP unit.

    .. note::
        Inputs into FSDP ``forward`` function will be moved to compute device
        (same device FSDP module is on) before running ``forward``, so user does
        not have to manually move inputs from CPU -> GPU.

    Args:
        module (nn.Module):
            This is the module to be wrapped with FSDP.
        process_group: Optional[Union[ProcessGroup, Tuple[ProcessGroup, ProcessGroup]]]
            This is the process group used for collective communications and
            the one over which the model is sharded. For hybrid sharding strategies such as
            ``ShardingStrategy.HYBRID_SHARD`` users can
            pass in a tuple of process groups representing the groups to shard and replicate across,
            respectively.
        sharding_strategy (Optional[ShardingStrategy]):
            This configures the sharding strategy used by FSDP, which may trade
            off memory saving and communication overhead. See
            :class:`ShardingStrategy` for details. (Default: ``FULL_SHARD``)
        cpu_offload (Optional[CPUOffload]):
            This configures CPU offloading. If this is set to ``None``, then
            no CPU offloading happens. See :class:`CPUOffload` for details.
            (Default: ``None``)
        auto_wrap_policy (Optional[Union[Callable[[nn.Module, bool, int], bool], _FSDPPolicy]]):
            This is either ``None``, an ``_FSDPPolicy``, or a callable of
            a fixed signature. If it is ``None``, then ``module`` is wrapped
            with only a top-level FSDP instance without any nested wrapping. If
            it is an ``_FSDPPolicy``, then the wrapping follows the given
            policy. ``ModuleWrapPolicy`` in ``torch.distributed.fsdp.wrap.py``
            is an example. If it is a callable, then it should take in three
            arguments ``module: nn.Module``, ``recurse: bool``, and
            ``nonwrapped_numel: int`` and should return a ``bool`` specifying
            whether the passed-in ``module`` should be wrapped if
            ``recurse=False`` or if the traversal should continue down the
            subtree if ``recurse=True``. Additional custom arguments may be
            added to the callable. The ``size_based_auto_wrap_policy`` in
            ``torch.distributed.fsdp.wrap.py`` gives an example callable that
            wraps a module if the parameters in its subtree exceed 100M numel.
            A good practice is to print the model after wrapping and adjust as
            needed.

            Example::

                >>> def custom_auto_wrap_policy(
                >>>     module: nn.Module,
                >>>     recurse: bool,
                >>>     nonwrapped_numel: int,
                >>>     # Additional custom arguments
                >>>     min_num_params: int = int(1e8),
                >>> ) -> bool:
                >>>     return nonwrapped_numel >= min_num_params
                >>> # Configure a custom `min_num_params`
                >>> my_auto_wrap_policy = functools.partial(custom_auto_wrap_policy, min_num_params=int(1e5))

        backward_prefetch (Optional[BackwardPrefetch]):
            This configures explicit backward prefetching of all-gathers. See
            :class:`BackwardPrefetch` for details. (Default: ``BACKWARD_PRE``)
        mixed_precision (Optional[MixedPrecision]):
            This configures native mixed precision for FSDP. If this is set to
            ``None``, then no mixed precision is used. Otherwise, parameter,
            buffer, and gradient reduction dtypes can be set. See
            :class:`MixedPrecision` for details. (Default: ``None``)
        ignored_modules (Optional[Iterable[torch.nn.Module]]): Modules whose
            own parameters and child modules\' parameters and buffers are
            ignored by this instance. None of the modules directly in
            ``ignored_modules`` should be :class:`FullyShardedDataParallel`
            instances, and any child modules that are already-constructed
            :class:`FullyShardedDataParallel` instances will not be ignored if
            they are nested under this instance. This argument may be used to
            avoid sharding specific parameters at module granularity when using an
            ``auto_wrap_policy`` or if parameters\' sharding is not managed by
            FSDP. (Default: ``None``)
        param_init_fn (Optional[Callable[[nn.Module], None]]):
            A ``Callable[torch.nn.Module] -> None`` that
            specifies how modules that are currently on the meta device should be initialized
            onto an actual device. Note that as of v1.12, we detect modules on the meta
            device via ``is_meta`` check and apply a default initialization that calls
            ``reset_parameters`` method on the passed in ``nn.Module`` if ``param_init_fn``
            is not specified, otherwise we run ``param_init_fn`` to initialize the passed
            in ``nn.Module``. In particular, this means that if ``is_meta=True`` for any
            module parameters for modules that will be wrapped with FSDP and ``param_init_fn``
            is not specified, we assume your module properly implements a ``reset_parameters()``
            and will throw errors if not. Note that additionally, we offer support for modules
            initialized with torchdistX\'s (https://github.com/pytorch/torchdistX)
            ``deferred_init`` API. In this case, deferred modules would be initialized
            by a default initialization function that calls torchdistX\'s
            ``materialize_module``, or the passed in ``param_init_fn``, if it is not
            ``None``. The same ``Callable`` is applied to initialize all meta modules.
            Note that this initialization function is applied before doing any FSDP sharding
            logic.

            Example::

                >>> # xdoctest: +SKIP("undefined variables")
                >>> module = MyModule(device="meta")
                >>> def my_init_fn(module):
                >>>     # responsible for initializing a module, such as with reset_parameters
                >>>     ...
                >>> fsdp_model = FSDP(module, param_init_fn=my_init_fn, auto_wrap_policy=size_based_auto_wrap_policy)
                >>> print(next(fsdp_model.parameters()).device) # current CUDA device
                >>> # With torchdistX
                >>> module = deferred_init.deferred_init(MyModule, device="cuda")
                >>> # Will initialize via deferred_init.materialize_module().
                >>> fsdp_model = FSDP(module, auto_wrap_policy=size_based_auto_wrap_policy)

        device_id (Optional[Union[int, torch.device]]): An ``int`` or ``torch.device``
            describing the CUDA device the FSDP module should be moved to determining where
            initialization such as sharding takes place. If this argument is not specified
            and ``module`` is on CPU, we issue a warning mentioning that this argument can
            be specified for faster initialization. If specified, resulting FSDP instances
            will reside on this device, including moving ignored modules\' parameters if
            needed. Note that if ``device_id`` is specified but ``module`` is already on a
            different CUDA device, an error will be thrown. (Default: ``None``)
        sync_module_states (bool): If ``True``, each individually wrapped FSDP unit will broadcast
            module parameters from rank 0 to ensure they are the same across all ranks after
            initialization. This helps ensure model parameters are the same across ranks
            before starting training, but adds communication overhead to ``__init__``, as at least
            one broadcast is triggered per individually wrapped FSDP unit.
            This can also help load checkpoints taken by ``state_dict`` and to be loaded by
            ``load_state_dict`` in a memory efficient way. See documentation for
            :class:`FullStateDictConfig` for an example of this. (Default: ``False``)
        forward_prefetch (bool): If ``True``, then FSDP *explicitly* prefetches
            the next upcoming all-gather while executing in the forward pass.
            This may improve communication and computation overlap for CPU
            bound workloads. This should only be used for static graph models
            since the forward order is fixed based on the first iteration\'s
            execution. (Default: ``False``)
        limit_all_gathers (bool): If ``False``, then FSDP allows the CPU
            thread to schedule all-gathers without any extra synchronization.
            If ``True``, then FSDP explicitly synchronizes the CPU thread to
            prevent too many in-flight all-gathers. This ``bool`` only affects
            the sharded strategies that schedule all-gathers. Enabling this can
            help lower the number of CUDA malloc retries.
        ignored_parameters (Optional[Iterable[torch.nn.Parameter]]): Ignored
            parameters will not be managed by this FSDP instance,
            that means these parameters will not be flattened and sharded by FSDP,
            their gradients will not be synchronized as well. With this newly added
            argument, ``ignored_modules`` could be deprecated soon. For backward compatibility,
            both ``ignored_parameters`` and ``ignored_modules`` are kept for now,
            but FSDP only allows one of them to be specified as not ``None``.
    '''
    def __init__(self, module: nn.Module, process_group: ProcessGroupType = None, sharding_strategy: ShardingStrategy | None = None, cpu_offload: CPUOffload | None = None, auto_wrap_policy: Callable | _FSDPPolicy | None = None, backward_prefetch: BackwardPrefetch | None = ..., mixed_precision: MixedPrecision | None = None, ignored_modules: Iterable[torch.nn.Module] | None = None, param_init_fn: Callable[[nn.Module], None] | None = None, device_id: int | torch.device | None = None, sync_module_states: bool = False, forward_prefetch: bool = False, limit_all_gathers: bool = False, use_orig_params: bool = False, ignored_parameters: Iterable[torch.nn.Parameter] | None = None) -> None: ...
    @property
    def module(self) -> nn.Module:
        """
        Returns the wrapped module (like :class:`DistributedDataParallel`).
        """
    def __getattr__(self, name: str) -> Any:
        """Forward missing attributes to the wrapped module."""
    def __getitem__(self, key: int) -> Any:
        """Forward indexing calls in case the module is an ``nn.Sequential``."""
    def check_is_root(self) -> bool: ...
    @staticmethod
    def fsdp_modules(module: nn.Module, root_only: bool = False) -> List['FullyShardedDataParallel']:
        """
        Returns all nested FSDP instances, possibly including ``module`` itself
        and only including FSDP root modules if ``root_only=True``.

        Args:
            module (torch.nn.Module): Root module, which may or may not be an
                ``FSDP`` module.
            root_only (bool): Whether to return only FSDP root modules.
                (Default: ``False``)

        Returns:
            List[FullyShardedDataParallel]: FSDP modules that are nested in
            the input ``module``.
        """
    def apply(self, fn: Callable[[nn.Module], None]) -> FullyShardedDataParallel:
        """Applies ``fn`` recursively to every submodule (as returned by ``.children()``)
        as well as self. Typical use includes initializing the parameters of a model
        (see also :ref:`nn-init-doc`).

        Compared to ``torch.nn.Module.apply``, this version additionally gathers
        the full parameters before applying ``fn``. It should not be called from
        within another ``summon_full_params`` context.

        Args:
            fn (:class:`Module` -> None): function to be applied to each submodule

        Returns:
            Module: self
        """
    @staticmethod
    def set_state_dict_type(module: nn.Module, state_dict_type: StateDictType, state_dict_config: StateDictConfig | None = None, optim_state_dict_config: OptimStateDictConfig | None = None) -> StateDictSettings:
        '''
        Set the ``state_dict_type`` and the corresponding (optional)
        configurations of all the descendant FSDP modules of the target module.
        The target module does not have to be a FSDP module. If the target
        module is a FSDP module, its ``state_dict_type`` will also be changed.

        .. note:: This API should be called for only the top-level (root)
            module.

        .. note:: This API enables users to transparently use the conventional
            ``state_dict`` API to take model checkpoints in cases where the
            root FSDP module is wrapped by another ``nn.Module``. For example,
            the following will ensure ``state_dict`` is called on all non-FSDP
            instances, while dispatching into `sharded_state_dict` implementation
            for FSDP:

        Example::

            >>> # xdoctest: +SKIP("undefined variables")
            >>> model = DDP(FSDP(...))
            >>> FSDP.set_state_dict_type(
            >>>     model,
            >>>     StateDictType.SHARDED_STATE_DICT,
            >>>     state_dict_config = ShardedStateDictConfig(offload_to_cpu=True),
            >>>     optim_state_dict_config = OptimStateDictConfig(offload_to_cpu=True),
            >>> )
            >>> param_state_dict = model.state_dict()
            >>> optim_state_dict = FSDP.optim_state_dict(model, optim)

        Args:
            module (torch.nn.Module): Root module.
            state_dict_type (StateDictType): the desired ``state_dict_type`` to set.
            state_dict_config (Optional[StateDictConfig]): the configuration for the
                target ``state_dict_type``.
        Returns:
            A StateDictSettings that include the previous state_dict type and
            configuration for the module.
        '''
    @staticmethod
    def get_state_dict_type(module: nn.Module) -> StateDictSettings: ...
    @staticmethod
    def state_dict_type(module: nn.Module, state_dict_type: StateDictType, state_dict_config: StateDictConfig | None = None, optim_state_dict_config: OptimStateDictConfig | None = None) -> Generator:
        '''
        A context manager to set the ``state_dict_type`` of all the descendant
        FSDP modules of the target module. This context manager has the same
        functions as :meth:`set_state_dict_type`. Read the document of
        :meth:`set_state_dict_type` for the detail.

        Example::

            >>> # xdoctest: +SKIP("undefined variables")
            >>> model = DDP(FSDP(...))
            >>> with FSDP.state_dict_type(
            >>>     model,
            >>>     StateDictType.SHARDED_STATE_DICT,
            >>> ):
            >>>     checkpoint = model.state_dict()

        Args:
            module (torch.nn.Module): Root module.
            state_dict_type (StateDictType): the desired ``state_dict_type`` to set.
            state_dict_config (Optional[StateDictConfig]): the configuration for the
                target ``state_dict_type``.
        '''
    def forward(self, *args: Any, **kwargs: Any) -> Any:
        """
        Runs the forward pass for the wrapped module, inserting FSDP-specific
        pre- and post-forward sharding logic.
        """
    @staticmethod
    def summon_full_params(module: nn.Module, recurse: bool = True, writeback: bool = True, rank0_only: bool = False, offload_to_cpu: bool = False, with_grads: bool = False) -> Generator:
        """A context manager to expose full params for FSDP instances.
        Can be useful *after* forward/backward for a model to get
        the params for additional processing or checking. It can take a non-FSDP
        module and will summon full params for all contained FSDP modules as
        well as their children, depending on the ``recurse`` argument.

        .. note:: This can be used on inner FSDPs.
        .. note:: This can *not* be used within a forward or backward pass. Nor
            can forward and backward be started from within this context.
        .. note:: Parameters will revert to their local shards after the context
            manager exits, storage behavior is the same as forward.
        .. note:: The full parameters can be modified, but only the portion
            corresponding to the local param shard will persist after the
            context manager exits (unless ``writeback=False``, in which case
            changes will be discarded). In the case where FSDP does not shard
            the parameters, currently only when ``world_size == 1``, or ``NO_SHARD``
            config, the modification is persisted regardless of ``writeback``.
        .. note:: This method works on modules which are not FSDP themselves but
            may contain multiple independent FSDP units. In that case, the given
            arguments will apply to all contained FSDP units.

        .. warning:: Note that ``rank0_only=True`` in conjunction with
            ``writeback=True`` is not currently supported and will raise an
            error. This is because model parameter shapes would be different
            across ranks within the context, and writing to them can lead to
            inconsistency across ranks when the context is exited.

        .. warning:: Note that ``offload_to_cpu`` and ``rank0_only=False`` will
            result in full parameters being redundantly copied to CPU memory for
            GPUs that reside on the same machine, which may incur the risk of
            CPU OOM. It is recommended to use ``offload_to_cpu`` with
            ``rank0_only=True``.

        Args:
            recurse (bool, Optional): recursively summon all params for nested
                FSDP instances (default: True).
            writeback (bool, Optional): if ``False``, modifications to params are
                discarded after the context manager exits;
                disabling this can be slightly more efficient (default: True)
            rank0_only (bool, Optional): if ``True``, full parameters are
                materialized on only global rank 0. This means that within the
                context, only rank 0 will have full parameters and the other
                ranks will have sharded parameters. Note that setting
                ``rank0_only=True`` with ``writeback=True`` is not supported,
                as model parameter shapes will be different across ranks
                within the context, and writing to them can lead to
                inconsistency across ranks when the context is exited.
            offload_to_cpu (bool, Optional): If ``True``, full parameters are
                offloaded to CPU. Note that this offloading currently only
                occurs if the parameter is sharded (which is only not the case
                for world_size = 1 or ``NO_SHARD`` config). It is recommended
                to use ``offload_to_cpu`` with ``rank0_only=True`` to avoid
                redundant copies of model parameters being offloaded to the same CPU memory.
            with_grads (bool, Optional): If ``True``, gradients are also
                unsharded with the parameters. Currently, this is only
                supported when passing ``use_orig_params=True`` to the FSDP
                constructor and ``offload_to_cpu=False`` to this method.
                (Default: ``False``)
        """
    def named_buffers(self, *args, **kwargs) -> Iterator[Tuple[str, torch.Tensor]]:
        """
        Overrides :meth:`named_buffers()` to intercept buffer names and
        remove all occurrences of the FSDP-specific flattened buffer prefix
        when inside the :meth:`summon_full_params` context manager.
        """
    def named_parameters(self, *args, **kwargs) -> Iterator[Tuple[str, torch.nn.Parameter]]:
        """
        Overrides :meth:`named_parameters()` to intercept parameter names and
        remove all occurrences of the FSDP-specific flattened parameter prefix
        when inside the :meth:`summon_full_params` context manager.
        """
    def no_sync(self) -> Generator:
        """
        A context manager to disable gradient synchronizations across FSDP
        instances. Within this context, gradients will be accumulated in module
        variables, which will later be synchronized in the first
        forward-backward pass after exiting the context. This should only be
        used on the root FSDP instance and will recursively apply to all
        children FSDP instances.

        .. note:: This likely results in higher memory usage because FSDP will
            accumulate the full model gradients (instead of gradient shards)
            until the eventual sync.

        .. note:: When used with CPU offloading, the gradients will not be
            offloaded to CPU when inside the context manager. Instead, they
            will only be offloaded right after the eventual sync.
        """
    def clip_grad_norm_(self, max_norm: float | int, norm_type: float | int = 2.0) -> torch.Tensor:
        '''
        Clips the gradient norm of all parameters. The norm is computed over
        all parameters\' gradients as viewed as a single vector, and the
        gradients are modified in-place.

        Args:
            max_norm (float or int): max norm of the gradients
            norm_type (float or int): type of the used p-norm. Can be ``\'inf\'``
                for infinity norm.

        Returns:
            Total norm of the parameters (viewed as a single vector).

        .. note:: If every FSDP instance uses ``NO_SHARD``, meaning that no
            gradients are sharded across ranks, then you may directly use
            :func:`torch.nn.utils.clip_grad_norm_`.

        .. note:: If at least some FSDP instance uses a sharded strategy (i.e.
            one other than ``NO_SHARD``), then you should use this method
            instead of :func:`torch.nn.utils.clip_grad_norm_` since this method
            handles the fact that gradients are sharded across ranks.

        .. note:: The total norm returned will have the "largest" dtype across
            all parameters/gradients as defined by PyTorch\'s type promotion
            semantics. For example, if *all* parameters/gradients use a low
            precision dtype, then the returned norm\'s dtype will be that low
            precision dtype, but if there exists at least one parameter/
            gradient using FP32, then the returned norm\'s dtype will be FP32.

        .. warning:: This needs to be called on all ranks since it uses
            collective communications.
        '''
    @staticmethod
    def full_optim_state_dict(model: torch.nn.Module, optim: torch.optim.Optimizer, optim_input: List[Dict[str, Any]] | Iterable[torch.nn.Parameter] | None = None, rank0_only: bool = True, group: dist.ProcessGroup | None = None) -> Dict[str, Any]:
        '''
        Consolidates the full optimizer state on rank 0 and returns it
        as a :class:`dict` following the convention of
        :meth:`torch.optim.Optimizer.state_dict`, i.e. with keys ``"state"``
        and ``"param_groups"``. The flattened parameters in ``FSDP`` modules
        contained in ``model`` are mapped back to their unflattened parameters.

        .. warning:: This needs to be called on all ranks since it uses
            collective communications. However, if ``rank0_only=True``, then
            the state dict is only populated on rank 0, and all other ranks
            return an empty :class:`dict`.

        .. warning:: Unlike ``torch.optim.Optimizer.state_dict()``, this method
            uses full parameter names as keys instead of parameter IDs.

        .. note:: Like in :meth:`torch.optim.Optimizer.state_dict`, the tensors
            contained in the optimizer state dict are not cloned, so there may
            be aliasing surprises. For best practices, consider saving the
            returned optimizer state dict immediately, e.g. using
            ``torch.save()``.

        Args:
            model (torch.nn.Module): Root module (which may or may not be a
                :class:`FullyShardedDataParallel` instance) whose parameters
                were passed into the optimizer ``optim``.
            optim (torch.optim.Optimizer): Optimizer for ``model`` \'s
                parameters.
            optim_input (Optional[Union[List[Dict[str, Any]], Iterable[torch.nn.Parameter]]]):
                Input passed into the optimizer ``optim`` representing either a
                :class:`list` of parameter groups or an iterable of parameters;
                if ``None``, then this method assumes the input was
                ``model.parameters()``. This argument is deprecated, and there
                is no need to pass it in anymore. (Default: ``None``)
            rank0_only (bool): If ``True``, saves the populated :class:`dict`
                only on rank 0; if ``False``, saves it on all ranks. (Default:
                ``True``)
            group (dist.ProcessGroup): Model\'s process group or ``None`` if using
                the default process group. (Default: ``None``)

        Returns:
            Dict[str, Any]: A :class:`dict` containing the optimizer state for
            ``model`` \'s original unflattened parameters and including keys
            "state" and "param_groups" following the convention of
            :meth:`torch.optim.Optimizer.state_dict`. If ``rank0_only=True``,
            then nonzero ranks return an empty :class:`dict`.
        '''
    @staticmethod
    def sharded_optim_state_dict(model: torch.nn.Module, optim: torch.optim.Optimizer, group: dist.ProcessGroup | None = None) -> Dict[str, Any]:
        """
        The API is similar to :meth:`full_optim_state_dict` but this API chunks
        all non-zero-dimension states to :class:`ShardedTensor` to save memory.
        This API should only be used when the model ``state_dict`` is derived
        with the context manager ``with state_dict_type(SHARDED_STATE_DICT):``.

        For the detailed usage, refer to :meth:`full_optim_state_dict`.

        .. warning:: The returned state dict contains ``ShardedTensor`` and
            cannot be directly used by the regular ``optim.load_state_dict``.
        """
    @staticmethod
    def shard_full_optim_state_dict(full_optim_state_dict: Dict[str, Any], model: torch.nn.Module, optim_input: List[Dict[str, Any]] | Iterable[torch.nn.Parameter] | None = None, optim: torch.optim.Optimizer | None = None) -> Dict[str, Any]:
        '''
        Shards the full optimizer state dict ``full_optim_state_dict`` by
        remapping the state to flattened parameters instead of unflattened
        parameters and restricting to only this rank\'s part of the optimizer
        state. The first argument should be the return value of
        :meth:`full_optim_state_dict`.

        Example::

            >>> # xdoctest: +SKIP("undefined variables")
            >>> from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
            >>> model, optim = ...
            >>> full_osd = FSDP.full_optim_state_dict(model, optim)
            >>> torch.save(full_osd, PATH)
            >>> # Define new model with possibly different world size
            >>> new_model, new_optim = ...
            >>> full_osd = torch.load(PATH)
            >>> sharded_osd = FSDP.shard_full_optim_state_dict(full_osd, new_model)
            >>> new_optim.load_state_dict(sharded_osd)

        .. note:: Both :meth:`shard_full_optim_state_dict` and
            :meth:`scatter_full_optim_state_dict` may be used to get the
            sharded optimizer state dict to load. Assuming that the full
            optimizer state dict resides in CPU memory, the former requires
            each rank to have the full dict in CPU memory, where each rank
            individually shards the dict without any communication, while the
            latter requires only rank 0 to have the full dict in CPU memory,
            where rank 0 moves each shard to GPU memory (for NCCL) and
            communicates it to ranks appropriately. Hence, the former has
            higher aggregate CPU memory cost, while the latter has higher
            communication cost.

        Args:
            full_optim_state_dict (Dict[str, Any]): Optimizer state dict
                corresponding to the unflattened parameters and holding the
                full non-sharded optimizer state.
            model (torch.nn.Module): Root module (which may or may not be a
                :class:`FullyShardedDataParallel` instance) whose parameters
                correspond to the optimizer state in ``full_optim_state_dict``.
            optim_input (Optional[Union[List[Dict[str, Any]], Iterable[torch.nn.Parameter]]]):
                Input passed into the optimizer representing either a
                :class:`list` of parameter groups or an iterable of parameters;
                if ``None``, then this method assumes the input was
                ``model.parameters()``. This argument is deprecated, and there
                is no need to pass it in anymore. (Default: ``None``)
            optim (Optional[torch.optim.Optimizer]): Optimizer that will load
                the state dict returned by this method. This is the preferred
                argument to use over ``optim_input``. (Default: ``None``)

        Returns:
            Dict[str, Any]: The full optimizer state dict now remapped to
            flattened parameters instead of unflattened parameters and
            restricted to only include this rank\'s part of the optimizer state.
        '''
    @staticmethod
    def flatten_sharded_optim_state_dict(sharded_optim_state_dict: Dict[str, Any], model: torch.nn.Module, optim: torch.optim.Optimizer) -> Dict[str, Any]:
        """
        The API is similar to :meth:`shard_full_optim_state_dict`. The only
        difference is that the input ``sharded_optim_state_dict`` should be
        returned from :meth:`sharded_optim_state_dict`. Therefore, there will
        be all-gather calls on each rank to gather ``ShardedTensor`` s.

        Args:
            sharded_optim_state_dict (Dict[str, Any]): Optimizer state dict
                corresponding to the unflattened parameters and holding the
                sharded optimizer state.
            model (torch.nn.Module):
                Refer to :meth:``shard_full_optim_state_dict``.
            optim (torch.optim.Optimizer): Optimizer for ``model`` 's
            parameters.

        Returns:
            Refer to :meth:`shard_full_optim_state_dict`.
        """
    @staticmethod
    def scatter_full_optim_state_dict(full_optim_state_dict: Dict[str, Any] | None, model: torch.nn.Module, optim_input: List[Dict[str, Any]] | Iterable[torch.nn.Parameter] | None = None, optim: torch.optim.Optimizer | None = None, group: Any | None = None) -> Dict[str, Any]:
        '''
        Scatters the full optimizer state dict from rank 0 to all other ranks,
        returning the sharded optimizer state dict on each rank. The return
        value is the same as :meth:`shard_full_optim_state_dict`, and on rank
        0, the first argument should be the return value of
        :meth:`full_optim_state_dict`.

        Example::

            >>> # xdoctest: +SKIP("undefined variables")
            >>> from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
            >>> model, optim = ...
            >>> full_osd = FSDP.full_optim_state_dict(model, optim)  # only non-empty on rank 0
            >>> # Define new model with possibly different world size
            >>> new_model, new_optim, new_group = ...
            >>> sharded_osd = FSDP.scatter_full_optim_state_dict(full_osd, new_model, group=new_group)
            >>> new_optim.load_state_dict(sharded_osd)

        .. note:: Both :meth:`shard_full_optim_state_dict` and
            :meth:`scatter_full_optim_state_dict` may be used to get the
            sharded optimizer state dict to load. Assuming that the full
            optimizer state dict resides in CPU memory, the former requires
            each rank to have the full dict in CPU memory, where each rank
            individually shards the dict without any communication, while the
            latter requires only rank 0 to have the full dict in CPU memory,
            where rank 0 moves each shard to GPU memory (for NCCL) and
            communicates it to ranks appropriately. Hence, the former has
            higher aggregate CPU memory cost, while the latter has higher
            communication cost.

        Args:
            full_optim_state_dict (Optional[Dict[str, Any]]): Optimizer state
                dict corresponding to the unflattened parameters and holding
                the full non-sharded optimizer state if on rank 0; the argument
                is ignored on nonzero ranks.
            model (torch.nn.Module): Root module (which may or may not be a
                :class:`FullyShardedDataParallel` instance) whose parameters
                correspond to the optimizer state in ``full_optim_state_dict``.
            optim_input (Optional[Union[List[Dict[str, Any]], Iterable[torch.nn.Parameter]]]):
                Input passed into the optimizer representing either a
                :class:`list` of parameter groups or an iterable of parameters;
                if ``None``, then this method assumes the input was
                ``model.parameters()``. This argument is deprecated, and there
                is no need to pass it in anymore. (Default: ``None``)
            optim (Optional[torch.optim.Optimizer]): Optimizer that will load
                the state dict returned by this method. This is the preferred
                argument to use over ``optim_input``. (Default: ``None``)
            group (dist.ProcessGroup): Model\'s process group or ``None`` if
                using the default process group. (Default: ``None``)

        Returns:
            Dict[str, Any]: The full optimizer state dict now remapped to
            flattened parameters instead of unflattened parameters and
            restricted to only include this rank\'s part of the optimizer state.
        '''
    @staticmethod
    def rekey_optim_state_dict(optim_state_dict: Dict[str, Any], optim_state_key_type: OptimStateKeyType, model: torch.nn.Module, optim_input: List[Dict[str, Any]] | Iterable[torch.nn.Parameter] | None = None, optim: torch.optim.Optimizer | None = None) -> Dict[str, Any]:
        '''
        Re-keys the optimizer state dict ``optim_state_dict`` to use the key
        type ``optim_state_key_type``. This can be used to achieve
        compatibility between optimizer state dicts from models with FSDP
        instances and ones without.

        To re-key an FSDP full optimizer state dict (i.e. from
        :meth:`full_optim_state_dict`) to use parameter IDs and be loadable to
        a non-wrapped model::

            >>> # xdoctest: +SKIP("undefined variables")
            >>> wrapped_model, wrapped_optim = ...
            >>> full_osd = FSDP.full_optim_state_dict(wrapped_model, wrapped_optim)
            >>> nonwrapped_model, nonwrapped_optim = ...
            >>> rekeyed_osd = FSDP.rekey_optim_state_dict(full_osd, OptimStateKeyType.PARAM_ID, nonwrapped_model)
            >>> nonwrapped_optim.load_state_dict(rekeyed_osd)

        To re-key a normal optimizer state dict from a non-wrapped model to be
        loadable to a wrapped model::

            >>> # xdoctest: +SKIP("undefined variables")
            >>> nonwrapped_model, nonwrapped_optim = ...
            >>> osd = nonwrapped_optim.state_dict()
            >>> rekeyed_osd = FSDP.rekey_optim_state_dict(osd, OptimStateKeyType.PARAM_NAME, nonwrapped_model)
            >>> wrapped_model, wrapped_optim = ...
            >>> sharded_osd = FSDP.shard_full_optim_state_dict(rekeyed_osd, wrapped_model)
            >>> wrapped_optim.load_state_dict(sharded_osd)

        Returns:
            Dict[str, Any]: The optimizer state dict re-keyed using the
            parameter keys specified by ``optim_state_key_type``.
        '''
    @staticmethod
    def optim_state_dict(model: torch.nn.Module, optim: torch.optim.Optimizer, group: dist.ProcessGroup | None = None) -> Dict[str, Any]:
        '''
        Returns the state dict of ``optim`` for the ``model`` that is (partially)
        sharded by FSDP. The state may be sharded, consolidated, or consolidated
        on rank 0 only depending on the ``state_dict_type`` set by
        :meth:`set_state_dict_type` or :meth:`state_dict_type`.

        Example::

            >>> # xdoctest: +SKIP("undefined variables")
            >>> from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
            >>> from torch.distributed.fsdp import StateDictType
            >>> from torch.distributed.fsdp import FullStateDictConfig
            >>> from torch.distributed.fsdp import FullOptimStateDictConfig
            >>> # Save a checkpoint
            >>> model, optim = ...
            >>> FSDP.set_state_dict_type(
            >>>     model,
            >>>     StateDictType.FULL_STATE_DICT,
            >>>     FullStateDictConfig(rank0_only=False),
            >>>     FullOptimStateDictConfig(rank0_only=False),
            >>> )
            >>> state_dict = model.state_dict()
            >>> optim_state_dict = FSDP.optim_state_dict(model, optim)
            >>> save_a_checkpoint(state_dict, optim_state_dict)
            >>> # Load a checkpoint
            >>> model, optim = ...
            >>> state_dict, optim_state_dict = load_a_checkponit()
            >>> FSDP.set_state_dict_type(
            >>>     model,
            >>>     StateDictType.FULL_STATE_DICT,
            >>>     FullStateDictConfig(rank0_only=False),
            >>>     FullOptimStateDictConfig(rank0_only=False),
            >>> )
            >>> model.load_state_dict(state_dict)
            >>> optim_state_dict = FSDP.optim_state_dict_to_load(
            >>>     optim_state_dict, model, optim
            >>> )
            >>> optim.load_state_dict(optim_state_dict)

        Args:
            model (torch.nn.Module): Root module (which may or may not be a
                :class:`FullyShardedDataParallel` instance) whose parameters
                were passed into the optimizer ``optim``.
            optim (torch.optim.Optimizer): Optimizer for ``model`` \'s
                parameters.
            group (dist.ProcessGroup): Model\'s process group across which parameters
                are sharded or ``None`` if using the default process group. (
                Default: ``None``)

        Returns:
            Dict[str, Any]: A :class:`dict` containing the optimizer state for
            ``model``. The sharding of the optimizer state is based on
            ``state_dict_type``.
        '''
    @staticmethod
    def optim_state_dict_post_hook(model: torch.nn.Module, optim: torch.optim.Optimizer, optim_state_dict: Dict[str, Any], group: dist.ProcessGroup | None = None) -> Dict[str, Any]:
        """
        This hook is intended be used by ``torch.distributed.NamedOptimizer``.
        The functionaility is identical to ``:meth:optim_state_dict`` except
        for the different arguments.

        Args:
            model (torch.nn.Module): Root module (which may or may not be a
                :class:`FullyShardedDataParallel` instance) whose parameters
                were passed into the optimizer ``optim``.
            optim (torch.optim.Optimizer): Optimizer for ``model`` 's
                parameters.
            optim (Dict[str, Any]: the optim_state_dict to be coverted. The value
               is typically returned by ``NamedOptimizer.state_dict()``.
            group (dist.ProcessGroup): Model's process group across which parameters
                are sharded or ``None`` if using the default process group. (
                Default: ``None``)

        Returns:
            Dict[str, Any]: A :class:`dict` containing the optimizer state for
            ``model``. The sharding of the optimizer state is based on
            ``state_dict_type``.
        """
    @staticmethod
    def optim_state_dict_to_load(optim_state_dict: Dict[str, Any], model: torch.nn.Module, optim: torch.optim.Optimizer, is_named_optimizer: bool = False, group: dist.ProcessGroup | None = None) -> Dict[str, Any]:
        '''
        Given a saved ``optim_state_dict``, converts it to the optimizer state_dict
        that can be loaded to ``optim`` which is the optimizer for ``model``.
        ``model`` is (partially) sharded by FullyShardedDataParallel.

            >>> # xdoctest: +SKIP("undefined variables")
            >>> from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
            >>> from torch.distributed.fsdp import StateDictType
            >>> from torch.distributed.fsdp import FullStateDictConfig
            >>> from torch.distributed.fsdp import FullOptimStateDictConfig
            >>> # Save a checkpoint
            >>> model, optim = ...
            >>> FSDP.set_state_dict_type(
            >>>     model,
            >>>     StateDictType.FULL_STATE_DICT,
            >>>     FullStateDictConfig(rank0_only=False),
            >>>     FullOptimStateDictConfig(rank0_only=False),
            >>> )
            >>> state_dict = model.state_dict()
            >>> optim_state_dict = FSDP.optim_state_dict(model, optim)
            >>> save_a_checkpoint(state_dict, optim_state_dict)
            >>> # Load a checkpoint
            >>> model, optim = ...
            >>> state_dict, optim_state_dict = load_a_checkponit()
            >>> FSDP.set_state_dict_type(
            >>>     model,
            >>>     StateDictType.FULL_STATE_DICT,
            >>>     FullStateDictConfig(rank0_only=False),
            >>>     FullOptimStateDictConfig(rank0_only=False),
            >>> )
            >>> model.load_state_dict(state_dict)
            >>> optim_state_dict = FSDP.optim_state_dict_to_load(
            >>>     optim_state_dict, model, optim
            >>> )
            >>> optim.load_state_dict(optim_state_dict)

        Args:
            optim_state_dict (Dict[str, Any]): The optimizer states to be loaded.
            model (torch.nn.Module): Root module (which may or may not be a
                :class:`FullyShardedDataParallel` instance) whose parameters
                were passed into the optimizer ``optim``.
            optim (torch.optim.Optimizer): Optimizer for ``model`` \'s
                parameters.
            is_named_optimizer (bool): Is this optimizer a NamedOptimizer or
                KeyedOptimizer. Only set to True if ``optim`` is TorchRec\'s
                KeyedOptimizer or torch.distributed\'s NamedOptimizer.
            group (dist.ProcessGroup): Model\'s process group across which parameters
                are sharded or ``None`` if using the default process group. (
                Default: ``None``)
        '''
    @staticmethod
    def load_optim_state_dict_pre_hook(model: torch.nn.Module, optim: torch.optim.Optimizer, optim_state_dict: Dict[str, Any], group: dist.ProcessGroup | None = None) -> Dict[str, Any]:
        """
        This hook is intended be used by ``torch.distributed.NamedOptimizer``.
        The functionaility is identical to ``:meth:optim_state_dict_to_load``
        except for the different arguments.

        Args:
            model (torch.nn.Module): Root module (which may or may not be a
                :class:`FullyShardedDataParallel` instance) whose parameters
                were passed into the optimizer ``optim``.
            optim (torch.optim.Optimizer): Optimizer for ``model`` 's
                parameters.
            optim_state_dict (Dict[str, Any]): The optimizer states to be loaded.
            group (dist.ProcessGroup): Model's process group across which parameters
                are sharded or ``None`` if using the default process group. (
                Default: ``None``)
        """
    def register_comm_hook(self, state: object, hook: callable):
        """
        Registers a communication hook which is an enhancement that provides a
        flexible hook to users where they can specify how FSDP aggregates gradients
        across multiple workers.
        This hook can be used to implement several algorithms like
        `GossipGrad <https://arxiv.org/abs/1803.05880>`_ and gradient compression
        which involve different communication strategies for
        parameter syncs while training with :class:`FullyShardedDataParallel`.

        .. warning ::
            FSDP communication hook should be registered before running an initial forward pass
            and only once.

        Args:
            state (object): Passed to the hook to maintain any state information during the training process.
                            Examples include error feedback in gradient compression,
                            peers to communicate with next in `GossipGrad <https://arxiv.org/abs/1803.05880>`_, etc.
                            It is locally stored by each worker
                            and shared by all the gradient tensors on the worker.
            hook (Callable): Callable, which has one of the following signatures:
                            1) ``hook: Callable[torch.Tensor] -> None``:
                            This function takes in a Python tensor, which represents
                            the full, flattened, unsharded gradient with respect to all variables
                            corresponding to the model this FSDP unit is wrapping
                            (that are not wrapped by other FSDP sub-units).
                            It then performs all necessary processing and returns ``None``;
                            2) ``hook: Callable[torch.Tensor, torch.Tensor] -> None``:
                            This function takes in two Python tensors, the first one represents
                            the full, flattened, unsharded gradient with respect to all variables
                            corresponding to the model this FSDP unit is wrapping
                            (that are not wrapped by other FSDP sub-units). The latter
                            represents a pre-sized tensor to store a chunk of a sharded gradient after
                            reduction.
                            In both cases, callable performs all necessary processing and returns ``None``.
                            Callables with signature 1 are expected to handle gradient communication for a `NO_SHARD` case.
                            Callables with signature 2 are expected to handle gradient communication for sharded cases.

        """
