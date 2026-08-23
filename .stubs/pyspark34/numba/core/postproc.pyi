from _typeshed import Incomplete
from functools import cached_property as cached_property
from numba.core import analysis as analysis, ir as ir, ir_utils as ir_utils, transforms as transforms

class YieldPoint:
    block: Incomplete
    inst: Incomplete
    live_vars: Incomplete
    weak_live_vars: Incomplete
    def __init__(self, block, inst) -> None: ...

class GeneratorInfo:
    yield_points: Incomplete
    state_vars: Incomplete
    def __init__(self) -> None: ...
    def get_yield_points(self):
        """
        Return an iterable of YieldPoint instances.
        """

class VariableLifetime:
    """
    For lazily building information of variable lifetime
    """
    def __init__(self, blocks) -> None: ...
    @cached_property
    def cfg(self): ...
    @cached_property
    def usedefs(self): ...
    @cached_property
    def livemap(self): ...
    @cached_property
    def deadmaps(self): ...

ir_extension_insert_dels: Incomplete

class PostProcessor:
    """
    A post-processor for Numba IR.
    """
    func_ir: Incomplete
    def __init__(self, func_ir) -> None: ...
    def run(self, emit_dels: bool = False, extend_lifetimes: bool = False):
        """
        Run the following passes over Numba IR:
        - canonicalize the CFG
        - emit explicit `del` instructions for variables
        - compute lifetime of variables
        - compute generator info (if function is a generator function)
        """
    def remove_dels(self) -> None:
        """
        Strips the IR of Del nodes
        """
