import mypy.checker
from _typeshed import Incomplete
from mypy import message_registry as message_registry
from mypy.checkmember import analyze_member_access as analyze_member_access
from mypy.expandtype import expand_type_by_instance as expand_type_by_instance
from mypy.join import join_types as join_types
from mypy.literals import literal_hash as literal_hash
from mypy.maptype import map_instance_to_supertype as map_instance_to_supertype
from mypy.meet import narrow_declared_type as narrow_declared_type
from mypy.messages import MessageBuilder as MessageBuilder
from mypy.nodes import ARG_POS as ARG_POS, Context as Context, Expression as Expression, NameExpr as NameExpr, TypeAlias as TypeAlias, TypeInfo as TypeInfo, Var as Var
from mypy.options import Options as Options
from mypy.patterns import AsPattern as AsPattern, ClassPattern as ClassPattern, MappingPattern as MappingPattern, OrPattern as OrPattern, Pattern as Pattern, SequencePattern as SequencePattern, SingletonPattern as SingletonPattern, StarredPattern as StarredPattern, ValuePattern as ValuePattern
from mypy.plugin import Plugin as Plugin
from mypy.subtypes import is_subtype as is_subtype
from mypy.typeops import coerce_to_literal as coerce_to_literal, make_simplified_union as make_simplified_union, try_getting_str_literals_from_type as try_getting_str_literals_from_type, tuple_fallback as tuple_fallback
from mypy.types import AnyType as AnyType, Instance as Instance, LiteralType as LiteralType, NoneType as NoneType, ProperType as ProperType, TupleType as TupleType, Type as Type, TypeOfAny as TypeOfAny, TypedDictType as TypedDictType, UninhabitedType as UninhabitedType, UnionType as UnionType, get_proper_type as get_proper_type
from mypy.typevars import fill_typevars as fill_typevars
from mypy.visitor import PatternVisitor as PatternVisitor
from typing import NamedTuple
from typing_extensions import Final

self_match_type_names: Final[Incomplete]
non_sequence_match_type_names: Final[Incomplete]

class PatternType(NamedTuple):
    type: Type
    rest_type: Type
    captures: dict[Expression, Type]

class PatternChecker(PatternVisitor[PatternType]):
    """Pattern checker.

    This class checks if a pattern can match a type, what the type can be narrowed to, and what
    type capture patterns should be inferred as.
    """
    chk: mypy.checker.TypeChecker
    msg: MessageBuilder
    plugin: Plugin
    subject: Expression
    subject_type: Type
    type_context: list[Type]
    self_match_types: list[Type]
    non_sequence_match_types: list[Type]
    options: Options
    def __init__(self, chk: mypy.checker.TypeChecker, msg: MessageBuilder, plugin: Plugin, options: Options) -> None: ...
    def accept(self, o: Pattern, type_context: Type) -> PatternType: ...
    def visit_as_pattern(self, o: AsPattern) -> PatternType: ...
    def visit_or_pattern(self, o: OrPattern) -> PatternType: ...
    def visit_value_pattern(self, o: ValuePattern) -> PatternType: ...
    def visit_singleton_pattern(self, o: SingletonPattern) -> PatternType: ...
    def visit_sequence_pattern(self, o: SequencePattern) -> PatternType: ...
    def get_sequence_type(self, t: Type, context: Context) -> Type | None: ...
    def contract_starred_pattern_types(self, types: list[Type], star_pos: int | None, num_patterns: int) -> list[Type]:
        """
        Contracts a list of types in a sequence pattern depending on the position of a starred
        capture pattern.

        For example if the sequence pattern [a, *b, c] is matched against types [bool, int, str,
        bytes] the contracted types are [bool, Union[int, str], bytes].

        If star_pos in None the types are returned unchanged.
        """
    def expand_starred_pattern_types(self, types: list[Type], star_pos: int | None, num_types: int) -> list[Type]:
        """Undoes the contraction done by contract_starred_pattern_types.

        For example if the sequence pattern is [a, *b, c] and types [bool, int, str] are extended
        to length 4 the result is [bool, int, int, str].
        """
    def visit_starred_pattern(self, o: StarredPattern) -> PatternType: ...
    def visit_mapping_pattern(self, o: MappingPattern) -> PatternType: ...
    def get_mapping_item_type(self, pattern: MappingPattern, mapping_type: Type, key: Expression) -> Type | None: ...
    def get_simple_mapping_item_type(self, pattern: MappingPattern, mapping_type: Type, key: Expression) -> Type: ...
    def visit_class_pattern(self, o: ClassPattern) -> PatternType: ...
    def should_self_match(self, typ: Type) -> bool: ...
    def can_match_sequence(self, typ: ProperType) -> bool: ...
    def generate_types_from_names(self, type_names: list[str]) -> list[Type]: ...
    def update_type_map(self, original_type_map: dict[Expression, Type], extra_type_map: dict[Expression, Type]) -> None: ...
    def construct_sequence_child(self, outer_type: Type, inner_type: Type) -> Type:
        """
        If outer_type is a child class of typing.Sequence returns a new instance of
        outer_type, that is a Sequence of inner_type. If outer_type is not a child class of
        typing.Sequence just returns a Sequence of inner_type

        For example:
        construct_sequence_child(List[int], str) = List[str]

        TODO: this doesn't make sense. For example if one has class S(Sequence[int], Generic[T])
        or class T(Sequence[Tuple[T, T]]), there is no way any of those can map to Sequence[str].
        """
    def early_non_match(self) -> PatternType: ...

def get_match_arg_names(typ: TupleType) -> list[str | None]: ...
def get_var(expr: Expression) -> Var:
    """
    Warning: this in only true for expressions captured by a match statement.
    Don't call it from anywhere else
    """
def get_type_range(typ: Type) -> mypy.checker.TypeRange: ...
def is_uninhabited(typ: Type) -> bool: ...
