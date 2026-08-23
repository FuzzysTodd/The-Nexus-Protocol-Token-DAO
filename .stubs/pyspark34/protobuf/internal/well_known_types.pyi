from _typeshed import Incomplete
from collections.abc import Generator

class Any:
    """Class for Any Message type."""
    type_url: Incomplete
    value: Incomplete
    def Pack(self, msg, type_url_prefix: str = 'type.googleapis.com/', deterministic: Incomplete | None = None) -> None:
        """Packs the specified message into current Any message."""
    def Unpack(self, msg):
        """Unpacks the current Any message into specified message."""
    def TypeName(self):
        """Returns the protobuf type name of the inner message."""
    def Is(self, descriptor):
        """Checks if this Any represents the given protobuf type."""

class Timestamp:
    """Class for Timestamp message type."""
    def ToJsonString(self):
        """Converts Timestamp to RFC 3339 date string format.

    Returns:
      A string converted from timestamp. The string is always Z-normalized
      and uses 3, 6 or 9 fractional digits as required to represent the
      exact time. Example of the return format: '1972-01-01T10:00:20.021Z'
    """
    seconds: Incomplete
    nanos: Incomplete
    def FromJsonString(self, value) -> None:
        """Parse a RFC 3339 date string format to Timestamp.

    Args:
      value: A date string. Any fractional digits (or none) and any offset are
          accepted as long as they fit into nano-seconds precision.
          Example of accepted format: '1972-01-01T10:00:20.021-05:00'

    Raises:
      ValueError: On parsing problems.
    """
    def GetCurrentTime(self) -> None:
        """Get the current UTC into Timestamp."""
    def ToNanoseconds(self):
        """Converts Timestamp to nanoseconds since epoch."""
    def ToMicroseconds(self):
        """Converts Timestamp to microseconds since epoch."""
    def ToMilliseconds(self):
        """Converts Timestamp to milliseconds since epoch."""
    def ToSeconds(self):
        """Converts Timestamp to seconds since epoch."""
    def FromNanoseconds(self, nanos) -> None:
        """Converts nanoseconds since epoch to Timestamp."""
    def FromMicroseconds(self, micros) -> None:
        """Converts microseconds since epoch to Timestamp."""
    def FromMilliseconds(self, millis) -> None:
        """Converts milliseconds since epoch to Timestamp."""
    def FromSeconds(self, seconds) -> None:
        """Converts seconds since epoch to Timestamp."""
    def ToDatetime(self, tzinfo: Incomplete | None = None):
        """Converts Timestamp to a datetime.

    Args:
      tzinfo: A datetime.tzinfo subclass; defaults to None.

    Returns:
      If tzinfo is None, returns a timezone-naive UTC datetime (with no timezone
      information, i.e. not aware that it's UTC).

      Otherwise, returns a timezone-aware datetime in the input timezone.
    """
    def FromDatetime(self, dt) -> None:
        """Converts datetime to Timestamp.

    Args:
      dt: A datetime. If it's timezone-naive, it's assumed to be in UTC.
    """

class Duration:
    """Class for Duration message type."""
    def ToJsonString(self):
        '''Converts Duration to string format.

    Returns:
      A string converted from self. The string format will contains
      3, 6, or 9 fractional digits depending on the precision required to
      represent the exact Duration value. For example: "1s", "1.010s",
      "1.000000100s", "-3.100s"
    '''
    seconds: Incomplete
    nanos: Incomplete
    def FromJsonString(self, value) -> None:
        '''Converts a string to Duration.

    Args:
      value: A string to be converted. The string must end with \'s\'. Any
          fractional digits (or none) are accepted as long as they fit into
          precision. For example: "1s", "1.01s", "1.0000001s", "-3.100s

    Raises:
      ValueError: On parsing problems.
    '''
    def ToNanoseconds(self):
        """Converts a Duration to nanoseconds."""
    def ToMicroseconds(self):
        """Converts a Duration to microseconds."""
    def ToMilliseconds(self):
        """Converts a Duration to milliseconds."""
    def ToSeconds(self):
        """Converts a Duration to seconds."""
    def FromNanoseconds(self, nanos) -> None:
        """Converts nanoseconds to Duration."""
    def FromMicroseconds(self, micros) -> None:
        """Converts microseconds to Duration."""
    def FromMilliseconds(self, millis) -> None:
        """Converts milliseconds to Duration."""
    def FromSeconds(self, seconds) -> None:
        """Converts seconds to Duration."""
    def ToTimedelta(self):
        """Converts Duration to timedelta."""
    def FromTimedelta(self, td) -> None:
        """Converts timedelta to Duration."""

