import typing as t
from .environment import Environment as Environment
from _typeshed import Incomplete
from markupsafe import Markup

class Impossible(Exception):
    """Raised if the node could not perform a requested action."""

class NodeType(type):
    """A metaclass for nodes that handles the field and attribute
    inheritance.  fields and attributes from the parent class are
    automatically forwarded to the child."""
    def __new__(mcs, name, bases, d): ...

class EvalContext:
    """Holds evaluation time information.  Custom attributes can be attached
    to it in extensions.
    """
    environment: Incomplete
    autoescape: Incomplete
    volatile: bool
    def __init__(self, environment: Environment, template_name: str | None = None) -> None: ...
    def save(self) -> t.Mapping[str, t.Any]: ...
    def revert(self, old: t.Mapping[str, t.Any]) -> None: ...

def get_eval_context(node: Node, ctx: EvalContext | None) -> EvalContext: ...

class Node(metaclass=NodeType):
    """Baseclass for all Jinja nodes.  There are a number of nodes available
    of different types.  There are four major types:

    -   :class:`Stmt`: statements
    -   :class:`Expr`: expressions
    -   :class:`Helper`: helper nodes
    -   :class:`Template`: the outermost wrapper node

    All nodes have fields and attributes.  Fields may be other nodes, lists,
    or arbitrary values.  Fields are passed to the constructor as regular
    positional arguments, attributes as keyword arguments.  Each node has
    two attributes: `lineno` (the line number of the node) and `environment`.
    The `environment` attribute is set at the end of the parsing process for
    all nodes automatically.
    """
    fields: t.Tuple[str, ...]
    attributes: t.Tuple[str, ...]
    abstract: bool
    lineno: int
    environment: Environment | None
    def __init__(self, *fields: t.Any, **attributes: t.Any) -> None: ...
    def iter_fields(self, exclude: t.Container[str] | None = None, only: t.Container[str] | None = None) -> t.Iterator[t.Tuple[str, t.Any]]:
        """This method iterates over all fields that are defined and yields
        ``(key, value)`` tuples.  Per default all fields are returned, but
        it's possible to limit that to some fields by providing the `only`
        parameter or to exclude some using the `exclude` parameter.  Both
        should be sets or tuples of field names.
        """
    def iter_child_nodes(self, exclude: t.Container[str] | None = None, only: t.Container[str] | None = None) -> t.Iterator['Node']:
        """Iterates over all direct child nodes of the node.  This iterates
        over all fields and yields the values of they are nodes.  If the value
        of a field is a list all the nodes in that list are returned.
        """
    def find(self, node_type: t.Type[_NodeBound]) -> _NodeBound | None:
        """Find the first node of a given type.  If no such node exists the
        return value is `None`.
        """
    def find_all(self, node_type: t.Type[_NodeBound] | t.Tuple[t.Type[_NodeBound], ...]) -> t.Iterator[_NodeBound]:
        """Find all the nodes of a given type.  If the type is a tuple,
        the check is performed for any of the tuple items.
        """
    def set_ctx(self, ctx: str) -> Node:
        """Reset the context of a node and all child nodes.  Per default the
        parser will all generate nodes that have a 'load' context as it's the
        most common one.  This method is used in the parser to set assignment
        targets and other nodes to a store context.
        """
    def set_lineno(self, lineno: int, override: bool = False) -> Node:
        """Set the line numbers of the node and children."""
    def set_environment(self, environment: Environment) -> Node:
        """Set the environment for all nodes."""
    def __eq__(self, other: t.Any) -> bool: ...
    __hash__: Incomplete
    def dump(self) -> str: ...

class Stmt(Node):
    """Base node for all statements."""
    abstract: bool

class Helper(Node):
    """Nodes that exist in a specific context only."""
    abstract: bool

class Template(Node):
    """Node that represents a template.  This must be the outermost node that
    is passed to the compiler.
    """
    fields: Incomplete
    body: t.List[Node]

class Output(Stmt):
    """A node that holds multiple expressions which are then printed out.
    This is used both for the `print` statement and the regular template data.
    """
    fields: Incomplete
    nodes: t.List['Expr']

class Extends(Stmt):
    """Represents an extends statement."""
    fields: Incomplete
    template: Expr

class For(Stmt):
    """The for loop.  `target` is the target for the iteration (usually a
    :class:`Name` or :class:`Tuple`), `iter` the iterable.  `body` is a list
    of nodes that are used as loop-body, and `else_` a list of nodes for the
    `else` block.  If no else node exists it has to be an empty list.

    For filtered nodes an expression can be stored as `test`, otherwise `None`.
    """
    fields: Incomplete
    target: Node
    iter: Node
    body: t.List[Node]
    else_: t.List[Node]
    test: Node | None
    recursive: bool

