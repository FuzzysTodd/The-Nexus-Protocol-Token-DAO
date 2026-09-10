import requests
from _typeshed import Incomplete

class SemPyException(Exception):
    """
    Base class for other exceptions.
    """

class FabricHTTPException(SemPyException, requests.HTTPError):
    """
    Raised when an API call to any Fabric REST API fails with status code >= 400.

    Parameters
    ----------
    response : requests.Response
        Response object returned from API call (see `requests.Response <https://requests.readthedocs.io/en/latest/api/#requests.Response>`_).
    """
    error_reason: str
    error_text: Incomplete
    status_code: Incomplete
    def __init__(self, response: requests.Response) -> None: ...

class DatasetNotFoundException(SemPyException):
    """
    Raised when specified dataset (name or UUID) is not found in workspace.

    Parameters
    ----------
    dataset : str
        Dataset name or id.
    workspace_name : str
        Workspace name.
    """
    dataset: Incomplete
    workspace_name: Incomplete
    def __init__(self, dataset: str, workspace_name: str) -> None: ...

class WorkspaceNotFoundException(SemPyException):
    """
    Raised when specified workspace (name or UUID) is not found.

    Parameters
    ----------
    workspace : str
        Workspace name or id.
    """
    workspace: Incomplete
    def __init__(self, workspace: str) -> None: ...
