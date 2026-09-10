import enum
from _typeshed import Incomplete
from typing import IO

class ELFInvalid(ValueError): ...

class EIClass(enum.IntEnum):
    C32: int
    C64: int

class EIData(enum.IntEnum):
    Lsb: int
    Msb: int

class EMachine(enum.IntEnum):
    I386: int
    S390: int
    Arm: int
    X8664: int
    AArc64: int

class ELFFile:
    """
    Representation of an ELF executable.
    """
    capacity: Incomplete
    encoding: Incomplete
    def __init__(self, f: IO[bytes]) -> None: ...
    @property
    def interpreter(self) -> str | None:
        """
        The path recorded in the ``PT_INTERP`` section header.
        """
