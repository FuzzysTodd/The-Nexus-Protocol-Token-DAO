from _typeshed import Incomplete
from databricks_cli.click_types import ContextObject as ContextObject

CONTEXT_SETTINGS: Incomplete
CLUSTER_OPTIONS: Incomplete
DEBUG_MODE: bool

def eat_exceptions(function): ...
def pipelines_exception_eater(function):
    """
    Formats error messages from the pipelines API while keeping the existing
    behavior of eat_exception
    """
def error_and_quit(message) -> None: ...

INTERVAL_MAX: int
INTERVAL_BASE: int
MAX_EXPONENT: int

def backoff_with_jitter(attempt):
    """
    Creates a growing but randomized wait time based on the number of attempts already made.
    """
def pretty_format(json, encode_utf8: bool = False): ...
def json_cli_base(json_file, json, api, error_msg: str = '', print_response: bool = True, encode_utf8: bool = False) -> None:
    '''
    Takes json_file or json string and calls an function "api" with the json
    deserialized
    '''
def truncate_string(s, length: int = 100): ...
def to_graph(dict_obj, graph_name: str = 'Graph'): ...

class InvalidConfigurationError(RuntimeError):
    @staticmethod
    def for_profile(profile): ...

def merge_dicts_shallow(*dicts):
    """
    Merges dicts through shallow copy.
    """
