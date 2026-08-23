import mypy.checkexpr
from _typeshed import Incomplete
from mypy import message_registry as message_registry, nodes as nodes, operators as operators
from mypy.binder import ConditionalTypeBinder as ConditionalTypeBinder, Frame as Frame, get_declaration as get_declaration
from mypy.checkmember import MemberContext as MemberContext, analyze_decorator_or_funcbase_access as analyze_decorator_or_funcbase_access, analyze_descriptor_access as analyze_descriptor_access, analyze_member_access as analyze_member_access, type_object_type as type_object_type
from mypy.checkpattern import PatternChecker as PatternChecker
from mypy.constraints import SUPERTYPE_OF as SUPERTYPE_OF
from mypy.erasetype import erase_type as erase_type, erase_typevars as erase_typevars, remove_instance_last_known_values as remove_instance_last_known_values
from mypy.errorcodes import ErrorCode as ErrorCode, TYPE_VAR as TYPE_VAR, UNUSED_AWAITABLE as UNUSED_AWAITABLE, UNUSED_COROUTINE as UNUSED_COROUTINE
from mypy.errors import ErrorWatcher as ErrorWatcher, Errors as Errors, report_internal_error as report_internal_error
from mypy.expandtype import expand_self_type as expand_self_type, expand_type as expand_type, expand_type_by_instance as expand_type_by_instance
from mypy.join import join_types as join_types
from mypy.literals import Key as Key, extract_var_from_literal_hash as extract_var_from_literal_hash, literal as literal, literal_hash as literal_hash
from mypy.maptype import map_instance_to_supertype as map_instance_to_supertype
from mypy.meet import is_overlapping_erased_types as is_overlapping_erased_types, is_overlapping_types as is_overlapping_types
from mypy.message_registry import ErrorMessage as ErrorMessage
from mypy.messages import MessageBuilder as MessageBuilder, SUGGESTED_TEST_FIXTURES as SUGGESTED_TEST_FIXTURES, append_invariance_notes as append_invariance_notes, format_type as format_type, format_type_bare as format_type_bare, format_type_distinctly as format_type_distinctly, make_inferred_type_note as make_inferred_type_note, pretty_seq as pretty_seq
from mypy.mro import MroError as MroError, calculate_mro as calculate_mro
from mypy.nodes import ARG_NAMED as ARG_NAMED, ARG_POS as ARG_POS, ARG_STAR as ARG_STAR, AssertStmt as AssertStmt, AssignmentExpr as AssignmentExpr, AssignmentStmt as AssignmentStmt, Block as Block, BreakStmt as BreakStmt, BytesExpr as BytesExpr, CONTRAVARIANT as CONTRAVARIANT, COVARIANT as COVARIANT, CallExpr as CallExpr, ClassDef as ClassDef, ComparisonExpr as ComparisonExpr, Context as Context, ContinueStmt as ContinueStmt, Decorator as Decorator, DelStmt as DelStmt, EllipsisExpr as EllipsisExpr, Expression as Expression, ExpressionStmt as ExpressionStmt, FUNC_NO_INFO as FUNC_NO_INFO, FloatExpr as FloatExpr, ForStmt as ForStmt, FuncBase as FuncBase, FuncDef as FuncDef, FuncItem as FuncItem, GDEF as GDEF, IMPLICITLY_ABSTRACT as IMPLICITLY_ABSTRACT, INVARIANT as INVARIANT, IS_ABSTRACT as IS_ABSTRACT, IfStmt as IfStmt, Import as Import, ImportAll as ImportAll, ImportBase as ImportBase, ImportFrom as ImportFrom, IndexExpr as IndexExpr, IntExpr as IntExpr, LDEF as LDEF, LITERAL_TYPE as LITERAL_TYPE, LambdaExpr as LambdaExpr, ListExpr as ListExpr, Lvalue as Lvalue, MDEF as MDEF, MatchStmt as MatchStmt, MemberExpr as MemberExpr, MypyFile as MypyFile, NOT_ABSTRACT as NOT_ABSTRACT, NameExpr as NameExpr, Node as Node, OpExpr as OpExpr, OperatorAssignmentStmt as OperatorAssignmentStmt, OverloadedFuncDef as OverloadedFuncDef, PassStmt as PassStmt, PromoteExpr as PromoteExpr, RaiseStmt as RaiseStmt, RefExpr as RefExpr, ReturnStmt as ReturnStmt, StarExpr as StarExpr, Statement as Statement, StrExpr as StrExpr, SymbolNode as SymbolNode, SymbolTable as SymbolTable, SymbolTableNode as SymbolTableNode, TempNode as TempNode, TryStmt as TryStmt, TupleExpr as TupleExpr, TypeAlias as TypeAlias, TypeInfo as TypeInfo, TypeVarExpr as TypeVarExpr, UnaryExpr as UnaryExpr, Var as Var, WhileStmt as WhileStmt, WithStmt as WithStmt, is_final_node as is_final_node
from mypy.options import Options as Options
from mypy.patterns import AsPattern as AsPattern, StarredPattern as StarredPattern
from mypy.plugin import CheckerPluginInterface as CheckerPluginInterface, Plugin as Plugin
from mypy.scope import Scope as Scope
from mypy.semanal import is_trivial_body as is_trivial_body, refers_to_fullname as refers_to_fullname, set_callable_name as set_callable_name
from mypy.semanal_enum import ENUM_BASES as ENUM_BASES, ENUM_SPECIAL_PROPS as ENUM_SPECIAL_PROPS
from mypy.sharedparse import BINARY_MAGIC_METHODS as BINARY_MAGIC_METHODS
from mypy.state import state as state
from mypy.subtypes import find_member as find_member, is_callable_compatible as is_callable_compatible, is_equivalent as is_equivalent, is_more_precise as is_more_precise, is_proper_subtype as is_proper_subtype, is_same_type as is_same_type, is_subtype as is_subtype, restrict_subtype_away as restrict_subtype_away, unify_generic_callable as unify_generic_callable
from mypy.traverser import TraverserVisitor as TraverserVisitor, all_return_statements as all_return_statements, has_return_statement as has_return_statement
from mypy.treetransform import TransformVisitor as TransformVisitor
from mypy.typeanal import check_for_explicit_any as check_for_explicit_any, has_any_from_unimported_type as has_any_from_unimported_type, make_optional_type as make_optional_type
from mypy.typeops import bind_self as bind_self, coerce_to_literal as coerce_to_literal, custom_special_method as custom_special_method, erase_def_to_union_or_bound as erase_def_to_union_or_bound, erase_to_bound as erase_to_bound, erase_to_union_or_bound as erase_to_union_or_bound, false_only as false_only, fixup_partial_type as fixup_partial_type, function_type as function_type, get_type_vars as get_type_vars, is_literal_type_like as is_literal_type_like, is_singleton_type as is_singleton_type, make_simplified_union as make_simplified_union, map_type_from_supertype as map_type_from_supertype, true_only as true_only, try_expanding_sum_type_to_union as try_expanding_sum_type_to_union, try_getting_int_literals_from_type as try_getting_int_literals_from_type, try_getting_str_literals as try_getting_str_literals, try_getting_str_literals_from_type as try_getting_str_literals_from_type, tuple_fallback as tuple_fallback
from mypy.types import ANY_STRATEGY as ANY_STRATEGY, AnyType as AnyType, BoolTypeQuery as BoolTypeQuery, CallableType as CallableType, DeletedType as DeletedType, ErasedType as ErasedType, FunctionLike as FunctionLike, Instance as Instance, LiteralType as LiteralType, MYPYC_NATIVE_INT_NAMES as MYPYC_NATIVE_INT_NAMES, NoneType as NoneType, OVERLOAD_NAMES as OVERLOAD_NAMES, Overloaded as Overloaded, PartialType as PartialType, ProperType as ProperType, TupleType as TupleType, Type as Type, TypeAliasType as TypeAliasType, TypeGuardedType as TypeGuardedType, TypeOfAny as TypeOfAny, TypeTranslator as TypeTranslator, TypeType as TypeType, TypeVarId as TypeVarId, TypeVarLikeType as TypeVarLikeType, TypeVarType as TypeVarType, TypedDictType as TypedDictType, UnboundType as UnboundType, UninhabitedType as UninhabitedType, UnionType as UnionType, flatten_nested_unions as flatten_nested_unions, get_proper_type as get_proper_type, get_proper_types as get_proper_types, is_literal_type as is_literal_type, is_named_instance as is_named_instance
from mypy.types_utils import is_optional as is_optional, remove_optional as remove_optional, store_argument_type as store_argument_type, strip_type as strip_type
from mypy.typetraverser import TypeTraverserVisitor as TypeTraverserVisitor
from mypy.typevars import fill_typevars as fill_typevars, fill_typevars_with_any as fill_typevars_with_any, has_no_typevars as has_no_typevars
from mypy.util import is_dunder as is_dunder, is_sunder as is_sunder, is_typeshed_file as is_typeshed_file
from mypy.visitor import NodeVisitor as NodeVisitor
from typing import AbstractSet, Callable, Generic, Iterable, Iterator, Mapping, NamedTuple, Sequence, TypeVar, overload
from typing_extensions import Final, TypeAlias as _TypeAlias

