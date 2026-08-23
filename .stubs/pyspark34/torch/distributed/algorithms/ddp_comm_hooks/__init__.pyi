from _typeshed import Incomplete
from enum import Enum

__all__ = ['DDPCommHookType', 'register_ddp_comm_hook']

class DDPCommHookType(Enum):
    """
    DDPCommHookType enumerates the hooks of ``torch.distributed.algorithms.ddp_comm_hooks``
    as names and ``ddp_comm_hook_wrapper`` partials with hook specified. As an example,
    you can register allreduce hook by
    ``DDPCommHookType.ALLREDUCE.value(model=model, state=process_group)``.
    """
    ALLREDUCE: Incomplete
    FP16_COMPRESS: Incomplete
    BF16_COMPRESS: Incomplete
    QUANTIZE_PER_TENSOR: Incomplete
    QUANTIZE_PER_CHANNEL: Incomplete
    POWER_SGD: Incomplete
    POWER_SGD_RANK2: Incomplete
    BATCHED_POWER_SGD: Incomplete
    BATCHED_POWER_SGD_RANK2: Incomplete
    NOOP: Incomplete

def register_ddp_comm_hook(comm_hook_type: DDPCommHookType, model, state: Incomplete | None = None):
    """
    Registers the hooks of ``torch.distributed.algorithms.ddp_comm_hooks``
    to the DDP model. User can specify the type of hook as an enum
    ``DDPCommHookType`` type using ``comm_hook_type`` input. State input will
    be passed to the model.
    Uses Python comm hook implementations.

    Example::
        >>> # xdoctest: +SKIP
        >>> register_ddp_comm_hook(DDPCommHookType.FP16_COMPRESS, model, state)
    """
