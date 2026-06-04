import os
import zmq
from typing import Any, Dict, List

__all__ = ['Authenticator', 'CURVE_ALLOW_ANY']

CURVE_ALLOW_ANY: str

class Authenticator:
    '''Implementation of ZAP authentication for zmq connections.

    This authenticator class does not register with an event loop. As a result,
    you will need to manually call `handle_zap_message`::

        auth = zmq.Authenticator()
        auth.allow("127.0.0.1")
        auth.start()
        while True:
            await auth.handle_zap_msg(auth.zap_socket.recv_multipart())

    Alternatively, you can register `auth.zap_socket` with a poller.

    Since many users will want to run ZAP in a way that does not block the
    main thread, other authentication classes (such as :mod:`zmq.auth.thread`)
    are provided.

    Note:

    - libzmq provides four levels of security: default NULL (which the Authenticator does
      not see), and authenticated NULL, PLAIN, CURVE, and GSSAPI, which the Authenticator can see.
    - until you add policies, all incoming NULL connections are allowed.
      (classic ZeroMQ behavior), and all PLAIN and CURVE connections are denied.
    - GSSAPI requires no configuration.
    '''
    context: zmq.Context
    encoding: str
    allow_any: bool
    credentials_providers: Dict[str, Any]
    zap_socket: zmq.Socket
    passwords: Dict[str, Dict[str, str]]
    certs: Dict[str, Dict[bytes, Any]]
    log: Any
    def __init__(self, context: zmq.Context | None = None, encoding: str = 'utf-8', log: Any = None) -> None: ...
    def start(self) -> None:
        """Create and bind the ZAP socket"""
    def stop(self) -> None:
        """Close the ZAP socket"""
    def allow(self, *addresses: str) -> None:
        """Allow IP address(es).

        Connections from addresses not explicitly allowed will be rejected.

        - For NULL, all clients from this address will be accepted.
        - For real auth setups, they will be allowed to continue with authentication.

        allow is mutually exclusive with deny.
        """
    def deny(self, *addresses: str) -> None:
        """Deny IP address(es).

        Addresses not explicitly denied will be allowed to continue with authentication.

        deny is mutually exclusive with allow.
        """
    def configure_plain(self, domain: str = '*', passwords: Dict[str, str] | None = None) -> None:
        '''Configure PLAIN authentication for a given domain.

        PLAIN authentication uses a plain-text password file.
        To cover all domains, use "*".
        You can modify the password file at any time; it is reloaded automatically.
        '''
    def configure_curve(self, domain: str = '*', location: str | os.PathLike = '.') -> None:
        '''Configure CURVE authentication for a given domain.

        CURVE authentication uses a directory that holds all public client certificates,
        i.e. their public keys.

        To cover all domains, use "*".

        You can add and remove certificates in that directory at any time. configure_curve must be called
        every time certificates are added or removed, in order to update the Authenticator\'s state

        To allow all client keys without checking, specify CURVE_ALLOW_ANY for the location.
        '''
    def configure_curve_callback(self, domain: str = '*', credentials_provider: Any = None) -> None:
        '''Configure CURVE authentication for a given domain.

        CURVE authentication using a callback function validating
        the client public key according to a custom mechanism, e.g. checking the
        key against records in a db. credentials_provider is an object of a class which
        implements a callback method accepting two parameters (domain and key), e.g.::

            class CredentialsProvider(object):

                def __init__(self):
                    ...e.g. db connection

                def callback(self, domain, key):
                    valid = ...lookup key and/or domain in db
                    if valid:
                        logging.info(\'Authorizing: {0}, {1}\'.format(domain, key))
                        return True
                    else:
                        logging.warning(\'NOT Authorizing: {0}, {1}\'.format(domain, key))
                        return False

        To cover all domains, use "*".
        '''
    def curve_user_id(self, client_public_key: bytes) -> str:
        """Return the User-Id corresponding to a CURVE client's public key

        Default implementation uses the z85-encoding of the public key.

        Override to define a custom mapping of public key : user-id

        This is only called on successful authentication.

        Parameters
        ----------
        client_public_key: bytes
            The client public key used for the given message

        Returns
        -------
        user_id: unicode
            The user ID as text
        """
    def configure_gssapi(self, domain: str = '*', location: str | None = None) -> None:
        """Configure GSSAPI authentication

        Currently this is a no-op because there is nothing to configure with GSSAPI.
        """
    async def handle_zap_message(self, msg: List[bytes]):
        """Perform ZAP authentication"""