class FieldMask:
    """Class for FieldMask message type."""
    def ToJsonString(self):
        """Converts FieldMask to string according to proto3 JSON spec."""
    def FromJsonString(self, value) -> None:
        """Converts string to FieldMask according to proto3 JSON spec."""
    def IsValidForDescriptor(self, message_descriptor):
        """Checks whether the FieldMask is valid for Message Descriptor."""
    def AllFieldsFromDescriptor(self, message_descriptor) -> None:
        """Gets all direct fields of Message Descriptor to FieldMask."""
    def CanonicalFormFromMask(self, mask) -> None:
        '''Converts a FieldMask to the canonical form.

    Removes paths that are covered by another path. For example,
    "foo.bar" is covered by "foo" and will be removed if "foo"
    is also in the FieldMask. Then sorts all paths in alphabetical order.

    Args:
      mask: The original FieldMask to be converted.
    '''
    def Union(self, mask1, mask2) -> None:
        """Merges mask1 and mask2 into this FieldMask."""
    def Intersect(self, mask1, mask2) -> None:
        """Intersects mask1 and mask2 into this FieldMask."""
    def MergeMessage(self, source, destination, replace_message_field: bool = False, replace_repeated_field: bool = False) -> None:
        """Merges fields specified in FieldMask from source to destination.

    Args:
      source: Source message.
      destination: The destination message to be merged into.
      replace_message_field: Replace message field if True. Merge message
          field if False.
      replace_repeated_field: Replace repeated field if True. Append
          elements of repeated field if False.
    """

class _FieldMaskTree:
    '''Represents a FieldMask in a tree structure.

  For example, given a FieldMask "foo.bar,foo.baz,bar.baz",
  the FieldMaskTree will be:
      [_root] -+- foo -+- bar
            |       |
            |       +- baz
            |
            +- bar --- baz
  In the tree, each leaf node represents a field path.
  '''
    def __init__(self, field_mask: Incomplete | None = None) -> None:
        """Initializes the tree by FieldMask."""
    def MergeFromFieldMask(self, field_mask) -> None:
        """Merges a FieldMask to the tree."""
    def AddPath(self, path) -> None:
        """Adds a field path into the tree.

    If the field path to add is a sub-path of an existing field path
    in the tree (i.e., a leaf node), it means the tree already matches
    the given path so nothing will be added to the tree. If the path
    matches an existing non-leaf node in the tree, that non-leaf node
    will be turned into a leaf node with all its children removed because
    the path matches all the node's children. Otherwise, a new path will
    be added.

    Args:
      path: The field path to add.
    """
    def ToFieldMask(self, field_mask) -> None:
        """Converts the tree to a FieldMask."""
    def IntersectPath(self, path, intersection) -> None:
        """Calculates the intersection part of a field path with this tree.

    Args:
      path: The field path to calculates.
      intersection: The out tree to record the intersection part.
    """
    def AddLeafNodes(self, prefix, node) -> None:
        """Adds leaf nodes begin with prefix to this tree."""
    def MergeMessage(self, source, destination, replace_message, replace_repeated) -> None:
        """Merge all fields specified by this tree from source to destination."""

class Struct:
    """Class for Struct message type."""
    def __getitem__(self, key): ...
    def __contains__(self, item) -> bool: ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def get_or_create_list(self, key):
        """Returns a list for this key, creating if it didn't exist already."""
    def get_or_create_struct(self, key):
        """Returns a struct for this key, creating if it didn't exist already."""
    def update(self, dictionary) -> None: ...

class ListValue:
    """Class for ListValue message type."""
    def __len__(self) -> int: ...
    def append(self, value) -> None: ...
    def extend(self, elem_seq) -> None: ...
    def __getitem__(self, index):
        """Retrieves item by the specified index."""
    def __setitem__(self, index, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def items(self) -> Generator[Incomplete, None, None]: ...
    def add_struct(self):
        """Appends and returns a struct value as the next value in the list."""
    def add_list(self):
        """Appends and returns a list value as the next value in the list."""

WKTBASES: Incomplete
