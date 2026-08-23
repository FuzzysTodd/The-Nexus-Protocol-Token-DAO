from .ply import lex as lex
from .ply.lex import TOKEN as TOKEN
from _typeshed import Incomplete

class CLexer:
    """ A lexer for the C language. After building it, set the
        input text with input(), and call token() to get new
        tokens.

        The public attribute filename can be set to an initial
        filename, but the lexer will update it upon #line
        directives.
    """
    error_func: Incomplete
    on_lbrace_func: Incomplete
    on_rbrace_func: Incomplete
    type_lookup_func: Incomplete
    filename: str
    last_token: Incomplete
    line_pattern: Incomplete
    pragma_pattern: Incomplete
    def __init__(self, error_func, on_lbrace_func, on_rbrace_func, type_lookup_func) -> None:
        """ Create a new Lexer.

            error_func:
                An error function. Will be called with an error
                message, line and column as arguments, in case of
                an error during lexing.

            on_lbrace_func, on_rbrace_func:
                Called when an LBRACE or RBRACE is encountered
                (likely to push/pop type_lookup_func's scope)

            type_lookup_func:
                A type lookup function. Given a string, it must
                return True IFF this string is a name of a type
                that was defined with a typedef earlier.
        """
    lexer: Incomplete
    def build(self, **kwargs) -> None:
        """ Builds the lexer from the specification. Must be
            called after the lexer object is created.

            This method exists separately, because the PLY
            manual warns against calling lex.lex inside
            __init__
        """
    def reset_lineno(self) -> None:
        """ Resets the internal line number counter of the lexer.
        """
    def input(self, text) -> None: ...
    def token(self): ...
    def find_tok_column(self, token):
        """ Find the column of the token in its line.
        """
    keywords: Incomplete
    keywords_new: Incomplete
    keyword_map: Incomplete
    tokens: Incomplete
    identifier: str
    hex_prefix: str
    hex_digits: str
    bin_prefix: str
    bin_digits: str
    integer_suffix_opt: str
    decimal_constant: Incomplete
    octal_constant: Incomplete
    hex_constant: Incomplete
    bin_constant: Incomplete
    bad_octal_constant: str
    simple_escape: str
    decimal_escape: str
    hex_escape: str
    bad_escape: str
    escape_sequence: Incomplete
    escape_sequence_start_in_string: str
    cconst_char: Incomplete
    char_const: Incomplete
    wchar_const: Incomplete
    u8char_const: Incomplete
    u16char_const: Incomplete
    u32char_const: Incomplete
    multicharacter_constant: Incomplete
    unmatched_quote: Incomplete
    bad_char_const: Incomplete
    string_char: Incomplete
    string_literal: Incomplete
    wstring_literal: Incomplete
    u8string_literal: Incomplete
    u16string_literal: Incomplete
    u32string_literal: Incomplete
    bad_string_literal: Incomplete
    exponent_part: str
    fractional_constant: str
    floating_constant: Incomplete
    binary_exponent_part: str
    hex_fractional_constant: Incomplete
    hex_floating_constant: Incomplete
    states: Incomplete
    pp_line: Incomplete
    def t_PPHASH(self, t):
        """[ \\t]*\\#"""
    pp_filename: Incomplete
    def t_ppline_FILENAME(self, t) -> None: ...
    def t_ppline_LINE_NUMBER(self, t) -> None: ...
    def t_ppline_NEWLINE(self, t) -> None:
        """\\n"""
    def t_ppline_PPLINE(self, t) -> None:
        """line"""
    t_ppline_ignore: str
    def t_ppline_error(self, t) -> None: ...
    def t_pppragma_NEWLINE(self, t) -> None:
        """\\n"""
    def t_pppragma_PPPRAGMA(self, t):
        """pragma"""
    t_pppragma_ignore: str
    def t_pppragma_STR(self, t):
        """.+"""
    def t_pppragma_error(self, t) -> None: ...
    t_ignore: str
    def t_NEWLINE(self, t) -> None:
        """\\n+"""
    t_PLUS: str
    t_MINUS: str
    t_TIMES: str
    t_DIVIDE: str
    t_MOD: str
    t_OR: str
    t_AND: str
    t_NOT: str
    t_XOR: str
    t_LSHIFT: str
    t_RSHIFT: str
    t_LOR: str
    t_LAND: str
    t_LNOT: str
    t_LT: str
    t_GT: str
    t_LE: str
    t_GE: str
    t_EQ: str
    t_NE: str
    t_EQUALS: str
    t_TIMESEQUAL: str
    t_DIVEQUAL: str
    t_MODEQUAL: str
    t_PLUSEQUAL: str
    t_MINUSEQUAL: str
    t_LSHIFTEQUAL: str
    t_RSHIFTEQUAL: str
    t_ANDEQUAL: str
    t_OREQUAL: str
    t_XOREQUAL: str
    t_PLUSPLUS: str
    t_MINUSMINUS: str
    t_ARROW: str
    t_CONDOP: str
    t_LPAREN: str
    t_RPAREN: str
    t_LBRACKET: str
    t_RBRACKET: str
    t_COMMA: str
    t_PERIOD: str
    t_SEMI: str
    t_COLON: str
    t_ELLIPSIS: str
    def t_LBRACE(self, t): ...
    def t_RBRACE(self, t): ...
    t_STRING_LITERAL = string_literal
    def t_FLOAT_CONST(self, t): ...
    def t_HEX_FLOAT_CONST(self, t): ...
    def t_INT_CONST_HEX(self, t): ...
    def t_INT_CONST_BIN(self, t): ...
    def t_BAD_CONST_OCT(self, t) -> None: ...
    def t_INT_CONST_OCT(self, t): ...
    def t_INT_CONST_DEC(self, t): ...
    def t_INT_CONST_CHAR(self, t): ...
    def t_CHAR_CONST(self, t): ...
    def t_WCHAR_CONST(self, t): ...
    def t_U8CHAR_CONST(self, t): ...
    def t_U16CHAR_CONST(self, t): ...
    def t_U32CHAR_CONST(self, t): ...
    def t_UNMATCHED_QUOTE(self, t) -> None: ...
    def t_BAD_CHAR_CONST(self, t) -> None: ...
    def t_WSTRING_LITERAL(self, t): ...
    def t_U8STRING_LITERAL(self, t): ...
    def t_U16STRING_LITERAL(self, t): ...
    def t_U32STRING_LITERAL(self, t): ...
    def t_BAD_STRING_LITERAL(self, t) -> None: ...
    def t_ID(self, t): ...
    def t_error(self, t) -> None: ...
