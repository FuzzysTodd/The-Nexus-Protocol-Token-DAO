import abc
from _typeshed import Incomplete
from tensorboard import program as program
from tensorboard.compat import tf as tf
from tensorboard.plugins import base_plugin as base_plugin
from tensorboard.uploader import auth as auth, dry_run_stubs as dry_run_stubs, flags_parser as flags_parser, formatters as formatters
from tensorboard.uploader.proto import experiment_pb2 as experiment_pb2, export_service_pb2_grpc as export_service_pb2_grpc, server_info_pb2 as server_info_pb2, write_service_pb2_grpc as write_service_pb2_grpc

class _Intent(metaclass=abc.ABCMeta):
    '''A description of the user\'s intent in invoking this program.

    Each valid set of CLI flags corresponds to one intent: e.g., "upload
    data from this logdir", or "delete the experiment with that ID".
    '''
    @abc.abstractmethod
    def get_ack_message_body(self):
        """Gets the message to show when executing this intent at first login.

        This need not include the header (program name) or Terms of Service
        notice.

        Returns:
          A Unicode string, potentially spanning multiple lines.
        """
    @abc.abstractmethod
    def execute(self, server_info, channel):
        """Carries out this intent with the specified gRPC channel.

        Args:
          server_info: A `server_info_pb2.ServerInfoResponse` value.
          channel: A connected gRPC channel whose server provides the TensorBoard
            reader and writer services.
        """

class _AuthRevokeIntent(_Intent):
    """The user intends to revoke credentials."""
    def get_ack_message_body(self) -> None:
        """Must not be called."""
    def execute(self, server_info, channel) -> None:
        """Execute handled specially by `main`.

        Must not be called.
        """

class _DeleteExperimentIntent(_Intent):
    """The user intends to delete an experiment."""
    experiment_id_list: Incomplete
    def __init__(self, experiment_id_list) -> None: ...
    def get_ack_message_body(self): ...
    def execute(self, server_info, channel) -> None: ...

class _UpdateMetadataIntent(_Intent):
    """The user intends to update the metadata for an experiment."""
    experiment_id: Incomplete
    name: Incomplete
    description: Incomplete
    def __init__(self, experiment_id, name: Incomplete | None = None, description: Incomplete | None = None) -> None: ...
    def get_ack_message_body(self): ...
    def execute(self, server_info, channel) -> None: ...

class _ListIntent(_Intent):
    """The user intends to list all their experiments."""
    json: Incomplete
    def __init__(self, json: Incomplete | None = None) -> None:
        """Constructor of _ListIntent.

        Args:
          json: If and only if `True`, will print the list as pretty-formatted
            JSON objects, one object for each experiment.
        """
    def get_ack_message_body(self): ...
    def execute(self, server_info, channel) -> None: ...

class UploadIntent(_Intent):
    """The user intends to upload an experiment from the given logdir."""
    logdir: Incomplete
    name: Incomplete
    description: Incomplete
    verbosity: Incomplete
    dry_run: Incomplete
    one_shot: Incomplete
    experiment_url_callback: Incomplete
    def __init__(self, logdir, name: Incomplete | None = None, description: Incomplete | None = None, verbosity: Incomplete | None = None, dry_run: Incomplete | None = None, one_shot: Incomplete | None = None, experiment_url_callback: Incomplete | None = None) -> None: ...
    def get_ack_message_body(self): ...
    def execute(self, server_info, channel) -> None: ...

class _ExportIntent(_Intent):
    """The user intends to download all their experiment data."""
    output_dir: Incomplete
    def __init__(self, output_dir) -> None: ...
    def get_ack_message_body(self): ...
    def execute(self, server_info, channel) -> None: ...

class UploaderSubcommand(program.TensorBoardSubcommand):
    """Integration point with `tensorboard` CLI."""
    def __init__(self, experiment_url_callback: Incomplete | None = None) -> None:
        """Constructor of UploaderSubcommand.

        Args:
          experiment_url_callback: A function accepting a single string argument
            containing the full TB.dev URL of the uploaded experiment.
        """
    def name(self): ...
    def define_flags(self, parser) -> None: ...
    def run(self, flags): ...
    def help(self): ...
