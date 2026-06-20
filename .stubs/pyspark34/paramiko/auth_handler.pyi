from _typeshed import Incomplete
from paramiko.common import AUTH_FAILED as AUTH_FAILED, AUTH_PARTIALLY_SUCCESSFUL as AUTH_PARTIALLY_SUCCESSFUL, AUTH_SUCCESSFUL as AUTH_SUCCESSFUL, DEBUG as DEBUG, DISCONNECT_NO_MORE_AUTH_METHODS_AVAILABLE as DISCONNECT_NO_MORE_AUTH_METHODS_AVAILABLE, DISCONNECT_SERVICE_NOT_AVAILABLE as DISCONNECT_SERVICE_NOT_AVAILABLE, INFO as INFO, MSG_NAMES as MSG_NAMES, MSG_SERVICE_ACCEPT as MSG_SERVICE_ACCEPT, MSG_SERVICE_REQUEST as MSG_SERVICE_REQUEST, MSG_USERAUTH_BANNER as MSG_USERAUTH_BANNER, MSG_USERAUTH_FAILURE as MSG_USERAUTH_FAILURE, MSG_USERAUTH_GSSAPI_ERROR as MSG_USERAUTH_GSSAPI_ERROR, MSG_USERAUTH_GSSAPI_ERRTOK as MSG_USERAUTH_GSSAPI_ERRTOK, MSG_USERAUTH_GSSAPI_MIC as MSG_USERAUTH_GSSAPI_MIC, MSG_USERAUTH_GSSAPI_RESPONSE as MSG_USERAUTH_GSSAPI_RESPONSE, MSG_USERAUTH_GSSAPI_TOKEN as MSG_USERAUTH_GSSAPI_TOKEN, MSG_USERAUTH_INFO_REQUEST as MSG_USERAUTH_INFO_REQUEST, MSG_USERAUTH_INFO_RESPONSE as MSG_USERAUTH_INFO_RESPONSE, MSG_USERAUTH_REQUEST as MSG_USERAUTH_REQUEST, MSG_USERAUTH_SUCCESS as MSG_USERAUTH_SUCCESS, WARNING as WARNING, cMSG_DISCONNECT as cMSG_DISCONNECT, cMSG_SERVICE_ACCEPT as cMSG_SERVICE_ACCEPT, cMSG_SERVICE_REQUEST as cMSG_SERVICE_REQUEST, cMSG_USERAUTH_BANNER as cMSG_USERAUTH_BANNER, cMSG_USERAUTH_FAILURE as cMSG_USERAUTH_FAILURE, cMSG_USERAUTH_GSSAPI_MIC as cMSG_USERAUTH_GSSAPI_MIC, cMSG_USERAUTH_GSSAPI_RESPONSE as cMSG_USERAUTH_GSSAPI_RESPONSE, cMSG_USERAUTH_GSSAPI_TOKEN as cMSG_USERAUTH_GSSAPI_TOKEN, cMSG_USERAUTH_INFO_REQUEST as cMSG_USERAUTH_INFO_REQUEST, cMSG_USERAUTH_INFO_RESPONSE as cMSG_USERAUTH_INFO_RESPONSE, cMSG_USERAUTH_PK_OK as cMSG_USERAUTH_PK_OK, cMSG_USERAUTH_REQUEST as cMSG_USERAUTH_REQUEST, cMSG_USERAUTH_SUCCESS as cMSG_USERAUTH_SUCCESS
from paramiko.message import Message as Message
from paramiko.server import InteractiveQuery as InteractiveQuery
from paramiko.ssh_exception import AuthenticationException as AuthenticationException, BadAuthenticationType as BadAuthenticationType, PartialAuthentication as PartialAuthentication, SSHException as SSHException
from paramiko.ssh_gss import GSSAuth as GSSAuth, GSS_EXCEPTIONS as GSS_EXCEPTIONS
from paramiko.util import b as b, u as u

class AuthHandler:
    """
    Internal class to handle the mechanics of authentication.
    """
    transport: Incomplete
    username: Incomplete
    authenticated: bool
    auth_event: Incomplete
    auth_method: str
    banner: Incomplete
    password: Incomplete
    private_key: Incomplete
    interactive_handler: Incomplete
    submethods: Incomplete
    auth_username: Incomplete
    auth_fail_count: int
    gss_host: Incomplete
    gss_deleg_creds: bool
    def __init__(self, transport) -> None: ...
    def is_authenticated(self): ...
    def get_username(self): ...
    def auth_none(self, username, event) -> None: ...
    def auth_publickey(self, username, key, event) -> None: ...
    def auth_password(self, username, password, event) -> None: ...
    def auth_interactive(self, username, handler, event, submethods: str = '') -> None:
        """
        response_list = handler(title, instructions, prompt_list)
        """
    def auth_gssapi_with_mic(self, username, gss_host, gss_deleg_creds, event) -> None: ...
    def auth_gssapi_keyex(self, username, event) -> None: ...
    def abort(self) -> None: ...
    def wait_for_response(self, event): ...

class GssapiWithMicAuthHandler:
    """A specialized Auth handler for gssapi-with-mic

    During the GSSAPI token exchange we need a modified dispatch table,
    because the packet type numbers are not unique.
    """
    method: str
    sshgss: Incomplete
    def __init__(self, delegate, sshgss) -> None: ...
    def abort(self): ...
    @property
    def transport(self): ...
    @property
    def auth_username(self): ...
    @property
    def gss_host(self): ...

class AuthOnlyHandler(AuthHandler):
    """
    AuthHandler, and just auth, no service requests!

    .. versionadded:: 3.2
    """
    auth_method: Incomplete
    username: Incomplete
    auth_event: Incomplete
    def send_auth_request(self, username, method, finish_message: Incomplete | None = None):
        """
        Submit a userauth request message & wait for response.

        Performs the transport message send call, sets self.auth_event, and
        will lock-n-block as necessary to both send, and wait for response to,
        the USERAUTH_REQUEST.

        Most callers will want to supply a callback to ``finish_message``,
        which accepts a Message ``m`` and may call mutator methods on it to add
        more fields.
        """
    def auth_none(self, username): ...
    def auth_publickey(self, username, key): ...
    def auth_password(self, username, password): ...
    interactive_handler: Incomplete
    def auth_interactive(self, username, handler, submethods: str = ''):
        """
        response_list = handler(title, instructions, prompt_list)
        """
