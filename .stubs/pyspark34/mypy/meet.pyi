from _typeshed import Incomplete
from mypy import join as join
from mypy.erasetype import erase_type as erase_type
from mypy.maptype import map_instance_to_supertype as map_instance_to_supertype
from mypy.state import state as state
from mypy.subtypes import is_callable_compatible as is_callable_compatible, is_equivalent as is_equivalent, is_proper_subtype as is_proper_subtype, is_same_type as is_same_type, is_subtype as is_subtype
from mypy.typeops import is_recursive_pair as is_recursive_pair, make_simplified_union as make_simplified_union, tuple_fallback as tuple_fallback
from mypy.types import AnyType as AnyType, CallableType as CallableType, DeletedType as DeletedType, ErasedType as ErasedType, FunctionLike as FunctionLike, Instance as Instance, LiteralType as LiteralType, MYPYC_NATIVE_INT_NAMES as MYPYC_NATIVE_INT_NAMES, NoneType as NoneType, Overloaded as Overloaded, ParamSpecType as ParamSpecType, Parameters as Parameters, PartialType as PartialType, ProperType as ProperType, TupleType as TupleType, Type as Type, TypeAliasType as TypeAliasType, TypeGuardedType as TypeGuardedType, TypeOfAny as TypeOfAny, TypeType as TypeType, TypeVarLikeType as TypeVarLikeType, TypeVarTupleType as TypeVarTupleType, TypeVarType as TypeVarType, TypeVisitor as TypeVisitor, TypedDictType as TypedDictType, UnboundType as UnboundType, UninhabitedType as UninhabitedType, UnionType as UnionType, UnpackType as UnpackType, get_proper_type as get_proper_type, get_proper_types as get_proper_types
from typing import Callable

def trivial_meet(s: Type, t: Type) -> ProperType:
    """Return one of types (expanded) if it is a subtype of other, otherwise bottom type."""
def meet_types(s: Type, t: Type) -> ProperType:
    """Return the greatest lower bound of two types."""
def narrow_declared_type(declared: Type, narrowed: Type) -> Type:
    """Return the declared type narrowed down to another type."""
def get_possible_variants(typ: Type) -> list[Type]:
    '''This function takes any "Union-like" type and returns a list of the available "options".

    Specifically, there are currently exactly three different types that can have
    "variants" or are "union-like":

    - Unions
    - TypeVars with value restrictions
    - Overloads

    This function will return a list of each "option" present in those types.

    If this function receives any other type, we return a list containing just that
    original type. (E.g. pretend the type was contained within a singleton union).

    The only current exceptions are regular TypeVars and ParamSpecs. For these "TypeVarLike"s,
    we return a list containing that TypeVarLike\'s upper bound.

    This function is useful primarily when checking to see if two types are overlapping:
    the algorithm to check if two unions are overlapping is fundamentally the same as
    the algorithm for checking if two overloads are overlapping.

    Normalizing both kinds of types in the same way lets us reuse the same algorithm
    for both.
    '''
def is_enum_overlapping_union(x: ProperType, y: ProperType) -> bool:
    """Return True if x is an Enum, and y is an Union with at least one Literal from x"""
def is_literal_in_union(x: ProperType, y: ProperType) -> bool:
    """Return True if x is a Literal and y is an Union that includes x"""
def is_overlapping_types(left: Type, right: Type, ignore_promotions: bool = False, prohibit_none_typevar_overlap: bool = False, ignore_uninhabited: bool = False) -> bool:
    """Can a value of type 'left' also be of type 'right' or vice-versa?

    If 'ignore_promotions' is True, we ignore promotions while checking for overlaps.
    If 'prohibit_none_typevar_overlap' is True, we disallow None from overlapping with
    TypeVars (in both strict-optional and non-strict-optional mode).
    """
def is_overlapping_erased_types(left: Type, right: Type, *, ignore_promotions: bool = False) -> bool:
    """The same as 'is_overlapping_erased_types', except the types are erased first."""
def are_typed_dicts_overlapping(left: TypedDictType, right: TypedDictType, *, ignore_promotions: bool = False, prohibit_none_typevar_overlap: bool = False) -> bool:
    """Returns 'true' if left and right are overlapping TypeDictTypes."""
