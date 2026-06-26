from _typeshed import Incomplete
from mlflow.entities import DatasetInput as DatasetInput, Experiment as Experiment, Metric as Metric, Run as Run, RunInputs as RunInputs, RunStatus as RunStatus, RunTag as RunTag, SourceType as SourceType, ViewType as ViewType
from mlflow.entities.lifecycle_stage import LifecycleStage as LifecycleStage
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INTERNAL_ERROR as INTERNAL_ERROR, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, INVALID_STATE as INVALID_STATE, RESOURCE_ALREADY_EXISTS as RESOURCE_ALREADY_EXISTS, RESOURCE_DOES_NOT_EXIST as RESOURCE_DOES_NOT_EXIST
from mlflow.store.db.db_types import MSSQL as MSSQL, MYSQL as MYSQL
from mlflow.store.entities.paged_list import PagedList as PagedList
from mlflow.store.tracking import SEARCH_MAX_RESULTS_DEFAULT as SEARCH_MAX_RESULTS_DEFAULT, SEARCH_MAX_RESULTS_THRESHOLD as SEARCH_MAX_RESULTS_THRESHOLD
from mlflow.store.tracking.abstract_store import AbstractStore as AbstractStore
from mlflow.store.tracking.dbmodels.models import SqlDataset as SqlDataset, SqlExperiment as SqlExperiment, SqlExperimentTag as SqlExperimentTag, SqlInput as SqlInput, SqlInputTag as SqlInputTag, SqlLatestMetric as SqlLatestMetric, SqlMetric as SqlMetric, SqlParam as SqlParam, SqlRun as SqlRun, SqlTag as SqlTag
from mlflow.utils.file_utils import local_file_uri_to_path as local_file_uri_to_path, mkdir as mkdir
from mlflow.utils.mlflow_tags import MLFLOW_DATASET_CONTEXT as MLFLOW_DATASET_CONTEXT, MLFLOW_LOGGED_MODELS as MLFLOW_LOGGED_MODELS, MLFLOW_RUN_NAME as MLFLOW_RUN_NAME
from mlflow.utils.search_utils import SearchExperimentsUtils as SearchExperimentsUtils, SearchUtils as SearchUtils
from mlflow.utils.string_utils import is_string_type as is_string_type
from mlflow.utils.time_utils import get_current_time_millis as get_current_time_millis
from mlflow.utils.uri import append_to_uri_path as append_to_uri_path, extract_db_type_from_uri as extract_db_type_from_uri, is_local_uri as is_local_uri, resolve_uri_if_local as resolve_uri_if_local
from typing import List

class SqlAlchemyStore(AbstractStore):
    """
    SQLAlchemy compliant backend store for tracking meta data for MLflow entities. MLflow
    supports the database dialects ``mysql``, ``mssql``, ``sqlite``, and ``postgresql``.
    As specified in the
    `SQLAlchemy docs <https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls>`_ ,
    the database URI is expected in the format
    ``<dialect>+<driver>://<username>:<password>@<host>:<port>/<database>``. If you do not
    specify a driver, SQLAlchemy uses a dialect's default driver.

    This store interacts with SQL store using SQLAlchemy abstractions defined for MLflow entities.
    :py:class:`mlflow.store.dbmodels.models.SqlExperiment`,
    :py:class:`mlflow.store.dbmodels.models.SqlRun`,
    :py:class:`mlflow.store.dbmodels.models.SqlTag`,
    :py:class:`mlflow.store.dbmodels.models.SqlMetric`, and
    :py:class:`mlflow.store.dbmodels.models.SqlParam`.

    Run artifacts are stored in a separate location using artifact stores conforming to
    :py:class:`mlflow.store.artifact_repo.ArtifactRepository`. Default artifact locations for
    user experiments are stored in the database along with metadata. Each run artifact location
    is recorded in :py:class:`mlflow.store.dbmodels.models.SqlRun` and stored in the backend DB.
    """
    ARTIFACTS_FOLDER_NAME: str
    DEFAULT_EXPERIMENT_ID: str
    db_uri: Incomplete
    db_type: Incomplete
    artifact_root_uri: Incomplete
    engine: Incomplete
    ManagedSessionMaker: Incomplete
    def __init__(self, db_uri, default_artifact_root) -> None:
        """
        Create a database backed store.

        :param db_uri: The SQLAlchemy database URI string to connect to the database. See
                       the `SQLAlchemy docs
                       <https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls>`_
                       for format specifications. Mlflow supports the dialects ``mysql``,
                       ``mssql``, ``sqlite``, and ``postgresql``.
        :param default_artifact_root: Path/URI to location suitable for large data (such as a blob
                                      store object, DBFS path, or shared NFS file system).
        """
    def create_experiment(self, name, artifact_location: Incomplete | None = None, tags: Incomplete | None = None): ...
    def search_experiments(self, view_type=..., max_results=..., filter_string: Incomplete | None = None, order_by: Incomplete | None = None, page_token: Incomplete | None = None): ...
    def get_experiment(self, experiment_id): ...
    def get_experiment_by_name(self, experiment_name):
        """
        Specialized implementation for SQL backed store.
        """
    def delete_experiment(self, experiment_id) -> None: ...
    def restore_experiment(self, experiment_id) -> None: ...
    def rename_experiment(self, experiment_id, new_name) -> None: ...
    def create_run(self, experiment_id, user_id, start_time, tags, run_name): ...
    def update_run_info(self, run_id, run_status, end_time, run_name): ...
    def get_run(self, run_id): ...
    def restore_run(self, run_id) -> None: ...
    def delete_run(self, run_id) -> None: ...
    def log_metric(self, run_id, metric) -> None: ...
    def get_metric_history(self, run_id, metric_key, max_results: Incomplete | None = None, page_token: Incomplete | None = None):
        """
        Return all logged values for a given metric.

        :param run_id: Unique identifier for run
        :param metric_key: Metric name within the run
        :param max_results: An indicator for paginated results. This functionality is not
            implemented for SQLAlchemyStore and is unused in this store's implementation.
        :param page_token: An indicator for paginated results. This functionality is not
            implemented for SQLAlchemyStore and if the value is overridden with a value other than
            ``None``, an MlflowException will be thrown.

        :return: A List of :py:class:`mlflow.entities.Metric` entities if ``metric_key`` values
            have been logged to the ``run_id``, else an empty list.
        """
    class MetricWithRunId(Metric):
        def __init__(self, metric: Metric, run_id) -> None: ...
        @property
        def run_id(self): ...
        def to_dict(self): ...
    def get_metric_history_bulk(self, run_ids, metric_key, max_results):
        """
        Return all logged values for a given metric.

        :param run_ids: Unique identifiers of the runs from which to fetch the metric histories for
                        the specified key.
        :param metric_key: Metric name within the runs.
        :param max_results: The maximum number of results to return.

        :return: A List of :py:class:`SqlAlchemyStore.MetricWithRunId` objects if ``metric_key``
            values have been logged to one or more of the specified ``run_ids``, else an empty
            list. Results are sorted by run ID in lexicographically ascending order, followed by
            timestamp, step, and value in numerically ascending order.
        """
    def log_param(self, run_id, param) -> None: ...
    def set_experiment_tag(self, experiment_id, tag) -> None:
        """
        Set a tag for the specified experiment

        :param experiment_id: String ID of the experiment
        :param tag: ExperimentRunTag instance to log
        """
    def set_tag(self, run_id, tag) -> None:
        """
        Set a tag on a run.

        :param run_id: String ID of the run
        :param tag: RunTag instance to log
        """
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
