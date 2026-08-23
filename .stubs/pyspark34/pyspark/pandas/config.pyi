from _typeshed import Incomplete
from pyspark._globals import _NoValueType
from typing import Any, Callable, Dict, Iterator, List, Tuple

__all__ = ['get_option', 'set_option', 'reset_option', 'options', 'option_context']

class Option:
    '''
    Option class that defines an option with related properties.

    This class holds all information relevant to the one option. Also,
    Its instance can validate if the given value is acceptable or not.

    It is currently for internal usage only.

    Parameters
    ----------
    key: str, keyword-only argument
        the option name to use.
    doc: str, keyword-only argument
        the documentation for the current option.
    default: Any, keyword-only argument
        default value for this option.
    types: Union[Tuple[type, ...], type], keyword-only argument
        default is str. It defines the expected types for this option. It is
        used with `isinstance` to validate the given value to this option.
    check_func: Tuple[Callable[[Any], bool], str], keyword-only argument
        default is a function that always returns `True` with an empty string.
        It defines:
          - a function to check the given value to this option
          - the error message to show when this check is failed
        When new value is set to this option, this function is called to check
        if the given value is valid.

    Examples
    --------
    >>> option = Option(
    ...     key=\'option.name\',
    ...     doc="this is a test option",
    ...     default="default",
    ...     types=(float, int),
    ...     check_func=(lambda v: v > 0, "should be a positive float"))

    >>> option.validate(\'abc\')  # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
      ...
    TypeError: The value for option \'option.name\' was <class \'str\'>;
    however, expected types are [(<class \'float\'>, <class \'int\'>)].

    >>> option.validate(-1.1)
    Traceback (most recent call last):
      ...
    ValueError: should be a positive float

    >>> option.validate(1.1)
    '''
    key: Incomplete
    doc: Incomplete
    default: Incomplete
    types: Incomplete
    check_func: Incomplete
    def __init__(self, *, key: str, doc: str, default: Any, types: Tuple[type, ...] | type = ..., check_func: Tuple[Callable[[Any], bool], str] = ...) -> None: ...
    def validate(self, v: Any) -> None:
        """
        Validate the given value and throw an exception with related information such as key.
        """

class OptionError(AttributeError, KeyError): ...

def get_option(key: str, default: Any | _NoValueType = ...) -> Any:
    """
    Retrieves the value of the specified option.

    Parameters
    ----------
    key : str
        The key which should match a single option.
    default : object
        The default value if the option is not set yet. The value should be JSON serializable.

    Returns
    -------
    result : the value of the option

    Raises
    ------
    OptionError : if no such option exists and the default is not provided
    """
def set_option(key: str, value: Any) -> None:
    """
    Sets the value of the specified option.

    Parameters
    ----------
    key : str
        The key which should match a single option.
    value : object
        New value of option. The value should be JSON serializable.

    Returns
    -------
    None
    """
def reset_option(key: str) -> None:
    '''
    Reset one option to their default value.

    Pass "all" as an argument to reset all options.

    Parameters
    ----------
    key : str
        If specified only option will be reset.

    Returns
    -------
    None
    '''
def option_context(*args: Any) -> Iterator[None]:
    """
    Context manager to temporarily set options in the `with` statement context.

    You need to invoke ``option_context(pat, val, [(pat, val), ...])``.

    Examples
    --------
    >>> with option_context('display.max_rows', 10, 'compute.max_rows', 5):
    ...     print(get_option('display.max_rows'), get_option('compute.max_rows'))
    10 5
    >>> print(get_option('display.max_rows'), get_option('compute.max_rows'))
    1000 1000
    """

class DictWrapper:
    """provide attribute-style access to a nested dict"""
    def __init__(self, d: Dict[str, Option], prefix: str = '') -> None: ...
    def __setattr__(self, key: str, val: Any) -> None: ...
    def __getattr__(self, key: str) -> DictWrapper | Any: ...
    def __dir__(self) -> List[str]: ...

options: Incomplete
