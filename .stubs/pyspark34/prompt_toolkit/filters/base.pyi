from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from typing import Callable, Iterable

__all__ = ['Filter', 'Never', 'Always', 'Condition', 'FilterOrBool']

class Filter(metaclass=ABCMeta):
    """
    Base class for any filter to activate/deactivate a feature, depending on a
    condition.

    The return value of ``__call__`` will tell if the feature should be active.
    """
    def __init__(self) -> None: ...
    @abstractmethod
    def __call__(self) -> bool:
        """
        The actual call to evaluate the filter.
        """
    def __and__(self, other: Filter) -> Filter:
        """
        Chaining of filters using the & operator.
        """
    def __or__(self, other: Filter) -> Filter:
        """
        Chaining of filters using the | operator.
        """
    def __invert__(self) -> Filter:
        """
        Inverting of filters using the ~ operator.
        """
    def __bool__(self) -> None:
        """
        By purpose, we don't allow bool(...) operations directly on a filter,
        because the meaning is ambiguous.

        Executing a filter has to be done always by calling it. Providing
        defaults for `None` values should be done through an `is None` check
        instead of for instance ``filter1 or Always()``.
        """

class _AndList(Filter):
    """
    Result of &-operation between several filters.
    """
    filters: Incomplete
    def __init__(self, filters: list[Filter]) -> None: ...
    @classmethod
    def create(cls, filters: Iterable[Filter]) -> Filter:
        """
        Create a new filter by applying an `&` operator between them.

        If there's only one unique filter in the given iterable, it will return
        that one filter instead of an `_AndList`.
        """
    def __call__(self) -> bool: ...

class _OrList(Filter):
    """
    Result of |-operation between several filters.
    """
    filters: Incomplete
    def __init__(self, filters: list[Filter]) -> None: ...
    @classmethod
    def create(cls, filters: Iterable[Filter]) -> Filter:
        """
        Create a new filter by applying an `|` operator between them.

        If there's only one unique filter in the given iterable, it will return
        that one filter instead of an `_OrList`.
        """
    def __call__(self) -> bool: ...

class _Invert(Filter):
    """
    Negation of another filter.
    """
    filter: Incomplete
    def __init__(self, filter: Filter) -> None: ...
    def __call__(self) -> bool: ...

class Always(Filter):
    """
    Always enable feature.
    """
    def __call__(self) -> bool: ...
    def __or__(self, other: Filter) -> Filter: ...
    def __invert__(self) -> Never: ...

class Never(Filter):
    """
    Never enable feature.
    """
    def __call__(self) -> bool: ...
    def __and__(self, other: Filter) -> Filter: ...
    def __invert__(self) -> Always: ...

class Condition(Filter):
    """
    Turn any callable into a Filter. The callable is supposed to not take any
    arguments.

    This can be used as a decorator::

        @Condition
        def feature_is_active():  # `feature_is_active` becomes a Filter.
            return True

    :param func: Callable which takes no inputs and returns a boolean.
    """
    func: Incomplete
    def __init__(self, func: Callable[[], bool]) -> None: ...
    def __call__(self) -> bool: ...
FilterOrBool = Filter | bool
