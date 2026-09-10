from _typeshed import Incomplete
from enum import Enum
from mlflow import pyfunc as pyfunc
from mlflow.environment_variables import MLFLOW_OPENAI_SECRET_SCOPE as MLFLOW_OPENAI_SECRET_SCOPE
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.types import ColSpec as ColSpec, Schema as Schema, TensorSpec as TensorSpec
from mlflow.utils.annotations import experimental as experimental
from mlflow.utils.databricks_utils import check_databricks_secret_scope_access as check_databricks_secret_scope_access, is_in_databricks_runtime as is_in_databricks_runtime
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import write_to as write_to
from typing import Any, Dict

FLAVOR_NAME: str
MODEL_FILENAME: str

def get_default_pip_requirements():
    """
    :return: A list of default pip requirements for MLflow Models produced by this flavor.
             Calls to :func:`save_model()` and :func:`log_model()` produce a pip environment
             that, at minimum, contains these requirements.
    """
def get_default_conda_env():
    """
    :return: The default Conda environment for MLflow Models produced by calls to
             :func:`save_model()` and :func:`log_model()`.
    """

class _OpenAIEnvVar(str, Enum):
    OPENAI_API_TYPE: str
    OPENAI_API_BASE: str
    OPENAI_API_KEY: str
    OPENAI_API_KEY_PATH: str
    OPENAI_ORGANIZATION: str
    @property
    def secret_key(self): ...
    @classmethod
    def read_environ(cls): ...

def save_model(model, task, path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, mlflow_model: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, **kwargs):
    '''
    Save an OpenAI model to a path on the local file system.

    :param model: The OpenAI model name or reference instance, e.g.,
                  ``openai.Model.retrieve("gpt-3.5-turbo")``.
    :param task: The task the model is performing, e.g., ``openai.ChatCompletion`` or
                 ``\'chat.completions\'``.
    :param path: Local path where the model is to be saved.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param mlflow_model: :py:mod:`mlflow.models.Model` this flavor is being added to.

    :param signature: :py:class:`ModelSignature <mlflow.models.ModelSignature>`
                      describes model input and output :py:class:`Schema <mlflow.types.Schema>`.
                      The model signature can be :py:func:`inferred <mlflow.models.infer_signature>`
                      from datasets with valid model input (e.g. the training dataset with target
                      column omitted) and valid model output (e.g. model predictions generated on
                      the training dataset), for example:

                      .. code-block:: python

                        from mlflow.models import infer_signature

                        train = df.drop_column("target_label")
                        predictions = ...  # compute model predictions
                        signature = infer_signature(train, predictions)
    :param input_example: Input example provides one or several instances of valid
                          model input. The example can be used as a hint of what data to feed the
                          model. The given example will be converted to a Pandas DataFrame and then
                          serialized to json using the Pandas split-oriented format. Bytes are
                          base64-encoded.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :param  kwargs:
        Keyword arguments specific to the OpenAI task, such as the ``messages`` (see
        :ref:`mlflow.openai.messages` for more details on this parameter)
        or ``top_p`` value to use for chat completion.

    .. code-block:: python

        import mlflow
        import openai

        # Chat
        mlflow.openai.save_model(
            model="gpt-3.5-turbo",
            task=openai.ChatCompletion,
            messages=[{"role": "user", "content": "Tell me a joke."}],
            path="model",
        )

        # Embeddings
        mlflow.openai.save_model(
            model="text-embedding-ada-002",
            task=openai.Embedding,
            path="model",
        )
    '''
def log_model(model, task, artifact_path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, await_registration_for=..., pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, **kwargs):
    '''
    Log an OpenAI model as an MLflow artifact for the current run.

    :param model: The OpenAI model name or reference instance, e.g.,
                  ``openai.Model.retrieve("gpt-3.5-turbo")``.
    :param task: The task the model is performing, e.g., ``openai.ChatCompletion`` or
                 ``\'chat.completions\'``.
    :param artifact_path: Run-relative artifact path.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param registered_model_name: If given, create a model version under
                                  ``registered_model_name``, also creating a registered model if one
                                  with the given name does not exist.

    :param signature: :py:class:`ModelSignature <mlflow.models.ModelSignature>`
                      describes model input and output :py:class:`Schema <mlflow.types.Schema>`.
                      The model signature can be :py:func:`inferred <mlflow.models.infer_signature>`
                      from datasets with valid model input (e.g. the training dataset with target
                      column omitted) and valid model output (e.g. model predictions generated on
                      the training dataset), for example:

                      .. code-block:: python

                        from mlflow.models import infer_signature

                        train = df.drop_column("target_label")
                        predictions = ...  # compute model predictions
                        signature = infer_signature(train, predictions)
    :param input_example: Input example provides one or several instances of valid
                          model input. The example can be used as a hint of what data to feed the
                          model. The given example will be converted to a Pandas DataFrame and then
                          serialized to json using the Pandas split-oriented format. Bytes are
                          base64-encoded.
    :param await_registration_for: Number of seconds to wait for the model version to finish
                            being created and is in ``READY`` status. By default, the function
                            waits for five minutes. Specify 0 or None to skip waiting.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :param  kwargs:
        Keyword arguments specific to the OpenAI task, such as the ``messages`` (see
        :ref:`mlflow.openai.messages` for more details on this parameter)
        or ``top_p`` value to use for chat completion.
    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.

    .. code-block:: python

        import mlflow
        import openai

        # Chat
        with mlflow.start_run():
            info = mlflow.openai.log_model(
                model="gpt-3.5-turbo",
                task=openai.ChatCompletion,
                messages=[{"role": "user", "content": "Tell me a joke about {animal}."}],
                artifact_path="model",
            )
            model = mlflow.pyfunc.load_model(info.model_uri)
            df = pd.DataFrame({"animal": ["cats", "dogs"]})
            print(model.predict(df))

        # Embeddings
        with mlflow.start_run():
            info = mlflow.openai.log_model(
                model="text-embedding-ada-002",
                task=openai.Embedding,
                artifact_path="embeddings",
            )
            model = mlflow.pyfunc.load_model(info.model_uri)
            print(model.predict(["hello", "world"]))

    '''

class _FormattableMessage:
    content: Incomplete
    role: Incomplete
    variables: Incomplete
    def __init__(self, message) -> None: ...
    def format(self, **params): ...

class _OpenAIWrapper:
    model: Incomplete
    task: Incomplete
    messages: Incomplete
    variables: Incomplete
    formattable_messages: Incomplete
    def __init__(self, model) -> None: ...
    def format_messages(self, params_list): ...
    def get_params_list(self, data): ...
    def predict(self, data, params: Dict[str, Any] | None = None):
        """
        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """

class _TestOpenAIWrapper(_OpenAIWrapper):
    """
    A wrapper class that should be used for testing purposes only.
    """
    def predict(self, data, params: Dict[str, Any] | None = None):
        """
        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """

def load_model(model_uri, dst_path: Incomplete | None = None):
    """
    Load an OpenAI model from a local file or a run.

    :param model_uri: The location, in URI format, of the MLflow model. For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/tracking.html#
                      artifact-locations>`_.
    :param dst_path: The local filesystem path to which to download the model artifact.
                     This directory must already exist. If unspecified, a local output
                     path will be created.

    :return: A dictionary representing the OpenAI model.
    """
