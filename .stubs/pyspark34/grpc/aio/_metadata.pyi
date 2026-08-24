from collections import abc
from typing import Any, Iterator, List, Tuple

MetadataKey = str
MetadataValue = str | bytes

class Metadata(abc.Mapping):
    """Metadata abstraction for the asynchronous calls and interceptors.

    The metadata is a mapping from str -> List[str]

    Traits
        * Multiple entries are allowed for the same key
        * The order of the values by key is preserved
        * Getting by an element by key, retrieves the first mapped value
        * Supports an immutable view of the data
        * Allows partial mutation on the data without recreating the new object from scratch.
    """
    def __init__(self, *args: Tuple[MetadataKey, MetadataValue]) -> None: ...
    @classmethod
    def from_tuple(cls, raw_metadata: tuple): ...
    def add(self, key: MetadataKey, value: MetadataValue) -> None: ...
    def __len__(self) -> int:
        """Return the total number of elements that there are in the metadata,
        including multiple values for the same key.
        """
    def __getitem__(self, key: MetadataKey) -> MetadataValue:
        """When calling <metadata>[<key>], the first element of all those
        mapped for <key> is returned.
        """
    def __setitem__(self, key: MetadataKey, value: MetadataValue) -> None:
        """Calling metadata[<key>] = <value>
        Maps <value> to the first instance of <key>.
        """
    def __delitem__(self, key: MetadataKey) -> None:
        """``del metadata[<key>]`` deletes the first mapping for <key>."""
    def delete_all(self, key: MetadataKey) -> None:
        """Delete all mappings for <key>."""
    def __iter__(self) -> Iterator[Tuple[MetadataKey, MetadataValue]]: ...
    def get_all(self, key: MetadataKey) -> List[MetadataValue]:
        """For compatibility with other Metadata abstraction objects (like in Java),
        this would return all items under the desired <key>.
        """
    def set_all(self, key: MetadataKey, values: List[MetadataValue]) -> None: ...
    def __contains__(self, key: MetadataKey) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __add__(self, other: Any) -> Metadata: ...
