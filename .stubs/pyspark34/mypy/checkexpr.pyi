import mypy.checker
from _typeshed import Incomplete
from mypy import applytype as applytype, erasetype as erasetype, join as join, message_registry as message_registry, nodes as nodes, operators as operators, types as types
from mypy.argmap import ArgTypeExpander as ArgTypeExpander, map_actuals_to_formals as map_actuals_to_formals, map_formals_to_actuals as map_formals_to_actuals
from mypy.checkmember import analyze_member_access as analyze_member_access, type_object_type as type_object_type
from mypy.checkstrformat import StringFormatterChecker as StringFormatterChecker
from mypy.erasetype import erase_type as erase_type, remove_instance_last_known_values as remove_instance_last_known_values, replace_meta_vars as replace_meta_vars
from mypy.errors import ErrorWatcher as ErrorWatcher, report_internal_error as report_internal_error
from mypy.expandtype import expand_type as expand_type, expand_type_by_instance as expand_type_by_instance, freshen_function_type_vars as freshen_function_type_vars
from mypy.infer import ArgumentInferContext as ArgumentInferContext, infer_function_type_arguments as infer_function_type_arguments, infer_type_arguments as infer_type_arguments
from mypy.literals import literal as literal
from mypy.maptype import map_instance_to_supertype as map_instance_to_supertype
from mypy.meet import is_overlapping_types as is_overlapping_types, narrow_declared_type as narrow_declared_type
from mypy.message_registry import ErrorMessage as ErrorMessage
from mypy.messages import MessageBuilder as MessageBuilder
from mypy.nodes import ARG_NAMED as ARG_NAMED, ARG_POS as ARG_POS, ARG_STAR as ARG_STAR, ARG_STAR2 as ARG_STAR2, ArgKind as ArgKind, AssertTypeExpr as AssertTypeExpr, AssignmentExpr as AssignmentExpr, AwaitExpr as AwaitExpr, BytesExpr as BytesExpr, CallExpr as CallExpr, CastExpr as CastExpr, ComparisonExpr as ComparisonExpr, ComplexExpr as ComplexExpr, ConditionalExpr as ConditionalExpr, Context as Context, Decorator as Decorator, DictExpr as DictExpr, DictionaryComprehension as DictionaryComprehension, EllipsisExpr as EllipsisExpr, EnumCallExpr as EnumCallExpr, Expression as Expression, FloatExpr as FloatExpr, FuncDef as FuncDef, GeneratorExpr as GeneratorExpr, IMPLICITLY_ABSTRACT as IMPLICITLY_ABSTRACT, IndexExpr as IndexExpr, IntExpr as IntExpr, LITERAL_TYPE as LITERAL_TYPE, LambdaExpr as LambdaExpr, ListComprehension as ListComprehension, ListExpr as ListExpr, MemberExpr as MemberExpr, MypyFile as MypyFile, NameExpr as NameExpr, NamedTupleExpr as NamedTupleExpr, NewTypeExpr as NewTypeExpr, OpExpr as OpExpr, OverloadedFuncDef as OverloadedFuncDef, ParamSpecExpr as ParamSpecExpr, PlaceholderNode as PlaceholderNode, PromoteExpr as PromoteExpr, REVEAL_TYPE as REVEAL_TYPE, RefExpr as RefExpr, RevealExpr as RevealExpr, SetComprehension as SetComprehension, SetExpr as SetExpr, SliceExpr as SliceExpr, StarExpr as StarExpr, StrExpr as StrExpr, SuperExpr as SuperExpr, SymbolNode as SymbolNode, TempNode as TempNode, TupleExpr as TupleExpr, TypeAlias as TypeAlias, TypeAliasExpr as TypeAliasExpr, TypeApplication as TypeApplication, TypeInfo as TypeInfo, TypeVarExpr as TypeVarExpr, TypeVarTupleExpr as TypeVarTupleExpr, TypedDictExpr as TypedDictExpr, UnaryExpr as UnaryExpr, Var as Var, YieldExpr as YieldExpr, YieldFromExpr as YieldFromExpr
from mypy.plugin import FunctionContext as FunctionContext, FunctionSigContext as FunctionSigContext, MethodContext as MethodContext, MethodSigContext as MethodSigContext, Plugin as Plugin
from mypy.semanal_enum import ENUM_BASES as ENUM_BASES
from mypy.state import state as state
from mypy.subtypes import is_equivalent as is_equivalent, is_same_type as is_same_type, is_subtype as is_subtype, non_method_protocol_members as non_method_protocol_members
from mypy.traverser import has_await_expression as has_await_expression
from mypy.typeanal import check_for_explicit_any as check_for_explicit_any, has_any_from_unimported_type as has_any_from_unimported_type, instantiate_type_alias as instantiate_type_alias, make_optional_type as make_optional_type, set_any_tvars as set_any_tvars
from mypy.typeops import callable_type as callable_type, custom_special_method as custom_special_method, erase_to_union_or_bound as erase_to_union_or_bound, false_only as false_only, fixup_partial_type as fixup_partial_type, function_type as function_type, is_literal_type_like as is_literal_type_like, make_simplified_union as make_simplified_union, simple_literal_type as simple_literal_type, true_only as true_only, try_expanding_sum_type_to_union as try_expanding_sum_type_to_union, try_getting_str_literals as try_getting_str_literals, tuple_fallback as tuple_fallback
from mypy.types import AnyType as AnyType, CallableType as CallableType, DeletedType as DeletedType, ErasedType as ErasedType, ExtraAttrs as ExtraAttrs, FunctionLike as FunctionLike, Instance as Instance, LITERAL_TYPE_NAMES as LITERAL_TYPE_NAMES, LiteralType as LiteralType, LiteralValue as LiteralValue, NoneType as NoneType, Overloaded as Overloaded, ParamSpecFlavor as ParamSpecFlavor, ParamSpecType as ParamSpecType, PartialType as PartialType, ProperType as ProperType, TUPLE_LIKE_INSTANCE_NAMES as TUPLE_LIKE_INSTANCE_NAMES, TupleType as TupleType, Type as Type, TypeAliasType as TypeAliasType, TypeOfAny as TypeOfAny, TypeType as TypeType, TypeVarTupleType as TypeVarTupleType, TypeVarType as TypeVarType, TypedDictType as TypedDictType, UninhabitedType as UninhabitedType, UnionType as UnionType, UnpackType as UnpackType, flatten_nested_tuples as flatten_nested_tuples, flatten_nested_unions as flatten_nested_unions, get_proper_type as get_proper_type, get_proper_types as get_proper_types, has_recursive_types as has_recursive_types, is_named_instance as is_named_instance, split_with_prefix_and_suffix as split_with_prefix_and_suffix
from mypy.types_utils import is_generic_instance as is_generic_instance, is_optional as is_optional, is_self_type_like as is_self_type_like, remove_optional as remove_optional
from mypy.typestate import type_state as type_state
from mypy.typevars import fill_typevars as fill_typevars
from mypy.typevartuples import find_unpack_in_list as find_unpack_in_list
from mypy.util import split_module_names as split_module_names
from mypy.visitor import ExpressionVisitor as ExpressionVisitor
from typing import Callable, ClassVar, Iterator, Sequence
from typing_extensions import Final, TypeAlias as _TypeAlias, overload

