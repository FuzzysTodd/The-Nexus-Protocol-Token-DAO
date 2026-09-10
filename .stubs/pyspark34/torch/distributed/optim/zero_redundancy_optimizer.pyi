import enum
import torch
from _typeshed import Incomplete
from torch.distributed.algorithms.join import JoinHook, Joinable
from torch.optim import Optimizer
from typing import Any, Callable, Dict, List, Type

__all__ = ['ZeroRedundancyOptimizer']

class _ZeROJoinHook(JoinHook):
    zero: Incomplete
    def __init__(self, zero) -> None: ...
    def main_hook(self) -> None:
        """
        Performs an optimizer step, which updates the joined process's shard of
        the parameters and broadcasts those parameters.
        """

class _DDPBucketAssignment:
    """
    This represents a :class:`DistributedDataParallel` bucket assignment,
    meaning a (possibly non-strict) subset of the parameters corresponding to
    a DDP bucket assigned to a rank to update.

    Attributes:
        bucket_index (int): index of the bucket determined by the DDP gradient
            bucket all-reduce order.
        parameters (List[torch.Tensor]): model parameters in the bucket
            assigned to this rank.
        offset (int): offset into the :class:`GradBucket` 's :meth:`parameters`
            giving the index of the first element in the passed-in
            ``parameters``; this equivalently indexes into the
            :class:`GradBucket` 's :meth:`gradients`.
        device (torch.device): device on which the parameters are stored.
        tensor (torch.Tensor): flattened tensor giving the data of the
            parameter subset assigned to the rank.
    """
    bucket_index: Incomplete
    parameters: Incomplete
    offset: Incomplete
    device: Incomplete
    tensor: Incomplete
    def __init__(self, bucket_index: int, parameters: List[torch.Tensor], offset: int) -> None: ...

class _OverlapStatus(enum.IntEnum):
    """
    This defines the three possible statuses that
    :class:`ZeroRedundancyOptimizer` can be in when overlapping with
    :class:`DistributedDataParallel`.

        ``UNINITIALIZED``: The ZeRO instance is effectively uninitialized and
            is waiting for DDP to finalize its bucketing.
        ``DDP_HAS_REBUILT_BUCKETS``: DDP has rebuilt its buckets, meaning that
            its bucketing is finalized. The ZeRO instance can now collect the
            necessary information about the DDP bucketing.
        ``INITIALIZED``: The ZeRO instance is fully initialized and can now
            optimize parameters.
    """
    UNINITIALIZED: int
    DDP_HAS_REBUILT_BUCKETS: int
    INITIALIZED: int

class _OverlapInfo:
    """
    This contains the information needed by :class:`ZeroRedundancyOptimizer`
    to overlap with :class:`DistributedDataParallel`.

    Arguments:
        world_size (int): world size of the process group being used.

    Attributes:
        shard_buckets (bool): if ``True``, then the assignment of each
            :class:`DistributedDataParallel` bucket is partitioned across
            possibly multiple :class:`ZeroRedundancyOptimizer` instances (i.e.
            across possibly multiple ranks) to approximate uniformity following
            a threshold given by the total parameter size divided by the world
            size; if ``False``, then each bucket is wholly assigned to a single
            :class:`ZeroRedundancyOptimizer` instance (i.e. to a single rank);
            this should be set to the value passed into the hook constructor.
        status (_OverlapStatus): current status; see :class:`_OverlapStatus`
            for more information.
        params_per_bucket (List[List[torch.Tensor]]): ``params_per_bucket[i]``
            gives the model parameters in the ``i``th bucket.
        params_per_rank (List[List[torch.Tensor]]): ``params_per_rank[i]``
            gives the model parameters assigned to the ``i``th rank, where the
            parameters are grouped by increasing bucket indices.
        offsets (Dict[int, int]): maps from bucket index to the offset in
            ``self.params_per_rank[rank]`` giving the index of the first
            parameter in that bucket, where ``rank`` is this process's own
            rank; the keys of this :class:`dict` are the bucket indices
            assigned to this rank.
        num_bucket_assignments (int): total number of bucket assignments across
            all ranks; this is equal to the number of
            :class:`DistributedDataParallel` gradient buckets if
            ``shard_buckets=False`` and possibly greater otherwise.
        total_size (int, optional): total size of all buckets (i.e. sum of
            ``param.numel()`` for all ``param`` across all buckets) if
            ``shard_buckets=True``; otherwise, ``None``.
        broadcast_handles (List[Work]): :class:`list` of async work handles for
            the parameter broadcasts.
        bucket_index_to_future (Dict[int, torch.futures.Future]):
            :class:`dict` mapping bucket index to the corresponding all-reduce
            future.
        bucket_index_to_bucket (Dict[int, dist.GradBucket]): :class:`dict`
            mapping bucket index to the corresponding bucket.
        bucket_indices_seen (List[int]): :class:`list` of the bucket indices
            seen on this iteration.
    """
    status: Incomplete
    shard_buckets: bool
    params_per_bucket: Incomplete
    params_per_rank: Incomplete
    offsets: Incomplete
    assigned_ranks_per_bucket: Incomplete
    num_bucket_assignments: int
    total_size: Incomplete
    broadcast_handles: Incomplete
    bucket_indices_seen: Incomplete
    bucket_index_to_future: Incomplete
    bucket_index_to_bucket: Incomplete
    def __init__(self, world_size) -> None: ...
    def wait_for_broadcasts(self) -> None:
        """
        Waits for all parameter broadcasts. This should be called once all
        broadcasts have been scheduled, meaning ``self.broadcast_handles`` is
        filled. This clears ``self.broadcast_handles`` in preparation for the
        next iteration.
        """
    def clear_per_iter_info(self) -> None:
        """
        Clears the data structures that are modified per-iteration. This should
        be called at the end of an iteration.
        """

