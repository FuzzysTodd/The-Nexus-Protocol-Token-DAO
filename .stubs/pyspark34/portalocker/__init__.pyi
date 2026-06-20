from . import constants, exceptions, portalocker, utils
from .redis import RedisLock as RedisLock

__all__ = ['lock', 'unlock', 'LOCK_EX', 'LOCK_SH', 'LOCK_NB', 'LOCK_UN', 'LockFlags', 'LockException', 'Lock', 'RLock', 'AlreadyLocked', 'BoundedSemaphore', 'open_atomic', 'RedisLock']

AlreadyLocked = exceptions.AlreadyLocked
LockException = exceptions.LockException
lock = portalocker.lock
unlock = portalocker.unlock
LOCK_EX: constants.LockFlags
LOCK_SH: constants.LockFlags
LOCK_NB: constants.LockFlags
LOCK_UN: constants.LockFlags
LockFlags = constants.LockFlags
Lock = utils.Lock
RLock = utils.RLock
BoundedSemaphore = utils.BoundedSemaphore
TemporaryFileLock = utils.TemporaryFileLock
open_atomic = utils.open_atomic
