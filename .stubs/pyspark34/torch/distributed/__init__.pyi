from .distributed_c10d import *
from .rendezvous import register_rendezvous_handler as register_rendezvous_handler, rendezvous as rendezvous
from _typeshed import Incomplete
from enum import Enum as Enum
from torch._C._distributed_c10d import BuiltinCommHookType as BuiltinCommHookType, DebugLevel as DebugLevel, FileStore as FileStore, GradBucket as GradBucket, HashStore as HashStore, Logger as Logger, PrefixStore as PrefixStore, ProcessGroup as ProcessGroup, Reducer as Reducer, Store as Store, TCPStore as TCPStore, get_debug_level as get_debug_level, set_debug_level as set_debug_level, set_debug_level_from_env as set_debug_level_from_env

def is_available() -> bool:
    """
    Returns ``True`` if the distributed package is available. Otherwise,
    ``torch.distributed`` does not expose any other APIs. Currently,
    ``torch.distributed`` is available on Linux, MacOS and Windows. Set
    ``USE_DISTRIBUTED=1`` to enable it when building PyTorch from source.
    Currently, the default value is ``USE_DISTRIBUTED=1`` for Linux and Windows,
    ``USE_DISTRIBUTED=0`` for MacOS.
    """

DistBackendError: Incomplete

class _ProcessGroupStub: ...
