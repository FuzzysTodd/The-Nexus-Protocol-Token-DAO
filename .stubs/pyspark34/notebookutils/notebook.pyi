from typing import Any, Dict, List, Optional, Union

__all__ = [
    'updateNBSEndpoint', 'help', 'run', 'exit', 'runMultiple', 'validateDAG', 
    'create', 'delete', 'list', 'get', 'update', 'updateDefinition', 'getDefinition'
]

def updateNBSEndpoint(endpoint: str) -> None:
    """
    Update the notebook service endpoint.
    
    :param endpoint: New endpoint URL
    """

def help(method_name: Optional[str] = None) -> None:
    """
    Provides help for the notebookutils.notebook module or the specified method.

    Examples:
    notebookutils.notebook.help()
    notebookutils.notebook.help("run")
    :param method_name: The name of the method to get help with.
    """

def run(path: str, timeout_seconds: int = 90, arguments: Dict[str, Any] = {}, workspace: str = "") -> int:
    """
    Run a notebook and return the exit value.
    
    :param path: Path to the notebook
    :param timeout_seconds: Timeout in seconds
    :param arguments: Arguments to pass to the notebook
    :param workspace: Workspace containing the notebook
    :return: Exit value
    """

def exit(value: int) -> None:
    """
    Exit the current notebook with a specific value.
    
    :param value: Exit value
    """

def runMultiple(dag: Union[List[str], Dict, str], config: Optional[Dict[str, Any]] = None) -> Any:
    """
    Runs multiple notebooks concurrently with support for dependency relationships.
    
    :param dag: A list of notebook names or a complex data structure (dict or JSON string)
    :param config: Configuration for the display DAG. Keys include: displayDAG, DAGLayout, DAGSize
    :return: Execution result
    """

def validateDAG(dag: Union[List[str], Dict, str]) -> bool:
    """
    Validate a DAG structure for notebook execution.
    
    :param dag: DAG structure to validate
    :return: True if valid
    """

def create(name: str, description: str = "", content: Optional[str] = None,
           defaultLakehouse: str = "", defaultLakehouseWorkspace: str = "", workspaceId: str = "") -> Any:
    """
    Create a new notebook.
    
    :param name: Name of the notebook
    :param description: Description of the notebook
    :param content: Notebook content
    :param defaultLakehouse: Default lakehouse for the notebook
    :param defaultLakehouseWorkspace: Workspace of the default lakehouse
    :param workspaceId: Workspace ID where to create the notebook
    :return: Created notebook information
    """

def delete(name: str, workspaceId: str = "") -> bool:
    """
    Delete a notebook.
    
    :param name: Name of the notebook to delete
    :param workspaceId: Workspace ID containing the notebook
    :return: True if successful
    """

def list(workspaceId: str = "", maxResults: int = 1000) -> List[Any]:
    """
    List notebooks in a workspace.
    
    :param workspaceId: Workspace ID to list from
    :param maxResults: Maximum number of results to return
    :return: List of notebook information
    """

def get(name: str, workspaceId: str = "") -> Any:
    """
    Get notebook information.
    
    :param name: Name of the notebook
    :param workspaceId: Workspace ID containing the notebook
    :return: Notebook information
    """

def update(name: str, newName: str, description: str = "", workspaceId: str = "") -> Any:
    """
    Update notebook properties.
    
    :param name: Current name of the notebook
    :param newName: New name for the notebook
    :param description: New description
    :param workspaceId: Workspace ID containing the notebook
    :return: Updated notebook information
    """

def updateDefinition(name: str,
                     content: Optional[str] = None,
                     defaultLakehouse: str = "",
                     defaultLakehouseWorkspace: str = "",
                     workspaceId: str = "",
                     environmentId: str = "",
                     environmentWorkspaceId: str = "") -> Any:
    """
    Update notebook definition.
    
    :param name: Name of the notebook
    :param content: New notebook content
    :param defaultLakehouse: Default lakehouse
    :param defaultLakehouseWorkspace: Default lakehouse workspace
    :param workspaceId: Workspace ID
    :param environmentId: Environment ID
    :param environmentWorkspaceId: Environment workspace ID
    :return: Updated notebook information
    """

def getDefinition(name: str, workspaceId: str = "", format: str = "ipynb") -> Any:
    """
    Get notebook definition.
    
    :param name: Name of the notebook
    :param workspaceId: Workspace ID containing the notebook
    :param format: Format of the definition (e.g., "ipynb")
    :return: Notebook definition
    """
