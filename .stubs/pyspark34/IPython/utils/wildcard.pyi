from IPython.utils.dir2 import dir2 as dir2
from _typeshed import Incomplete

def create_typestr2type_dicts(dont_include_in_type2typestr=['lambda']):
    """Return dictionaries mapping lower case typename (e.g. 'tuple') to type
    objects from the types package, and vice versa."""

typestr2type: Incomplete
type2typestr: Incomplete

def is_type(obj, typestr_or_type):
    """is_type(obj, typestr_or_type) verifies if obj is of a certain type. It
    can take strings or actual python types for the second argument, i.e.
    'tuple'<->TupleType. 'all' matches all types.

    TODO: Should be extended for choosing more than one type."""
def show_hidden(str, show_all: bool = False):
    """Return true for strings starting with single _ if show_all is true."""
def dict_dir(obj):
    """Produce a dictionary of an object's attributes. Builds on dir2 by
    checking that a getattr() call actually succeeds."""
def filter_ns(ns, name_pattern: str = '*', type_pattern: str = 'all', ignore_case: bool = True, show_all: bool = True):
    """Filter a namespace dictionary by name pattern and item type."""
def list_namespace(namespace, type_pattern, filter, ignore_case: bool = False, show_all: bool = False):
    """Return dictionary of all objects in a namespace dictionary that match
    type_pattern and filter."""
