import enum
import gast
from _typeshed import Incomplete
from tensorflow.python.autograph.pyct import anno as anno, parser as parser, pretty_printer as pretty_printer, templates as templates
from typing import NamedTuple

class AnalysisLevel(enum.IntEnum):
    NONE: int
    ACTIVITY: int
    DEFINEDNESS: int
    LIVENESS: int

class Context:
    """Contains information about a source code transformation.

  This object is mutable, and is updated during conversion. Not thread safe.

  Attributes:
    info: EntityInfo, immutable.
    namer: naming.Namer.
    current_origin: origin_info.OriginInfo, holds the OriginInfo of the last
      AST node to be processed successfully. Useful for error handling.
    user: An user-supplied context object. The object is opaque to the
      infrastructure, but will pe passed through to all custom transformations.
  """
    info: Incomplete
    namer: Incomplete
    current_origin: Incomplete
    user: Incomplete
    def __init__(self, info, namer, user_context) -> None: ...

class EntityInfo(NamedTuple('EntityInfo', [('name', Incomplete), ('source_code', Incomplete), ('source_file', Incomplete), ('future_features', Incomplete), ('namespace', Incomplete)])):
    """Contains information about a Python entity.

  Immutable.

  Examples of entities include functions and classes.

  Attributes:
    name: The name that identifies this entity.
    source_code: The entity's source code.
    source_file: The entity's source file.
    future_features: Tuple[Text], the future features that this entity was
      compiled with. See
      https://docs.python.org/2/reference/simple_stmts.html#future.
    namespace: Dict[str, ], containing symbols visible to the entity (excluding
      parameters).
  """

class _StateStack:
    """Templated context manager.

  This class provides syntactic sugar for a stack of objects of known
  type. It allows accessing attributes of the object at the top of the stack
  directly against this object, which allows for very terse syntax.

  For example, this code:

    stack = _StateStack(Foo)
    stack.enter()
    stack.bar

  Is equivalent to:

    stack = []
    stack.append(Foo())
    foo = stack[-1]
    foo.bar

  See _State for more on how this is used.

  Attributes:
    type: Any, the type of objects that this stack holds
    level: int, the current stack depth
    stack: List[Any], the actual stack
    value: Any, the instance of the object at the top of the stack
  """
    def __init__(self, type_) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def enter(self) -> None: ...
    def exit(self) -> None: ...
    @property
    def stack(self): ...
    @property
    def level(self): ...
    @property
    def value(self): ...
    def __iter__(self): ...
    def __getattr__(self, key): ...
    def __setattr__(self, key, value) -> None: ...

class _State:
    """Syntactic sugar for accessing an instance of a StateStack context manager.

  This structure offers syntactic sugar over a dict of stacks of objects
  of known type. These structures are useful to keep state during AST walks.
  Multiple different scopes can be tracked in parallel. For example:

    s = _State()

    s[foo].enter()
    s[bar].enter()  # this will not affect s[foo]

  Element access has special semantics:
    * keys are a data type
    * element values are _StateStack(type=key) objects
    * missing elements are automatically added, similarly to defaultdict

  For example, the following block :

    _State s
    s[Foo]

  Is equivalent to:

    s = {}
    if Foo not in s:
      s[Foo] = Foo()
    s[Foo]

  See Base for how it's used.
  """
    def __init__(self) -> None: ...
    def __getitem__(self, key): ...

