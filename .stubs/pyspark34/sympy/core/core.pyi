from _typeshed import Incomplete

ordering_of_classes: Incomplete

class Registry:
    """
    Base class for registry objects.

    Registries map a name to an object using attribute notation. Registry
    classes behave singletonically: all their instances share the same state,
    which is stored in the class object.

    All subclasses should set `__slots__ = ()`.
    """
    def __setattr__(self, name, obj) -> None: ...
    def __delattr__(self, name) -> None: ...
