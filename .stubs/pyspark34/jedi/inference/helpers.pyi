from _typeshed import Incomplete
from collections.abc import Generator

def is_stdlib_path(path): ...
def deep_ast_copy(obj):
    """
    Much, much faster than copy.deepcopy, but just for parser tree nodes.
    """
def infer_call_of_leaf(context, leaf, cut_own_trailer: bool = False):
    '''
    Creates a "call" node that consist of all ``trailer`` and ``power``
    objects.  E.g. if you call it with ``append``::

        list([]).append(3) or None

    You would get a node with the content ``list([]).append`` back.

    This generates a copy of the original ast node.

    If you\'re using the leaf, e.g. the bracket `)` it will return ``list([])``.

    We use this function for two purposes. Given an expression ``bar.foo``,
    we may want to
      - infer the type of ``foo`` to offer completions after foo
      - infer the type of ``bar`` to be able to jump to the definition of foo
    The option ``cut_own_trailer`` must be set to true for the second purpose.
    '''
def get_names_of_node(node): ...
def is_string(value): ...
def is_literal(value): ...
def get_int_or_none(value): ...
def get_str_or_none(value): ...
def is_number(value): ...

class SimpleGetItemNotFound(Exception): ...

def reraise_getitem_errors(*exception_classes) -> Generator[None, None, None]: ...
def parse_dotted_names(nodes, is_import_from, until_node: Incomplete | None = None): ...
def values_from_qualified_names(inference_state, *names): ...
def is_big_annoying_library(context): ...
