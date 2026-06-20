from ._constants import CACHE_CAE_SUFFIX as CACHE_CAE_SUFFIX, CACHE_NON_CAE_SUFFIX as CACHE_NON_CAE_SUFFIX
from _typeshed import Incomplete
from typing import Any

class TokenCachePersistenceOptions:
    """Options for persistent token caching.

    Most credentials accept an instance of this class to configure persistent token caching. The default values
    configure a credential to use a cache shared with Microsoft developer tools and
    :class:`~azure.identity.SharedTokenCacheCredential`. To isolate a credential's data from other applications,
    specify a `name` for the cache.

    By default, the cache is encrypted with the current platform's user data protection API, and will raise an error
    when this is not available. To configure the cache to fall back to an unencrypted file instead of raising an
    error, specify `allow_unencrypted_storage=True`.

    .. warning:: The cache contains authentication secrets. If the cache is not encrypted, protecting it is the
       application's responsibility. A breach of its contents will fully compromise accounts.

    .. admonition:: Example:

        .. literalinclude:: ../tests/test_persistent_cache.py
            :start-after: [START snippet]
            :end-before: [END snippet]
            :language: python
            :caption: Configuring a credential for persistent caching
            :dedent: 8

    :keyword str name: prefix name of the cache, used to isolate its data from other applications. Defaults to the
        name of the cache shared by Microsoft dev tools and :class:`~azure.identity.SharedTokenCacheCredential`.
        Additional strings may be appended to the name for further isolation.
    :keyword bool allow_unencrypted_storage: whether the cache should fall back to storing its data in plain text when
        encryption isn't possible. False by default. Setting this to True does not disable encryption. The cache will
        always try to encrypt its data.
    """
    allow_unencrypted_storage: Incomplete
    name: Incomplete
    def __init__(self, *, allow_unencrypted_storage: bool = False, name: str = 'msal.cache', **kwargs: Any) -> None: ...
