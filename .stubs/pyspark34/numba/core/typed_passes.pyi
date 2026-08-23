import abc
from _typeshed import Incomplete
from collections.abc import Generator
from numba.core import config as config, errors as errors, funcdesc as funcdesc, ir as ir, lowering as lowering, postproc as postproc, rewrites as rewrites, typeinfer as typeinfer, types as types, typing as typing
from numba.core.annotations import type_annotations as type_annotations
from numba.core.compiler_machinery import AnalysisPass as AnalysisPass, FunctionPass as FunctionPass, LoweringPass as LoweringPass, register_pass as register_pass
from numba.core.ir_utils import build_definitions as build_definitions, check_and_legalize_ir as check_and_legalize_ir, compute_cfg_from_blocks as compute_cfg_from_blocks, dead_code_elimination as dead_code_elimination, get_definition as get_definition, guard as guard, is_operator_or_getitem as is_operator_or_getitem, raise_on_unsupported_feature as raise_on_unsupported_feature, simplify_CFG as simplify_CFG, warn_deprecated as warn_deprecated
from numba.parfors.parfor import Parfor as Parfor
from numba.parfors.parfor_lowering import ParforLower as ParforLower
from typing import NamedTuple

class _TypingResults(NamedTuple):
    typemap: Incomplete
    return_type: Incomplete
    calltypes: Incomplete
    typing_errors: Incomplete

def fallback_context(state, msg) -> Generator[None, None, None]:
    """
    Wraps code that would signal a fallback to object mode
    """
def type_inference_stage(typingctx, targetctx, interp, args, return_type, locals={}, raise_errors: bool = True): ...

class BaseTypeInference(FunctionPass):
    def __init__(self) -> None: ...
    def run_pass(self, state):
        """
        Type inference and legalization
        """

class NopythonTypeInference(BaseTypeInference): ...
class PartialTypeInference(BaseTypeInference): ...

class AnnotateTypes(AnalysisPass):
    def __init__(self) -> None: ...
    def get_analysis_usage(self, AU) -> None: ...
    def run_pass(self, state):
        """
        Create type annotation after type inference
        """

class NopythonRewrites(FunctionPass):
    def __init__(self) -> None: ...
    def run_pass(self, state):
        """
        Perform any intermediate representation rewrites after type
        inference.
        """

class PreParforPass(FunctionPass):
    def __init__(self) -> None: ...
    def run_pass(self, state):
        """
        Preprocessing for data-parallel computations.
        """

class ParforPass(FunctionPass):
    def __init__(self) -> None: ...
    def run_pass(self, state):
        """
        Convert data-parallel computations into Parfor nodes
        """

class ParforFusionPass(FunctionPass):
    def __init__(self) -> None: ...
    def run_pass(self, state):
        """
        Do fusion of parfor nodes.
        """

class ParforPreLoweringPass(FunctionPass):
    def __init__(self) -> None: ...
    def run_pass(self, state):
        """
        Prepare parfors for lowering.
        """

class DumpParforDiagnostics(AnalysisPass):
    def __init__(self) -> None: ...
    def run_pass(self, state): ...

class BaseNativeLowering(abc.ABC, LoweringPass, metaclass=abc.ABCMeta):
    """The base class for a lowering pass. The lowering functionality must be
    specified in inheriting classes by providing an appropriate lowering class
    implementation in the overridden `lowering_class` property."""
    def __init__(self) -> None: ...
    @property
    @abc.abstractmethod
    def lowering_class(self):
        """Returns the class that performs the lowering of the IR describing the
        function that is the target of the current compilation."""
    def run_pass(self, state): ...

class NativeLowering(BaseNativeLowering):
    """Lowering pass for a native function IR described solely in terms of
     Numba's standard `numba.core.ir` nodes."""
    @property
    def lowering_class(self): ...

class NativeParforLowering(BaseNativeLowering):
    """Lowering pass for a native function IR described using Numba's standard
    `numba.core.ir` nodes and also parfor.Parfor nodes."""
    @property
    def lowering_class(self): ...

class NoPythonSupportedFeatureValidation(AnalysisPass):
    """NoPython Mode check: Validates the IR to ensure that features in use are
    in a form that is supported"""
    def __init__(self) -> None: ...
    def run_pass(self, state): ...

class IRLegalization(AnalysisPass):
    def __init__(self) -> None: ...
    def run_pass(self, state): ...

class NoPythonBackend(LoweringPass):
    def __init__(self) -> None: ...
    def run_pass(self, state):
        """
        Back-end: Generate LLVM IR from Numba IR, compile to machine code
        """

class InlineOverloads(FunctionPass):
    """
    This pass will inline a function wrapped by the numba.extending.overload
    decorator directly into the site of its call depending on the value set in
    the 'inline' kwarg to the decorator.

    This is a typed pass. CFG simplification and DCE are performed on
    completion.
    """
    def __init__(self) -> None: ...
    def run_pass(self, state):
        """Run inlining of overloads
        """

class DeadCodeElimination(FunctionPass):
    """
    Does dead code elimination
    """
    def __init__(self) -> None: ...
    def run_pass(self, state): ...

class PreLowerStripPhis(FunctionPass):
    """Remove phi nodes (ir.Expr.phi) introduced by SSA.

    This is needed before Lowering because the phi nodes in Numba IR do not
    match the semantics of phi nodes in LLVM IR. In Numba IR, phi nodes may
    expand into multiple LLVM instructions.
    """
    def __init__(self) -> None: ...
    def run_pass(self, state): ...
