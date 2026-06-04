from _typeshed import Incomplete
from mlflow.entities import Run as Run
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_uc_registry_messages_pb2 import CreateModelVersionRequest as CreateModelVersionRequest, CreateModelVersionResponse as CreateModelVersionResponse, CreateRegisteredModelRequest as CreateRegisteredModelRequest, CreateRegisteredModelResponse as CreateRegisteredModelResponse, DeleteModelVersionRequest as DeleteModelVersionRequest, DeleteModelVersionResponse as DeleteModelVersionResponse, DeleteModelVersionTagRequest as DeleteModelVersionTagRequest, DeleteModelVersionTagResponse as DeleteModelVersionTagResponse, DeleteRegisteredModelAliasRequest as DeleteRegisteredModelAliasRequest, DeleteRegisteredModelAliasResponse as DeleteRegisteredModelAliasResponse, DeleteRegisteredModelRequest as DeleteRegisteredModelRequest, DeleteRegisteredModelResponse as DeleteRegisteredModelResponse, DeleteRegisteredModelTagRequest as DeleteRegisteredModelTagRequest, DeleteRegisteredModelTagResponse as DeleteRegisteredModelTagResponse, Entity as Entity, FinalizeModelVersionRequest as FinalizeModelVersionRequest, FinalizeModelVersionResponse as FinalizeModelVersionResponse, GenerateTemporaryModelVersionCredentialsRequest as GenerateTemporaryModelVersionCredentialsRequest, GenerateTemporaryModelVersionCredentialsResponse as GenerateTemporaryModelVersionCredentialsResponse, GetModelVersionByAliasRequest as GetModelVersionByAliasRequest, GetModelVersionByAliasResponse as GetModelVersionByAliasResponse, GetModelVersionDownloadUriRequest as GetModelVersionDownloadUriRequest, GetModelVersionDownloadUriResponse as GetModelVersionDownloadUriResponse, GetModelVersionRequest as GetModelVersionRequest, GetModelVersionResponse as GetModelVersionResponse, GetRegisteredModelRequest as GetRegisteredModelRequest, GetRegisteredModelResponse as GetRegisteredModelResponse, Job as Job, LineageHeaderInfo as LineageHeaderInfo, MODEL_VERSION_OPERATION_READ_WRITE as MODEL_VERSION_OPERATION_READ_WRITE, Notebook as Notebook, SearchModelVersionsRequest as SearchModelVersionsRequest, SearchModelVersionsResponse as SearchModelVersionsResponse, SearchRegisteredModelsRequest as SearchRegisteredModelsRequest, SearchRegisteredModelsResponse as SearchRegisteredModelsResponse, SetModelVersionTagRequest as SetModelVersionTagRequest, SetModelVersionTagResponse as SetModelVersionTagResponse, SetRegisteredModelAliasRequest as SetRegisteredModelAliasRequest, SetRegisteredModelAliasResponse as SetRegisteredModelAliasResponse, SetRegisteredModelTagRequest as SetRegisteredModelTagRequest, SetRegisteredModelTagResponse as SetRegisteredModelTagResponse, TemporaryCredentials as TemporaryCredentials, UpdateModelVersionRequest as UpdateModelVersionRequest, UpdateModelVersionResponse as UpdateModelVersionResponse, UpdateRegisteredModelRequest as UpdateRegisteredModelRequest, UpdateRegisteredModelResponse as UpdateRegisteredModelResponse
from mlflow.protos.databricks_uc_registry_service_pb2 import UcModelRegistryService as UcModelRegistryService
from mlflow.protos.service_pb2 import GetRun as GetRun, MlflowService as MlflowService
from mlflow.store._unity_catalog.registry.utils import get_artifact_repo_from_storage_info as get_artifact_repo_from_storage_info, get_full_name_from_sc as get_full_name_from_sc, model_version_from_uc_proto as model_version_from_uc_proto, registered_model_from_uc_proto as registered_model_from_uc_proto, uc_model_version_tag_from_mlflow_tags as uc_model_version_tag_from_mlflow_tags, uc_registered_model_tag_from_mlflow_tags as uc_registered_model_tag_from_mlflow_tags
from mlflow.store.entities.paged_list import PagedList as PagedList
from mlflow.store.model_registry.rest_store import BaseRestStore as BaseRestStore
from mlflow.utils.annotations import experimental as experimental
from mlflow.utils.databricks_utils import get_databricks_host_creds as get_databricks_host_creds, is_databricks_uri as is_databricks_uri
from mlflow.utils.mlflow_tags import MLFLOW_DATABRICKS_JOB_ID as MLFLOW_DATABRICKS_JOB_ID, MLFLOW_DATABRICKS_JOB_RUN_ID as MLFLOW_DATABRICKS_JOB_RUN_ID, MLFLOW_DATABRICKS_NOTEBOOK_ID as MLFLOW_DATABRICKS_NOTEBOOK_ID
from mlflow.utils.proto_json_utils import message_to_json as message_to_json, parse_dict as parse_dict
from mlflow.utils.rest_utils import extract_all_api_info_for_service as extract_all_api_info_for_service, extract_api_info_for_service as extract_api_info_for_service, http_request as http_request, verify_rest_response as verify_rest_response

def get_feature_dependencies(model_dir):
    '''
    Gets the features which a model depends on. This functionality is only implemented on
    Databricks. In OSS mlflow, the dependencies are always empty ("").
    '''

class UcModelRegistryStore(BaseRestStore):
    """
    Client for a remote model registry server accessed via REST API calls

    :param store_uri: URI with scheme 'databricks-uc'
    :param tracking_uri: URI of the Databricks MLflow tracking server from which to fetch
                         run info and download run artifacts, when creating new model
                         versions from source artifacts logged to an MLflow run.
    """
    tracking_uri: Incomplete
    get_tracking_host_creds: Incomplete
    spark: Incomplete
    def __init__(self, store_uri, tracking_uri) -> None: ...
    def create_registered_model(self, name, tags: Incomplete | None = None, description: Incomplete | None = None):
        """
        Create a new registered model in backend store.

        :param name: Name of the new model. This is expected to be unique in the backend store.
        :param tags: A list of :py:class:`mlflow.entities.model_registry.RegisteredModelTag`
                     instances associated with this registered model.
        :param description: Description of the model.
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
    def rename_registered_model(self, name, new_name) -> None:
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
    def search_registered_models(self, filter_string: Incomplete | None = None, max_results: Incomplete | None = None, order_by: Incomplete | None = None, page_token: Incomplete | None = None):
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
    def get_latest_versions(self, name, stages: Incomplete | None = None) -> None:
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
    def transition_model_version_stage(self, name, version, stage, archive_existing_versions) -> None:
        '''
        Update model version stage.

        :param name: Registered model name.
        :param version: Registered model version.
        :param stage: New desired stage for this model version.
        :param archive_existing_versions: If this flag is set to ``True``, all existing model
            versions in the stage will be automatically moved to the "archived" stage. Only valid
            when ``stage`` is ``"staging"`` or ``"production"`` otherwise an error will be raised.

        '''
    def update_model_version(self, name, version, description):
        """
        Update metadata associated with a model version in backend.

        :param name: Registered model name.
        :param version: Registered model version.
        :param description: New model description.
        :return: A single :py:class:`mlflow.entities.model_registry.ModelVersion` object.
        """
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
    def search_model_versions(self, filter_string: Incomplete | None = None, max_results: Incomplete | None = None, order_by: Incomplete | None = None, page_token: Incomplete | None = None):
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
        """
    def delete_model_version_tag(self, name, version, key) -> None:
        """
        Delete a tag associated with the model version.

        :param name: Registered model name.
        :param version: Registered model version.
        :param key: Tag key.
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
