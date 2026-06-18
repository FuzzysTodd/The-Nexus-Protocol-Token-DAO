from _typeshed import Incomplete
from mlflow import pyfunc as pyfunc
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models import Model as Model, ModelInputExample as ModelInputExample, ModelSignature as ModelSignature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.tracking._model_registry import DEFAULT_AWAIT_MAX_SLEEP_SECONDS as DEFAULT_AWAIT_MAX_SLEEP_SECONDS
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import write_to as write_to
from typing import Any, Dict

FLAVOR_NAME: str
ONNX_EXECUTION_PROVIDERS: Incomplete

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
def save_model(onnx_model, path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, mlflow_model: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, onnx_execution_providers: Incomplete | None = None, onnx_session_options: Incomplete | None = None, metadata: Incomplete | None = None):
    '''
    Save an ONNX model to a path on the local file system.

    :param onnx_model: ONNX model to be saved.
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
                          model. The given example can be a Pandas DataFrame where the given
                          example will be serialized to json using the Pandas split-oriented
                          format, or a numpy array where the example will be serialized to json
                          by converting it to a list. Bytes are base64-encoded.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param onnx_execution_providers: List of strings defining onnxruntime execution providers.
                                     Defaults to example:
                                     ``[\'CUDAExecutionProvider\', \'CPUExecutionProvider\']``
                                     This uses GPU preferentially over CPU.
                                     See onnxruntime API for further descriptions:
                                     https://onnxruntime.ai/docs/execution-providers/
    :param onnx_session_options: Dictionary of options to be passed to onnxruntime.InferenceSession.
                                 For example:
                                 ``{
                                 \'graph_optimization_level\': 99,
                                 \'intra_op_num_threads\': 1,
                                 \'inter_op_num_threads\': 1,
                                 \'execution_mode\': \'sequential\'
                                 }``
                                 \'execution_mode\' can be set to \'sequential\' or \'parallel\'.
                                 See onnxruntime API for further descriptions:
                                 https://onnxruntime.ai/docs/api/python/api_summary.html#sessionoptions
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    '''

class _OnnxModelWrapper:
    rt: Incomplete
    inputs: Incomplete
    output_names: Incomplete
    def __init__(self, path, providers: Incomplete | None = None) -> None: ...
    def predict(self, data, params: Dict[str, Any] | None = None):
        """
        :param data: Either a pandas DataFrame, numpy.ndarray or a dictionary.

                     Dictionary input is expected to be a valid ONNX model feed dictionary.

                     Numpy array input is supported iff the model has a single tensor input and is
                     converted into an ONNX feed dictionary with the appropriate key.

                     Pandas DataFrame is converted to ONNX inputs as follows:
                        - If the underlying ONNX model only defines a *single* input tensor, the
                          DataFrame's values are converted to a NumPy array representation using the
                         `DataFrame.values()
                         <https://pandas.pydata.org/pandas-docs/stable/reference/api/
                          pandas.DataFrame.values.html#pandas.DataFrame.values>`_ method.
                        - If the underlying ONNX model defines *multiple* input tensors, each column
                          of the DataFrame is converted to a NumPy array representation.

                      For more information about the ONNX Runtime, see
                      `<https://github.com/microsoft/onnxruntime>`_.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.
        :return: Model predictions. If the input is a pandas.DataFrame, the predictions are returned
                 in a pandas.DataFrame. If the input is a numpy array or a dictionary the
                 predictions are returned in a dictionary.
        """

def load_model(model_uri, dst_path: Incomplete | None = None):
    """
    Load an ONNX model from a local file or a run.

    :param model_uri: The location, in URI format, of the MLflow model, for example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``models:/<model_name>/<model_version>``
                      - ``models:/<model_name>/<stage>``

                      For more information about supported URI schemes, see the
                      `Artifacts Documentation <https://www.mlflow.org/docs/latest/
                      tracking.html#artifact-stores>`_.
    :param dst_path: The local filesystem path to which to download the model artifact.
                     This directory must already exist. If unspecified, a local output
                     path will be created.

    :return: An ONNX model instance.

    """
def log_model(onnx_model, artifact_path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, await_registration_for=..., pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, onnx_execution_providers: Incomplete | None = None, onnx_session_options: Incomplete | None = None, metadata: Incomplete | None = None):
    '''
    Log an ONNX model as an MLflow artifact for the current run.

    :param onnx_model: ONNX model to be saved.
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
                          model. The given example can be a Pandas DataFrame where the given
                          example will be serialized to json using the Pandas split-oriented
                          format, or a numpy array where the example will be serialized to json
                          by converting it to a list. Bytes are base64-encoded.
    :param await_registration_for: Number of seconds to wait for the model version to finish
                            being created and is in ``READY`` status. By default, the function
                            waits for five minutes. Specify 0 or None to skip waiting.
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param onnx_execution_providers: List of strings defining onnxruntime execution providers.
                                     Defaults to example:
                                     [\'CUDAExecutionProvider\', \'CPUExecutionProvider\']
                                     This uses GPU preferentially over CPU.
                                     See onnxruntime API for further descriptions:
                                     https://onnxruntime.ai/docs/execution-providers/
    :param onnx_session_options: Dictionary of options to be passed to onnxruntime.InferenceSession.
                                 For example:
                                 ``{
                                 \'graph_optimization_level\': 99,
                                 \'intra_op_num_threads\': 1,
                                 \'inter_op_num_threads\': 1,
                                 \'execution_mode\': \'sequential\'
                                 }``
                                 \'execution_mode\' can be set to \'sequential\' or \'parallel\'.
                                 See onnxruntime API for further descriptions:
                                 https://onnxruntime.ai/docs/api/python/api_summary.html#sessionoptions
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.
    '''
