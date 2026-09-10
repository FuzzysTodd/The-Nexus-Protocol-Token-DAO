from _typeshed import Incomplete
from mypy.erasetype import erase_type as erase_type
from mypy.expandtype import expand_self_type as expand_self_type, expand_type_by_instance as expand_type_by_instance
from mypy.maptype import map_instance_to_supertype as map_instance_to_supertype
from mypy.nodes import ARG_STAR as ARG_STAR, ARG_STAR2 as ARG_STAR2, CONTRAVARIANT as CONTRAVARIANT, COVARIANT as COVARIANT, Decorator as Decorator, FuncBase as FuncBase, OverloadedFuncDef as OverloadedFuncDef, TypeInfo as TypeInfo, Var as Var
from mypy.options import Options as Options
from mypy.state import state as state
from mypy.types import AnyType as AnyType, CallableType as CallableType, DeletedType as DeletedType, ErasedType as ErasedType, FormalArgument as FormalArgument, FunctionLike as FunctionLike, Instance as Instance, LiteralType as LiteralType, MYPYC_NATIVE_INT_NAMES as MYPYC_NATIVE_INT_NAMES, NoneType as NoneType, NormalizedCallableType as NormalizedCallableType, Overloaded as Overloaded, ParamSpecType as ParamSpecType, Parameters as Parameters, PartialType as PartialType, ProperType as ProperType, TUPLE_LIKE_INSTANCE_NAMES as TUPLE_LIKE_INSTANCE_NAMES, TYPED_NAMEDTUPLE_NAMES as TYPED_NAMEDTUPLE_NAMES, TupleType as TupleType, Type as Type, TypeAliasType as TypeAliasType, TypeOfAny as TypeOfAny, TypeType as TypeType, TypeVarTupleType as TypeVarTupleType, TypeVarType as TypeVarType, TypeVisitor as TypeVisitor, TypedDictType as TypedDictType, UnboundType as UnboundType, UninhabitedType as UninhabitedType, UnionType as UnionType, UnpackType as UnpackType, get_proper_type as get_proper_type, is_named_instance as is_named_instance
from mypy.types_utils import flatten_types as flatten_types
from mypy.typestate import SubtypeKind as SubtypeKind, type_state as type_state
from mypy.typevars import fill_typevars_with_any as fill_typevars_with_any
from mypy.typevartuples import extract_unpack as extract_unpack, fully_split_with_mapped_and_template as fully_split_with_mapped_and_template
from typing import Callable, Iterator, TypeVar
from typing_extensions import Final, TypeAlias as _TypeAlias

IS_SETTABLE: Final[int]
IS_CLASSVAR: Final[int]
IS_CLASS_OR_STATIC: Final[int]
IS_VAR: Final[int]
TypeParameterChecker: _TypeAlias

class SubtypeContext:
    ignore_type_params: Incomplete
    ignore_pos_arg_names: Incomplete
    ignore_declared_variance: Incomplete
    ignore_promotions: Incomplete
    ignore_uninhabited: Incomplete
    erase_instances: Incomplete
    keep_erased_types: Incomplete
    options: Incomplete
    def __init__(self, *, ignore_type_params: bool = False, ignore_pos_arg_names: bool = False, ignore_declared_variance: bool = False, ignore_promotions: bool = False, ignore_uninhabited: bool = False, erase_instances: bool = False, keep_erased_types: bool = False, options: Options | None = None) -> None: ...
    def check_context(self, proper_subtype: bool) -> None: ...

def is_subtype(left: Type, right: Type, *, subtype_context: SubtypeContext | None = None, ignore_type_params: bool = False, ignore_pos_arg_names: bool = False, ignore_declared_variance: bool = False, ignore_promotions: bool = False, ignore_uninhabited: bool = False, options: Options | None = None) -> bool:
    """Is 'left' subtype of 'right'?

    Also consider Any to be a subtype of any type, and vice versa. This
    recursively applies to components of composite types (List[int] is subtype
    of List[Any], for example).

    type_parameter_checker is used to check the type parameters (for example,
    A with B in is_subtype(C[A], C[B]). The default checks for subtype relation
    between the type arguments (e.g., A and B), taking the variance of the
    type var into account.
    """
def is_proper_subtype(left: Type, right: Type, *, subtype_context: SubtypeContext | None = None, ignore_promotions: bool = False, ignore_uninhabited: bool = False, erase_instances: bool = False, keep_erased_types: bool = False) -> bool:
    """Is left a proper subtype of right?

    For proper subtypes, there's no need to rely on compatibility due to
    Any types. Every usable type is a proper subtype of itself.

    If erase_instances is True, erase left instance *after* mapping it to supertype
    (this is useful for runtime isinstance() checks). If keep_erased_types is True,
    do not consider ErasedType a subtype of all types (used by type inference against unions).
    """
