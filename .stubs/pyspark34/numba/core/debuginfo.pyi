import abc
from _typeshed import Incomplete
from collections.abc import Generator
from numba.core import cgutils as cgutils, config as config, types as types
from numba.core.datamodel.models import ComplexModel as ComplexModel, UniTupleModel as UniTupleModel

def suspend_emission(builder) -> Generator[None, None, None]:
    """Suspends the emission of debug_metadata for the duration of the context
    managed block."""

class AbstractDIBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def mark_variable(self, builder, allocavalue, name, lltype, size, line, datamodel: Incomplete | None = None, argidx: Incomplete | None = None):
        """Emit debug info for the variable.
        """
    @abc.abstractmethod
    def mark_location(self, builder, line):
        """Emit source location information to the given IRBuilder.
        """
    @abc.abstractmethod
    def mark_subprogram(self, function, qualname, argnames, argtypes, line):
        """Emit source location information for the given function.
        """
    @abc.abstractmethod
    def initialize(self):
        """Initialize the debug info. An opportunity for the debuginfo to
        prepare any necessary data structures.
        """
    @abc.abstractmethod
    def finalize(self):
        """Finalize the debuginfo by emitting all necessary metadata.
        """

class DummyDIBuilder(AbstractDIBuilder):
    def __init__(self, module, filepath, cgctx, directives_only) -> None: ...
    def mark_variable(self, builder, allocavalue, name, lltype, size, line, datamodel: Incomplete | None = None, argidx: Incomplete | None = None) -> None: ...
    def mark_location(self, builder, line) -> None: ...
    def mark_subprogram(self, function, qualname, argnames, argtypes, line) -> None: ...
    def initialize(self) -> None: ...
    def finalize(self) -> None: ...

class DIBuilder(AbstractDIBuilder):
    DWARF_VERSION: int
    DEBUG_INFO_VERSION: int
    DBG_CU_NAME: str
    module: Incomplete
    filepath: Incomplete
    difile: Incomplete
    subprograms: Incomplete
    cgctx: Incomplete
    emission_kind: str
    def __init__(self, module, filepath, cgctx, directives_only) -> None: ...
    dicompileunit: Incomplete
    def initialize(self) -> None: ...
    def mark_variable(self, builder, allocavalue, name, lltype, size, line, datamodel: Incomplete | None = None, argidx: Incomplete | None = None): ...
    def mark_location(self, builder, line) -> None: ...
    def mark_subprogram(self, function, qualname, argnames, argtypes, line) -> None: ...
    def finalize(self) -> None: ...
