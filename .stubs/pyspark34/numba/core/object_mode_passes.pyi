from numba.core import config as config, errors as errors, funcdesc as funcdesc, pylowering as pylowering, transforms as transforms, types as types, typing as typing
from numba.core.compiler_machinery import FunctionPass as FunctionPass, LoweringPass as LoweringPass, register_pass as register_pass

class ObjectModeFrontEnd(FunctionPass):
    def __init__(self) -> None: ...
    def run_pass(self, state): ...

class ObjectModeBackEnd(LoweringPass):
    def __init__(self) -> None: ...
    def run_pass(self, state):
        """
        Lowering for object mode
        """
