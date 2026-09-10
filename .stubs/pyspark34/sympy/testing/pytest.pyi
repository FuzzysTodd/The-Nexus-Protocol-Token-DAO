from _typeshed import Incomplete
from collections.abc import Generator
from sympy.utilities.exceptions import SymPyDeprecationWarning as SymPyDeprecationWarning, ignore_warnings as ignore_warnings
from typing import Any, Callable

ON_CI: Incomplete
USE_PYTEST: Incomplete
raises: Callable[[Any, Any], Any]
XFAIL: Callable[[Any], Any]
skip: Callable[[Any], Any]
SKIP: Callable[[Any], Any]
slow: Callable[[Any], Any]
nocache_fail: Callable[[Any], Any]

class ExceptionInfo:
    value: Incomplete
    def __init__(self, value) -> None: ...

class RaisesContext:
    expectedException: Incomplete
    def __init__(self, expectedException) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None): ...

class XFail(Exception): ...
class XPass(Exception): ...
class Skipped(Exception): ...
class Failed(Exception): ...

def warns(warningcls, *, match: str = '', test_stacklevel: bool = True) -> Generator[Incomplete, None, None]:
    """
    Like raises but tests that warnings are emitted.

    >>> from sympy.testing.pytest import warns
    >>> import warnings

    >>> with warns(UserWarning):
    ...     warnings.warn('deprecated', UserWarning, stacklevel=2)

    >>> with warns(UserWarning):
    ...     pass
    Traceback (most recent call last):
    ...
    Failed: DID NOT WARN. No warnings of type UserWarning    was emitted. The list of emitted warnings is: [].

    ``test_stacklevel`` makes it check that the ``stacklevel`` parameter to
    ``warn()`` is set so that the warning shows the user line of code (the
    code under the warns() context manager). Set this to False if this is
    ambiguous or if the context manager does not test the direct user code
    that emits the warning.

    If the warning is a ``SymPyDeprecationWarning``, this additionally tests
    that the ``active_deprecations_target`` is a real target in the
    ``active-deprecations.md`` file.

    """
def warns_deprecated_sympy() -> Generator[None, None, None]:
    '''
    Shorthand for ``warns(SymPyDeprecationWarning)``

    This is the recommended way to test that ``SymPyDeprecationWarning`` is
    emitted for deprecated features in SymPy. To test for other warnings use
    ``warns``. To suppress warnings without asserting that they are emitted
    use ``ignore_warnings``.

    .. note::

       ``warns_deprecated_sympy()`` is only intended for internal use in the
       SymPy test suite to test that a deprecation warning triggers properly.
       All other code in the SymPy codebase, including documentation examples,
       should not use deprecated behavior.

       If you are a user of SymPy and you want to disable
       SymPyDeprecationWarnings, use ``warnings`` filters (see
       :ref:`silencing-sympy-deprecation-warnings`).

    >>> from sympy.testing.pytest import warns_deprecated_sympy
    >>> from sympy.utilities.exceptions import sympy_deprecation_warning
    >>> with warns_deprecated_sympy():
    ...     sympy_deprecation_warning("Don\'t use",
    ...        deprecated_since_version="1.0",
    ...        active_deprecations_target="active-deprecations")

    >>> with warns_deprecated_sympy():
    ...     pass
    Traceback (most recent call last):
    ...
    Failed: DID NOT WARN. No warnings of type     SymPyDeprecationWarning was emitted. The list of emitted warnings is: [].

    .. note::

       Sometimes the stacklevel test will fail because the same warning is
       emitted multiple times. In this case, you can use
       :func:`sympy.utilities.exceptions.ignore_warnings` in the code to
       prevent the ``SymPyDeprecationWarning`` from being emitted again
       recursively. In rare cases it is impossible to have a consistent
       ``stacklevel`` for deprecation warnings because different ways of
       calling a function will produce different call stacks.. In those cases,
       use ``warns(SymPyDeprecationWarning)`` instead.

    See Also
    ========
    sympy.utilities.exceptions.SymPyDeprecationWarning
    sympy.utilities.exceptions.sympy_deprecation_warning
    sympy.utilities.decorator.deprecated

    '''
def skip_under_pyodide(message):
    """Decorator to skip a test if running under pyodide."""
