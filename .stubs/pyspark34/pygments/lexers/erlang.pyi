from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer, RegexLexer

__all__ = ['ErlangLexer', 'ErlangShellLexer', 'ElixirConsoleLexer', 'ElixirLexer']

class ErlangLexer(RegexLexer):
    """
    For the Erlang functional programming language.

    .. versionadded:: 0.9
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    keywords: Incomplete
    builtins: Incomplete
    operators: str
    word_operators: Incomplete
    atom_re: str
    variable_re: str
    esc_char_re: str
    esc_octal_re: str
    esc_hex_re: str
    esc_ctrl_re: str
    escape_re: Incomplete
    macro_re: Incomplete
    base_re: str
    tokens: Incomplete

class ErlangShellLexer(Lexer):
    """
    Shell sessions in erl (for Erlang code).

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, Incomplete, None]: ...

class ElixirLexer(RegexLexer):
    """
    For the Elixir language.

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    KEYWORD: Incomplete
    KEYWORD_OPERATOR: Incomplete
    BUILTIN: Incomplete
    BUILTIN_DECLARATION: Incomplete
    BUILTIN_NAMESPACE: Incomplete
    CONSTANT: Incomplete
    PSEUDO_VAR: Incomplete
    OPERATORS3: Incomplete
    OPERATORS2: Incomplete
    OPERATORS1: Incomplete
    PUNCTUATION: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...
    def gen_elixir_sigil_rules(): ...
    op3_re: Incomplete
    op2_re: Incomplete
    op1_re: Incomplete
    ops_re: Incomplete
    punctuation_re: Incomplete
    alnum: str
    name_re: Incomplete
    modname_re: Incomplete
    complex_name_re: Incomplete
    special_atom_re: str
    long_hex_char_re: str
    hex_char_re: str
    escape_char_re: str
    tokens: Incomplete

class ElixirConsoleLexer(Lexer):
    """
    For Elixir interactive console (iex) output like:

    .. sourcecode:: iex

        iex> [head | tail] = [1,2,3]
        [1,2,3]
        iex> head
        1
        iex> tail
        [2,3]
        iex> [head | tail]
        [1,2,3]
        iex> length [head | tail]
        3

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    mimetypes: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, Incomplete, None]: ...
