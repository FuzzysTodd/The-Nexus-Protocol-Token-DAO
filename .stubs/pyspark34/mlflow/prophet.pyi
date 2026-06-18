from _typeshed import Incomplete
from mlflow import pyfunc as pyfunc
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import write_to as write_to
from typing import Any, Dict

FLAVOR_NAME: str

def get_default_pip_requirements():
    """
    :return: A list of default pip requirements for MLflow Models produced by this flavor.
             Calls to :func:`save_model()` and :func:`log_model()` produce a pip environment
             that, at a minimum, contains these requirements.
    """
def get_default_conda_env():
    """
    :return: The default Conda environment for MLflow Models produced by calls to
             :func:`save_model()` and :func:`log_model()`.
    """
def save_model(pr_model, path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, mlflow_model: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None):
    """
    Save a Prophet model to a path on the local file system.

    :param pr_model: Prophet model (an instance of Prophet() forecaster that has been fit
                     on a temporal series.
    :param path: Local path where the serialized model (as JSON) is to be saved.
    :param conda_env: {{ conda_env }}
    :param code_paths: A list of local filesystem paths to Python file dependencies (or directories
                       containing file dependencies). These files are *prepended* to the system
                       path when the model is loaded.
    :param mlflow_model: :py:mod:`mlflow.models.Model` this flavor is being added to.
    :param signature: an instance of the :py:class:`ModelSignature <mlflow.models.ModelSignature>`
                      class that describes the model's inputs and outputs. If not specified but an
                      ``input_example`` is supplied, a signature will be automatically inferred
                      based on the supplied input example and model. To disable automatic signature
                      inference when providing an input example, set ``signature`` to ``False``.
                      To manually infer a model signature, call
                      :py:func:`infer_signature() <mlflow.models.infer_signature>` on datasets
                      with valid model inputs, such as a training dataset with the target column
                      omitted, and valid model outputs, like model predictions made on the training
                      dataset, for example:

                      .. code-block:: python

                        from mlflow.models import infer_signature

                        model = Prophet().fit(df)
                        train = model.history
                        predictions = model.predict(model.make_future_dataframe(30))
                        signature = infer_signature(train, predictions)
    :param input_example: {{ input_example }}
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    """
def log_model(pr_model, artifact_path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, await_registration_for=..., pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None):
    """
    Log a Prophet model as an MLflow artifact for the current run.

    :param pr_model: Prophet model to be saved.
    :param artifact_path: Run-relative artifact path.
    :param conda_env: {{ conda_env }}
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
                      based on the supplied input example and model. To disable automatic signature
                      inference when providing an input example, set ``signature`` to ``False``.
                      To manually infer a model signature, call
                      :py:func:`infer_signature() <mlflow.models.infer_signature>` on datasets
                      with valid model inputs, such as a training dataset with the target column
                      omitted, and valid model outputs, like model predictions made on the training
                      dataset, for example:

                      .. code-block:: python

                        from mlflow.models import infer_signature

                        model = Prophet().fit(df)
                        train = model.history
                        predictions = model.predict(model.make_future_dataframe(30))
                        signature = infer_signature(train, predictions)

    :param input_example: {{ input_example }}
    :param await_registration_for: Number of seconds to wait for the model version
                        to finish being created and is in ``READY`` status.
                        By default, the function waits for five minutes.
                        Specify 0 or None to skip waiting.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.
    """
def load_model(model_uri, dst_path: Incomplete | None = None):
    """
    Load a Prophet model from a local file or a run.

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

    :return: A Prophet model instance
    """

class _ProphetModelWrapper:
    pr_model: Incomplete
    def __init__(self, pr_model) -> None: ...
    def predict(self, dataframe, params: Dict[str, Any] | None = None):
        """
        :param dataframe: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """
