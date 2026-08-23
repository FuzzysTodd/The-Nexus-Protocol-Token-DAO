import typing
from _typeshed import Incomplete
from ipyparallel.serialize import codeutil as codeutil

buffer = memoryview
class_type = type
PICKLE_PROTOCOL: Incomplete
cell_type: Incomplete

def interactive(f):
    """decorator for making functions appear as interactively defined.
    This results in the function being linked to the user_ns as globals()
    instead of the module globals().
    """
def use_dill() -> None:
    """use dill to expand serialization support

    adds support for object methods and closures to serialization.
    """
def use_cloudpickle() -> None:
    """use cloudpickle to expand serialization support

    adds support for object methods and closures to serialization.
    """

class CannedObject:
    """A canned object."""
    keys: Incomplete
    obj: Incomplete
    hook: Incomplete
    buffers: Incomplete
    def __init__(self, obj, keys: Incomplete | None = None, hook: Incomplete | None = None) -> None:
        """can an object for safe pickling

        Parameters
        ----------
        obj
            The object to be canned
        keys : list (optional)
            list of attribute names that will be explicitly canned / uncanned
        hook : callable (optional)
            An optional extra callable,
            which can do additional processing of the uncanned object.

        Notes
        -----
        large data may be offloaded into the buffers list,
        used for zero-copy transfers.
        """
    def get_object(self, g: Incomplete | None = None):
        """Get an object."""

class Reference(CannedObject):
    """object for wrapping a remote reference by name."""
    name: Incomplete
    buffers: Incomplete
    def __init__(self, name) -> None:
        """Initialize the reference."""
    def get_object(self, g: Incomplete | None = None):
        """Get an object in the reference."""

class CannedCell(CannedObject):
    """Can a closure cell"""
    cell_contents: Incomplete
    def __init__(self, cell) -> None:
        """Initialize the canned cell."""
    def get_object(self, g: Incomplete | None = None):
        """Get an object in the cell."""

class CannedFunction(CannedObject):
    """Can a function."""
    code: Incomplete
    defaults: Incomplete
    closure: Incomplete
    module: Incomplete
    buffers: Incomplete
    def __init__(self, f) -> None:
        """Initialize the can"""
    def get_object(self, g: Incomplete | None = None):
        """Get an object out of the can."""

class CannedClass(CannedObject):
    """A canned class object."""
    name: Incomplete
    old_style: Incomplete
    parents: Incomplete
    buffers: Incomplete
    def __init__(self, cls) -> None:
        """Initialize the can."""
    def get_object(self, g: Incomplete | None = None):
        """Get an object from the can."""

class CannedArray(CannedObject):
    """A canned numpy array."""
    shape: Incomplete
    dtype: Incomplete
    pickled: bool
    buffers: Incomplete
    def __init__(self, obj) -> None:
        """Initialize the can."""
    def get_object(self, g: Incomplete | None = None):
        """Get the object."""

class CannedBytes(CannedObject):
    """A canned bytes object."""
    @staticmethod
    def wrap(buf: memoryview | bytes | typing.SupportsBytes) -> bytes:
        """Cast a buffer or memoryview object to bytes"""
    buffers: Incomplete
    def __init__(self, obj) -> None:
        """Initialize the can."""
    def get_object(self, g: Incomplete | None = None):
        """Get the canned object."""

class CannedBuffer(CannedBytes):
    """A canned buffer."""
    wrap = buffer

class CannedMemoryView(CannedBytes):
    """A canned memory view."""
    wrap = memoryview

def istype(obj, check):
    """like isinstance(obj, check), but strict

    This won't catch subclasses.
    """
def can(obj):
    """prepare an object for pickling"""
def can_class(obj):
    """Can a class object."""
def can_dict(obj):
    """can the *values* of a dict"""

sequence_types: Incomplete

def can_sequence(obj):
    """can the elements of a sequence"""
def uncan(obj, g: Incomplete | None = None):
    """invert canning"""
def uncan_dict(obj, g: Incomplete | None = None):
    """Uncan a dict object."""
def uncan_sequence(obj, g: Incomplete | None = None):
    """Uncan a sequence."""

can_map: Incomplete
uncan_map: typing.Dict[type, typing.Any]
