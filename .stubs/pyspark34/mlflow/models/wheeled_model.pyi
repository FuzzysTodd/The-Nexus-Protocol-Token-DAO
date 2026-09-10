from _typeshed import Incomplete
from mlflow import MlflowClient as MlflowClient
from mlflow.environment_variables import MLFLOW_WHEELED_MODEL_PIP_DOWNLOAD_OPTIONS as MLFLOW_WHEELED_MODEL_PIP_DOWNLOAD_OPTIONS
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import BAD_REQUEST as BAD_REQUEST
from mlflow.pyfunc.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME, Model as Model
from mlflow.store.artifact.utils.models import get_model_name_and_version as get_model_name_and_version
from mlflow.utils.annotations import experimental as experimental
from mlflow.utils.uri import get_databricks_profile_uri_from_artifact_uri as get_databricks_profile_uri_from_artifact_uri

class WheeledModel:
    """
    Helper class to create a model with added dependency wheels from an existing registered model.
    The `wheeled` model contains all the model dependencies as wheels stored as model artifacts.
    .. note::
        This utility only operates on a model that has been registered to the Model Registry.
    """
    def __init__(self, model_uri) -> None: ...
    @classmethod
    def log_model(cls, model_uri, registered_model_name: Incomplete | None = None):
        """
        Logs a registered model as an MLflow artifact for the current run. This only operates on
        a model which has been registered to the Model Registry. Given a registered model_uri (
        e.g. models:/<model_name>/<model_version>), this utility re-logs the model along with all
        the required model libraries back to the Model Registry. The required model libraries are
        stored along with the model as model artifacts. In addition, supporting files to the
        model (e.g. conda.yaml, requirements.txt) are modified to use the added libraries.

        By default, this utility creates a new model version under the same registered model
        specified by ``model_uri``. This behavior can be overridden by specifying the
        ``registered_model_name`` argument.

        :param model_uri: A registered model uri in the Model Registry of the form
                          models:/<model_name>/<model_version/stage/latest>
        :param registered_model_name: The new model version (model with its libraries) is
                                      registered under the inputted registered_model_name. If None,
                                      a new version is logged to the existing model in the Model
                                      Registry.

        .. code-block:: python
            :caption: Example

            # Given a model uri, log the wheeled model
            with mlflow.start_run():
                WheeledModel.log_model(model_uri)
        """
    def save_model(self, path, mlflow_model: Incomplete | None = None):
        """
        Given an existing registered model, saves the model along with it's dependencies stored as
        wheels to a path on the local file system.

        This does not modify existing model behavior or existing model flavors. It simply downloads
        the model dependencies as wheels and modifies the requirements.txt and conda.yaml file to
        point to the downloaded wheels.

        The download_command defaults to downloading only binary packages using the
        `--only-binary=:all:` option. This behavior can be overridden using an environment
        variable `MLFLOW_WHEELED_MODEL_PIP_DOWNLOAD_OPTIONS`, which will allows setting
        different options such as `--prefer-binary`, `--no-binary`, etc.
        :param path: Local path where the model is to be saved.
        :param mlflow_model: The new :py:mod:`mlflow.models.Model` metadata file to store the
                             updated model metadata.
        """
    @classmethod
    def get_wheel_artifact_path(cls, original_artifact_path): ...
