import torch
from _typeshed import Incomplete
from collections.abc import Generator
from torch.onnx._internal.diagnostics import infra as infra
from torch.utils import cpp_backtrace as cpp_backtrace

class ExportDiagnostic(infra.Diagnostic):
    """Base class for all export diagnostics.

    This class is used to represent all export diagnostics. It is a subclass of
    infra.Diagnostic, and adds additional methods to add more information to the
    diagnostic.
    """
    python_call_stack: infra.Stack | None
    cpp_call_stack: infra.Stack | None
    def __init__(self, *args, frames_to_skip: int = 1, cpp_stack: bool = False, **kwargs) -> None: ...
    def record_cpp_call_stack(self, frames_to_skip: int) -> infra.Stack:
        """Records the current C++ call stack in the diagnostic."""
    def record_fx_graphmodule(self, gm: torch.fx.GraphModule) -> None: ...

class ExportDiagnosticEngine(infra.DiagnosticEngine):
    """PyTorch ONNX Export diagnostic engine.

    The only purpose of creating this class instead of using the base class directly
    is to provide a background context for `diagnose` calls inside exporter.

    By design, one `torch.onnx.export` call should initialize one diagnostic context.
    All `diagnose` calls inside exporter should be made in the context of that export.
    However, since diagnostic context is currently being accessed via a global variable,
    there is no guarantee that the context is properly initialized. Therefore, we need
    to provide a default background context to fallback to, otherwise any invocation of
    exporter internals, e.g. unit tests, will fail due to missing diagnostic context.
    This can be removed once the pipeline for context to flow through the exporter is
    established.
    """
    def __init__(self) -> None: ...
    @property
    def background_context(self) -> infra.DiagnosticContext: ...
    def clear(self) -> None: ...
    def sarif_log(self): ...

engine: Incomplete

def create_export_diagnostic_context() -> Generator[infra.DiagnosticContext, None, None]:
    """Create a diagnostic context for export.

    This is a workaround for code robustness since diagnostic context is accessed by
    export internals via global variable. See `ExportDiagnosticEngine` for more details.
    """
def diagnose(rule: infra.Rule, level: infra.Level, message: str | None = None, frames_to_skip: int = 2, **kwargs) -> ExportDiagnostic:
    """Creates a diagnostic and record it in the global diagnostic context.

    This is a wrapper around `context.record` that uses the global diagnostic context.
    """
def export_context() -> infra.DiagnosticContext: ...
