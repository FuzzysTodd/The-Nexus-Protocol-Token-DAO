from chromadb.auth import AbstractCredentials, AuthInfoType, ClientAuthProvider, ClientAuthResponse, SecretStrAbstractCredentials, ServerAuthCredentialsProvider, ServerAuthProvider, ServerAuthenticationRequest
from chromadb.config import System
from enum import Enum
from pydantic import SecretStr
from typing import Any, Dict, Tuple, TypeVar

__all__ = ['TokenAuthServerProvider', 'TokenAuthClientProvider']

T = TypeVar('T')

class TokenTransportHeader(Enum):
    AUTHORIZATION: str
    X_CHROMA_TOKEN: str

class TokenAuthClientAuthResponse(ClientAuthResponse):
    def __init__(self, credentials: SecretStr, token_transport_header: TokenTransportHeader = ...) -> None: ...
    def get_auth_info_type(self) -> AuthInfoType: ...
    def get_auth_info(self) -> Tuple[str, SecretStr]: ...

class TokenConfigServerAuthCredentialsProvider(ServerAuthCredentialsProvider):
    def __init__(self, system: System) -> None: ...
    def validate_credentials(self, credentials: AbstractCredentials[T]) -> bool: ...

class TokenAuthCredentials(SecretStrAbstractCredentials):
    def __init__(self, token: SecretStr) -> None: ...
    def get_credentials(self) -> Dict[str, SecretStr]: ...
    @staticmethod
    def from_header(header: str, token_transport_header: TokenTransportHeader = ...) -> TokenAuthCredentials:
        """
        Extracts token from header and returns a TokenAuthCredentials object.
        """

class TokenAuthServerProvider(ServerAuthProvider):
    def __init__(self, system: System) -> None: ...
    def authenticate(self, request: ServerAuthenticationRequest[Any]) -> bool: ...

class TokenAuthClientProvider(ClientAuthProvider):
    def __init__(self, system: System) -> None: ...
    def authenticate(self) -> ClientAuthResponse: ...
