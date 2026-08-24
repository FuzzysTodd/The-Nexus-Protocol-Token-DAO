from . import Descriptor as Descriptor, MetaSerialisable as MetaSerialisable
from .namespace import namespaced as namespaced
from .sequence import MultiSequencePart as MultiSequencePart, NestedSequence as NestedSequence, Sequence as Sequence
from _typeshed import Incomplete
from openpyxl.compat import safe_string as safe_string
from openpyxl.xml.functions import Element as Element, localname as localname

KEYWORDS: Incomplete
seq_types: Incomplete

class Serialisable(metaclass=MetaSerialisable):
    """
    Objects can serialise to XML their attributes and child objects.
    The following class attributes are created by the metaclass at runtime:
    __attrs__ = attributes
    __nested__ = single-valued child treated as an attribute
    __elements__ = child elements
    """
    __attrs__: Incomplete
    __nested__: Incomplete
    __elements__: Incomplete
    __namespaced__: Incomplete
    idx_base: int
    @property
    def tagname(self) -> None: ...
    namespace: Incomplete
    @classmethod
    def from_tree(cls, node):
        """
        Create object from XML
        """
    def to_tree(self, tagname: Incomplete | None = None, idx: Incomplete | None = None, namespace: Incomplete | None = None): ...
    def __iter__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...
    def __add__(self, other): ...
    def __copy__(self): ...
