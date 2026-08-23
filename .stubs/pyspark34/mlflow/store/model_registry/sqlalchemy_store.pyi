from _typeshed import Incomplete
from mlflow.entities.model_registry.model_version_stages import ALL_STAGES as ALL_STAGES, DEFAULT_STAGES_FOR_GET_LATEST_VERSIONS as DEFAULT_STAGES_FOR_GET_LATEST_VERSIONS, STAGE_ARCHIVED as STAGE_ARCHIVED, STAGE_DELETED_INTERNAL as STAGE_DELETED_INTERNAL, get_canonical_stage as get_canonical_stage
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE, INVALID_STATE as INVALID_STATE, RESOURCE_ALREADY_EXISTS as RESOURCE_ALREADY_EXISTS, RESOURCE_DOES_NOT_EXIST as RESOURCE_DOES_NOT_EXIST
from mlflow.store.entities.paged_list import PagedList as PagedList
from mlflow.store.model_registry import SEARCH_MODEL_VERSION_MAX_RESULTS_DEFAULT as SEARCH_MODEL_VERSION_MAX_RESULTS_DEFAULT, SEARCH_MODEL_VERSION_MAX_RESULTS_THRESHOLD as SEARCH_MODEL_VERSION_MAX_RESULTS_THRESHOLD, SEARCH_REGISTERED_MODEL_MAX_RESULTS_DEFAULT as SEARCH_REGISTERED_MODEL_MAX_RESULTS_DEFAULT, SEARCH_REGISTERED_MODEL_MAX_RESULTS_THRESHOLD as SEARCH_REGISTERED_MODEL_MAX_RESULTS_THRESHOLD
from mlflow.store.model_registry.abstract_store import AbstractStore as AbstractStore
from mlflow.store.model_registry.dbmodels.models import SqlModelVersion as SqlModelVersion, SqlModelVersionTag as SqlModelVersionTag, SqlRegisteredModel as SqlRegisteredModel, SqlRegisteredModelAlias as SqlRegisteredModelAlias, SqlRegisteredModelTag as SqlRegisteredModelTag
from mlflow.utils.search_utils import SearchModelUtils as SearchModelUtils, SearchModelVersionUtils as SearchModelVersionUtils, SearchUtils as SearchUtils
from mlflow.utils.time_utils import get_current_time_millis as get_current_time_millis
from mlflow.utils.uri import extract_db_type_from_uri as extract_db_type_from_uri

