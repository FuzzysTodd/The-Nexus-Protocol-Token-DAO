import abc
import mypy.strconv
import mypy.types
from _typeshed import Incomplete
from abc import abstractmethod
from collections import defaultdict
from enum import Enum
from mypy.options import Options as Options
from mypy.patterns import Pattern as Pattern
from mypy.util import short_type as short_type
from mypy.visitor import ExpressionVisitor as ExpressionVisitor, NodeVisitor as NodeVisitor, StatementVisitor as StatementVisitor
from typing import Callable, Dict, Iterator, Sequence, TypeVar
from typing_extensions import Final, TypeAlias as _TypeAlias, TypeGuard

class Context:
    """Base type for objects that are valid as error message locations."""
    line: Incomplete
    column: Incomplete
    end_line: Incomplete
    end_column: Incomplete
    def __init__(self, line: int = -1, column: int = -1) -> None: ...
    def set_line(self, target: Context | int, column: int | None = None, end_line: int | None = None, end_column: int | None = None) -> None:
        """If target is a node, pull line (and column) information
        into this node. If column is specified, this will override any column
        information coming from a node.
        """
T = TypeVar('T')
JsonDict: _TypeAlias
LDEF: Final[int]
GDEF: Final[int]
MDEF: Final[int]
UNBOUND_IMPORTED: Final[int]
REVEAL_TYPE: Final[int]
REVEAL_LOCALS: Final[int]
LITERAL_YES: Final[int]
LITERAL_TYPE: Final[int]
LITERAL_NO: Final[int]
node_kinds: Final[Incomplete]
inverse_node_kinds: Final[Incomplete]
implicit_module_attrs: Final[Incomplete]
type_aliases: Final[Incomplete]
type_aliases_source_versions: Final[Incomplete]
typing_extensions_aliases: Final[Incomplete]
reverse_builtin_aliases: Final[Incomplete]

def get_nongen_builtins(python_version: tuple[int, int]) -> dict[str, str]: ...

RUNTIME_PROTOCOL_DECOS: Final[Incomplete]

class Node(Context):
    """Common base class for all non-type parse tree nodes."""
    def str_with_options(self, options: Options) -> str: ...
    def accept(self, visitor: NodeVisitor[T]) -> T: ...

class Statement(Node):
    """A statement node."""
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class Expression(Node):
    """An expression node."""
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class FakeExpression(Expression):
    """A dummy expression.

    We need a dummy expression in one place, and can't instantiate Expression
    because it is a trait and mypyc barfs.
    """

Lvalue: _TypeAlias

class SymbolNode(Node, metaclass=abc.ABCMeta):
    """Nodes that can be stored in a symbol table."""
    @property
    @abstractmethod
    def name(self) -> str: ...
    @property
    @abstractmethod
    def fullname(self) -> str: ...
    @abstractmethod
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict) -> SymbolNode: ...

Definition: _TypeAlias

class MypyFile(SymbolNode):
    """The abstract syntax tree of a single source file."""
    __match_args__: Incomplete
    path: str
    defs: list[Statement]
    alias_deps: defaultdict[str, set[str]]
    is_bom: bool
    names: SymbolTable
    imports: list[ImportBase]
    ignored_lines: dict[int, list[str]]
    unreachable_lines: set[int]
    is_stub: bool
    is_cache_skeleton: bool
    is_partial_stub_package: bool
    plugin_deps: dict[str, set[str]]
    future_import_flags: set[str]
    line: int
    column: int
    def __init__(self, defs: list[Statement], imports: list[ImportBase], is_bom: bool = False, ignored_lines: dict[int, list[str]] | None = None) -> None: ...
    def local_definitions(self) -> Iterator[Definition]:
        """Return all definitions within the module (including nested).

        This doesn't include imported definitions.
        """
    @property
    def name(self) -> str: ...
    @property
    def fullname(self) -> str: ...
    def accept(self, visitor: NodeVisitor[T]) -> T: ...
    def is_package_init_file(self) -> bool: ...
    def is_future_flag_set(self, flag: str) -> bool: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict) -> MypyFile: ...

class ImportBase(Statement):
    """Base class for all import statements."""
    is_unreachable: bool
    is_top_level: bool
    is_mypy_only: bool
    assignments: list[AssignmentStmt]
    def __init__(self) -> None: ...

class Import(ImportBase):
    """import m [as n]"""
    __match_args__: Incomplete
    ids: list[tuple[str, str | None]]
    def __init__(self, ids: list[tuple[str, str | None]]) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class ImportFrom(ImportBase):
    """from m import x [as y], ..."""
    __match_args__: Incomplete
    id: str
    relative: int
    names: list[tuple[str, str | None]]
    def __init__(self, id: str, relative: int, names: list[tuple[str, str | None]]) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class ImportAll(ImportBase):
    """from m import *"""
    __match_args__: Incomplete
    id: str
    relative: int
    def __init__(self, id: str, relative: int) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

FUNCBASE_FLAGS: Final[Incomplete]

class FuncBase(Node, metaclass=abc.ABCMeta):
    """Abstract base class for function-like nodes.

    N.B: Although this has SymbolNode subclasses (FuncDef,
    OverloadedFuncDef), avoid calling isinstance(..., FuncBase) on
    something that is typed as SymbolNode.  This is to work around
    mypy bug #3603, in which mypy doesn't understand multiple
    inheritance very well, and will assume that a SymbolNode
    cannot be a FuncBase.

    Instead, test against SYMBOL_FUNCBASE_TYPES, which enumerates
    SymbolNode subclasses that are also FuncBase subclasses.
    """
    type: Incomplete
    unanalyzed_type: Incomplete
    info: Incomplete
    is_property: bool
    is_class: bool
    is_static: bool
    is_final: bool
    is_explicit_override: bool
    def __init__(self) -> None: ...
    @property
    @abstractmethod
    def name(self) -> str: ...
    @property
    def fullname(self) -> str: ...

