from mypyc.common import ENV_ATTR_NAME as ENV_ATTR_NAME, SELF_NAME as SELF_NAME
from mypyc.ir.class_ir import ClassIR as ClassIR
from mypyc.ir.func_ir import FuncDecl as FuncDecl, FuncIR as FuncIR, FuncSignature as FuncSignature, RuntimeArg as RuntimeArg
from mypyc.ir.ops import BasicBlock as BasicBlock, Call as Call, Register as Register, Return as Return, SetAttr as SetAttr, Value as Value
from mypyc.ir.rtypes import RInstance as RInstance, object_rprimitive as object_rprimitive
from mypyc.irbuild.builder import IRBuilder as IRBuilder
from mypyc.irbuild.context import FuncInfo as FuncInfo, ImplicitClass as ImplicitClass
from mypyc.primitives.misc_ops import method_new_op as method_new_op

def setup_callable_class(builder: IRBuilder) -> None:
    """Generate an (incomplete) callable class representing a function.

    This can be a nested function or a function within a non-extension
    class.  Also set up the 'self' variable for that class.

    This takes the most recently visited function and returns a
    ClassIR to represent that function. Each callable class contains
    an environment attribute which points to another ClassIR
    representing the environment class where some of its variables can
    be accessed.

    Note that some methods, such as '__call__', are not yet
    created here. Use additional functions, such as
    add_call_to_callable_class(), to add them.

    Return a newly constructed ClassIR representing the callable
    class for the nested function.
    """
def add_call_to_callable_class(builder: IRBuilder, args: list[Register], blocks: list[BasicBlock], sig: FuncSignature, fn_info: FuncInfo) -> FuncIR:
    """Generate a '__call__' method for a callable class representing a nested function.

    This takes the blocks and signature associated with a function
    definition and uses those to build the '__call__' method of a
    given callable class, used to represent that function.
    """
def add_get_to_callable_class(builder: IRBuilder, fn_info: FuncInfo) -> None:
    """Generate the '__get__' method for a callable class."""
def instantiate_callable_class(builder: IRBuilder, fn_info: FuncInfo) -> Value:
    """Create an instance of a callable class for a function.

    Calls to the function will actually call this instance.

    Note that fn_info refers to the function being assigned, whereas
    builder.fn_info refers to the function encapsulating the function
    being turned into a callable class.
    """
