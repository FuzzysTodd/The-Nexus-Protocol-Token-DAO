import json
from _typeshed import Incomplete
from json import JSONEncoder
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.protos.databricks_pb2 import BAD_REQUEST as BAD_REQUEST
from typing import Any, Dict

def message_to_json(message):
    """Converts a message to JSON, using snake_case for field names."""
def parse_dict(js_dict, message) -> None:
    """Parses a JSON dictionary into a message proto, ignoring unknown fields in the JSON."""

class NumpyEncoder(JSONEncoder):
    """Special json encoder for numpy types.
    Note that some numpy types doesn't have native python equivalence,
    hence json.dumps will raise TypeError.
    In this case, you'll need to convert your numpy types into its closest python equivalence.
    """
    def try_convert(self, o): ...
    def default(self, o): ...

class MlflowFailedTypeConversion(MlflowException):
    def __init__(self, col_name, col_type, ex) -> None: ...

def cast_df_types_according_to_schema(pdf, schema): ...

class MlflowBadScoringInputException(MlflowException):
    def __init__(self, message) -> None: ...

def dataframe_from_parsed_json(decoded_input, pandas_orient, schema: Incomplete | None = None):
    """
    Convert parsed json into pandas.DataFrame. If schema is provided this methods will attempt to
    cast data types according to the schema. This include base64 decoding for binary columns.

    :param decoded_input: Parsed json - either a list or a dictionary.
    :param schema: Mlflow schema used when parsing the data.
    :param pandas_orient: pandas data frame convention used to store the data.
    :return: pandas.DataFrame.
    """
def dataframe_from_raw_json(path_or_str, schema: Incomplete | None = None, pandas_orient: str = 'split'):
    """
    Parse raw json into a pandas.Dataframe.

    If schema is provided this methods will attempt to cast data types according to the schema. This
    include base64 decoding for binary columns.

    :param path_or_str: Path to a json file or a json string.
    :param schema: Mlflow schema used when parsing the data.
    :param pandas_orient: pandas data frame convention used to store the data.
    :return: pandas.DataFrame.
    """
def parse_tf_serving_input(inp_dict, schema: Incomplete | None = None):
    """
    :param inp_dict: A dict deserialized from a JSON string formatted as described in TF's
                     serving API doc
                     (https://www.tensorflow.org/tfx/serving/api_rest#request_format_2)
    :param schema: Mlflow schema used when parsing the data.
    """

class _CustomJsonEncoder(json.JSONEncoder):
    def default(self, o): ...

def get_jsonable_input(name, data): ...
def dump_input_data(data, inputs_key: str = 'inputs', params: Dict[str, Any] | None = None):
    """
    :param data: Input data.
    :param inputs_key: Key to represent data in the request payload.
    :param params: Additional parameters to pass to the model for inference.

                       .. Note:: Experimental: This parameter may change or be removed in a future
                                               release without warning.
    """