OverloadPart: _TypeAlias

class OverloadedFuncDef(FuncBase, SymbolNode, Statement):
    """A logical node representing all the variants of a multi-declaration function.

    A multi-declaration function is often an @overload, but can also be a
    @property with a setter and a/or a deleter.

    This node has no explicit representation in the source program.
    Overloaded variants must be consecutive in the source file.
    """
    items: list[OverloadPart]
    unanalyzed_items: list[OverloadPart]
    impl: OverloadPart | None
    is_final: bool
    def __init__(self, items: list[OverloadPart]) -> None: ...
    @property
    def name(self) -> str: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict) -> OverloadedFuncDef: ...

class Argument(Node):
    """A single argument in a FuncItem."""
    __match_args__: Incomplete
    variable: Incomplete
    type_annotation: Incomplete
    initializer: Incomplete
    kind: Incomplete
    pos_only: Incomplete
    def __init__(self, variable: Var, type_annotation: mypy.types.Type | None, initializer: Expression | None, kind: ArgKind, pos_only: bool = False) -> None: ...
    def set_line(self, target: Context | int, column: int | None = None, end_line: int | None = None, end_column: int | None = None) -> None: ...

FUNCITEM_FLAGS: Final[Incomplete]

class FuncItem(FuncBase, metaclass=abc.ABCMeta):
    """Base class for nodes usable as overloaded function items."""
    __deletable__: Incomplete
    arguments: Incomplete
    arg_names: Incomplete
    arg_kinds: Incomplete
    max_pos: Incomplete
    body: Incomplete
    type: Incomplete
    unanalyzed_type: Incomplete
    is_overload: bool
    is_generator: bool
    is_coroutine: bool
    is_async_generator: bool
    is_awaitable_coroutine: bool
    expanded: Incomplete
    min_args: int
    def __init__(self, arguments: list[Argument] | None = None, body: Block | None = None, typ: mypy.types.FunctionLike | None = None) -> None: ...
    def max_fixed_argc(self) -> int: ...
    def is_dynamic(self) -> bool: ...

FUNCDEF_FLAGS: Final[Incomplete]
NOT_ABSTRACT: Final[int]
IS_ABSTRACT: Final[int]
IMPLICITLY_ABSTRACT: Final[int]

class FuncDef(FuncItem, SymbolNode, Statement):
    """Function definition.

    This is a non-lambda function defined using 'def'.
    """
    __match_args__: Incomplete
    is_decorated: bool
    is_conditional: bool
    abstract_status: Incomplete
    is_trivial_body: bool
    is_final: bool
    original_def: Incomplete
    deco_line: Incomplete
    is_mypy_only: bool
    dataclass_transform_spec: Incomplete
    def __init__(self, name: str = '', arguments: list[Argument] | None = None, body: Block | None = None, typ: mypy.types.FunctionLike | None = None) -> None: ...
    @property
    def name(self) -> str: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict) -> FuncDef: ...

SYMBOL_FUNCBASE_TYPES: Incomplete

class Decorator(SymbolNode, Statement):
    """A decorated function.

    A single Decorator object can include any number of function decorators.
    """
    __match_args__: Incomplete
    func: FuncDef
    decorators: list[Expression]
    original_decorators: list[Expression]
    var: Var
    is_overload: bool
    def __init__(self, func: FuncDef, decorators: list[Expression], var: Var) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def fullname(self) -> str: ...
    @property
    def is_final(self) -> bool: ...
    @property
    def info(self) -> TypeInfo: ...
    @property
    def type(self) -> mypy.types.Type | None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict) -> Decorator: ...

VAR_FLAGS: Final[Incomplete]

class Var(SymbolNode):
    """A variable.

    It can refer to global/local variable or a data attribute.
    """
    __match_args__: Incomplete
    info: Incomplete
    type: Incomplete
    is_self: bool
    is_cls: bool
    is_ready: bool
    is_inferred: Incomplete
    is_initialized_in_class: bool
    is_staticmethod: bool
    is_classmethod: bool
    is_property: bool
    is_settable_property: bool
    is_classvar: bool
    is_abstract_var: bool
    is_suppressed_import: bool
    is_final: bool
    final_value: Incomplete
    final_unset_in_class: bool
    final_set_in_init: bool
    explicit_self_type: bool
    from_module_getattr: bool
    has_explicit_value: bool
    allow_incompatible_override: bool
    invalid_partial_type: bool
    def __init__(self, name: str, type: mypy.types.Type | None = None) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def fullname(self) -> str: ...
    def accept(self, visitor: NodeVisitor[T]) -> T: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict) -> Var: ...

class ClassDef(Statement):
    """Class definition"""
    __match_args__: Incomplete
    name: str
    defs: Block
    type_vars: list[mypy.types.TypeVarLikeType]
    base_type_exprs: list[Expression]
    removed_base_type_exprs: list[Expression]
    info: TypeInfo
    metaclass: Expression | None
    decorators: list[Expression]
    keywords: dict[str, Expression]
    analyzed: Expression | None
    has_incompatible_baseclass: bool
    removed_statements: list[Statement]
    deco_line: Incomplete
    def __init__(self, name: str, defs: Block, type_vars: list[mypy.types.TypeVarLikeType] | None = None, base_type_exprs: list[Expression] | None = None, metaclass: Expression | None = None, keywords: list[tuple[str, Expression]] | None = None) -> None: ...
    @property
    def fullname(self) -> str: ...
    @fullname.setter
    def fullname(self, v: str) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...
    def is_generic(self) -> bool: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(self, data: JsonDict) -> ClassDef: ...

