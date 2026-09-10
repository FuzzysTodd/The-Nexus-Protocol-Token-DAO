import typing as t
from ..json import dumps as dumps, loads as loads
from _typeshed import Incomplete

class JSONTag:
    """Base class for defining type tags for :class:`TaggedJSONSerializer`."""
    key: str | None
    serializer: Incomplete
    def __init__(self, serializer: TaggedJSONSerializer) -> None:
        """Create a tagger for the given serializer."""
    def check(self, value: t.Any) -> bool:
        """Check if the given value should be tagged by this tag."""
    def to_json(self, value: t.Any) -> t.Any:
        """Convert the Python object to an object that is a valid JSON type.
        The tag will be added later."""
    def to_python(self, value: t.Any) -> t.Any:
        """Convert the JSON representation back to the correct type. The tag
        will already be removed."""
    def tag(self, value: t.Any) -> t.Any:
        """Convert the value to a valid JSON type and add the tag structure
        around it."""

class TagDict(JSONTag):
    """Tag for 1-item dicts whose only key matches a registered tag.

    Internally, the dict key is suffixed with `__`, and the suffix is removed
    when deserializing.
    """
    key: str
    def check(self, value: t.Any) -> bool: ...
    def to_json(self, value: t.Any) -> t.Any: ...
    def to_python(self, value: t.Any) -> t.Any: ...

class PassDict(JSONTag):
    def check(self, value: t.Any) -> bool: ...
    def to_json(self, value: t.Any) -> t.Any: ...
    tag = to_json

class TagTuple(JSONTag):
    key: str
    def check(self, value: t.Any) -> bool: ...
    def to_json(self, value: t.Any) -> t.Any: ...
    def to_python(self, value: t.Any) -> t.Any: ...

class PassList(JSONTag):
    def check(self, value: t.Any) -> bool: ...
    def to_json(self, value: t.Any) -> t.Any: ...
    tag = to_json

class TagBytes(JSONTag):
    key: str
    def check(self, value: t.Any) -> bool: ...
    def to_json(self, value: t.Any) -> t.Any: ...
    def to_python(self, value: t.Any) -> t.Any: ...

class TagMarkup(JSONTag):
    """Serialize anything matching the :class:`~markupsafe.Markup` API by
    having a ``__html__`` method to the result of that method. Always
    deserializes to an instance of :class:`~markupsafe.Markup`."""
    key: str
    def check(self, value: t.Any) -> bool: ...
    def to_json(self, value: t.Any) -> t.Any: ...
    def to_python(self, value: t.Any) -> t.Any: ...

class TagUUID(JSONTag):
    key: str
    def check(self, value: t.Any) -> bool: ...
    def to_json(self, value: t.Any) -> t.Any: ...
    def to_python(self, value: t.Any) -> t.Any: ...

class TagDateTime(JSONTag):
    key: str
    def check(self, value: t.Any) -> bool: ...
    def to_json(self, value: t.Any) -> t.Any: ...
    def to_python(self, value: t.Any) -> t.Any: ...

class TaggedJSONSerializer:
    """Serializer that uses a tag system to compactly represent objects that
    are not JSON types. Passed as the intermediate serializer to
    :class:`itsdangerous.Serializer`.

    The following extra types are supported:

    * :class:`dict`
    * :class:`tuple`
    * :class:`bytes`
    * :class:`~markupsafe.Markup`
    * :class:`~uuid.UUID`
    * :class:`~datetime.datetime`
    """
    default_tags: Incomplete
    tags: Incomplete
    order: Incomplete
    def __init__(self) -> None: ...
    def register(self, tag_class: type[JSONTag], force: bool = False, index: int | None = None) -> None:
        """Register a new tag with this serializer.

        :param tag_class: tag class to register. Will be instantiated with this
            serializer instance.
        :param force: overwrite an existing tag. If false (default), a
            :exc:`KeyError` is raised.
        :param index: index to insert the new tag in the tag order. Useful when
            the new tag is a special case of an existing tag. If ``None``
            (default), the tag is appended to the end of the order.

        :raise KeyError: if the tag key is already registered and ``force`` is
            not true.
        """
    def tag(self, value: t.Any) -> dict[str, t.Any]:
        """Convert a value to a tagged representation if necessary."""
    def untag(self, value: dict[str, t.Any]) -> t.Any:
        """Convert a tagged representation back to the original type."""
    def dumps(self, value: t.Any) -> str:
        """Tag the value and dump it to a compact JSON string."""
    def loads(self, value: str) -> t.Any:
        """Load data from a JSON string and deserialized any tagged objects."""
