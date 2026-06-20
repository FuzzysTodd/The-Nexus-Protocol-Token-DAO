import builtins
from typing import Type

class CryptoError(Exception):
    """
    Base exception for all nacl related errors
    """
class BadSignatureError(CryptoError):
    """
    Raised when the signature was forged or otherwise corrupt.
    """
class RuntimeError(builtins.RuntimeError, CryptoError): ...
class AssertionError(builtins.AssertionError, CryptoError): ...
class TypeError(builtins.TypeError, CryptoError): ...
class ValueError(builtins.ValueError, CryptoError): ...
class InvalidkeyError(CryptoError): ...
class CryptPrefixError(InvalidkeyError): ...
class UnavailableError(RuntimeError):
    """
    is a subclass of :class:`~nacl.exceptions.RuntimeError`, raised when
    trying to call functions not available in a minimal build of
    libsodium.
    """

def ensure(cond: bool, *args: object, **kwds: Type[Exception]) -> None:
    """
    Return if a condition is true, otherwise raise a caller-configurable
    :py:class:`Exception`
    :param bool cond: the condition to be checked
    :param sequence args: the arguments to be passed to the exception's
                          constructor
    The only accepted named parameter is `raising` used to configure the
    exception to be raised if `cond` is not `True`
    """
