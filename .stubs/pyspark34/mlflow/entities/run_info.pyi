from _typeshed import Incomplete
from mlflow.entities._mlflow_object import _MLflowObject
from mlflow.entities.lifecycle_stage import LifecycleStage as LifecycleStage
from mlflow.entities.run_status import RunStatus as RunStatus
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE

def check_run_is_active(run_info) -> None: ...

class searchable_attribute(property): ...
class orderable_attribute(property): ...

class RunInfo(_MLflowObject):
    """
    Metadata about a run.
    """
    def __init__(self, run_uuid, experiment_id, user_id, status, start_time, end_time, lifecycle_stage, artifact_uri: Incomplete | None = None, run_id: Incomplete | None = None, run_name: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    @property
    def run_uuid(self):
        """[Deprecated, use run_id instead] String containing run UUID."""
    def run_id(self):
        """String containing run id."""
    @property
    def experiment_id(self):
        """String ID of the experiment for the current run."""
    def run_name(self):
        """String containing run name."""
    def user_id(self):
        """String ID of the user who initiated this run."""
    def status(self):
        """
        One of the values in :py:class:`mlflow.entities.RunStatus`
        describing the status of the run.
        """
    def start_time(self):
        """Start time of the run, in number of milliseconds since the UNIX epoch."""
    def end_time(self):
        """End time of the run, in number of milliseconds since the UNIX epoch."""
    def artifact_uri(self):
        """String root artifact URI of the run."""
    @property
    def lifecycle_stage(self): ...
    def to_proto(self): ...
    @classmethod
    def from_proto(cls, proto): ...
    @classmethod
    def get_searchable_attributes(cls): ...
    @classmethod
    def get_orderable_attributes(cls): ...
