from _typeshed import Incomplete
from mypy.argmap import ArgTypeExpander as ArgTypeExpander
from mypy.erasetype import erase_typevars as erase_typevars
from mypy.infer import ArgumentInferContext as ArgumentInferContext
from mypy.maptype import map_instance_to_supertype as map_instance_to_supertype
from mypy.nodes import ARG_OPT as ARG_OPT, ARG_POS as ARG_POS, ArgKind as ArgKind, CONTRAVARIANT as CONTRAVARIANT, COVARIANT as COVARIANT
from mypy.types import AnyType as AnyType, CallableType as CallableType, DeletedType as DeletedType, ErasedType as ErasedType, Instance as Instance, LiteralType as LiteralType, NoneType as NoneType, Overloaded as Overloaded, ParamSpecType as ParamSpecType, Parameters as Parameters, PartialType as PartialType, ProperType as ProperType, TUPLE_LIKE_INSTANCE_NAMES as TUPLE_LIKE_INSTANCE_NAMES, TupleType as TupleType, Type as Type, TypeAliasType as TypeAliasType, TypeOfAny as TypeOfAny, TypeQuery as TypeQuery, TypeType as TypeType, TypeVarId as TypeVarId, TypeVarLikeType as TypeVarLikeType, TypeVarTupleType as TypeVarTupleType, TypeVarType as TypeVarType, TypeVisitor as TypeVisitor, TypedDictType as TypedDictType, UnboundType as UnboundType, UninhabitedType as UninhabitedType, UnionType as UnionType, UnpackType as UnpackType, callable_with_ellipsis as callable_with_ellipsis, get_proper_type as get_proper_type, has_recursive_types as has_recursive_types, has_type_vars as has_type_vars, is_named_instance as is_named_instance, split_with_prefix_and_suffix as split_with_prefix_and_suffix
from mypy.types_utils import is_union_with_any as is_union_with_any
from mypy.typestate import type_state as type_state
from mypy.typevartuples import extract_unpack as extract_unpack, find_unpack_in_list as find_unpack_in_list, split_with_mapped_and_template as split_with_mapped_and_template
from typing import Iterable, List, Sequence
from typing_extensions import Final

SUBTYPE_OF: Final[int]
SUPERTYPE_OF: Final[int]

class Constraint:
    """A representation of a type constraint.

    It can be either T <: type or T :> type (T is a type variable).
    """
    type_var: TypeVarId
    op: int
    target: Type
    origin_type_var: Incomplete
    def __init__(self, type_var: TypeVarLikeType, op: int, target: Type) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...

def infer_constraints_for_callable(callee: CallableType, arg_types: Sequence[Type | None], arg_kinds: list[ArgKind], formal_to_actual: list[list[int]], context: ArgumentInferContext) -> list[Constraint]:
    """Infer type variable constraints for a callable and actual arguments.

    Return a list of constraints.
    """
def infer_constraints(template: Type, actual: Type, direction: int) -> list[Constraint]:
    """Infer type constraints.

    Match a template type, which may contain type variable references,
    recursively against a type which does not contain (the same) type
    variable references. The result is a list of type constrains of
    form 'T is a supertype/subtype of x', where T is a type variable
    present in the template and x is a type without reference to type
    variables present in the template.

    Assume T and S are type variables. Now the following results can be
    calculated (read as '(template, actual) --> result'):

      (T, X)            -->  T :> X
      (X[T], X[Y])      -->  T <: Y and T :> Y
      ((T, T), (X, Y))  -->  T :> X and T :> Y
      ((T, S), (X, Y))  -->  T :> X and S :> Y
      (X[T], Any)       -->  T <: Any and T :> Any

    The constraints are represented as Constraint objects.
    """
def infer_constraints_if_possible(template: Type, actual: Type, direction: int) -> list[Constraint] | None:
    """Like infer_constraints, but return None if the input relation is
    known to be unsatisfiable, for example if template=List[T] and actual=int.
    (In this case infer_constraints would return [], just like it would for
    an automatically satisfied relation like template=List[T] and actual=object.)
    """
def select_trivial(options: Sequence[list[Constraint] | None]) -> list[list[Constraint]]:
    """Select only those lists where each item is a constraint against Any."""
def merge_with_any(constraint: Constraint) -> Constraint:
    """Transform a constraint target into a union with given Any type."""
def handle_recursive_union(template: UnionType, actual: Type, direction: int) -> list[Constraint]: ...
def any_constraints(options: list[list[Constraint] | None], eager: bool) -> list[Constraint]:
    """Deduce what we can from a collection of constraint lists.

    It's a given that at least one of the lists must be satisfied. A
    None element in the list of options represents an unsatisfiable
    constraint and is ignored.  Ignore empty constraint lists if eager
    is true -- they are always trivially satisfiable.
    """
