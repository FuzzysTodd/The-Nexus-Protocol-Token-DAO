from mypy.copytype import copy_type as copy_type
from mypy.expandtype import expand_type as expand_type, expand_type_by_instance as expand_type_by_instance
from mypy.maptype import map_instance_to_supertype as map_instance_to_supertype
from mypy.nodes import ARG_POS as ARG_POS, ARG_STAR as ARG_STAR, ARG_STAR2 as ARG_STAR2, Decorator as Decorator, Expression as Expression, FuncBase as FuncBase, FuncDef as FuncDef, FuncItem as FuncItem, OverloadedFuncDef as OverloadedFuncDef, SYMBOL_FUNCBASE_TYPES as SYMBOL_FUNCBASE_TYPES, StrExpr as StrExpr, TypeInfo as TypeInfo, Var as Var
from mypy.state import state as state
from mypy.types import AnyType as AnyType, CallableType as CallableType, ENUM_REMOVED_PROPS as ENUM_REMOVED_PROPS, ExtraAttrs as ExtraAttrs, FormalArgument as FormalArgument, FunctionLike as FunctionLike, Instance as Instance, LiteralType as LiteralType, NoneType as NoneType, Overloaded as Overloaded, ParamSpecType as ParamSpecType, Parameters as Parameters, PartialType as PartialType, ProperType as ProperType, TupleType as TupleType, Type as Type, TypeAliasType as TypeAliasType, TypeOfAny as TypeOfAny, TypeQuery as TypeQuery, TypeType as TypeType, TypeVarLikeType as TypeVarLikeType, TypeVarTupleType as TypeVarTupleType, TypeVarType as TypeVarType, TypedDictType as TypedDictType, UninhabitedType as UninhabitedType, UnionType as UnionType, UnpackType as UnpackType, flatten_nested_unions as flatten_nested_unions, get_proper_type as get_proper_type, get_proper_types as get_proper_types
from mypy.typevars import fill_typevars as fill_typevars
from typing import List, Sequence, TypeVar

def is_recursive_pair(s: Type, t: Type) -> bool:
    """Is this a pair of recursive types?

    There may be more cases, and we may be forced to use e.g. has_recursive_types()
    here, but this function is called in very hot code, so we try to keep it simple
    and return True only in cases we know may have problems.
    """
def tuple_fallback(typ: TupleType) -> Instance:
    """Return fallback type for a tuple."""
def get_self_type(func: CallableType, default_self: Instance | TupleType) -> Type | None: ...
def type_object_type_from_function(signature: FunctionLike, info: TypeInfo, def_info: TypeInfo, fallback: Instance, is_new: bool) -> FunctionLike: ...
def class_callable(init_type: CallableType, info: TypeInfo, type_type: Instance, special_sig: str | None, is_new: bool, orig_self_type: Type | None = None) -> CallableType:
    """Create a type object type based on the signature of __init__."""
def map_type_from_supertype(typ: Type, sub_info: TypeInfo, super_info: TypeInfo) -> Type:
    """Map type variables in a type defined in a supertype context to be valid
    in the subtype context. Assume that the result is unique; if more than
    one type is possible, return one of the alternatives.

    For example, assume

      class D(Generic[S]): ...
      class C(D[E[T]], Generic[T]): ...

    Now S in the context of D would be mapped to E[T] in the context of C.
    """
def supported_self_type(typ: ProperType) -> bool:
    """Is this a supported kind of explicit self-types?

    Currently, this means a X or Type[X], where X is an instance or
    a type variable with an instance upper bound.
    """
F = TypeVar('F', bound=FunctionLike)

def bind_self(method: F, original_type: Type | None = None, is_classmethod: bool = False) -> F:
    '''Return a copy of `method`, with the type of its first parameter (usually
    self or cls) bound to original_type.

    If the type of `self` is a generic type (T, or Type[T] for classmethods),
    instantiate every occurrence of type with original_type in the rest of the
    signature and in the return type.

    original_type is the type of E in the expression E.copy(). It is None in
    compatibility checks. In this case we treat it as the erasure of the
    declared type of self.

    This way we can express "the type of self". For example:

    T = TypeVar(\'T\', bound=\'A\')
    class A:
        def copy(self: T) -> T: ...

    class B(A): pass

    b = B().copy()  # type: B

    '''
def erase_to_bound(t: Type) -> Type: ...
def callable_corresponding_argument(typ: CallableType | Parameters, model: FormalArgument) -> FormalArgument | None:
    """Return the argument a function that corresponds to `model`"""
def simple_literal_type(t: ProperType | None) -> Instance | None:
    """Extract the underlying fallback Instance type for a simple Literal"""
def is_simple_literal(t: ProperType) -> bool: ...
def make_simplified_union(items: Sequence[Type], line: int = -1, column: int = -1, *, keep_erased: bool = False, contract_literals: bool = True) -> ProperType:
    """Build union type with redundant union items removed.

    If only a single item remains, this may return a non-union type.

    Examples:

    * [int, str] -> Union[int, str]
    * [int, object] -> object
    * [int, int] -> int
    * [int, Any] -> Union[int, Any] (Any types are not simplified away!)
    * [Any, Any] -> Any
    * [int, Union[bytes, str]] -> Union[int, bytes, str]

    Note: This must NOT be used during semantic analysis, since TypeInfos may not
          be fully initialized.

    The keep_erased flag is used for type inference against union types
    containing type variables. If set to True, keep all ErasedType items.

    The contract_literals flag indicates whether we need to contract literal types
    back into a sum type. Set it to False when called by try_expanding_sum_type_
    to_union().
    """
