from typing import Any, Optional
from notebookutils.mssparkutils.handlers import VariableLibrary

__all__ = ['get', 'help', 'getLibrary']


def get(variableReference: str) -> Any:
    """
    Get a variable value from the variable library.
    
    :param variableReference: Reference to the variable
    :return: Variable value
    """

def help(method: Optional[str] = None) -> None:
    """
    Provides help for the notebookutils.variableLibrary module or the specified method.

    Examples:
    notebookutils.variableLibrary.help()
    notebookutils.variableLibrary.help("get")
    :param method: The name of the method to get help with.
    """

def getLibrary(variableLibraryName: str) -> VariableLibrary:
    """
    Get a variable library instance.
    
    :param variableLibraryName: Name of the variable library
    :return: VariableLibrary instance
    """
