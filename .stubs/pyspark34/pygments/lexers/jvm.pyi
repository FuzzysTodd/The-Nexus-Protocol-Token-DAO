from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import Lexer, RegexLexer

__all__ = ['JavaLexer', 'ScalaLexer', 'GosuLexer', 'GosuTemplateLexer', 'GroovyLexer', 'IokeLexer', 'ClojureLexer', 'ClojureScriptLexer', 'KotlinLexer', 'XtendLexer', 'AspectJLexer', 'CeylonLexer', 'PigLexer', 'GoloLexer', 'JasminLexer', 'SarlLexer']

class JavaLexer(RegexLexer):
    """
    For Java source code.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class AspectJLexer(JavaLexer):
    """
    For AspectJ source code.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    aj_keywords: Incomplete
    aj_inter_type: Incomplete
    aj_inter_type_annotation: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...

class ScalaLexer(RegexLexer):
    """
    For Scala source code.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    opchar: Incomplete
    letter: Incomplete
    upperLetter: Incomplete
    letterOrDigit: Incomplete
    letterOrDigitNoDollarSign: Incomplete
    alphaId: Incomplete
    simpleInterpolatedVariable: Incomplete
    idrest: Incomplete
    idUpper: Incomplete
    plainid: Incomplete
    backQuotedId: str
    anyId: Incomplete
    notStartOfComment: str
    endOfLineMaybeWithComment: str
    keywords: Incomplete
    operators: Incomplete
    storage_modifiers: Incomplete
    tokens: Incomplete

class GosuLexer(RegexLexer):
    """
    For Gosu source code.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class GosuTemplateLexer(Lexer):
    """
    For Gosu templates.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, Incomplete, None]: ...

class GroovyLexer(RegexLexer):
    """
    For Groovy source code.

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class IokeLexer(RegexLexer):
    """
    For Ioke (a strongly typed, dynamic,
    prototype based programming language) source.

    .. versionadded:: 1.4
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class ClojureLexer(RegexLexer):
    """
    Lexer for Clojure source code.

    .. versionadded:: 0.11
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    special_forms: Incomplete
    declarations: Incomplete
    builtins: Incomplete
    valid_name: str
    tokens: Incomplete

class ClojureScriptLexer(ClojureLexer):
    """
    Lexer for ClojureScript source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete

class TeaLangLexer(RegexLexer):
    """
    For Tea source code. Only used within a
    TeaTemplateLexer.

    .. versionadded:: 1.5
    """
    flags: Incomplete
    tokens: Incomplete

class CeylonLexer(RegexLexer):
    """
    For Ceylon source code.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class KotlinLexer(RegexLexer):
    """
    For Kotlin source code.

    .. versionadded:: 1.5
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    kt_name: Incomplete
    kt_space_name: Incomplete
    kt_id: Incomplete
    modifiers: str
    tokens: Incomplete

class XtendLexer(RegexLexer):
    """
    For Xtend source code.

    .. versionadded:: 1.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class PigLexer(RegexLexer):
    """
    For Pig Latin source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete

class GoloLexer(RegexLexer):
    """
    For Golo source code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    filenames: Incomplete
    aliases: Incomplete
    tokens: Incomplete

class JasminLexer(RegexLexer):
    """
    For Jasmin assembly code.

    .. versionadded:: 2.0
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class SarlLexer(RegexLexer):
    """
    For SARL source code.

    .. versionadded:: 2.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    flags: Incomplete
    tokens: Incomplete
