from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping

def identity(x: _T) -> _T: ...
def exhaust(rule: Callable[[_T], _T]) -> Callable[[_T], _T]:
    """ Apply a rule repeatedly until it has no effect """
def memoize(rule: Callable[[_S], _T]) -> Callable[[_S], _T]:
    """Memoized version of a rule

    Notes
    =====

    This cache can grow infinitely, so it is not recommended to use this
    than ``functools.lru_cache`` unless you need very heavy computation.
    """
def condition(cond: Callable[[_T], bool], rule: Callable[[_T], _T]) -> Callable[[_T], _T]:
    """ Only apply rule if condition is true """
def chain(*rules: Callable[[_T], _T]) -> Callable[[_T], _T]:
    """
    Compose a sequence of rules so that they apply to the expr sequentially
    """
def debug(rule, file: Incomplete | None = None):
    """ Print out before and after expressions each time rule is used """
def null_safe(rule: Callable[[_T], _T | None]) -> Callable[[_T], _T]:
    """ Return original expr if rule returns None """
def tryit(rule: Callable[[_T], _T], exception) -> Callable[[_T], _T]:
    """ Return original expr if rule raises exception """
def do_one(*rules: Callable[[_T], _T]) -> Callable[[_T], _T]:
    """ Try each of the rules until one works. Then stop. """
def switch(key: Callable[[_S], _T], ruledict: Mapping[_T, Callable[[_S], _S]]) -> Callable[[_S], _S]:
    """ Select a rule based on the result of key called on the function """
def minimize(*rules: Callable[[_S], _T], objective=...) -> Callable[[_S], _T]:
    """ Select result of rules that minimizes objective

    >>> from sympy.strategies import minimize
    >>> inc = lambda x: x + 1
    >>> dec = lambda x: x - 1
    >>> rl = minimize(inc, dec)
    >>> rl(4)
    3

    >>> rl = minimize(inc, dec, objective=lambda x: -x)  # maximize
    >>> rl(4)
    5
    """
