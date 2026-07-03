from _typeshed import Incomplete
from mlflow import pyfunc as pyfunc
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models import Model as Model, ModelSignature as ModelSignature
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.models.utils import ModelInputExample as ModelInputExample
from mlflow.utils.docstring_utils import LOG_MODEL_PARAM_DOCS as LOG_MODEL_PARAM_DOCS, format_docstring as format_docstring
from mlflow.utils.file_utils import write_to as write_to
from typing import Any, Dict

FLAVOR_NAME: str

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
def save_model(spacy_model, path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, mlflow_model: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None):
    '''
    Save a spaCy model to a path on the local file system.

    :param spacy_model: spaCy model to be saved.
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
    '''
def log_model(spacy_model, artifact_path, conda_env: Incomplete | None = None, code_paths: Incomplete | None = None, registered_model_name: Incomplete | None = None, signature: ModelSignature = None, input_example: ModelInputExample = None, pip_requirements: Incomplete | None = None, extra_pip_requirements: Incomplete | None = None, metadata: Incomplete | None = None, **kwargs):
    '''
    Log a spaCy model as an MLflow artifact for the current run.

    :param spacy_model: spaCy model to be saved.
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
    :param pip_requirements: {{ pip_requirements }}
    :param extra_pip_requirements: {{ extra_pip_requirements }}
    :param metadata: Custom metadata dictionary passed to the model and stored in the MLmodel file.

                     .. Note:: Experimental: This parameter may change or be removed in a future
                                             release without warning.
    :param kwargs: kwargs to pass to ``spacy.save_model`` method.
    :return: A :py:class:`ModelInfo <mlflow.models.model.ModelInfo>` instance that contains the
             metadata of the logged model.
    '''

class _SpacyModelWrapper:
    spacy_model: Incomplete
    def __init__(self, spacy_model) -> None: ...
    def predict(self, dataframe, params: Dict[str, Any] | None = None):
        """
        Only works for predicting using text categorizer.
        Not suitable for other pipeline components (e.g: parser)
        :param dataframe: pandas dataframe containing texts to be categorized
                          expected shape is (n_rows,1 column)
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: dataframe with predictions
        """

def load_model(model_uri, dst_path: Incomplete | None = None):
    """
    Load a spaCy model from a local file (if ``run_id`` is ``None``) or a run.

    :param model_uri: The location, in URI format, of the MLflow model. For example:

                      - ``/Users/me/path/to/local/model``
                      - ``relative/path/to/local/model``
                      - ``s3://my_bucket/path/to/model``
                      - ``runs:/<mlflow_run_id>/run-relative/path/to/model``
                      - ``models:/<model_name>/<model_version>``
                      - ``models:/<model_name>/<stage>``

                      For more information about supported URI schemes, see
                      `Referencing Artifacts <https://www.mlflow.org/docs/latest/concepts.html#
                      artifact-locations>`_.
    :param dst_path: The local filesystem path to which to download the model artifact.
                     This directory must already exist. If unspecified, a local output
                     path will be created.

    :return: A spaCy loaded model
    """
