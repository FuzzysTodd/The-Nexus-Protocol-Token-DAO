from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import RegexLexer
from pygments.lexers.c_cpp import CLexer, CppLexer

__all__ = ['PikeLexer', 'NesCLexer', 'ClayLexer', 'ECLexer', 'ValaLexer', 'CudaLexer', 'SwigLexer', 'MqlLexer', 'ArduinoLexer', 'CharmciLexer', 'OmgIdlLexer']

class PikeLexer(CppLexer):
    """
    For `Pike <http://pike.lysator.liu.se/>`_ source code.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class NesCLexer(CLexer):
    """
    For `nesC <https://github.com/tinyos/nesc>`_ source code with preprocessor
    directives.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class ClayLexer(RegexLexer):
    """
    For `Clay <http://claylabs.com/clay/>`_ source.

    .. versionadded:: 2.0
    """
    name: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class ECLexer(CLexer):
    """
    For eC source code with preprocessor directives.

    .. versionadded:: 1.5
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class ValaLexer(RegexLexer):
    """
    For Vala source code with preprocessor directives.

    .. versionadded:: 1.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class CudaLexer(CLexer):
    """
    For NVIDIA `CUDA™ <http://developer.nvidia.com/category/zone/cuda-zone>`_
    source.

    .. versionadded:: 1.6
    """
    name: str
    filenames: Incomplete
    aliases: Incomplete
    mimetypes: Incomplete
    function_qualifiers: Incomplete
    variable_qualifiers: Incomplete
    vector_types: Incomplete
    variables: Incomplete
    functions: Incomplete
    execution_confs: Incomplete
    def get_tokens_unprocessed(self, text, stack=('root',)) -> Generator[Incomplete, None, None]: ...

class SwigLexer(CppLexer):
    """
    For `SWIG <http://www.swig.org/>`_ source code.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    priority: float
    tokens: Incomplete
    swig_directives: Incomplete
    def analyse_text(text): ...

class MqlLexer(CppLexer):
    """
    For `MQL4 <http://docs.mql4.com/>`_ and
    `MQL5 <http://www.mql5.com/en/docs>`_ source code.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class ArduinoLexer(CppLexer):
    """
    For `Arduino(tm) <https://arduino.cc/>`_ source.

    This is an extension of the CppLexer, as the Arduino® Language is a superset
    of C++

    .. versionadded:: 2.1
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    structure: Incomplete
    operators: Incomplete
    variables: Incomplete
    functions: Incomplete
    suppress_highlight: Incomplete
    def get_tokens_unprocessed(self, text, stack=('root',)) -> Generator[Incomplete, None, None]: ...

class CharmciLexer(CppLexer):
    """
    For `Charm++ <https://charm.cs.illinois.edu>`_ interface files (.ci).

    .. versionadded:: 2.4
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class OmgIdlLexer(CLexer):
    """
    Lexer for Object Management Group Interface Definition Language.

    .. versionadded:: 2.9
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    scoped_name: str
    tokens: Incomplete