class SqlAlchemyStore(AbstractStore):
    """
    This entity may change or be removed in a future release without warning.
    SQLAlchemy compliant backend store for tracking meta data for MLflow entities. MLflow
    supports the database dialects ``mysql``, ``mssql``, ``sqlite``, and ``postgresql``.
    As specified in the
    `SQLAlchemy docs <https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls>`_ ,
    the database URI is expected in the format
    ``<dialect>+<driver>://<username>:<password>@<host>:<port>/<database>``. If you do not
    specify a driver, SQLAlchemy uses a dialect's default driver.

    This store interacts with SQL store using SQLAlchemy abstractions defined for MLflow entities.
    :py:class:`mlflow.store.model_registry.models.RegisteredModel` and
    :py:class:`mlflow.store.model_registry.models.ModelVersion`
    """
    CREATE_MODEL_VERSION_RETRIES: int
    db_uri: Incomplete
    db_type: Incomplete
    engine: Incomplete
    ManagedSessionMaker: Incomplete
    def __init__(self, db_uri) -> None:
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
    def create_registered_model(self, name, tags: Incomplete | None = None, description: Incomplete | None = None):
        """
        Create a new registered model in backend store.

        :param name: Name of the new model. This is expected to be unique in the backend store.
        :param tags: A list of :py:class:`mlflow.entities.model_registry.RegisteredModelTag`
                     instances associated with this registered model.
        :param description: Description of the version.
        :return: A single object of :py:class:`mlflow.entities.model_registry.RegisteredModel`
                 created in the backend.
        """
    def update_registered_model(self, name, description):
        """
        Update description of the registered model.

        :param name: Registered model name.
        :param description: New description.
        :return: A single updated :py:class:`mlflow.entities.model_registry.RegisteredModel` object.
        """
    def rename_registered_model(self, name, new_name):
        """
        Rename the registered model.

        :param name: Registered model name.
        :param new_name: New proposed name.
        :return: A single updated :py:class:`mlflow.entities.model_registry.RegisteredModel` object.
        """
    def delete_registered_model(self, name) -> None:
        """
        Delete the registered model.
        Backend raises exception if a registered model with given name does not exist.

        :param name: Registered model name.
        :return: None
        """
    def search_registered_models(self, filter_string: Incomplete | None = None, max_results=..., order_by: Incomplete | None = None, page_token: Incomplete | None = None):
        """
        Search for registered models in backend that satisfy the filter criteria.

        :param filter_string: Filter query string, defaults to searching all registered models.
        :param max_results: Maximum number of registered models desired.
        :param order_by: List of column names with ASC|DESC annotation, to be used for ordering
                         matching search results.
        :param page_token: Token specifying the next page of results. It should be obtained from
                            a ``search_registered_models`` call.
        :return: A PagedList of :py:class:`mlflow.entities.model_registry.RegisteredModel` objects
                that satisfy the search expressions. The pagination token for the next page can be
                obtained via the ``token`` attribute of the object.
        """
    def get_registered_model(self, name):
        """
        Get registered model instance by name.

        :param name: Registered model name.
        :return: A single :py:class:`mlflow.entities.model_registry.RegisteredModel` object.
        """
    def get_latest_versions(self, name, stages: Incomplete | None = None):
        """
        Latest version models for each requested stage. If no ``stages`` argument is provided,
        returns the latest version for each stage.

        :param name: Registered model name.
        :param stages: List of desired stages. If input list is None, return latest versions for
                       each stage.
        :return: List of :py:class:`mlflow.entities.model_registry.ModelVersion` objects.
        """
    def set_registered_model_tag(self, name, tag) -> None:
        """
        Set a tag for the registered model.

        :param name: Registered model name.
        :param tag: :py:class:`mlflow.entities.model_registry.RegisteredModelTag` instance to log.
        :return: None
        """
    def delete_registered_model_tag(self, name, key) -> None:
        """
        Delete a tag associated with the registered model.

        :param name: Registered model name.
        :param key: Registered model tag key.
        :return: None
        """
    def create_model_version(self, name, source, run_id: Incomplete | None = None, tags: Incomplete | None = None, run_link: Incomplete | None = None, description: Incomplete | None = None, local_model_path: Incomplete | None = None):
        """
        Create a new model version from given source and run ID.

        :param name: Registered model name.
        :param source: Source path where the MLflow model is stored.
        :param run_id: Run ID from MLflow tracking server that generated the model.
        :param tags: A list of :py:class:`mlflow.entities.model_registry.ModelVersionTag`
                     instances associated with this model version.
        :param run_link: Link to the run from an MLflow tracking server that generated this model.
        :param description: Description of the version.
        :return: A single object of :py:class:`mlflow.entities.model_registry.ModelVersion`
                 created in the backend.
        """
    def update_model_version(self, name, version, description: Incomplete | None = None):
        """
        Update metadata associated with a model version in backend.

        :param name: Registered model name.
        :param version: Registered model version.
        :param description: New model description.
        :return: A single :py:class:`mlflow.entities.model_registry.ModelVersion` object.
        """
    def transition_model_version_stage(self, name, version, stage, archive_existing_versions):
        '''
        Update model version stage.

        :param name: Registered model name.
        :param version: Registered model version.
        :param stage: New desired stage for this model version.
        :param archive_existing_versions: If this flag is set to ``True``, all existing model
            versions in the stage will be automatically moved to the "archived" stage. Only valid
            when ``stage`` is ``"staging"`` or ``"production"`` otherwise an error will be raised.

        :return: A single :py:class:`mlflow.entities.model_registry.ModelVersion` object.
        '''
    def delete_model_version(self, name, version) -> None:
        """
        Delete model version in backend.

        :param name: Registered model name.
        :param version: Registered model version.
        :return: None
        """
    def get_model_version(self, name, version):
        """
        Get the model version instance by name and version.

        :param name: Registered model name.
        :param version: Registered model version.
        :return: A single :py:class:`mlflow.entities.model_registry.ModelVersion` object.
        """
    def get_model_version_download_uri(self, name, version):
        """
        Get the download location in Model Registry for this model version.
        NOTE: For first version of Model Registry, since the models are not copied over to another
              location, download URI points to input source path.

        :param name: Registered model name.
        :param version: Registered model version.
        :return: A single URI location that allows reads for downloading.
        """
    def search_model_versions(self, filter_string: Incomplete | None = None, max_results=..., order_by: Incomplete | None = None, page_token: Incomplete | None = None):
        """
        Search for model versions in backend that satisfy the filter criteria.

        :param filter_string: A filter string expression. Currently supports a single filter
                              condition either name of model like ``name = 'model_name'`` or
                              ``run_id = '...'``.
        :param max_results: Maximum number of model versions desired.
        :param order_by: List of column names with ASC|DESC annotation, to be used for ordering
                         matching search results.
        :param page_token: Token specifying the next page of results. It should be obtained from
                            a ``search_model_versions`` call.
        :return: A PagedList of :py:class:`mlflow.entities.model_registry.ModelVersion`
                 objects that satisfy the search expressions. The pagination token for the next
                 page can be obtained via the ``token`` attribute of the object.
        """
    def set_model_version_tag(self, name, version, tag) -> None:
        """
        Set a tag for the model version.

        :param name: Registered model name.
        :param version: Registered model version.
        :param tag: :py:class:`mlflow.entities.model_registry.ModelVersionTag` instance to log.
        :return: None
        """
    def delete_model_version_tag(self, name, version, key) -> None:
        """
        Delete a tag associated with the model version.

        :param name: Registered model name.
        :param version: Registered model version.
        :param key: Tag key.
        :return: None
        """
    def set_registered_model_alias(self, name, alias, version) -> None:
        """
        Set a registered model alias pointing to a model version.

        :param name: Registered model name.
        :param alias: Name of the alias.
        :param version: Registered model version number.
        :return: None
        """
    def delete_registered_model_alias(self, name, alias) -> None:
        """
        Delete an alias associated with a registered model.

        :param name: Registered model name.
        :param alias: Name of the alias.
        :return: None
        """
    def get_model_version_by_alias(self, name, alias):
        """
        Get the model version instance by name and alias.

        :param name: Registered model name.
        :param alias: Name of the alias.
        :return: A single :py:class:`mlflow.entities.model_registry.ModelVersion` object.
        """
