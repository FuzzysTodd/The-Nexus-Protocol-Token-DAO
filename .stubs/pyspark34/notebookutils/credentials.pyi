from typing import Any, Optional

__all__ = ['help', 'getToken', 'getSecret', 'putSecret', 'isValidToken']

def help(method_name: Optional[str] = None) -> None:
    """
    Provides help for the notebookutils.credentials module or the specified method.

    Examples:
    notebookutils.credentials.help()
    notebookutils.credentials.help("getToken")
    :param method_name: The name of the method to get help with.
    """

def getToken(audience: str) -> str:
    """
    Gets a token for the given audience.
    
    :param audience: The audience for the token
    :return: The token
    """

def getSecret(akvName: str, secret: str) -> str:
    """
    Gets a secret from the given Azure Key Vault.
    
    :param akvName: The name of the Azure Key Vault
    :param secret: The name of the secret
    :return: The secret value
    """

def putSecret(akvName: str, secretName: str, secretValue: str) -> str:
    """
    Puts a secret in the given Azure Key Vault.
    
    :param akvName: The name of the Azure Key Vault
    :param secretName: The name of the secret
    :param secretValue: The value of the secret
    :return: The secret value
    """

def isValidToken(token: str) -> bool:
    """
    Checks if the given token is valid.
    
    :param token: The token to check
    :return: True if the token is valid
    """
