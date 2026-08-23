from _typeshed import Incomplete
from typing import Any

fs_client: Any | None
environment: str | None
on_fabric: bool | None
on_jupyter: bool | None
on_aiskill: bool | None
jupyter_config: dict[str, str] | None
SUPPORTED_ENVIRONMENTS: Incomplete
SUPPORTED_FABRIC_REST_ENVIRONMENTS: Incomplete

def get_workspace_id() -> str:
    """
    Return workspace id or default Lakehouse's workspace id.

    Returns
    -------
    str
        Workspace id guid if no default Lakehouse is set; otherwise, the default Lakehouse's workspace id guid.
    """
def get_lakehouse_id() -> str:
    """
    Return lakehouse id of the lakehouse that is connected to the workspace.

    Returns
    -------
    str
        Lakehouse id guid.
    """
def get_notebook_workspace_id() -> str:
    """
    Return notebook workspace id.

    Returns
    -------
    str
        Workspace id guid.
    """
def get_artifact_id() -> str:
    """
    Return artifact id.

    Returns
    -------
    str
        Artifact (most commonly notebook) id guid.
    """
