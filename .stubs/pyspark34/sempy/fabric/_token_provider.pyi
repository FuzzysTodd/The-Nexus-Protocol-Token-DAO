import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from typing import Callable, Literal

class TokenProvider(ABC, metaclass=abc.ABCMeta):
    """
    Abstract base class for logic that acquires auth tokens.
    """
    @abstractmethod
    def __call__(self, audience: Literal['pbi', 'storage'] = 'pbi') -> str:
        """
        Get implementation specific token.

        Returns
        -------
        str
            Auth token.
        """

class ConstantTokenProvider(TokenProvider):
    """
    Wrapper around a token that was externally acquired by the user.

    Parameters
    ----------
    token : str
        Token that will be supplied upon requst.
    """
    token_dict: Incomplete
    def __init__(self, pbi_token, storage_token: Incomplete | None = None) -> None: ...
    def __call__(self, audience: Literal['pbi', 'storage'] = 'pbi'):
        """
        Get token.

        Returns
        -------
        str
            Fixed token provided by user during instantiation.
        """

class SynapseTokenProvider(TokenProvider):
    """
    Acquire an auth token from within a Trident workspace.
    """
    def __call__(self, audience: Literal['pbi', 'storage'] = 'pbi'):
        """
        Get token from within a Trident workspace.

        Returns
        -------
        str
            Token acquired from Trident libraries.
        """

def create_on_access_token_expired_callback(token_provider: TokenProvider) -> Callable: ...
