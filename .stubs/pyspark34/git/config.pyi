import abc
import configparser as cp
from _typeshed import Incomplete
from git.repo.base import Repo
from git.types import Lit_config_levels, PathLike, _T
from git.util import LockFile
from io import BytesIO
from typing import Any, Dict, Generic, List, OrderedDict, Sequence, Tuple, TypeVar

__all__ = ['GitConfigParser', 'SectionConstraint']

T_ConfigParser = TypeVar('T_ConfigParser', bound='GitConfigParser')
T_OMD_value = TypeVar('T_OMD_value', str, bytes, int, float, bool)
OrderedDict_OMD = OrderedDict
OrderedDict_OMD = OrderedDict[str, List[T_OMD_value]]

class MetaParserBuilder(abc.ABCMeta):
    """Utility class wrapping base-class methods into decorators that assure read-only properties"""
    def __new__(cls, name: str, bases: Tuple, clsdict: Dict[str, Any]) -> MetaParserBuilder:
        """
        Equip all base-class methods with a needs_values decorator, and all non-const methods
        with a set_dirty_and_flush_changes decorator in addition to that."""

class SectionConstraint(Generic[T_ConfigParser]):
    """Constrains a ConfigParser to only option commands which are constrained to
    always use the section we have been initialized with.

    It supports all ConfigParser methods that operate on an option.

    :note:
        If used as a context manager, will release the wrapped ConfigParser."""
    def __init__(self, config: T_ConfigParser, section: str) -> None: ...
    def __del__(self) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...
    @property
    def config(self) -> T_ConfigParser:
        """return: Configparser instance we constrain"""
    def release(self) -> None:
        """Equivalent to GitConfigParser.release(), which is called on our underlying parser instance"""
    def __enter__(self) -> SectionConstraint[T_ConfigParser]: ...
    def __exit__(self, exception_type: str, exception_value: str, traceback: str) -> None: ...

class _OMD(OrderedDict_OMD):
    """Ordered multi-dict."""
    def __setitem__(self, key: str, value: _T) -> None: ...
    def add(self, key: str, value: Any) -> None: ...
    def setall(self, key: str, values: List[_T]) -> None: ...
    def __getitem__(self, key: str) -> Any: ...
    def getlast(self, key: str) -> Any: ...
    def setlast(self, key: str, value: Any) -> None: ...
    def get(self, key: str, default: _T | None = None) -> _T | None: ...
    def getall(self, key: str) -> List[_T]: ...
    def items(self) -> List[Tuple[str, _T]]:
        """List of (key, last value for key)."""
    def items_all(self) -> List[Tuple[str, List[_T]]]:
        """List of (key, list of values for key)."""

