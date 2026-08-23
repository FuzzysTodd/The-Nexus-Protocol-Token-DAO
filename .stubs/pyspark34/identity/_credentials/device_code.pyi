from .._constants import DEVELOPER_SIGN_ON_CLIENT_ID as DEVELOPER_SIGN_ON_CLIENT_ID
from .._internal import InteractiveCredential as InteractiveCredential, wrap_exceptions as wrap_exceptions
from datetime import datetime
from typing import Any, Callable

class DeviceCodeCredential(InteractiveCredential):
    '''Authenticates users through the device code flow.

    When :func:`get_token` is called, this credential acquires a verification URL and code from Azure Active Directory.
    A user must browse to the URL, enter the code, and authenticate with Azure Active Directory. If the user
    authenticates successfully, the credential receives an access token.

    This credential is primarily useful for authenticating a user in an environment without a web browser, such as an
    SSH session. If a web browser is available, :class:`~azure.identity.InteractiveBrowserCredential` is more
    convenient because it automatically opens a browser to the login page.

    :param str client_id: client ID of the application users will authenticate to. When not specified users will
        authenticate to an Azure development application.

    :keyword str authority: Authority of an Azure Active Directory endpoint, for example "login.microsoftonline.com",
        the authority for Azure Public Cloud (which is the default). :class:`~azure.identity.AzureAuthorityHosts`
        defines authorities for other clouds.
    :keyword str tenant_id: an Azure Active Directory tenant ID. Defaults to the "organizations" tenant, which can
        authenticate work or school accounts. **Required for single-tenant applications.**
    :keyword int timeout: seconds to wait for the user to authenticate. Defaults to the validity period of the
        device code as set by Azure Active Directory, which also prevails when **timeout** is longer.
    :keyword prompt_callback: A callback enabling control of how authentication
        instructions are presented. Must accept arguments (``verification_uri``, ``user_code``, ``expires_on``):

        - ``verification_uri`` (str) the URL the user must visit
        - ``user_code`` (str) the code the user must enter there
        - ``expires_on`` (datetime.datetime) the UTC time at which the code will expire
        If this argument isn\'t provided, the credential will print instructions to stdout.
    :paramtype prompt_callback: Callable[str, str, ~datetime.datetime]
    :keyword AuthenticationRecord authentication_record: :class:`AuthenticationRecord` returned by :func:`authenticate`
    :keyword bool disable_automatic_authentication: if True, :func:`get_token` will raise
        :class:`AuthenticationRequiredError` when user interaction is required to acquire a token. Defaults to False.
    :keyword cache_persistence_options: configuration for persistent token caching. If unspecified, the credential
        will cache tokens in memory.
    :paramtype cache_persistence_options: ~azure.identity.TokenCachePersistenceOptions
    :keyword bool disable_instance_discovery: Determines whether or not instance discovery is performed when attempting
        to authenticate. Setting this to true will completely disable both instance discovery and authority validation.
        This functionality is intended for use in scenarios where the metadata endpoint cannot be reached, such as in
        private clouds or Azure Stack. The process of instance discovery entails retrieving authority metadata from
        https://login.microsoft.com/ to validate the authority. By setting this to **True**, the validation of the
        authority is disabled. As a result, it is crucial to ensure that the configured authority host is valid and
        trustworthy.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_device_code_credential]
            :end-before: [END create_device_code_credential]
            :language: python
            :dedent: 4
            :caption: Create a DeviceCodeCredential.
    '''
    def __init__(self, client_id: str = ..., *, timeout: int | None = None, prompt_callback: Callable[[str, str, datetime], None] | None = None, **kwargs: Any) -> None: ...
