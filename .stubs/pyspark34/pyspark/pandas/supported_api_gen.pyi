from _typeshed import Incomplete
from enum import Enum
from pyspark.pandas.exceptions import PandasNotImplementedError as PandasNotImplementedError
from typing import NamedTuple

MAX_MISSING_PARAMS_SIZE: int
COMMON_PARAMETER_SET: Incomplete
MODULE_GROUP_MATCH: Incomplete
RST_HEADER: str

class Implemented(Enum):
    IMPLEMENTED: str
    NOT_IMPLEMENTED: str
    PARTIALLY_IMPLEMENTED: str

class SupportedStatus(NamedTuple):
    """
    Defines a supported status for specific pandas API
    """
    implemented: str
    missing: str

def generate_supported_api(output_rst_file_path: str) -> None:
    """
    Generate supported APIs status dictionary.

    Parameters
    ----------
    output_rst_file_path : str
        The path to the document file in RST format.

    Write supported APIs documentation.
    """