class GitConfigParser(cp.RawConfigParser, metaclass=MetaParserBuilder):
    """Implements specifics required to read git style configuration files.

    This variation behaves much like the git.config command such that the configuration
    will be read on demand based on the filepath given during initialization.

    The changes will automatically be written once the instance goes out of scope, but
    can be triggered manually as well.

    The configuration file will be locked if you intend to change values preventing other
    instances to write concurrently.

    :note:
        The config is case-sensitive even when queried, hence section and option names
        must match perfectly.
        If used as a context manager, will release the locked file."""
    t_lock = LockFile
    re_comment: Incomplete
    optvalueonly_source: str
    OPTVALUEONLY: Incomplete
    OPTCRE: Incomplete
    def __init__(self, file_or_files: None | PathLike | BytesIO | Sequence[PathLike | BytesIO] = None, read_only: bool = True, merge_includes: bool = True, config_level: Lit_config_levels | None = None, repo: Repo | None = None) -> None:
        """Initialize a configuration reader to read the given file_or_files and to
        possibly allow changes to it by setting read_only False

        :param file_or_files:
            A single file path or file objects or multiple of these

        :param read_only:
            If True, the ConfigParser may only read the data , but not change it.
            If False, only a single file path or file object may be given. We will write back the changes
            when they happen, or when the ConfigParser is released. This will not happen if other
            configuration files have been included
        :param merge_includes: if True, we will read files mentioned in [include] sections and merge their
            contents into ours. This makes it impossible to write back an individual configuration file.
            Thus, if you want to modify a single configuration file, turn this off to leave the original
            dataset unaltered when reading it.
        :param repo: Reference to repository to use if [includeIf] sections are found in configuration files.

        """
    def __del__(self) -> None:
        """Write pending changes if required and release locks"""
    def __enter__(self) -> GitConfigParser: ...
    def __exit__(self, *args: Any) -> None: ...
    def release(self) -> None:
        """Flush changes and release the configuration write lock. This instance must not be used anymore afterwards.
        In Python 3, it's required to explicitly release locks and flush changes, as __del__ is not called
        deterministically anymore."""
    def optionxform(self, optionstr: str) -> str:
        """Do not transform options in any way when writing"""
    def read(self) -> None:
        """Reads the data stored in the files we have been initialized with. It will
        ignore files that cannot be read, possibly leaving an empty configuration

        :return: Nothing
        :raise IOError: if a file cannot be handled"""
    def items(self, section_name: str) -> List[Tuple[str, str]]:
        """:return: list((option, value), ...) pairs of all items in the given section"""
    def items_all(self, section_name: str) -> List[Tuple[str, List[str]]]:
        """:return: list((option, [values...]), ...) pairs of all items in the given section"""
    def write(self) -> None:
        """Write changes to our file, if there are changes at all

        :raise IOError: if this is a read-only writer instance or if we could not obtain
            a file lock"""
    def add_section(self, section: str) -> None:
        """Assures added options will stay in order"""
    @property
    def read_only(self) -> bool:
        """:return: True if this instance may change the configuration file"""
    def get_value(self, section: str, option: str, default: int | float | str | bool | None = None) -> int | float | str | bool:
        """Get an option's value.

        If multiple values are specified for this option in the section, the
        last one specified is returned.

        :param default:
            If not None, the given default value will be returned in case
            the option did not exist
        :return: a properly typed value, either int, float or string

        :raise TypeError: in case the value could not be understood
            Otherwise the exceptions known to the ConfigParser will be raised."""
    def get_values(self, section: str, option: str, default: int | float | str | bool | None = None) -> List[int | float | str | bool]:
        """Get an option's values.

        If multiple values are specified for this option in the section, all are
        returned.

        :param default:
            If not None, a list containing the given default value will be
            returned in case the option did not exist
        :return: a list of properly typed values, either int, float or string

        :raise TypeError: in case the value could not be understood
            Otherwise the exceptions known to the ConfigParser will be raised."""
    def set_value(self, section: str, option: str, value: str | bytes | int | float | bool) -> GitConfigParser:
        """Sets the given option in section to the given value.
        It will create the section if required, and will not throw as opposed to the default
        ConfigParser 'set' method.

        :param section: Name of the section in which the option resides or should reside
        :param option: Name of the options whose value to set

        :param value: Value to set the option to. It must be a string or convertible
            to a string
        :return: this instance"""
    def add_value(self, section: str, option: str, value: str | bytes | int | float | bool) -> GitConfigParser:
        """Adds a value for the given option in section.
        It will create the section if required, and will not throw as opposed to the default
        ConfigParser 'set' method. The value becomes the new value of the option as returned
        by 'get_value', and appends to the list of values returned by 'get_values`'.

        :param section: Name of the section in which the option resides or should reside
        :param option: Name of the option

        :param value: Value to add to option. It must be a string or convertible
            to a string
        :return: this instance"""
    def rename_section(self, section: str, new_name: str) -> GitConfigParser:
        """rename the given section to new_name
        :raise ValueError: if section doesn't exit
        :raise ValueError: if a section with new_name does already exist
        :return: this instance
        """