T = TypeVar('T')
DEFAULT_LAST_PASS: Final[int]
DeferredNodeType: _TypeAlias
FineGrainedDeferredNodeType: _TypeAlias

class DeferredNode(NamedTuple):
    node: DeferredNodeType
    active_typeinfo: TypeInfo | None

class FineGrainedDeferredNode(NamedTuple):
    node: FineGrainedDeferredNodeType
    active_typeinfo: TypeInfo | None

TypeMap: _TypeAlias

class TypeRange(NamedTuple):
    item: Type
    is_upper_bound: bool

class PartialTypeScope(NamedTuple):
    map: dict[Var, Context]
    is_function: bool
    is_local: bool

class TypeChecker(NodeVisitor[None], CheckerPluginInterface):
    """Mypy type checker.

    Type check mypy source files that have been semantically analyzed.

    You must create a separate instance for each source file.
    """
    is_stub: bool
    errors: Errors
    msg: MessageBuilder
    binder: ConditionalTypeBinder
    expr_checker: mypy.checkexpr.ExpressionChecker
    pattern_checker: PatternChecker
    tscope: Scope
    scope: CheckerScope
    return_types: list[Type]
    dynamic_funcs: list[bool]
    partial_types: list[PartialTypeScope]
    partial_reported: set[Var]
    globals: SymbolTable
    modules: dict[str, MypyFile]
    deferred_nodes: list[DeferredNode]
    pass_num: int
    last_pass = DEFAULT_LAST_PASS
    current_node_deferred: bool
    is_typeshed_stub: bool
    options: Options
    inferred_attribute_types: dict[Var, Type] | None
    no_partial_types: bool
    module_refs: set[str]
    var_decl_frames: dict[Var, set[int]]
    plugin: Plugin
    tree: Incomplete
    path: Incomplete
    recurse_into_functions: bool
    checking_missing_await: bool
    allow_abstract_call: bool
    def __init__(self, errors: Errors, modules: dict[str, MypyFile], options: Options, tree: MypyFile, path: str, plugin: Plugin, per_line_checking_time_ns: dict[int, int]) -> None:
        """Construct a type checker.

        Use errors to report type check errors.
        """
    @property
    def type_context(self) -> list[Type | None]: ...
    temp_type_map: Incomplete
    def reset(self) -> None:
        """Cleanup stale state that might be left over from a typechecking run.

        This allows us to reuse TypeChecker objects in fine-grained
        incremental mode.
        """
    def check_first_pass(self) -> None:
        """Type check the entire file, but defer functions with unresolved references.

        Unresolved references are forward references to variables
        whose types haven't been inferred yet.  They may occur later
        in the same file or in a different file that's being processed
        later (usually due to an import cycle).

        Deferred functions will be processed by check_second_pass().
        """
    def check_second_pass(self, todo: Sequence[DeferredNode | FineGrainedDeferredNode] | None = None) -> bool:
        """Run second or following pass of type checking.

        This goes through deferred nodes, returning True if there were any.
        """
    def check_partial(self, node: DeferredNodeType | FineGrainedDeferredNodeType) -> None: ...
    def check_top_level(self, node: MypyFile) -> None:
        """Check only the top-level of a module, skipping function definitions."""
    def defer_node(self, node: DeferredNodeType, enclosing_class: TypeInfo | None) -> None:
        """Defer a node for processing during next type-checking pass.

        Args:
            node: function/method being deferred
            enclosing_class: for methods, the class where the method is defined
        NOTE: this can't handle nested functions/methods.
        """
    def handle_cannot_determine_type(self, name: str, context: Context) -> None: ...
    def accept(self, stmt: Statement) -> None:
        """Type check a node in the given type context."""
    def accept_loop(self, body: Statement, else_body: Statement | None = None, *, exit_condition: Expression | None = None) -> None:
        """Repeatedly type check a loop body until the frame doesn't change.
        If exit_condition is set, assume it must be False on exit from the loop.

        Then check the else_body.
        """
    def visit_overloaded_func_def(self, defn: OverloadedFuncDef) -> None: ...
    def check_overlapping_overloads(self, defn: OverloadedFuncDef) -> None: ...
    def is_generator_return_type(self, typ: Type, is_coroutine: bool) -> bool:
        """Is `typ` a valid type for a generator/coroutine?

        True if `typ` is a *supertype* of Generator or Awaitable.
        Also true it it's *exactly* AwaitableGenerator (modulo type parameters).
        """
    def is_async_generator_return_type(self, typ: Type) -> bool:
        """Is `typ` a valid type for an async generator?

        True if `typ` is a supertype of AsyncGenerator.
        """
    def get_generator_yield_type(self, return_type: Type, is_coroutine: bool) -> Type:
        """Given the declared return type of a generator (t), return the type it yields (ty)."""
    def get_generator_receive_type(self, return_type: Type, is_coroutine: bool) -> Type:
        """Given a declared generator return type (t), return the type its yield receives (tc)."""
    def get_coroutine_return_type(self, return_type: Type) -> Type: ...
    def get_generator_return_type(self, return_type: Type, is_coroutine: bool) -> Type:
        """Given the declared return type of a generator (t), return the type it returns (tr)."""
    def visit_func_def(self, defn: FuncDef) -> None: ...
    def check_func_item(self, defn: FuncItem, type_override: CallableType | None = None, name: str | None = None, allow_empty: bool = False) -> None:
        """Type check a function.

        If type_override is provided, use it as the function type.
        """
    def enter_attribute_inference_context(self) -> Iterator[None]: ...
    def check_func_def(self, defn: FuncItem, typ: CallableType, name: str | None, allow_empty: bool = False) -> None:
        """Type check a function definition."""
    def is_var_redefined_in_outer_context(self, v: Var, after_line: int) -> bool:
        """Can the variable be assigned to at module top level or outer function?

        Note that this doesn't do a full CFG analysis but uses a line number based
        heuristic that isn't correct in some (rare) cases.
        """
    def check_unbound_return_typevar(self, typ: CallableType) -> None:
        """Fails when the return typevar is not defined in arguments."""
    def check_default_args(self, item: FuncItem, body_is_trivial: bool) -> None: ...
    def is_forward_op_method(self, method_name: str) -> bool: ...
    def is_reverse_op_method(self, method_name: str) -> bool: ...
    def check_for_missing_annotations(self, fdef: FuncItem) -> None: ...
    def check___new___signature(self, fdef: FuncDef, typ: CallableType) -> None: ...
    def check_reverse_op_method(self, defn: FuncItem, reverse_type: CallableType, reverse_name: str, context: Context) -> None:
        """Check a reverse operator method such as __radd__."""
    def check_overlapping_op_methods(self, reverse_type: CallableType, reverse_name: str, reverse_class: TypeInfo, forward_type: Type, forward_name: str, forward_base: Type, context: Context) -> None:
        """Check for overlapping method and reverse method signatures.

        This function assumes that:

        -   The reverse method has valid argument count and kinds.
        -   If the reverse operator method accepts some argument of type
            X, the forward operator method also belong to class X.

            For example, if we have the reverse operator `A.__radd__(B)`, then the
            corresponding forward operator must have the type `B.__add__(...)`.
        """
    def is_unsafe_overlapping_op(self, forward_item: CallableType, forward_base: Type, reverse_type: CallableType) -> bool: ...
    def check_inplace_operator_method(self, defn: FuncBase) -> None:
        """Check an inplace operator method such as __iadd__.

        They cannot arbitrarily overlap with __add__.
        """
    def check_getattr_method(self, typ: Type, context: Context, name: str) -> None: ...
    def check_setattr_method(self, typ: Type, context: Context) -> None: ...
    def check_slots_definition(self, typ: Type, context: Context) -> None:
        """Check the type of __slots__."""
    def check_match_args(self, var: Var, typ: Type, context: Context) -> None:
        """Check that __match_args__ contains literal strings"""
    def expand_typevars(self, defn: FuncItem, typ: CallableType) -> list[tuple[FuncItem, CallableType]]: ...
    def check_method_override(self, defn: FuncDef | OverloadedFuncDef | Decorator) -> bool | None:
        """Check if function definition is compatible with base classes.

        This may defer the method if a signature is not available in at least one base class.
        Return ``None`` if that happens.

        Return ``True`` if an attribute with the method name was found in the base class.
        """
    def check_method_or_accessor_override_for_base(self, defn: FuncDef | OverloadedFuncDef | Decorator, base: TypeInfo) -> bool | None:
        """Check if method definition is compatible with a base class.

        Return ``None`` if the node was deferred because one of the corresponding
        superclass nodes is not ready.

        Return ``True`` if an attribute with the method name was found in the base class.
        """
    def check_method_override_for_base_with_name(self, defn: FuncDef | OverloadedFuncDef | Decorator, name: str, base: TypeInfo) -> bool:
        """Check if overriding an attribute `name` of `base` with `defn` is valid.

        Return True if the supertype node was not analysed yet, and `defn` was deferred.
        """
    def bind_and_map_method(self, sym: SymbolTableNode, typ: FunctionLike, sub_info: TypeInfo, super_info: TypeInfo) -> FunctionLike:
        """Bind self-type and map type variables for a method.

        Arguments:
            sym: a symbol that points to method definition
            typ: method type on the definition
            sub_info: class where the method is used
            super_info: class where the method was defined
        """
    def get_op_other_domain(self, tp: FunctionLike) -> Type | None: ...
    def check_override(self, override: FunctionLike, original: FunctionLike, name: str, name_in_super: str, supertype: str, original_class_or_static: bool, override_class_or_static: bool, node: Context) -> None:
        """Check a method override with given signatures.

        Arguments:
          override:  The signature of the overriding method.
          original:  The signature of the original supertype method.
          name:      The name of the subtype. This and the next argument are
                     only used for generating error messages.
          supertype: The name of the supertype.
        """
    def check__exit__return_type(self, defn: FuncItem) -> None:
        '''Generate error if the return type of __exit__ is problematic.

        If __exit__ always returns False but the return type is declared
        as bool, mypy thinks that a with statement may "swallow"
        exceptions even though this is not the case, resulting in
        invalid reachability inference.
        '''
    def visit_class_def(self, defn: ClassDef) -> None:
        """Type check a class definition."""
    def check_final_deletable(self, typ: TypeInfo) -> None: ...
    def check_init_subclass(self, defn: ClassDef) -> None:
        """Check that keywords in a class definition are valid arguments for __init_subclass__().

        In this example:
            1   class Base:
            2       def __init_subclass__(cls, thing: int):
            3           pass
            4   class Child(Base, thing=5):
            5       def __init_subclass__(cls):
            6           pass
            7   Child()

        Base.__init_subclass__(thing=5) is called at line 4. This is what we simulate here.
        Child.__init_subclass__ is never called.
        """
    def check_enum(self, defn: ClassDef) -> None: ...
    def check_final_enum(self, defn: ClassDef, base: TypeInfo) -> None: ...
    def is_final_enum_value(self, sym: SymbolTableNode) -> bool: ...
    def check_enum_bases(self, defn: ClassDef) -> None:
        """
        Non-enum mixins cannot appear after enum bases; this is disallowed at runtime:

            class Foo: ...
            class Bar(enum.Enum, Foo): ...

        But any number of enum mixins can appear in a class definition
        (even if multiple enum bases define __new__). So this is fine:

            class Foo(enum.Enum):
                def __new__(cls, val): ...
            class Bar(enum.Enum):
                def __new__(cls, val): ...
            class Baz(int, Foo, Bar, enum.Flag): ...
        """
    def check_enum_new(self, defn: ClassDef) -> None: ...
    def check_protocol_variance(self, defn: ClassDef) -> None:
        """Check that protocol definition is compatible with declared
        variances of type variables.

        Note that we also prohibit declaring protocol classes as invariant
        if they are actually covariant/contravariant, since this may break
        transitivity of subtyping, see PEP 544.
        """
    def check_multiple_inheritance(self, typ: TypeInfo) -> None:
        """Check for multiple inheritance related errors."""
    def determine_type_of_member(self, sym: SymbolTableNode) -> Type | None: ...
    def check_compatibility(self, name: str, base1: TypeInfo, base2: TypeInfo, ctx: TypeInfo) -> None:
        """Check if attribute name in base1 is compatible with base2 in multiple inheritance.

        Assume base1 comes before base2 in the MRO, and that base1 and base2 don't have
        a direct subclass relationship (i.e., the compatibility requirement only derives from
        multiple inheritance).

        This check verifies that a definition taken from base1 (and mapped to the current
        class ctx), is type compatible with the definition taken from base2 (also mapped), so
        that unsafe subclassing like this can be detected:
            class A(Generic[T]):
                def foo(self, x: T) -> None: ...

            class B:
                def foo(self, x: str) -> None: ...

            class C(B, A[int]): ...  # this is unsafe because...

            x: A[int] = C()
            x.foo  # ...runtime type is (str) -> None, while static type is (int) -> None
        """
    def check_metaclass_compatibility(self, typ: TypeInfo) -> None:
        """Ensures that metaclasses of all parent types are compatible."""
    def visit_import_from(self, node: ImportFrom) -> None: ...
    def visit_import_all(self, node: ImportAll) -> None: ...
    def visit_import(self, node: Import) -> None: ...
    def check_import(self, node: ImportBase) -> None: ...
    def visit_block(self, b: Block) -> None: ...
    def should_report_unreachable_issues(self) -> bool: ...
    def is_raising_or_empty(self, s: Statement) -> bool:
        """Returns 'true' if the given statement either throws an error of some kind
        or is a no-op.

        We use this function mostly while handling the '--warn-unreachable' flag. When
        that flag is present, we normally report an error on any unreachable statement.
        But if that statement is just something like a 'pass' or a just-in-case 'assert False',
        reporting an error would be annoying.
        """
    def visit_assignment_stmt(self, s: AssignmentStmt) -> None:
        """Type check an assignment statement.

        Handle all kinds of assignment statements (simple, indexed, multiple).
        """
    def check_type_alias_rvalue(self, s: AssignmentStmt) -> None: ...
    def check_assignment(self, lvalue: Lvalue, rvalue: Expression, infer_lvalue_type: bool = True, new_syntax: bool = False) -> None:
        """Type check a single assignment: lvalue = rvalue."""
    partial_type_augmented_ops: Final[Incomplete]
    def get_variable_type_context(self, inferred: Var) -> Type | None: ...
    def try_infer_partial_generic_type_from_assignment(self, lvalue: Lvalue, rvalue: Expression, op: str) -> None:
        """Try to infer a precise type for partial generic type from assignment.

        'op' is '=' for normal assignment and a binary operator ('+', ...) for
        augmented assignment.

        Example where this happens:

            x = []
            if foo():
                x = [1]  # Infer List[int] as type of 'x'
        """
    def check_compatibility_all_supers(self, lvalue: RefExpr, lvalue_type: Type | None, rvalue: Expression) -> bool: ...
    def check_compatibility_super(self, lvalue: RefExpr, lvalue_type: Type | None, rvalue: Expression, base: TypeInfo, base_type: Type, base_node: Node) -> bool: ...
    def lvalue_type_from_base(self, expr_node: Var, base: TypeInfo) -> tuple[Type | None, Node | None]:
        """For a NameExpr that is part of a class, walk all base classes and try
        to find the first class that defines a Type for the same name."""
    def check_compatibility_classvar_super(self, node: Var, base: TypeInfo, base_node: Node | None) -> bool: ...
    def check_compatibility_final_super(self, node: Var, base: TypeInfo, base_node: Node | None) -> bool:
        """Check if an assignment overrides a final attribute in a base class.

        This only checks situations where either a node in base class is not a variable
        but a final method, or where override is explicitly declared as final.
        In these cases we give a more detailed error message. In addition, we check that
        a final variable doesn't override writeable attribute, which is not safe.

        Other situations are checked in `check_final()`.
        """
    def check_if_final_var_override_writable(self, name: str, base_node: Node | None, ctx: Context) -> None:
        """Check that a final variable doesn't override writeable attribute.

        This is done to prevent situations like this:
            class C:
                attr = 1
            class D(C):
                attr: Final = 2

            x: C = D()
            x.attr = 3  # Oops!
        """
    def get_final_context(self) -> bool:
        """Check whether we a currently checking a final declaration."""
    def enter_final_context(self, is_final_def: bool) -> Iterator[None]:
        """Store whether the current checked assignment is a final declaration."""
    def check_final(self, s: AssignmentStmt | OperatorAssignmentStmt | AssignmentExpr) -> None:
        """Check if this assignment does not assign to a final attribute.

        This function performs the check only for name assignments at module
        and class scope. The assignments to `obj.attr` and `Cls.attr` are checked
        in checkmember.py.
        """
    def check_assignment_to_slots(self, lvalue: Lvalue) -> None: ...
    def is_assignable_slot(self, lvalue: Lvalue, typ: Type | None) -> bool: ...
    def check_assignment_to_multiple_lvalues(self, lvalues: list[Lvalue], rvalue: Expression, context: Context, infer_lvalue_type: bool = True) -> None: ...
    def check_rvalue_count_in_assignment(self, lvalues: list[Lvalue], rvalue_count: int, context: Context) -> bool: ...
    def check_multi_assignment(self, lvalues: list[Lvalue], rvalue: Expression, context: Context, infer_lvalue_type: bool = True, rv_type: Type | None = None, undefined_rvalue: bool = False) -> None:
        """Check the assignment of one rvalue to a number of lvalues."""
    def check_multi_assignment_from_union(self, lvalues: list[Expression], rvalue: Expression, rvalue_type: UnionType, context: Context, infer_lvalue_type: bool) -> None:
        """Check assignment to multiple lvalue targets when rvalue type is a Union[...].
        For example:

            t: Union[Tuple[int, int], Tuple[str, str]]
            x, y = t
            reveal_type(x)  # Union[int, str]

        The idea in this case is to process the assignment for every item of the union.
        Important note: the types are collected in two places, 'union_types' contains
        inferred types for first assignments, 'assignments' contains the narrowed types
        for binder.
        """
    def flatten_lvalues(self, lvalues: list[Expression]) -> list[Expression]: ...
    def check_multi_assignment_from_tuple(self, lvalues: list[Lvalue], rvalue: Expression, rvalue_type: TupleType, context: Context, undefined_rvalue: bool, infer_lvalue_type: bool = True) -> None: ...
    def lvalue_type_for_inference(self, lvalues: list[Lvalue], rvalue_type: TupleType) -> Type: ...
    def split_around_star(self, items: list[T], star_index: int, length: int) -> tuple[list[T], list[T], list[T]]:
        """Splits a list of items in three to match another list of length 'length'
        that contains a starred expression at 'star_index' in the following way:

        star_index = 2, length = 5 (i.e., [a,b,*,c,d]), items = [1,2,3,4,5,6,7]
        returns in: ([1,2], [3,4,5], [6,7])
        """
    def type_is_iterable(self, type: Type) -> bool: ...
    def check_multi_assignment_from_iterable(self, lvalues: list[Lvalue], rvalue_type: Type, context: Context, infer_lvalue_type: bool = True) -> None: ...
    def check_lvalue(self, lvalue: Lvalue) -> tuple[Type | None, IndexExpr | None, Var | None]: ...
    def is_definition(self, s: Lvalue) -> bool: ...
    def infer_variable_type(self, name: Var, lvalue: Lvalue, init_type: Type, context: Context) -> None:
        """Infer the type of initialized variables from initializer type."""
    def infer_partial_type(self, name: Var, lvalue: Lvalue, init_type: Type) -> bool: ...
    def is_valid_defaultdict_partial_value_type(self, t: ProperType) -> bool:
        """Check if t can be used as the basis for a partial defaultdict value type.

        Examples:

          * t is 'int' --> True
          * t is 'list[<nothing>]' --> True
          * t is 'dict[...]' --> False (only generic types with a single type
            argument supported)
        """
    def set_inferred_type(self, var: Var, lvalue: Lvalue, type: Type) -> None:
        """Store inferred variable type.

        Store the type to both the variable node and the expression node that
        refers to the variable (lvalue). If var is None, do nothing.
        """
    def set_inference_error_fallback_type(self, var: Var, lvalue: Lvalue, type: Type) -> None:
        """Store best known type for variable if type inference failed.

        If a program ignores error on type inference error, the variable should get some
        inferred type so that if can used later on in the program. Example:

          x = []  # type: ignore
          x.append(1)   # Should be ok!

        We implement this here by giving x a valid type (replacing inferred <nothing> with Any).
        """
    def inference_error_fallback_type(self, type: Type) -> Type: ...
    def simple_rvalue(self, rvalue: Expression) -> bool:
        """Returns True for expressions for which inferred type should not depend on context.

        Note that this function can still return False for some expressions where inferred type
        does not depend on context. It only exists for performance optimizations.
        """
    def check_simple_assignment(self, lvalue_type: Type | None, rvalue: Expression, context: Context, msg: ErrorMessage = ..., lvalue_name: str = 'variable', rvalue_name: str = 'expression', *, notes: list[str] | None = None) -> Type: ...
    def check_member_assignment(self, instance_type: Type, attribute_type: Type, rvalue: Expression, context: Context) -> tuple[Type, Type, bool]:
        """Type member assignment.

        This defers to check_simple_assignment, unless the member expression
        is a descriptor, in which case this checks descriptor semantics as well.

        Return the inferred rvalue_type, inferred lvalue_type, and whether to use the binder
        for this assignment.

        Note: this method exists here and not in checkmember.py, because we need to take
        care about interaction between binder and __set__().
        """
    def check_indexed_assignment(self, lvalue: IndexExpr, rvalue: Expression, context: Context) -> None:
        """Type check indexed assignment base[index] = rvalue.

        The lvalue argument is the base[index] expression.
        """
    def try_infer_partial_type_from_indexed_assignment(self, lvalue: IndexExpr, rvalue: Expression) -> None: ...
    def type_requires_usage(self, typ: Type) -> tuple[str, ErrorCode] | None:
        """Some types require usage in all cases. The classic example is
        an unused coroutine.

        In the case that it does require usage, returns a note to attach
        to the error message.
        """
    def visit_expression_stmt(self, s: ExpressionStmt) -> None: ...
    def visit_return_stmt(self, s: ReturnStmt) -> None:
        """Type check a return statement."""
    def check_return_stmt(self, s: ReturnStmt) -> None: ...
    def visit_if_stmt(self, s: IfStmt) -> None:
        """Type check an if statement."""
    def visit_while_stmt(self, s: WhileStmt) -> None:
        """Type check a while statement."""
    def visit_operator_assignment_stmt(self, s: OperatorAssignmentStmt) -> None:
        """Type check an operator assignment statement, e.g. x += 1."""
    def visit_assert_stmt(self, s: AssertStmt) -> None: ...
    def visit_raise_stmt(self, s: RaiseStmt) -> None:
        """Type check a raise statement."""
    def type_check_raise(self, e: Expression, s: RaiseStmt, optional: bool = False) -> None: ...
    def visit_try_stmt(self, s: TryStmt) -> None:
        """Type check a try statement."""
    def visit_try_without_finally(self, s: TryStmt, try_frame: bool) -> None:
        """Type check a try statement, ignoring the finally block.

        On entry, the top frame should receive all flow that exits the
        try block abnormally (i.e., such that the else block does not
        execute), and its parent should receive all flow that exits
        the try block normally.
        """
    def check_except_handler_test(self, n: Expression, is_star: bool) -> Type:
        """Type check an exception handler test clause."""
    def default_exception_type(self, is_star: bool) -> Type:
        """Exception type to return in case of a previous type error."""
    def wrap_exception_group(self, types: Sequence[Type]) -> Type:
        """Transform except* variable type into an appropriate exception group."""
    def get_types_from_except_handler(self, typ: Type, n: Expression) -> list[Type]:
        """Helper for check_except_handler_test to retrieve handler types."""
    def visit_for_stmt(self, s: ForStmt) -> None:
        """Type check a for statement."""
    def analyze_async_iterable_item_type(self, expr: Expression) -> tuple[Type, Type]:
        """Analyse async iterable expression and return iterator and iterator item types."""
    def analyze_iterable_item_type(self, expr: Expression) -> tuple[Type, Type]:
        """Analyse iterable expression and return iterator and iterator item types."""
    def analyze_iterable_item_type_without_expression(self, type: Type, context: Context) -> tuple[Type, Type]:
        """Analyse iterable type and return iterator and iterator item types."""
    def analyze_range_native_int_type(self, expr: Expression) -> Type | None:
        '''Try to infer native int item type from arguments to range(...).

        For example, return i64 if the expression is "range(0, i64(n))".

        Return None if unsuccessful.
        '''
    def analyze_container_item_type(self, typ: Type) -> Type | None:
        """Check if a type is a nominal container of a union of such.

        Return the corresponding container item type.
        """
    def analyze_index_variables(self, index: Expression, item_type: Type, infer_lvalue_type: bool, context: Context) -> None:
        """Type check or infer for loop or list comprehension index vars."""
    def visit_del_stmt(self, s: DelStmt) -> None: ...
    def visit_decorator(self, e: Decorator) -> None: ...
    def check_for_untyped_decorator(self, func: FuncDef, dec_type: Type, dec_expr: Expression) -> None: ...
    def check_incompatible_property_override(self, e: Decorator) -> None: ...
    def visit_with_stmt(self, s: WithStmt) -> None: ...
    def check_untyped_after_decorator(self, typ: Type, func: FuncDef) -> None: ...
    def check_async_with_item(self, expr: Expression, target: Expression | None, infer_lvalue_type: bool) -> Type: ...
    def check_with_item(self, expr: Expression, target: Expression | None, infer_lvalue_type: bool) -> Type: ...
    def visit_break_stmt(self, s: BreakStmt) -> None: ...
    def visit_continue_stmt(self, s: ContinueStmt) -> None: ...
    def visit_match_stmt(self, s: MatchStmt) -> None: ...
    def infer_variable_types_from_type_maps(self, type_maps: list[TypeMap]) -> dict[Var, Type]: ...
    def remove_capture_conflicts(self, type_map: TypeMap, inferred_types: dict[Var, Type]) -> None: ...
    def make_fake_typeinfo(self, curr_module_fullname: str, class_gen_name: str, class_short_name: str, bases: list[Instance]) -> tuple[ClassDef, TypeInfo]: ...
    def intersect_instances(self, instances: tuple[Instance, Instance], errors: list[tuple[str, str]]) -> Instance | None:
        """Try creating an ad-hoc intersection of the given instances.

        Note that this function does *not* try and create a full-fledged
        intersection type. Instead, it returns an instance of a new ad-hoc
        subclass of the given instances.

        This is mainly useful when you need a way of representing some
        theoretical subclass of the instances the user may be trying to use
        the generated intersection can serve as a placeholder.

        This function will create a fresh subclass every time you call it,
        even if you pass in the exact same arguments. So this means calling
        `self.intersect_intersection([inst_1, inst_2], ctx)` twice will result
        in instances of two distinct subclasses of inst_1 and inst_2.

        This is by design: we want each ad-hoc intersection to be unique since
        they're supposed represent some other unknown subclass.

        Returns None if creating the subclass is impossible (e.g. due to
        MRO errors or incompatible signatures). If we do successfully create
        a subclass, its TypeInfo will automatically be added to the global scope.
        """
    def intersect_instance_callable(self, typ: Instance, callable_type: CallableType) -> Instance:
        """Creates a fake type that represents the intersection of an Instance and a CallableType.

        It operates by creating a bare-minimum dummy TypeInfo that
        subclasses type and adds a __call__ method matching callable_type.
        """
    def make_fake_callable(self, typ: Instance) -> Instance:
        """Produce a new type that makes type Callable with a generic callable type."""
    def partition_by_callable(self, typ: Type, unsound_partition: bool) -> tuple[list[Type], list[Type]]:
        """Partitions a type into callable subtypes and uncallable subtypes.

        Thus, given:
        `callables, uncallables = partition_by_callable(type)`

        If we assert `callable(type)` then `type` has type Union[*callables], and
        If we assert `not callable(type)` then `type` has type Union[*uncallables]

        If unsound_partition is set, assume that anything that is not
        clearly callable is in fact not callable. Otherwise we generate a
        new subtype that *is* callable.

        Guaranteed to not return [], [].
        """
    def conditional_callable_type_map(self, expr: Expression, current_type: Type | None) -> tuple[TypeMap, TypeMap]:
        """Takes in an expression and the current type of the expression.

        Returns a 2-tuple: The first element is a map from the expression to
        the restricted type if it were callable. The second element is a
        map from the expression to the type it would hold if it weren't
        callable.
        """
    def conditional_types_for_iterable(self, item_type: Type, iterable_type: Type) -> tuple[Type | None, Type | None]:
        """
        Narrows the type of `iterable_type` based on the type of `item_type`.
        For now, we only support narrowing unions of TypedDicts based on left operand being literal string(s).
        """
    def find_type_equals_check(self, node: ComparisonExpr, expr_indices: list[int]) -> tuple[TypeMap, TypeMap]:
        """Narrow types based on any checks of the type ``type(x) == T``

        Args:
            node: The node that might contain the comparison
            expr_indices: The list of indices of expressions in ``node`` that are being
                compared
        """
    def find_isinstance_check(self, node: Expression) -> tuple[TypeMap, TypeMap]:
        """Find any isinstance checks (within a chain of ands).  Includes
        implicit and explicit checks for None and calls to callable.
        Also includes TypeGuard functions.

        Return value is a map of variables to their types if the condition
        is true and a map of variables to their types if the condition is false.

        If either of the values in the tuple is None, then that particular
        branch can never occur.

        May return {}, {}.
        Can return None, None in situations involving NoReturn.
        """
    def find_isinstance_check_helper(self, node: Expression) -> tuple[TypeMap, TypeMap]: ...
    def propagate_up_typemap_info(self, new_types: TypeMap) -> TypeMap:
        '''Attempts refining parent expressions of any MemberExpr or IndexExprs in new_types.

        Specifically, this function accepts two mappings of expression to original types:
        the original mapping (existing_types), and a new mapping (new_types) intended to
        update the original.

        This function iterates through new_types and attempts to use the information to try
        refining any parent types that happen to be unions.

        For example, suppose there are two types "A = Tuple[int, int]" and "B = Tuple[str, str]".
        Next, suppose that \'new_types\' specifies the expression \'foo[0]\' has a refined type
        of \'int\' and that \'foo\' was previously deduced to be of type Union[A, B].

        Then, this function will observe that since A[0] is an int and B[0] is not, the type of
        \'foo\' can be further refined from Union[A, B] into just B.

        We perform this kind of "parent narrowing" for member lookup expressions and indexing
        expressions into tuples, namedtuples, and typeddicts. We repeat this narrowing
        recursively if the parent is also a "lookup expression". So for example, if we have
        the expression "foo[\'bar\'].baz[0]", we\'d potentially end up refining types for the
        expressions "foo", "foo[\'bar\']", and "foo[\'bar\'].baz".

        We return the newly refined map. This map is guaranteed to be a superset of \'new_types\'.
        '''
    def refine_parent_types(self, expr: Expression, expr_type: Type) -> Mapping[Expression, Type]:
        """Checks if the given expr is a 'lookup operation' into a union and iteratively refines
        the parent types based on the 'expr_type'.

        For example, if 'expr' is an expression like 'a.b.c.d', we'll potentially return refined
        types for expressions 'a', 'a.b', and 'a.b.c'.

        For more details about what a 'lookup operation' is and how we use the expr_type to refine
        the parent types of lookup_expr, see the docstring in 'propagate_up_typemap_info'.
        """
    def refine_identity_comparison_expression(self, operands: list[Expression], operand_types: list[Type], chain_indices: list[int], narrowable_operand_indices: AbstractSet[int], is_valid_target: Callable[[ProperType], bool], coerce_only_in_literal_context: bool) -> tuple[TypeMap, TypeMap]:
        """Produce conditional type maps refining expressions by an identity/equality comparison.

        The 'operands' and 'operand_types' lists should be the full list of operands used
        in the overall comparison expression. The 'chain_indices' list is the list of indices
        actually used within this identity comparison chain.

        So if we have the expression:

            a <= b is c is d <= e

        ...then 'operands' and 'operand_types' would be lists of length 5 and 'chain_indices'
        would be the list [1, 2, 3].

        The 'narrowable_operand_indices' parameter is the set of all indices we are allowed
        to refine the types of: that is, all operands that will potentially be a part of
        the output TypeMaps.

        Although this function could theoretically try setting the types of the operands
        in the chains to the meet, doing that causes too many issues in real-world code.
        Instead, we use 'is_valid_target' to identify which of the given chain types
        we could plausibly use as the refined type for the expressions in the chain.

        Similarly, 'coerce_only_in_literal_context' controls whether we should try coercing
        expressions in the chain to a Literal type. Performing this coercion is sometimes
        too aggressive of a narrowing, depending on context.
        """
    def refine_away_none_in_comparison(self, operands: list[Expression], operand_types: list[Type], chain_indices: list[int], narrowable_operand_indices: AbstractSet[int]) -> tuple[TypeMap, TypeMap]:
        """Produces conditional type maps refining away None in an identity/equality chain.

        For more details about what the different arguments mean, see the
        docstring of 'refine_identity_comparison_expression' up above.
        """
    @overload
    def check_subtype(self, subtype: Type, supertype: Type, context: Context, msg: str, subtype_label: str | None = None, supertype_label: str | None = None, *, notes: list[str] | None = None, code: ErrorCode | None = None, outer_context: Context | None = None) -> bool: ...
    @overload
    def check_subtype(self, subtype: Type, supertype: Type, context: Context, msg: ErrorMessage, subtype_label: str | None = None, supertype_label: str | None = None, *, notes: list[str] | None = None, outer_context: Context | None = None) -> bool: ...
    def get_precise_awaitable_type(self, typ: Type, local_errors: ErrorWatcher) -> Type | None:
        """If type implements Awaitable[X] with non-Any X, return X.

        In all other cases return None. This method must be called in context
        of local_errors.
        """
    def checking_await_set(self) -> Iterator[None]: ...
    def check_possible_missing_await(self, subtype: Type, supertype: Type, context: Context) -> None:
        """Check if the given type becomes a subtype when awaited."""
    def contains_none(self, t: Type) -> bool: ...
    def named_type(self, name: str) -> Instance:
        """Return an instance type with given name and implicit Any type args.

        For example, named_type('builtins.object') produces the 'object' type.
        """
    def named_generic_type(self, name: str, args: list[Type]) -> Instance:
        """Return an instance with the given name and type arguments.

        Assume that the number of arguments is correct.  Assume that
        the name refers to a compatible generic type.
        """
    def lookup_typeinfo(self, fullname: str) -> TypeInfo: ...
    def type_type(self) -> Instance:
        """Return instance type 'type'."""
    def str_type(self) -> Instance:
        """Return instance type 'str'."""
    def store_type(self, node: Expression, typ: Type) -> None:
        """Store the type of a node in the type map."""
    def has_type(self, node: Expression) -> bool: ...
    def lookup_type_or_none(self, node: Expression) -> Type | None: ...
    def lookup_type(self, node: Expression) -> Type: ...
    def store_types(self, d: dict[Expression, Type]) -> None: ...
    def local_type_map(self) -> Iterator[dict[Expression, Type]]:
        '''Store inferred types into a temporary type map (returned).

        This can be used to perform type checking "experiments" without
        affecting exported types (which are used by mypyc).
        '''
    def in_checked_function(self) -> bool:
        """Should we type-check the current function?

        - Yes if --check-untyped-defs is set.
        - Yes outside functions.
        - Yes in annotated functions.
        - No otherwise.
        """
    def lookup(self, name: str) -> SymbolTableNode:
        """Look up a definition from the symbol table with the given name."""
    def lookup_qualified(self, name: str) -> SymbolTableNode: ...
    def enter_partial_types(self, *, is_function: bool = False, is_class: bool = False) -> Iterator[None]:
        """Enter a new scope for collecting partial types.

        Also report errors for (some) variables which still have partial
        types, i.e. we couldn't infer a complete type.
        """
    def handle_partial_var_type(self, typ: PartialType, is_lvalue: bool, node: Var, context: Context) -> Type:
        """Handle a reference to a partial type through a var.

        (Used by checkexpr and checkmember.)
        """
    def is_defined_in_base_class(self, var: Var) -> bool: ...
    def find_partial_types(self, var: Var) -> dict[Var, Context] | None:
        """Look for an active partial type scope containing variable.

        A scope is active if assignments in the current context can refine a partial
        type originally defined in the scope. This is affected by the local_partial_types
        configuration option.
        """
    def find_partial_types_in_all_scopes(self, var: Var) -> tuple[bool, bool, dict[Var, Context] | None]:
        """Look for partial type scope containing variable.

        Return tuple (is the scope active, is the scope a local scope, scope).
        """
    def temp_node(self, t: Type, context: Context | None = None) -> TempNode:
        """Create a temporary node with the given, fixed type."""
    def fail(self, msg: str | ErrorMessage, context: Context, *, code: ErrorCode | None = None) -> None:
        """Produce an error message."""
    def note(self, msg: str | ErrorMessage, context: Context, offset: int = 0, *, code: ErrorCode | None = None) -> None:
        """Produce a note."""
    def iterable_item_type(self, it: Instance | CallableType | TypeType | Overloaded, context: Context) -> Type: ...
    def function_type(self, func: FuncBase) -> FunctionLike: ...
    def push_type_map(self, type_map: TypeMap) -> None: ...
    def infer_issubclass_maps(self, node: CallExpr, expr: Expression) -> tuple[TypeMap, TypeMap]:
        """Infer type restrictions for an expression in issubclass call."""
    @overload
    def conditional_types_with_intersection(self, expr_type: Type, type_ranges: list[TypeRange] | None, ctx: Context, default: None = None) -> tuple[Type | None, Type | None]: ...
    @overload
    def conditional_types_with_intersection(self, expr_type: Type, type_ranges: list[TypeRange] | None, ctx: Context, default: Type) -> tuple[Type, Type]: ...
    def is_writable_attribute(self, node: Node) -> bool:
        """Check if an attribute is writable"""
    def get_isinstance_type(self, expr: Expression) -> list[TypeRange] | None: ...
    def is_literal_enum(self, n: Expression) -> bool:
        """Returns true if this expression (with the given type context) is an Enum literal.

        For example, if we had an enum:

            class Foo(Enum):
                A = 1
                B = 2

        ...and if the expression 'Foo' referred to that enum within the current type context,
        then the expression 'Foo.A' would be a literal enum. However, if we did 'a = Foo.A',
        then the variable 'a' would *not* be a literal enum.

        We occasionally special-case expressions like 'Foo.A' and treat them as a single primitive
        unit for the same reasons we sometimes treat 'True', 'False', or 'None' as a single
        primitive unit.
        """
    def add_any_attribute_to_type(self, typ: Type, name: str) -> Type:
        """Inject an extra attribute with Any type using fallbacks."""
    def hasattr_type_maps(self, expr: Expression, source_type: Type, name: str) -> tuple[TypeMap, TypeMap]:
        """Simple support for hasattr() checks.

        Essentially the logic is following:
            * In the if branch, keep types that already has a valid attribute as is,
              for other inject an attribute with `Any` type.
            * In the else branch, remove types that already have a valid attribute,
              while keeping the rest.
        """
    def partition_union_by_attr(self, source_type: UnionType, name: str) -> tuple[list[Type], list[Type]]: ...
    def has_valid_attribute(self, typ: Type, name: str) -> bool: ...

class CollectArgTypeVarTypes(TypeTraverserVisitor):
    """Collects the non-nested argument types in a set."""
    arg_types: Incomplete
    def __init__(self) -> None: ...
    def visit_type_var(self, t: TypeVarType) -> None: ...

@overload
def conditional_types(current_type: Type, proposed_type_ranges: list[TypeRange] | None, default: None = None) -> tuple[Type | None, Type | None]: ...
@overload
def conditional_types(current_type: Type, proposed_type_ranges: list[TypeRange] | None, default: Type) -> tuple[Type, Type]: ...
def conditional_types_to_typemaps(expr: Expression, yes_type: Type | None, no_type: Type | None) -> tuple[TypeMap, TypeMap]: ...
def gen_unique_name(base: str, table: SymbolTable) -> str:
    """Generate a name that does not appear in table by appending numbers to base."""
def is_true_literal(n: Expression) -> bool:
    """Returns true if this expression is the 'True' literal/keyword."""
def is_false_literal(n: Expression) -> bool:
    """Returns true if this expression is the 'False' literal/keyword."""
def is_literal_none(n: Expression) -> bool:
    """Returns true if this expression is the 'None' literal/keyword."""
def is_literal_not_implemented(n: Expression) -> bool: ...
def builtin_item_type(tp: Type) -> Type | None:
    """Get the item type of a builtin container.

    If 'tp' is not one of the built containers (these includes NamedTuple and TypedDict)
    or if the container is not parameterized (like List or List[Any])
    return None. This function is used to narrow optional types in situations like this:

        x: Optional[int]
        if x in (1, 2, 3):
            x + 42  # OK

    Note: this is only OK for built-in containers, where we know the behavior
    of __contains__.
    """
def and_conditional_maps(m1: TypeMap, m2: TypeMap) -> TypeMap:
    """Calculate what information we can learn from the truth of (e1 and e2)
    in terms of the information that we can learn from the truth of e1 and
    the truth of e2.
    """
def or_conditional_maps(m1: TypeMap, m2: TypeMap) -> TypeMap:
    """Calculate what information we can learn from the truth of (e1 or e2)
    in terms of the information that we can learn from the truth of e1 and
    the truth of e2.
    """
def reduce_conditional_maps(type_maps: list[tuple[TypeMap, TypeMap]]) -> tuple[TypeMap, TypeMap]:
    '''Reduces a list containing pairs of if/else TypeMaps into a single pair.

    We "and" together all of the if TypeMaps and "or" together the else TypeMaps. So
    for example, if we had the input:

        [
            ({x: TypeIfX, shared: TypeIfShared1}, {x: TypeElseX, shared: TypeElseShared1}),
            ({y: TypeIfY, shared: TypeIfShared2}, {y: TypeElseY, shared: TypeElseShared2}),
        ]

    ...we\'d return the output:

        (
            {x: TypeIfX,   y: TypeIfY,   shared: PseudoIntersection[TypeIfShared1, TypeIfShared2]},
            {shared: Union[TypeElseShared1, TypeElseShared2]},
        )

    ...where "PseudoIntersection[X, Y] == Y" because mypy actually doesn\'t understand intersections
    yet, so we settle for just arbitrarily picking the right expr\'s type.

    We only retain the shared expression in the \'else\' case because we don\'t actually know
    whether x was refined or y was refined -- only just that one of the two was refined.
    '''
def convert_to_typetype(type_map: TypeMap) -> TypeMap: ...
def flatten(t: Expression) -> list[Expression]:
    """Flatten a nested sequence of tuples/lists into one list of nodes."""
def flatten_types(t: Type) -> list[Type]:
    """Flatten a nested sequence of tuples into one list of nodes."""
def expand_func(defn: FuncItem, map: dict[TypeVarId, Type]) -> FuncItem: ...

class TypeTransformVisitor(TransformVisitor):
    map: Incomplete
    def __init__(self, map: dict[TypeVarId, Type]) -> None: ...
    def type(self, type: Type) -> Type: ...

def are_argument_counts_overlapping(t: CallableType, s: CallableType) -> bool:
    """Can a single call match both t and s, based just on positional argument counts?"""
def is_unsafe_overlapping_overload_signatures(signature: CallableType, other: CallableType) -> bool:
    """Check if two overloaded signatures are unsafely overlapping or partially overlapping.

    We consider two functions 's' and 't' to be unsafely overlapping if both
    of the following are true:

    1.  s's parameters are all more precise or partially overlapping with t's
    2.  s's return type is NOT a subtype of t's.

    Assumes that 'signature' appears earlier in the list of overload
    alternatives then 'other' and that their argument counts are overlapping.
    """
def detach_callable(typ: CallableType) -> CallableType:
    """Ensures that the callable's type variables are 'detached' and independent of the context.

    A callable normally keeps track of the type variables it uses within its 'variables' field.
    However, if the callable is from a method and that method is using a class type variable,
    the callable will not keep track of that type variable since it belongs to the class.

    This function will traverse the callable and find all used type vars and add them to the
    variables field if it isn't already present.

    The caller can then unify on all type variables whether or not the callable is originally
    from a class or not."""
def overload_can_never_match(signature: CallableType, other: CallableType) -> bool:
    """Check if the 'other' method can never be matched due to 'signature'.

    This can happen if signature's parameters are all strictly broader then
    other's parameters.

    Assumes that both signatures have overlapping argument counts.
    """
def is_more_general_arg_prefix(t: FunctionLike, s: FunctionLike) -> bool:
    """Does t have wider arguments than s?"""
def is_same_arg_prefix(t: CallableType, s: CallableType) -> bool: ...
def infer_operator_assignment_method(typ: Type, operator: str) -> tuple[bool, str]:
    """Determine if operator assignment on given value type is in-place, and the method name.

    For example, if operator is '+', return (True, '__iadd__') or (False, '__add__')
    depending on which method is supported by the type.
    """
def is_valid_inferred_type(typ: Type, is_lvalue_final: bool = False) -> bool:
    """Is an inferred type valid and needs no further refinement?

    Examples of invalid types include the None type (when we are not assigning
    None to a final lvalue) or List[<uninhabited>].

    When not doing strict Optional checking, all types containing None are
    invalid.  When doing strict Optional checking, only None and types that are
    incompletely defined (i.e. contain UninhabitedType) are invalid.
    """

class InvalidInferredTypes(BoolTypeQuery):
    """Find type components that are not valid for an inferred type.

    These include <Erased> type, and any <nothing> types resulting from failed
    (ambiguous) type inference.
    """
    def __init__(self) -> None: ...
    def visit_uninhabited_type(self, t: UninhabitedType) -> bool: ...
    def visit_erased_type(self, t: ErasedType) -> bool: ...

class SetNothingToAny(TypeTranslator):
    """Replace all ambiguous <nothing> types with Any (to avoid spurious extra errors)."""
    def visit_uninhabited_type(self, t: UninhabitedType) -> Type: ...
    def visit_type_alias_type(self, t: TypeAliasType) -> Type: ...

def is_node_static(node: Node | None) -> bool | None:
    """Find out if a node describes a static function method."""

class CheckerScope:
    stack: list[TypeInfo | FuncItem | MypyFile]
    def __init__(self, module: MypyFile) -> None: ...
    def top_function(self) -> FuncItem | None: ...
    def top_non_lambda_function(self) -> FuncItem | None: ...
    def active_class(self) -> TypeInfo | None: ...
    def enclosing_class(self) -> TypeInfo | None:
        """Is there a class *directly* enclosing this function?"""
    def active_self_type(self) -> Instance | TupleType | None:
        """An instance or tuple type representing the current class.

        This returns None unless we are in class body or in a method.
        In particular, inside a function nested in method this returns None.
        """
    def push_function(self, item: FuncItem) -> Iterator[None]: ...
    def push_class(self, info: TypeInfo) -> Iterator[None]: ...
TKey = TypeVar('TKey')
TValue = TypeVar('TValue')

class DisjointDict(Generic[TKey, TValue]):
    """An variation of the union-find algorithm/data structure where instead of keeping
    track of just disjoint sets, we keep track of disjoint dicts -- keep track of multiple
    Set[Key] -> Set[Value] mappings, where each mapping's keys are guaranteed to be disjoint.

    This data structure is currently used exclusively by 'group_comparison_operands' below
    to merge chains of '==' and 'is' comparisons when two or more chains use the same expression
    in best-case O(n), where n is the number of operands.

    Specifically, the `add_mapping()` function and `items()` functions will take on average
    O(k + v) and O(n) respectively, where k and v are the number of keys and values we're adding
    for a given chain. Note that k <= n and v <= n.

    We hit these average/best-case scenarios for most user code: e.g. when the user has just
    a single chain like 'a == b == c == d == ...' or multiple disjoint chains like
    'a==b < c==d < e==f < ...'. (Note that a naive iterative merging would be O(n^2) for
    the latter case).

    In comparison, this data structure will make 'group_comparison_operands' have a worst-case
    runtime of O(n*log(n)): 'add_mapping()' and 'items()' are worst-case O(k*log(n) + v) and
    O(k*log(n)) respectively. This happens only in the rare case where the user keeps repeatedly
    making disjoint mappings before merging them in a way that persistently dodges the path
    compression optimization in '_lookup_root_id', which would end up constructing a single
    tree of height log_2(n). This makes root lookups no longer amoritized constant time when we
    finally call 'items()'.
    """
    def __init__(self) -> None: ...
    def add_mapping(self, keys: set[TKey], values: set[TValue]) -> None:
        """Adds a 'Set[TKey] -> Set[TValue]' mapping. If there already exists a mapping
        containing one or more of the given keys, we merge the input mapping with the old one.

        Note that the given set of keys must be non-empty -- otherwise, nothing happens.
        """
    def items(self) -> list[tuple[set[TKey], set[TValue]]]:
        """Returns all disjoint mappings in key-value pairs."""

def group_comparison_operands(pairwise_comparisons: Iterable[tuple[str, Expression, Expression]], operand_to_literal_hash: Mapping[int, Key], operators_to_group: set[str]) -> list[tuple[str, list[int]]]:
    '''Group a series of comparison operands together chained by any operand
    in the \'operators_to_group\' set. All other pairwise operands are kept in
    groups of size 2.

    For example, suppose we have the input comparison expression:

        x0 == x1 == x2 < x3 < x4 is x5 is x6 is not x7 is not x8

    If we get these expressions in a pairwise way (e.g. by calling ComparisionExpr\'s
    \'pairwise()\' method), we get the following as input:

        [(\'==\', x0, x1), (\'==\', x1, x2), (\'<\', x2, x3), (\'<\', x3, x4),
         (\'is\', x4, x5), (\'is\', x5, x6), (\'is not\', x6, x7), (\'is not\', x7, x8)]

    If `operators_to_group` is the set {\'==\', \'is\'}, this function will produce
    the following "simplified operator list":

       [("==", [0, 1, 2]), ("<", [2, 3]), ("<", [3, 4]),
        ("is", [4, 5, 6]), ("is not", [6, 7]), ("is not", [7, 8])]

    Note that (a) we yield *indices* to the operands rather then the operand
    expressions themselves and that (b) operands used in a consecutive chain
    of \'==\' or \'is\' are grouped together.

    If two of these chains happen to contain operands with the same underlying
    literal hash (e.g. are assignable and correspond to the same expression),
    we combine those chains together. For example, if we had:

        same == x < y == same

    ...and if \'operand_to_literal_hash\' contained the same values for the indices
    0 and 3, we\'d produce the following output:

        [("==", [0, 1, 2, 3]), ("<", [1, 2])]

    But if the \'operand_to_literal_hash\' did *not* contain an entry, we\'d instead
    default to returning:

        [("==", [0, 1]), ("<", [1, 2]), ("==", [2, 3])]

    This function is currently only used to assist with type-narrowing refinements
    and is extracted out to a helper function so we can unit test it.
    '''
def is_typed_callable(c: Type | None) -> bool: ...
def is_untyped_decorator(typ: Type | None) -> bool: ...
def is_static(func: FuncBase | Decorator) -> bool: ...
def is_property(defn: SymbolNode) -> bool: ...
def get_property_type(t: ProperType) -> ProperType: ...
def is_subtype_no_promote(left: Type, right: Type) -> bool: ...
def is_overlapping_types_no_promote_no_uninhabited(left: Type, right: Type) -> bool: ...
def is_private(node_name: str) -> bool:
    """Check if node is private to class definition."""
def is_string_literal(typ: Type) -> bool: ...
def has_bool_item(typ: ProperType) -> bool:
    """Return True if type is 'bool' or a union with a 'bool' item."""
def collapse_walrus(e: Expression) -> Expression:
    """If an expression is an AssignmentExpr, pull out the assignment target.

    We don't make any attempt to pull out all the targets in code like `x := (y := z)`.
    We could support narrowing those if that sort of code turns out to be common.
    """
def find_last_var_assignment_line(n: Node, v: Var) -> int:
    """Find the highest line number of a potential assignment to variable within node.

    This supports local and global variables.

    Return -1 if no assignment was found.
    """

class VarAssignVisitor(TraverserVisitor):
    last_line: int
    lvalue: bool
    var_node: Incomplete
    def __init__(self, v: Var) -> None: ...
    def visit_assignment_stmt(self, s: AssignmentStmt) -> None: ...
    def visit_name_expr(self, e: NameExpr) -> None: ...
    def visit_member_expr(self, e: MemberExpr) -> None: ...
    def visit_index_expr(self, e: IndexExpr) -> None: ...
    def visit_with_stmt(self, s: WithStmt) -> None: ...
    def visit_for_stmt(self, s: ForStmt) -> None: ...
    def visit_assignment_expr(self, e: AssignmentExpr) -> None: ...
    def visit_as_pattern(self, p: AsPattern) -> None: ...
    def visit_starred_pattern(self, p: StarredPattern) -> None: ...
