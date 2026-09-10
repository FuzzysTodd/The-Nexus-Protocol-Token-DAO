from .core import NestedDateTime as NestedDateTime
from _typeshed import Incomplete
from openpyxl.descriptors import Alias as Alias, Bool as Bool, DateTime as DateTime, Float as Float, Integer as Integer, Strict as Strict, String as String
from openpyxl.descriptors.nested import NestedText as NestedText
from openpyxl.descriptors.sequence import Sequence as Sequence
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.xml.constants import CPROPS_FMTID as CPROPS_FMTID, CUSTPROPS_NS as CUSTPROPS_NS, VTYPES_NS as VTYPES_NS

class NestedBoolText(Bool, NestedText):
    """
    Descriptor for handling nested elements with the value stored in the text part
    """

class _CustomDocumentProperty(Serialisable):
    """
    Low-level representation of a Custom Document Property.
    Not used directly
    Must always contain a child element, even if this is empty
    """
    tagname: str
    name: Incomplete
    lpwstr: Incomplete
    i4: Incomplete
    r8: Incomplete
    filetime: Incomplete
    bool: Incomplete
    linkTarget: Incomplete
    fmtid: Incomplete
    pid: Incomplete
    def __init__(self, name: Incomplete | None = None, pid: int = 0, fmtid=..., linkTarget: Incomplete | None = None, **kw) -> None: ...
    @property
    def type(self): ...
    def to_tree(self, tagname: Incomplete | None = None, idx: Incomplete | None = None, namespace: Incomplete | None = None): ...

class _CustomDocumentPropertyList(Serialisable):
    """
    Parses and seriliases property lists but is not used directly
    """
    tagname: str
    property: Incomplete
    customProps: Incomplete
    def __init__(self, property=()) -> None: ...
    def __len__(self) -> int: ...
    def to_tree(self, tagname: Incomplete | None = None, idx: Incomplete | None = None, namespace: Incomplete | None = None): ...

class _TypedProperty(Strict):
    name: Incomplete
    value: Incomplete
    def __init__(self, name, value) -> None: ...
    def __eq__(self, other): ...

class IntProperty(_TypedProperty):
    value: Incomplete

class FloatProperty(_TypedProperty):
    value: Incomplete

class StringProperty(_TypedProperty):
    value: Incomplete

class DateTimeProperty(_TypedProperty):
    value: Incomplete

class BoolProperty(_TypedProperty):
    value: Incomplete

class LinkProperty(_TypedProperty):
    value: Incomplete

CLASS_MAPPING: Incomplete
XML_MAPPING: Incomplete

class CustomPropertyList(Strict):
    props: Incomplete
    def __init__(self) -> None: ...
    @classmethod
    def from_tree(cls, tree):
        """
        Create list from OOXML element
        """
    def append(self, prop) -> None: ...
    def to_tree(self): ...
    def __len__(self) -> int: ...
    @property
    def names(self):
        """List of property names"""
    def __getitem__(self, name):
        """
        Get property by name
        """
    def __delitem__(self, name) -> None:
        """
        Delete a propery by name
        """
    def __iter__(self): ...
