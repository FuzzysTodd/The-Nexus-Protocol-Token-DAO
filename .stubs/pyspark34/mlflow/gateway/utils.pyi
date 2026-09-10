from mlflow.environment_variables import MLFLOW_GATEWAY_URI as MLFLOW_GATEWAY_URI
from mlflow.exceptions import MlflowException as MlflowException
from mlflow.utils.annotations import experimental as experimental
from mlflow.utils.uri import append_to_uri_path as append_to_uri_path
from typing import List

def is_valid_endpoint_name(name: str) -> bool:
    """
    Check whether a string contains any URL reserved characters, spaces, or characters other
    than alphanumeric, underscore, hyphen, and dot.

    Returns True if the string doesn't contain any of these characters.
    """
def check_configuration_route_name_collisions(config) -> None: ...
def kill_child_processes(parent_pid) -> None:
    """
    Gracefully terminate or kill child processes from a main process
    """
def set_gateway_uri(gateway_uri: str):
    '''
    Sets the uri of a configured and running MLflow AI Gateway server in a global context.
    Providing a valid uri and calling this function is required in order to use the MLflow
    AI Gateway fluent APIs.

    :param gateway_uri: The full uri of a running MLflow AI Gateway server or, if running on
                        Databricks, "databricks".
    '''
def get_gateway_uri() -> str:
    """
    Returns the currently set MLflow AI Gateway server uri iff set.
    If the Gateway uri has not been set by using ``set_gateway_uri``, an ``MlflowException``
    is raised.
    """
def assemble_uri_path(paths: List[str]) -> str:
    """
    Assemble a correct URI path from a list of path parts.

    :param paths: A list of strings representing parts of a URI path.
    :return: A string representing the complete assembled URI path.
    """
def resolve_route_url(base_url: str, route: str) -> str:
    """
    Performs a validation on whether the returned value is a fully qualified url (as the case
    with Databricks) or requires the assembly of a fully qualified url by appending the
    Route return route_url to the base url of the AI Gateway server.

    :param base_url: The base URL. Should include the scheme and domain, e.g.,
                     ``http://127.0.0.1:6000``.
    :param route: The route to be appended to the base URL, e.g., ``/api/2.0/gateway/routes/`` or,
                  in the case of Databricks, the fully qualified url.
    :return: The complete URL, either directly returned or formed and returned by joining the
             base URL and the route path.
    """

class SearchRoutesToken:
    def __init__(self, index: int) -> None: ...
    @property
    def index(self): ...
    @classmethod
    def decode(cls, encoded_token: str): ...
    def encode(self) -> str: ...
