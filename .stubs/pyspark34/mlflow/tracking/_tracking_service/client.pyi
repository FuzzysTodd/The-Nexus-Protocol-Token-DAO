from _typeshed import Incomplete
from mlflow.entities import ExperimentTag as ExperimentTag, Metric as Metric, Param as Param, RunStatus as RunStatus, RunTag as RunTag, ViewType as ViewType
from mlflow.entities.dataset_input import DatasetInput as DatasetInput
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import ErrorCode as ErrorCode, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.store.artifact.artifact_repository_registry import get_artifact_repository as get_artifact_repository
from mlflow.store.tracking import GET_METRIC_HISTORY_MAX_RESULTS as GET_METRIC_HISTORY_MAX_RESULTS, SEARCH_MAX_RESULTS_DEFAULT as SEARCH_MAX_RESULTS_DEFAULT
from mlflow.tracking._tracking_service import utils as utils
from mlflow.tracking.metric_value_conversion_utils import convert_metric_value_to_float_if_possible as convert_metric_value_to_float_if_possible
from mlflow.utils import chunk_list as chunk_list
from mlflow.utils.mlflow_tags import MLFLOW_USER as MLFLOW_USER
from mlflow.utils.string_utils import is_string_type as is_string_type
from mlflow.utils.time_utils import get_current_time_millis as get_current_time_millis
from mlflow.utils.uri import add_databricks_profile_info_to_artifact_uri as add_databricks_profile_info_to_artifact_uri
from mlflow.utils.validation import MAX_ENTITIES_PER_BATCH as MAX_ENTITIES_PER_BATCH, MAX_METRICS_PER_BATCH as MAX_METRICS_PER_BATCH, MAX_PARAMS_TAGS_PER_BATCH as MAX_PARAMS_TAGS_PER_BATCH, PARAM_VALIDATION_MSG as PARAM_VALIDATION_MSG
from typing import List

