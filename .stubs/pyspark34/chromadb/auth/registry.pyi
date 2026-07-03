from _typeshed import Incomplete
from chromadb.auth import ClientAuthConfigurationProvider as ClientAuthConfigurationProvider, ClientAuthCredentialsProvider as ClientAuthCredentialsProvider, ClientAuthProtocolAdapter as ClientAuthProtocolAdapter, ClientAuthProvider as ClientAuthProvider, ServerAuthConfigurationProvider as ServerAuthConfigurationProvider, ServerAuthCredentialsProvider as ServerAuthCredentialsProvider, ServerAuthProvider as ServerAuthProvider
from chromadb.utils import get_class as get_class
from typing import Callable, Type

logger: Incomplete
ProviderTypes: Incomplete

def register_classes_from_package(package_name: str) -> None: ...
def register_provider(short_hand: str) -> Callable[[Type[ProviderTypes]], Type[ProviderTypes]]: ...
def resolve_provider(class_or_name: str, cls: Type[ProviderTypes]) -> Type[ProviderTypes]: ...
