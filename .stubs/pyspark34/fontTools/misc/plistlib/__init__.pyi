from _typeshed import Incomplete
from datetime import datetime
from fontTools.misc import etree as etree
from fontTools.misc.textTools import tostr as tostr
from numbers import Integral
from typing import Any, IO, Mapping, MutableMapping, Sequence, Type

USE_BUILTIN_TYPES: bool
XML_DECLARATION: bytes
PLIST_DOCTYPE: bytes

class Data:
    """Represents binary data when ``use_builtin_types=False.``

    This class wraps binary data loaded from a plist file when the
    ``use_builtin_types`` argument to the loading function (:py:func:`fromtree`,
    :py:func:`load`, :py:func:`loads`) is false.

    The actual binary data is retrieved using the ``data`` attribute.
    """
    data: Incomplete
    def __init__(self, data: bytes) -> None: ...
    @classmethod
    def fromBase64(cls, data: bytes | str) -> Data: ...
    def asBase64(self, maxlinelength: int = 76, indent_level: int = 1) -> bytes: ...
    def __eq__(self, other: Any) -> bool: ...
PlistEncodable = bool | bytes | Data | datetime | float | Integral | Mapping[str, Any] | Sequence[Any] | str

class PlistTarget:
    '''Event handler using the ElementTree Target API that can be
    passed to a XMLParser to produce property list objects from XML.
    It is based on the CPython plistlib module\'s _PlistParser class,
    but does not use the expat parser.

    >>> from fontTools.misc import etree
    >>> parser = etree.XMLParser(target=PlistTarget())
    >>> result = etree.XML(
    ...     "<dict>"
    ...     "    <key>something</key>"
    ...     "    <string>blah</string>"
    ...     "</dict>",
    ...     parser=parser)
    >>> result == {"something": "blah"}
    True

    Links:
    https://github.com/python/cpython/blob/main/Lib/plistlib.py
    http://lxml.de/parsing.html#the-target-parser-interface
    '''
    stack: Incomplete
    current_key: Incomplete
    root: Incomplete
    def __init__(self, use_builtin_types: bool | None = None, dict_type: Type[MutableMapping[str, Any]] = ...) -> None: ...
    def start(self, tag: str, attrib: Mapping[str, str]) -> None: ...
    def end(self, tag: str) -> None: ...
    def data(self, data: str) -> None: ...
    def close(self) -> PlistEncodable: ...
    def add_object(self, value: PlistEncodable) -> None: ...
    def get_data(self) -> str: ...

def start_dict(self) -> None: ...
def end_dict(self) -> None: ...
def end_key(self) -> None: ...
def start_array(self) -> None: ...
def end_array(self) -> None: ...
def end_true(self) -> None: ...
def end_false(self) -> None: ...
def end_integer(self) -> None: ...
def end_real(self) -> None: ...
def end_string(self) -> None: ...
def end_data(self) -> None: ...
def end_date(self) -> None: ...
def totree(value: PlistEncodable, sort_keys: bool = True, skipkeys: bool = False, use_builtin_types: bool | None = None, pretty_print: bool = True, indent_level: int = 1) -> etree.Element:
    """Convert a value derived from a plist into an XML tree.

    Args:
        value: Any kind of value to be serialized to XML.
        sort_keys: Whether keys of dictionaries should be sorted.
        skipkeys (bool): Whether to silently skip non-string dictionary
            keys.
        use_builtin_types (bool): If true, byte strings will be
            encoded in Base-64 and wrapped in a ``data`` tag; if
            false, they will be either stored as ASCII strings or an
            exception raised if they cannot be decoded as such. Defaults
            to ``True`` if not present. Deprecated.
        pretty_print (bool): Whether to indent the output.
        indent_level (int): Level of indentation when serializing.

    Returns: an ``etree`` ``Element`` object.

    Raises:
        ``TypeError``
            if non-string dictionary keys are serialized
            and ``skipkeys`` is false.
        ``ValueError``
            if non-ASCII binary data is present
            and `use_builtin_types` is false.
    """
def fromtree(tree: etree.Element, use_builtin_types: bool | None = None, dict_type: Type[MutableMapping[str, Any]] = ...) -> Any:
    """Convert an XML tree to a plist structure.

    Args:
        tree: An ``etree`` ``Element``.
        use_builtin_types: If True, binary data is deserialized to
            bytes strings. If False, it is wrapped in :py:class:`Data`
            objects. Defaults to True if not provided. Deprecated.
        dict_type: What type to use for dictionaries.

    Returns: An object (usually a dictionary).
    """
def load(fp: IO[bytes], use_builtin_types: bool | None = None, dict_type: Type[MutableMapping[str, Any]] = ...) -> Any:
    """Load a plist file into an object.

    Args:
        fp: An opened file.
        use_builtin_types: If True, binary data is deserialized to
            bytes strings. If False, it is wrapped in :py:class:`Data`
            objects. Defaults to True if not provided. Deprecated.
        dict_type: What type to use for dictionaries.

    Returns:
        An object (usually a dictionary) representing the top level of
        the plist file.
    """
def loads(value: bytes, use_builtin_types: bool | None = None, dict_type: Type[MutableMapping[str, Any]] = ...) -> Any:
    """Load a plist file from a string into an object.

    Args:
        value: A bytes string containing a plist.
        use_builtin_types: If True, binary data is deserialized to
            bytes strings. If False, it is wrapped in :py:class:`Data`
            objects. Defaults to True if not provided. Deprecated.
        dict_type: What type to use for dictionaries.

    Returns:
        An object (usually a dictionary) representing the top level of
        the plist file.
    """
def dump(value: PlistEncodable, fp: IO[bytes], sort_keys: bool = True, skipkeys: bool = False, use_builtin_types: bool | None = None, pretty_print: bool = True) -> None:
    """Write a Python object to a plist file.

    Args:
        value: An object to write.
        fp: A file opened for writing.
        sort_keys (bool): Whether keys of dictionaries should be sorted.
        skipkeys (bool): Whether to silently skip non-string dictionary
            keys.
        use_builtin_types (bool): If true, byte strings will be
            encoded in Base-64 and wrapped in a ``data`` tag; if
            false, they will be either stored as ASCII strings or an
            exception raised if they cannot be represented. Defaults
        pretty_print (bool): Whether to indent the output.
        indent_level (int): Level of indentation when serializing.

    Raises:
        ``TypeError``
            if non-string dictionary keys are serialized
            and ``skipkeys`` is false.
        ``ValueError``
            if non-representable binary data is present
            and `use_builtin_types` is false.
    """
def dumps(value: PlistEncodable, sort_keys: bool = True, skipkeys: bool = False, use_builtin_types: bool | None = None, pretty_print: bool = True) -> bytes:
    """Write a Python object to a string in plist format.

    Args:
        value: An object to write.
        sort_keys (bool): Whether keys of dictionaries should be sorted.
        skipkeys (bool): Whether to silently skip non-string dictionary
            keys.
        use_builtin_types (bool): If true, byte strings will be
            encoded in Base-64 and wrapped in a ``data`` tag; if
            false, they will be either stored as strings or an
            exception raised if they cannot be represented. Defaults
        pretty_print (bool): Whether to indent the output.
        indent_level (int): Level of indentation when serializing.

    Returns:
        string: A plist representation of the Python object.

    Raises:
        ``TypeError``
            if non-string dictionary keys are serialized
            and ``skipkeys`` is false.
        ``ValueError``
            if non-representable binary data is present
            and `use_builtin_types` is false.
    """
