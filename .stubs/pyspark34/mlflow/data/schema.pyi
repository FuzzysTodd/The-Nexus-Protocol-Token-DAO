from _typeshed import Incomplete
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.types.schema import Schema as Schema
from typing import Any, Dict

class TensorDatasetSchema:
    """
    Represents the schema of a dataset with tensor features and targets.
    """
    features: Incomplete
    targets: Incomplete
    def __init__(self, features: Schema, targets: Schema = None) -> None: ...
    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize into a 'jsonable' dictionary.

        :return: dictionary representation of the schema's features and targets (if defined).
        """
    @classmethod
    def from_dict(cls, schema_dict: Dict[str, Any]):
        '''
        Deserialize from dictionary representation.

        :param schema_dict: Dictionary representation of model signature.
                            Expected dictionary format:
                            `{\'features\': <json string>, \'targets\': <json string>" }`

        :return: TensorDatasetSchema populated with the data from the dictionary.
        '''
    def __eq__(self, other) -> bool: ...
