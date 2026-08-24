import mypy.checker
import mypy.checkexpr
from _typeshed import Incomplete
from mypy import message_registry as message_registry
from mypy.errors import Errors as Errors
from mypy.maptype import map_instance_to_supertype as map_instance_to_supertype
from mypy.messages import MessageBuilder as MessageBuilder
from mypy.nodes import ARG_NAMED as ARG_NAMED, ARG_POS as ARG_POS, ARG_STAR as ARG_STAR, ARG_STAR2 as ARG_STAR2, BytesExpr as BytesExpr, CallExpr as CallExpr, Context as Context, DictExpr as DictExpr, Expression as Expression, ExpressionStmt as ExpressionStmt, IndexExpr as IndexExpr, IntExpr as IntExpr, MemberExpr as MemberExpr, MypyFile as MypyFile, NameExpr as NameExpr, Node as Node, StarExpr as StarExpr, StrExpr as StrExpr, TempNode as TempNode, TupleExpr as TupleExpr
from mypy.parse import parse as parse
from mypy.subtypes import is_subtype as is_subtype
from mypy.typeops import custom_special_method as custom_special_method
from mypy.types import AnyType as AnyType, Instance as Instance, LiteralType as LiteralType, TupleType as TupleType, Type as Type, TypeOfAny as TypeOfAny, TypeVarType as TypeVarType, UnionType as UnionType, get_proper_type as get_proper_type, get_proper_types as get_proper_types
from typing import Match, Pattern
from typing_extensions import Final, TypeAlias as _TypeAlias

FormatStringExpr: _TypeAlias
Checkers: _TypeAlias
MatchMap: _TypeAlias

def compile_format_re() -> Pattern[str]:
    """Construct regexp to match format conversion specifiers in % interpolation.

    See https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
    The regexp is intentionally a bit wider to report better errors.
    """
def compile_new_format_re(custom_spec: bool) -> Pattern[str]:
    """Construct regexps to match format conversion specifiers in str.format() calls.

    See After https://docs.python.org/3/library/string.html#formatspec for
    specifications. The regexps are intentionally wider, to report better errors,
    instead of just not matching.
    """

FORMAT_RE: Final[Incomplete]
FORMAT_RE_NEW: Final[Incomplete]
FORMAT_RE_NEW_CUSTOM: Final[Incomplete]
DUMMY_FIELD_NAME: Final[str]
NUMERIC_TYPES_OLD: Final[Incomplete]
NUMERIC_TYPES_NEW: Final[Incomplete]
REQUIRE_INT_OLD: Final[Incomplete]
REQUIRE_INT_NEW: Final[Incomplete]
FLOAT_TYPES: Final[Incomplete]

class ConversionSpecifier:
    whole_seq: Incomplete
    start_pos: Incomplete
    key: Incomplete
    conv_type: Incomplete
    flags: Incomplete
    width: Incomplete
    precision: Incomplete
    format_spec: Incomplete
    non_standard_format_spec: Incomplete
    conversion: Incomplete
    field: Incomplete
    def __init__(self, match: Match[str], start_pos: int = -1, non_standard_format_spec: bool = False) -> None: ...
    def has_key(self) -> bool: ...
    def has_star(self) -> bool: ...

def parse_conversion_specifiers(format_str: str) -> list[ConversionSpecifier]:
    """Parse c-printf-style format string into list of conversion specifiers."""
def parse_format_value(format_value: str, ctx: Context, msg: MessageBuilder, nested: bool = False) -> list[ConversionSpecifier] | None:
    """Parse format string into list of conversion specifiers.

    The specifiers may be nested (two levels maximum), in this case they are ordered as
    '{0:{1}}, {2:{3}{4}}'. Return None in case of an error.
    """
def find_non_escaped_targets(format_value: str, ctx: Context, msg: MessageBuilder) -> list[tuple[str, int]] | None:
    """Return list of raw (un-parsed) format specifiers in format string.

    Format specifiers don't include enclosing braces. We don't use regexp for
    this because they don't work well with nested/repeated patterns
    (both greedy and non-greedy), and these are heavily used internally for
    representation of f-strings.

    Return None in case of an error.
    """

