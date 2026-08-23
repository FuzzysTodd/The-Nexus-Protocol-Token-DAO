import torch
import torch.distributed as dist
import torch.nn as nn
from _typeshed import Incomplete
from collections.abc import Generator
from enum import Enum
from torch import Tensor
from typing import Iterator, NamedTuple, Sequence, Tuple

__all__ = ['FlatParameter', 'FlatParamHandle', 'FlatParamShardMetadata', 'ParamInfo', 'SharedParamInfo', 'HandleShardingStrategy']

class ParamInfo(NamedTuple):
    """Information for an original module parameter."""
    param_name: str
    module: nn.Module
    module_name: str

class SharedParamInfo(NamedTuple):
    '''
    Additional information for a shared parameter.

    For each shared parameter, we designate one module and its parameter
    variable to be the primary owner, determined as the first one encountered
    in the parameter walk. These are prefixed with "prim". The primary module
    and parameter do not have their own :class:`SharedParamInfo` instance.
    '''
    param_name: str
    module: nn.Module
    module_name: str
    prim_param_name: str
    prim_module: nn.Module
    prim_module_name: str

class FlatParamShardMetadata(NamedTuple):
    """
    This holds metadata specific to this rank's shard of the flattened
    parameter.

    Attributes:
        param_names (Tuple[str, ...]): Prefixed parameter names of this rank's
            shard of the parameters; see :class:`FlatParameter`.
        param_shapes (Tuple[torch.Size, ...]): Parameter shapes of this rank's
            shard of the parameters; see :class:`FlatParameter`.
        param_numels (Tuple[int, ...]): Parameter numels of this rank's shard
            of the parameters; see :class:`FlatParameter`.
        param_offsets (Tuple[Tuple[int, int], ...]): [start, end] offsets (in
            units of numels) giving this rank's part of each flattened
            original module parameter.
    """
    param_names: Tuple[str, ...]
    param_shapes: Tuple[torch.Size, ...]
    param_numels: Tuple[int, ...]
    param_offsets: Tuple[Tuple[int, int], ...]

class HandleShardingStrategy(Enum):
    FULL_SHARD: Incomplete
    SHARD_GRAD_OP: Incomplete
    NO_SHARD: Incomplete
    HYBRID_SHARD: Incomplete

class FlatParameter(nn.Parameter):
    '''
    This is the flattened parameter used by :class:`FullyShardedDataParallel`.
    It is comprised of one or more original parameters, which are flattened
    and concatenated to construct the flattened parameter.

    Under the current design, this parameter logically represents both the
    unsharded and sharded flattened parameter, and its data changes storages
    dynamically.
        - In the :class:`FullyShardedDataParallel` constructor, the parameter
        is initialized as unsharded and then sharded in-place.
        - At runtime, the parameter is lazily (re)-initialized. The sharded
        parameter data is saved in ``self._local_shard``, and a new ``Tensor``
        ``self._full_param_padded`` is created, which is the all-gather
        destination and owns the unsharded parameter storage thereafter. (See
        :meth:`FlatParamHandle.init_flat_param_attributes`.)
        - Throughout runtime, the parameter data changes storages as needed,
        e.g. to the sharded flattened parameter, reduced-precision sharded
        flattened parameter, or the unsharded flattened parameter.

    Attributes:
        _unpadded_unsharded_size (torch.Size): Unsharded flattened parameter\'s
            size without padding.
        _padded_unsharded_size (torch.Size): Unsharded flattened parameter\'s
            size with padding. This is only set for sharded strategies since
            they require padding for the all-gather.
        _sharded_size (torch.Size): Sharded flattened parameter\'s size with
            padding. This is also set for ``NO_SHARD``, in which case it is the
            same as the unsharded sizes. (We omit "padded" because there is no
            analogous unpadded one.)

        _param_infos (Tuple[ParamInfo, ...]): Each parameter\'s parameter info
            entry; see :class:`ParamInfo`.
        _numels (Tuple[int, ...]): Each parameter\'s numel.
        _shapes (Tuple[torch.Size, ...]): Each parameter\'s shape.
        _fqns (Tuple[str, ...]): The original parameters\' FQNs prefixed from
            the owning handle\'s ``_fully_sharded_module``. The names are
            guaranteed to be unique within the subtree rooted at that module.
        _num_params (int): Number of original parameters flattened into this
            flattened parameter; this is the length of ``_param_infos``,
            ``_numels``, ``_shapes``, and ``_fqns``.
        _shared_param_infos (Tuple[SharedParamInfo, ...]): Shared parameter
            info entries; see :class:`SharedParamInfo`.
        _param_extensions (Tuple[Optional[Any], ...]): Parameter extensions
            (i.e. some per-parameter state) used to customize pre-flatten and
            post-unflatten behavior. This is experimental, and users should not
            depend on its existence in the future.
        _modules (Set[nn.Module]): Modules that contain some original parameter
            that is flattened into the ``FlatParameter``.

        _shard_param_offsets (List[Tuple[int, int])): [start, end] offsets (in
            units of numel) giving this rank\'s part of each flattened original
            module parameter; for any parameter ``p`` that is not sharded
            across ranks, this will be [0, ``p.numel()``-1].
        _shard_indices (Tuple[int, int]): [start, end] indices (in units of
            parameters) for this rank\'s shard of the original model parameters,
            where the parameters follow the order in which they were originally
            flattened; this indexes appropriately into any data structure that
            follows the flattening order (e.g. ``_param_infos``, ``_numels``,
            etc.).
        _shard_numel_padded (int): Numel padded for this rank\'s sharded
            flattened parameter.

        _local_shard (Tensor): Sharded flattened parameter with padding if
            using a sharded strategy. If using ``NO_SHARD``, then this is the
            unpadded unsharded flattened parameter, and there is no notion of a
            sharded flattened parameter or padded unsharded flattened
            parameter.
        _full_param_padded (Tensor): Unsharded flattened parameter with
            padding. This is not defined for ``NO_SHARD``. When using mixed
            precision for parameters, this has the low precision.
        _full_prec_full_param_padded (Tensor): Full precision unsharded
            flattened parameter with padding. This is used for unsharding
            outside of computation when using mixed precision for parameters.
            This is never defined for ``NO_SHARD``.
        _post_backward_hook_state (Tuple[AccumulateGrad, RemovableHandle]):
            Flattened parameter\'s :class:`AccumulateGrad` object and
            post-backward hook handle.
        _mp_shard (Tensor): Low precision sharded flattened parameter with
            padding. This is only defined when parameter mixed precision is
            enabled. For ``NO_SHARD``, this is used for computation.
        _cpu_grad (Tensor): Sharded gradient with padding stored on CPU.
            This is only defined when offloading parameters is enabled.
        _saved_grad_shard (Tensor): Sharded gradient with padding from previous
            iterations for gradient accumulation without :meth:`no_sync`.

        _params (Optional[List[nn.Parameter]]): The original parameter
            variables if ``use_orig_params=True`` and ``None`` otherwise.
        _shared_params (Optional[List[nn.Parameter]]): The original shared
            parameter variables if ``use_orig_params=True`` and ``None``
            otherwise.
        _tensors (Optional[List[Optional[Tensor]]]): This saves the ``Tensor``
            views created in the forward and tracked by autograd when
            ``use_orig_params=True`` and is ``None`` otherwise. This is to
            preserve those ``Tensor`` variables for the backward to ensure that
            the ``FlatParameter`` \'s ``AccumulateGrad`` object does not change
            in which case the post-backward hook does not run. This is relevant
            for cases like reentrant activation checkpointing.
        _is_grad_none (Optional[List[bool]]): A mask over the original
            parameters\' gradients indicating if it is logically ``None`` or not
            if ``use_orig_params=True`` and ``None`` otherwise. This is needed
            because only some of the parameters may have ``None`` gradient, in
            which case the ``FlatParameter`` gradient must be non-``None`` and
            must use zeros to approximate those original ``None`` gradients.
            This mask informs FSDP to set the original parameter gradients to
            ``None`` (instead of zeros) as needed.
    '''