class If(Stmt):
    """If `test` is true, `body` is rendered, else `else_`."""
    fields: Incomplete
    test: Node
    body: t.List[Node]
    elif_: t.List['If']
    else_: t.List[Node]

class Macro(Stmt):
    """A macro definition.  `name` is the name of the macro, `args` a list of
    arguments and `defaults` a list of defaults if there are any.  `body` is
    a list of nodes for the macro body.
    """
    fields: Incomplete
    name: str
    args: t.List['Name']
    defaults: t.List['Expr']
    body: t.List[Node]

class CallBlock(Stmt):
    """Like a macro without a name but a call instead.  `call` is called with
    the unnamed macro as `caller` argument this node holds.
    """
    fields: Incomplete
    call: Call
    args: t.List['Name']
    defaults: t.List['Expr']
    body: t.List[Node]

class FilterBlock(Stmt):
    """Node for filter sections."""
    fields: Incomplete
    body: t.List[Node]
    filter: Filter

class With(Stmt):
    """Specific node for with statements.  In older versions of Jinja the
    with statement was implemented on the base of the `Scope` node instead.

    .. versionadded:: 2.9.3
    """
    fields: Incomplete
    targets: t.List['Expr']
    values: t.List['Expr']
    body: t.List[Node]

class Block(Stmt):
    """A node that represents a block.

    .. versionchanged:: 3.0.0
        the `required` field was added.
    """
    fields: Incomplete
    name: str
    body: t.List[Node]
    scoped: bool
    required: bool

class Include(Stmt):
    """A node that represents the include tag."""
    fields: Incomplete
    template: Expr
    with_context: bool
    ignore_missing: bool

class Import(Stmt):
    """A node that represents the import tag."""
    fields: Incomplete
    template: Expr
    target: str
    with_context: bool

class FromImport(Stmt):
    """A node that represents the from import tag.  It's important to not
    pass unsafe names to the name attribute.  The compiler translates the
    attribute lookups directly into getattr calls and does *not* use the
    subscript callback of the interface.  As exported variables may not
    start with double underscores (which the parser asserts) this is not a
    problem for regular Jinja code, but if this node is used in an extension
    extra care must be taken.

    The list of names may contain tuples if aliases are wanted.
    """
    fields: Incomplete
    template: Expr
    names: t.List[str | t.Tuple[str, str]]
    with_context: bool

class ExprStmt(Stmt):
    """A statement that evaluates an expression and discards the result."""
    fields: Incomplete
    node: Node

class Assign(Stmt):
    """Assigns an expression to a target."""
    fields: Incomplete
    target: Expr
    node: Node

class AssignBlock(Stmt):
    """Assigns a block to a target."""
    fields: Incomplete
    target: Expr
    filter: Filter | None
    body: t.List[Node]

class Expr(Node):
    """Baseclass for all expressions."""
    abstract: bool
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Any:
        """Return the value of the expression as constant or raise
        :exc:`Impossible` if this was not possible.

        An :class:`EvalContext` can be provided, if none is given
        a default context is created which requires the nodes to have
        an attached environment.

        .. versionchanged:: 2.4
           the `eval_ctx` parameter was added.
        """
    def can_assign(self) -> bool:
        """Check if it's possible to assign something to this node."""

class BinExpr(Expr):
    """Baseclass for all binary expressions."""
    fields: Incomplete
    left: Expr
    right: Expr
    operator: str
    abstract: bool
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Any: ...

class UnaryExpr(Expr):
    """Baseclass for all unary expressions."""
    fields: Incomplete
    node: Expr
    operator: str
    abstract: bool
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Any: ...

class Name(Expr):
    """Looks up a name or stores a value in a name.
    The `ctx` of the node can be one of the following values:

    -   `store`: store a value in the name
    -   `load`: load that name
    -   `param`: like `store` but if the name was defined as function parameter.
    """
    fields: Incomplete
    name: str
    ctx: str
    def can_assign(self) -> bool: ...

class NSRef(Expr):
    """Reference to a namespace value assignment"""
    fields: Incomplete
    name: str
    attr: str
    def can_assign(self) -> bool: ...

class Literal(Expr):
    """Baseclass for literals."""
    abstract: bool

class Const(Literal):
    '''All constant values.  The parser will return this node for simple
    constants such as ``42`` or ``"foo"`` but it can be used to store more
    complex values such as lists too.  Only constants with a safe
    representation (objects where ``eval(repr(x)) == x`` is true).
    '''
    fields: Incomplete
    value: t.Any
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Any: ...
    @classmethod
    def from_untrusted(cls, value: t.Any, lineno: int | None = None, environment: Environment | None = None) -> Const:
        """Return a const object if the value is representable as
        constant value in the generated code, otherwise it will raise
        an `Impossible` exception.
        """

