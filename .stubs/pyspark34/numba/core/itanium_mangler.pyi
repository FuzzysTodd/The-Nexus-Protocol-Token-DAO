from _typeshed import Incomplete
from numba.core import types as types

PREFIX: str
N2CODE: Incomplete

def mangle_abi_tag(abi_tag: str) -> str: ...
def mangle_identifier(ident, template_params: str = '', *, abi_tags=(), uid: Incomplete | None = None):
    """
    Mangle the identifier with optional template parameters and abi_tags.

    Note:

    This treats '.' as '::' in C++.
    """
def mangle_type_or_value(typ):
    """
    Mangle type parameter and arbitrary value.
    """
mangle_type = mangle_type_or_value
mangle_value = mangle_type_or_value

def mangle_templated_ident(identifier, parameters):
    """
    Mangle templated identifier.
    """
def mangle_args(argtys):
    """
    Mangle sequence of Numba type objects and arbitrary values.
    """
def mangle(ident, argtys, *, abi_tags=(), uid: Incomplete | None = None):
    """
    Mangle identifier with Numba type objects and abi-tags.
    """
def prepend_namespace(mangled, ns):
    """
    Prepend namespace to mangled name.
    """
