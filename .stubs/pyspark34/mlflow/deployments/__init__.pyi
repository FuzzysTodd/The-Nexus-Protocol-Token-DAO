from _typeshed import Incomplete
from mlflow.deployments.base import BaseDeploymentClient as BaseDeploymentClient
from mlflow.deployments.interface import get_deploy_client as get_deploy_client, run_local as run_local

__all__ = ['get_deploy_client', 'run_local', 'BaseDeploymentClient', 'PredictionsResponse']

class PredictionsResponse(dict):
    """
    Represents the predictions and metadata returned in response to a scoring request, such as a
    REST API request sent to the ``/invocations`` endpoint of an MLflow Model Server.
    """
    def get_predictions(self, predictions_format: str = 'dataframe', dtype: Incomplete | None = None):
        '''
        Get the predictions returned from the MLflow Model Server in the specified format.

        :param predictions_format: The format in which to return the predictions. Either
                                   ``"dataframe"`` or ``"ndarray"``.
        :param dtype: The NumPy datatype to which to coerce the predictions. Only used when
                      the ``"ndarray"`` ``predictions_format`` is specified.
        :throws: Exception if the predictions cannot be represented in the specified format.
        :return: The predictions, represented in the specified format.
        '''
    def to_json(self, path: Incomplete | None = None):
        """
        Get the JSON representation of the MLflow Predictions Response.

        :param path: If specified, the JSON representation is written to this file path.
        :return: If ``path`` is unspecified, the JSON representation of the MLflow Predictions
                 Response. Else, None.
        """
    @classmethod
    def from_json(cls, json_str): ...