class GlobalDecl(Statement):
    """Declaration global x, y, ..."""
    __match_args__: Incomplete
    names: list[str]
    def __init__(self, names: list[str]) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class NonlocalDecl(Statement):
    """Declaration nonlocal x, y, ..."""
    __match_args__: Incomplete
    names: list[str]
    def __init__(self, names: list[str]) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class Block(Statement):
    __match_args__: Incomplete
    body: Incomplete
    is_unreachable: bool
    def __init__(self, body: list[Statement]) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class ExpressionStmt(Statement):
    """An expression as a statement, such as print(s)."""
    __match_args__: Incomplete
    expr: Expression
    def __init__(self, expr: Expression) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class AssignmentStmt(Statement):
    '''Assignment statement.

    The same node class is used for single assignment, multiple assignment
    (e.g. x, y = z) and chained assignment (e.g. x = y = z), assignments
    that define new names, and assignments with explicit types ("# type: t"
    or "x: t [= ...]").

    An lvalue can be NameExpr, TupleExpr, ListExpr, MemberExpr, or IndexExpr.
    '''
    __match_args__: Incomplete
    lvalues: list[Lvalue]
    rvalue: Expression
    type: mypy.types.Type | None
    unanalyzed_type: mypy.types.Type | None
    new_syntax: bool
    is_alias_def: bool
    is_final_def: bool
    invalid_recursive_alias: bool
    def __init__(self, lvalues: list[Lvalue], rvalue: Expression, type: mypy.types.Type | None = None, new_syntax: bool = False) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class OperatorAssignmentStmt(Statement):
    """Operator assignment statement such as x += 1"""
    __match_args__: Incomplete
    op: str
    lvalue: Lvalue
    rvalue: Expression
    def __init__(self, op: str, lvalue: Lvalue, rvalue: Expression) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class WhileStmt(Statement):
    __match_args__: Incomplete
    expr: Expression
    body: Block
    else_body: Block | None
    def __init__(self, expr: Expression, body: Block, else_body: Block | None) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class ForStmt(Statement):
    __match_args__: Incomplete
    index: Lvalue
    index_type: mypy.types.Type | None
    unanalyzed_index_type: mypy.types.Type | None
    inferred_item_type: mypy.types.Type | None
    inferred_iterator_type: mypy.types.Type | None
    expr: Expression
    body: Block
    else_body: Block | None
    is_async: bool
    def __init__(self, index: Lvalue, expr: Expression, body: Block, else_body: Block | None, index_type: mypy.types.Type | None = None) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class ReturnStmt(Statement):
    __match_args__: Incomplete
    expr: Expression | None
    def __init__(self, expr: Expression | None) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class AssertStmt(Statement):
    __match_args__: Incomplete
    expr: Expression
    msg: Expression | None
    def __init__(self, expr: Expression, msg: Expression | None = None) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class DelStmt(Statement):
    __match_args__: Incomplete
    expr: Lvalue
    def __init__(self, expr: Lvalue) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class BreakStmt(Statement):
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class ContinueStmt(Statement):
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class PassStmt(Statement):
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class IfStmt(Statement):
    __match_args__: Incomplete
    expr: list[Expression]
    body: list[Block]
    else_body: Block | None
    def __init__(self, expr: list[Expression], body: list[Block], else_body: Block | None) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class RaiseStmt(Statement):
    __match_args__: Incomplete
    expr: Expression | None
    from_expr: Expression | None
    def __init__(self, expr: Expression | None, from_expr: Expression | None) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class TryStmt(Statement):
    __match_args__: Incomplete
    body: Block
    types: list[Expression | None]
    vars: list[NameExpr | None]
    handlers: list[Block]
    else_body: Block | None
    finally_body: Block | None
    is_star: bool
    def __init__(self, body: Block, vars: list[NameExpr | None], types: list[Expression | None], handlers: list[Block], else_body: Block | None, finally_body: Block | None) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class WithStmt(Statement):
    __match_args__: Incomplete
    expr: list[Expression]
    target: list[Lvalue | None]
    unanalyzed_type: mypy.types.Type | None
    analyzed_types: list[mypy.types.Type]
    body: Block
    is_async: bool
    def __init__(self, expr: list[Expression], target: list[Lvalue | None], body: Block, target_type: mypy.types.Type | None = None) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class MatchStmt(Statement):
    __match_args__: Incomplete
    subject: Expression
    patterns: list[Pattern]
    guards: list[Expression | None]
    bodies: list[Block]
    def __init__(self, subject: Expression, patterns: list[Pattern], guards: list[Expression | None], bodies: list[Block]) -> None: ...
    def accept(self, visitor: StatementVisitor[T]) -> T: ...

class IntExpr(Expression):
    """Integer literal"""
    __match_args__: Incomplete
    value: int
    def __init__(self, value: int) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class StrExpr(Expression):
    """String literal"""
    __match_args__: Incomplete
    value: str
    def __init__(self, value: str) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

def is_StrExpr_list(seq: list[Expression]) -> TypeGuard[list[StrExpr]]: ...

class BytesExpr(Expression):
    """Bytes literal"""
    __match_args__: Incomplete
    value: str
    def __init__(self, value: str) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class FloatExpr(Expression):
    """Float literal"""
    __match_args__: Incomplete
    value: float
    def __init__(self, value: float) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class ComplexExpr(Expression):
    """Complex literal"""
    __match_args__: Incomplete
    value: complex
    def __init__(self, value: complex) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class EllipsisExpr(Expression):
    """Ellipsis (...)"""
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class StarExpr(Expression):
    """Star expression"""
    __match_args__: Incomplete
    expr: Expression
    valid: bool
    def __init__(self, expr: Expression) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class RefExpr(Expression):
    """Abstract base class for name-like constructs"""
    kind: Incomplete
    node: Incomplete
    is_new_def: bool
    is_inferred_def: bool
    is_alias_rvalue: bool
    type_guard: Incomplete
    def __init__(self) -> None: ...
    @property
    def fullname(self) -> str: ...
    @fullname.setter
    def fullname(self, v: str) -> None: ...

class NameExpr(RefExpr):
    """Name expression

    This refers to a local name, global name or a module.
    """
    __match_args__: Incomplete
    name: Incomplete
    is_special_form: bool
    def __init__(self, name: str) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...
    def serialize(self) -> JsonDict: ...

class MemberExpr(RefExpr):
    """Member access expression x.y"""
    __match_args__: Incomplete
    expr: Incomplete
    name: Incomplete
    def_var: Incomplete
    def __init__(self, expr: Expression, name: str) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class ArgKind(Enum):
    ARG_POS: int
    ARG_OPT: int
    ARG_STAR: int
    ARG_NAMED: int
    ARG_STAR2: int
    ARG_NAMED_OPT: int
    def is_positional(self, star: bool = False) -> bool: ...
    def is_named(self, star: bool = False) -> bool: ...
    def is_required(self) -> bool: ...
    def is_optional(self) -> bool: ...
    def is_star(self) -> bool: ...

ARG_POS: Final[Incomplete]
ARG_OPT: Final[Incomplete]
ARG_STAR: Final[Incomplete]
ARG_NAMED: Final[Incomplete]
ARG_STAR2: Final[Incomplete]
ARG_NAMED_OPT: Final[Incomplete]

class CallExpr(Expression):
    """Call expression.

    This can also represent several special forms that are syntactically calls
    such as cast(...) and None  # type: ....
    """
    __match_args__: Incomplete
    callee: Incomplete
    args: Incomplete
    arg_kinds: Incomplete
    arg_names: Incomplete
    analyzed: Incomplete
    def __init__(self, callee: Expression, args: list[Expression], arg_kinds: list[ArgKind], arg_names: list[str | None], analyzed: Expression | None = None) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class YieldFromExpr(Expression):
    __match_args__: Incomplete
    expr: Expression
    def __init__(self, expr: Expression) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class YieldExpr(Expression):
    __match_args__: Incomplete
    expr: Expression | None
    def __init__(self, expr: Expression | None) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class IndexExpr(Expression):
    """Index expression x[y].

    Also wraps type application such as List[int] as a special form.
    """
    __match_args__: Incomplete
    base: Expression
    index: Expression
    method_type: mypy.types.Type | None
    analyzed: TypeApplication | TypeAliasExpr | None
    def __init__(self, base: Expression, index: Expression) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class UnaryExpr(Expression):
    """Unary operation"""
    __match_args__: Incomplete
    op: str
    expr: Expression
    method_type: mypy.types.Type | None
    def __init__(self, op: str, expr: Expression) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class AssignmentExpr(Expression):
    '''Assignment expressions in Python 3.8+, like "a := 2".'''
    __match_args__: Incomplete
    target: Incomplete
    value: Incomplete
    def __init__(self, target: Expression, value: Expression) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class OpExpr(Expression):
    """Binary operation.

    The dot (.), [] and comparison operators have more specific nodes.
    """
    __match_args__: Incomplete
    op: str
    left: Expression
    right: Expression
    method_type: mypy.types.Type | None
    right_always: bool
    right_unreachable: bool
    analyzed: TypeAliasExpr | None
    def __init__(self, op: str, left: Expression, right: Expression, analyzed: TypeAliasExpr | None = None) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class ComparisonExpr(Expression):
    """Comparison expression (e.g. a < b > c < d)."""
    __match_args__: Incomplete
    operators: list[str]
    operands: list[Expression]
    method_types: list[mypy.types.Type | None]
    def __init__(self, operators: list[str], operands: list[Expression]) -> None: ...
    def pairwise(self) -> Iterator[tuple[str, Expression, Expression]]:
        '''If this comparison expr is "a < b is c == d", yields the sequence
        ("<", a, b), ("is", b, c), ("==", c, d)
        '''
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class SliceExpr(Expression):
    """Slice expression (e.g. 'x:y', 'x:', '::2' or ':').

    This is only valid as index in index expressions.
    """
    __match_args__: Incomplete
    begin_index: Expression | None
    end_index: Expression | None
    stride: Expression | None
    def __init__(self, begin_index: Expression | None, end_index: Expression | None, stride: Expression | None) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class CastExpr(Expression):
    """Cast expression cast(type, expr)."""
    __match_args__: Incomplete
    expr: Expression
    type: mypy.types.Type
    def __init__(self, expr: Expression, typ: mypy.types.Type) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class AssertTypeExpr(Expression):
    """Represents a typing.assert_type(expr, type) call."""
    __match_args__: Incomplete
    expr: Expression
    type: mypy.types.Type
    def __init__(self, expr: Expression, typ: mypy.types.Type) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class RevealExpr(Expression):
    """Reveal type expression reveal_type(expr) or reveal_locals() expression."""
    __match_args__: Incomplete
    expr: Expression | None
    kind: int
    local_nodes: list[Var] | None
    def __init__(self, kind: int, expr: Expression | None = None, local_nodes: list[Var] | None = None) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class SuperExpr(Expression):
    """Expression super().name"""
    __match_args__: Incomplete
    name: str
    info: TypeInfo | None
    call: CallExpr
    def __init__(self, name: str, call: CallExpr) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class LambdaExpr(FuncItem, Expression):
    """Lambda expression"""
    __match_args__: Incomplete
    @property
    def name(self) -> str: ...
    def expr(self) -> Expression:
        """Return the expression (the body) of the lambda."""
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...
    def is_dynamic(self) -> bool: ...

class ListExpr(Expression):
    """List literal expression [...]."""
    __match_args__: Incomplete
    items: list[Expression]
    def __init__(self, items: list[Expression]) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class DictExpr(Expression):
    """Dictionary literal expression {key: value, ...}."""
    __match_args__: Incomplete
    items: list[tuple[Expression | None, Expression]]
    def __init__(self, items: list[tuple[Expression | None, Expression]]) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class TupleExpr(Expression):
    """Tuple literal expression (..., ...)

    Also lvalue sequences (..., ...) and [..., ...]"""
    __match_args__: Incomplete
    items: list[Expression]
    def __init__(self, items: list[Expression]) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class SetExpr(Expression):
    """Set literal expression {value, ...}."""
    __match_args__: Incomplete
    items: list[Expression]
    def __init__(self, items: list[Expression]) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class GeneratorExpr(Expression):
    """Generator expression ... for ... in ... [ for ...  in ... ] [ if ... ]."""
    __match_args__: Incomplete
    left_expr: Expression
    sequences: list[Expression]
    condlists: list[list[Expression]]
    is_async: list[bool]
    indices: list[Lvalue]
    def __init__(self, left_expr: Expression, indices: list[Lvalue], sequences: list[Expression], condlists: list[list[Expression]], is_async: list[bool]) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class ListComprehension(Expression):
    """List comprehension (e.g. [x + 1 for x in a])"""
    __match_args__: Incomplete
    generator: GeneratorExpr
    def __init__(self, generator: GeneratorExpr) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class SetComprehension(Expression):
    """Set comprehension (e.g. {x + 1 for x in a})"""
    __match_args__: Incomplete
    generator: GeneratorExpr
    def __init__(self, generator: GeneratorExpr) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class DictionaryComprehension(Expression):
    """Dictionary comprehension (e.g. {k: v for k, v in a}"""
    __match_args__: Incomplete
    key: Expression
    value: Expression
    sequences: list[Expression]
    condlists: list[list[Expression]]
    is_async: list[bool]
    indices: list[Lvalue]
    def __init__(self, key: Expression, value: Expression, indices: list[Lvalue], sequences: list[Expression], condlists: list[list[Expression]], is_async: list[bool]) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class ConditionalExpr(Expression):
    """Conditional expression (e.g. x if y else z)"""
    __match_args__: Incomplete
    cond: Expression
    if_expr: Expression
    else_expr: Expression
    def __init__(self, cond: Expression, if_expr: Expression, else_expr: Expression) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class TypeApplication(Expression):
    """Type application expr[type, ...]"""
    __match_args__: Incomplete
    expr: Expression
    types: list[mypy.types.Type]
    def __init__(self, expr: Expression, types: list[mypy.types.Type]) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

INVARIANT: Final[int]
COVARIANT: Final[int]
CONTRAVARIANT: Final[int]

class TypeVarLikeExpr(SymbolNode, Expression, metaclass=abc.ABCMeta):
    """Base class for TypeVarExpr, ParamSpecExpr and TypeVarTupleExpr.

    Note that they are constructed by the semantic analyzer.
    """
    upper_bound: mypy.types.Type
    default: mypy.types.Type
    variance: int
    def __init__(self, name: str, fullname: str, upper_bound: mypy.types.Type, default: mypy.types.Type, variance: int = ...) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def fullname(self) -> str: ...

class TypeVarExpr(TypeVarLikeExpr):
    """Type variable expression TypeVar(...).

    This is also used to represent type variables in symbol tables.

    A type variable is not valid as a type unless bound in a TypeVarLikeScope.
    That happens within:

     1. a generic class that uses the type variable as a type argument or
     2. a generic function that refers to the type variable in its signature.
    """
    __match_args__: Incomplete
    values: list[mypy.types.Type]
    def __init__(self, name: str, fullname: str, values: list[mypy.types.Type], upper_bound: mypy.types.Type, default: mypy.types.Type, variance: int = ...) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict) -> TypeVarExpr: ...

class ParamSpecExpr(TypeVarLikeExpr):
    __match_args__: Incomplete
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict) -> ParamSpecExpr: ...

class TypeVarTupleExpr(TypeVarLikeExpr):
    """Type variable tuple expression TypeVarTuple(...)."""
    tuple_fallback: mypy.types.Instance
    __match_args__: Incomplete
    def __init__(self, name: str, fullname: str, upper_bound: mypy.types.Type, tuple_fallback: mypy.types.Instance, default: mypy.types.Type, variance: int = ...) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict) -> TypeVarTupleExpr: ...

class TypeAliasExpr(Expression):
    """Type alias expression (rvalue)."""
    __match_args__: Incomplete
    type: mypy.types.Type
    tvars: list[str]
    no_args: bool
    node: TypeAlias
    def __init__(self, node: TypeAlias) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class NamedTupleExpr(Expression):
    """Named tuple expression namedtuple(...) or NamedTuple(...)."""
    __match_args__: Incomplete
    info: TypeInfo
    is_typed: bool
    def __init__(self, info: TypeInfo, is_typed: bool = False) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class TypedDictExpr(Expression):
    """Typed dict expression TypedDict(...)."""
    __match_args__: Incomplete
    info: TypeInfo
    def __init__(self, info: TypeInfo) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class EnumCallExpr(Expression):
    """Named tuple expression Enum('name', 'val1 val2 ...')."""
    __match_args__: Incomplete
    info: TypeInfo
    items: list[str]
    values: list[Expression | None]
    def __init__(self, info: TypeInfo, items: list[str], values: list[Expression | None]) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class PromoteExpr(Expression):
    """Ducktype class decorator expression _promote(...)."""
    type: mypy.types.ProperType
    def __init__(self, type: mypy.types.ProperType) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class NewTypeExpr(Expression):
    """NewType expression NewType(...)."""
    __match_args__: Incomplete
    name: str
    old_type: mypy.types.Type | None
    info: TypeInfo | None
    def __init__(self, name: str, old_type: mypy.types.Type | None, line: int, column: int) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class AwaitExpr(Expression):
    """Await expression (await ...)."""
    __match_args__: Incomplete
    expr: Expression
    def __init__(self, expr: Expression) -> None: ...
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class TempNode(Expression):
    """Temporary dummy node used during type checking.

    This node is not present in the original program; it is just an artifact
    of the type checker implementation. It only represents an opaque node with
    some fixed type.
    """
    type: mypy.types.Type
    no_rhs: bool
    line: Incomplete
    column: Incomplete
    def __init__(self, typ: mypy.types.Type, no_rhs: bool = False, *, context: Context | None = None) -> None:
        """Construct a dummy node; optionally borrow line/column from context object."""
    def accept(self, visitor: ExpressionVisitor[T]) -> T: ...

class TypeInfo(SymbolNode):
    '''The type structure of a single class.

    Each TypeInfo corresponds one-to-one to a ClassDef, which
    represents the AST of the class.

    In type-theory terms, this is a "type constructor", and if the
    class is generic then it will be a type constructor of higher kind.
    Where the class is used in an actual type, it\'s in the form of an
    Instance, which amounts to a type application of the tycon to
    the appropriate number of arguments.
    '''
    module_name: str
    defn: ClassDef
    mro: list[TypeInfo]
    bad_mro: bool
    is_final: bool
    declared_metaclass: mypy.types.Instance | None
    metaclass_type: mypy.types.Instance | None
    names: SymbolTable
    is_abstract: bool
    is_protocol: bool
    runtime_protocol: bool
    abstract_attributes: list[tuple[str, int]]
    deletable_attributes: list[str]
    slots: set[str] | None
    assuming: list[tuple[mypy.types.Instance, mypy.types.Instance]]
    assuming_proper: list[tuple[mypy.types.Instance, mypy.types.Instance]]
    inferring: list[mypy.types.Instance]
    is_enum: bool
    fallback_to_any: bool
    meta_fallback_to_any: bool
    type_vars: list[str]
    has_param_spec_type: bool
    bases: list[mypy.types.Instance]
    alt_promote: mypy.types.Instance | None
    tuple_type: mypy.types.TupleType | None
    is_named_tuple: bool
    typeddict_type: mypy.types.TypedDictType | None
    is_newtype: bool
    is_intersection: bool
    metadata: dict[str, JsonDict]
    special_alias: TypeAlias | None
    self_type: mypy.types.TypeVarType | None
    dataclass_transform_spec: DataclassTransformSpec | None
    FLAGS: Final[Incomplete]
    has_type_var_tuple_type: bool
    type_var_tuple_prefix: Incomplete
    type_var_tuple_suffix: Incomplete
    def __init__(self, names: SymbolTable, defn: ClassDef, module_name: str) -> None:
        """Initialize a TypeInfo."""
    def add_type_vars(self) -> None: ...
    @property
    def name(self) -> str:
        """Short name."""
    @property
    def fullname(self) -> str: ...
    def is_generic(self) -> bool:
        """Is the type generic (i.e. does it have type variables)?"""
    def get(self, name: str) -> SymbolTableNode | None: ...
    def get_containing_type_info(self, name: str) -> TypeInfo | None: ...
    @property
    def protocol_members(self) -> list[str]: ...
    def __getitem__(self, name: str) -> SymbolTableNode: ...
    def __bool__(self) -> bool: ...
    def has_readable_member(self, name: str) -> bool: ...
    def get_method(self, name: str) -> FuncBase | Decorator | None: ...
    def calculate_metaclass_type(self) -> mypy.types.Instance | None: ...
    def is_metaclass(self) -> bool: ...
    def has_base(self, fullname: str) -> bool:
        """Return True if type has a base type with the specified name.

        This can be either via extension or via implementation.
        """
    def direct_base_classes(self) -> list[TypeInfo]:
        """Return a direct base classes.

        Omit base classes of other base classes.
        """
    def update_tuple_type(self, typ: mypy.types.TupleType) -> None:
        """Update tuple_type and special_alias as needed."""
    def update_typeddict_type(self, typ: mypy.types.TypedDictType) -> None:
        """Update typeddict_type and special_alias as needed."""
    def dump(self, str_conv: mypy.strconv.StrConv, type_str_conv: mypy.types.TypeStrVisitor) -> str:
        """Return a string dump of the contents of the TypeInfo."""
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict) -> TypeInfo: ...

class FakeInfo(TypeInfo):
    msg: Incomplete
    def __init__(self, msg: str) -> None: ...
    def __getattribute__(self, attr: str) -> type: ...

VAR_NO_INFO: Final[TypeInfo]
CLASSDEF_NO_INFO: Final[TypeInfo]
FUNC_NO_INFO: Final[TypeInfo]

class TypeAlias(SymbolNode):
    """
    A symbol node representing a type alias.

    Type alias is a static concept, in contrast to variables with types
    like Type[...]. Namely:
        * type aliases
            - can be used in type context (annotations)
            - cannot be re-assigned
        * variables with type Type[...]
            - cannot be used in type context
            - but can be re-assigned

    An alias can be defined only by an assignment to a name (not any other lvalues).

    Such assignment defines an alias by default. To define a variable,
    an explicit Type[...] annotation is required. As an exception,
    at non-global scope non-subscripted rvalue creates a variable even without
    an annotation. This exception exists to accommodate the common use case of
    class-valued attributes. See SemanticAnalyzerPass2.check_and_set_up_type_alias
    for details.

    Aliases can be generic. We use bound type variables for generic aliases, similar
    to classes. Essentially, type aliases work as macros that expand textually.
    The definition and expansion rules are following:

        1. An alias targeting a generic class without explicit variables act as
        the given class (this doesn't apply to TypedDict, Tuple and Callable, which
        are not proper classes but special type constructors):

            A = List
            AA = List[Any]

            x: A  # same as List[Any]
            x: A[int]  # same as List[int]

            x: AA  # same as List[Any]
            x: AA[int]  # Error!

            C = Callable  # Same as Callable[..., Any]
            T = Tuple  # Same as Tuple[Any, ...]

        2. An alias using explicit type variables in its rvalue expects
        replacements (type arguments) for these variables. If missing, they
        are treated as Any, like for other generics:

            B = List[Tuple[T, T]]

            x: B  # same as List[Tuple[Any, Any]]
            x: B[int]  # same as List[Tuple[int, int]]

            def f(x: B[T]) -> T: ...  # without T, Any would be used here

        3. An alias can be defined using another aliases. In the definition
        rvalue the Any substitution doesn't happen for top level unsubscripted
        generic classes:

            A = List
            B = A  # here A is expanded to List, _not_ List[Any],
                   # to match the Python runtime behaviour
            x: B[int]  # same as List[int]
            C = List[A]  # this expands to List[List[Any]]

            AA = List[T]
            D = AA  # here AA expands to List[Any]
            x: D[int]  # Error!

    Note: the fact that we support aliases like `A = List` means that the target
    type will be initially an instance type with wrong number of type arguments.
    Such instances are all fixed either during or after main semantic analysis passes.
    We therefore store the difference between `List` and `List[Any]` rvalues (targets)
    using the `no_args` flag. See also TypeAliasExpr.no_args.

    Meaning of other fields:

    target: The target type. For generic aliases contains bound type variables
        as nested types (currently TypeVar and ParamSpec are supported).
    _fullname: Qualified name of this type alias. This is used in particular
        to track fine grained dependencies from aliases.
    alias_tvars: Type variables used to define this alias.
    normalized: Used to distinguish between `A = List`, and `A = list`. Both
        are internally stored using `builtins.list` (because `typing.List` is
        itself an alias), while the second cannot be subscripted because of
        Python runtime limitation.
    line and column: Line and column on the original alias definition.
    eager: If True, immediately expand alias when referred to (useful for aliases
        within functions that can't be looked up from the symbol table)
    """
    __match_args__: Incomplete
    target: Incomplete
    alias_tvars: Incomplete
    no_args: Incomplete
    normalized: Incomplete
    eager: Incomplete
    tvar_tuple_index: Incomplete
    def __init__(self, target: mypy.types.Type, fullname: str, line: int, column: int, *, alias_tvars: list[mypy.types.TypeVarLikeType] | None = None, no_args: bool = False, normalized: bool = False, eager: bool = False) -> None: ...
    @classmethod
    def from_tuple_type(cls, info: TypeInfo) -> TypeAlias:
        """Generate an alias to the tuple type described by a given TypeInfo.

        NOTE: this doesn't set type alias type variables (for generic tuple types),
        they must be set by the caller (when fully analyzed).
        """
    @classmethod
    def from_typeddict_type(cls, info: TypeInfo) -> TypeAlias:
        """Generate an alias to the TypedDict type described by a given TypeInfo.

        NOTE: this doesn't set type alias type variables (for generic TypedDicts),
        they must be set by the caller (when fully analyzed).
        """
    @property
    def name(self) -> str: ...
    @property
    def fullname(self) -> str: ...
    @property
    def has_param_spec_type(self) -> bool: ...
    def serialize(self) -> JsonDict: ...
    def accept(self, visitor: NodeVisitor[T]) -> T: ...
    @classmethod
    def deserialize(cls, data: JsonDict) -> TypeAlias: ...

class PlaceholderNode(SymbolNode):
    """Temporary symbol node that will later become a real SymbolNode.

    These are only present during semantic analysis when using the new
    semantic analyzer. These are created if some essential dependencies
    of a definition are not yet complete.

    A typical use is for names imported from a module which is still
    incomplete (within an import cycle):

      from m import f  # Initially may create PlaceholderNode

    This is particularly important if the imported shadows a name from
    an enclosing scope or builtins:

      from m import int  # Placeholder avoids mixups with builtins.int

    Another case where this is useful is when there is another definition
    or assignment:

      from m import f
      def f() -> None: ...

    In the above example, the presence of PlaceholderNode allows us to
    handle the second definition as a redefinition.

    They are also used to create PlaceholderType instances for types
    that refer to incomplete types. Example:

      class C(Sequence[C]): ...

    We create a PlaceholderNode (with becomes_typeinfo=True) for C so
    that the type C in Sequence[C] can be bound.

    Attributes:

      fullname: Full name of the PlaceholderNode.
      node: AST node that contains the definition that caused this to
          be created. This is useful for tracking order of incomplete definitions
          and for debugging.
      becomes_typeinfo: If True, this refers something that could later
          become a TypeInfo. It can't be used with type variables, in
          particular, as this would cause issues with class type variable
          detection.

    The long-term purpose of placeholder nodes/types is to evolve into
    something that can support general recursive types.
    """
    node: Incomplete
    becomes_typeinfo: Incomplete
    line: Incomplete
    def __init__(self, fullname: str, node: Node, line: int, *, becomes_typeinfo: bool = False) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def fullname(self) -> str: ...
    def serialize(self) -> JsonDict: ...
    def accept(self, visitor: NodeVisitor[T]) -> T: ...

