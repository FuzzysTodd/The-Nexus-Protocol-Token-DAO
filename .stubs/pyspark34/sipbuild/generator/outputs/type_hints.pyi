from ...exceptions import UserException as UserException
from ..scoped_name import ScopedName as ScopedName
from ..specification import MappedType as MappedType, WrappedClass as WrappedClass, WrappedEnum as WrappedEnum
from _typeshed import Incomplete
from dataclasses import dataclass, field as field
from enum import Enum
from typing import List

class NodeType(Enum):
    """ The node types. """
    TYPING: Incomplete
    NESTED: Incomplete
    ENUM: Incomplete
    OTHER: Incomplete

class ParseState(Enum):
    """ The different parse states of a type hint. """
    REQUIRED: Incomplete
    PARSED: Incomplete

@dataclass
class ManagedTypeHint:
    """ Encapsulate a managed type hint. """
    type_hint: str
    as_docstring: str | None = ...
    as_rest_ref: str | None = ...
    parse_state: ParseState = ...
    root: TypeHintNode | None = ...
    def __init__(self, type_hint, as_docstring, as_rest_ref, parse_state, root) -> None: ...

@dataclass
class TypeHintNode:
    """ Encapsulate a node of a parsed type hint. """
    type: NodeType
    children: List['TypeHintNode'] | None = ...
    definition: str | MappedType | WrappedClass | WrappedEnum | None = ...
    def __init__(self, type, children, definition) -> None: ...

class TypeHintManager:
    """ A manager for type hints on behalf of a Specification object. """
    def __new__(cls, spec):
        """ Return the existing manager for a specification or create a new one
        if necessary.
        """
    def as_docstring(self, type_hint, out, context):
        """ Return the type hint as a docstring. """
    def as_rest_ref(self, type_hint, out, context, as_xml: bool = False):
        """ Return the type hint with appropriate reST references. """
    def as_type_hint(self, type_hint, out, context, defined):
        """ Return the type hint as a type hint. """

def format_voidptr(spec, as_xml):
    """ Return the representation of a voidptr in the context of either a type
    hint, XML or a docstring.
    """