ArgChecker: _TypeAlias
MAX_UNIONS: Final[int]
OVERLAPPING_TYPES_ALLOWLIST: Final[Incomplete]
OVERLAPPING_BYTES_ALLOWLIST: Final[Incomplete]

class TooManyUnions(Exception):
    """Indicates that we need to stop splitting unions in an attempt
    to match an overload in order to save performance.
    """

def allow_fast_container_literal(t: Type) -> bool: ...
def extract_refexpr_names(expr: RefExpr) -> set[str]:
    """Recursively extracts all module references from a reference expression.

    Note that currently, the only two subclasses of RefExpr are NameExpr and
    MemberExpr."""

class Finished(Exception):
    """Raised if we can terminate overload argument check early (no match)."""

class ExpressionChecker(ExpressionVisitor[Type]):
    """Expression type checker.

    This class works closely together with checker.TypeChecker.
    """
    chk: mypy.checker.TypeChecker
    msg: MessageBuilder
    type_context: list[Type | None]
    resolved_type: dict[Expression, ProperType]
    strfrm_checker: StringFormatterChecker
    plugin: Plugin
    per_line_checking_time_ns: Incomplete
    collect_line_checking_stats: Incomplete
    in_expression: bool
    type_overrides: Incomplete
    is_callee: bool
    def __init__(self, chk: mypy.checker.TypeChecker, msg: MessageBuilder, plugin: Plugin, per_line_checking_time_ns: dict[int, int]) -> None:
        """Construct an expression type checker."""
    def reset(self) -> None: ...
    def visit_name_expr(self, e: NameExpr) -> Type:
        """Type check a name expression.

        It can be of any kind: local, member or global.
        """
    def analyze_ref_expr(self, e: RefExpr, lvalue: bool = False) -> Type: ...
    def analyze_var_ref(self, var: Var, context: Context) -> Type: ...
    def module_type(self, node: MypyFile) -> Instance: ...
    def visit_call_expr(self, e: CallExpr, allow_none_return: bool = False) -> Type:
        """Type check a call expression."""
    def refers_to_typeddict(self, base: Expression) -> bool: ...
    def visit_call_expr_inner(self, e: CallExpr, allow_none_return: bool = False) -> Type: ...
    def check_str_format_call(self, e: CallExpr) -> None:
        """More precise type checking for str.format() calls on literals."""
    def method_fullname(self, object_type: Type, method_name: str) -> str | None:
        """Convert a method name to a fully qualified name, based on the type of the object that
        it is invoked on. Return `None` if the name of `object_type` cannot be determined.
        """
    def always_returns_none(self, node: Expression) -> bool:
        """Check if `node` refers to something explicitly annotated as only returning None."""
    def defn_returns_none(self, defn: SymbolNode | None) -> bool:
        """Check if `defn` can _only_ return None."""
    def check_runtime_protocol_test(self, e: CallExpr) -> None: ...
    def check_protocol_issubclass(self, e: CallExpr) -> None: ...
    def check_typeddict_call(self, callee: TypedDictType, arg_kinds: list[ArgKind], arg_names: Sequence[str | None], args: list[Expression], context: Context, orig_callee: Type | None) -> Type: ...
    def validate_typeddict_kwargs(self, kwargs: DictExpr) -> dict[str, Expression] | None: ...
    def match_typeddict_call_with_dict(self, callee: TypedDictType, kwargs: DictExpr, context: Context) -> bool: ...
    def check_typeddict_call_with_dict(self, callee: TypedDictType, kwargs: DictExpr, context: Context, orig_callee: Type | None) -> Type: ...
    def typeddict_callable(self, info: TypeInfo) -> CallableType:
        """Construct a reasonable type for a TypedDict type in runtime context.

        If it appears as a callee, it will be special-cased anyway, e.g. it is
        also allowed to accept a single positional argument if it is a dict literal.

        Note it is not safe to move this to type_object_type() since it will crash
        on plugin-generated TypedDicts, that may not have the special_alias.
        """
    def typeddict_callable_from_context(self, callee: TypedDictType) -> CallableType: ...
    def check_typeddict_call_with_kwargs(self, callee: TypedDictType, kwargs: dict[str, Expression], context: Context, orig_callee: Type | None) -> Type: ...
    def get_partial_self_var(self, expr: MemberExpr) -> Var | None:
        """Get variable node for a partial self attribute.

        If the expression is not a self attribute, or attribute is not variable,
        or variable is not partial, return None.
        """
    item_args: ClassVar[dict[str, list[str]]]
    container_args: ClassVar[dict[str, dict[str, list[str]]]]
    def try_infer_partial_type(self, e: CallExpr) -> None:
        """Try to make partial type precise from a call."""
    def get_partial_var(self, ref: RefExpr) -> tuple[Var, dict[Var, Context]] | None: ...
    def try_infer_partial_value_type_from_call(self, e: CallExpr, methodname: str, var: Var) -> Instance | None:
        """Try to make partial type precise from a call such as 'x.append(y)'."""
    def apply_function_plugin(self, callee: CallableType, arg_kinds: list[ArgKind], arg_types: list[Type], arg_names: Sequence[str | None] | None, formal_to_actual: list[list[int]], args: list[Expression], fullname: str, object_type: Type | None, context: Context) -> Type:
        """Use special case logic to infer the return type of a specific named function/method.

        Caller must ensure that a plugin hook exists. There are two different cases:

        - If object_type is None, the caller must ensure that a function hook exists
          for fullname.
        - If object_type is not None, the caller must ensure that a method hook exists
          for fullname.

        Return the inferred return type.
        """
    def apply_signature_hook(self, callee: FunctionLike, args: list[Expression], arg_kinds: list[ArgKind], arg_names: Sequence[str | None] | None, hook: Callable[[list[list[Expression]], CallableType], FunctionLike]) -> FunctionLike:
        """Helper to apply a signature hook for either a function or method"""
    def apply_function_signature_hook(self, callee: FunctionLike, args: list[Expression], arg_kinds: list[ArgKind], context: Context, arg_names: Sequence[str | None] | None, signature_hook: Callable[[FunctionSigContext], FunctionLike]) -> FunctionLike:
        """Apply a plugin hook that may infer a more precise signature for a function."""
    def apply_method_signature_hook(self, callee: FunctionLike, args: list[Expression], arg_kinds: list[ArgKind], context: Context, arg_names: Sequence[str | None] | None, object_type: Type, signature_hook: Callable[[MethodSigContext], FunctionLike]) -> FunctionLike:
        """Apply a plugin hook that may infer a more precise signature for a method."""
    def transform_callee_type(self, callable_name: str | None, callee: Type, args: list[Expression], arg_kinds: list[ArgKind], context: Context, arg_names: Sequence[str | None] | None = None, object_type: Type | None = None) -> Type:
        """Attempt to determine a more accurate signature for a method call.

        This is done by looking up and applying a method signature hook (if one exists for the
        given method name).

        If no matching method signature hook is found, callee is returned unmodified. The same
        happens if the arguments refer to a non-method callable (this is allowed so that the code
        calling transform_callee_type needs to perform fewer boilerplate checks).

        Note: this method is *not* called automatically as part of check_call, because in some
        cases check_call is called multiple times while checking a single call (for example when
        dealing with overloads). Instead, this method needs to be called explicitly
        (if appropriate) before the signature is passed to check_call.
        """
    def check_call_expr_with_callee_type(self, callee_type: Type, e: CallExpr, callable_name: str | None, object_type: Type | None, member: str | None = None) -> Type:
        """Type check call expression.

        The callee_type should be used as the type of callee expression. In particular,
        in case of a union type this can be a particular item of the union, so that we can
        apply plugin hooks to each item.

        The 'member', 'callable_name' and 'object_type' are only used to call plugin hooks.
        If 'callable_name' is None but 'member' is not None (member call), try constructing
        'callable_name' using 'object_type' (the base type on which the method is called),
        for example 'typing.Mapping.get'.
        """
    def check_union_call_expr(self, e: CallExpr, object_type: UnionType, member: str) -> Type:
        """Type check calling a member expression where the base type is a union."""
    def check_call(self, callee: Type, args: list[Expression], arg_kinds: list[ArgKind], context: Context, arg_names: Sequence[str | None] | None = None, callable_node: Expression | None = None, callable_name: str | None = None, object_type: Type | None = None) -> tuple[Type, Type]:
        """Type check a call.

        Also infer type arguments if the callee is a generic function.

        Return (result type, inferred callee type).

        Arguments:
            callee: type of the called value
            args: actual argument expressions
            arg_kinds: contains nodes.ARG_* constant for each argument in args
                 describing whether the argument is positional, *arg, etc.
            context: current expression context, used for inference.
            arg_names: names of arguments (optional)
            callable_node: associate the inferred callable type to this node,
                if specified
            callable_name: Fully-qualified name of the function/method to call,
                or None if unavailable (examples: 'builtins.open', 'typing.Mapping.get')
            object_type: If callable_name refers to a method, the type of the object
                on which the method is being called
        """
    def check_callable_call(self, callee: CallableType, args: list[Expression], arg_kinds: list[ArgKind], context: Context, arg_names: Sequence[str | None] | None, callable_node: Expression | None, callable_name: str | None, object_type: Type | None) -> tuple[Type, Type]:
        """Type check a call that targets a callable value.

        See the docstring of check_call for more information.
        """
    def can_return_none(self, type: TypeInfo, attr_name: str) -> bool:
        """Is the given attribute a method with a None-compatible return type?

        Overloads are only checked if there is an implementation.
        """
    def analyze_type_type_callee(self, item: ProperType, context: Context) -> Type:
        """Analyze the callee X in X(...) where X is Type[item].

        Return a Y that we can pass to check_call(Y, ...).
        """
    def infer_arg_types_in_empty_context(self, args: list[Expression]) -> list[Type]:
        """Infer argument expression types in an empty context.

        In short, we basically recurse on each argument without considering
        in what context the argument was called.
        """
    def infer_more_unions_for_recursive_type(self, type_context: Type) -> bool:
        """Adjust type inference of unions if type context has a recursive type.

        Return the old state. The caller must assign it to type_state.infer_unions
        afterwards.

        This is a hack to better support inference for recursive types.

        Note: This is performance-sensitive and must not be a context manager
        until mypyc supports them better.
        """
    def infer_arg_types_in_context(self, callee: CallableType, args: list[Expression], arg_kinds: list[ArgKind], formal_to_actual: list[list[int]]) -> list[Type]:
        """Infer argument expression types using a callable type as context.

        For example, if callee argument 2 has type List[int], infer the
        argument expression with List[int] type context.

        Returns the inferred types of *actual arguments*.
        """
    def infer_function_type_arguments_using_context(self, callable: CallableType, error_context: Context) -> CallableType:
        """Unify callable return type to type context to infer type vars.

        For example, if the return type is set[t] where 't' is a type variable
        of callable, and if the context is set[int], return callable modified
        by substituting 't' with 'int'.
        """
    def infer_function_type_arguments(self, callee_type: CallableType, args: list[Expression], arg_kinds: list[ArgKind], formal_to_actual: list[list[int]], context: Context) -> CallableType:
        """Infer the type arguments for a generic callee type.

        Infer based on the types of arguments.

        Return a derived callable type that has the arguments applied.
        """
    def infer_function_type_arguments_pass2(self, callee_type: CallableType, args: list[Expression], arg_kinds: list[ArgKind], formal_to_actual: list[list[int]], old_inferred_args: Sequence[Type | None], context: Context) -> tuple[CallableType, list[Type | None]]:
        """Perform second pass of generic function type argument inference.

        The second pass is needed for arguments with types such as Callable[[T], S],
        where both T and S are type variables, when the actual argument is a
        lambda with inferred types.  The idea is to infer the type variable T
        in the first pass (based on the types of other arguments).  This lets
        us infer the argument and return type of the lambda expression and
        thus also the type variable S in this second pass.

        Return (the callee with type vars applied, inferred actual arg types).
        """
    def argument_infer_context(self) -> ArgumentInferContext: ...
    def get_arg_infer_passes(self, arg_types: list[Type], formal_to_actual: list[list[int]], num_actuals: int) -> list[int]:
        """Return pass numbers for args for two-pass argument type inference.

        For each actual, the pass number is either 1 (first pass) or 2 (second
        pass).

        Two-pass argument type inference primarily lets us infer types of
        lambdas more effectively.
        """
    def apply_inferred_arguments(self, callee_type: CallableType, inferred_args: Sequence[Type | None], context: Context) -> CallableType:
        """Apply inferred values of type arguments to a generic function.

        Inferred_args contains the values of function type arguments.
        """
    def check_argument_count(self, callee: CallableType, actual_types: list[Type], actual_kinds: list[ArgKind], actual_names: Sequence[str | None] | None, formal_to_actual: list[list[int]], context: Context | None, object_type: Type | None = None, callable_name: str | None = None) -> bool:
        """Check that there is a value for all required arguments to a function.

        Also check that there are no duplicate values for arguments. Report found errors
        using 'messages' if it's not None. If 'messages' is given, 'context' must also be given.

        Return False if there were any errors. Otherwise return True
        """
    def check_for_extra_actual_arguments(self, callee: CallableType, actual_types: list[Type], actual_kinds: list[ArgKind], actual_names: Sequence[str | None] | None, all_actuals: dict[int, int], context: Context) -> tuple[bool, bool]:
        """Check for extra actual arguments.

        Return tuple (was everything ok,
                      was there an extra keyword argument error [used to avoid duplicate errors]).
        """
    def missing_classvar_callable_note(self, object_type: Type, callable_name: str, context: Context) -> None: ...
    def check_argument_types(self, arg_types: list[Type], arg_kinds: list[ArgKind], args: list[Expression], callee: CallableType, formal_to_actual: list[list[int]], context: Context, check_arg: ArgChecker | None = None, object_type: Type | None = None) -> None:
        """Check argument types against a callable type.

        Report errors if the argument types are not compatible.

        The check_call docstring describes some of the arguments.
        """
    def check_arg(self, caller_type: Type, original_caller_type: Type, caller_kind: ArgKind, callee_type: Type, n: int, m: int, callee: CallableType, object_type: Type | None, context: Context, outer_context: Context) -> None:
        """Check the type of a single argument in a call."""
    def check_overload_call(self, callee: Overloaded, args: list[Expression], arg_kinds: list[ArgKind], arg_names: Sequence[str | None] | None, callable_name: str | None, object_type: Type | None, context: Context) -> tuple[Type, Type]:
        """Checks a call to an overloaded function."""
    def plausible_overload_call_targets(self, arg_types: list[Type], arg_kinds: list[ArgKind], arg_names: Sequence[str | None] | None, overload: Overloaded) -> list[CallableType]:
        '''Returns all overload call targets that having matching argument counts.

        If the given args contains a star-arg (*arg or **kwarg argument), this method
        will ensure all star-arg overloads appear at the start of the list, instead
        of their usual location.

        The only exception is if the starred argument is something like a Tuple or a
        NamedTuple, which has a definitive "shape". If so, we don\'t move the corresponding
        alternative to the front since we can infer a more precise match using the original
        order.'''
    def infer_overload_return_type(self, plausible_targets: list[CallableType], args: list[Expression], arg_types: list[Type], arg_kinds: list[ArgKind], arg_names: Sequence[str | None] | None, callable_name: str | None, object_type: Type | None, context: Context) -> tuple[Type, Type] | None:
        """Attempts to find the first matching callable from the given list.

        If a match is found, returns a tuple containing the result type and the inferred
        callee type. (This tuple is meant to be eventually returned by check_call.)
        If multiple targets match due to ambiguous Any parameters, returns (AnyType, AnyType).
        If no targets match, returns None.

        Assumes all of the given targets have argument counts compatible with the caller.
        """
    def overload_erased_call_targets(self, plausible_targets: list[CallableType], arg_types: list[Type], arg_kinds: list[ArgKind], arg_names: Sequence[str | None] | None, args: list[Expression], context: Context) -> list[CallableType]:
        """Returns a list of all targets that match the caller after erasing types.

        Assumes all of the given targets have argument counts compatible with the caller.
        """
    def union_overload_result(self, plausible_targets: list[CallableType], args: list[Expression], arg_types: list[Type], arg_kinds: list[ArgKind], arg_names: Sequence[str | None] | None, callable_name: str | None, object_type: Type | None, context: Context, level: int = 0) -> list[tuple[Type, Type]] | None:
        """Accepts a list of overload signatures and attempts to match calls by destructuring
        the first union.

        Return a list of (<return type>, <inferred variant type>) if call succeeds for every
        item of the desctructured union. Returns None if there is no match.
        """
    def real_union(self, typ: Type) -> bool: ...
    def type_overrides_set(self, exprs: Sequence[Expression], overrides: Sequence[Type]) -> Iterator[None]:
        """Set _temporary_ type overrides for given expressions."""
    def combine_function_signatures(self, types: list[ProperType]) -> AnyType | CallableType:
        """Accepts a list of function signatures and attempts to combine them together into a
        new CallableType consisting of the union of all of the given arguments and return types.

        If there is at least one non-callable type, return Any (this can happen if there is
        an ambiguity because of Any in arguments).
        """
    def erased_signature_similarity(self, arg_types: list[Type], arg_kinds: list[ArgKind], arg_names: Sequence[str | None] | None, args: list[Expression], callee: CallableType, context: Context) -> bool:
        """Determine whether arguments could match the signature at runtime, after
        erasing types."""
    def apply_generic_arguments(self, callable: CallableType, types: Sequence[Type | None], context: Context, skip_unsatisfied: bool = False) -> CallableType:
        """Simple wrapper around mypy.applytype.apply_generic_arguments."""
    def check_any_type_call(self, args: list[Expression], callee: Type) -> tuple[Type, Type]: ...
    def check_union_call(self, callee: UnionType, args: list[Expression], arg_kinds: list[ArgKind], arg_names: Sequence[str | None] | None, context: Context) -> tuple[Type, Type]: ...
    def visit_member_expr(self, e: MemberExpr, is_lvalue: bool = False) -> Type:
        """Visit member expression (of form e.id)."""
    def analyze_ordinary_member_access(self, e: MemberExpr, is_lvalue: bool) -> Type:
        """Analyse member expression or member lvalue."""
    def analyze_external_member_access(self, member: str, base_type: Type, context: Context) -> Type:
        """Analyse member access that is external, i.e. it cannot
        refer to private definitions. Return the result type.
        """
    def is_literal_context(self) -> bool: ...
    def infer_literal_expr_type(self, value: LiteralValue, fallback_name: str) -> Type:
        '''Analyzes the given literal expression and determines if we should be
        inferring an Instance type, a Literal[...] type, or an Instance that
        remembers the original literal. We...

        1. ...Infer a normal Instance in most circumstances.

        2. ...Infer a Literal[...] if we\'re in a literal context. For example, if we
           were analyzing the "3" in "foo(3)" where "foo" has a signature of
           "def foo(Literal[3]) -> None", we\'d want to infer that the "3" has a
           type of Literal[3] instead of Instance.

        3. ...Infer an Instance that remembers the original Literal if we\'re declaring
           a Final variable with an inferred type -- for example, "bar" in "bar: Final = 3"
           would be assigned an Instance that remembers it originated from a \'3\'. See
           the comments in Instance\'s constructor for more details.
        '''
    def concat_tuples(self, left: TupleType, right: TupleType) -> TupleType:
        """Concatenate two fixed length tuples."""
    def visit_int_expr(self, e: IntExpr) -> Type:
        """Type check an integer literal (trivial)."""
    def visit_str_expr(self, e: StrExpr) -> Type:
        """Type check a string literal (trivial)."""
    def visit_bytes_expr(self, e: BytesExpr) -> Type:
        """Type check a bytes literal (trivial)."""
    def visit_float_expr(self, e: FloatExpr) -> Type:
        """Type check a float literal (trivial)."""
    def visit_complex_expr(self, e: ComplexExpr) -> Type:
        """Type check a complex literal."""
    def visit_ellipsis(self, e: EllipsisExpr) -> Type:
        """Type check '...'."""
    def visit_op_expr(self, e: OpExpr) -> Type:
        """Type check a binary operator expression."""
    def visit_comparison_expr(self, e: ComparisonExpr) -> Type:
        """Type check a comparison expression.

        Comparison expressions are type checked consecutive-pair-wise
        That is, 'a < b > c == d' is check as 'a < b and b > c and c == d'
        """
    def find_partial_type_ref_fast_path(self, expr: Expression) -> Type | None:
        """If expression has a partial generic type, return it without additional checks.

        In particular, this does not generate an error about a missing annotation.

        Otherwise, return None.
        """
    def dangerous_comparison(self, left: Type, right: Type, original_container: Type | None = None, *, prefer_literal: bool = True) -> bool:
        """Check for dangerous non-overlapping comparisons like 42 == 'no'.

        The original_container is the original container type for 'in' checks
        (and None for equality checks).

        Rules:
            * X and None are overlapping even in strict-optional mode. This is to allow
            'assert x is not None' for x defined as 'x = None  # type: str' in class body
            (otherwise mypy itself would have couple dozen errors because of this).
            * Optional[X] and Optional[Y] are non-overlapping if X and Y are
            non-overlapping, although technically None is overlap, it is most
            likely an error.
            * Any overlaps with everything, i.e. always safe.
            * Special case: b'abc' in b'cde' is safe.
        """
    def check_method_call_by_name(self, method: str, base_type: Type, args: list[Expression], arg_kinds: list[ArgKind], context: Context, original_type: Type | None = None) -> tuple[Type, Type]:
        """Type check a call to a named method on an object.

        Return tuple (result type, inferred method type). The 'original_type'
        is used for error messages.
        """
    def check_union_method_call_by_name(self, method: str, base_type: UnionType, args: list[Expression], arg_kinds: list[ArgKind], context: Context, original_type: Type | None = None) -> tuple[Type, Type]:
        """Type check a call to a named method on an object with union type.

        This essentially checks the call using check_method_call_by_name() for each
        union item and unions the result. We do this to allow plugins to act on
        individual union items.
        """
    def check_method_call(self, method_name: str, base_type: Type, method_type: Type, args: list[Expression], arg_kinds: list[ArgKind], context: Context) -> tuple[Type, Type]:
        """Type check a call to a method with the given name and type on an object.

        Return tuple (result type, inferred method type).
        """
    def check_op_reversible(self, op_name: str, left_type: Type, left_expr: Expression, right_type: Type, right_expr: Expression, context: Context) -> tuple[Type, Type]: ...
    def check_op(self, method: str, base_type: Type, arg: Expression, context: Context, allow_reverse: bool = False) -> tuple[Type, Type]:
        """Type check a binary operation which maps to a method call.

        Return tuple (result type, inferred operator method type).
        """
    def check_boolean_op(self, e: OpExpr, context: Context) -> Type:
        """Type check a boolean operation ('and' or 'or')."""
    def check_list_multiply(self, e: OpExpr) -> Type:
        """Type check an expression of form '[...] * e'.

        Type inference is special-cased for this common construct.
        """
    def visit_assignment_expr(self, e: AssignmentExpr) -> Type: ...
    def visit_unary_expr(self, e: UnaryExpr) -> Type:
        """Type check an unary operation ('not', '-', '+' or '~')."""
    def visit_index_expr(self, e: IndexExpr) -> Type:
        """Type check an index expression (base[index]).

        It may also represent type application.
        """
    def visit_index_expr_helper(self, e: IndexExpr) -> Type: ...
    def visit_index_with_type(self, left_type: Type, e: IndexExpr, original_type: ProperType | None = None) -> Type:
        """Analyze type of an index expression for a given type of base expression.

        The 'original_type' is used for error messages (currently used for union types).
        """
    def visit_tuple_slice_helper(self, left_type: TupleType, slic: SliceExpr) -> Type: ...
    def try_getting_int_literals(self, index: Expression) -> list[int] | None:
        """If the given expression or type corresponds to an int literal
        or a union of int literals, returns a list of the underlying ints.
        Otherwise, returns None.

        Specifically, this function is guaranteed to return a list with
        one or more ints if one one the following is true:

        1. 'expr' is a IntExpr or a UnaryExpr backed by an IntExpr
        2. 'typ' is a LiteralType containing an int
        3. 'typ' is a UnionType containing only LiteralType of ints
        """
    def nonliteral_tuple_index_helper(self, left_type: TupleType, index: Expression) -> Type: ...
    def visit_typeddict_index_expr(self, td_type: TypedDictType, index: Expression, setitem: bool = False) -> Type: ...
    def visit_enum_index_expr(self, enum_type: TypeInfo, index: Expression, context: Context) -> Type: ...
    def visit_cast_expr(self, expr: CastExpr) -> Type:
        """Type check a cast expression."""
    def visit_assert_type_expr(self, expr: AssertTypeExpr) -> Type: ...
    def visit_reveal_expr(self, expr: RevealExpr) -> Type:
        """Type check a reveal_type expression."""
    def visit_type_application(self, tapp: TypeApplication) -> Type:
        """Type check a type application (expr[type, ...]).

        There are two different options here, depending on whether expr refers
        to a type alias or directly to a generic class. In the first case we need
        to use a dedicated function typeanal.instantiate_type_alias(). This
        is due to slight differences in how type arguments are applied and checked.
        """
    def visit_type_alias_expr(self, alias: TypeAliasExpr) -> Type:
        """Right hand side of a type alias definition.

        It has the same type as if the alias itself was used in a runtime context.
        For example, here:

            A = reveal_type(List[T])
            reveal_type(A)

        both `reveal_type` instances will reveal the same type `def (...) -> builtins.list[Any]`.
        Note that type variables are implicitly substituted with `Any`.
        """
    def alias_type_in_runtime_context(self, alias: TypeAlias, *, ctx: Context, alias_definition: bool = False) -> Type:
        """Get type of a type alias (could be generic) in a runtime expression.

        Note that this function can be called only if the alias appears _not_
        as a target of type application, which is treated separately in the
        visit_type_application method. Some examples where this method is called are
        casts and instantiation:

            class LongName(Generic[T]): ...
            A = LongName[int]

            x = A()
            y = cast(A, ...)
        """
    def split_for_callable(self, t: CallableType, args: Sequence[Type], ctx: Context) -> list[Type]:
        """Handle directly applying type arguments to a variadic Callable.

        This is needed in situations where e.g. variadic class object appears in
        runtime context. For example:
            class C(Generic[T, Unpack[Ts]]): ...
            x = C[int, str]()

        We simply group the arguments that need to go into Ts variable into a TupleType,
        similar to how it is done in other places using split_with_prefix_and_suffix().
        """
    def apply_type_arguments_to_callable(self, tp: Type, args: Sequence[Type], ctx: Context) -> Type:
        """Apply type arguments to a generic callable type coming from a type object.

        This will first perform type arguments count checks, report the
        error as needed, and return the correct kind of Any. As a special
        case this returns Any for non-callable types, because if type object type
        is not callable, then an error should be already reported.
        """
    def visit_list_expr(self, e: ListExpr) -> Type:
        """Type check a list expression [...]."""
    def visit_set_expr(self, e: SetExpr) -> Type: ...
    def fast_container_type(self, e: ListExpr | SetExpr | TupleExpr, container_fullname: str) -> Type | None:
        """
        Fast path to determine the type of a list or set literal,
        based on the list of entries. This mostly impacts large
        module-level constant definitions.

        Limitations:
         - no active type context
         - no star expressions
         - the joined type of all entries must be an Instance or Tuple type
        """
    def check_lst_expr(self, e: ListExpr | SetExpr | TupleExpr, fullname: str, tag: str) -> Type: ...
    def visit_tuple_expr(self, e: TupleExpr) -> Type:
        """Type check a tuple expression."""
    def fast_dict_type(self, e: DictExpr) -> Type | None:
        """
        Fast path to determine the type of a dict literal,
        based on the list of entries. This mostly impacts large
        module-level constant definitions.

        Limitations:
         - no active type context
         - only supported star expressions are other dict instances
         - the joined types of all keys and values must be Instance or Tuple types
        """
    def check_typeddict_literal_in_context(self, e: DictExpr, typeddict_context: TypedDictType) -> Type: ...
    def visit_dict_expr(self, e: DictExpr) -> Type:
        """Type check a dict expression.

        Translate it into a call to dict(), with provisions for **expr.
        """
    def find_typeddict_context(self, context: Type | None, dict_expr: DictExpr) -> list[TypedDictType]: ...
    def visit_lambda_expr(self, e: LambdaExpr) -> Type:
        """Type check lambda expression."""
    def infer_lambda_type_using_context(self, e: LambdaExpr) -> tuple[CallableType | None, CallableType | None]:
        """Try to infer lambda expression type using context.

        Return None if could not infer type.
        The second item in the return type is the type_override parameter for check_func_item.
        """
    def visit_super_expr(self, e: SuperExpr) -> Type:
        """Type check a super expression (non-lvalue)."""
    def visit_slice_expr(self, e: SliceExpr) -> Type: ...
    def visit_list_comprehension(self, e: ListComprehension) -> Type: ...
    def visit_set_comprehension(self, e: SetComprehension) -> Type: ...
    def visit_generator_expr(self, e: GeneratorExpr) -> Type: ...
    def check_generator_or_comprehension(self, gen: GeneratorExpr, type_name: str, id_for_messages: str, additional_args: list[Type] | None = None) -> Type:
        """Type check a generator expression or a list comprehension."""
    def visit_dictionary_comprehension(self, e: DictionaryComprehension) -> Type:
        """Type check a dictionary comprehension."""
    def check_for_comp(self, e: GeneratorExpr | DictionaryComprehension) -> None:
        """Check the for_comp part of comprehensions. That is the part from 'for':
        ... for x in y if z

        Note: This adds the type information derived from the condlists to the current binder.
        """
    def visit_conditional_expr(self, e: ConditionalExpr, allow_none_return: bool = False) -> Type: ...
    def analyze_cond_branch(self, map: dict[Expression, Type] | None, node: Expression, context: Type | None, allow_none_return: bool = False) -> Type: ...
    def accept(self, node: Expression, type_context: Type | None = None, allow_none_return: bool = False, always_allow_any: bool = False, is_callee: bool = False) -> Type:
        """Type check a node in the given type context.  If allow_none_return
        is True and this expression is a call, allow it to return None.  This
        applies only to this expression and not any subexpressions.
        """
    def named_type(self, name: str) -> Instance:
        """Return an instance type with type given by the name and no type
        arguments. Alias for TypeChecker.named_type.
        """
    def is_valid_var_arg(self, typ: Type) -> bool:
        """Is a type valid as a *args argument?"""
    def is_valid_keyword_var_arg(self, typ: Type) -> bool:
        """Is a type valid as a **kwargs argument?"""
    def has_member(self, typ: Type, member: str) -> bool:
        """Does type have member with the given name?"""
    def not_ready_callback(self, name: str, context: Context) -> None:
        """Called when we can't infer the type of a variable because it's not ready yet.

        Either defer type checking of the enclosing function to the next
        pass or report an error.
        """
    def visit_yield_expr(self, e: YieldExpr) -> Type: ...
    def visit_await_expr(self, e: AwaitExpr, allow_none_return: bool = False) -> Type: ...
    def check_awaitable_expr(self, t: Type, ctx: Context, msg: str | ErrorMessage, ignore_binder: bool = False) -> Type:
        """Check the argument to `await` and extract the type of value.

        Also used by `async for` and `async with`.
        """
    def visit_yield_from_expr(self, e: YieldFromExpr, allow_none_return: bool = False) -> Type: ...
    def visit_temp_node(self, e: TempNode) -> Type: ...
    def visit_type_var_expr(self, e: TypeVarExpr) -> Type: ...
    def visit_paramspec_expr(self, e: ParamSpecExpr) -> Type: ...
    def visit_type_var_tuple_expr(self, e: TypeVarTupleExpr) -> Type: ...
    def visit_newtype_expr(self, e: NewTypeExpr) -> Type: ...
    def visit_namedtuple_expr(self, e: NamedTupleExpr) -> Type: ...
    def visit_enum_call_expr(self, e: EnumCallExpr) -> Type: ...
    def visit_typeddict_expr(self, e: TypedDictExpr) -> Type: ...
    def visit__promote_expr(self, e: PromoteExpr) -> Type: ...
    def visit_star_expr(self, e: StarExpr) -> Type: ...
    def object_type(self) -> Instance:
        """Return instance type 'object'."""
    def bool_type(self) -> Instance:
        """Return instance type 'bool'."""
    @overload
    def narrow_type_from_binder(self, expr: Expression, known_type: Type) -> Type: ...
    @overload
    def narrow_type_from_binder(self, expr: Expression, known_type: Type, skip_non_overlapping: bool) -> Type | None: ...

