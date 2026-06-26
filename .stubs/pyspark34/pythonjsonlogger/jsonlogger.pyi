import json
import logging
from _typeshed import Incomplete
from typing import Any, Dict, List, Tuple

RESERVED_ATTRS: Tuple[str, ...]

def merge_record_extra(record: logging.LogRecord, target: Dict, reserved: Dict | List, rename_fields: Dict[str, str] | None = None) -> Dict:
    """
    Merges extra attributes from LogRecord object into target dictionary

    :param record: logging.LogRecord
    :param target: dict to update
    :param reserved: dict or list with reserved keys to skip
    :param rename_fields: an optional dict, used to rename field names in the output.
            Rename levelname to log.level: {'levelname': 'log.level'}
    """

class JsonEncoder(json.JSONEncoder):
    """
    A custom encoder extending the default JSONEncoder
    """
    def default(self, obj): ...
    def format_datetime_obj(self, obj): ...

class JsonFormatter(logging.Formatter):
    """
    A custom formatter to format logging records as json strings.
    Extra values will be formatted as str() if not supported by
    json default encoder
    """
    json_default: Incomplete
    json_encoder: Incomplete
    json_serializer: Incomplete
    json_indent: Incomplete
    json_ensure_ascii: Incomplete
    prefix: Incomplete
    rename_fields: Incomplete
    static_fields: Incomplete
    reserved_attrs: Incomplete
    timestamp: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        '''
        :param json_default: a function for encoding non-standard objects
            as outlined in https://docs.python.org/3/library/json.html
        :param json_encoder: optional custom encoder
        :param json_serializer: a :meth:`json.dumps`-compatible callable
            that will be used to serialize the log record.
        :param json_indent: an optional :meth:`json.dumps`-compatible numeric value
            that will be used to customize the indent of the output json.
        :param prefix: an optional string prefix added at the beginning of
            the formatted string
        :param rename_fields: an optional dict, used to rename field names in the output.
            Rename message to @message: {\'message\': \'@message\'}
        :param static_fields: an optional dict, used to add fields with static values to all logs
        :param json_indent: indent parameter for json.dumps
        :param json_ensure_ascii: ensure_ascii parameter for json.dumps
        :param reserved_attrs: an optional list of fields that will be skipped when
            outputting json log record. Defaults to all log record attributes:
            http://docs.python.org/library/logging.html#logrecord-attributes
        :param timestamp: an optional string/boolean field to add a timestamp when
            outputting the json log record. If string is passed, timestamp will be added
            to log record using string as key. If True boolean is passed, timestamp key
            will be "timestamp". Defaults to False/off.
        '''
    def parse(self) -> List[str]:
        """
        Parses format string looking for substitutions

        This method is responsible for returning a list of fields (as strings)
        to include in all log messages.
        """
    def add_fields(self, log_record: Dict[str, Any], record: logging.LogRecord, message_dict: Dict[str, Any]) -> None:
        """
        Override this method to implement custom logic for adding fields.
        """
    def process_log_record(self, log_record):
        """
        Override this method to implement custom logic
        on the possibly ordered dictionary.
        """
    def jsonify_log_record(self, log_record):
        """Returns a json string of the log record."""
    def serialize_log_record(self, log_record: Dict[str, Any]) -> str:
        """Returns the final representation of the log record."""
    def format(self, record: logging.LogRecord) -> str:
        """Formats a log record and serializes to json"""