class ZeroRedundancyOptimizer(Optimizer, Joinable):
    """
    This class wraps an arbitrary :class:`optim.Optimizer
    <torch.optim.Optimizer>` and shards its states across ranks in the group as
    described by ZeRO_. The local optimizer instance in each rank is only
    responsible for updating approximately ``1 / world_size`` parameters and
    hence only needs to keep ``1 / world_size`` optimizer states. After
    parameters are updated locally, each rank will broadcast its parameters to
    all other peers to keep all model replicas in the same state.
    ``ZeroRedundancyOptimizer`` can be used in conjunction with
    :class:`torch.nn.parallel.DistributedDataParallel` to reduce per-rank peak
    memory consumption.

    ``ZeroRedundancyOptimizer`` uses a sorted-greedy algorithm to pack a number
    of parameters at each rank. Each parameter belongs to a single rank and is
    not divided among ranks. The partition is arbitrary and might not match the
    the parameter registration or usage order.

    Arguments:
        params (``Iterable``): an ``Iterable`` of :class:`torch.Tensor` s
            or :class:`dict` s giving all parameters, which will be sharded
            across ranks.

    Keyword Args:
        optimizer_class (:class:`torch.nn.Optimizer`): the class of the local
            optimizer.
        process_group (``ProcessGroup``, optional): ``torch.distributed``
            ``ProcessGroup`` (default: ``dist.group.WORLD`` initialized by
            :meth:`torch.distributed.init_process_group`).
        parameters_as_bucket_view (bool, optional): if ``True``, parameters are
            packed into buckets to speed up communication, and ``param.data``
            fields point to bucket views at different offsets; if ``False``,
            each individual parameter is communicated separately, and each
            ``params.data`` stays intact (default: ``False``).
        overlap_with_ddp (bool, optional): if ``True``, :meth:`step` is
            overlapped with :class:`DistributedDataParallel` 's gradient
            synchronization; this requires (1) either a functional optimizer
            for the ``optimizer_class`` argument or one with a functional
            equivalent and (2) registering a DDP communication hook
            constructed from one of the functions in ``ddp_zero_hook.py``;
            parameters are packed into buckets matching those in
            :class:`DistributedDataParallel`, meaning that the
            ``parameters_as_bucket_view`` argument is ignored.
            If ``False``, :meth:`step` runs disjointly after the backward pass
            (per normal).
            (default: ``False``)
        **defaults: any trailing arguments, which are forwarded to the local
            optimizer.

    Example::

        >>> # xdoctest: +SKIP
        >>> import torch.nn as nn
        >>> from torch.distributed.optim import ZeroRedundancyOptimizer
        >>> from torch.nn.parallel import DistributedDataParallel as DDP
        >>> model = nn.Sequential(*[nn.Linear(2000, 2000).to(rank) for _ in range(20)])
        >>> ddp = DDP(model, device_ids=[rank])
        >>> opt = ZeroRedundancyOptimizer(
        >>>     ddp.parameters(),
        >>>     optimizer_class=torch.optim.Adam,
        >>>     lr=0.01
        >>> )
        >>> ddp(inputs).sum().backward()
        >>> opt.step()

    .. warning::
        Currently, ``ZeroRedundancyOptimizer`` requires that all of the
        passed-in parameters are the same dense type.

    .. warning::
        If you pass ``overlap_with_ddp=True``, be wary of the following: Given
        the way that overlapping :class:`DistributedDataParallel` with
        :class:`ZeroRedundancyOptimizer` is currently implemented, the first
        two or three training iterations do not perform parameter updates in
        the optimizer step, depending on if ``static_graph=False`` or
        ``static_graph=True``, respectively. This is because it needs
        information about the gradient bucketing strategy used by
        :class:`DistributedDataParallel`, which is not finalized until the
        second forward pass if ``static_graph=False`` or until the third
        forward pass if ``static_graph=True``. To adjust for this, one option
        is to prepend dummy inputs.

    .. warning:: ZeroRedundancyOptimizer is experimental and subject to change.

    .. _ZeRO: https://arxiv.org/abs/1910.02054

    """
    initialized: bool
    process_group: Incomplete
    world_size: Incomplete
    rank: Incomplete
    global_rank: Incomplete
    parameters_as_bucket_view: Incomplete
    def __init__(self, params, optimizer_class: Type[Optimizer], process_group: Any | None = None, parameters_as_bucket_view: bool = False, overlap_with_ddp: bool = False, **defaults: Any) -> None: ...
    def add_param_group(self, param_group: dict) -> None:
        """
        Add a parameter group to the :class:`Optimizer` 's ``param_groups``.

        This can be useful when fine tuning a pre-trained network, as frozen
        layers can be made trainable and added to the :class:`Optimizer` as
        training progresses.

        Arguments:
            param_group (dict): specifies the parameters to be optimized and
                group-specific optimization options.

        .. warning:: This method handles updating the shards on all partitions
            but needs to be called on all ranks. Calling this on a subset of
            the ranks will cause the training to hang because communication
            primitives are called depending on the managed parameters and
            expect all the ranks to participate on the same set of parameters.
        """
    def consolidate_state_dict(self, to: int = 0) -> None:
        """
        Consolidate a list of ``state_dict`` s (one per rank) on the target
        rank.

        Arguments:
            to (int): the rank that receives the optimizer states (default: 0).

        Raises:
            RuntimeError: if ``overlap_with_ddp=True`` and this method is
                called before this :class:`ZeroRedundancyOptimizer` instance
                has been fully initialized, which happens once
                :class:`DistributedDataParallel` gradient buckets have been
                rebuilt.

        .. warning:: This needs to be called on all ranks.
        """
    def step(self, closure: Callable[[], float] | None = None, **kwargs: Any) -> float | None:
        """
        Performs a single optimizer step and syncs parameters across all ranks.

        Arguments:
            closure (Callable): a closure that re-evaluates the model and
                returns the loss; optional for most optimizers.
        Returns:
            Optional loss depending on the underlying local optimizer.

        .. note: Any extra parameters are passed to the base optimizer as-is.
        """
    def join_hook(self, **kwargs):
        """
        Returns the ZeRO join hook, which enables training on uneven inputs by
        shadowing the collective communications in the optimizer step.

        Gradients must be properly set before this hook is called.

        Arguments:
            kwargs (dict): a :class:`dict` containing any keyword arguments
                to modify the behavior of the join hook at run time; all
                :class:`Joinable` instances sharing the same join context
                manager are forwarded the same value for ``kwargs``.

        This hook does not support any keyword arguments; i.e. ``kwargs`` is
        unused.
        """
    @property
    def join_device(self) -> torch.device: ...
    @property
    def join_process_group(self) -> Any: ...
    def load_state_dict(self, state_dict: Dict[str, Any]) -> None:
        """
        Load the state pertaining to the given rank from the input
        ``state_dict``, updating the local optimizer as needed.

        Arguments:
            state_dict (dict): optimizer state; should be an object returned
                from a call to :meth:`state_dict`.

        Raises:
            RuntimeError: if ``overlap_with_ddp=True`` and this method is
                called before this :class:`ZeroRedundancyOptimizer` instance
                has been fully initialized, which happens once
                :class:`DistributedDataParallel` gradient buckets have been
                rebuilt.
        """
    def state_dict(self) -> Dict[str, Any]:
        """
        Returns the last global optimizer state known to this rank.

        .. warning:
            If the state has not been consolidated to this rank, this raises a
            runtime error, and even if it has, the state may not be up-to-date,
            depending on when :meth:`consolidate_state_dict` was last called.

        Raises:
            RuntimeError: if ``overlap_with_ddp=True`` and this method is
                called before this :class:`ZeroRedundancyOptimizer` instance
                has been fully initialized, which happens once
                :class:`DistributedDataParallel` gradient buckets have been
                rebuilt; or if this method is called without a preceding call
                to :meth:`consolidate_state_dict`.
        """
