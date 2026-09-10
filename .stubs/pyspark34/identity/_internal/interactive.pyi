import abc
from .._auth_record import AuthenticationRecord as AuthenticationRecord
from .._constants import KnownAuthorities as KnownAuthorities
from .._exceptions import AuthenticationRequiredError as AuthenticationRequiredError, CredentialUnavailableError as CredentialUnavailableError
from .._internal import wrap_exceptions as wrap_exceptions
from .msal_credentials import MsalCredential as MsalCredential
from azure.core.credentials import AccessToken
from typing import Any

ABC = abc.ABC

class InteractiveCredential(MsalCredential, ABC, metaclass=abc.ABCMeta):
    def __init__(self, *, authentication_record: AuthenticationRecord | None = None, disable_automatic_authentication: bool = False, **kwargs: Any) -> None: ...
    def get_token(self, *scopes: str, claims: str | None = None, tenant_id: str | None = None, **kwargs: Any) -> AccessToken:
        """Request an access token for `scopes`.

        This method is called automatically by Azure SDK clients.

        :param str scopes: desired scopes for the access token. This method requires at least one scope.
            For more information about scopes, see
            https://learn.microsoft.com/azure/active-directory/develop/scopes-oidc.
        :keyword str claims: additional claims required in the token, such as those returned in a resource provider's
            claims challenge following an authorization failure
        :keyword str tenant_id: optional tenant to include in the token request.
        :keyword bool enable_cae: indicates whether to enable Continuous Access Evaluation (CAE) for the requested
            token. Defaults to False.
        :return: An access token with the desired scopes.
        :rtype: ~azure.core.credentials.AccessToken
        :raises CredentialUnavailableError: the credential is unable to attempt authentication because it lacks
            required data, state, or platform support
        :raises ~azure.core.exceptions.ClientAuthenticationError: authentication failed. The error's ``message``
            attribute gives a reason.
        :raises AuthenticationRequiredError: user interaction is necessary to acquire a token, and the credential is
            configured not to begin this automatically. Call :func:`authenticate` to begin interactive authentication.
        """
    def authenticate(self, **kwargs: Any) -> AuthenticationRecord:
        """Interactively authenticate a user.

        :keyword Iterable[str] scopes: scopes to request during authentication, such as those provided by
          :func:`AuthenticationRequiredError.scopes`. If provided, successful authentication will cache an access token
          for these scopes.
        :keyword str claims: additional claims required in the token, such as those provided by
          :func:`AuthenticationRequiredError.claims`
        :rtype: ~azure.identity.AuthenticationRecord
        :raises ~azure.core.exceptions.ClientAuthenticationError: authentication failed. The error's ``message``
          attribute gives a reason.
        """