class StringFormatterChecker:
    """String interpolation/formatter type checker.

    This class works closely together with checker.ExpressionChecker.
    """
    chk: mypy.checker.TypeChecker
    msg: MessageBuilder
    exprchk: mypy.checkexpr.ExpressionChecker
    def __init__(self, exprchk: mypy.checkexpr.ExpressionChecker, chk: mypy.checker.TypeChecker, msg: MessageBuilder) -> None:
        """Construct an expression type checker."""
    def check_str_format_call(self, call: CallExpr, format_value: str) -> None:
        """Perform more precise checks for str.format() calls when possible.

        Currently the checks are performed for:
          * Actual string literals
          * Literal types with string values
          * Final names with string values

        The checks that we currently perform:
          * Check generic validity (e.g. unmatched { or }, and {} in invalid positions)
          * Check consistency of specifiers' auto-numbering
          * Verify that replacements can be found for all conversion specifiers,
            and all arguments were used
          * Non-standard format specs are only allowed for types with custom __format__
          * Type check replacements with accessors applied (if any).
          * Verify that specifier type is known and matches replacement type
          * Perform special checks for some specifier types:
            - 'c' requires a single character string
            - 's' must not accept bytes
            - non-empty flags are only allowed for numeric types
        """
    def check_specs_in_format_call(self, call: CallExpr, specs: list[ConversionSpecifier], format_value: str) -> None:
        """Perform pairwise checks for conversion specifiers vs their replacements.

        The core logic for format checking is implemented in this method.
        """
    def perform_special_format_checks(self, spec: ConversionSpecifier, call: CallExpr, repl: Expression, actual_type: Type, expected_type: Type) -> None: ...
    def find_replacements_in_call(self, call: CallExpr, keys: list[str]) -> list[Expression]:
        """Find replacement expression for every specifier in str.format() call.

        In case of an error use TempNode(AnyType).
        """
    def get_expr_by_position(self, pos: int, call: CallExpr) -> Expression | None:
        """Get positional replacement expression from '{0}, {1}'.format(x, y, ...) call.

        If the type is from *args, return TempNode(<item type>). Return None in case of
        an error.
        """
    def get_expr_by_name(self, key: str, call: CallExpr) -> Expression | None:
        """Get named replacement expression from '{name}'.format(name=...) call.

        If the type is from **kwargs, return TempNode(<item type>). Return None in case of
        an error.
        """
    def auto_generate_keys(self, all_specs: list[ConversionSpecifier], ctx: Context) -> bool:
        """Translate '{} {name} {}' to '{0} {name} {1}'.

        Return True if generation was successful, otherwise report an error and return false.
        """
    def apply_field_accessors(self, spec: ConversionSpecifier, repl: Expression, ctx: Context) -> Expression:
        """Transform and validate expr in '{.attr[item]}'.format(expr) into expr.attr['item'].

        If validation fails, return TempNode(AnyType).
        """
    def validate_and_transform_accessors(self, temp_ast: Expression, original_repl: Expression, spec: ConversionSpecifier, ctx: Context) -> bool:
        """Validate and transform (in-place) format field accessors.

        On error, report it and return False. The transformations include replacing the dummy
        variable with actual replacement expression and translating any name expressions in an
        index into strings, so that this will work:

            class User(TypedDict):
                name: str
                id: int
            u: User
            '{[id]:d} -> {[name]}'.format(u)
        """
    def check_str_interpolation(self, expr: FormatStringExpr, replacements: Expression) -> Type:
        """Check the types of the 'replacements' in a string interpolation
        expression: str % replacements.
        """
    def analyze_conversion_specifiers(self, specifiers: list[ConversionSpecifier], context: Context) -> bool | None: ...
    def check_simple_str_interpolation(self, specifiers: list[ConversionSpecifier], replacements: Expression, expr: FormatStringExpr) -> None:
        """Check % string interpolation with positional specifiers '%s, %d' % ('yes, 42')."""
    def check_mapping_str_interpolation(self, specifiers: list[ConversionSpecifier], replacements: Expression, expr: FormatStringExpr) -> None:
        """Check % string interpolation with names specifiers '%(name)s' % {'name': 'John'}."""
    def build_dict_type(self, expr: FormatStringExpr) -> Type:
        """Build expected mapping type for right operand in % formatting."""
    def build_replacement_checkers(self, specifiers: list[ConversionSpecifier], context: Context, expr: FormatStringExpr) -> list[Checkers] | None: ...
    def replacement_checkers(self, specifier: ConversionSpecifier, context: Context, expr: FormatStringExpr) -> list[Checkers] | None:
        """Returns a list of tuples of two functions that check whether a replacement is
        of the right type for the specifier. The first function takes a node and checks
        its type in the right type context. The second function just checks a type.
        """
    def checkers_for_star(self, context: Context) -> Checkers:
        """Returns a tuple of check functions that check whether, respectively,
        a node or a type is compatible with a star in a conversion specifier.
        """
    def check_placeholder_type(self, typ: Type, expected_type: Type, context: Context) -> bool: ...
    def checkers_for_regular_type(self, conv_type: str, context: Context, expr: FormatStringExpr) -> Checkers | None:
        """Returns a tuple of check functions that check whether, respectively,
        a node or a type is compatible with 'type'. Return None in case of an error.
        """
    def check_s_special_cases(self, expr: FormatStringExpr, typ: Type, context: Context) -> bool:
        """Additional special cases for %s in bytes vs string context."""
    def checkers_for_c_type(self, type: str, context: Context, format_expr: FormatStringExpr) -> Checkers | None:
        """Returns a tuple of check functions that check whether, respectively,
        a node or a type is compatible with 'type' that is a character type.
        """
    def conversion_type(self, p: str, context: Context, expr: FormatStringExpr, format_call: bool = False) -> Type | None:
        """Return the type that is accepted for a string interpolation conversion specifier type.

        Note that both Python's float (e.g. %f) and integer (e.g. %d)
        specifier types accept both float and integers.

        The 'format_call' argument indicates whether this type came from % interpolation or from
        a str.format() call, the meaning of few formatting types are different.
        """
    def named_type(self, name: str) -> Instance:
        """Return an instance type with type given by the name and no type
        arguments. Alias for TypeChecker.named_type.
        """
    def accept(self, expr: Expression, context: Type | None = None) -> Type:
        """Type check a node. Alias for TypeChecker.accept."""

def has_type_component(typ: Type, fullname: str) -> bool:
    """Is this a specific instance type, or a union that contains it?

    We use this ad-hoc function instead of a proper visitor or subtype check
    because some str vs bytes errors are strictly speaking not runtime errors,
    but rather highly counter-intuitive behavior. This is similar to what is used for
    --strict-equality.
    """