def is_equivalent(a: Type, b: Type, *, ignore_type_params: bool = False, ignore_pos_arg_names: bool = False, options: Options | None = None, subtype_context: SubtypeContext | None = None) -> bool: ...
def is_same_type(a: Type, b: Type, ignore_promotions: bool = True, subtype_context: SubtypeContext | None = None) -> bool:
    """Are these types proper subtypes of each other?

    This means types may have different representation (e.g. an alias, or
    a non-simplified union) but are semantically exchangeable in all contexts.
    """
def check_type_parameter(left: Type, right: Type, variance: int, proper_subtype: bool, subtype_context: SubtypeContext) -> bool: ...

class SubtypeVisitor(TypeVisitor[bool]):
    right: Incomplete
    orig_right: Incomplete
    proper_subtype: Incomplete
    subtype_context: Incomplete
    options: Incomplete
    def __init__(self, right: Type, subtype_context: SubtypeContext, proper_subtype: bool) -> None: ...
    @staticmethod
    def build_subtype_kind(subtype_context: SubtypeContext, proper_subtype: bool) -> SubtypeKind: ...
    def visit_unbound_type(self, left: UnboundType) -> bool: ...
    def visit_any(self, left: AnyType) -> bool: ...
    def visit_none_type(self, left: None) -> bool: ...
    def visit_uninhabited_type(self, left: UninhabitedType) -> bool: ...
    def visit_erased_type(self, left: ErasedType) -> bool: ...
    def visit_deleted_type(self, left: DeletedType) -> bool: ...
    def visit_instance(self, left: Instance) -> bool: ...
    def visit_type_var(self, left: TypeVarType) -> bool: ...
    def visit_param_spec(self, left: ParamSpecType) -> bool: ...
    def visit_type_var_tuple(self, left: TypeVarTupleType) -> bool: ...
    def visit_unpack_type(self, left: UnpackType) -> bool: ...
    def visit_parameters(self, left: Parameters) -> bool: ...
    def visit_callable_type(self, left: CallableType) -> bool: ...
    def visit_tuple_type(self, left: TupleType) -> bool: ...
    def visit_typeddict_type(self, left: TypedDictType) -> bool: ...
    def visit_literal_type(self, left: LiteralType) -> bool: ...
    def visit_overloaded(self, left: Overloaded) -> bool: ...
    def visit_union_type(self, left: UnionType) -> bool: ...
    def visit_partial_type(self, left: PartialType) -> bool: ...
    def visit_type_type(self, left: TypeType) -> bool: ...
    def visit_type_alias_type(self, left: TypeAliasType) -> bool: ...
T = TypeVar('T', bound=Type)

def pop_on_exit(stack: list[tuple[T, T]], left: T, right: T) -> Iterator[None]: ...
def is_protocol_implementation(left: Instance, right: Instance, proper_subtype: bool = False, class_obj: bool = False, skip: list[str] | None = None) -> bool:
    """Check whether 'left' implements the protocol 'right'.

    If 'proper_subtype' is True, then check for a proper subtype.
    Treat recursive protocols by using the 'assuming' structural subtype matrix
    (in sparse representation, i.e. as a list of pairs (subtype, supertype)),
    see also comment in nodes.TypeInfo. When we enter a check for classes
    (A, P), defined as following::

      class P(Protocol):
          def f(self) -> P: ...
      class A:
          def f(self) -> A: ...

    this results in A being a subtype of P without infinite recursion.
    On every false result, we pop the assumption, thus avoiding an infinite recursion
    as well.
    """
def find_member(name: str, itype: Instance, subtype: Type, is_operator: bool = False, class_obj: bool = False) -> Type | None:
    """Find the type of member by 'name' in 'itype's TypeInfo.

    Find the member type after applying type arguments from 'itype', and binding
    'self' to 'subtype'. Return None if member was not found.
    """
def get_member_flags(name: str, itype: Instance, class_obj: bool = False) -> set[int]:
    """Detect whether a member 'name' is settable, whether it is an
    instance or class variable, and whether it is class or static method.

    The flags are defined as following:
    * IS_SETTABLE: whether this attribute can be set, not set for methods and
      non-settable properties;
    * IS_CLASSVAR: set if the variable is annotated as 'x: ClassVar[t]';
    * IS_CLASS_OR_STATIC: set for methods decorated with @classmethod or
      with @staticmethod.
    """
def find_node_type(node: Var | FuncBase, itype: Instance, subtype: Type, class_obj: bool = False) -> Type:
    """Find type of a variable or method 'node' (maybe also a decorated method).
    Apply type arguments from 'itype', and bind 'self' to 'subtype'.
    """
def non_method_protocol_members(tp: TypeInfo) -> list[str]:
    """Find all non-callable members of a protocol."""
