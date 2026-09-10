import torch.distributed as dist
import torch.nn as nn
from _typeshed import Incomplete
from enum import Enum
from torch.distributed.fsdp._common_utils import _FSDPState
from torch.distributed.fsdp.flat_param import FlatParamHandle as FlatParamHandle
from typing import List

class _ExecOrderWarnStatus(Enum):
    """Used internally for execution order validation."""
    NONE: Incomplete
    WARNING: Incomplete
    WARNED: Incomplete

class _ExecOrderData:
    """
    This contains the data structures to track the execution order. We track
    the pre-forward order on the *first* iteration for forward prefetching
    (which thus assumes static graph) and the post-forward order on *every*
    iteration for backward prefetching (which thus does not assume static
    graph but may be provide an incorrect order).
    """
    handles_pre_forward_order: Incomplete
    handles_to_pre_forward_order_index: Incomplete
    handles_post_forward_order: Incomplete
    handles_to_post_forward_order_index: Incomplete
    process_group: Incomplete
    world_size: Incomplete
    all_handles: Incomplete
    handle_to_handle_index: Incomplete
    param_to_fqn: Incomplete
    current_order_index: int
    warn_status: Incomplete
    def __init__(self, debug_level: dist.DebugLevel, backward_prefetch_limit: int, forward_prefetch_limit: int) -> None: ...
    rank: Incomplete
    def init(self, state: _FSDPState, root_module: nn.Module, process_group: dist.ProcessGroup) -> None:
        """
        Initializes the data structures needed for checking the forward order.
        This should be called after a root FSDP instance has been set during
        lazy initialization.
        """
    @property
    def is_first_iter(self) -> bool: ...
    def get_handles_to_backward_prefetch(self, current_handles_key: _HandlesKey) -> List[_HandlesKey] | None:
        """
        Returns a :class:`list` of the handles keys of the handles to backward
        prefetch given the current handles key. If there are no valid handles
        keys to prefetch, then this returns an empty :class:`list`.
        """
    def get_handles_to_forward_prefetch(self, current_handles_key: _HandlesKey) -> List[_HandlesKey] | None:
        """
        Returns a :class:`list` of the handles keys of the handles to forward
        prefetch given the current handles key. If there are no valid handles
        keys to prefetch, then this returns an empty :class:`list`.
        """
    def record_post_forward(self, handles: List[FlatParamHandle]) -> None:
        """
        Records ``handles`` in the post-forward order, where ``handles`` should
        be a group of handles used in the same module's forward. If ``handles``
        is empty, then it is omitted.

        Unlike :meth:`record_pre_forward`, this records the order *every*
        iteration with the expectation that the recorded order is reset in
        :meth:`next_iter`.
        """
    def record_pre_forward(self, handles: List[FlatParamHandle], is_training: bool) -> None:
        """
        Records ``handles`` in the pre-forward order, where ``handles`` should
        be a group of handles used in the same module's forward. If ``handles``
        is empty, then it is omitted.

        On the first iteration, this checks the execution order across ranks.
        See :meth:`_check_order` for details.
        """
    def next_iter(self) -> None:
        """
        Advances the internal data structures per iteration. This should be
        called in the post-backward callback since that marks the true end of
        an iteration.
        """
