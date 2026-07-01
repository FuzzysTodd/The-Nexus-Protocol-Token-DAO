from . import DefaultTable as DefaultTable, ttProgram as ttProgram
from _typeshed import Incomplete

class table__f_p_g_m(DefaultTable.DefaultTable):
    program: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    def compile(self, ttFont): ...
    def toXML(self, writer, ttFont) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
    def __bool__(self) -> bool:
        """
        >>> fpgm = table__f_p_g_m()
        >>> bool(fpgm)
        False
        >>> p = ttProgram.Program()
        >>> fpgm.program = p
        >>> bool(fpgm)
        False
        >>> bc = bytearray([0])
        >>> p.fromBytecode(bc)
        >>> bool(fpgm)
        True
        >>> p.bytecode.pop()
        0
        >>> bool(fpgm)
        False
        """
    __nonzero__ = __bool__
