from _typeshed import Incomplete
from collections.abc import Generator
from tensorboard.uploader import util as util
from tensorboard.uploader.proto import blob_pb2 as blob_pb2, experiment_pb2 as experiment_pb2, export_service_pb2 as export_service_pb2
from tensorboard.util import grpc_util as grpc_util, tb_logging as tb_logging, tensor_util as tensor_util

logger: Incomplete

class TensorBoardExporter:
    '''Exports all of the user\'s experiment data from TensorBoard.dev.

    Data is exported into a directory, with one file per experiment. Each
    experiment file is a sequence of time series, represented as a stream
    of JSON objects, one per line. Each JSON object includes a run name,
    tag name, `tensorboard.compat.proto.summary_pb2.SummaryMetadata` proto
    (base64-encoded, standard RFC 4648 alphabet), and set of points.
    Points are stored in three equal-length lists of steps, wall times (as
    seconds since epoch), and scalar values, for storage efficiency.

    Such streams of JSON objects may be conveniently processed with tools
    like jq(1).

    For example one line of an experiment file might read (when
    pretty-printed):

        {
          "points": {
            "steps": [0, 5],
            "values": [4.8935227394104, 2.5438034534454346],
            "wall_times": [1563406522.669238, 1563406523.0268838]
          },
          "run": "lr_1E-04,conv=1,fc=2",
          "summary_metadata": "CgkKB3NjYWxhcnMSC3hlbnQveGVudF8x",
          "tag": "xent/xent_1"
        }

    This is a time series with two points, both logged on 2019-07-17, one
    about 0.36 seconds after the other.
    '''
    def __init__(self, reader_service_client, output_directory) -> None:
        """Constructs a TensorBoardExporter.

        Args:
          reader_service_client: A TensorBoardExporterService stub instance.
          output_directory: Path to a directory into which to write data. The
            directory must not exist, to avoid stomping existing or concurrent
            output. Its ancestors will be created if needed.
        """
    def export(self, read_time: Incomplete | None = None) -> Generator[Incomplete, None, None]:
        """Executes the export flow.

        Args:
          read_time: A fixed timestamp from which to export data, as float seconds
            since epoch (like `time.time()`). Optional; defaults to the current
            time.

        Yields:
          After each experiment is successfully downloaded, the ID of that
          experiment, as a string.
        """

def list_experiments(api_client, fieldmask: Incomplete | None = None, read_time: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """Yields all of the calling user's experiments.

    Args:
      api_client: A TensorBoardExporterService stub instance.
      fieldmask: An optional `experiment_pb2.ExperimentMask` value.
      read_time: A fixed timestamp from which to export data, as float seconds
        since epoch (like `time.time()`). Optional; defaults to the current
        time.

    Yields:
      For each experiment owned by the user, an `experiment_pb2.Experiment`
      value.

    Raises:
      RuntimeError: If the server returns experiment IDs but no experiments,
        as in an old, unsupported version of the protocol.
    """

class OutputDirectoryExistsError(ValueError): ...

class GrpcTimeoutException(Exception):
    experiment_id: Incomplete
    def __init__(self, experiment_id) -> None: ...
