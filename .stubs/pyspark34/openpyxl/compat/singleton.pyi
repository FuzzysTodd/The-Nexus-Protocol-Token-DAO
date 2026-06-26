class Singleton(type):
    """
    Singleton metaclass
    Based on Python Cookbook 3rd Edition Recipe 9.13
    Only one instance of a class can exist. Does not work with __slots__
    """
    def __init__(self, *args, **kw) -> None: ...
    def __call__(self, *args, **kw): ...

class Cached(type):
    """
    Caching metaclass
    Child classes will only create new instances of themselves if
    one doesn't already exist. Does not work with __slots__
    """
    def __init__(self, *args, **kw) -> None: ...
    def __call__(self, *args): ...
