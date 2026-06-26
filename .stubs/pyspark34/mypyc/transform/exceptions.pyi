from mypyc.ir.func_ir import FuncIR as FuncIR
from mypyc.ir.ops import BasicBlock as BasicBlock, Branch as Branch, CallC as CallC, ComparisonOp as ComparisonOp, ERR_ALWAYS as ERR_ALWAYS, ERR_FALSE as ERR_FALSE, ERR_MAGIC as ERR_MAGIC, ERR_MAGIC_OVERLAPPING as ERR_MAGIC_OVERLAPPING, ERR_NEVER as ERR_NEVER, Float as Float, GetAttr as GetAttr, Integer as Integer, LoadErrorValue as LoadErrorValue, NO_TRACEBACK_LINE_NO as NO_TRACEBACK_LINE_NO, Op as Op, RegisterOp as RegisterOp, Return as Return, SetAttr as SetAttr, TupleGet as TupleGet, Value as Value
from mypyc.ir.rtypes import RTuple as RTuple, bool_rprimitive as bool_rprimitive, is_float_rprimitive as is_float_rprimitive
from mypyc.primitives.exc_ops import err_occurred_op as err_occurred_op
from mypyc.primitives.registry import CFunctionDescription as CFunctionDescription

def insert_exception_handling(ir: FuncIR) -> None: ...
def add_default_handler_block(ir: FuncIR) -> BasicBlock: ...
def split_blocks_at_errors(blocks: list[BasicBlock], default_error_handler: BasicBlock, func_name: str | None) -> list[BasicBlock]: ...
def primitive_call(desc: CFunctionDescription, args: list[Value], line: int) -> CallC: ...
def adjust_error_kinds(block: BasicBlock) -> None:
    """Infer more precise error_kind attributes for ops.

    We have access here to more information than what was available
    when the IR was initially built.
    """
def insert_overlapping_error_value_check(ops: list[Op], target: Value) -> ComparisonOp:
    """Append to ops to check for an overlapping error value."""
