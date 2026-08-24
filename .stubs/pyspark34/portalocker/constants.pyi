import enum
from _typeshed import Incomplete

LOCK_EX: int
LOCK_SH: int
LOCK_NB: int
LOCK_UN: Incomplete

class LockFlags(enum.IntFlag):
    EXCLUSIVE = LOCK_EX
    SHARED = LOCK_SH
    NON_BLOCKING = LOCK_NB
    UNBLOCK = LOCK_UN
