import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from mlflow.deployments import PredictionsResponse as PredictionsResponse
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.pyfunc import scoring_server as scoring_server
from mlflow.utils.proto_json_utils import dump_input_data as dump_input_data
from typing import Any, Dict

class BaseScoringServerClient(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def wait_server_ready(self, timeout: int = 30, scoring_server_proc: Incomplete | None = None):
        """
        Wait until the scoring server is ready to accept requests.
        """
    @abstractmethod
    def invoke(self, data, params: Dict[str, Any] | None = None):
        """
        Invoke inference on input data. The input data must be pandas dataframe or numpy array or
        a dict of numpy arrays.
        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.
        :return: Prediction result.
        """

class ScoringServerClient(BaseScoringServerClient):
    url_prefix: Incomplete
    def __init__(self, host, port) -> None: ...
    def ping(self) -> None: ...
    def get_version(self): ...
    def wait_server_ready(self, timeout: int = 30, scoring_server_proc: Incomplete | None = None) -> None: ...
    def invoke(self, data, params: Dict[str, Any] | None = None):
        """
        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.
        :return: :py:class:`PredictionsResponse <mlflow.deployments.PredictionsResponse>` result.
        """

class StdinScoringServerClient(BaseScoringServerClient):
    process: Incomplete
    tmpdir: Incomplete
    output_json: Incomplete
    def __init__(self, process) -> None: ...
    def wait_server_ready(self, timeout: int = 30, scoring_server_proc: Incomplete | None = None) -> None: ...
    def invoke(self, data, params: Dict[str, Any] | None = None):
        """
        Invoke inference on input data. The input data must be pandas dataframe or numpy array or
        a dict of numpy arrays.

        :param data: Model input data.
        :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.
        :return: :py:class:`PredictionsResponse <mlflow.deployments.PredictionsResponse>` result.
        """