def true_only(t: Type) -> ProperType:
    """
    Restricted version of t with only True-ish values
    """
def false_only(t: Type) -> ProperType:
    """
    Restricted version of t with only False-ish values
    """
def true_or_false(t: Type) -> ProperType:
    """
    Unrestricted version of t with both True-ish and False-ish values
    """
def erase_def_to_union_or_bound(tdef: TypeVarLikeType) -> Type: ...
def erase_to_union_or_bound(typ: TypeVarType) -> ProperType: ...
def function_type(func: FuncBase, fallback: Instance) -> FunctionLike: ...
def callable_type(fdef: FuncItem, fallback: Instance, ret_type: Type | None = None) -> CallableType: ...
def try_getting_str_literals(expr: Expression, typ: Type) -> list[str] | None:
    """If the given expression or type corresponds to a string literal
    or a union of string literals, returns a list of the underlying strings.
    Otherwise, returns None.

    Specifically, this function is guaranteed to return a list with
    one or more strings if one of the following is true:

    1. 'expr' is a StrExpr
    2. 'typ' is a LiteralType containing a string
    3. 'typ' is a UnionType containing only LiteralType of strings
    """
def try_getting_str_literals_from_type(typ: Type) -> list[str] | None:
    '''If the given expression or type corresponds to a string Literal
    or a union of string Literals, returns a list of the underlying strings.
    Otherwise, returns None.

    For example, if we had the type \'Literal["foo", "bar"]\' as input, this function
    would return a list of strings ["foo", "bar"].
    '''
def try_getting_int_literals_from_type(typ: Type) -> list[int] | None:
    """If the given expression or type corresponds to an int Literal
    or a union of int Literals, returns a list of the underlying ints.
    Otherwise, returns None.

    For example, if we had the type 'Literal[1, 2, 3]' as input, this function
    would return a list of ints [1, 2, 3].
    """
T = TypeVar('T')

def try_getting_literals_from_type(typ: Type, target_literal_type: type[T], target_fullname: str) -> list[T] | None:
    """If the given expression or type corresponds to a Literal or
    union of Literals where the underlying values correspond to the given
    target type, returns a list of those underlying values. Otherwise,
    returns None.
    """
def is_literal_type_like(t: Type | None) -> bool:
    """Returns 'true' if the given type context is potentially either a LiteralType,
    a Union of LiteralType, or something similar.
    """
def is_singleton_type(typ: Type) -> bool:
    '''Returns \'true\' if this type is a "singleton type" -- if there exists
    exactly only one runtime value associated with this type.

    That is, given two values \'a\' and \'b\' that have the same type \'t\',
    \'is_singleton_type(t)\' returns True if and only if the expression \'a is b\' is
    always true.

    Currently, this returns True when given NoneTypes, enum LiteralTypes,
    enum types with a single value and ... (Ellipses).

    Note that other kinds of LiteralTypes cannot count as singleton types. For
    example, suppose we do \'a = 100000 + 1\' and \'b = 100001\'. It is not guaranteed
    that \'a is b\' will always be true -- some implementations of Python will end up
    constructing two distinct instances of 100001.
    '''
def try_expanding_sum_type_to_union(typ: Type, target_fullname: str) -> ProperType:
    """Attempts to recursively expand any enum Instances with the given target_fullname
    into a Union of all of its component LiteralTypes.

    For example, if we have:

        class Color(Enum):
            RED = 1
            BLUE = 2
            YELLOW = 3

        class Status(Enum):
            SUCCESS = 1
            FAILURE = 2
            UNKNOWN = 3

    ...and if we call `try_expanding_enum_to_union(Union[Color, Status], 'module.Color')`,
    this function will return Literal[Color.RED, Color.BLUE, Color.YELLOW, Status].
    """
def try_contracting_literals_in_union(types: Sequence[Type]) -> list[ProperType]:
    """Contracts any literal types back into a sum type if possible.

    Will replace the first instance of the literal with the sum type and
    remove all others.

    If we call `try_contracting_union(Literal[Color.RED, Color.BLUE, Color.YELLOW])`,
    this function will return Color.

    We also treat `Literal[True, False]` as `bool`.
    """
def coerce_to_literal(typ: Type) -> Type:
    """Recursively converts any Instances that have a last_known_value or are
    instances of enum types with a single value into the corresponding LiteralType.
    """
def get_type_vars(tp: Type) -> list[TypeVarType]: ...

class TypeVarExtractor(TypeQuery[List[TypeVarType]]):
    def __init__(self) -> None: ...
    def visit_type_var(self, t: TypeVarType) -> list[TypeVarType]: ...

def custom_special_method(typ: Type, name: str, check_all: bool = False) -> bool:
    """Does this type have a custom special method such as __format__() or __eq__()?

    If check_all is True ensure all items of a union have a custom method, not just some.
    """
def separate_union_literals(t: UnionType) -> tuple[Sequence[LiteralType], Sequence[Type]]:
    """Separate literals from other members in a union type."""
def try_getting_instance_fallback(typ: Type) -> Instance | None:
    """Returns the Instance fallback for this type if one exists or None."""
def fixup_partial_type(typ: Type) -> Type:
    """Convert a partial type that we couldn't resolve into something concrete.

    This means, for None we make it Optional[Any], and for anything else we
    fill in all of the type arguments with Any.
    """
def get_protocol_member(left: Instance, member: str, class_obj: bool) -> ProperType | None: ...
