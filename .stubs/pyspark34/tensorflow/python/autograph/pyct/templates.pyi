import gast
from _typeshed import Incomplete
from tensorflow.python.autograph.pyct import anno as anno, ast_util as ast_util, parser as parser, qual_names as qual_names

class ContextAdjuster(gast.NodeTransformer):
    """Adjusts the ctx field of nodes to ensure consistency.

  This transformer can change the ctx fields of a variable, tuple and other
  AST elements that allow one, based on whether the element is being read or
  written.
  """
    def __init__(self, override_value) -> None: ...
    def visit(self, node): ...
    def visit_Attribute(self, node): ...
    def visit_Tuple(self, node): ...
    def visit_List(self, node): ...
    def visit_Name(self, node): ...
    def visit_Call(self, node): ...
    def visit_Dict(self, node): ...
    def visit_Subscript(self, node): ...
    def visit_comprehension(self, node): ...
    def visit_Lambda(self, node): ...

class ReplaceTransformer(gast.NodeTransformer):
    """Replace AST nodes."""
    replacements: Incomplete
    in_replacements: bool
    preserved_annos: Incomplete
    def __init__(self, replacements) -> None:
        """Create a new ReplaceTransformer.

    Args:
      replacements: A mapping from placeholder names to (lists of) AST nodes
          that these placeholders will be replaced by.
    """
    def visit_Expr(self, node): ...
    def visit_keyword(self, node): ...
    def visit_FunctionDef(self, node): ...
    def visit_Attribute(self, node): ...
    def visit_Name(self, node): ...

def replace(template, **replacements):
    """Replaces placeholders in a Python template.

  AST Name and Tuple nodes always receive the context that inferred from
  the template. However, when replacing more complex nodes (that can potentially
  contain Name children), then the caller is responsible for setting the
  appropriate context.

  Args:
    template: A string representing Python code. Any symbol name can be used
        that appears in the template code can be used as placeholder.
    **replacements: A mapping from placeholder names to (lists of) AST nodes
        that these placeholders will be replaced by. String values are also
        supported as a shorthand for AST Name nodes with the respective ID.

  Returns:
    An AST node or list of AST nodes with the replacements made. If the
    template was a function, a list will be returned. If the template was a
    node, the same node will be returned. If the template was a string, an
    AST node will be returned (a `Module` node in the case of a multi-line
    string, an `Expr` node otherwise).

  Raises:
    ValueError: if the arguments are incorrect.
  """
def replace_as_expression(template, **replacements):
    """Variant of replace that generates expressions, instead of code blocks."""
