from mako import exceptions as exceptions
from mako.cache import CacheImpl as CacheImpl

has_beaker: bool

class BeakerCacheImpl(CacheImpl):
    """A :class:`.CacheImpl` provided for the Beaker caching system.

    This plugin is used by default, based on the default
    value of ``'beaker'`` for the ``cache_impl`` parameter of the
    :class:`.Template` or :class:`.TemplateLookup` classes.

    """
    def __init__(self, cache) -> None: ...
    def get_or_create(self, key, creation_function, **kw): ...
    def put(self, key, value, **kw) -> None: ...
    def get(self, key, **kw): ...
    def invalidate(self, key, **kw) -> None: ...
