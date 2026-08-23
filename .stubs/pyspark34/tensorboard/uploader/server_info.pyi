from tensorboard import version as version
from tensorboard.uploader.proto import server_info_pb2 as server_info_pb2

def fetch_server_info(origin, upload_plugins):
    '''Fetches server info from a remote server.

    Args:
      origin: The server with which to communicate. Should be a string
        like "https://tensorboard.dev", including protocol, host, and (if
        needed) port.
      upload_plugins: List of plugins names requested by the user and to be
        verified by the server.

    Returns:
      A `server_info_pb2.ServerInfoResponse` message.

    Raises:
      CommunicationError: Upon failure to connect to or successfully
        communicate with the remote server.
    '''
def create_server_info(frontend_origin, api_endpoint, upload_plugins):
    '''Manually creates server info given a frontend and backend.

    Args:
      frontend_origin: The origin of the TensorBoard.dev frontend, like
        "https://tensorboard.dev" or "http://localhost:8000".
      api_endpoint: As to `server_info_pb2.ApiServer.endpoint`.
      upload_plugins: List of plugin names requested by the user and to be
        verified by the server.

    Returns:
      A `server_info_pb2.ServerInfoResponse` message.
    '''
def experiment_url(server_info, experiment_id):
    """Formats a URL that will resolve to the provided experiment.

    Args:
      server_info: A `server_info_pb2.ServerInfoResponse` message.
      experiment_id: A string; the ID of the experiment to link to.

    Returns:
      A URL resolving to the given experiment, as a string.
    """
def allowed_plugins(server_info):
    """Determines which plugins may upload data.

    This pulls from the `plugin_control` on the `server_info` when that
    submessage is set, else falls back to a default.

    Args:
      server_info: A `server_info_pb2.ServerInfoResponse` message.

    Returns:
      A `frozenset` of plugin names.
    """
def upload_limits(server_info):
    """Returns UploadLimits, from server_info if possible, otherwise from defaults.

    Args:
      server_info: A `server_info_pb2.ServerInfoResponse` message.

    Returns:
      An instance of UploadLimits.
    """

class CommunicationError(RuntimeError):
    """Raised upon failure to communicate with the server."""
