from _typeshed import Incomplete
from typing import Any, Callable, TypeVar

C = TypeVar('C', bound=Callable[..., Any])

def experimental(api_or_type: C | str) -> C:
    """
    Decorator / decorator creator for marking APIs experimental in the docstring.

    :param api_or_type: An API to mark, or an API typestring for which to generate a decorator.
    :return: Decorated API (if a ``api_or_type`` is an API) or a function that decorates
             the specified API type (if ``api_or_type`` is a typestring).
    """
def developer_stable(func):
    """
    The API marked here as `@developer_stable` has certain protections associated with future
    development work.
    Classes marked with this decorator implicitly apply this status to all methods contained within
    them.

    APIs that are annotated with this decorator are guaranteed (except in cases of notes below) to:
    - maintain backwards compatibility such that earlier versions of any MLflow client, cli, or
      server will not have issues with any changes being made to them from an interface perspective.
    - maintain a consistent contract with respect to existing named arguments such that
      modifications will not alter or remove an existing named argument.
    - maintain implied or declared types of arguments within its signature.
    - maintain consistent behavior with respect to return types.

    Note: Should an API marked as `@developer_stable` require a modification for enhanced feature
      functionality, a deprecation warning will be added to the API well in advance of its
      modification.

    Note: Should an API marked as `@developer_stable` require patching for any security reason,
      advanced notice is not guaranteed and the labeling of such API as stable will be ignored
      for the sake of such a security patch.

    """
def deprecated(alternative: Incomplete | None = None, since: Incomplete | None = None, impact: Incomplete | None = None):
    """
    Annotation decorator for marking APIs as deprecated in docstrings and raising a warning if
    called.
    :param alternative: (Optional string) The name of a superseded replacement function, method,
                        or class to use in place of the deprecated one.
    :param since: (Optional string) A version designator defining during which release the function,
                  method, or class was marked as deprecated.
    :param impact: (Optional boolean) Indication of whether the method, function, or class will be
                   removed in a future release.
    :return: Decorated function.
    """
def keyword_only(func):
    """
    A decorator that forces keyword arguments in the wrapped method.
    """