def has_any_type(t: Type, ignore_in_type_obj: bool = False) -> bool:
    """Whether t contains an Any type"""

class HasAnyType(types.BoolTypeQuery):
    ignore_in_type_obj: Incomplete
    def __init__(self, ignore_in_type_obj: bool) -> None: ...
    def visit_any(self, t: AnyType) -> bool: ...
    def visit_callable_type(self, t: CallableType) -> bool: ...
    def visit_type_var(self, t: TypeVarType) -> bool: ...
    def visit_param_spec(self, t: ParamSpecType) -> bool: ...
    def visit_type_var_tuple(self, t: TypeVarTupleType) -> bool: ...

def has_coroutine_decorator(t: Type) -> bool:
    """Whether t came from a function decorated with `@coroutine`."""
def is_async_def(t: Type) -> bool:
    """Whether t came from a function defined using `async def`."""
def is_non_empty_tuple(t: Type) -> bool: ...
def is_duplicate_mapping(mapping: list[int], actual_types: list[Type], actual_kinds: list[ArgKind]) -> bool: ...
def replace_callable_return_type(c: CallableType, new_ret_type: Type) -> CallableType:
    """Return a copy of a callable type with a different return type."""

class ArgInferSecondPassQuery(types.BoolTypeQuery):
    """Query whether an argument type should be inferred in the second pass.

    The result is True if the type has a type variable in a callable return
    type anywhere. For example, the result for Callable[[], T] is True if t is
    a type variable.
    """
    def __init__(self) -> None: ...
    def visit_callable_type(self, t: CallableType) -> bool: ...

