from . import compat as compat
from .. import exc as exc
from .langhelpers import decorator as decorator, inject_docstring_text as inject_docstring_text, inject_param_text as inject_param_text
from typing import Any, Callable, Sequence, Tuple, Type

def warn_deprecated(msg: str, version: str, stacklevel: int = 3, code: str | None = None) -> None: ...
def warn_deprecated_limited(msg: str, args: Sequence[Any], version: str, stacklevel: int = 3, code: str | None = None) -> None:
    """Issue a deprecation warning with a parameterized string,
    limiting the number of registrations.

    """
def deprecated_cls(version: str, message: str, constructor: str | None = '__init__') -> Callable[[Type[_T]], Type[_T]]: ...
def deprecated(version: str, message: str | None = None, add_deprecation_to_docstring: bool = True, warning: Type[exc.SADeprecationWarning] | None = None, enable_warnings: bool = True) -> Callable[[_F], _F]:
    """Decorates a function and issues a deprecation warning on use.

    :param version:
      Issue version in the warning.

    :param message:
      If provided, issue message in the warning.  A sensible default
      is used if not provided.

    :param add_deprecation_to_docstring:
      Default True.  If False, the wrapped function's __doc__ is left
      as-is.  If True, the 'message' is prepended to the docs if
      provided, or sensible default if message is omitted.

    """
def moved_20(message: str, **kw: Any) -> Callable[[Callable[..., _T]], Callable[..., _T]]: ...
def became_legacy_20(api_name: str, alternative: str | None = None, **kw: Any) -> Callable[[_F], _F]: ...
def deprecated_params(**specs: Tuple[str, str]) -> Callable[[_F], _F]:
    '''Decorates a function to warn on use of certain parameters.

    e.g. ::

        @deprecated_params(
            weak_identity_map=(
                "0.7",
                "the :paramref:`.Session.weak_identity_map parameter "
                "is deprecated."
            )

        )

    '''
