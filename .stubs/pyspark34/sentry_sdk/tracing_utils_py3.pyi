from sentry_sdk import get_current_span as get_current_span
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP
from sentry_sdk.utils import logger as logger, qualname_from_function as qualname_from_function
from typing import Any

def start_child_span_decorator(func: Any) -> Any:
    """
    Decorator to add child spans for functions.

    This is the Python 3 compatible version of the decorator.
    For Python 2 there is duplicated code here: ``sentry_sdk.tracing_utils_python2.start_child_span_decorator()``.

    See also ``sentry_sdk.tracing.trace()``.
    """
