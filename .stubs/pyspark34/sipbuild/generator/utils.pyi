from .scoped_name import ScopedName as ScopedName
from .specification import ArgumentType as ArgumentType, CachedName as CachedName, IfaceFile as IfaceFile, IfaceFileType as IfaceFileType
from _typeshed import Incomplete

def append_iface_file(iface_file_list, iface_file) -> None:
    """ Append an IfaceFile object to a list of them. """
def argument_as_str(arg):
    """ Convert an Argument object to a string of valid C++. """
def cached_name(spec, name):
    """ Add a name to the cache if necessary and return the cached name. """
def find_iface_file(spec, mod, fq_cpp_name, iface_file_type, error_logger, cpp_type: Incomplete | None = None, scope: Incomplete | None = None):
    """ Return an interface file for a fully qualified C/C++ name and type
    creating it if necessary.
    """
def find_method(klass, name):
    """ Return the Member object for a named member of a class or None if there
    was none.
    """
def normalised_scoped_name(scoped_name, scope):
    """ Convert a scoped name to a fully qualified name. """
def same_argument_type(spec, arg1, arg2, strict: bool = True):
    """ Compare two argument types and return True if they are the same.
    'strict' means as C++ would see it, rather than Python.
    """
def same_base_type(type1, type2):
    """ Return True if two Argument objects refer to the same base type, ie.
    without taking into account const and pointers.
    """
def same_signature(spec, sig1, sig2, strict: bool = True):
    """ Compare two signatures and return True if they are the same. """
def search_typedefs(spec, cpp_name, type) -> None:
    """ Search the typedefs and update the given type from any definition. """