def filter_satisfiable(option: list[Constraint] | None) -> list[Constraint] | None:
    """Keep only constraints that can possibly be satisfied.

    Currently, we filter out constraints where target is not a subtype of the upper bound.
    Since those can be never satisfied. We may add more cases in future if it improves type
    inference.
    """
def is_same_constraints(x: list[Constraint], y: list[Constraint]) -> bool: ...
def is_same_constraint(c1: Constraint, c2: Constraint) -> bool: ...
def is_similar_constraints(x: list[Constraint], y: list[Constraint]) -> bool:
    """Check that two lists of constraints have similar structure.

    This means that each list has same type variable plus direction pairs (i.e we
    ignore the target). Except for constraints where target is Any type, there
    we ignore direction as well.
    """
def simplify_away_incomplete_types(types: Iterable[Type]) -> list[Type]: ...
def is_complete_type(typ: Type) -> bool:
    """Is a type complete?

    A complete doesn't have uninhabited type components or (when not in strict
    optional mode) None components.
    """

class CompleteTypeVisitor(TypeQuery[bool]):
    def __init__(self) -> None: ...
    def visit_uninhabited_type(self, t: UninhabitedType) -> bool: ...

class ConstraintBuilderVisitor(TypeVisitor[List[Constraint]]):
    """Visitor class for inferring type constraints."""
    actual: ProperType
    direction: Incomplete
    def __init__(self, actual: ProperType, direction: int) -> None: ...
    def visit_unbound_type(self, template: UnboundType) -> list[Constraint]: ...
    def visit_any(self, template: AnyType) -> list[Constraint]: ...
    def visit_none_type(self, template: None) -> list[Constraint]: ...
    def visit_uninhabited_type(self, template: UninhabitedType) -> list[Constraint]: ...
    def visit_erased_type(self, template: ErasedType) -> list[Constraint]: ...
    def visit_deleted_type(self, template: DeletedType) -> list[Constraint]: ...
    def visit_literal_type(self, template: LiteralType) -> list[Constraint]: ...
    def visit_partial_type(self, template: PartialType) -> list[Constraint]: ...
    def visit_type_var(self, template: TypeVarType) -> list[Constraint]: ...
    def visit_param_spec(self, template: ParamSpecType) -> list[Constraint]: ...
    def visit_type_var_tuple(self, template: TypeVarTupleType) -> list[Constraint]: ...
    def visit_unpack_type(self, template: UnpackType) -> list[Constraint]: ...
    def visit_parameters(self, template: Parameters) -> list[Constraint]: ...
    def visit_instance(self, template: Instance) -> list[Constraint]: ...
    def infer_constraints_from_protocol_members(self, instance: Instance, template: Instance, subtype: Type, protocol: Instance, class_obj: bool = False) -> list[Constraint]:
        """Infer constraints for situations where either 'template' or 'instance' is a protocol.

        The 'protocol' is the one of two that is an instance of protocol type, 'subtype'
        is the type used to bind self during inference. Currently, we just infer constrains for
        every protocol member type (both ways for settable members).
        """
    def visit_callable_type(self, template: CallableType) -> list[Constraint]: ...
    def infer_against_overloaded(self, overloaded: Overloaded, template: CallableType) -> list[Constraint]: ...
    def visit_tuple_type(self, template: TupleType) -> list[Constraint]: ...
    def visit_typeddict_type(self, template: TypedDictType) -> list[Constraint]: ...
    def visit_union_type(self, template: UnionType) -> list[Constraint]: ...
    def visit_type_alias_type(self, template: TypeAliasType) -> list[Constraint]: ...
    def infer_against_any(self, types: Iterable[Type], any_type: AnyType) -> list[Constraint]: ...
    def visit_overloaded(self, template: Overloaded) -> list[Constraint]: ...
    def visit_type_type(self, template: TypeType) -> list[Constraint]: ...

def neg_op(op: int) -> int:
    """Map SubtypeOf to SupertypeOf and vice versa."""
def find_matching_overload_item(overloaded: Overloaded, template: CallableType) -> CallableType:
    """Disambiguate overload item against a template."""
def find_matching_overload_items(overloaded: Overloaded, template: CallableType) -> list[CallableType]:
    """Like find_matching_overload_item, but return all matches, not just the first."""
def find_and_build_constraints_for_unpack(mapped: tuple[Type, ...], template: tuple[Type, ...], direction: int) -> tuple[list[Constraint], tuple[Type, ...], tuple[Type, ...]]: ...
def build_constraints_for_unpack(mapped: tuple[Type, ...], mapped_prefix_len: int | None, mapped_suffix_len: int | None, template: tuple[Type, ...], template_prefix_len: int, template_suffix_len: int, direction: int) -> tuple[list[Constraint], tuple[Type, ...], tuple[Type, ...]]: ...
