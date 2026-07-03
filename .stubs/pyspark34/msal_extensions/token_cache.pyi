import msal
from .cache_lock import CrossPlatLock as CrossPlatLock
from .persistence import PersistenceNotFound as PersistenceNotFound
from _typeshed import Incomplete

logger: Incomplete

class PersistedTokenCache(msal.SerializableTokenCache):
    '''A token cache backed by a persistence layer, coordinated by a file lock,
    to sustain a certain level of multi-process concurrency for a desktop app.

    The scenario is that multiple instances of same desktop app
    (or even multiple different apps)
    create their own ``PersistedTokenCache`` instances,
    which are all backed by the same token cache file on disk
    (known as a persistence). The goal is to have Single Sign On (SSO).

    Each instance of ``PersistedTokenCache`` holds a snapshot of the token cache
    in memory.
    Each :func:`~find` call will
    automatically reload token cache from the persistence when necessary,
    so that it will have fresh data.
    Each :func:`~modify` call will
    automatically reload token cache from the persistence when necessary,
    so that new writes will be appended on top of latest token cache data,
    and then the new data will be immediately flushed back to the persistence.

    Note: :func:`~deserialize` and :func:`~serialize` remain the same
    as their counterparts in the parent class ``msal.SerializableTokenCache``.
    In other words, they do not have the "reload from persistence if necessary"
    nor the "flush back to persistence" behavior.
    '''
    is_encrypted: Incomplete
    def __init__(self, persistence, lock_location: Incomplete | None = None) -> None: ...
    def modify(self, credential_type, old_entry, new_key_value_pairs: Incomplete | None = None) -> None: ...
    def find(self, credential_type, **kwargs): ...
