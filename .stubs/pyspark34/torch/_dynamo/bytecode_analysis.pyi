import dataclasses
import dis
from _typeshed import Incomplete
from numbers import Real

TERMINAL_OPCODES: Incomplete
JUMP_OPCODES: Incomplete
JUMP_OPNAMES: Incomplete
HASLOCAL: Incomplete
HASFREE: Incomplete
stack_effect = dis.stack_effect

def remove_dead_code(instructions):
    """Dead code elimination"""
def remove_pointless_jumps(instructions):
    """Eliminate jumps to the next instruction"""
def propagate_line_nums(instructions) -> None:
    """Ensure every instruction has line number set in case some are removed"""
def remove_extra_line_nums(instructions) -> None:
    """Remove extra starts line properties before packing bytecode"""

@dataclasses.dataclass
class ReadsWrites:
    reads: set
    writes: set
    visited: set
    def __init__(self, reads, writes, visited) -> None: ...

def livevars_analysis(instructions, instruction): ...

@dataclasses.dataclass
class FixedPointBox:
    value: bool = ...
    def __init__(self, value) -> None: ...

@dataclasses.dataclass
class StackSize:
    low: Real
    high: Real
    fixed_point: FixedPointBox
    def zero(self) -> None: ...
    def offset_of(self, other, n) -> None: ...
    def __init__(self, low, high, fixed_point) -> None: ...

def stacksize_analysis(instructions): ...
