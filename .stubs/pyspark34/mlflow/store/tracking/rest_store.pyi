from _typeshed import Incomplete
from mlflow.entities import DatasetInput as DatasetInput, Experiment as Experiment, Metric as Metric, Run as Run, RunInfo as RunInfo, ViewType as ViewType
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos import databricks_pb2 as databricks_pb2
from mlflow.protos.service_pb2 import CreateExperiment as CreateExperiment, CreateRun as CreateRun, DeleteExperiment as DeleteExperiment, DeleteRun as DeleteRun, DeleteTag as DeleteTag, GetExperiment as GetExperiment, GetExperimentByName as GetExperimentByName, GetMetricHistory as GetMetricHistory, GetRun as GetRun, LogBatch as LogBatch, LogInputs as LogInputs, LogMetric as LogMetric, LogModel as LogModel, LogParam as LogParam, MlflowService as MlflowService, RestoreExperiment as RestoreExperiment, RestoreRun as RestoreRun, SearchExperiments as SearchExperiments, SearchRuns as SearchRuns, SetExperimentTag as SetExperimentTag, SetTag as SetTag, UpdateExperiment as UpdateExperiment, UpdateRun as UpdateRun
from mlflow.store.entities.paged_list import PagedList as PagedList
from mlflow.store.tracking.abstract_store import AbstractStore as AbstractStore
from mlflow.utils.proto_json_utils import message_to_json as message_to_json
from mlflow.utils.rest_utils import call_endpoint as call_endpoint, extract_api_info_for_service as extract_api_info_for_service
from typing import List

class RestStore(AbstractStore):
    """
    Client for a remote tracking server accessed via REST API calls

    :param get_host_creds: Method to be invoked prior to every REST request to get the
      :py:class:`mlflow.rest_utils.MlflowHostCreds` for the request. Note that this
      is a function so that we can obtain fresh credentials in the case of expiry.
    """
    get_host_creds: Incomplete
    def __init__(self, get_host_creds) -> None: ...
    def search_experiments(self, view_type=..., max_results: Incomplete | None = None, filter_string: Incomplete | None = None, order_by: Incomplete | None = None, page_token: Incomplete | None = None): ...
    def create_experiment(self, name, artifact_location: Incomplete | None = None, tags: Incomplete | None = None):
        """
        Create a new experiment.
        If an experiment with the given name already exists, throws exception.

        :param name: Desired name for an experiment

        :return: experiment_id (string) for the newly created experiment if successful, else None
        """
    def get_experiment(self, experiment_id):
        """
        Fetch the experiment from the backend store.

        :param experiment_id: String id for the experiment

        :return: A single :py:class:`mlflow.entities.Experiment` object if it exists,
        otherwise raises an Exception.
        """
    def delete_experiment(self, experiment_id) -> None: ...
    def restore_experiment(self, experiment_id) -> None: ...
    def rename_experiment(self, experiment_id, new_name) -> None: ...
    def get_run(self, run_id):
        """
        Fetch the run from backend store

        :param run_id: Unique identifier for the run

        :return: A single Run object if it exists, otherwise raises an Exception
        """
    def update_run_info(self, run_id, run_status, end_time, run_name):
        """Updates the metadata of the specified run."""
    def create_run(self, experiment_id, user_id, start_time, tags, run_name):
        '''
        Create a run under the specified experiment ID, setting the run\'s status to "RUNNING"
        and the start time to the current time.

        :param experiment_id: ID of the experiment for this run
        :param user_id: ID of the user launching this run
        :param start_time: timestamp of the initialization of the run
        :param tags: tags to apply to this run at initialization
        :param name: Name of this run.

        :return: The created Run object
        '''
    def log_metric(self, run_id, metric) -> None:
        """
        Log a metric for the specified run

        :param run_id: String id for the run
        :param metric: Metric instance to log
        """
    def log_param(self, run_id, param) -> None:
        """
        Log a param for the specified run

        :param run_id: String id for the run
        :param param: Param instance to log
        """
    def set_experiment_tag(self, experiment_id, tag) -> None:
        """
        Set a tag for the specified experiment

        :param experiment_id: String ID of the experiment
        :param tag: ExperimentRunTag instance to log
        """
    def set_tag(self, run_id, tag) -> None:
        """
        Set a tag for the specified run

        :param run_id: String ID of the run
        :param tag: RunTag instance to log
        """
    def delete_tag(self, run_id, key) -> None:
        """
        Delete a tag from a run. This is irreversible.
        :param run_id: String ID of the run
        :param key: Name of the tag
        """
    def get_metric_history(self, run_id, metric_key, max_results: Incomplete | None = None, page_token: Incomplete | None = None):
        """
        Return all logged values for a given metric.

        :param run_id: Unique identifier for run
        :param metric_key: Metric name within the run
        :param max_results: Maximum number of metric history events (steps) to return per paged
            query. Only supported in 'databricks' backend.
        :param page_token: A Token specifying the next paginated set of results of metric history.

        :return: A PagedList of :py:class:`mlflow.entities.Metric` entities if a paginated request
            is made by setting ``max_results`` to a value other than ``None``, a List of
            :py:class:`mlflow.entities.Metric` entities if ``max_results`` is None, else, if no
            metrics of the ``metric_key`` have been logged to the ``run_id``, an empty list.
        """
    def delete_run(self, run_id) -> None: ...
    def restore_run(self, run_id) -> None: ...
    def get_experiment_by_name(self, experiment_name): ...
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
