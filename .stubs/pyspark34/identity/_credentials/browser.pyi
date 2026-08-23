from .. import CredentialUnavailableError as CredentialUnavailableError
from .._constants import DEVELOPER_SIGN_ON_CLIENT_ID as DEVELOPER_SIGN_ON_CLIENT_ID
from .._internal import AuthCodeRedirectServer as AuthCodeRedirectServer, InteractiveCredential as InteractiveCredential, within_dac as within_dac, wrap_exceptions as wrap_exceptions
from typing import Any

class InteractiveBrowserCredential(InteractiveCredential):
    '''Opens a browser to interactively authenticate a user.

    :func:`~get_token` opens a browser to a login URL provided by Azure Active Directory and authenticates a user
    there with the authorization code flow, using PKCE (Proof Key for Code Exchange) internally to protect the code.

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example "login.microsoftonline.com",
        the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
        defines authorities for other clouds.
    :keyword str tenant_id: an Azure Active Directory tenant ID. Defaults to the "organizations" tenant, which can
        authenticate work or school accounts.
    :keyword str client_id: Client ID of the Azure Active Directory application users will sign in to. If
        unspecified, users will authenticate to an Azure development application.
    :keyword str login_hint: a username suggestion to pre-fill the login page\'s username/email address field. A user
        may still log in with a different username.
    :keyword str redirect_uri: a redirect URI for the application identified by `client_id` as configured in Azure
        Active Directory, for example "http://localhost:8400". This is only required when passing a value for
        **client_id**, and must match a redirect URI in the application\'s registration. The credential must be able to
        bind a socket to this URI.
    :keyword AuthenticationRecord authentication_record: :class:`AuthenticationRecord` returned by :func:`authenticate`
    :keyword bool disable_automatic_authentication: if True, :func:`get_token` will raise
        :class:`AuthenticationRequiredError` when user interaction is required to acquire a token. Defaults to False.
    :keyword cache_persistence_options: configuration for persistent token caching. If unspecified, the credential
        will cache tokens in memory.
    :paramtype cache_persistence_options: ~azure.identity.TokenCachePersistenceOptions
    :keyword int timeout: seconds to wait for the user to complete authentication. Defaults to 300 (5 minutes).
    :keyword bool disable_instance_discovery: Determines whether or not instance discovery is performed when attempting
        to authenticate. Setting this to true will completely disable both instance discovery and authority validation.
        This functionality is intended for use in scenarios where the metadata endpoint cannot be reached, such as in
        private clouds or Azure Stack. The process of instance discovery entails retrieving authority metadata from
        https://login.microsoft.com/ to validate the authority. By setting this to **True**, the validation of the
        authority is disabled. As a result, it is crucial to ensure that the configured authority host is valid and
        trustworthy.
    :raises ValueError: invalid **redirect_uri**

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_interactive_browser_credential]
            :end-before: [END create_interactive_browser_credential]
            :language: python
            :dedent: 4
            :caption: Create an InteractiveBrowserCredential.
    '''
    def __init__(self, **kwargs: Any) -> None: ...
