from . import argument as argument, log as log
from .authority import Authority as Authority
from .code_request import CodeRequest as CodeRequest
from .constants import OAuth2DeviceCodeResponseParameters as OAuth2DeviceCodeResponseParameters
from .token_cache import TokenCache as TokenCache
from .token_request import TokenRequest as TokenRequest
from _typeshed import Incomplete

GLOBAL_ADAL_OPTIONS: Incomplete

class AuthenticationContext:
    '''Retrieves authentication tokens from Azure Active Directory.

    For usages, check out the "sample" folder at:
        https://github.com/AzureAD/azure-activedirectory-library-for-python
    '''
    authority: Incomplete
    correlation_id: Incomplete
    cache: Incomplete
    def __init__(self, authority, validate_authority: Incomplete | None = None, cache: Incomplete | None = None, api_version: Incomplete | None = None, timeout: Incomplete | None = None, enable_pii: bool = False, verify_ssl: Incomplete | None = None, proxies: Incomplete | None = None) -> None:
        '''Creates a new AuthenticationContext object.

        By default the authority will be checked against a list of known Azure
        Active Directory authorities. If the authority is not recognized as 
        one of these well known authorities then token acquisition will fail.
        This behavior can be turned off via the validate_authority parameter
        below.

        :param str authority: A URL that identifies a token authority. It should be of the
            format https://login.microsoftonline.com/your_tenant
        :param bool validate_authority: (optional) Turns authority validation 
            on or off. This parameter default to true.
        :param TokenCache cache: (optional) Sets the token cache used by this 
            AuthenticationContext instance. If this parameter is not set, then
            a default is used. Cache instances is only used by that instance of
            the AuthenticationContext and are not shared unless it has been
            manually passed during the construction of other
            AuthenticationContexts.
        :param api_version: (optional) Specifies API version using on the wire.
            Historically it has a hardcoded default value as "1.0".
            Developers have been encouraged to set it as None explicitly,
            which means the underlying API version will be automatically chosen.
            Starting from ADAL Python 1.0, this default value becomes None.
        :param timeout: (optional) requests timeout. How long to wait for the server to send
            data before giving up, as a float, or a `(connect timeout,
            read timeout) <timeouts>` tuple.
        :param enable_pii: (optional) Unless this is set to True,
            there will be no Personally Identifiable Information (PII) written in log.
        :param verify_ssl: (optional) requests verify. Either a boolean, in which case it 
            controls whether we verify the server\'s TLS certificate, or a string, in which 
            case it must be a path to a CA bundle to use. If this value is not provided, and 
            ADAL_PYTHON_SSL_NO_VERIFY env varaible is set, behavior is equivalent to 
            verify_ssl=False.
        :param proxies: (optional) requests proxies. Dictionary mapping protocol to the URL 
            of the proxy. See http://docs.python-requests.org/en/master/user/advanced/#proxies
            for details.
        '''
    @property
    def options(self): ...
    @options.setter
    def options(self, val) -> None: ...
    def acquire_token(self, resource, user_id, client_id):
        '''Gets a token for a given resource via cached tokens.

        :param str resource: A URI that identifies the resource for which the
            token is valid.
        :param str user_id: The username of the user on behalf this application
            is authenticating.
        :param str client_id: The OAuth client id of the calling application.
        :returns: dic with several keys, include "accessToken" and
            "refreshToken".
        '''
    def acquire_token_with_username_password(self, resource, username, password, client_id):
        '''Gets a token for a given resource via user credentails.
        
        :param str resource: A URI that identifies the resource for which the 
            token is valid.
        :param str username: The username of the user on behalf this
            application is authenticating.
        :param str password: The password of the user named in the username
            parameter.
        :param str client_id: The OAuth client id of the calling application.
        :returns: dict with several keys, include "accessToken" and
            "refreshToken".
        '''
    def acquire_token_with_client_credentials(self, resource, client_id, client_secret):
        '''Gets a token for a given resource via client credentials.

        :param str resource: A URI that identifies the resource for which the 
            token is valid.
        :param str client_id: The OAuth client id of the calling application.
        :param str client_secret: The OAuth client secret of the calling application.
        :returns: dict with several keys, include "accessToken".
        '''
    def acquire_token_with_authorization_code(self, authorization_code, redirect_uri, resource, client_id, client_secret: Incomplete | None = None, code_verifier: Incomplete | None = None):
        '''Gets a token for a given resource via authorization code for a
        server app.
        
        :param str authorization_code: An authorization code returned from a
            client.
        :param str redirect_uri: the redirect uri that was used in the
            authorize call.
        :param str resource: A URI that identifies the resource for which the
            token is valid.
        :param str client_id: The OAuth client id of the calling application.
        :param str client_secret: (only for confidential clients)The OAuth
            client secret of the calling application. This parameter if not set,
            defaults to None
        :param str code_verifier: (optional)The code verifier that was used to
            obtain authorization code if PKCE was used in the authorization
            code grant request.(usually used by public clients) This parameter if not set,
            defaults to None
        :returns: dict with several keys, include "accessToken" and
            "refreshToken".
        '''
    def acquire_token_with_refresh_token(self, refresh_token, client_id, resource, client_secret: Incomplete | None = None):
        '''Gets a token for a given resource via refresh tokens
        
        :param str refresh_token: A refresh token returned in a tokne response
            from a previous invocation of acquireToken.
        :param str client_id: The OAuth client id of the calling application.
        :param str resource: A URI that identifies the resource for which the
            token is valid.
        :param str client_secret: (optional)The OAuth client secret of the
            calling application.                 
        :returns: dict with several keys, include "accessToken" and
            "refreshToken".
        '''
    def acquire_token_with_client_certificate(self, resource, client_id, certificate, thumbprint, public_certificate: Incomplete | None = None):
        '''Gets a token for a given resource via certificate credentials

        :param str resource: A URI that identifies the resource for which the
            token is valid.
        :param str client_id: The OAuth client id of the calling application.
        :param str certificate: A PEM encoded certificate private key.
        :param str thumbprint: hex encoded thumbprint of the certificate.
        :param str public_certificate(optional): if not None, it will be sent to the service for subject name
            and issuer based authentication, which is to support cert auto rolls. The value must match the
            certificate private key parameter.

            Per `specs <https://tools.ietf.org/html/rfc7515#section-4.1.6>`_,
            "the certificate containing
            the public key corresponding to the key used to digitally sign the
            JWS MUST be the first certificate.  This MAY be followed by
            additional certificates, with each subsequent certificate being the
            one used to certify the previous one."
            However, your certificate\'s issuer may use a different order.
            So, if your attempt ends up with an error AADSTS700027 -
            "The provided signature value did not match the expected signature value",
            you may try use only the leaf cert (in PEM/str format) instead.

        :returns: dict with several keys, include "accessToken".
        '''
    def acquire_user_code(self, resource, client_id, language: Incomplete | None = None):
        """Gets the user code info which contains user_code, device_code for
        authenticating user on device.
        
        :param str resource: A URI that identifies the resource for which the 
            device_code and user_code is valid for.
        :param str client_id: The OAuth client id of the calling application.
        :param str language: The language code specifying how the message
            should be localized to.
        :returns: dict contains code and uri for users to login through browser.
        """
    def acquire_token_with_device_code(self, resource, user_code_info, client_id):
        '''Gets a new access token using via a device code. 
        
        :param str resource: A URI that identifies the resource for which the
            token is valid.
        :param dict user_code_info: The code info from the invocation of
            "acquire_user_code"
        :param str client_id: The OAuth client id of the calling application.
        :returns: dict with several keys, include "accessToken" and
            "refreshToken".
        '''
    def cancel_request_to_get_token_with_device_code(self, user_code_info) -> None:
        '''Cancels the polling request to get token with device code. 

        :param dict user_code_info: The code info from the invocation of
            "acquire_user_code"
        :returns: None
        '''
