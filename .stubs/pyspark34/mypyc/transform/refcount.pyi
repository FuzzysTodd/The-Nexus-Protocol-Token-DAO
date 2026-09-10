from mypyc.analysis.dataflow import AnalysisDict as AnalysisDict, analyze_borrowed_arguments as analyze_borrowed_arguments, analyze_live_regs as analyze_live_regs, analyze_must_defined_regs as analyze_must_defined_regs, cleanup_cfg as cleanup_cfg, get_cfg as get_cfg
from mypyc.ir.func_ir import FuncIR as FuncIR, all_values as all_values
from mypyc.ir.ops import Assign as Assign, BasicBlock as BasicBlock, Branch as Branch, ControlOp as ControlOp, DecRef as DecRef, Goto as Goto, IncRef as IncRef, Integer as Integer, KeepAlive as KeepAlive, LoadAddress as LoadAddress, Op as Op, Register as Register, RegisterOp as RegisterOp, Value as Value
from typing import Dict, Iterable, Tuple

Decs = Tuple[Tuple[Value, bool], ...]
Incs = Tuple[Value, ...]
BlockCache = Dict[Tuple[BasicBlock, Decs, Incs], BasicBlock]

def insert_ref_count_opcodes(ir: FuncIR) -> None:
    """Insert reference count inc/dec opcodes to a function.

    This is the entry point to this module.
    """
def is_maybe_undefined(post_must_defined: set[Value], src: Value) -> bool: ...
def maybe_append_dec_ref(ops: list[Op], dest: Value, defined: AnalysisDict[Value], key: tuple[BasicBlock, int]) -> None: ...
def maybe_append_inc_ref(ops: list[Op], dest: Value) -> None: ...
def transform_block(block: BasicBlock, pre_live: AnalysisDict[Value], post_live: AnalysisDict[Value], pre_borrow: AnalysisDict[Value], post_must_defined: AnalysisDict[Value]) -> None: ...
def insert_branch_inc_and_decrefs(block: BasicBlock, cache: BlockCache, blocks: list[BasicBlock], pre_live: AnalysisDict[Value], pre_borrow: AnalysisDict[Value], post_borrow: AnalysisDict[Value], post_must_defined: AnalysisDict[Value], ordering: dict[Value, int]) -> None:
    """Insert inc_refs and/or dec_refs after a branch/goto.

    Add dec_refs for registers that become dead after a branch.
    Add inc_refs for registers that become unborrowed after a branch or goto.

    Branches are special as the true and false targets may have a different
    live and borrowed register sets. Add new blocks before the true/false target
    blocks that tweak reference counts.

    Example where we need to add an inc_ref:

      def f(a: int) -> None
          if a:
              a = 1
          return a  # a is borrowed if condition is false and unborrowed if true
    """
def after_branch_decrefs(label: BasicBlock, pre_live: AnalysisDict[Value], source_defined: set[Value], source_borrowed: set[Value], source_live_regs: set[Value], ordering: dict[Value, int], omitted: Iterable[Value]) -> tuple[tuple[Value, bool], ...]: ...
def after_branch_increfs(label: BasicBlock, pre_live: AnalysisDict[Value], pre_borrow: AnalysisDict[Value], source_borrowed: set[Value], ordering: dict[Value, int]) -> tuple[Value, ...]: ...
def add_block(decs: Decs, incs: Incs, cache: BlockCache, blocks: list[BasicBlock], label: BasicBlock) -> BasicBlock: ...
def make_value_ordering(ir: FuncIR) -> dict[Value, int]:
    """Create a ordering of values that allows them to be sorted.

    This omits registers that are only ever read.
    """
