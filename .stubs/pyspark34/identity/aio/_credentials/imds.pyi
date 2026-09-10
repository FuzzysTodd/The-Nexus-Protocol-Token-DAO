from ... import CredentialUnavailableError as CredentialUnavailableError
from ..._constants import EnvironmentVariables as EnvironmentVariables
from ..._credentials.imds import PIPELINE_SETTINGS as PIPELINE_SETTINGS
from .._internal import AsyncContextManager as AsyncContextManager
from .._internal.get_token_mixin import GetTokenMixin as GetTokenMixin
from .._internal.managed_identity_client import AsyncManagedIdentityClient as AsyncManagedIdentityClient
from azure.core.credentials import AccessToken as AccessToken
from typing import Any, TypeVar

T = TypeVar('T', bound='ImdsCredential')

class ImdsCredential(AsyncContextManager, GetTokenMixin):
    def __init__(self, **kwargs: Any) -> None: ...
    async def __aenter__(self) -> T: ...
    async def close(self) -> None: ...
