from _typeshed import Incomplete
from mypyc.analysis.dataflow import AnalysisResult as AnalysisResult, BaseAnalysisVisitor as BaseAnalysisVisitor, CFG as CFG, MAYBE_ANALYSIS as MAYBE_ANALYSIS, get_cfg as get_cfg, run_analysis as run_analysis
from mypyc.analysis.selfleaks import analyze_self_leaks as analyze_self_leaks
from mypyc.ir.class_ir import ClassIR as ClassIR
from mypyc.ir.ops import Assign as Assign, AssignMulti as AssignMulti, BasicBlock as BasicBlock, Branch as Branch, Call as Call, ControlOp as ControlOp, GetAttr as GetAttr, Register as Register, RegisterOp as RegisterOp, Return as Return, SetAttr as SetAttr, SetMem as SetMem, Unreachable as Unreachable
from mypyc.ir.rtypes import RInstance as RInstance
from typing import Final, Set, Tuple

dump_always_defined: Final[bool]

def analyze_always_defined_attrs(class_irs: list[ClassIR]) -> None:
    """Find always defined attributes all classes of a compilation unit.

    Also tag attribute initialization ops to not decref the previous
    value (as this would read a NULL pointer and segfault).

    Update the _always_initialized_attrs, _sometimes_initialized_attrs
    and init_self_leak attributes in ClassIR instances.

    This is the main entry point.
    """
def analyze_always_defined_attrs_in_class(cl: ClassIR, seen: set[ClassIR]) -> None: ...
def find_always_defined_attributes(blocks: list[BasicBlock], self_reg: Register, all_attrs: set[str], maybe_defined: AnalysisResult[str], maybe_undefined: AnalysisResult[str], dirty: AnalysisResult[None]) -> set[str]:
    """Find attributes that are always initialized in some basic blocks.

    The analysis results are expected to be up-to-date for the blocks.

    Return a set of always defined attributes.
    """
def find_sometimes_defined_attributes(blocks: list[BasicBlock], self_reg: Register, maybe_defined: AnalysisResult[str], dirty: AnalysisResult[None]) -> set[str]:
    """Find attributes that are sometimes initialized in some basic blocks."""
def mark_attr_initialiation_ops(blocks: list[BasicBlock], self_reg: Register, maybe_defined: AnalysisResult[str], dirty: AnalysisResult[None]) -> None:
    """Tag all SetAttr ops in the basic blocks that initialize attributes.

    Initialization ops assume that the previous attribute value is the error value,
    so there's no need to decref or check for definedness.
    """
GenAndKill = Tuple[Set[str], Set[str]]

def attributes_initialized_by_init_call(op: Call) -> set[str]:
    """Calculate attributes that are always initialized by a super().__init__ call."""
def attributes_maybe_initialized_by_init_call(op: Call) -> set[str]:
    """Calculate attributes that may be initialized by a super().__init__ call."""

class AttributeMaybeDefinedVisitor(BaseAnalysisVisitor[str]):
    """Find attributes that may have been defined via some code path.

    Consider initializations in class body and assignments to 'self.x'
    and calls to base class '__init__'.
    """
    self_reg: Incomplete
    def __init__(self, self_reg: Register) -> None: ...
    def visit_branch(self, op: Branch) -> tuple[set[str], set[str]]: ...
    def visit_return(self, op: Return) -> tuple[set[str], set[str]]: ...
    def visit_unreachable(self, op: Unreachable) -> tuple[set[str], set[str]]: ...
    def visit_register_op(self, op: RegisterOp) -> tuple[set[str], set[str]]: ...
    def visit_assign(self, op: Assign) -> tuple[set[str], set[str]]: ...
    def visit_assign_multi(self, op: AssignMulti) -> tuple[set[str], set[str]]: ...
    def visit_set_mem(self, op: SetMem) -> tuple[set[str], set[str]]: ...

def analyze_maybe_defined_attrs_in_init(blocks: list[BasicBlock], self_reg: Register, attrs_with_defaults: set[str], cfg: CFG) -> AnalysisResult[str]: ...

class AttributeMaybeUndefinedVisitor(BaseAnalysisVisitor[str]):
    """Find attributes that may be undefined via some code path.

    Consider initializations in class body, assignments to 'self.x'
    and calls to base class '__init__'.
    """
    self_reg: Incomplete
    def __init__(self, self_reg: Register) -> None: ...
    def visit_branch(self, op: Branch) -> tuple[set[str], set[str]]: ...
    def visit_return(self, op: Return) -> tuple[set[str], set[str]]: ...
    def visit_unreachable(self, op: Unreachable) -> tuple[set[str], set[str]]: ...
    def visit_register_op(self, op: RegisterOp) -> tuple[set[str], set[str]]: ...
    def visit_assign(self, op: Assign) -> tuple[set[str], set[str]]: ...
    def visit_assign_multi(self, op: AssignMulti) -> tuple[set[str], set[str]]: ...
    def visit_set_mem(self, op: SetMem) -> tuple[set[str], set[str]]: ...

def analyze_maybe_undefined_attrs_in_init(blocks: list[BasicBlock], self_reg: Register, initial_undefined: set[str], cfg: CFG) -> AnalysisResult[str]: ...
def update_always_defined_attrs_using_subclasses(cl: ClassIR, seen: set[ClassIR]) -> None:
    """Remove attributes not defined in all subclasses from always defined attrs."""
def detect_undefined_bitmap(cl: ClassIR, seen: set[ClassIR]) -> None: ...
