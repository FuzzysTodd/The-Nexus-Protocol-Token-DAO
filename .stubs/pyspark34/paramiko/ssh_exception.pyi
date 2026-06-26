import socket
from _typeshed import Incomplete

class SSHException(Exception):
    """
    Exception raised by failures in SSH2 protocol negotiation or logic errors.
    """
class AuthenticationException(SSHException):
    """
    Exception raised when authentication failed for some reason.  It may be
    possible to retry with different credentials.  (Other classes specify more
    specific reasons.)

    .. versionadded:: 1.6
    """
class PasswordRequiredException(AuthenticationException):
    """
    Exception raised when a password is needed to unlock a private key file.
    """

class BadAuthenticationType(AuthenticationException):
    """
    Exception raised when an authentication type (like password) is used, but
    the server isn't allowing that type.  (It may only allow public-key, for
    example.)

    .. versionadded:: 1.1
    """
    allowed_types: Incomplete
    explanation: Incomplete
    def __init__(self, explanation, types) -> None: ...

class PartialAuthentication(AuthenticationException):
    """
    An internal exception thrown in the case of partial authentication.
    """
    allowed_types: Incomplete
    def __init__(self, types) -> None: ...

class UnableToAuthenticate(AuthenticationException): ...

class ChannelException(SSHException):
    """
    Exception raised when an attempt to open a new `.Channel` fails.

    :param int code: the error code returned by the server

    .. versionadded:: 1.6
    """
    code: Incomplete
    text: Incomplete
    def __init__(self, code, text) -> None: ...

class BadHostKeyException(SSHException):
    """
    The host key given by the SSH server did not match what we were expecting.

    :param str hostname: the hostname of the SSH server
    :param PKey got_key: the host key presented by the server
    :param PKey expected_key: the host key expected

    .. versionadded:: 1.6
    """
    hostname: Incomplete
    key: Incomplete
    expected_key: Incomplete
    def __init__(self, hostname, got_key, expected_key) -> None: ...

class IncompatiblePeer(SSHException):
    """
    A disagreement arose regarding an algorithm required for key exchange.

    .. versionadded:: 2.9
    """

class ProxyCommandFailure(SSHException):
    '''
    The "ProxyCommand" found in the .ssh/config file returned an error.

    :param str command: The command line that is generating this exception.
    :param str error: The error captured from the proxy command output.
    '''
    command: Incomplete
    error: Incomplete
    def __init__(self, command, error) -> None: ...

class NoValidConnectionsError(socket.error):
    '''
    Multiple connection attempts were made and no families succeeded.

    This exception class wraps multiple "real" underlying connection errors,
    all of which represent failed connection attempts. Because these errors are
    not guaranteed to all be of the same error type (i.e. different errno,
    `socket.error` subclass, message, etc) we expose a single unified error
    message and a ``None`` errno so that instances of this class match most
    normal handling of `socket.error` objects.

    To see the wrapped exception objects, access the ``errors`` attribute.
    ``errors`` is a dict whose keys are address tuples (e.g. ``(\'127.0.0.1\',
    22)``) and whose values are the exception encountered trying to connect to
    that address.

    It is implied/assumed that all the errors given to a single instance of
    this class are from connecting to the same hostname + port (and thus that
    the differences are in the resolution of the hostname - e.g. IPv4 vs v6).

    .. versionadded:: 1.16
    '''
    errors: Incomplete
    def __init__(self, errors) -> None:
        """
        :param dict errors:
            The errors dict to store, as described by class docstring.
        """
    def __reduce__(self): ...

class CouldNotCanonicalize(SSHException):
    """
    Raised when hostname canonicalization fails & fallback is disabled.

    .. versionadded:: 2.7
    """
class ConfigParseError(SSHException):
    """
    A fatal error was encountered trying to parse SSH config data.

    Typically this means a config file violated the ``ssh_config``
    specification in a manner that requires exiting immediately, such as not
    matching ``key = value`` syntax or misusing certain ``Match`` keywords.

    .. versionadded:: 2.7
    """
