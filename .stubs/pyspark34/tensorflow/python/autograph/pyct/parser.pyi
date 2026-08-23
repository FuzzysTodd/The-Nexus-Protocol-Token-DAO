import ast
from _typeshed import Incomplete
from tensorflow.python.autograph.pyct import errors as errors, inspect_utils as inspect_utils
from tensorflow.python.util import tf_inspect as tf_inspect

PY2_PREAMBLE: Incomplete
PY3_PREAMBLE: str
MAX_SIZE: int
astunparse = ast
STANDARD_PREAMBLE = PY3_PREAMBLE
STANDARD_PREAMBLE_LEN: Incomplete

def dedent_block(code_string):
    """Dedents a code so that its first line starts at row zero."""
def parse_entity(entity, future_features):
    """Returns the AST and source code of given entity.

  Args:
    entity: Any, Python function/method/class
    future_features: Iterable[Text], future features to use (e.g.
      'print_statement'). See
      https://docs.python.org/2/reference/simple_stmts.html#future

  Returns:
    gast.AST, Text: the parsed AST node; the source code that was parsed to
    generate the AST (including any prefixes that this function may have added).
  """
def parse(src, preamble_len: int = 0, single_node: bool = True):
    """Returns the AST of given piece of code.

  Args:
    src: Text
    preamble_len: Int, indicates leading nodes in the parsed AST which should be
      dropped.
    single_node: Bool, whether `src` is assumed to be represented by exactly one
      AST node.

  Returns:
    ast.AST
  """
def parse_expression(src):
    """Returns the AST of given identifier.

  Args:
    src: A piece of code that represents a single Python expression
  Returns:
    A gast.AST object.
  Raises:
    ValueError: if src does not consist of a single Expression.
  """
def unparse(node, indentation: Incomplete | None = None, include_encoding_marker: bool = True):
    """Returns the source code of given AST.

  Args:
    node: The code to compile, as an AST object.
    indentation: Unused, deprecated. The returning code will always be indented
      at 4 spaces.
    include_encoding_marker: Bool, whether to include a comment on the first
      line to explicitly specify UTF-8 encoding.

  Returns:
    code: The source code generated from the AST object
    source_mapping: A mapping between the user and AutoGraph generated code.
  """
