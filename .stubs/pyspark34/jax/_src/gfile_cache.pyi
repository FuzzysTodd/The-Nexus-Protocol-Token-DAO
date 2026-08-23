from jax._src.compilation_cache_interface import CacheInterface as CacheInterface

class GFileCache(CacheInterface):
    def __init__(self, path: str) -> None:
        """Sets up a cache at 'path'. Cached values may already be present."""
    def get(self, key: str):
        """Returns None if 'key' isn't present."""
    def put(self, key: str, value: bytes):
        """Adds new cache entry."""
