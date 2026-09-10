import datetime
from _typeshed import Incomplete
from typing import Any, Iterable, Iterator, Mapping, MutableMapping, Tuple

TZ_UTC: Incomplete

class _FixedOffset(datetime.tzinfo):
    """Fixed offset in minutes east from UTC.

    Copy/pasted from Python doc

    :param int offset: offset in minutes
    """
    def __init__(self, offset) -> None: ...
    def utcoffset(self, dt): ...
    def tzname(self, dt): ...
    def dst(self, dt): ...

def case_insensitive_dict(*args: Mapping[str, Any] | Iterable[Tuple[str, Any]] | None, **kwargs: Any) -> MutableMapping[str, Any]:
    """Return a case-insensitive mutable mapping from an inputted mapping structure.

    :param args: The positional arguments to pass to the dict.
    :type args: Mapping[str, Any] or Iterable[Tuple[str, Any]
    :return: A case-insensitive mutable mapping object.
    :rtype: ~collections.abc.MutableMapping
    """

class CaseInsensitiveDict(MutableMapping[str, Any]):
    """
    NOTE: This implementation is heavily inspired from the case insensitive dictionary from the requests library.
    Thank you !!
    Case insensitive dictionary implementation.
    The keys are expected to be strings and will be stored in lower case.
    case_insensitive_dict = CaseInsensitiveDict()
    case_insensitive_dict['Key'] = 'some_value'
    case_insensitive_dict['key'] == 'some_value' #True

    :param data: Initial data to store in the dictionary.
    :type data: Mapping[str, Any] or Iterable[Tuple[str, Any]]
    """
    def __init__(self, data: Mapping[str, Any] | Iterable[Tuple[str, Any]] | None = None, **kwargs: Any) -> None: ...
    def copy(self) -> CaseInsensitiveDict: ...
    def __setitem__(self, key: str, value: Any) -> None:
        """Set the `key` to `value`.

        The original key will be stored with the value

        :param str key: The key to set.
        :param value: The value to set the key to.
        :type value: any
        """
    def __getitem__(self, key: str) -> Any: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def lowerkey_items(self) -> Iterator[Tuple[str, Any]]: ...
    def __eq__(self, other: Any) -> bool: ...
