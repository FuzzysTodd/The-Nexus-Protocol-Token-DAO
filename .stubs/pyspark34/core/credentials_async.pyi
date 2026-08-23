from .credentials import AccessToken as _AccessToken
from types import TracebackType
from typing import Any, AsyncContextManager, Type
from typing_extensions import Protocol

class AsyncTokenCredential(AsyncContextManager['AsyncTokenCredential'], Protocol):
    """Protocol for classes able to provide OAuth tokens."""
    async def get_token(self, *scopes: str, claims: str | None = None, tenant_id: str | None = None, **kwargs: Any) -> _AccessToken:
        """Request an access token for `scopes`.

        :param str scopes: The type of access needed.

        :keyword str claims: Additional claims required in the token, such as those returned in a resource
            provider's claims challenge following an authorization failure.
        :keyword str tenant_id: Optional tenant to include in the token request.
        :keyword bool enable_cae: Indicates whether to enable Continuous Access Evaluation (CAE) for the requested
            token. Defaults to False.

        :rtype: AccessToken
        :return: An AccessToken instance containing the token string and its expiration time in Unix time.
        """
    async def close(self) -> None: ...
    async def __aexit__(self, exc_type: Type[BaseException] | None = None, exc_value: BaseException | None = None, traceback: TracebackType | None = None) -> None: ...
