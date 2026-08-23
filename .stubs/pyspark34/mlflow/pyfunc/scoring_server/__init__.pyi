from _typeshed import Incomplete
from mlflow.environment_variables import MLFLOW_SCORING_SERVER_REQUEST_TIMEOUT as MLFLOW_SCORING_SERVER_REQUEST_TIMEOUT
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import BAD_REQUEST as BAD_REQUEST, INVALID_PARAMETER_VALUE as INVALID_PARAMETER_VALUE
from mlflow.pyfunc import PyFuncModel as PyFuncModel, load_pyfunc as load_model
from mlflow.server.handlers import catch_mlflow_exception as catch_mlflow_exception
from mlflow.types import Schema as Schema
from mlflow.utils import reraise as reraise
from mlflow.utils.annotations import deprecated as deprecated
from mlflow.utils.file_utils import path_to_local_file_uri as path_to_local_file_uri
from mlflow.utils.os import is_windows as is_windows
from mlflow.utils.proto_json_utils import NumpyEncoder as NumpyEncoder, dataframe_from_parsed_json as dataframe_from_parsed_json, parse_tf_serving_input as parse_tf_serving_input
from mlflow.version import VERSION as VERSION
from typing import Dict, NamedTuple, Tuple

CONTENT_TYPE_CSV: str
CONTENT_TYPE_JSON: str
CONTENT_TYPES: Incomplete
DF_RECORDS: str
DF_SPLIT: str
INSTANCES: str
INPUTS: str
SUPPORTED_FORMATS: Incomplete
REQUIRED_INPUT_FORMAT: Incomplete
SCORING_PROTOCOL_CHANGE_INFO: str

def infer_and_parse_json_input(json_input, schema: Schema = None):
    """
    :param json_input: A JSON-formatted string representation of TF serving input or a Pandas
                       DataFrame, or a stream containing such a string representation.
    :param schema: Optional schema specification to be used during parsing.
    """
def infer_and_parse_data(data, schema: Schema = None):
    """
    :param data: A dictionary representation of TF serving input or a Pandas
                 DataFrame, or a stream containing such a string representation.
    :param schema: Optional schema specification to be used during parsing.
    """
def parse_csv_input(csv_input, schema: Schema = None):
    """
    :param csv_input: A CSV-formatted string representation of a Pandas DataFrame, or a stream
                      containing such a string representation.
    :param schema: Optional schema specification to be used during parsing.
    """
def predictions_to_json(raw_predictions, output, metadata: Incomplete | None = None): ...

class InvocationsResponse(NamedTuple):
    response: str
    status: int
    mimetype: str

def invocations(data, content_type, model, input_schema): ...
def init(model: PyFuncModel):
    """
    Initialize the server. Loads pyfunc model from the path.
    """
def get_cmd(model_uri: str, port: int = None, host: int = None, timeout: int = None, nworkers: int = None) -> Tuple[str, Dict[str, str]]: ...
