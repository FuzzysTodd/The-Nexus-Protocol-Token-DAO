from typing import Any, Callable, List, Type

class QueryException(Exception): ...
class GroupingException(Exception): ...
class CaseException(Exception): ...
class JoinException(Exception): ...
class SetOperationException(Exception): ...
class RollupException(Exception): ...
class DialectNotSupported(Exception): ...
class FunctionException(Exception): ...

def builder(func: Callable) -> Callable:
    '''
    Decorator for wrapper "builder" functions.  These are functions on the Query class or other classes used for
    building queries which mutate the query and return self.  To make the build functions immutable, this decorator is
    used which will deepcopy the current instance.  This decorator will return the return value of the inner function
    or the new copy of the instance.  The inner function does not need to return self.
    '''
def ignore_copy(func: Callable) -> Callable:
    """
    Decorator for wrapping the __getattr__ function for classes that are copied via deepcopy.  This prevents infinite
    recursion caused by deepcopy looking for magic functions in the class. Any class implementing __getattr__ that is
    meant to be deepcopy'd should use this decorator.

    deepcopy is used by pypika in builder functions (decorated by @builder) to make the results immutable.  Any data
    model type class (stored in the Query instance) is copied.
    """
def resolve_is_aggregate(values: List[bool | None]) -> bool | None:
    """
    Resolves the is_aggregate flag for an expression that contains multiple terms.  This works like a voter system,
    each term votes True or False or abstains with None.

    :param values: A list of booleans (or None) for each term in the expression
    :return: If all values are True or None, True is returned.  If all values are None, None is returned. Otherwise,
        False is returned.
    """
def format_quotes(value: Any, quote_char: str | None) -> str: ...
def format_alias_sql(sql: str, alias: str | None, quote_char: str | None = None, alias_quote_char: str | None = None, as_keyword: bool = False, **kwargs: Any) -> str: ...
def validate(*args: Any, exc: Exception | None = None, type: Type | None = None) -> None: ...
