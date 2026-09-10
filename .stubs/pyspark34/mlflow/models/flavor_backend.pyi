import abc
from _typeshed import Incomplete
from abc import ABCMeta, abstractmethod
from mlflow.utils.annotations import developer_stable as developer_stable

class FlavorBackend(metaclass=abc.ABCMeta):
    """
    Abstract class for Flavor Backend.
    This class defines the API interface for local model deployment of MLflow model flavors.
    """
    __metaclass__ = ABCMeta
    def __init__(self, config, **kwargs) -> None: ...
    @abstractmethod
    def predict(self, model_uri, input_path, output_path, content_type):
        """
        Generate predictions using a saved MLflow model referenced by the given URI.
        Input and output are read from and written to a file or stdin / stdout.

        :param model_uri: URI pointing to the MLflow model to be used for scoring.
        :param input_path: Path to the file with input data. If not specified, data is read from
                           stdin.
        :param output_path: Path to the file with output predictions. If not specified, data is
                            written to stdout.
        :param content_type: Specifies the input format. Can be one of {``json``, ``csv``}
        """
    @abstractmethod
    def serve(self, model_uri, port, host, timeout, enable_mlserver, synchronous: bool = True, stdout: Incomplete | None = None, stderr: Incomplete | None = None):
        """
        Serve the specified MLflow model locally.

        :param model_uri: URI pointing to the MLflow model to be used for scoring.
        :param port: Port to use for the model deployment.
        :param host: Host to use for the model deployment. Defaults to ``localhost``.
        :param timeout: Timeout in seconds to serve a request. Defaults to 60.
        :param enable_mlserver: Whether to use MLServer or the local scoring server.
        :param synchronous: If True, wait until server process exit and return 0, if process exit
                            with non-zero return code, raise exception.
                            If False, return the server process `Popen` instance immediately.
        :param stdout: Redirect server stdout
        :param stderr: Redirect server stderr
        """
    def prepare_env(self, model_uri, capture_output: bool = False) -> None:
        """
        Performs any preparation necessary to predict or serve the model, for example
        downloading dependencies or initializing a conda environment. After preparation,
        calling predict or serve should be fast.
        """
    @abstractmethod
    def build_image(self, model_uri, image_name, install_mlflow, mlflow_home, enable_mlserver): ...
    @abstractmethod
    def generate_dockerfile(self, model_uri, output_path, install_mlflow, mlflow_home, enable_mlserver): ...
    @abstractmethod
    def can_score_model(self):
        """
        Check whether this flavor backend can be deployed in the current environment.

        :return: True if this flavor backend can be applied in the current environment.
        """
    def can_build_image(self):
        """
        :return: True if this flavor has a `build_image` method defined for building a docker
                 container capable of serving the model, False otherwise.
        """
