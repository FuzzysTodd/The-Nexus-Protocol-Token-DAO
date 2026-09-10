from _typeshed import Incomplete
from statsmodels.compat.pandas import cache_readonly as PandasCacheReadonly

__all__ = ['cache_readonly', 'cache_writable', 'deprecated_alias', 'ResettableCache']

class ResettableCache(dict):
    """DO NOT USE. BACKWARD COMPAT ONLY"""
    __dict__: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...

def deprecated_alias(old_name, new_name, remove_version: Incomplete | None = None, msg: Incomplete | None = None, warning=...):
    """
    Deprecate attribute in favor of alternative name.

    Parameters
    ----------
    old_name : str
        Old, deprecated name
    new_name : str
        New name
    remove_version : str, optional
        Version that the alias will be removed
    msg : str, optional
        Message to show.  Default is
        `old_name` is a deprecated alias for `new_name`
    warning : Warning, optional
        Warning class to give.  Default is FutureWarning.

    Notes
    -----
    Older or less-used classes may not conform to statsmodels naming
    conventions.  `deprecated_alias` lets us bring them into conformance
    without breaking backward-compatibility.

    Example
    -------
    Instances of the `Foo` class have a `nvars` attribute, but it _should_
    be called `neqs`:

    class Foo:
        nvars = deprecated_alias('nvars', 'neqs')
        def __init__(self, neqs):
            self.neqs = neqs

    >>> foo = Foo(3)
    >>> foo.nvars
    __main__:1: FutureWarning: nvars is a deprecated alias for neqs
    3
    """

class CachedAttribute:
    fget: Incomplete
    name: Incomplete
    cachename: Incomplete
    def __init__(self, func, cachename: Incomplete | None = None) -> None: ...
    def __get__(self, obj, type: Incomplete | None = None): ...
    def __set__(self, obj, value) -> None: ...

class CachedWritableAttribute(CachedAttribute):
    def __set__(self, obj, value) -> None: ...

class _cache_readonly(property):
    """
    Decorator for CachedAttribute
    """
    func: Incomplete
    cachename: Incomplete
    def __init__(self, cachename: Incomplete | None = None) -> None: ...
    def __call__(self, func): ...

class cache_writable(_cache_readonly):
    """
    Decorator for CachedWritableAttribute
    """
    def __call__(self, func): ...
cache_readonly = PandasCacheReadonly
cached_data = PandasCacheReadonly
cached_value = PandasCacheReadonly
