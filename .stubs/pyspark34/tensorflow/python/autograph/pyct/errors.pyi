class PyCTError(Exception):
    """Base class for all exceptions."""
class UnsupportedLanguageElementError(PyCTError, NotImplementedError):
    """Raised for code patterns that AutoGraph does not support."""
class InaccessibleSourceCodeError(PyCTError, ValueError):
    """Raised when inspect can not access source code."""
