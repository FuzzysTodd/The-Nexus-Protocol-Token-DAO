from _typeshed import Incomplete
from mlflow.entities import Dataset as Dataset, DatasetInput as DatasetInput, Experiment as Experiment, ExperimentTag as ExperimentTag, InputTag as InputTag, Metric as Metric, Param as Param, Run as Run, RunData as RunData, RunInfo as RunInfo, RunInputs as RunInputs, RunStatus as RunStatus, RunTag as RunTag, SourceType as SourceType, ViewType as ViewType
from mlflow.entities.lifecycle_stage import LifecycleStage as LifecycleStage
from mlflow.entities.run_info import check_run_is_active as check_run_is_active
from mlflow.environment_variables import MLFLOW_TRACKING_DIR as MLFLOW_TRACKING_DIR
from mlflow.exceptions import MissingConfigException as MissingConfigException, MlflowException as MlflowException
from mlflow.protos import databricks_pb2 as databricks_pb2
from mlflow.protos.databricks_pb2 import INTERNAL_ERROR as INTERNAL_ERROR, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, RESOURCE_DOES_NOT_EXIST as RESOURCE_DOES_NOT_EXIST
from mlflow.protos.internal_pb2 import InputVertexType as InputVertexType
from mlflow.store.entities.paged_list import PagedList as PagedList
from mlflow.store.tracking import DEFAULT_LOCAL_FILE_AND_ARTIFACT_PATH as DEFAULT_LOCAL_FILE_AND_ARTIFACT_PATH, SEARCH_MAX_RESULTS_DEFAULT as SEARCH_MAX_RESULTS_DEFAULT, SEARCH_MAX_RESULTS_THRESHOLD as SEARCH_MAX_RESULTS_THRESHOLD
from mlflow.store.tracking.abstract_store import AbstractStore as AbstractStore
from mlflow.utils import get_results_from_paginated_fn as get_results_from_paginated_fn
from mlflow.utils.file_utils import append_to as append_to, exists as exists, find as find, get_parent_dir as get_parent_dir, is_directory as is_directory, list_all as list_all, list_subdirs as list_subdirs, local_file_uri_to_path as local_file_uri_to_path, make_containing_dirs as make_containing_dirs, mkdir as mkdir, mv as mv, overwrite_yaml as overwrite_yaml, path_to_local_file_uri as path_to_local_file_uri, read_file as read_file, read_file_lines as read_file_lines, read_yaml as read_yaml, write_to as write_to, write_yaml as write_yaml
from mlflow.utils.mlflow_tags import MLFLOW_DATASET_CONTEXT as MLFLOW_DATASET_CONTEXT, MLFLOW_LOGGED_MODELS as MLFLOW_LOGGED_MODELS, MLFLOW_RUN_NAME as MLFLOW_RUN_NAME
from mlflow.utils.search_utils import SearchExperimentsUtils as SearchExperimentsUtils, SearchUtils as SearchUtils
from mlflow.utils.string_utils import is_string_type as is_string_type
from mlflow.utils.time_utils import get_current_time_millis as get_current_time_millis
from mlflow.utils.uri import append_to_uri_path as append_to_uri_path, resolve_uri_if_local as resolve_uri_if_local
from typing import Dict, List, NamedTuple

class FileStore(AbstractStore):
    TRASH_FOLDER_NAME: str
    ARTIFACTS_FOLDER_NAME: str
    METRICS_FOLDER_NAME: str
    PARAMS_FOLDER_NAME: str
    TAGS_FOLDER_NAME: str
    EXPERIMENT_TAGS_FOLDER_NAME: str
    DATASETS_FOLDER_NAME: str
    INPUTS_FOLDER_NAME: str
    RESERVED_EXPERIMENT_FOLDERS: Incomplete
    META_DATA_FILE_NAME: str
    DEFAULT_EXPERIMENT_ID: str
    root_directory: Incomplete
    artifact_root_uri: Incomplete
    trash_folder: Incomplete
    def __init__(self, root_directory: Incomplete | None = None, artifact_root_uri: Incomplete | None = None) -> None:
        """
        Create a new FileStore with the given root directory and a given default artifact root URI.
        """
    def search_experiments(self, view_type=..., max_results=..., filter_string: Incomplete | None = None, order_by: Incomplete | None = None, page_token: Incomplete | None = None): ...
    def get_experiment_by_name(self, experiment_name): ...
    def create_experiment(self, name, artifact_location: Incomplete | None = None, tags: Incomplete | None = None): ...
    def get_experiment(self, experiment_id):
        """
        Fetch the experiment.
        Note: This API will search for active as well as deleted experiments.

        :param experiment_id: Integer id for the experiment
        :return: A single Experiment object if it exists, otherwise raises an Exception.
        """
    def delete_experiment(self, experiment_id) -> None: ...
    def restore_experiment(self, experiment_id) -> None: ...
    def rename_experiment(self, experiment_id, new_name) -> None: ...
    def delete_run(self, run_id) -> None: ...
    def restore_run(self, run_id) -> None: ...
    def update_run_info(self, run_id, run_status, end_time, run_name): ...
    def create_run(self, experiment_id, user_id, start_time, tags, run_name):
        """
        Creates a run with the specified attributes.
        """
    def get_run(self, run_id):
        """
        Note: Will get both active and deleted runs.
        """
    def get_all_metrics(self, run_uuid): ...
    def get_metric_history(self, run_id, metric_key, max_results: Incomplete | None = None, page_token: Incomplete | None = None):
        """
        Return all logged values for a given metric.

        :param run_id: Unique identifier for run
        :param metric_key: Metric name within the run
        :param max_results: An indicator for paginated results. This functionality is not
            implemented for FileStore and is unused in this store's implementation.
        :param page_token: An indicator for paginated results. This functionality is not
            implemented for FileStore and if the value is overridden with a value other than
            ``None``, an MlflowException will be thrown.

        :return: A List of :py:class:`mlflow.entities.Metric` entities if ``metric_key`` values
            have been logged to the ``run_id``, else an empty list.
        """
    def get_all_params(self, run_uuid): ...
    def get_all_experiment_tags(self, exp_id): ...
    def get_all_tags(self, run_uuid): ...
    def log_metric(self, run_id, metric) -> None: ...
    def log_param(self, run_id, param) -> None: ...
    def set_experiment_tag(self, experiment_id, tag) -> None:
        """
        Set a tag for the specified experiment

        :param experiment_id: String ID of the experiment
        :param tag: ExperimentRunTag instance to log
        """
    def set_tag(self, run_id, tag) -> None: ...
    def delete_tag(self, run_id, key) -> None:
        """
        Delete a tag from a run. This is irreversible.
        :param run_id: String ID of the run
        :param key: Name of the tag
        """
    def log_batch(self, run_id, metrics, params, tags) -> None: ...
    def record_logged_model(self, run_id, mlflow_model) -> None: ...
    def log_inputs(self, run_id: str, datasets: List[DatasetInput] | None = None):
        """
        Log inputs, such as datasets, to the specified run.

        :param run_id: String id for the run
        :param datasets: List of :py:class:`mlflow.entities.DatasetInput` instances to log
                         as inputs to the run.

        :return: None.
        """
    class _FileStoreInput(NamedTuple):
        source_type: int
        source_id: str
        destination_type: int
        destination_id: str
        tags: Dict[str, str]
        def write_yaml(self, root: str, file_name: str): ...
        @classmethod
        def from_yaml(cls, root, file_name): ...
