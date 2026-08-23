import torch
import types
from .. import variables as variables
from ..bytecode_transformation import create_instruction as create_instruction
from ..exc import unimplemented as unimplemented
from ..guards import GuardBuilder as GuardBuilder
from ..source import AttrSource as AttrSource
from ..utils import identity as identity, proxy_args_kwargs as proxy_args_kwargs
from .base import VariableTracker as VariableTracker
from .functions import NestedUserFunctionVariable as NestedUserFunctionVariable, UserFunctionVariable as UserFunctionVariable, UserMethodVariable as UserMethodVariable, WrappedUserFunctionVariable as WrappedUserFunctionVariable, WrappedUserMethodVariable as WrappedUserMethodVariable
from _typeshed import Incomplete
from torch._guards import Guard as Guard, GuardSource as GuardSource
from typing import Dict, List

class SuperVariable(VariableTracker):
    typevar: Incomplete
    objvar: Incomplete
    specialized: Incomplete
    def __init__(self, typevar, objvar: Incomplete | None = None, specialized: bool = False, **kwargs) -> None: ...
    def reconstruct(self, codegen): ...
    def const_getattr(self, tx, name): ...
    def call_method(self, tx, name, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...

class UnknownVariable(VariableTracker):
    """
    It could be anything!
    """

class ComptimeVariable(VariableTracker):
    """
    This variable is special, it lets you execute arbitrary code at
    Dynamo compile time
    """
    def reconstruct(self, codegen) -> None: ...
    def var_getattr(self, tx, name: str) -> VariableTracker: ...
    def call_function(self, tx, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...

class ClosureVariable(UnknownVariable):
    name: Incomplete
    def __init__(self, name, **kwargs) -> None: ...
    def reconstruct(self, codegen): ...

class NewCellVariable(VariableTracker):
    def __init__(self, **kwargs) -> None: ...

class NewGlobalVariable(VariableTracker):
    def __init__(self, **kwargs) -> None: ...

class ContextWrappingVariable(VariableTracker):
    target_values: Incomplete
    initial_values: Incomplete
    recursively_contains: Incomplete
    def __init__(self, target_values, initial_values: Incomplete | None = None, **kwargs) -> None: ...
    def enter(self, tx): ...
    def exit(self, tx, *args): ...
    def reconstruct(self, codegen, target_inst: Incomplete | None = None):
        """
        Generate following Python Bytecode, with a `torch._C._set_grad_enable` call
        Python 3.8
             0 LOAD_GLOBAL              0 (torch)
             2 LOAD_ATTR                1 (_C)
             4 LOAD_METHOD              2 (_set_grad_enable)
             6 LOAD_CONST               1 (False)
             8 CALL_METHOD              1
            10 POP_TOP

            12 SETUP_FINALLY           10 (to 24)

            14 LOAD_GLOBAL              3 (user_inst)
            16 CALL_FUNCTION            0
            18 POP_TOP
            20 POP_BLOCK
            22 BEGIN_FINALLY

            24 LOAD_GLOBAL              0 (torch)
            26 LOAD_ATTR                1 (_C)
            28 LOAD_METHOD              2 (_set_grad_enable)
            30 LOAD_CONST               2 (True)
            32 CALL_METHOD              1
            34 POP_TOP
            36 END_FINALLY
            38 LOAD_CONST               0 (None)
            40 RETURN_VALUE

        Instructions 0-10 and 24-34 call torch._C.set_grad_enable(True/False)

        Python 3.9, 3.10
             0 LOAD_GLOBAL              0 (torch)
             2 LOAD_ATTR                1 (_C)
             4 LOAD_METHOD              2 (_set_grad_enable)
             6 LOAD_CONST               1 (False)
             8 CALL_METHOD              1
            10 POP_TOP

            12 SETUP_FINALLY           22 (to 36)

            14 LOAD_GLOBAL              3 (user_inst)
            16 CALL_FUNCTION            0
            18 POP_TOP
            20 POP_BLOCK

            22 LOAD_GLOBAL              0 (torch)
            24 LOAD_ATTR                1 (_C)
            26 LOAD_METHOD              2 (_set_grad_enable)
            28 LOAD_CONST               2 (True)
            30 CALL_METHOD              1
            32 POP_TOP

            34 JUMP_FORWARD            14 (to 50)

            36 LOAD_GLOBAL              0 (torch)
            38 LOAD_ATTR                1 (_C)
            40 LOAD_METHOD              2 (_set_grad_enable)
            42 LOAD_CONST               2 (True)
            44 CALL_METHOD              1
            46 POP_TOP
            48 RERAISE

            50 LOAD_CONST               0 (None)
            52 RETURN_VALUE

        """
    def module_name(self) -> None: ...
    def fn_name(self) -> None: ...
    def call_function(self, tx, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...

class GradModeVariable(ContextWrappingVariable):
    """represents torch.{no_grad,enable_grad,set_grad_mode}()"""
    @staticmethod
    def create(tx, target_value, **kwargs): ...
    guards: Incomplete
    def __init__(self, target_values, initial_values: Incomplete | None = None, **kwargs) -> None: ...
    def enter(self, tx): ...
    def module_name(self): ...
    def fn_name(self): ...

class AutocastModeVariable(ContextWrappingVariable):
    @staticmethod
    def create(target_values, kwargs): ...
    target_values: Incomplete
    mode: Incomplete
    def __init__(self, target_values, initial_values: Incomplete | None = None, **kwargs) -> None: ...
    def exit(self, tx, *args) -> None: ...
    def enter(self, tx) -> None: ...
    def module_name(self): ...
    def fn_name(self): ...

def enter_functional_autocast(*vals): ...
def exit_functional_autocast(mode) -> None: ...

class NullContextVariable(ContextWrappingVariable):
    """
    This class represents Python contextlib.nullcontext.
    It's used as a placeholder for other context managers that Dynamo doesn't
    support yet, e.g, torch.autograd.profiler.record_function.
    """
    def __init__(self, target_values: Incomplete | None = None, **kwargs) -> None: ...
    def enter(self, tx): ...
    def exit(self, tx, *args): ...
    def module_name(self): ...
    def fn_name(self): ...

class CUDAStreamContextVariable(ContextWrappingVariable):
    @staticmethod
    def create(tx, target_value, **kwargs): ...
    def __init__(self, target_values, initial_values: Incomplete | None = None, **kwargs) -> None: ...
    def enter(self, tx) -> None: ...
    def exit(self, tx, *args) -> None: ...
    def fn_name(self): ...

class CUDAStreamVariable(VariableTracker):
    proxy: Incomplete
    value: Incomplete
    def __init__(self, proxy, value, **kwargs) -> None: ...
    def call_method(self, tx, name, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...
    def as_proxy(self): ...

class WithExitFunctionVariable(VariableTracker):
    ctx: Incomplete
    target: Incomplete
    def __init__(self, ctx: ContextWrappingVariable, target, **kwargs) -> None: ...
    def call_function(self, tx, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...
    def reconstruct(self, codegen): ...

class InspectSignatureVariable(VariableTracker):
    """represents inspect.signature(...)"""
    @staticmethod
    def create(callable, **kwargs): ...
    inspected: Incomplete
    def __init__(self, inspected, **kwargs) -> None: ...

class AutogradFunctionVariable(VariableTracker):
    """represents a torch.autograd.Function subclass"""
    fn_cls: Incomplete
    def __init__(self, fn_cls, **kwargs) -> None: ...
    def call_apply(self, tx, args, kwargs): ...
    def call_function(self, tx, args, kwargs): ...

class BlackHoleVariable(VariableTracker):
    """A autograd.function context that just ignores everything (for forward extraction)"""
    def call_method(self, tx, name, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...

class AutogradFunctionContextVariable(VariableTracker):
    """
    A autograd.function context used after graph break in forward.
    Any call method on this context object will be graph break.
    The is different from BlackHoleVariable which is only used in inference mode.
    """

class LambdaVariable(VariableTracker):
    fn: Incomplete
    def __init__(self, fn, **kwargs) -> None: ...
    def call_function(self, tx, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...

class GetAttrVariable(VariableTracker):
    obj: Incomplete
    name: Incomplete
    def __init__(self, obj, name, **kwargs) -> None: ...
    @staticmethod
    def create_getattr_proxy(base_proxy: torch.fx.Proxy, attr): ...
    def as_proxy(self): ...
    def const_getattr(self, tx, name): ...
    def reconstruct(self, codegen): ...
    def call_function(self, tx, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...
    def call_method(self, tx, name, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...

class PythonModuleVariable(VariableTracker):
    value: Incomplete
    def __init__(self, value: types.ModuleType, **kwargs) -> None: ...
    def python_type(self): ...

class SkipFilesVariable(VariableTracker):
    value: Incomplete
    def __init__(self, value, **kwargs) -> None: ...
    def python_type(self): ...
    def as_python_constant(self): ...
    def call_function(self, tx, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...

class TypingVariable(VariableTracker):
    value: Incomplete
    def __init__(self, value, **kwargs) -> None: ...
    def call_method(self, tx, name, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...
    def python_type(self): ...
    def as_python_constant(self): ...

class NumpyVariable(VariableTracker):
    """
    Wrapper around `numpy.*` for better error messages.
    """
    value: Incomplete
    def __init__(self, value, **kwargs) -> None: ...
    def call_function(self, tx, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...
    def call_method(self, tx, name, args: List[VariableTracker], kwargs: Dict[str, VariableTracker]) -> VariableTracker: ...
    def python_type(self): ...
    def as_python_constant(self): ...
