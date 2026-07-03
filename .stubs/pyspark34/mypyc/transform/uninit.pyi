from mypyc.analysis.dataflow import AnalysisDict as AnalysisDict, analyze_must_defined_regs as analyze_must_defined_regs, cleanup_cfg as cleanup_cfg, get_cfg as get_cfg
from mypyc.common import BITMAP_BITS as BITMAP_BITS
from mypyc.ir.func_ir import FuncIR as FuncIR, all_values as all_values
from mypyc.ir.ops import Assign as Assign, BasicBlock as BasicBlock, Branch as Branch, ComparisonOp as ComparisonOp, IntOp as IntOp, Integer as Integer, LoadAddress as LoadAddress, LoadErrorValue as LoadErrorValue, Op as Op, RaiseStandardError as RaiseStandardError, Register as Register, Unreachable as Unreachable, Value as Value
from mypyc.ir.rtypes import bitmap_rprimitive as bitmap_rprimitive

def insert_uninit_checks(ir: FuncIR) -> None: ...
def split_blocks_at_uninits(blocks: list[BasicBlock], pre_must_defined: AnalysisDict[Value]) -> list[BasicBlock]: ...
def check_for_uninit_using_bitmap(ops: list[Op], src: Register, bitmap_registers: list[Register], bitmap_backed: list[Register], error_block: BasicBlock, ok_block: BasicBlock, line: int) -> None:
    """Check if src is defined using a bitmap.

    Modifies ops, bitmap_registers and bitmap_backed.
    """
def update_register_assignments_to_set_bitmap(blocks: list[BasicBlock], bitmap_registers: list[Register], bitmap_backed: list[Register]) -> None:
    """Update some assignments to registers to also set a bit in a bitmap.

    The bitmaps are used to track if a local variable has been assigned to.

    Modifies blocks.
    """
