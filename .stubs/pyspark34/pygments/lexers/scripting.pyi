from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer

__all__ = ['LuaLexer', 'MoonScriptLexer', 'ChaiscriptLexer', 'LSLLexer', 'AppleScriptLexer', 'RexxLexer', 'MOOCodeLexer', 'HybrisLexer', 'EasytrieveLexer', 'JclLexer', 'MiniScriptLexer']

class LuaLexer(RegexLexer):
    """
    For Lua source code.

    Additional options accepted:

    `func_name_highlighting`
        If given and ``True``, highlight builtin function names
        (default: ``True``).
    `disabled_modules`
        If given, must be a list of module names whose function names
        should not be highlighted. By default all modules are highlighted.

        To get a list of allowed modules have a look into the
        `_lua_builtins` module:

        .. sourcecode:: pycon

            >>> from pygments.lexers._lua_builtins import MODULES
            >>> MODULES.keys()
            ['string', 'coroutine', 'modules', 'io', 'basic', ...]
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    func_name_highlighting: Incomplete
    disabled_modules: Incomplete
    def __init__(self, **options) -> None: ...
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...

class MoonScriptLexer(LuaLexer):
    """
    For MoonScript source code.

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...

class ChaiscriptLexer(RegexLexer):
    """
    For ChaiScript source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class LSLLexer(RegexLexer):
    """
    For Second Life's Linden Scripting Language source code.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    lsl_keywords: str
    lsl_types: str
    lsl_states: str
    lsl_events: str
    lsl_functions_builtin: str
    lsl_constants_float: str
    lsl_constants_integer: str
    lsl_constants_integer_boolean: str
    lsl_constants_rotation: str
    lsl_constants_string: str
    lsl_constants_vector: str
    lsl_invalid_broken: str
    lsl_invalid_deprecated: str
    lsl_invalid_illegal: str
    lsl_invalid_unimplemented: str
    lsl_reserved_godmode: str
    lsl_reserved_log: str
    lsl_operators: str
    tokens: Incomplete

class AppleScriptLexer(RegexLexer):
    """
    For AppleScript source code,
    including `AppleScript Studio
    <http://developer.apple.com/documentation/AppleScript/
    Reference/StudioReference>`_.
    Contributed by Andreas Amann <aamann@mac.com>.

    .. versionadded:: 1.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    Identifiers: str
    Literals: Incomplete
    Classes: Incomplete
    BuiltIn: Incomplete
    HandlerParams: Incomplete
    Commands: Incomplete
    References: Incomplete
    Operators: Incomplete
    Control: Incomplete
    Declarations: Incomplete
    Reserved: Incomplete
    StudioClasses: Incomplete
    StudioEvents: Incomplete
    StudioCommands: Incomplete
    StudioProperties: Incomplete
    tokens: Incomplete

class RexxLexer(RegexLexer):
    """
    Rexx is a scripting language available for
    a wide range of different platforms with its roots found on mainframe
    systems. It is popular for I/O- and data based tasks and can act as glue
    language to bind different applications together.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    PATTERNS_AND_WEIGHTS: Incomplete
    def analyse_text(text):
        """
        Check for initial comment and patterns that distinguish Rexx from other
        C-like languages.
        """

class MOOCodeLexer(RegexLexer):
    """
    For MOOCode (the MOO scripting language).

    .. versionadded:: 0.9
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class HybrisLexer(RegexLexer):
    """
    For Hybris source code.

    .. versionadded:: 1.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """public method and private method don't seem to be quite common
        elsewhere."""

class EasytrieveLexer(RegexLexer):
    """
    Easytrieve Plus is a programming language for extracting, filtering and
    converting sequential data. Furthermore it can layout data for reports.
    It is mainly used on mainframe platforms and can access several of the
    mainframe's native file formats. It is somewhat comparable to awk.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: int
    tokens: Incomplete
    def analyse_text(text):
        """
        Perform a structural analysis for basic Easytrieve constructs.
        """

class JclLexer(RegexLexer):
    """
    Job Control Language (JCL)
    is a scripting language used on mainframe platforms to instruct the system
    on how to run a batch job or start a subsystem. It is somewhat
    comparable to MS DOS batch and Unix shell scripts.

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """
        Recognize JCL job by header.
        """

class MiniScriptLexer(RegexLexer):
    """
    For MiniScript source code.

    .. versionadded:: 2.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
