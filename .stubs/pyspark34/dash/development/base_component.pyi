import abc
from .._utils import OrderedSet as OrderedSet, patch_collections_abc as patch_collections_abc, stringify_id as stringify_id
from _typeshed import Incomplete

MutableSequence: Incomplete
rd: Incomplete

class ComponentRegistry:
    """Holds a registry of the namespaces used by components."""
    registry: Incomplete
    children_props: Incomplete
    @classmethod
    def get_resources(cls, resource_name): ...

class ComponentMeta(abc.ABCMeta):
    def __new__(mcs, name, bases, attributes): ...

def is_number(s): ...

class Component(metaclass=ComponentMeta):
    class _UNDEFINED: ...
    UNDEFINED: Incomplete
    class _REQUIRED: ...
    REQUIRED: Incomplete
    def __init__(self, **kwargs) -> None: ...
    def to_plotly_json(self): ...
    def __getitem__(self, id):
        """Recursively find the element with the given ID through the tree of
        children."""
    def __setitem__(self, id, item) -> None:
        """Set an element by its ID."""
    def __delitem__(self, id) -> None:
        """Delete items by ID in the tree of children."""
    def __iter__(self):
        """Yield IDs in the tree of children."""
    def __len__(self) -> int:
        """Return the number of items in the tree."""
