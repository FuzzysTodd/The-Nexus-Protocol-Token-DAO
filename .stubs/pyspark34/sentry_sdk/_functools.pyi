from _typeshed import Incomplete
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from typing import Any, Callable

WRAPPER_ASSIGNMENTS: Incomplete
WRAPPER_UPDATES: Incomplete

def update_wrapper(wrapper: Any, wrapped: Any, assigned: Any = ..., updated: Any = ...) -> Any:
    """Update a wrapper function to look like the wrapped function

    wrapper is the function to be updated
    wrapped is the original function
    assigned is a tuple naming the attributes assigned directly
    from the wrapped function to the wrapper function (defaults to
    functools.WRAPPER_ASSIGNMENTS)
    updated is a tuple naming the attributes of the wrapper that
    are updated with the corresponding attribute from the wrapped
    function (defaults to functools.WRAPPER_UPDATES)
    """
def wraps(wrapped: Callable[..., Any], assigned: Any = ..., updated: Any = ...) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator factory to apply update_wrapper() to a wrapper function

    Returns a decorator that invokes update_wrapper() with the decorated
    function as the wrapper argument and the arguments to wraps() as the
    remaining arguments. Default arguments are as for update_wrapper().
    This is a convenience function to simplify applying partial() to
    update_wrapper().
    """