def is_callable_compatible(left: CallableType, right: CallableType, *, is_compat: Callable[[Type, Type], bool], is_compat_return: Callable[[Type, Type], bool] | None = None, ignore_return: bool = False, ignore_pos_arg_names: bool = False, check_args_covariantly: bool = False, allow_partial_overlap: bool = False, strict_concatenate: bool = False) -> bool:
    '''Is the left compatible with the right, using the provided compatibility check?

    is_compat:
        The check we want to run against the parameters.

    is_compat_return:
        The check we want to run against the return type.
        If None, use the \'is_compat\' check.

    check_args_covariantly:
        If true, check if the left\'s args is compatible with the right\'s
        instead of the other way around (contravariantly).

        This function is mostly used to check if the left is a subtype of the right which
        is why the default is to check the args contravariantly. However, it\'s occasionally
        useful to check the args using some other check, so we leave the variance
        configurable.

        For example, when checking the validity of overloads, it\'s useful to see if
        the first overload alternative has more precise arguments then the second.
        We would want to check the arguments covariantly in that case.

        Note! The following two function calls are NOT equivalent:

            is_callable_compatible(f, g, is_compat=is_subtype, check_args_covariantly=False)
            is_callable_compatible(g, f, is_compat=is_subtype, check_args_covariantly=True)

        The two calls are similar in that they both check the function arguments in
        the same direction: they both run `is_subtype(argument_from_g, argument_from_f)`.

        However, the two calls differ in which direction they check things like
        keyword arguments. For example, suppose f and g are defined like so:

            def f(x: int, *y: int) -> int: ...
            def g(x: int) -> int: ...

        In this case, the first call will succeed and the second will fail: f is a
        valid stand-in for g but not vice-versa.

    allow_partial_overlap:
        By default this function returns True if and only if *all* calls to left are
        also calls to right (with respect to the provided \'is_compat\' function).

        If this parameter is set to \'True\', we return True if *there exists at least one*
        call to left that\'s also a call to right.

        In other words, we perform an existential check instead of a universal one;
        we require left to only overlap with right instead of being a subset.

        For example, suppose we set \'is_compat\' to some subtype check and compare following:

            f(x: float, y: str = "...", *args: bool) -> str
            g(*args: int) -> str

        This function would normally return \'False\': f is not a subtype of g.
        However, we would return True if this parameter is set to \'True\': the two
        calls are compatible if the user runs "f_or_g(3)". In the context of that
        specific call, the two functions effectively have signatures of:

            f2(float) -> str
            g2(int) -> str

        Here, f2 is a valid subtype of g2 so we return True.

        Specifically, if this parameter is set this function will:

        -   Ignore optional arguments on either the left or right that have no
            corresponding match.
        -   No longer mandate optional arguments on either side are also optional
            on the other.
        -   No longer mandate that if right has a *arg or **kwarg that left must also
            have the same.

        Note: when this argument is set to True, this function becomes "symmetric" --
        the following calls are equivalent:

            is_callable_compatible(f, g,
                                   is_compat=some_check,
                                   check_args_covariantly=False,
                                   allow_partial_overlap=True)
            is_callable_compatible(g, f,
                                   is_compat=some_check,
                                   check_args_covariantly=True,
                                   allow_partial_overlap=True)

        If the \'some_check\' function is also symmetric, the two calls would be equivalent
        whether or not we check the args covariantly.
    '''
def are_trivial_parameters(param: Parameters | NormalizedCallableType) -> bool: ...
def are_parameters_compatible(left: Parameters | NormalizedCallableType, right: Parameters | NormalizedCallableType, *, is_compat: Callable[[Type, Type], bool], ignore_pos_arg_names: bool = False, check_args_covariantly: bool = False, allow_partial_overlap: bool = False, strict_concatenate_check: bool = True) -> bool:
    """Helper function for is_callable_compatible, used for Parameter compatibility"""
def are_args_compatible(left: FormalArgument, right: FormalArgument, ignore_pos_arg_names: bool, allow_partial_overlap: bool, is_compat: Callable[[Type, Type], bool]) -> bool: ...
def flip_compat_check(is_compat: Callable[[Type, Type], bool]) -> Callable[[Type, Type], bool]: ...
def unify_generic_callable(type: NormalizedCallableType, target: NormalizedCallableType, ignore_return: bool, return_constraint_direction: int | None = None) -> NormalizedCallableType | None:
    """Try to unify a generic callable type with another callable type.

    Return unified CallableType if successful; otherwise, return None.
    """
def try_restrict_literal_union(t: UnionType, s: Type) -> list[Type] | None:
    """Return the items of t, excluding any occurrence of s, if and only if
      - t only contains simple literals
      - s is a simple literal

    Otherwise, returns None
    """
def restrict_subtype_away(t: Type, s: Type) -> Type:
    """Return t minus s for runtime type assertions.

    If we can't determine a precise result, return a supertype of the
    ideal result (just t is a valid result).

    This is used for type inference of runtime type checks such as
    isinstance(). Currently, this just removes elements of a union type.
    """
def covers_at_runtime(item: Type, supertype: Type) -> bool:
    """Will isinstance(item, supertype) always return True at runtime?"""
def is_more_precise(left: Type, right: Type, *, ignore_promotions: bool = False) -> bool:
    """Check if left is a more precise type than right.

    A left is a proper subtype of right, left is also more precise than
    right. Also, if right is Any, left is more precise than right, for
    any left.
    """
