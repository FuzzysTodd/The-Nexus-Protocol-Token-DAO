from typing import Any, Dict, List, Optional

__all__ = [
    'create', 'delete', 'list', 'get', 'update', 'getDefinition', 
    'updateDefinition', 'listTables', 'loadTable', 'getWithProperties', 'help'
]

def create(name: str, description: str = "", definition: Optional[Dict] = None, workspaceId: str = "") -> Any:
    """
    Create a new lakehouse.
    
    :param name: Name of the lakehouse
    :param description: Description of the lakehouse
    :param definition: Lakehouse definition
    :param workspaceId: Workspace ID where to create the lakehouse
    :return: Created lakehouse information
    """

def delete(name: str, workspaceId: str = "") -> bool:
    """
    Delete a lakehouse.
    
    :param name: Name of the lakehouse to delete
    :param workspaceId: Workspace ID containing the lakehouse
    :return: True if successful
    """

def list(workspaceId: str = "", maxResults: int = 1000) -> List[Any]:
    """
    List lakehouses in a workspace.
    
    :param workspaceId: Workspace ID to list from
    :param maxResults: Maximum number of results to return
    :return: List of lakehouse information
    """

def get(name: str = "", workspaceId: str = "") -> Any:
    """
    Get lakehouse information.
    
    :param name: Name of the lakehouse
    :param workspaceId: Workspace ID containing the lakehouse
    :return: Lakehouse information
    """

def update(name: str, newName: str, description: str = "", workspaceId: str = "") -> Any:
    """
    Update lakehouse properties.
    
    :param name: Current name of the lakehouse
    :param newName: New name for the lakehouse
    :param description: New description
    :param workspaceId: Workspace ID containing the lakehouse
    :return: Updated lakehouse information
    """

def getDefinition(name: str, workspaceId: str = "") -> Any:
    """
    Get lakehouse definition.
    
    :param name: Name of the lakehouse
    :param workspaceId: Workspace ID containing the lakehouse
    :return: Lakehouse definition
    """

def updateDefinition(name: str, definition: Dict, workspaceId: str = "") -> Any:
    """
    Update lakehouse definition.
    
    :param name: Name of the lakehouse
    :param definition: New definition
    :param workspaceId: Workspace ID containing the lakehouse
    :return: Updated lakehouse information
    """

def listTables(lakehouse: str = "", workspaceId: str = "", maxResults: int = 1000) -> List[Any]:
    """
    List tables in a lakehouse.
    
    :param lakehouse: Name of the lakehouse
    :param workspaceId: Workspace ID containing the lakehouse
    :param maxResults: Maximum number of results to return
    :return: List of table information
    """

def loadTable(loadOption: str, table: str, lakehouse: str = "", workspaceId: str = "") -> Any:
    """
    Load a table from lakehouse.
    
    :param loadOption: Load option specification
    :param table: Table name
    :param lakehouse: Lakehouse name
    :param workspaceId: Workspace ID
    :return: Loaded table
    """

def getWithProperties(name: str, workspaceId: str = "") -> Any:
    """
    Get lakehouse with detailed properties.
    
    :param name: Name of the lakehouse
    :param workspaceId: Workspace ID containing the lakehouse
    :return: Lakehouse information with properties
    """

def help(method_name: Optional[str] = None) -> None:
    """
    Provides help for the notebookutils.lakehouse module or the specified method.

    Examples:
    notebookutils.lakehouse.help()
    notebookutils.lakehouse.help("create")
    :param method_name: The name of the method to get help with.
    """
