import logging
from .handler import LOGGER_ROOT_PREFIX as LOGGER_ROOT_PREFIX, SynapseHandler as SynapseHandler
from .scrubbers.scrubber import IScrub as IScrub
from _typeshed import Incomplete
from typing import Any, List

logger: Incomplete

def default_converter(obj: Any) -> str: ...

class DecoratorJSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord): ...

def get_mds_logger(name: str, log_level: int = ..., tableName: str | None = None, formatter: logging.Formatter | None = None, scrubbers: List[IScrub] | None = None) -> logging.Logger:
    """
    Get a mds Logger for fabric internal use only
    """
def get_mds_json_logger(name: str, log_level: int = ..., tableName: str | None = None, scrubbers: List[IScrub] | None = None) -> logging.Logger: ...
def add_mds_table_handler(logger: logging.Logger, tableName: str, formatter: logging.Formatter | None = None, scrubbers: List[IScrub] | None = None):
    """
    Add handler sending kusto logs to existing logger
    """