class HasTypeVarQuery(types.BoolTypeQuery):
    """Visitor for querying whether a type has a type variable component."""
    def __init__(self) -> None: ...
    def visit_type_var(self, t: TypeVarType) -> bool: ...

def has_erased_component(t: Type | None) -> bool: ...

class HasErasedComponentsQuery(types.BoolTypeQuery):
    """Visitor for querying whether a type has an erased component."""
    def __init__(self) -> None: ...
    def visit_erased_type(self, t: ErasedType) -> bool: ...

def has_uninhabited_component(t: Type | None) -> bool: ...

class HasUninhabitedComponentsQuery(types.BoolTypeQuery):
    """Visitor for querying whether a type has an UninhabitedType component."""
    def __init__(self) -> None: ...
    def visit_uninhabited_type(self, t: UninhabitedType) -> bool: ...

def arg_approximate_similarity(actual: Type, formal: Type) -> bool:
    '''Return if caller argument (actual) is roughly compatible with signature arg (formal).

    This function is deliberately loose and will report two types are similar
    as long as their "shapes" are plausibly the same.

    This is useful when we\'re doing error reporting: for example, if we\'re trying
    to select an overload alternative and there\'s no exact match, we can use
    this function to help us identify which alternative the user might have
    *meant* to match.
    '''
def any_causes_overload_ambiguity(items: list[CallableType], return_types: list[Type], arg_types: list[Type], arg_kinds: list[ArgKind], arg_names: Sequence[str | None] | None) -> bool:
    """May an argument containing 'Any' cause ambiguous result type on call to overloaded function?

    Note that this sometimes returns True even if there is no ambiguity, since a correct
    implementation would be complex (and the call would be imprecisely typed due to Any
    types anyway).

    Args:
        items: Overload items matching the actual arguments
        arg_types: Actual argument types
        arg_kinds: Actual argument kinds
        arg_names: Actual argument names
    """
def all_same_types(types: list[Type]) -> bool: ...
def merge_typevars_in_callables_by_name(callables: Sequence[CallableType]) -> tuple[list[CallableType], list[TypeVarType]]:
    '''Takes all the typevars present in the callables and \'combines\' the ones with the same name.

    For example, suppose we have two callables with signatures "f(x: T, y: S) -> T" and
    "f(x: List[Tuple[T, S]]) -> Tuple[T, S]". Both callables use typevars named "T" and
    "S", but we treat them as distinct, unrelated typevars. (E.g. they could both have
    distinct ids.)

    If we pass in both callables into this function, it returns a list containing two
    new callables that are identical in signature, but use the same underlying TypeVarType
    for T and S.

    This is useful if we want to take the output lists and "merge" them into one callable
    in some way -- for example, when unioning together overloads.

    Returns both the new list of callables and a list of all distinct TypeVarType objects used.
    '''
def try_getting_literal(typ: Type) -> ProperType:
    """If possible, get a more precise literal type for a given type."""
def is_expr_literal_type(node: Expression) -> bool:
    """Returns 'true' if the given node is a Literal"""
def has_bytes_component(typ: Type) -> bool:
    """Is this one of builtin byte types, or a union that contains it?"""
def type_info_from_type(typ: Type) -> TypeInfo | None:
    """Gets the TypeInfo for a type, indirecting through things like type variables and tuples."""
def is_operator_method(fullname: str | None) -> bool: ...
def get_partial_instance_type(t: Type | None) -> PartialType | None: ...
