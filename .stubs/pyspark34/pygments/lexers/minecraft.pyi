from _typeshed import Incomplete
from pygments.lexer import RegexLexer

__all__ = ['SNBTLexer', 'MCFunctionLexer', 'MCSchemaLexer']

class SNBTLexer(RegexLexer):
    """Lexer for stringified NBT, a data format used in Minecraft

    .. versionadded:: 2.12.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class MCFunctionLexer(RegexLexer):
    """Lexer for the mcfunction scripting language used in Minecraft
    Modelled somewhat after the `GitHub mcfunction grammar <https://github.com/Arcensoth/language-mcfunction>`_.

    .. versionadded:: 2.12.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class MCSchemaLexer(RegexLexer):
    """Lexer for Minecraft Add-ons data Schemas, an interface structure standard used in Minecraft

    .. versionadded:: 2.14.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
