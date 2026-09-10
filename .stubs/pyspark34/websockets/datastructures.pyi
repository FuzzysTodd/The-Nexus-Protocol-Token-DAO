from typing import Any, Iterable, Iterator, List, Mapping, MutableMapping, Protocol, Tuple

__all__ = ['Headers', 'HeadersLike', 'MultipleValuesError']

class MultipleValuesError(LookupError):
    """
    Exception raised when :class:`Headers` has more than one value for a key.

    """

class Headers(MutableMapping[str, str]):
    """
    Efficient data structure for manipulating HTTP headers.

    A :class:`list` of ``(name, values)`` is inefficient for lookups.

    A :class:`dict` doesn't suffice because header names are case-insensitive
    and multiple occurrences of headers with the same name are possible.

    :class:`Headers` stores HTTP headers in a hybrid data structure to provide
    efficient insertions and lookups while preserving the original data.

    In order to account for multiple values with minimal hassle,
    :class:`Headers` follows this logic:

    - When getting a header with ``headers[name]``:
        - if there's no value, :exc:`KeyError` is raised;
        - if there's exactly one value, it's returned;
        - if there's more than one value, :exc:`MultipleValuesError` is raised.

    - When setting a header with ``headers[name] = value``, the value is
      appended to the list of values for that header.

    - When deleting a header with ``del headers[name]``, all values for that
      header are removed (this is slow).

    Other methods for manipulating headers are consistent with this logic.

    As long as no header occurs multiple times, :class:`Headers` behaves like
    :class:`dict`, except keys are lower-cased to provide case-insensitivity.

    Two methods support manipulating multiple values explicitly:

    - :meth:`get_all` returns a list of all values for a header;
    - :meth:`raw_items` returns an iterator of ``(name, values)`` pairs.

    """
    def __init__(self, *args: HeadersLike, **kwargs: str) -> None: ...
    def copy(self) -> Headers: ...
    def serialize(self) -> bytes: ...
    def __contains__(self, key: object) -> bool: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: str) -> str: ...
    def __setitem__(self, key: str, value: str) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def clear(self) -> None:
        """
        Remove all headers.

        """
    def update(self, *args: HeadersLike, **kwargs: str) -> None:
        """
        Update from a :class:`Headers` instance and/or keyword arguments.

        """
    def get_all(self, key: str) -> List[str]:
        """
        Return the (possibly empty) list of all values for a header.

        Args:
            key: header name.

        """
    def raw_items(self) -> Iterator[Tuple[str, str]]:
        """
        Return an iterator of all values as ``(name, value)`` pairs.

        """

class SupportsKeysAndGetItem(Protocol):
    """
    Dict-like types with ``keys() -> str`` and ``__getitem__(key: str) -> str`` methods.

    """
    def keys(self) -> Iterable[str]: ...
    def __getitem__(self, key: str) -> str: ...
HeadersLike = Headers | Mapping[str, str] | Iterable[Tuple[str, str]] | SupportsKeysAndGetItem
