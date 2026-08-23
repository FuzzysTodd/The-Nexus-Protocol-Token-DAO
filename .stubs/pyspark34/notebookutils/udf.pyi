from typing import Any, Dict, Optional
from notebookutils.mssparkutils.handlers import UDF

__all__ = ['getFunctions', 'run', 'help']


def getFunctions(udf: str, workspaceId: str = "") -> UDF:
    """
    Get the User defined functions (UDF).
    
    :param udf: The UDF artifact id or name
    :param workspaceId: The UDF workspace id, if not provided, it will be retrieved from the current workspace
    :return: The UDF functions
    
    Example:
    myFunctions = notebookutils.udf.getFunctions("myUdf")
    myFunctions.functionDetails # get function details
    myFunctions.add(1, 2) # call function add
    myFunctions.multiply(1, 2, 3) # call function multiply
    """

def run(artifactId: str, functionName: str, parameters: Optional[Dict[Any, Any]] = None, 
        workspaceId: str = "", capacityId: str = "") -> Any:
    """
    Run a User defined function (UDF).
    
    :param artifactId: The UDF artifact id
    :param functionName: The UDF function name
    :param parameters: The UDF parameters
    :param workspaceId: The UDF workspace id, if not provided, it will be retrieved from the current workspace
    :param capacityId: The UDF capacity id, if not provided, it will be retrieved from the current capacity
    :return: The UDF execution result
    """

def help(method: Optional[str] = None) -> None:
    """
    Provides help for the notebookutils.udf module or the specified method.

    Examples:
    notebookutils.udf.help()
    notebookutils.udf.help("getFunctions")
    :param method: The name of the method to get help with.
    """