class TrackingServiceClient:
    """
    Client of an MLflow Tracking Server that creates and manages experiments and runs.
    """
    tracking_uri: Incomplete
    def __init__(self, tracking_uri) -> None:
        """
        :param tracking_uri: Address of local or remote tracking server.
        """
    @property
    def store(self): ...
    def get_run(self, run_id):
        """
        Fetch the run from backend store. The resulting :py:class:`Run <mlflow.entities.Run>`
        contains a collection of run metadata -- :py:class:`RunInfo <mlflow.entities.RunInfo>`,
        as well as a collection of run parameters, tags, and metrics --
        :py:class:`RunData <mlflow.entities.RunData>`. In the case where multiple metrics with the
        same key are logged for the run, the :py:class:`RunData <mlflow.entities.RunData>` contains
        the most recently logged value at the largest step for each metric.

        :param run_id: Unique identifier for the run.

        :return: A single :py:class:`mlflow.entities.Run` object, if the run exists. Otherwise,
                 raises an exception.
        """
    def get_metric_history(self, run_id, key):
        """
        Return a list of metric objects corresponding to all values logged for a given metric.

        :param run_id: Unique identifier for run
        :param key: Metric name within the run

        :return: A list of :py:class:`mlflow.entities.Metric` entities if logged, else empty list
        """
    def create_run(self, experiment_id, start_time: Incomplete | None = None, tags: Incomplete | None = None, run_name: Incomplete | None = None):
        '''
        Create a :py:class:`mlflow.entities.Run` object that can be associated with
        metrics, parameters, artifacts, etc.
        Unlike :py:func:`mlflow.projects.run`, creates objects but does not run code.
        Unlike :py:func:`mlflow.start_run`, does not change the "active run" used by
        :py:func:`mlflow.log_param`.

        :param experiment_id: The ID of the experiment to create a run in.
        :param start_time: If not provided, use the current timestamp.
        :param tags: A dictionary of key-value pairs that are converted into
                     :py:class:`mlflow.entities.RunTag` objects.
        :param run_name: The name of this run.
        :return: :py:class:`mlflow.entities.Run` that was created.
        '''
    def search_experiments(self, view_type=..., max_results=..., filter_string: Incomplete | None = None, order_by: Incomplete | None = None, page_token: Incomplete | None = None):
        '''
        Search for experiments that match the specified search query.

        :param view_type: One of enum values ``ACTIVE_ONLY``, ``DELETED_ONLY``, or ``ALL``
                          defined in :py:class:`mlflow.entities.ViewType`.
        :param max_results: Maximum number of experiments desired. Certain server backend may apply
                            its own limit.
        :param filter_string:
            Filter query string (e.g., ``"name = \'my_experiment\'"``), defaults to searching for all
            experiments. The following identifiers, comparators, and logical operators are
            supported.

            Identifiers
              - ``name``: Experiment name
              - ``creation_time``: Experiment creation time
              - ``last_update_time``: Experiment last update time
              - ``tags.<tag_key>``: Experiment tag. If ``tag_key`` contains
                spaces, it must be wrapped with backticks (e.g., ``"tags.`extra key`"``).

            Comparators for string attributes and tags
              - ``=``: Equal to
              - ``!=``: Not equal to
              - ``LIKE``: Case-sensitive pattern match
              - ``ILIKE``: Case-insensitive pattern match

            Comparators for numeric attributes
              - ``=``: Equal to
              - ``!=``: Not equal to
              - ``<``: Less than
              - ``<=``: Less than or equal to
              - ``>``: Greater than
              - ``>=``: Greater than or equal to

            Logical operators
              - ``AND``: Combines two sub-queries and returns True if both of them are True.

        :param order_by:
            List of columns to order by. The ``order_by`` column can contain an optional ``DESC`` or
            ``ASC`` value (e.g., ``"name DESC"``). The default ordering is ``ASC``, so ``"name"`` is
            equivalent to ``"name ASC"``. If unspecified, defaults to ``["last_update_time DESC"]``,
            which lists experiments updated most recently first. The following fields are supported:

            - ``experiment_id``: Experiment ID
            - ``name``: Experiment name
            - ``creation_time``: Experiment creation time
            - ``last_update_time``: Experiment last update time

        :param page_token: Token specifying the next page of results. It should be obtained from
                           a ``search_experiments`` call.
        :return: A :py:class:`PagedList <mlflow.store.entities.PagedList>` of
                 :py:class:`Experiment <mlflow.entities.Experiment>` objects. The pagination token
                 for the next page can be obtained via the ``token`` attribute of the object.
        '''
    def get_experiment(self, experiment_id):
        """
        :param experiment_id: The experiment ID returned from ``create_experiment``.
        :return: :py:class:`mlflow.entities.Experiment`
        """
    def get_experiment_by_name(self, name):
        """
        :param name: The experiment name.
        :return: :py:class:`mlflow.entities.Experiment`
        """
    def create_experiment(self, name, artifact_location: Incomplete | None = None, tags: Incomplete | None = None):
        """Create an experiment.

        :param name: The experiment name. Must be unique.
        :param artifact_location: The location to store run artifacts.
                                  If not provided, the server picks an appropriate default.
        :param tags: A dictionary of key-value pairs that are converted into
                                  :py:class:`mlflow.entities.ExperimentTag` objects.
        :return: Integer ID of the created experiment.
        """
    def delete_experiment(self, experiment_id) -> None:
        """
        Delete an experiment from the backend store.

        :param experiment_id: The experiment ID returned from ``create_experiment``.
        """
    def restore_experiment(self, experiment_id) -> None:
        """
        Restore a deleted experiment unless permanently deleted.

        :param experiment_id: The experiment ID returned from ``create_experiment``.
        """
    def rename_experiment(self, experiment_id, new_name) -> None:
        """
        Update an experiment's name. The new name must be unique.

        :param experiment_id: The experiment ID returned from ``create_experiment``.
        """
    def log_metric(self, run_id, key, value, timestamp: Incomplete | None = None, step: Incomplete | None = None) -> None:
        """
        Log a metric against the run ID.

        :param run_id: The run id to which the metric should be logged.
        :param key: Metric name (string). This string may only contain alphanumerics,
                    underscores (_), dashes (-), periods (.), spaces ( ), and slashes (/).
                    All backend stores will support keys up to length 250, but some may
                    support larger keys.
        :param value: Metric value (float) or single-item ndarray / tensor.
                      Note that some special values such
                      as +/- Infinity may be replaced by other values depending on the store. For
                      example, the SQLAlchemy store replaces +/- Inf with max / min float values.
                      All backend stores will support values up to length 5000, but some
                      may support larger values.
        :param timestamp: Time when this metric was calculated. Defaults to the current system time.
        :param step: Training step (iteration) at which was the metric calculated. Defaults to 0.
        """
    def log_param(self, run_id, key, value) -> None:
        """
        Log a parameter (e.g. model hyperparameter) against the run ID. Value is converted to
        a string.
        """
    def set_experiment_tag(self, experiment_id, key, value) -> None:
        """
        Set a tag on the experiment with the specified ID. Value is converted to a string.

        :param experiment_id: String ID of the experiment.
        :param key: Name of the tag.
        :param value: Tag value (converted to a string).
        """
    def set_tag(self, run_id, key, value) -> None:
        """
        Set a tag on the run with the specified ID. Value is converted to a string.

        :param run_id: String ID of the run.
        :param key: Tag name (string). This string may only contain alphanumerics, underscores
                    (_), dashes (-), periods (.), spaces ( ), and slashes (/).
                    All backend stores will support keys up to length 250, but some may
                    support larger keys.
        :param value: Tag value (string, but will be string-ified if not).
                      All backend stores will support values up to length 5000, but some
                      may support larger values.
        """
    def delete_tag(self, run_id, key) -> None:
        """
        Delete a tag from a run. This is irreversible.

        :param run_id: String ID of the run
        :param key: Name of the tag
        """
    def update_run(self, run_id, status: Incomplete | None = None, name: Incomplete | None = None) -> None:
        """
        Update a run with the specified ID to a new status or name.

        :param run_id: The ID of the Run to update.
        :param status: The new status of the run to set, if specified.
                       At least one of ``status`` or ``name`` should be specified.
        :param name: The new name of the run to set, if specified.
                     At least one of ``name`` or ``status`` should be specified.
        """
    def log_batch(self, run_id, metrics=(), params=(), tags=()) -> None:
        """
        Log multiple metrics, params, and/or tags.

        :param run_id: String ID of the run
        :param metrics: If provided, List of Metric(key, value, timestamp) instances.
        :param params: If provided, List of Param(key, value) instances.
        :param tags: If provided, List of RunTag(key, value) instances.

        Raises an MlflowException if any errors occur.
        :return: None
        """
    def log_inputs(self, run_id: str, datasets: List[DatasetInput] | None = None):
        """
        Log one or more dataset inputs to a run.

        :param run_id: String ID of the run
        :param datasets: List of :py:class:`mlflow.entities.DatasetInput` instances to log.

        Raises an MlflowException if any errors occur.
        :return: None
        """
    def log_artifact(self, run_id, local_path, artifact_path: Incomplete | None = None) -> None:
        """
        Write a local file or directory to the remote ``artifact_uri``.

        :param local_path: Path to the file or directory to write.
        :param artifact_path: If provided, the directory in ``artifact_uri`` to write to.
        """
    def log_artifacts(self, run_id, local_dir, artifact_path: Incomplete | None = None) -> None:
        """
        Write a directory of files to the remote ``artifact_uri``.

        :param local_dir: Path to the directory of files to write.
        :param artifact_path: If provided, the directory in ``artifact_uri`` to write to.
        """
    def list_artifacts(self, run_id, path: Incomplete | None = None):
        """
        List the artifacts for a run.

        :param run_id: The run to list artifacts from.
        :param path: The run's relative artifact path to list from. By default it is set to None
                     or the root artifact path.
        :return: List of :py:class:`mlflow.entities.FileInfo`
        """
    def download_artifacts(self, run_id, path, dst_path: Incomplete | None = None):
        """
        Download an artifact file or directory from a run to a local directory if applicable,
        and return a local path for it.

        :param run_id: The run to download artifacts from.
        :param path: Relative source path to the desired artifact.
        :param dst_path: Absolute path of the local filesystem destination directory to which to
                         download the specified artifacts. This directory must already exist.
                         If unspecified, the artifacts will either be downloaded to a new
                         uniquely-named directory on the local filesystem or will be returned
                         directly in the case of the LocalArtifactRepository.
        :return: Local path of desired artifact.
        """
    def set_terminated(self, run_id, status: Incomplete | None = None, end_time: Incomplete | None = None) -> None:
        '''Set a run\'s status to terminated.

        :param status: A string value of :py:class:`mlflow.entities.RunStatus`.
                       Defaults to "FINISHED".
        :param end_time: If not provided, defaults to the current time.'''
    def delete_run(self, run_id) -> None:
        """
        Deletes a run with the given ID.
        """
    def restore_run(self, run_id) -> None:
        """
        Restores a deleted run with the given ID.
        """
    def search_runs(self, experiment_ids, filter_string: str = '', run_view_type=..., max_results=..., order_by: Incomplete | None = None, page_token: Incomplete | None = None):
        '''
        Search experiments that fit the search criteria.

        :param experiment_ids: List of experiment IDs, or a single int or string id.
        :param filter_string: Filter query string, defaults to searching all runs.
        :param run_view_type: one of enum values ACTIVE_ONLY, DELETED_ONLY, or ALL runs
                              defined in :py:class:`mlflow.entities.ViewType`.
        :param max_results: Maximum number of runs desired.
        :param order_by: List of columns to order by (e.g., "metrics.rmse"). The ``order_by`` column
                     can contain an optional ``DESC`` or ``ASC`` value. The default is ``ASC``.
                     The default ordering is to sort by ``start_time DESC``, then ``run_id``.
        :param page_token: Token specifying the next page of results. It should be obtained from
            a ``search_runs`` call.

        :return: A :py:class:`PagedList <mlflow.store.entities.PagedList>` of
            :py:class:`Run <mlflow.entities.Run>` objects that satisfy the search expressions.
            If the underlying tracking store supports pagination, the token for the next page may
            be obtained via the ``token`` attribute of the returned object.
        '''
