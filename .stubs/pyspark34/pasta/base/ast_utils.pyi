import ast
from _typeshed import Incomplete
from pasta.augment import errors as errors

class _TreeNormalizer(ast.NodeTransformer):
    """Replaces all op nodes with unique instances."""
    def visit(self, node): ...

def parse(src):
    """Replaces ast.parse; ensures additional properties on the parsed tree.

  This enforces the assumption that each node in the ast is unique.
  """
def sanitize_source(src):
    """Strip the 'coding' directive from python source code, if present.

  This is a workaround for https://bugs.python.org/issue18960. Also see PEP-0263.
  """
def find_nodes_by_type(node, accept_types): ...

class FindNodeVisitor(ast.NodeVisitor):
    results: Incomplete
    def __init__(self, condition) -> None: ...
    def visit(self, node) -> None: ...

def get_last_child(node):
    """Get the last child node of a block statement.

  The input must be a block statement (e.g. ast.For, ast.With, etc).

  Examples:
    1. with first():
         second()
         last()

    2. try:
         first()
       except:
         second()
       finally:
         last()

  In both cases, the last child is the node for `last`.
  """
def remove_child(parent, child) -> None: ...
def replace_child(parent, node, replace_with) -> None:
    """Replace a node's child with another node while preserving formatting.

  Arguments:
    parent: (ast.AST) Parent node to replace a child of.
    node: (ast.AST) Child node to replace.
    replace_with: (ast.AST) New child node.
  """
def has_docstring(node): ...
