from zope.interface import Interface

class IException(Interface):
    """Interface for `Exception`"""
class IStandardError(IException):
    """Interface for `StandardError` (no longer existing.)"""
class IWarning(IException):
    """Interface for `Warning`"""
class ISyntaxError(IStandardError):
    """Interface for `SyntaxError`"""
class ILookupError(IStandardError):
    """Interface for `LookupError`"""
class IValueError(IStandardError):
    """Interface for `ValueError`"""
class IRuntimeError(IStandardError):
    """Interface for `RuntimeError`"""
class IArithmeticError(IStandardError):
    """Interface for `ArithmeticError`"""
class IAssertionError(IStandardError):
    """Interface for `AssertionError`"""
class IAttributeError(IStandardError):
    """Interface for `AttributeError`"""
class IDeprecationWarning(IWarning):
    """Interface for `DeprecationWarning`"""
class IEOFError(IStandardError):
    """Interface for `EOFError`"""
class IEnvironmentError(IStandardError):
    """Interface for `EnvironmentError`"""
class IFloatingPointError(IArithmeticError):
    """Interface for `FloatingPointError`"""
class IIOError(IEnvironmentError):
    """Interface for `IOError`"""
class IImportError(IStandardError):
    """Interface for `ImportError`"""
class IIndentationError(ISyntaxError):
    """Interface for `IndentationError`"""
class IIndexError(ILookupError):
    """Interface for `IndexError`"""
class IKeyError(ILookupError):
    """Interface for `KeyError`"""
class IKeyboardInterrupt(IStandardError):
    """Interface for `KeyboardInterrupt`"""
class IMemoryError(IStandardError):
    """Interface for `MemoryError`"""
class INameError(IStandardError):
    """Interface for `NameError`"""
class INotImplementedError(IRuntimeError):
    """Interface for `NotImplementedError`"""
class IOSError(IEnvironmentError):
    """Interface for `OSError`"""
class IOverflowError(IArithmeticError):
    """Interface for `ArithmeticError`"""
class IOverflowWarning(IWarning):
    """Deprecated, no standard class implements this.

    This was the interface for ``OverflowWarning`` prior to Python 2.5,
    but that class was removed for all versions after that.
    """
class IReferenceError(IStandardError):
    """Interface for `ReferenceError`"""
class IRuntimeWarning(IWarning):
    """Interface for `RuntimeWarning`"""
class IStopIteration(IException):
    """Interface for `StopIteration`"""
class ISyntaxWarning(IWarning):
    """Interface for `SyntaxWarning`"""
class ISystemError(IStandardError):
    """Interface for `SystemError`"""
class ISystemExit(IException):
    """Interface for `SystemExit`"""
class ITabError(IIndentationError):
    """Interface for `TabError`"""
class ITypeError(IStandardError):
    """Interface for `TypeError`"""
class IUnboundLocalError(INameError):
    """Interface for `UnboundLocalError`"""
class IUnicodeError(IValueError):
    """Interface for `UnicodeError`"""
class IUserWarning(IWarning):
    """Interface for `UserWarning`"""
class IZeroDivisionError(IArithmeticError):
    """Interface for `ZeroDivisionError`"""
