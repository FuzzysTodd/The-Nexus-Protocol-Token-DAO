from .authority import canonicalize as canonicalize
from .oauth2cli.oidc import decode_id_token as decode_id_token, decode_part as decode_part
from _typeshed import Incomplete

logger: Incomplete

def is_subdict_of(small, big): ...

class TokenCache:
    """This is considered as a base class containing minimal cache behavior.

    Although it maintains tokens using unified schema across all MSAL libraries,
    this class does not serialize/persist them.
    See subclass :class:`SerializableTokenCache` for details on serialization.
    """
    class CredentialType:
        ACCESS_TOKEN: str
        REFRESH_TOKEN: str
        ACCOUNT: str
        ID_TOKEN: str
        APP_METADATA: str
    class AuthorityType:
        ADFS: str
        MSSTS: str
    key_makers: Incomplete
    def __init__(self) -> None: ...
    def find(self, credential_type, target: Incomplete | None = None, query: Incomplete | None = None): ...
    def add(self, event, now: Incomplete | None = None):
        """Handle a token obtaining event, and add tokens into cache."""
    def modify(self, credential_type, old_entry, new_key_value_pairs: Incomplete | None = None) -> None: ...
    def remove_rt(self, rt_item): ...
    def update_rt(self, rt_item, new_rt): ...
    def remove_at(self, at_item): ...
    def remove_idt(self, idt_item): ...
    def remove_account(self, account_item): ...

class SerializableTokenCache(TokenCache):
    '''This serialization can be a starting point to implement your own persistence.

    This class does NOT actually persist the cache on disk/db/etc..
    Depending on your need,
    the following simple recipe for file-based persistence may be sufficient::

        import os, atexit, msal
        cache = msal.SerializableTokenCache()
        if os.path.exists("my_cache.bin"):
            cache.deserialize(open("my_cache.bin", "r").read())
        atexit.register(lambda:
            open("my_cache.bin", "w").write(cache.serialize())
            # Hint: The following optional line persists only when state changed
            if cache.has_state_changed else None
            )
        app = msal.ClientApplication(..., token_cache=cache)
        ...

    :var bool has_state_changed:
        Indicates whether the cache state in the memory has changed since last
        :func:`~serialize` or :func:`~deserialize` call.
    '''
    has_state_changed: bool
    def add(self, event, **kwargs) -> None: ...
    def modify(self, credential_type, old_entry, new_key_value_pairs: Incomplete | None = None) -> None: ...
    def deserialize(self, state: Optional[str]) -> None:
        """Deserialize the cache from a state previously obtained by serialize()"""
    def serialize(self) -> str:
        """Serialize the current cache state into a string."""
