import inspect
from torch.onnx._internal.diagnostics.infra import _infra, formatter as formatter
from typing import Any, Callable, Dict, Mapping, Tuple

def python_frame(frame: inspect.FrameInfo) -> _infra.StackFrame:
    """Returns a StackFrame for the given inspect.FrameInfo."""
def python_call_stack(frames_to_skip: int = 0, frames_to_log: int = 16) -> _infra.Stack:
    """Returns the current Python call stack."""
def function_location(fn: Callable) -> _infra.Location:
    """Returns a Location for the given function."""
def function_state(fn: Callable, args: Tuple[Any, ...], kwargs: Dict[str, Any]) -> Mapping[str, Any]: ...
