from _typeshed import Incomplete
from numba.core import intrinsics as intrinsics, utils as utils

def compile_multi3(context):
    """
    Compile the multi3() helper function used by LLVM
    for 128-bit multiplication on 32-bit platforms.
    """

class _Installer:
    def install(self, context) -> None:
        """
        Install the functions into LLVM.  This only needs to be done once,
        as the mappings are persistent during the process lifetime.
        """

class _ExternalMathFunctions(_Installer):
    """
    Map the math functions from the C runtime library into the LLVM
    execution environment.
    """

c_math_functions: Incomplete
