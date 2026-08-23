from mypy.nodes import Argument as Argument, FuncDef, SymbolNode as SymbolNode
from mypyc.common import BITMAP_BITS as BITMAP_BITS, ENV_ATTR_NAME as ENV_ATTR_NAME, SELF_NAME as SELF_NAME, bitmap_name as bitmap_name
from mypyc.ir.class_ir import ClassIR as ClassIR
from mypyc.ir.ops import Call as Call, GetAttr as GetAttr, SetAttr as SetAttr, Value as Value
from mypyc.ir.rtypes import RInstance as RInstance, bitmap_rprimitive as bitmap_rprimitive, object_rprimitive as object_rprimitive
from mypyc.irbuild.builder import IRBuilder as IRBuilder, SymbolTarget as SymbolTarget
from mypyc.irbuild.context import FuncInfo as FuncInfo, GeneratorClass as GeneratorClass, ImplicitClass as ImplicitClass
from mypyc.irbuild.targets import AssignmentTargetAttr as AssignmentTargetAttr

def setup_env_class(builder: IRBuilder) -> ClassIR:
    """Generate a class representing a function environment.

    Note that the variables in the function environment are not
    actually populated here. This is because when the environment
    class is generated, the function environment has not yet been
    visited. This behavior is allowed so that when the compiler visits
    nested functions, it can use the returned ClassIR instance to
    figure out free variables it needs to access.  The remaining
    attributes of the environment class are populated when the
    environment registers are loaded.

    Return a ClassIR representing an environment for a function
    containing a nested function.
    """
def finalize_env_class(builder: IRBuilder) -> None:
    """Generate, instantiate, and set up the environment of an environment class."""
def instantiate_env_class(builder: IRBuilder) -> Value:
    """Assign an environment class to a register named after the given function definition."""
def load_env_registers(builder: IRBuilder) -> None:
    """Load the registers for the current FuncItem being visited.

    Adds the arguments of the FuncItem to the environment. If the
    FuncItem is nested inside of another function, then this also
    loads all of the outer environments of the FuncItem into registers
    so that they can be used when accessing free variables.
    """
def load_outer_env(builder: IRBuilder, base: Value, outer_env: dict[SymbolNode, SymbolTarget]) -> Value:
    """Load the environment class for a given base into a register.

    Additionally, iterates through all of the SymbolNode and
    AssignmentTarget instances of the environment at the given index's
    symtable, and adds those instances to the environment of the
    current environment. This is done so that the current environment
    can access outer environment variables without having to reload
    all of the environment registers.

    Returns the register where the environment class was loaded.
    """
def load_outer_envs(builder: IRBuilder, base: ImplicitClass) -> None: ...
def num_bitmap_args(builder: IRBuilder, args: list[Argument]) -> int: ...
def add_args_to_env(builder: IRBuilder, local: bool = True, base: FuncInfo | ImplicitClass | None = None, reassign: bool = True) -> None: ...
def setup_func_for_recursive_call(builder: IRBuilder, fdef: FuncDef, base: ImplicitClass) -> None:
    """Enable calling a nested function (with a callable class) recursively.

    Adds the instance of the callable class representing the given
    FuncDef to a register in the environment so that the function can
    be called recursively. Note that this needs to be done only for
    nested functions.
    """
def is_free_variable(builder: IRBuilder, symbol: SymbolNode) -> bool: ...
