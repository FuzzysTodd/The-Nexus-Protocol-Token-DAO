from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer

__all__ = ['GLShaderLexer', 'PostScriptLexer', 'AsymptoteLexer', 'GnuplotLexer', 'PovrayLexer', 'HLSLShaderLexer']

class GLShaderLexer(RegexLexer):
    """
    GLSL (OpenGL Shader) lexer.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class HLSLShaderLexer(RegexLexer):
    """
    HLSL (Microsoft Direct3D Shader) lexer.

    .. versionadded:: 2.3
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class PostScriptLexer(RegexLexer):
    """
    Lexer for PostScript files.

    .. versionadded:: 1.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    delimiter: str
    delimiter_end: Incomplete
    valid_name_chars: Incomplete
    valid_name: Incomplete
    tokens: Incomplete

class AsymptoteLexer(RegexLexer):
    """
    For Asymptote source code.

    .. versionadded:: 1.2
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def get_tokens_unprocessed(self, text) -> Generator[Incomplete, None, None]: ...

class GnuplotLexer(RegexLexer):
    """
    For Gnuplot plotting scripts.

    .. versionadded:: 0.11
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class PovrayLexer(RegexLexer):
    """
    For Persistence of Vision Raytracer files.

    .. versionadded:: 0.11
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete
    def analyse_text(text):
        """POVRAY is similar to JSON/C, but the combination of camera and
        light_source is probably not very likely elsewhere. HLSL or GLSL
        are similar (GLSL even has #version), but they miss #declare, and
        light_source/camera are not keywords anywhere else -- it's fair
        to assume though that any POVRAY scene must have a camera and
        lightsource."""
