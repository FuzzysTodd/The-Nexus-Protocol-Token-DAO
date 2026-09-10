from mypyc.common import ENV_ATTR_NAME as ENV_ATTR_NAME, NEXT_LABEL_ATTR_NAME as NEXT_LABEL_ATTR_NAME, SELF_NAME as SELF_NAME
from mypyc.ir.class_ir import ClassIR as ClassIR
from mypyc.ir.func_ir import FuncDecl as FuncDecl, FuncIR as FuncIR, FuncSignature as FuncSignature, RuntimeArg as RuntimeArg
from mypyc.ir.ops import BasicBlock as BasicBlock, Branch as Branch, Call as Call, Goto as Goto, Integer as Integer, MethodCall as MethodCall, NO_TRACEBACK_LINE_NO as NO_TRACEBACK_LINE_NO, RaiseStandardError as RaiseStandardError, Register as Register, Return as Return, SetAttr as SetAttr, TupleSet as TupleSet, Unreachable as Unreachable, Value as Value
from mypyc.ir.rtypes import RInstance as RInstance, int_rprimitive as int_rprimitive, object_rprimitive as object_rprimitive
from mypyc.irbuild.builder import IRBuilder as IRBuilder, gen_arg_defaults as gen_arg_defaults
from mypyc.irbuild.context import FuncInfo as FuncInfo, GeneratorClass as GeneratorClass
from mypyc.irbuild.env_class import add_args_to_env as add_args_to_env, finalize_env_class as finalize_env_class, load_env_registers as load_env_registers, load_outer_env as load_outer_env
from mypyc.irbuild.nonlocalcontrol import ExceptNonlocalControl as ExceptNonlocalControl
from mypyc.primitives.exc_ops import error_catch_op as error_catch_op, exc_matches_op as exc_matches_op, raise_exception_with_tb_op as raise_exception_with_tb_op, reraise_exception_op as reraise_exception_op, restore_exc_info_op as restore_exc_info_op

def gen_generator_func(builder: IRBuilder) -> None: ...
def instantiate_generator_class(builder: IRBuilder) -> Value: ...
def setup_generator_class(builder: IRBuilder) -> ClassIR: ...
def create_switch_for_generator_class(builder: IRBuilder) -> None: ...
def populate_switch_for_generator_class(builder: IRBuilder) -> None: ...
def add_raise_exception_blocks_to_generator_class(builder: IRBuilder, line: int) -> None:
    """Add error handling blocks to a generator class.

    Generates blocks to check if error flags are set while calling the
    helper method for generator functions, and raises an exception if
    those flags are set.
    """
def add_methods_to_generator_class(builder: IRBuilder, fn_info: FuncInfo, sig: FuncSignature, arg_regs: list[Register], blocks: list[BasicBlock], is_coroutine: bool) -> None: ...
def add_helper_to_generator_class(builder: IRBuilder, arg_regs: list[Register], blocks: list[BasicBlock], sig: FuncSignature, fn_info: FuncInfo) -> FuncDecl:
    """Generates a helper method for a generator class, called by '__next__' and 'throw'."""
def add_iter_to_generator_class(builder: IRBuilder, fn_info: FuncInfo) -> None:
    """Generates the '__iter__' method for a generator class."""
def add_next_to_generator_class(builder: IRBuilder, fn_info: FuncInfo, fn_decl: FuncDecl, sig: FuncSignature) -> None:
    """Generates the '__next__' method for a generator class."""
def add_send_to_generator_class(builder: IRBuilder, fn_info: FuncInfo, fn_decl: FuncDecl, sig: FuncSignature) -> None:
    """Generates the 'send' method for a generator class."""
def add_throw_to_generator_class(builder: IRBuilder, fn_info: FuncInfo, fn_decl: FuncDecl, sig: FuncSignature) -> None:
    """Generates the 'throw' method for a generator class."""
def add_close_to_generator_class(builder: IRBuilder, fn_info: FuncInfo) -> None:
    """Generates the '__close__' method for a generator class."""
def add_await_to_generator_class(builder: IRBuilder, fn_info: FuncInfo) -> None:
    """Generates the '__await__' method for a generator class."""
def setup_env_for_generator_class(builder: IRBuilder) -> None:
    """Populates the environment for a generator class."""
