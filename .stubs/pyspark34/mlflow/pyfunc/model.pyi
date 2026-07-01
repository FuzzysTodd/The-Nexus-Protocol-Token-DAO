import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.models import Model as Model
from mlflow.models.model import MLMODEL_FILE_NAME as MLMODEL_FILE_NAME
from mlflow.utils.file_utils import TempDir as TempDir, write_to as write_to
from typing import Any, Dict

CONFIG_KEY_ARTIFACTS: str
CONFIG_KEY_ARTIFACT_RELATIVE_PATH: str
CONFIG_KEY_ARTIFACT_URI: str
CONFIG_KEY_PYTHON_MODEL: str
CONFIG_KEY_CLOUDPICKLE_VERSION: str

def get_default_pip_requirements():
    """
    :return: A list of default pip requirements for MLflow Models produced by this flavor.
             Calls to :func:`save_model()` and :func:`log_model()` produce a pip environment
             that, at minimum, contains these requirements.
    """
def get_default_conda_env():
    """
    :return: The default Conda environment for MLflow Models produced by calls to
             :func:`save_model() <mlflow.pyfunc.save_model>`
             and :func:`log_model() <mlflow.pyfunc.log_model>` when a user-defined subclass of
             :class:`PythonModel` is provided.
    """

class PythonModel(metaclass=abc.ABCMeta):
    '''
    Represents a generic Python model that evaluates inputs and produces API-compatible outputs.
    By subclassing :class:`~PythonModel`, users can create customized MLflow models with the
    "python_function" ("pyfunc") flavor, leveraging custom inference logic and artifact
    dependencies.
    '''
    __metaclass__ = ABCMeta
    def load_context(self, context) -> None:
        """
        Loads artifacts from the specified :class:`~PythonModelContext` that can be used by
        :func:`~PythonModel.predict` when evaluating inputs. When loading an MLflow model with
        :func:`~load_model`, this method is called as soon as the :class:`~PythonModel` is
        constructed.

        The same :class:`~PythonModelContext` will also be available during calls to
        :func:`~PythonModel.predict`, but it may be more efficient to override this method
        and load artifacts from the context at model load time.

        :param context: A :class:`~PythonModelContext` instance containing artifacts that the model
                        can use to perform inference.
        """
    @abstractmethod
    def predict(self, context, model_input, params: Dict[str, Any] | None = None):
        """
        Evaluates a pyfunc-compatible input and produces a pyfunc-compatible output.
        For more information about the pyfunc input/output API, see the :ref:`pyfunc-inference-api`.

        :param context: A :class:`~PythonModelContext` instance containing artifacts that the model
                        can use to perform inference.
        :param model_input: A pyfunc-compatible input for the model to evaluate.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.
        """

class _FunctionPythonModel(PythonModel):
    """
    When a user specifies a ``python_model`` argument that is a function, we wrap the function
    in an instance of this class.
    """
    func: Incomplete
    hints: Incomplete
    signature: Incomplete
    def __init__(self, func, hints: Incomplete | None = None, signature: Incomplete | None = None) -> None: ...
    def predict(self, context, model_input, params: Dict[str, Any] | None = None):
        """
        :param context: A :class:`~PythonModelContext` instance containing artifacts that the model
                        can use to perform inference.
        :param model_input: A pyfunc-compatible input for the model to evaluate.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """

class PythonModelContext:
    """
    A collection of artifacts that a :class:`~PythonModel` can use when performing inference.
    :class:`~PythonModelContext` objects are created *implicitly* by the
    :func:`save_model() <mlflow.pyfunc.save_model>` and
    :func:`log_model() <mlflow.pyfunc.log_model>` persistence methods, using the contents specified
    by the ``artifacts`` parameter of these methods.
    """
    def __init__(self, artifacts) -> None:
        """
        :param artifacts: A dictionary of ``<name, artifact_path>`` entries, where ``artifact_path``
                          is an absolute filesystem path to a given artifact.
        """
    @property
    def artifacts(self):
        """
        A dictionary containing ``<name, artifact_path>`` entries, where ``artifact_path`` is an
        absolute filesystem path to the artifact.
        """

class _PythonModelPyfuncWrapper:
    """
    Wrapper class that creates a predict function such that
    predict(model_input: pd.DataFrame) -> model's output as pd.DataFrame (pandas DataFrame)
    """
    python_model: Incomplete
    context: Incomplete
    signature: Incomplete
    def __init__(self, python_model, context, signature) -> None:
        """
        :param python_model: An instance of a subclass of :class:`~PythonModel`.
        :param context: A :class:`~PythonModelContext` instance containing artifacts that
                        ``python_model`` may use when performing inference.
        :param signature: :class:`~ModelSignature` instance describing model input and output.
        """
    def predict(self, model_input, params: Dict[str, Any] | None = None):
        """
        :param model_input: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.

        :return: Model predictions.
        """