class TemplateData(Literal):
    """A constant template string."""
    fields: Incomplete
    data: str
    def as_const(self, eval_ctx: EvalContext | None = None) -> str: ...

class Tuple(Literal):
    """For loop unpacking and some other things like multiple arguments
    for subscripts.  Like for :class:`Name` `ctx` specifies if the tuple
    is used for loading the names or storing.
    """
    fields: Incomplete
    items: t.List[Expr]
    ctx: str
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Tuple[t.Any, ...]: ...
    def can_assign(self) -> bool: ...

class List(Literal):
    """Any list literal such as ``[1, 2, 3]``"""
    fields: Incomplete
    items: t.List[Expr]
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.List[t.Any]: ...

class Dict(Literal):
    """Any dict literal such as ``{1: 2, 3: 4}``.  The items must be a list of
    :class:`Pair` nodes.
    """
    fields: Incomplete
    items: t.List['Pair']
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Dict[t.Any, t.Any]: ...

class Pair(Helper):
    """A key, value pair for dicts."""
    fields: Incomplete
    key: Expr
    value: Expr
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Tuple[t.Any, t.Any]: ...

class Keyword(Helper):
    """A key, value pair for keyword arguments where key is a string."""
    fields: Incomplete
    key: str
    value: Expr
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Tuple[str, t.Any]: ...

class CondExpr(Expr):
    """A conditional expression (inline if expression).  (``{{
    foo if bar else baz }}``)
    """
    fields: Incomplete
    test: Expr
    expr1: Expr
    expr2: Expr | None
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Any: ...

def args_as_const(node: _FilterTestCommon | Call, eval_ctx: EvalContext | None) -> t.Tuple[t.List[t.Any], t.Dict[t.Any, t.Any]]: ...

class _FilterTestCommon(Expr):
    fields: Incomplete
    node: Expr
    name: str
    args: t.List[Expr]
    kwargs: t.List[Pair]
    dyn_args: Expr | None
    dyn_kwargs: Expr | None
    abstract: bool
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Any: ...

class Filter(_FilterTestCommon):
    """Apply a filter to an expression. ``name`` is the name of the
    filter, the other fields are the same as :class:`Call`.

    If ``node`` is ``None``, the filter is being used in a filter block
    and is applied to the content of the block.
    """
    node: Expr | None
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Any: ...

class Test(_FilterTestCommon):
    """Apply a test to an expression. ``name`` is the name of the test,
    the other field are the same as :class:`Call`.

    .. versionchanged:: 3.0
        ``as_const`` shares the same logic for filters and tests. Tests
        check for volatile, async, and ``@pass_context`` etc.
        decorators.
    """

class Call(Expr):
    """Calls an expression.  `args` is a list of arguments, `kwargs` a list
    of keyword arguments (list of :class:`Keyword` nodes), and `dyn_args`
    and `dyn_kwargs` has to be either `None` or a node that is used as
    node for dynamic positional (``*args``) or keyword (``**kwargs``)
    arguments.
    """
    fields: Incomplete
    node: Expr
    args: t.List[Expr]
    kwargs: t.List[Keyword]
    dyn_args: Expr | None
    dyn_kwargs: Expr | None

class Getitem(Expr):
    """Get an attribute or item from an expression and prefer the item."""
    fields: Incomplete
    node: Expr
    arg: Expr
    ctx: str
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Any: ...

class Getattr(Expr):
    """Get an attribute or item from an expression that is a ascii-only
    bytestring and prefer the attribute.
    """
    fields: Incomplete
    node: Expr
    attr: str
    ctx: str
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Any: ...

class Slice(Expr):
    """Represents a slice object.  This must only be used as argument for
    :class:`Subscript`.
    """
    fields: Incomplete
    start: Expr | None
    stop: Expr | None
    step: Expr | None
    def as_const(self, eval_ctx: EvalContext | None = None) -> slice: ...

class Concat(Expr):
    """Concatenates the list of expressions provided after converting
    them to strings.
    """
    fields: Incomplete
    nodes: t.List[Expr]
    def as_const(self, eval_ctx: EvalContext | None = None) -> str: ...

class Compare(Expr):
    """Compares an expression with some other expressions.  `ops` must be a
    list of :class:`Operand`\\s.
    """
    fields: Incomplete
    expr: Expr
    ops: t.List['Operand']
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Any: ...

class Operand(Helper):
    """Holds an operator and an expression."""
    fields: Incomplete
    op: str
    expr: Expr

class Mul(BinExpr):
    """Multiplies the left with the right node."""
    operator: str

class Div(BinExpr):
    """Divides the left by the right node."""
    operator: str

class FloorDiv(BinExpr):
    """Divides the left by the right node and converts the
    result into an integer by truncating.
    """
    operator: str

