from .base import Alias as Alias, Descriptor as Descriptor
from .namespace import namespaced as namespaced
from _typeshed import Incomplete
from collections.abc import Generator
from openpyxl.compat import safe_string as safe_string
from openpyxl.utils.indexed_list import IndexedList as IndexedList
from openpyxl.xml.functions import Element as Element

class Sequence(Descriptor):
    """
    A sequence (list or tuple) that may only contain objects of the declared
    type
    """
    expected_type: Incomplete
    seq_types: Incomplete
    idx_base: int
    unique: bool
    container = list
    def __set__(self, instance, seq) -> None: ...
    def to_tree(self, tagname, obj, namespace: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """
        Convert the sequence represented by the descriptor to an XML element
        """

class UniqueSequence(Sequence):
    """
    Use a set to keep values unique
    """
    seq_types: Incomplete
    container = set

class ValueSequence(Sequence):
    '''
    A sequence of primitive types that are stored as a single attribute.
    "val" is the default attribute
    '''
    attribute: str
    def to_tree(self, tagname, obj, namespace: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
    def from_tree(self, node): ...

class NestedSequence(Sequence):
    """
    Wrap a sequence in an containing object
    """
    count: bool
    def to_tree(self, tagname, obj, namespace: Incomplete | None = None): ...
    def from_tree(self, node): ...

class MultiSequence(Sequence):
    """
    Sequences can contain objects with different tags
    """
    def __set__(self, instance, seq) -> None: ...
    def to_tree(self, tagname, obj, namespace: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """
        Convert the sequence represented by the descriptor to an XML element
        """

class MultiSequencePart(Alias):
    """
    Allow a multisequence to be built up from parts

    Excluded from the instance __elements__ or __attrs__ as is effectively an Alias
    """
    expected_type: Incomplete
    store: Incomplete
    def __init__(self, expected_type, store) -> None: ...
    def __set__(self, instance, value) -> None: ...
    def __get__(self, instance, cls): ...
