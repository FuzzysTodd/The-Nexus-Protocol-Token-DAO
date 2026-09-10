from _typeshed import Incomplete
from pasta.base import annotate as annotate, fstring_utils as fstring_utils

class PrintError(Exception):
    """An exception for when we failed to print the tree."""

class Printer(annotate.BaseVisitor):
    """Traverses an AST and generates formatted python source code.
  
  This uses the same base visitor as annotating the AST, but instead of eating a
  token it spits one out. For special formatting information which was stored on
  the node, this is output exactly as it was read in unless one or more of the
  dependency attributes used to generate it has changed, in which case its
  default formatting is used.
  """
    code: str
    def __init__(self) -> None: ...
    def visit(self, node): ...
    def visit_Num(self, node) -> None: ...
    def visit_Str(self, node) -> None: ...
    def visit_JoinedStr(self, node) -> None: ...
    def visit_Bytes(self, node) -> None: ...
    def token(self, value) -> None: ...
    def optional_token(self, node, attr_name, token_val, allow_whitespace_prefix: bool = False, default: bool = False) -> None: ...
    def attr(self, node, attr_name, attr_vals, deps: Incomplete | None = None, default: Incomplete | None = None) -> None:
        """Add the formatted data stored for a given attribute on this node.

    If any of the dependent attributes of the node have changed since it was
    annotated, then the stored formatted data for this attr_name is no longer
    valid, and we must use the default instead.
    
    Arguments:
      node: (ast.AST) An AST node to retrieve formatting information from.
      attr_name: (string) Name to load the formatting information from.
      attr_vals: (list of functions/strings) Unused here.
      deps: (optional, set of strings) Attributes of the node which the stored
        formatting data depends on.
      default: (string) Default formatted data for this attribute.
    """
    def check_is_elif(self, node): ...
    def check_is_continued_try(self, node): ...
    def check_is_continued_with(self, node): ...

def to_str(tree):
    """Convenient function to get the python source for an AST."""
