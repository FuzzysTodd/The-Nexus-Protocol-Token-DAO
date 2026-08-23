import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from chromadb.config import Component as Component, System as System
from chromadb.errors import ChromaError as ChromaError
from enum import Enum
from overrides import EnforceOverrides
from pydantic import SecretStr
from typing import Dict, Generic, Tuple, TypeVar

logger: Incomplete
T = TypeVar('T')
S = TypeVar('S')

class AuthInfoType(Enum):
    COOKIE: str
    HEADER: str
    URL: str
    METADATA: str

class ClientAuthResponse(EnforceOverrides, ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def get_auth_info_type(self) -> AuthInfoType: ...
    @abstractmethod
    def get_auth_info(self) -> Tuple[str, SecretStr]: ...

class ClientAuthProvider(Component, metaclass=abc.ABCMeta):
    def __init__(self, system: System) -> None: ...
    @abstractmethod
    def authenticate(self) -> ClientAuthResponse: ...

class ClientAuthConfigurationProvider(Component, metaclass=abc.ABCMeta):
    def __init__(self, system: System) -> None: ...
    @abstractmethod
    def get_configuration(self) -> T | None: ...

class ClientAuthCredentialsProvider(Component, Generic[T], metaclass=abc.ABCMeta):
    def __init__(self, system: System) -> None: ...
    @abstractmethod
    def get_credentials(self) -> T: ...

class ClientAuthProtocolAdapter(Component, Generic[T], metaclass=abc.ABCMeta):
    def __init__(self, system: System) -> None: ...
    @abstractmethod
    def inject_credentials(self, injection_context: T) -> None: ...

class ServerAuthenticationRequest(EnforceOverrides, ABC, Generic[T], metaclass=abc.ABCMeta):
    @abstractmethod
    def get_auth_info(self, auth_info_type: AuthInfoType, auth_info_id: str | None = None) -> T:
        """
        This method should return the necessary auth info based on the type of authentication (e.g. header, cookie, url)
         and a given id for the respective auth type (e.g. name of the header, cookie, url param).

        :param auth_info_type: The type of auth info to return
        :param auth_info_id: The id of the auth info to return
        :return: The auth info which can be specific to the implementation
        """

class ServerAuthenticationResponse(EnforceOverrides, ABC):
    def success(self) -> bool: ...

class ServerAuthProvider(Component, metaclass=abc.ABCMeta):
    def __init__(self, system: System) -> None: ...
    @abstractmethod
    def authenticate(self, request: ServerAuthenticationRequest[T]) -> bool: ...

class ChromaAuthMiddleware(Component, metaclass=abc.ABCMeta):
    def __init__(self, system: System) -> None: ...
    @abstractmethod
    def authenticate(self, request: ServerAuthenticationRequest[T]) -> ServerAuthenticationResponse | None: ...
    @abstractmethod
    def ignore_operation(self, verb: str, path: str) -> bool: ...
    @abstractmethod
    def instrument_server(self, app: T) -> None: ...

class ServerAuthConfigurationProvider(Component, metaclass=abc.ABCMeta):
    def __init__(self, system: System) -> None: ...
    @abstractmethod
    def get_configuration(self) -> T | None: ...

class AuthenticationError(ChromaError):
    def code(self) -> int: ...
    @classmethod
    def name(cls) -> str: ...

class AbstractCredentials(EnforceOverrides, ABC, Generic[T], metaclass=abc.ABCMeta):
    """
    The class is used by Auth Providers to encapsulate credentials received from the server
    and pass them to a ServerAuthCredentialsProvider.
    """
    @abstractmethod
    def get_credentials(self) -> Dict[str, T]:
        """
        Returns the data encapsulated by the credentials object.
        """

class SecretStrAbstractCredentials(AbstractCredentials[SecretStr], metaclass=abc.ABCMeta):
    @abstractmethod
    def get_credentials(self) -> Dict[str, SecretStr]:
        """
        Returns the data encapsulated by the credentials object.
        """

class BasicAuthCredentials(SecretStrAbstractCredentials):
    username: Incomplete
    password: Incomplete
    def __init__(self, username: SecretStr, password: SecretStr) -> None: ...
    def get_credentials(self) -> Dict[str, SecretStr]: ...
    @staticmethod
    def from_header(header: str) -> BasicAuthCredentials:
        """
        Parses a basic auth header and returns a BasicAuthCredentials object.
        """

class ServerAuthCredentialsProvider(Component, metaclass=abc.ABCMeta):
    def __init__(self, system: System) -> None: ...
    @abstractmethod
    def validate_credentials(self, credentials: AbstractCredentials[T]) -> bool: ...
