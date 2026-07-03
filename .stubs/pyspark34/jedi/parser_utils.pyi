from _typeshed import Incomplete
from collections.abc import Generator

def get_executable_nodes(node, last_added: bool = False):
    """
    For static analysis.
    """
def get_sync_comp_fors(comp_for) -> Generator[Incomplete, None, None]: ...
def for_stmt_defines_one_name(for_stmt):
    """
    Returns True if only one name is returned: ``for x in y``.
    Returns False if the for loop is more complicated: ``for x, z in y``.

    :returns: bool
    """
def get_flow_branch_keyword(flow_node, node): ...
def clean_scope_docstring(scope_node):
    """ Returns a cleaned version of the docstring token. """
def find_statement_documentation(tree_node): ...
def safe_literal_eval(value): ...
def get_signature(funcdef, width: int = 72, call_string: Incomplete | None = None, omit_first_param: bool = False, omit_return_annotation: bool = False):
    """
    Generate a string signature of a function.

    :param width: Fold lines if a line is longer than this value.
    :type width: int
    :arg func_name: Override function name when given.
    :type func_name: str

    :rtype: str
    """
def move(node, line_offset) -> None:
    """
    Move the `Node` start_pos.
    """
def get_following_comment_same_line(node):
    """
    returns (as string) any comment that appears on the same line,
    after the node, including the #
    """
def is_scope(node): ...
def get_parent_scope(node, include_flows: bool = False):
    """
    Returns the underlying scope.
    """

get_cached_parent_scope: Incomplete

def get_cached_code_lines(grammar, path):
    """
    Basically access the cached code lines in parso. This is not the nicest way
    to do this, but we avoid splitting all the lines again.
    """
def get_parso_cache_node(grammar, path):
    """
    This is of course not public. But as long as I control parso, this
    shouldn't be a problem. ~ Dave

    The reason for this is mostly caching. This is obviously also a sign of a
    broken caching architecture.
    """
def cut_value_at_position(leaf, position):
    """
    Cuts of the value of the leaf at position
    """
def expr_is_dotted(node):
    """
    Checks if a path looks like `name` or `name.foo.bar` and not `name()`.
    """

function_is_staticmethod: Incomplete
function_is_classmethod: Incomplete
function_is_property: Incomplete
