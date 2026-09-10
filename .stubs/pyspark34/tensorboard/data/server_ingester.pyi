from _typeshed import Incomplete
from tensorboard.data import grpc_provider as grpc_provider, ingester as ingester
from tensorboard.data.proto import data_provider_pb2 as data_provider_pb2
from tensorboard.util import tb_logging as tb_logging

logger: Incomplete

class ExistingServerDataIngester(ingester.DataIngester):
    """Connect to an already running gRPC server."""
    def __init__(self, address, *, channel_creds_type) -> None:
        """Initializes an ingester with the given configuration.

        Args:
          address: String, as passed to `--grpc_data_provider`.
          channel_creds_type: `grpc_util.ChannelCredsType`, as passed to
            `--grpc_creds_type`.
        """
    @property
    def data_provider(self): ...
    def start(self) -> None: ...

class SubprocessServerDataIngester(ingester.DataIngester):
    """Start a new data server as a subprocess."""
    def __init__(self, server_binary, logdir, *, reload_interval, channel_creds_type, samples_per_plugin: Incomplete | None = None, extra_flags: Incomplete | None = None) -> None:
        """Initializes an ingester with the given configuration.

        Args:
          server_binary: `ServerBinary` to launch.
          logdir: String, as passed to `--logdir`.
          reload_interval: Number, as passed to `--reload_interval`.
          channel_creds_type: `grpc_util.ChannelCredsType`, as passed to
            `--grpc_creds_type`.
          samples_per_plugin: Dict[String, Int], as parsed from
            `--samples_per_plugin`.
          extra_flags: List of extra string flags to be passed to the
            data server without further interpretation.
        """
    @property
    def data_provider(self): ...
    def start(self) -> None: ...

class NoDataServerError(RuntimeError): ...
class DataServerStartupError(RuntimeError): ...

class ServerBinary:
    """Information about a data server binary."""
    def __init__(self, path, version) -> None:
        """Initializes a `ServerBinary`.

        Args:
          path: String path to executable on disk.
          version: PEP 396-compliant version string, or `None` if
            unknown or not applicable. Binaries at unknown versions are
            assumed to be bleeding-edge: if you bring your own binary,
            it's on you to make sure that it's up to date.
        """
    @property
    def path(self): ...
    def at_least_version(self, required_version):
        '''Test whether the binary\'s version is at least the given one.

        Useful for gating features that are available in the latest data
        server builds from head, but not yet released to PyPI. For
        example, if v0.4.0 is the latest published version, you can
        check `at_least_version("0.5.0a0")` to include both prereleases
        at head and the eventual final release of v0.5.0.

        If this binary\'s version was set to `None` at construction time,
        this method always returns `True`.

        Args:
          required_version: PEP 396-compliant version string.

        Returns:
          Boolean.
        '''

def get_server_binary():
    """Get `ServerBinary` info or raise `NoDataServerError`."""
