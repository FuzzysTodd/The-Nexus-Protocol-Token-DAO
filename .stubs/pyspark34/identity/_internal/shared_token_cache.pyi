import abc
from .. import CredentialUnavailableError as CredentialUnavailableError
from .._constants import KnownAuthorities as KnownAuthorities
from .._internal import AadClientBase as AadClientBase, get_default_authority as get_default_authority, normalize_authority as normalize_authority, wrap_exceptions as wrap_exceptions
from .._persistent_cache import TokenCachePersistenceOptions as TokenCachePersistenceOptions
from _typeshed import Incomplete
from typing import Any, Mapping

ABC = abc.ABC
CacheItem = Mapping[str, str]
MULTIPLE_ACCOUNTS: str
MULTIPLE_MATCHING_ACCOUNTS: str
NO_ACCOUNTS: str
NO_MATCHING_ACCOUNTS: str
NO_TOKEN: str
KNOWN_ALIASES: Incomplete

class SharedTokenCacheBase(ABC, metaclass=abc.ABCMeta):
    def __init__(self, username: str | None = None, *, authority: str | None = None, tenant_id: str | None = None, **kwargs: Any) -> None: ...
    @staticmethod
    def supported() -> bool:
        """Whether the shared token cache is supported on the current platform.

        :return: True if the shared token cache is supported on the current platform.
        :rtype: bool
        """
