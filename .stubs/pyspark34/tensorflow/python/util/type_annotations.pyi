import typing

def is_generic_union(tp):
    """Returns true if `tp` is a parameterized typing.Union value."""
def is_generic_tuple(tp):
    """Returns true if `tp` is a parameterized typing.Tuple value."""
def is_generic_list(tp):
    """Returns true if `tp` is a parameterized typing.List value."""
def is_generic_mapping(tp):
    """Returns true if `tp` is a parameterized typing.Mapping value."""
def is_forward_ref(tp):
    """Returns true if `tp` is a typing forward reference."""
get_generic_type_args = typing.get_args
