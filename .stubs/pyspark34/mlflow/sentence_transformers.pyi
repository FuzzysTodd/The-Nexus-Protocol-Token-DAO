from _typeshed import Incomplete
from mlflow import pyfunc as pyfunc
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature, infer_pip_requirements as infer_pip_requirements
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.types.schema import ColSpec as ColSpec, Schema as Schema, TensorSpec as TensorSpec
from mlflow.utils.annotations import experimental as experimental
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, docstring_version_compatibility_warning as docstring_version_compatibility_warning, format_docstring as format_docstring
from mlflow.utils.file_utils import write_to as write_to
from typing import Any, Dict, List

FLAVOR_NAME: str
SENTENCE_TRANSFORMERS_DATA_PATH: str

def get_default_pip_requirements() -> List[str]:
    """
    Retrieves the set of minimal dependencies for the ``sentence_transformers`` flavor.

    :return: A list of default pip requirements for MLflow Models that have been produced with the
             ``sentence-transformers`` flavor. Calls to :py:func:`save_model()` and
             :py:func:`log_model()` produce a pip environment that contain these
             requirements at a minimum.
    """
def get_default_conda_env():
    """
    :return: The default Conda environment for MLflow Models produced with the
             ``sentence_transformers`` flavor.
    """
def save_model(model, path: str, inference_config: Dict[str, Any] | None = None, code_paths: List[str] | None = None, mlflow_model: Model | None = None, signature: ModelSignature | None = None, input_example: ModelInputExample | None = None, pip_requirements: List[str] | str | None = None, extra_pip_requirements: List[str] | str | None = None, conda_env: Incomplete | None = None, metadata: Dict[str, Any] = None) -> None:
    """
    Save a trained ``sentence-transformers`` model to a path on the local file system.

    :param model: A trained ``sentence-transformers`` model.
    :param path: Local path destination for the serialized model to be saved.
    :param inference_config:
        A dict of valid inference parameters that can be applied to a ``sentence-transformer``
        model instance during inference.
        These arguments are used exclusively for the case of loading the model as a ``pyfunc``
        Model or for use in Spark.
        These values are not applied to a returned model from a call to
        ``mlflow.sentence_transformers.load_model()``
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param mlflow_model: An MLflow model object that specifies the flavor that this model is being
                         added to.
    :param signature: an instance of the :py:class:`ModelSignature <mlflow.models.ModelSignature>`
                      class that describes the model's inputs and outputs. If not specified but an
                      ``input_example`` is supplied, a signature will be automatically inferred
                      based on the supplied input example and model. If both ``signature`` and
                      ``input_example`` are not specified or the automatic signature inference
                      fails, a default signature will be adopted. To prevent a signature from being
                      adopted, set ``signature`` to ``False``. To manually infer a model signature,
                      call :py:func:`infer_signature() <mlflow.models.infer_signature>` on datasets
                      with valid model inputs and valid model outputs.
    :param input_example: {{ input_example }}
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param conda_env: {{ conda_env }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.

    :return: None
    """
def log_model(model, artifact_path: str, inference_config: Dict[str, Any] | None = None, code_paths: List[str] | None = None, registered_model_name: str = None, signature: ModelSignature | None = None, input_example: ModelInputExample | None = None, await_registration_for=..., pip_requirements: List[str] | str | None = None, extra_pip_requirements: List[str] | str | None = None, conda_env: Incomplete | None = None, metadata: Dict[str, Any] = None):
    """
    Log a ``sentence_transformers`` model as an MLflow artifact for the current run.

    :param model: A trained ``sentence-transformers`` model.
    :param artifact_path: Local path destination for the serialized model to be saved.
    :param inference_config:
        A dict of valid overrides that can be applied to a ``sentence-transformer`` model instance
        during inference.
        These arguments are used exclusively for the case of loading the model as a ``pyfunc``
        Model or for use in Spark.
        These values are not applied to a returned model from a call to
        ``mlflow.sentence_transformers.load_model()``
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param registered_model_name: This argument may change or be removed in a
                                  future release without warning. If given, create a model
                                  version under ``registered_model_name``, also creating a
                                  registered model if one with the given name does not exist.
    :param signature: an instance of the :py:class:`ModelSignature <mlflow.models.ModelSignature>`
                      class that describes the model's inputs and outputs. If not specified but an
                      ``input_example`` is supplied, a signature will be automatically inferred
                      based on the supplied input example and model. If both ``signature`` and
                      ``input_example`` are not specified or the automatic signature inference
                      fails, a default signature will be adopted. To prevent a signature from being
                      adopted, set ``signature`` to ``False``. To manually infer a model signature,
                      call :py:func:`infer_signature() <mlflow.models.infer_signature>` on datasets
                      with valid model inputs and valid model outputs.
    :param input_example: {{ input_example }}
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param conda_env: {{ conda_env }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.

    """
def load_model(model_uri: str, dst_path: str = None):
    """
    Load a ``sentence_transformers`` object from a local file or a run.

    :param model_uri: The location, in URI format, of the MLflow model. For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``mlflow-artifacts:/path/to/model``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/tracking.html#
                      artifact-locations>`_.
    :param dst_path: The local filesystem path to utilize for downloading the model artifact.
                     This directory must already exist if provided. If unspecified, a local output
                     path will be created.
    :return: A ``sentence_transformers`` model instance
    """

class _SentenceTransformerModelWrapper:
    model: Incomplete
    def __init__(self, model) -> None: ...
    def predict(self, sentences, params: Dict[str, Any] | None = None):
        """
        :param sentences: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """
