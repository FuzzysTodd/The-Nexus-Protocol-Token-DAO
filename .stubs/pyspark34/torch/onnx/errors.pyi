from torch import _C

__all__ = ['OnnxExporterError', 'OnnxExporterWarning', 'CallHintViolationWarning', 'CheckerError', 'UnsupportedOperatorError', 'SymbolicValueError']

class OnnxExporterWarning(UserWarning):
    """Base class for all warnings in the ONNX exporter."""
class CallHintViolationWarning(OnnxExporterWarning):
    """Warning raised when a type hint is violated during a function call."""
class OnnxExporterError(RuntimeError):
    """Errors raised by the ONNX exporter."""
class CheckerError(OnnxExporterError):
    """Raised when ONNX checker detects an invalid model."""

class UnsupportedOperatorError(OnnxExporterError):
    """Raised when an operator is unsupported by the exporter."""
    def __init__(self, name: str, version: int, supported_version: int | None) -> None: ...

class SymbolicValueError(OnnxExporterError):
    """Errors around TorchScript values and nodes."""
    def __init__(self, msg: str, value: _C.Value) -> None: ...