class Add(BinExpr):
    """Add the left to the right node."""
    operator: str

class Sub(BinExpr):
    """Subtract the right from the left node."""
    operator: str

class Mod(BinExpr):
    """Left modulo right."""
    operator: str

class Pow(BinExpr):
    """Left to the power of right."""
    operator: str

class And(BinExpr):
    """Short circuited AND."""
    operator: str
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Any: ...

class Or(BinExpr):
    """Short circuited OR."""
    operator: str
    def as_const(self, eval_ctx: EvalContext | None = None) -> t.Any: ...

class Not(UnaryExpr):
    """Negate the expression."""
    operator: str

class Neg(UnaryExpr):
    """Make the expression negative."""
    operator: str

class Pos(UnaryExpr):
    """Make the expression positive (noop for most expressions)"""
    operator: str

class EnvironmentAttribute(Expr):
    """Loads an attribute from the environment object.  This is useful for
    extensions that want to call a callback stored on the environment.
    """
    fields: Incomplete
    name: str

class ExtensionAttribute(Expr):
    """Returns the attribute of an extension bound to the environment.
    The identifier is the identifier of the :class:`Extension`.

    This node is usually constructed by calling the
    :meth:`~jinja2.ext.Extension.attr` method on an extension.
    """
    fields: Incomplete
    identifier: str
    name: str

class ImportedName(Expr):
    """If created with an import name the import name is returned on node
    access.  For example ``ImportedName('cgi.escape')`` returns the `escape`
    function from the cgi module on evaluation.  Imports are optimized by the
    compiler so there is no need to assign them to local variables.
    """
    fields: Incomplete
    importname: str

class InternalName(Expr):
    """An internal name in the compiler.  You cannot create these nodes
    yourself but the parser provides a
    :meth:`~jinja2.parser.Parser.free_identifier` method that creates
    a new identifier for you.  This identifier is not available from the
    template and is not treated specially by the compiler.
    """
    fields: Incomplete
    name: str
    def __init__(self) -> None: ...

class MarkSafe(Expr):
    """Mark the wrapped expression as safe (wrap it as `Markup`)."""
    fields: Incomplete
    expr: Expr
    def as_const(self, eval_ctx: EvalContext | None = None) -> Markup: ...

class MarkSafeIfAutoescape(Expr):
    """Mark the wrapped expression as safe (wrap it as `Markup`) but
    only if autoescaping is active.

    .. versionadded:: 2.5
    """
    fields: Incomplete
    expr: Expr
    def as_const(self, eval_ctx: EvalContext | None = None) -> Markup | t.Any: ...

class ContextReference(Expr):
    """Returns the current template context.  It can be used like a
    :class:`Name` node, with a ``'load'`` ctx and will return the
    current :class:`~jinja2.runtime.Context` object.

    Here an example that assigns the current template name to a
    variable named `foo`::

        Assign(Name('foo', ctx='store'),
               Getattr(ContextReference(), 'name'))

    This is basically equivalent to using the
    :func:`~jinja2.pass_context` decorator when using the high-level
    API, which causes a reference to the context to be passed as the
    first argument to a function.
    """
class DerivedContextReference(Expr):
    """Return the current template context including locals. Behaves
    exactly like :class:`ContextReference`, but includes local
    variables, such as from a ``for`` loop.

    .. versionadded:: 2.11
    """
class Continue(Stmt):
    """Continue a loop."""
class Break(Stmt):
    """Break a loop."""

class Scope(Stmt):
    """An artificial scope."""
    fields: Incomplete
    body: t.List[Node]

class OverlayScope(Stmt):
    """An overlay scope for extensions.  This is a largely unoptimized scope
    that however can be used to introduce completely arbitrary variables into
    a sub scope from a dictionary or dictionary like object.  The `context`
    field has to evaluate to a dictionary object.

    Example usage::

        OverlayScope(context=self.call_method('get_context'),
                     body=[...])

    .. versionadded:: 2.10
    """
    fields: Incomplete
    context: Expr
    body: t.List[Node]

class EvalContextModifier(Stmt):
    """Modifies the eval context.  For each option that should be modified,
    a :class:`Keyword` has to be added to the :attr:`options` list.

    Example to change the `autoescape` setting::

        EvalContextModifier(options=[Keyword('autoescape', Const(True))])
    """
    fields: Incomplete
    options: t.List[Keyword]

class ScopedEvalContextModifier(EvalContextModifier):
    """Modifies the eval context and reverts it later.  Works exactly like
    :class:`EvalContextModifier` but will only modify the
    :class:`~jinja2.nodes.EvalContext` for nodes in the :attr:`body`.
    """
    fields: Incomplete
    body: t.List[Node]