def are_tuples_overlapping(left: Type, right: Type, *, ignore_promotions: bool = False, prohibit_none_typevar_overlap: bool = False) -> bool:
    """Returns true if left and right are overlapping tuples."""
def adjust_tuple(left: ProperType, r: ProperType) -> TupleType | None:
    """Find out if `left` is a Tuple[A, ...], and adjust its length to `right`"""
def is_tuple(typ: Type) -> bool: ...

class TypeMeetVisitor(TypeVisitor[ProperType]):
    s: Incomplete
    def __init__(self, s: ProperType) -> None: ...
    def visit_unbound_type(self, t: UnboundType) -> ProperType: ...
    def visit_any(self, t: AnyType) -> ProperType: ...
    def visit_union_type(self, t: UnionType) -> ProperType: ...
    def visit_none_type(self, t: None) -> ProperType: ...
    def visit_uninhabited_type(self, t: UninhabitedType) -> ProperType: ...
    def visit_deleted_type(self, t: DeletedType) -> ProperType: ...
    def visit_erased_type(self, t: ErasedType) -> ProperType: ...
    def visit_type_var(self, t: TypeVarType) -> ProperType: ...
    def visit_param_spec(self, t: ParamSpecType) -> ProperType: ...
    def visit_type_var_tuple(self, t: TypeVarTupleType) -> ProperType: ...
    def visit_unpack_type(self, t: UnpackType) -> ProperType: ...
    def visit_parameters(self, t: Parameters) -> ProperType: ...
    def visit_instance(self, t: Instance) -> ProperType: ...
    def visit_callable_type(self, t: CallableType) -> ProperType: ...
    def visit_overloaded(self, t: Overloaded) -> ProperType: ...
    def visit_tuple_type(self, t: TupleType) -> ProperType: ...
    def visit_typeddict_type(self, t: TypedDictType) -> ProperType: ...
    def visit_literal_type(self, t: LiteralType) -> ProperType: ...
    def visit_partial_type(self, t: PartialType) -> ProperType: ...
    def visit_type_type(self, t: TypeType) -> ProperType: ...
    def visit_type_alias_type(self, t: TypeAliasType) -> ProperType: ...
    def meet(self, s: Type, t: Type) -> ProperType: ...
    def default(self, typ: Type) -> ProperType: ...

def meet_similar_callables(t: CallableType, s: CallableType) -> CallableType: ...
def meet_type_list(types: list[Type]) -> Type: ...
def typed_dict_mapping_pair(left: Type, right: Type) -> bool:
    """Is this a pair where one type is a TypedDict and another one is an instance of Mapping?

    This case requires a precise/principled consideration because there are two use cases
    that push the boundary the opposite ways: we need to avoid spurious overlaps to avoid
    false positives for overloads, but we also need to avoid spuriously non-overlapping types
    to avoid false positives with --strict-equality.
    """
def typed_dict_mapping_overlap(left: Type, right: Type, overlapping: Callable[[Type, Type], bool]) -> bool:
    """Check if a TypedDict type is overlapping with a Mapping.

    The basic logic here consists of two rules:

    * A TypedDict with some required keys is overlapping with Mapping[str, <some type>]
      if and only if every key type is overlapping with <some type>. For example:

      - TypedDict(x=int, y=str) overlaps with Dict[str, Union[str, int]]
      - TypedDict(x=int, y=str) doesn't overlap with Dict[str, int]

      Note that any additional non-required keys can't change the above result.

    * A TypedDict with no required keys overlaps with Mapping[str, <some type>] if and
      only if at least one of key types overlaps with <some type>. For example:

      - TypedDict(x=str, y=str, total=False) overlaps with Dict[str, str]
      - TypedDict(x=str, y=str, total=False) doesn't overlap with Dict[str, int]
      - TypedDict(x=int, y=str, total=False) overlaps with Dict[str, str]

    As usual empty, dictionaries lie in a gray area. In general, List[str] and List[str]
    are considered non-overlapping despite empty list belongs to both. However, List[int]
    and List[<nothing>] are considered overlapping.

    So here we follow the same logic: a TypedDict with no required keys is considered
    non-overlapping with Mapping[str, <some type>], but is considered overlapping with
    Mapping[<nothing>, <nothing>]. This way we avoid false positives for overloads, and also
    avoid false positives for comparisons like SomeTypedDict == {} under --strict-equality.
    """
