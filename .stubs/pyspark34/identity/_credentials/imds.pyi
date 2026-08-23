from .. import CredentialUnavailableError as CredentialUnavailableError
from .._constants import EnvironmentVariables as EnvironmentVariables
from .._internal.get_token_mixin import GetTokenMixin as GetTokenMixin
from .._internal.managed_identity_client import ManagedIdentityClient as ManagedIdentityClient
from _typeshed import Incomplete
from azure.core.credentials import AccessToken as AccessToken
from typing import Any

IMDS_AUTHORITY: str
IMDS_TOKEN_PATH: str
PIPELINE_SETTINGS: Incomplete

class ImdsCredential(GetTokenMixin):
    def __init__(self, **kwargs: Any) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def close(self) -> None: ...
