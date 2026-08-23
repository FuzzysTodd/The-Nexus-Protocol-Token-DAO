from ._abstract_span import AbstractSpan
from typing import Any, Callable, Generator

__all__ = ['change_context', 'with_current_context']

def change_context(span: AbstractSpan | None) -> Generator:
    """Execute this block inside the given context and restore it afterwards.

    This does not start and ends the span, but just make sure all code is executed within
    that span.

    If span is None, no-op.

    :param span: A span
    :type span: AbstractSpan
    :rtype: contextmanager
    :return: A context manager that will run the given span in the new context
    """
def with_current_context(func: Callable) -> Any:
    """Passes the current spans to the new context the function will be run in.

    :param func: The function that will be run in the new context
    :type func: callable
    :return: The func wrapped with correct context
    :rtype: callable
    """
