from _typeshed import Incomplete
from tensorboard.data.experimental import base_experiment as base_experiment
from tensorboard.uploader import auth as auth, util as util
from tensorboard.uploader.proto import export_service_pb2 as export_service_pb2, export_service_pb2_grpc as export_service_pb2_grpc, server_info_pb2 as server_info_pb2
from tensorboard.util import grpc_util as grpc_util

DEFAULT_ORIGIN: str

def import_pandas():
    """Import pandas, guarded by a user-friendly error message on failure."""

class ExperimentFromDev(base_experiment.BaseExperiment):
    """Implementation of BaseExperiment, specialized for tensorboard.dev."""
    def __init__(self, experiment_id, api_endpoint: Incomplete | None = None) -> None:
        '''Constructor of ExperimentFromDev.

        Args:
          experiment_id: String ID of the experiment on tensorboard.dev (e.g.,
            "AdYd1TgeTlaLWXx6I8JUbA").
          api_endpoint: Optional override value for API endpoint. Used for
            development only.
        '''
    def get_scalars(self, runs_filter: Incomplete | None = None, tags_filter: Incomplete | None = None, pivot: bool = False, include_wall_time: bool = False): ...

def get_api_client(api_endpoint: Incomplete | None = None): ...
