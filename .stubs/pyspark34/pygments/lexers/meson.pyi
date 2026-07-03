from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['MesonLexer']

class MesonLexer(RegexLexer):
    """Meson language lexer.

    The grammar definition use to transcribe the syntax was retrieved from
    https://mesonbuild.com/Syntax.html#grammar for version 0.58.
    Some of those definitions are improperly transcribed, so the Meson++
    implementation was also checked: https://github.com/dcbaker/meson-plus-plus.

    .. versionadded:: 2.10
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
