from typing import Any, Optional

__all__ = ['getCredential', 'help']

def getCredential(connection_id: str, artifact_id: str = "") -> Any:
    """
    Retrieve the credential details using data connection id and artifact id.
    
    :param connection_id: The data connection id
    :param artifact_id: The artifact id
    :return: The credential info
    """

def help(method: Optional[str] = None) -> None:
    """
    Provides help for the notebookutils.connections module or the specified method.

    Examples:
    notebookutils.connections.help()
    notebookutils.connections.help("getCredential")
    :param method: The name of the method to get help with.
    """
