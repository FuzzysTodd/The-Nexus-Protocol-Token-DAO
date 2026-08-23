import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from mlflow.entities import DatasetInput as DatasetInput, ViewType as ViewType
from mlflow.store.entities.paged_list import PagedList as PagedList
from mlflow.store.tracking import SEARCH_MAX_RESULTS_DEFAULT as SEARCH_MAX_RESULTS_DEFAULT
from mlflow.utils.annotations import developer_stable as developer_stable, experimental as experimental
from typing import List

class AbstractStore(metaclass=abc.ABCMeta):
    """
    Abstract class for Backend Storage.
    This class defines the API interface for front ends to connect with various types of backends.
    """
    __metaclass__ = ABCMeta
    def __init__(self) -> None:
        """
        Empty constructor for now. This is deliberately not marked as abstract, else every
        derived class would be forced to create one.
        """
    @abstractmethod
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
    @abstractmethod
    def create_experiment(self, name, artifact_location, tags):
        """
        Create a new experiment.
        If an experiment with the given name already exists, throws exception.

        :param name: Desired name for an experiment
        :param artifact_location: Base location for artifacts in runs. May be None.
        :param tags: Experiment tags to set upon experiment creation

        :return: experiment_id (string) for the newly created experiment if successful, else None.
        """
    @abstractmethod
    def get_experiment(self, experiment_id):
        """
        Fetch the experiment by ID from the backend store.

        :param experiment_id: String id for the experiment

        :return: A single :py:class:`mlflow.entities.Experiment` object if it exists,
            otherwise raises an exception.

        """
    def get_experiment_by_name(self, experiment_name) -> None:
        """
        Fetch the experiment by name from the backend store.

        :param experiment_name: Name of experiment

        :return: A single :py:class:`mlflow.entities.Experiment` object if it exists.
        """
    @abstractmethod
    def delete_experiment(self, experiment_id):
        """
        Delete the experiment from the backend store. Deleted experiments can be restored until
        permanently deleted.

        :param experiment_id: String id for the experiment
        """
    @abstractmethod
    def restore_experiment(self, experiment_id):
        """
        Restore deleted experiment unless it is permanently deleted.

        :param experiment_id: String id for the experiment
        """
    @abstractmethod
    def rename_experiment(self, experiment_id, new_name):
        """
        Update an experiment's name. The new name must be unique.

        :param experiment_id: String id for the experiment
        """
    @abstractmethod
    def get_run(self, run_id):
        """
        Fetch the run from backend store. The resulting :py:class:`Run <mlflow.entities.Run>`
        contains a collection of run metadata - :py:class:`RunInfo <mlflow.entities.RunInfo>`,
        as well as a collection of run parameters, tags, and metrics -
        :py:class`RunData <mlflow.entities.RunData>`. In the case where multiple metrics with the
        same key are logged for the run, the :py:class:`RunData <mlflow.entities.RunData>` contains
        the value at the latest timestamp for each metric. If there are multiple values with the
        latest timestamp for a given metric, the maximum of these values is returned.

        :param run_id: Unique identifier for the run.

        :return: A single :py:class:`mlflow.entities.Run` object, if the run exists. Otherwise,
                 raises an exception.
        """
    @abstractmethod
    def update_run_info(self, run_id, run_status, end_time, run_name):
        """
        Update the metadata of the specified run.

        :return: :py:class:`mlflow.entities.RunInfo` describing the updated run.
        """
    @abstractmethod
    def create_run(self, experiment_id, user_id, start_time, tags, run_name):
        '''
        Create a run under the specified experiment ID, setting the run\'s status to "RUNNING"
        and the start time to the current time.

        :param experiment_id: String id of the experiment for this run
        :param user_id: ID of the user launching this run

        :return: The created Run object
        '''
    @abstractmethod
    def delete_run(self, run_id):
        """
        Delete a run.

        :param run_id
        """
    @abstractmethod
    def restore_run(self, run_id):
        """
        Restore a run.

        :param run_id
        """
    def log_metric(self, run_id, metric) -> None:
        """
        Log a metric for the specified run

        :param run_id: String id for the run
        :param metric: :py:class:`mlflow.entities.Metric` instance to log
        """
    def log_param(self, run_id, param) -> None:
        """
        Log a param for the specified run

        :param run_id: String id for the run
        :param param: :py:class:`mlflow.entities.Param` instance to log
        """
    def set_experiment_tag(self, experiment_id, tag) -> None:
        """
        Set a tag for the specified experiment

        :param experiment_id: String id for the experiment
        :param tag: :py:class:`mlflow.entities.ExperimentTag` instance to set
        """
    def set_tag(self, run_id, tag) -> None:
        """
        Set a tag for the specified run

        :param run_id: String id for the run
        :param tag: :py:class:`mlflow.entities.RunTag` instance to set
        """
    @abstractmethod
    def get_metric_history(self, run_id, metric_key, max_results: Incomplete | None = None, page_token: Incomplete | None = None):
        """
        Return a list of metric objects corresponding to all values logged for a given metric
        within a run.

        :param run_id: Unique identifier for run
        :param metric_key: Metric name within the run
        :param max_results: Maximum number of metric history events (steps) to return per paged
            query.
        :param page_token: A Token specifying the next paginated set of results of metric history.
            This value is obtained as a return value from a paginated call to GetMetricHistory.

        :return: A list of :py:class:`mlflow.entities.Metric` entities if logged, else empty list
        """
    def search_runs(self, experiment_ids, filter_string, run_view_type, max_results=..., order_by: Incomplete | None = None, page_token: Incomplete | None = None):
        """
        Return runs that match the given list of search expressions within the experiments.

        :param experiment_ids: List of experiment ids to scope the search
        :param filter_string: A search filter string.
        :param run_view_type: ACTIVE_ONLY, DELETED_ONLY, or ALL runs
        :param max_results: Maximum number of runs desired.
        :param order_by: List of order_by clauses.
        :param page_token: Token specifying the next page of results. It should be obtained from
            a ``search_runs`` call.

        :return: A :py:class:`PagedList <mlflow.store.entities.PagedList>` of
            :py:class:`Run <mlflow.entities.Run>` objects that satisfy the search expressions.
            If the underlying tracking store supports pagination, the token for the next page may
            be obtained via the ``token`` attribute of the returned object; however, some store
            implementations may not support pagination and thus the returned token would not be
            meaningful in such cases.
        """
    @abstractmethod
    def log_batch(self, run_id, metrics, params, tags):
        """
        Log multiple metrics, params, and tags for the specified run

        :param run_id: String id for the run
        :param metrics: List of :py:class:`mlflow.entities.Metric` instances to log
        :param params: List of :py:class:`mlflow.entities.Param` instances to log
        :param tags: List of :py:class:`mlflow.entities.RunTag` instances to log

        :return: None.
        """
    @abstractmethod
    def record_logged_model(self, run_id, mlflow_model):
        """
        Record logged model information with tracking store. The list of logged model infos is
        maintained in a mlflow.models tag in JSON format.

        Note: The actual models are logged as artifacts via artifact repository.

        :param run_id: String id for the run
        :param mlflow_model: Model object to be recorded.

        The default implementation is a no-op.

        :return: None.
        """
    @abstractmethod
    def log_inputs(self, run_id: str, datasets: List[DatasetInput] | None = None):
        """
        Log inputs, such as datasets, to the specified run.

        :param run_id: String id for the run
        :param datasets: List of :py:class:`mlflow.entities.DatasetInput` instances to log
                         as inputs to the run.

        :return: None.
        """
