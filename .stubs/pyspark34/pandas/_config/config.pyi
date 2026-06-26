from _typeshed import Incomplete
from contextlib import ContextDecorator
from pandas._typing import F as F, T as T
from pandas.util._exceptions import find_stack_level as find_stack_level
from typing import Any, Callable, Generator, Generic, Iterable, NamedTuple

class DeprecatedOption(NamedTuple):
    key: str
    msg: str | None
    rkey: str | None
    removal_ver: str | None

class RegisteredOption(NamedTuple):
    key: str
    defval: object
    doc: str
    validator: Callable[[object], Any] | None
    cb: Callable[[str], Any] | None

class OptionError(AttributeError, KeyError):
    """
    Exception raised for pandas.options.

    Backwards compatible with KeyError checks.
    """

def get_default_val(pat: str): ...

class DictWrapper:
    """provide attribute-style access to a nested dict"""
    def __init__(self, d: dict[str, Any], prefix: str = '') -> None: ...
    def __setattr__(self, key: str, val: Any) -> None: ...
    def __getattr__(self, key: str): ...
    def __dir__(self) -> Iterable[str]: ...

class CallableDynamicDoc(Generic[T]):
    __doc_tmpl__: Incomplete
    __func__: Incomplete
    def __init__(self, func: Callable[..., T], doc_tmpl: str) -> None: ...
    def __call__(self, *args, **kwds) -> T: ...
    @property
    def __doc__(self) -> str: ...

get_option: Incomplete
set_option: Incomplete
reset_option: Incomplete
describe_option: Incomplete
options: Incomplete

class option_context(ContextDecorator):
    """
    Context manager to temporarily set options in the `with` statement context.

    You need to invoke as ``option_context(pat, val, [(pat, val), ...])``.

    Examples
    --------
    >>> from pandas import option_context
    >>> with option_context('display.max_rows', 10, 'display.max_columns', 5):
    ...     pass
    """
    ops: Incomplete
    def __init__(self, *args) -> None: ...
    undo: Incomplete
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...

def register_option(key: str, defval: object, doc: str = '', validator: Callable[[object], Any] | None = None, cb: Callable[[str], Any] | None = None) -> None:
    '''
    Register an option in the package-wide pandas config object

    Parameters
    ----------
    key : str
        Fully-qualified key, e.g. "x.y.option - z".
    defval : object
        Default value of the option.
    doc : str
        Description of the option.
    validator : Callable, optional
        Function of a single argument, should raise `ValueError` if
        called with a value which is not a legal value for the option.
    cb
        a function of a single argument "key", which is called
        immediately after an option value is set/reset. key is
        the full name of the option.

    Raises
    ------
    ValueError if `validator` is specified and `defval` is not a valid value.

    '''
def deprecate_option(key: str, msg: str | None = None, rkey: str | None = None, removal_ver: str | None = None) -> None:
    '''
    Mark option `key` as deprecated, if code attempts to access this option,
    a warning will be produced, using `msg` if given, or a default message
    if not.
    if `rkey` is given, any access to the key will be re-routed to `rkey`.

    Neither the existence of `key` nor that if `rkey` is checked. If they
    do not exist, any subsequence access will fail as usual, after the
    deprecation warning is given.

    Parameters
    ----------
    key : str
        Name of the option to be deprecated.
        must be a fully-qualified option name (e.g "x.y.z.rkey").
    msg : str, optional
        Warning message to output when the key is referenced.
        if no message is given a default message will be emitted.
    rkey : str, optional
        Name of an option to reroute access to.
        If specified, any referenced `key` will be
        re-routed to `rkey` including set/get/reset.
        rkey must be a fully-qualified option name (e.g "x.y.z.rkey").
        used by the default message if no `msg` is specified.
    removal_ver : str, optional
        Specifies the version in which this option will
        be removed. used by the default message if no `msg` is specified.

    Raises
    ------
    OptionError
        If the specified key has already been deprecated.
    '''
def pp_options_list(keys: Iterable[str], width: int = 80, _print: bool = False):
    """Builds a concise listing of available options, grouped by prefix"""
def config_prefix(prefix) -> Generator[None, None, None]:
    '''
    contextmanager for multiple invocations of API with a common prefix

    supported API functions: (register / get / set )__option

    Warning: This is not thread - safe, and won\'t work properly if you import
    the API functions into your module using the "from x import y" construct.

    Example
    -------
    import pandas._config.config as cf
    with cf.config_prefix("display.font"):
        cf.register_option("color", "red")
        cf.register_option("size", " 5 pt")
        cf.set_option(size, " 6 pt")
        cf.get_option(size)
        ...

        etc\'

    will register options "display.font.color", "display.font.size", set the
    value of "display.font.size"... and so on.
    '''
def is_type_factory(_type: type[Any]) -> Callable[[Any], None]:
    """

    Parameters
    ----------
    `_type` - a type to be compared against (e.g. type(x) == `_type`)

    Returns
    -------
    validator - a function of a single argument x , which raises
                ValueError if type(x) is not equal to `_type`

    """
def is_instance_factory(_type) -> Callable[[Any], None]:
    """

    Parameters
    ----------
    `_type` - the type to be checked against

    Returns
    -------
    validator - a function of a single argument x , which raises
                ValueError if x is not an instance of `_type`

    """
def is_one_of_factory(legal_values) -> Callable[[Any], None]: ...
def is_nonnegative_int(value: object) -> None:
    """
    Verify that value is None or a positive int.

    Parameters
    ----------
    value : None or int
            The `value` to be checked.

    Raises
    ------
    ValueError
        When the value is not None or is a negative integer
    """

is_int: Incomplete
is_bool: Incomplete
is_float: Incomplete
is_str: Incomplete
is_text: Incomplete

def is_callable(obj) -> bool:
    """

    Parameters
    ----------
    `obj` - the object to be checked

    Returns
    -------
    validator - returns True if object is callable
        raises ValueError otherwise.

    """
