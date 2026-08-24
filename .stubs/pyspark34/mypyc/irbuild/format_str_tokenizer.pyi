from _typeshed import Incomplete
from enum import Enum
from mypy.checkstrformat import ConversionSpecifier as ConversionSpecifier
from mypy.nodes import Expression as Expression
from mypyc.ir.ops import Integer as Integer, Value as Value
from mypyc.ir.rtypes import c_pyssize_t_rprimitive as c_pyssize_t_rprimitive, is_bytes_rprimitive as is_bytes_rprimitive, is_int_rprimitive as is_int_rprimitive, is_short_int_rprimitive as is_short_int_rprimitive, is_str_rprimitive as is_str_rprimitive
from mypyc.irbuild.builder import IRBuilder as IRBuilder
from mypyc.primitives.bytes_ops import bytes_build_op as bytes_build_op
from mypyc.primitives.int_ops import int_to_str_op as int_to_str_op
from mypyc.primitives.str_ops import str_build_op as str_build_op, str_op as str_op
from typing import Final

class FormatOp(Enum):
    """FormatOp represents conversion operations of string formatting during
    compile time.

    Compare to ConversionSpecifier, FormatOp has fewer attributes.
    For example, to mark a conversion from any object to string,
    ConversionSpecifier may have several representations, like '%s', '{}'
    or '{:{}}'. However, there would only exist one corresponding FormatOp.
    """
    STR: str
    INT: str
    BYTES: str

def generate_format_ops(specifiers: list[ConversionSpecifier]) -> list[FormatOp] | None:
    """Convert ConversionSpecifier to FormatOp.

    Different ConversionSpecifiers may share a same FormatOp.
    """
def tokenizer_printf_style(format_str: str) -> tuple[list[str], list[FormatOp]] | None:
    """Tokenize a printf-style format string using regex.

    Return:
        A list of string literals and a list of FormatOps.
    """

EMPTY_CONTEXT: Final[Incomplete]

def tokenizer_format_call(format_str: str) -> tuple[list[str], list[FormatOp]] | None:
    """Tokenize a str.format() format string.

    The core function parse_format_value() is shared with mypy.
    With these specifiers, we then parse the literal substrings
    of the original format string and convert `ConversionSpecifier`
    to `FormatOp`.

    Return:
        A list of string literals and a list of FormatOps. The literals
        are interleaved with FormatOps and the length of returned literals
        should be exactly one more than FormatOps.
        Return None if it cannot parse the string.
    """
def convert_format_expr_to_str(builder: IRBuilder, format_ops: list[FormatOp], exprs: list[Expression], line: int) -> list[Value] | None:
    """Convert expressions into string literal objects with the guidance
    of FormatOps. Return None when fails."""
def join_formatted_strings(builder: IRBuilder, literals: list[str] | None, substitutions: list[Value], line: int) -> Value:
    """Merge the list of literals and the list of substitutions
    alternatively using 'str_build_op'.

    `substitutions` is the result value of formatting conversions.

    If the `literals` is set to None, we simply join the substitutions;
    Otherwise, the `literals` is the literal substrings of the original
    format string and its length should be exactly one more than
    substitutions.

    For example:
    (1)    'This is a %s and the value is %d'
        -> literals: ['This is a ', ' and the value is', '']
    (2)    '{} and the value is {}'
        -> literals: ['', ' and the value is', '']
    """
def convert_format_expr_to_bytes(builder: IRBuilder, format_ops: list[FormatOp], exprs: list[Expression], line: int) -> list[Value] | None:
    """Convert expressions into bytes literal objects with the guidance
    of FormatOps. Return None when fails."""
def join_formatted_bytes(builder: IRBuilder, literals: list[str], substitutions: list[Value], line: int) -> Value:
    """Merge the list of literals and the list of substitutions
    alternatively using 'bytes_build_op'."""