class FlatParamHandle:
    """
    This handle manages a flattened parameter (:class:`FlatParameter`). This
    includes sharding and view management.

    Args:
        params (Sequence[nn.Parameter]): The parameters to use for the
            flattened parameter.
        fully_sharded_module (nn.Module): See [Note: Fully Sharded Module].
        device (torch.device): The compute and communication device, which
            should be a non-CPU device. We refer to it as the compute device.
        sharding_strategy (ShardingStrategy): Sharding strategy to apply to
            this handle's ``FlatParameter``.
        offload_params (bool): Whether to offload the handle's
            ``FlatParameter`` to CPU.
        mp_param_dtype (Optional[torch.dtype]): Parameter mixed precision
            setting passed to the FSDP constructor.
        mp_reduce_dtype (Optional[torch.dtype]): Gradient reduction mixed
            precision setting passed to the FSDP constructor.
        keep_low_precision_grads (bool): Whether to keep gradients in low
            precision.
        use_orig_params (bool): If ``True``, then FSDP preserves the original
            parameter variables and returns them from ``named_parameters()``
            (e.g. to support different optimizer hyperparameters within one
            :class:`FlatParameter`). If ``False``, then FSDP reconstructs the
            parameter every iteration and returns the :class:`FlatParameter` s
            from ``named_parameters()``.
    """
    device: Incomplete
    process_group: Incomplete
    rank: Incomplete
    world_size: Incomplete
    def __init__(self, params: Sequence[nn.Parameter], fully_sharded_module: nn.Module, device: torch.device, sharding_strategy: HandleShardingStrategy, offload_params: bool, mp_param_dtype: torch.dtype | None, mp_reduce_dtype: torch.dtype | None, keep_low_precision_grads: bool, process_group: dist.ProcessGroup, use_orig_params: bool) -> None: ...
    @staticmethod
    def flatten_params(params: Sequence[torch.Tensor], requires_grad: bool) -> FlatParameter:
        """
        Flattens the parameters in ``params`` into a single
        :class:`FlatParameter`. This should be the only way used to construct
        :class:`FlatParameter` s.

        We expose this factory method for checkpointing (e.g. sharded state
        dict). The flattened parameter's metadata should only be initialized
        once (see :meth:`_init_metadata`), but its tensor data may be reloaded.
        """
    def shard(self) -> None:
        """
        Shards the handle's ``FlatParameter``. In terms of memory, this
        allocates new memory for the sharded flattened parameter and frees the
        unsharded flattened parameter's storage.

        Postcondition: ``self.flat_param`` is the sharded flattened parameter.
        Shard metadata attributes are set for all sharding strategies.
        ``process_group``, ``rank``, and ``world_size`` attributes are set if
        using a sharded strategy.
        """
    def shard_metadata(self) -> FlatParamShardMetadata:
        """Returns shard-related metadata specific to this rank's shard of the
        flattened parameter."""
    def init_flat_param_attributes(self) -> None:
        """
        This initializes some attributes on the handle's ``FlatParameter``.
        This should be called during lazy initialization since it requires the
        parameter to be on the compute device if not offloading to CPU and we
        want to give users the chance to move the parameter appropriately after
        the FSDP constructor.

        For each tensor attribute on the ``FlatParameter``, see the unshard and
        reshard methods in this class for the allocation and free pattern.
        """
    def pre_unshard(self) -> bool:
        """
        Returns: ``False`` if this is a no-op and ``True`` otherwise.

        Postcondition: ``self.flat_param`` 's data is on the device for
        communication and is what should be all-gathered. This means that it
        matches the dtype of the expected unsharded parameter.
        """
    def unshard(self) -> None:
        """
        Runs the unshard logic. This includes all-gathering the flattened
        parameter and switching to using the unsharded flattened parameter. If
        the handle does not need unsharding, then this only switches to using
        the unsharded flattened parameter. For ``NO_SHARD``, this is a no-op.

        If FSDP is in :meth:`summon_full_params` and the handle uses parameter
        mixed precision, then the parameter is forced to full precision.
        """
    def needs_unshard(self) -> bool:
        """Returns if the handle's flattened parameter needs to be unsharded."""
    def post_unshard(self) -> None:
        """
        Runs the post-unshard logic. This includes freeing the low precision
        shard if needed.
        """
    def unshard_grad(self) -> None:
        """
        Unshards the handle's ``FlatParameter`` 's gradient. If all ranks have
        ``None`` gradient, then all original parameters will as well. This
        method performs an all-reduce and an all-gather. The additional
        all-reduce is tolerable since this method is not meant to be used on
        the computation critical path.

        Postcondition: ``_saved_grad_shard`` is defined and contains the value
        to set ``flat_param.grad`` after gradients are resharded.
        """
    def reshard_grad(self) -> None: ...
    def prepare_gradient_for_backward(self) -> None:
        """
        Prepares the gradient for the backward computation by saving and
        clearing any existing sharded gradient in ``.grad`` to enable computing
        a new unsharded gradient.
        """
    def prepare_gradient_for_optim(self) -> None:
        """
        Prepares the gradient for optimizer computation by moving the sharded
        gradient to the ``.grad`` attribute.
        """
    def to_cpu(self) -> Generator[None, None, None]:
        """
        Moves the unpadded unsharded flattened parameter to CPU while in the
        context and moves it back to the previous device upon exit. For now,
        this assumes the ``FlatParameter`` is the unpadded unsharded flattened
        parameter since (1) there is no reason to include the padding in the
        copy and (2) there is no use case for the sharded flattened parameter.

        Precondition: ``self.flat_param`` 's data is the unpadded unsharded
        flattened parameter on the compute device, and the handle uses a
        sharded strategy.
        Postcondition: Same as the precondition.
        """
    def reshard(self, free_unsharded_flat_param: bool):
        """
        Runs the reshard logic. This includes freeing the unsharded flattened
        parameter if ``free_unsharded_flat_param`` and switching to using the
        sharded flattened parameter.
        """
    def post_reshard(self) -> None:
        """
        Runs the post-reshard logic. This includes freeing any memory that
        can now be freed given that the ``FlatParameter`` points to the full
        precision sharded flattened parameter.

        Precondition: ``self.flat_param`` 's data points to the full precision
        sharded flattened parameter.
        """
    def unflatten_as_params(self) -> Generator:
        """
        Assumes the flattened parameter is unsharded. When in the context,
        unflattens the original parameters as ``nn.Parameter`` views into the
        flattened parameter, and after the context, restores the original
        parameters as ``Tensor`` views into the flattened parameter.
        """
    def flat_param_to(self, *args, **kwargs) -> None:
        """Wraps an in-place call to ``.to()`` for ``self.flat_param``."""
    def is_sharded(self, tensor: Tensor) -> bool:
        """
        Returns if ``tensor`` is *currently* sharded. For ``NO_SHARD``, we
        choose to have this always return ``False`` for clarity.
        """
    def parameter_module_names(self) -> Iterator[Tuple[str, str]]: ...
    def shared_parameter_module_names(self) -> Iterator[Tuple[str, str]]: ...
    @property
    def sharded_grad(self) -> Tensor | None:
        """Returns the handle's sharded gradient."""
    @property
    def uses_sharded_strategy(self) -> bool: ...
