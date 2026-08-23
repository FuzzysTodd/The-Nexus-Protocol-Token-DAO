from ..util import sqla_compat as sqla_compat
from _typeshed import Incomplete
from sqlalchemy.testing.assertions import eq_ as eq_, is_ as is_, is_false as is_false, is_not_ as is_not_, is_true as is_true, ne_ as ne_
from typing import Any

def assert_raises(except_cls, callable_, *args, **kw): ...
def assert_raises_context_ok(except_cls, callable_, *args, **kw): ...
def assert_raises_message(except_cls, msg, callable_, *args, **kwargs): ...
def assert_raises_message_context_ok(except_cls, msg, callable_, *args, **kwargs): ...

class _ErrorContainer:
    error: Any

def expect_raises(except_cls, check_context: bool = True): ...
def expect_raises_message(except_cls, msg, check_context: bool = True): ...
def eq_ignore_whitespace(a, b, msg: Incomplete | None = None) -> None: ...
def expect_warnings(*messages, **kw):
    """Context manager which expects one or more warnings.

    With no arguments, squelches all SAWarnings emitted via
    sqlalchemy.util.warn and sqlalchemy.util.warn_limited.   Otherwise
    pass string expressions that will match selected warnings via regex;
    all non-matching warnings are sent through.

    The expect version **asserts** that the warnings were in fact seen.

    Note that the test suite sets SAWarning warnings to raise exceptions.

    """
def emits_python_deprecation_warning(*messages):
    """Decorator form of expect_warnings().

    Note that emits_warning does **not** assert that the warnings
    were in fact seen.

    """
def expect_sqlalchemy_deprecated(*messages, **kw): ...
def expect_sqlalchemy_deprecated_20(*messages, **kw): ...
