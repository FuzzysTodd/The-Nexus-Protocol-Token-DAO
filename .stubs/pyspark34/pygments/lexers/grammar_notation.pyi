from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['BnfLexer', 'AbnfLexer', 'JsgfLexer', 'PegLexer']

class BnfLexer(RegexLexer):
    """
    This lexer is for grammar notations which are similar to
    original BNF.

    In order to maximize a number of targets of this lexer,
    let's decide some designs:

    * We don't distinguish `Terminal Symbol`.

    * We do assume that `NonTerminal Symbol` are always enclosed
      with arrow brackets.

    * We do assume that `NonTerminal Symbol` may include
      any printable characters except arrow brackets and ASCII 0x20.
      This assumption is for `RBNF <http://www.rfc-base.org/txt/rfc-5511.txt>`_.

    * We do assume that target notation doesn't support comment.

    * We don't distinguish any operators and punctuation except
      `::=`.

    Though these decision making might cause too minimal highlighting
    and you might be disappointed, but it is reasonable for us.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class AbnfLexer(RegexLexer):
    """
    Lexer for IETF 7405 ABNF.

    (Updates `5234 <http://www.ietf.org/rfc/rfc5234.txt>`_) grammars.

    .. versionadded:: 2.1
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class JsgfLexer(RegexLexer):
    """
    For JSpeech Grammar Format grammars.

    .. versionadded:: 2.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class PegLexer(RegexLexer):
    '''
    This lexer is for Parsing Expression Grammars (PEG).

    Various implementations of PEG have made different decisions
    regarding the syntax, so let\'s try to be accommodating:

    * `<-`, `←`, `:`, and `=` are all accepted as rule operators.

    * Both `|` and `/` are choice operators.

    * `^`, `↑`, and `~` are cut operators.

    * A single `a-z` character immediately before a string, or
      multiple `a-z` characters following a string, are part of the
      string (e.g., `r"..."` or `"..."ilmsuxa`).

    .. versionadded:: 2.6
    '''
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