class SymbolTableNode:
    """Description of a name binding in a symbol table.

    These are only used as values in module (global), function (local)
    and class symbol tables (see SymbolTable). The name that is bound is
    the key in SymbolTable.

    Symbol tables don't contain direct references to AST nodes primarily
    because there can be multiple symbol table references to a single
    AST node (due to imports and aliases), and different references can
    behave differently. This class describes the unique properties of
    each reference.

    The most fundamental attribute is 'node', which is the AST node that
    the name refers to.

    The kind is usually one of LDEF, GDEF or MDEF, depending on the scope
    of the definition. These three kinds can usually be used
    interchangeably and the difference between local, global and class
    scopes is mostly descriptive, with no semantic significance.
    However, some tools that consume mypy ASTs may care about these so
    they should be correct.

    Attributes:
        node: AST node of definition. Among others, this can be one of
            FuncDef, Var, TypeInfo, TypeVarExpr or MypyFile -- or None
            for cross_ref that hasn't been fixed up yet.
        kind: Kind of node. Possible values:
               - LDEF: local definition
               - GDEF: global (module-level) definition
               - MDEF: class member definition
               - UNBOUND_IMPORTED: temporary kind for imported names (we
                 don't know the final kind yet)
        module_public: If False, this name won't be imported via
            'from <module> import *'. This has no effect on names within
            classes.
        module_hidden: If True, the name will be never exported (needed for
            stub files)
        cross_ref: For deserialized MypyFile nodes, the referenced module
            name; for other nodes, optionally the name of the referenced object.
        implicit: Was this defined by assignment to self attribute?
        plugin_generated: Was this symbol generated by a plugin?
            (And therefore needs to be removed in aststrip.)
        no_serialize: Do not serialize this node if True. This is used to prevent
            keys in the cache that refer to modules on which this file does not
            depend. Currently this can happen if there is a module not in build
            used e.g. like this:
                import a.b.c # type: ignore
            This will add a submodule symbol to parent module `a` symbol table,
            but `a.b` is _not_ added as its dependency. Therefore, we should
            not serialize these symbols as they may not be found during fixup
            phase, instead they will be re-added during subsequent patch parents
            phase.
            TODO: Refactor build.py to make dependency tracking more transparent
            and/or refactor look-up functions to not require parent patching.

    NOTE: No other attributes should be added to this class unless they
    are shared by all node kinds.
    """
    kind: Incomplete
    node: Incomplete
    module_public: Incomplete
    implicit: Incomplete
    module_hidden: Incomplete
    cross_ref: Incomplete
    plugin_generated: Incomplete
    no_serialize: Incomplete
    def __init__(self, kind: int, node: SymbolNode | None, module_public: bool = True, implicit: bool = False, module_hidden: bool = False, *, plugin_generated: bool = False, no_serialize: bool = False) -> None: ...
    @property
    def fullname(self) -> str | None: ...
    @property
    def type(self) -> mypy.types.Type | None: ...
    def copy(self) -> SymbolTableNode: ...
    def serialize(self, prefix: str, name: str) -> JsonDict:
        """Serialize a SymbolTableNode.

        Args:
          prefix: full name of the containing module or class; or None
          name: name of this object relative to the containing object
        """
    @classmethod
    def deserialize(cls, data: JsonDict) -> SymbolTableNode: ...

class SymbolTable(Dict[str, SymbolTableNode]):
    """Static representation of a namespace dictionary.

    This is used for module, class and function namespaces.
    """
    def copy(self) -> SymbolTable: ...
    def serialize(self, fullname: str) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict) -> SymbolTable: ...

class DataclassTransformSpec:
    """Specifies how a dataclass-like transform should be applied. The fields here are based on the
    parameters accepted by `typing.dataclass_transform`."""
    eq_default: Incomplete
    order_default: Incomplete
    kw_only_default: Incomplete
    frozen_default: Incomplete
    field_specifiers: Incomplete
    def __init__(self, *, eq_default: bool | None = None, order_default: bool | None = None, kw_only_default: bool | None = None, field_specifiers: tuple[str, ...] | None = None, frozen_default: bool | None = None) -> None: ...
    def serialize(self) -> JsonDict: ...
    @classmethod
    def deserialize(cls, data: JsonDict) -> DataclassTransformSpec: ...

def get_flags(node: Node, names: list[str]) -> list[str]: ...
def set_flags(node: Node, flags: list[str]) -> None: ...
def get_member_expr_fullname(expr: MemberExpr) -> str | None:
    """Return the qualified name representation of a member expression.

    Return a string of form foo.bar, foo.bar.baz, or similar, or None if the
    argument cannot be represented in this form.
    """

deserialize_map: Final[Incomplete]

def check_arg_kinds(arg_kinds: list[ArgKind], nodes: list[T], fail: Callable[[str, T], None]) -> None: ...
def check_arg_names(names: Sequence[str | None], nodes: list[T], fail: Callable[[str, T], None], description: str = 'function definition') -> None: ...
def is_class_var(expr: NameExpr) -> bool:
    """Return whether the expression is ClassVar[...]"""
def is_final_node(node: SymbolNode | None) -> bool:
    """Check whether `node` corresponds to a final attribute."""
def local_definitions(names: SymbolTable, name_prefix: str, info: TypeInfo | None = None) -> Iterator[Definition]:
    """Iterate over local definitions (not imported) in a symbol table.

    Recursively iterate over class members and nested classes.
    """
