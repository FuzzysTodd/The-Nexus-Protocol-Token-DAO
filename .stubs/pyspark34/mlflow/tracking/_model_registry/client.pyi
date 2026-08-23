from _typeshed import Incomplete
from mlflow.entities.model_registry import ModelVersionTag as ModelVersionTag, RegisteredModelTag as RegisteredModelTag
from mlflow.entities.model_registry.model_version_status import ModelVersionStatus as ModelVersionStatus
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.store.model_registry import SEARCH_MODEL_VERSION_MAX_RESULTS_DEFAULT as SEARCH_MODEL_VERSION_MAX_RESULTS_DEFAULT, SEARCH_REGISTERED_MODEL_MAX_RESULTS_DEFAULT as SEARCH_REGISTERED_MODEL_MAX_RESULTS_DEFAULT
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS, utils as utils

AWAIT_MODEL_VERSION_CREATE_SLEEP_DURATION_SECONDS: int

class ModelRegistryClient:
    """
    Client of an MLflow Model Registry Server that creates and manages registered
    models and model versions.
    """
    registry_uri: Incomplete
    tracking_uri: Incomplete
    def __init__(self, registry_uri, tracking_uri) -> None:
        """
        :param registry_uri: Address of local or remote model registry server.
        :param tracking_uri: Address of local or remote tracking server.
        """
    @property
    def store(self): ...
    def create_registered_model(self, name, tags: Incomplete | None = None, description: Incomplete | None = None):
        """
         Create a new registered model in backend store.

         :param name: Name of the new model. This is expected to be unique in the backend store.
         :param tags: A dictionary of key-value pairs that are converted into
                      :py:class:`mlflow.entities.model_registry.RegisteredModelTag` objects.
        :param description: Description of the model.
         :return: A single object of :py:class:`mlflow.entities.model_registry.RegisteredModel`
                  created by backend.
        """
    def update_registered_model(self, name, description):
        """
        Updates description for RegisteredModel entity.

        Backend raises exception if a registered model with given name does not exist.

        :param name: Name of the registered model to update.
        :param description: New description.
        :return: A single updated :py:class:`mlflow.entities.model_registry.RegisteredModel` object.
        """
    def rename_registered_model(self, name, new_name):
        """
        Update registered model name.

        :param name: Name of the registered model to update.
        :param new_name: New proposed name for the registered model.

        :return: A single updated :py:class:`mlflow.entities.model_registry.RegisteredModel` object.
        """
    def delete_registered_model(self, name) -> None:
        """
        Delete registered model.
        Backend raises exception if a registered model with given name does not exist.

        :param name: Name of the registered model to delete.
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
        :param name: Name of the registered model to get.
        :return: A single :py:class:`mlflow.entities.model_registry.RegisteredModel` object.
        """
    def get_latest_versions(self, name, stages: Incomplete | None = None):
        """
        Latest version models for each requests stage. If no ``stages`` provided, returns the
        latest version for each stage.

        :param name: Name of the registered model from which to get the latest versions.
        :param stages: List of desired stages. If input list is None, return latest versions for
                       for 'Staging' and 'Production' stages.
        :return: List of :py:class:`mlflow.entities.model_registry.ModelVersion` objects.
        """
    def set_registered_model_tag(self, name, key, value) -> None:
        """
        Set a tag for the registered model.

        :param name: Registered model name.
        :param key: Tag key to log.
        :param value: Tag value log.
        :return: None
        """
    def delete_registered_model_tag(self, name, key) -> None:
        """
        Delete a tag associated with the registered model.

        :param name: Registered model name.
        :param key: Registered model tag key.
        :return: None
        """
    def create_model_version(self, name, source, run_id: Incomplete | None = None, tags: Incomplete | None = None, run_link: Incomplete | None = None, description: Incomplete | None = None, await_creation_for=..., local_model_path: Incomplete | None = None):
        """
        Create a new model version from given source.

        :param name: Name of the containing registered model.
        :param source: Source path where the MLflow model is stored.
        :param run_id: Run ID from MLflow tracking server that generated the model.
        :param tags: A dictionary of key-value pairs that are converted into
                     :py:class:`mlflow.entities.model_registry.ModelVersionTag` objects.
        :param run_link: Link to the run from an MLflow tracking server that generated this model.
        :param description: Description of the version.
        :param await_creation_for: Number of seconds to wait for the model version to finish being
                                    created and is in ``READY`` status. By default, the function
                                    waits for five minutes. Specify 0 or None to skip waiting.
        Wait until the model version is finished being created and is in ``READY`` status.
        :return: Single :py:class:`mlflow.entities.model_registry.ModelVersion` object created by
                 backend.
        """
    def update_model_version(self, name, version, description):
        """
        Update metadata associated with a model version in backend.

        :param name: Name of the containing registered model.
        :param version: Version number of the model version.
        :param description: New description.
        """
    def transition_model_version_stage(self, name, version, stage, archive_existing_versions: bool = False):
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
    def get_model_version(self, name, version):
        """
        :param name: Name of the containing registered model.
        :param version: Version number of the model version.
        :return: A single :py:class:`mlflow.entities.model_registry.ModelVersion` object.
        """
    def delete_model_version(self, name, version) -> None:
        """
        Delete model version in backend.

        :param name: Name of the containing registered model.
        :param version: Version number of the model version.
        """
    def get_model_version_download_uri(self, name, version):
        """
        Get the download location in Model Registry for this model version.

        :param name: Name of the containing registered model.
        :param version: Version number of the model version.
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
    def get_model_version_stages(self, name, version):
        """
        :return: A list of valid stages.
        """
    def set_model_version_tag(self, name, version, key, value) -> None:
        """
        Set a tag for the model version.

        :param name: Registered model name.
        :param version: Registered model version.
        :param key: Tag key to log.
        :param value: Tag value to log.
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
