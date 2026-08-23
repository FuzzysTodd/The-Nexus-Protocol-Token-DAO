import abc
from _typeshed import Incomplete
from abc import abstractmethod
from mypyc.ir.ops import BasicBlock as BasicBlock, Branch as Branch, Goto as Goto, Integer as Integer, NO_TRACEBACK_LINE_NO as NO_TRACEBACK_LINE_NO, Register as Register, Return as Return, Unreachable as Unreachable, Value as Value
from mypyc.irbuild.builder import IRBuilder as IRBuilder
from mypyc.irbuild.targets import AssignmentTarget as AssignmentTarget
from mypyc.primitives.exc_ops import restore_exc_info_op as restore_exc_info_op, set_stop_iteration_value as set_stop_iteration_value

class NonlocalControl(metaclass=abc.ABCMeta):
    """ABC representing a stack frame of constructs that modify nonlocal control flow.

    The nonlocal control flow constructs are break, continue, and
    return, and their behavior is modified by a number of other
    constructs.  The most obvious is loop, which override where break
    and continue jump to, but also `except` (which needs to clear
    exc_info when left) and (eventually) finally blocks (which need to
    ensure that the finally block is always executed when leaving the
    try/except blocks).
    """
    @abstractmethod
    def gen_break(self, builder: IRBuilder, line: int) -> None: ...
    @abstractmethod
    def gen_continue(self, builder: IRBuilder, line: int) -> None: ...
    @abstractmethod
    def gen_return(self, builder: IRBuilder, value: Value, line: int) -> None: ...

class BaseNonlocalControl(NonlocalControl):
    """Default nonlocal control outside any statements that affect it."""
    def gen_break(self, builder: IRBuilder, line: int) -> None: ...
    def gen_continue(self, builder: IRBuilder, line: int) -> None: ...
    def gen_return(self, builder: IRBuilder, value: Value, line: int) -> None: ...

class LoopNonlocalControl(NonlocalControl):
    """Nonlocal control within a loop."""
    outer: Incomplete
    continue_block: Incomplete
    break_block: Incomplete
    def __init__(self, outer: NonlocalControl, continue_block: BasicBlock, break_block: BasicBlock) -> None: ...
    def gen_break(self, builder: IRBuilder, line: int) -> None: ...
    def gen_continue(self, builder: IRBuilder, line: int) -> None: ...
    def gen_return(self, builder: IRBuilder, value: Value, line: int) -> None: ...

class GeneratorNonlocalControl(BaseNonlocalControl):
    """Default nonlocal control in a generator function outside statements."""
    def gen_return(self, builder: IRBuilder, value: Value, line: int) -> None: ...

class CleanupNonlocalControl(NonlocalControl, metaclass=abc.ABCMeta):
    """Abstract nonlocal control that runs some cleanup code."""
    outer: Incomplete
    def __init__(self, outer: NonlocalControl) -> None: ...
    @abstractmethod
    def gen_cleanup(self, builder: IRBuilder, line: int) -> None: ...
    def gen_break(self, builder: IRBuilder, line: int) -> None: ...
    def gen_continue(self, builder: IRBuilder, line: int) -> None: ...
    def gen_return(self, builder: IRBuilder, value: Value, line: int) -> None: ...

class TryFinallyNonlocalControl(NonlocalControl):
    """Nonlocal control within try/finally."""
    target: Incomplete
    ret_reg: Incomplete
    def __init__(self, target: BasicBlock) -> None: ...
    def gen_break(self, builder: IRBuilder, line: int) -> None: ...
    def gen_continue(self, builder: IRBuilder, line: int) -> None: ...
    def gen_return(self, builder: IRBuilder, value: Value, line: int) -> None: ...

class ExceptNonlocalControl(CleanupNonlocalControl):
    """Nonlocal control for except blocks.

    Just makes sure that sys.exc_info always gets restored when we leave.
    This is super annoying.
    """
    saved: Incomplete
    def __init__(self, outer: NonlocalControl, saved: Value | AssignmentTarget) -> None: ...
    def gen_cleanup(self, builder: IRBuilder, line: int) -> None: ...

class FinallyNonlocalControl(CleanupNonlocalControl):
    """Nonlocal control for finally blocks.

    Just makes sure that sys.exc_info always gets restored when we
    leave and the return register is decrefed if it isn't null.
    """
    saved: Incomplete
    def __init__(self, outer: NonlocalControl, saved: Value) -> None: ...
    def gen_cleanup(self, builder: IRBuilder, line: int) -> None: ...
