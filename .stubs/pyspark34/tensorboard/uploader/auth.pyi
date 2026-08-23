import google.oauth2.credentials
import grpc
from _typeshed import Incomplete
from tensorboard.uploader import util as util
from tensorboard.util import tb_logging as tb_logging

logger: Incomplete
OPENID_CONNECT_SCOPES: Incomplete
TENSORBOARD_CREDENTIALS_FILEPATH_PARTS: Incomplete

class CredentialsStore:
    """Private file store for a `google.oauth2.credentials.Credentials`."""
    def __init__(self, user_config_directory=...) -> None:
        """Creates a CredentialsStore.

        Args:
          user_config_directory: Optional absolute path to the root directory for
            storing user configs, under which to store the credentials file. If not
            set, defaults to a platform-specific location. If set to None, the
            store is disabled (reads return None; write and clear are no-ops).
        """
    def read_credentials(self):
        """Returns the current `google.oauth2.credentials.Credentials`, or
        None."""
    def write_credentials(self, credentials) -> None:
        """Writes a `google.oauth2.credentials.Credentials` to the store."""
    def clear(self) -> None:
        """Clears the store of any persisted credentials information."""

def authenticate_user(force_console: bool = False) -> google.oauth2.credentials.Credentials:
    """Makes the user authenticate to retrieve auth credentials.

    The default behavior is to use the [installed app flow](
    http://developers.google.com/identity/protocols/oauth2/native-app), in which
    a browser is started for the user to authenticate, along with a local web
    server. The authentication in the browser would produce a redirect response
    to `localhost` with an authorization code that would then be received by the
    local web server started here.

    The two most notable cases where the default flow is not well supported are:
    - When the uploader is run from a colab notebook.
    - Then the uploader is run via a remote terminal (SSH).

    If any of the following is true, a different auth flow will be used:
    - the flag `--auth_force_console` is set to true, or
    - a browser is not available, or
    - a local web server cannot be started

    In this case, a [limited-input device flow](
    http://developers.google.com/identity/protocols/oauth2/limited-input-device)
    will be used, in which the user is presented with a URL and a short code
    that they'd need to use to authenticate and authorize access in a separate
    browser or device. The uploader will poll for access until the access is
    granted or rejected, or the initiated authorization request expires.
    """

class _LimitedInputDeviceAuthFlow:
    """OAuth flow to authenticate using the limited-input device flow.

    See:
    http://developers.google.com/identity/protocols/oauth2/limited-input-device
    """
    def __init__(self, client_config, scopes) -> None: ...
    def run(self) -> google.oauth2.credentials.Credentials: ...

class IdTokenAuthMetadataPlugin(grpc.AuthMetadataPlugin):
    """A `gRPC AuthMetadataPlugin` that uses ID tokens.

    This works like the existing `google.auth.transport.grpc.AuthMetadataPlugin`
    except that instead of always using access tokens, it preferentially uses the
    `Credentials.id_token` property if available (and logs an error otherwise).

    See http://www.grpc.io/grpc/python/grpc.html#grpc.AuthMetadataPlugin
    """
    def __init__(self, credentials, request) -> None:
        """Constructs an IdTokenAuthMetadataPlugin.

        Args:
          credentials (google.auth.credentials.Credentials): The credentials to
            add to requests.
          request (google.auth.transport.Request): A HTTP transport request object
            used to refresh credentials as needed.
        """
    def __call__(self, context, callback) -> None:
        """Passes authorization metadata into the given callback.

        Args:
          context (grpc.AuthMetadataContext): The RPC context.
          callback (grpc.AuthMetadataPluginCallback): The callback that will
            be invoked to pass in the authorization metadata.
        """

def id_token_call_credentials(credentials):
    """Constructs `grpc.CallCredentials` using
    `google.auth.Credentials.id_token`.

    Args:
      credentials (google.auth.credentials.Credentials): The credentials to use.

    Returns:
      grpc.CallCredentials: The call credentials.
    """