class NodeStateTracker:
    """Base class for general-purpose Python code transformation.

  This abstract class provides helpful functions, like state tracking within
  the scope of arbitrary node, helpers for processing code blocks, debugging,
  mapping of transformed code to original code, and others.

  Scope-local state tracking: to keep state across nodes, at the level of
  (possibly nested) scopes, use enter/exit_local_scope and set/get_local.
  You must call enter/exit_local_scope manually, but the transformer detects
  when they are not properly paired.

  The transformer allows keeping state across calls that is local
  to arbitrary nodes and their descendants, using the self.state attribute.
  Multiple independent scopes are allowed and automatically constructed.

  For example, to keep track of the `If` node that encloses any `Name` node,
  one can write:

  ```
    class FooType(object):

      def __init__(self):
        self.foo_property = None

    class DummyTransformer(NodeStateTracker, ast.NodeTransformer):

      def visit_If(self, node):
        self.state[FooType].enter()
        self.state[FooType].foo_property = node
        node = self.veneric_visit(node)
        self.state[FooType].exit()
        return node

      def visit_Name(self, node):
        self.state[FooType].foo_property  # will hold the innermost enclosing if
  ```

  Alternatively, the `enter()`/`exit()` calls can be managed by a `with`
  statement:

  ```
      def visit_If(self, node):
        with self.state[FooType] as foo:
          foo.foo_property = node
          return self.generic_visit(node)
  ```
  """
    ctx: Incomplete
    state: Incomplete
    def __init__(self, ctx) -> None:
        """Initialize the transformer.

    Subclasses should call this.

    Args:
      ctx: A Context object.
    """
    def debug_print(self, node):
        """Helper method useful for debugging. Prints the AST."""
    def debug_print_src(self, node):
        """Helper method useful for debugging. Prints the AST as code."""
    def visit_block(self, nodes, before_visit: Incomplete | None = None, after_visit: Incomplete | None = None):
        """A more powerful version of generic_visit for statement blocks.

    An example of a block is the body of an if statement.

    This function allows specifying a postprocessing callback (the
    after_visit argument) argument which can be used to move nodes to a new
    destination. This is done by after_visit by returning a non-null
    second return value, e.g. return new_node, new_destination.

    For example, a transformer could perform the following move:

        foo()
        bar()
        baz()

        foo()
        if cond:
          bar()
          baz()

    The above could be done with a postprocessor of this kind:

        def after_visit(node):
          if node_is_function_call(bar):
            new_container_node = build_cond()
            new_container_node.body.append(node)
            return new_container_node, new_container_node.body
          else:
            # Once we set a new destination, all subsequent items will be
            # moved to it, so we don't need to explicitly handle baz.
            return node, None

    Args:
      nodes: enumerable of AST node objects. If None, the function returns None.
      before_visit: optional callable that is called before visiting each item
        in nodes
      after_visit: optional callable that takes in an AST node and returns a
        tuple (new_node, new_destination). It is called after visiting each item
        in nodes. Is used in the same was as the
          visit_* methods: new_node will replace the node; if not None,
            new_destination must be a list, and subsequent nodes will be placed
            in this list instead of the list returned by visit_block.

    Returns:
      A list of AST node objects containing the transformed items fron nodes,
      except those nodes that have been relocated using after_visit.
    """

class Base(NodeStateTracker, gast.NodeTransformer):
    """Base class for general-purpose Python-to-Python code transformation.

  This is an extension of ast.NodeTransformer that provides the additional
  functions offered by NodeStateTracker.
  """
    def create_assignment(self, target, expression): ...
    def apply_to_single_assignments(self, targets, values, apply_fn) -> None:
        """Applies a function to each individual assignment.

    This function can process a possibly-unpacked (e.g. a, b = c, d) assignment.
    It tries to break down the unpacking if possible. In effect, it has the same
    effect as passing the assigned values in SSA form to apply_fn.

    Examples:

    The following will result in apply_fn(a, c), apply_fn(b, d):

        a, b = c, d

    The following will result in apply_fn(a, c[0]), apply_fn(b, c[1]):

        a, b = c

    The following will result in apply_fn(a, (b, c)):

        a = b, c

    It uses the visitor pattern to allow subclasses to process single
    assignments individually.

    Args:
      targets: list, tuple of or individual AST node. Should be used with the
        targets field of an ast.Assign node.
      values: an AST node.
      apply_fn: a function of a single argument, which will be called with the
        respective nodes of each single assignment. The signature is
        apply_fn(target, value), no return value.
    """
    def visit(self, node): ...

class CodeGenerator(NodeStateTracker, gast.NodeVisitor):
    """Base class for general-purpose Python-to-string code transformation.

  Similar to Base, but outputs arbitrary strings instead of a Python AST.

  This uses the same visitor mechanism that the standard NodeVisitor uses,
  meaning that subclasses write handlers for the different kinds of nodes.
  New code is generated using the emit method, which appends to a code buffer
  that can be afterwards obtained from code_buffer.

  Example:

    class SimpleCodeGen(CodeGenerator):

      def visitIf(self, node):
        self.emit('if ')
        self.visit(node.test)
        self.emit(' { ')
        self.visit(node.body)
        self.emit(' } else { ')
        self.visit(node.orelse)
        self.emit(' } ')

    node = ast.parse(...)
    gen = SimpleCodeGen()
    gen.visit(node)
    # gen.code_buffer contains the resulting code
  """
    source_map: Incomplete
    def __init__(self, ctx) -> None: ...
    def emit(self, code) -> None: ...
    @property
    def code_buffer(self): ...
    def visit(self, node): ...
