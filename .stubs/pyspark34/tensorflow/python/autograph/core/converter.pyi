import enum
from _typeshed import Incomplete
from tensorflow.python.autograph.pyct import anno as anno, ast_util as ast_util, parser as parser, templates as templates, transformer as transformer
from tensorflow.python.util.tf_export import tf_export as tf_export

class Feature(enum.Enum):
    """This enumeration represents optional conversion options.

  These conversion options are experimental. They are subject to change without
  notice and offer no guarantees.

  _Example Usage_

  ```python
  optionals= tf.autograph.experimental.Feature.EQUALITY_OPERATORS
  @tf.function(experimental_autograph_options=optionals)
  def f(i):
    if i == 0:  # EQUALITY_OPERATORS allows the use of == here.
      tf.print('i is zero')
  ```

  Attributes:
    ALL: Enable all features.
    AUTO_CONTROL_DEPS: Insert of control dependencies in the generated code.
    ASSERT_STATEMENTS: Convert Tensor-dependent assert statements to tf.Assert.
    BUILTIN_FUNCTIONS: Convert builtin functions applied to Tensors to
      their TF counterparts.
    EQUALITY_OPERATORS: Whether to convert the equality operator ('==') to
      tf.math.equal.
    LISTS: Convert list idioms, like initializers, slices, append, etc.
    NAME_SCOPES: Insert name scopes that name ops according to context, like the
      function they were defined in.
  """
    ALL: str
    AUTO_CONTROL_DEPS: str
    ASSERT_STATEMENTS: str
    BUILTIN_FUNCTIONS: str
    EQUALITY_OPERATORS: str
    LISTS: str
    NAME_SCOPES: str
    @classmethod
    def all(cls):
        """Returns a tuple that enables all options."""
    @classmethod
    def all_but(cls, exclude):
        """Returns a tuple that enables all but the excluded options."""

STANDARD_OPTIONS: Incomplete

class ConversionOptions:
    """Immutable container for global conversion flags.

  Attributes:
    recursive: bool, whether to recursively convert any user functions or
      classes that the converted function may use.
    user_requested: bool, whether the conversion was explicitly requested by
      the user, as opposed to being performed as a result of other logic. This
      value always auto-resets to False in child conversions.
    optional_features: Union[Feature, Set[Feature]], controls the use of
      optional features in the conversion process. See Feature for available
      options.
  """
    recursive: Incomplete
    user_requested: Incomplete
    internal_convert_user_code: Incomplete
    optional_features: Incomplete
    def __init__(self, recursive: bool = False, user_requested: bool = False, internal_convert_user_code: bool = True, optional_features=...) -> None: ...
    def as_tuple(self): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def uses(self, feature): ...
    def call_options(self):
        """Returns the corresponding options to be used for recursive conversion."""
    def to_ast(self):
        """Returns a representation of this object as an AST node.

    The AST node encodes a constructor that would create an object with the
    same contents.

    Returns:
      ast.Node
    """

class ProgramContext:
    """ProgramContext keeps track of converting function hierarchies.

  Attributes:
    options: ConversionOptions
    autograph_module: Deprecated. Do not use.
  """
    options: Incomplete
    autograph_module: Incomplete
    def __init__(self, options, autograph_module: Incomplete | None = None) -> None: ...

class Base(transformer.Base):
    """All converters should inherit from this class.

  Attributes:
    ctx: EntityContext
  """
    def __init__(self, ctx) -> None: ...
    def get_definition_directive(self, node, directive, arg, default):
        """Returns the unique directive argument for a symbol.

    See lang/directives.py for details on directives.

    Example:
       # Given a directive in the code:
       ag.foo_directive(bar, baz=1)

       # One can write for an AST node Name(id='bar'):
       get_definition_directive(node, ag.foo_directive, 'baz')

    Args:
      node: ast.AST, the node representing the symbol for which the directive
        argument is needed.
      directive: Callable[..., Any], the directive to search.
      arg: str, the directive argument to return.
      default: Any

    Raises:
      ValueError: if conflicting annotations have been found
    """
    def visit(self, node): ...
