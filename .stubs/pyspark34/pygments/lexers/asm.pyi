from _typeshed import Incomplete
from collections.abc import Generator
from pygments.lexer import DelegatingLexer, RegexLexer

__all__ = ['GasLexer', 'ObjdumpLexer', 'DObjdumpLexer', 'CppObjdumpLexer', 'CObjdumpLexer', 'HsailLexer', 'LlvmLexer', 'LlvmMirBodyLexer', 'LlvmMirLexer', 'NasmLexer', 'NasmObjdumpLexer', 'TasmLexer', 'Ca65Lexer', 'Dasm16Lexer']

class GasLexer(RegexLexer):
    """
    For Gas (AT&T) assembly code.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    string: str
    char: str
    identifier: Incomplete
    number: str
    register: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class ObjdumpLexer(RegexLexer):
    """
    For the output of ``objdump -dr``.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class DObjdumpLexer(DelegatingLexer):
    """
    For the output of ``objdump -Sr`` on compiled D files.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class CppObjdumpLexer(DelegatingLexer):
    """
    For the output of ``objdump -Sr`` on compiled C++ files.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class CObjdumpLexer(DelegatingLexer):
    """
    For the output of ``objdump -Sr`` on compiled C files.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    def __init__(self, **options) -> None: ...

class HsailLexer(RegexLexer):
    """
    For HSAIL assembly code.

    .. versionadded:: 2.2
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    string: str
    identifier: str
    register_number: str
    register: Incomplete
    alignQual: str
    widthQual: str
    allocQual: str
    roundingMod: str
    datatypeMod: str
    float: str
    hexfloat: str
    ieeefloat: str
    tokens: Incomplete

class LlvmLexer(RegexLexer):
    """
    For LLVM assembly code.
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    string: str
    identifier: Incomplete
    block_label: Incomplete
    tokens: Incomplete

class LlvmMirBodyLexer(RegexLexer):
    """
    For LLVM MIR examples without the YAML wrapper.

    .. versionadded:: 2.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class LlvmMirLexer(RegexLexer):
    """
    Lexer for the overall LLVM MIR document format.

    MIR is a human readable serialization format that's used to represent LLVM's
    machine specific intermediate representation. It allows LLVM's developers to
    see the state of the compilation process at various points, as well as test
    individual pieces of the compiler.

    .. versionadded:: 2.6
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    tokens: Incomplete

class NasmLexer(RegexLexer):
    """
    For Nasm (Intel) assembly code.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    priority: float
    identifier: str
    hexn: str
    octn: str
    binn: str
    decn: str
    floatn: Incomplete
    string: Incomplete
    declkw: str
    register: str
    wordop: str
    type: str
    directives: str
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class NasmObjdumpLexer(ObjdumpLexer):
    """
    For the output of ``objdump -d -M intel``.

    .. versionadded:: 2.0
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    tokens: Incomplete

class TasmLexer(RegexLexer):
    """
    For Tasm (Turbo Assembler) assembly code.
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    identifier: str
    hexn: str
    octn: str
    binn: str
    decn: str
    floatn: Incomplete
    string: Incomplete
    declkw: str
    register: str
    wordop: str
    type: str
    directives: str
    datatype: str
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(text): ...

class Ca65Lexer(RegexLexer):
    """
    For ca65 assembler sources.

    .. versionadded:: 1.6
    """
    name: str
    aliases: Incomplete
    filenames: Incomplete
    flags: Incomplete
    tokens: Incomplete
    def analyse_text(self, text): ...

class Dasm16Lexer(RegexLexer):
    """
    For DCPU-16 Assembly.

    .. versionadded:: 2.4
    """
    name: str
    url: str
    aliases: Incomplete
    filenames: Incomplete
    mimetypes: Incomplete
    INSTRUCTIONS: Incomplete
    REGISTERS: Incomplete
    char: str
    identifier: Incomplete
    number: str
    binary_number: str
    instruction: Incomplete
    single_char: Incomplete
    string: str
    def guess_identifier(lexer, match) -> Generator[Incomplete, None, None]: ...
    tokens: Incomplete
