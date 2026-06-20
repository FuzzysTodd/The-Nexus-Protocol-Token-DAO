from _typeshed import Incomplete

DEVICE_AUTH_GRANT: str

class ThrottledHttpClient:
    post: Incomplete
    get: Incomplete
    def __init__(self, http_client, http_cache) -> None:
        """Throttle the given http_client by storing and retrieving data from cache.

        This wrapper exists so that our patching post() and get() would prevent
        re-patching side effect when/if same http_client being reused.
        """
    def close(self):
        """MSAL won't need this. But we allow throttled_http_client.close() anyway"""
