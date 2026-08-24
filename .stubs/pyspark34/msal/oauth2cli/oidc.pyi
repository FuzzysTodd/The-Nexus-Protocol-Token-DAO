from . import oauth2 as oauth2
from _typeshed import Incomplete

def decode_part(raw, encoding: str = 'utf-8'):
    '''Decode a part of the JWT.

    JWT is encoded by padding-less base64url,
    based on `JWS specs <https://tools.ietf.org/html/rfc7515#appendix-C>`_.

    :param encoding:
        If you are going to decode the first 2 parts of a JWT, i.e. the header
        or the payload, the default value "utf-8" would work fine.
        If you are going to decode the last part i.e. the signature part,
        it is a binary string so you should use `None` as encoding here.
    '''
base64decode = decode_part

def decode_id_token(id_token, client_id: Incomplete | None = None, issuer: Incomplete | None = None, nonce: Incomplete | None = None, now: Incomplete | None = None):
    '''Decodes and validates an id_token and returns its claims as a dictionary.

    ID token claims would at least contain: "iss", "sub", "aud", "exp", "iat",
    per `specs <https://openid.net/specs/openid-connect-core-1_0.html#IDToken>`_
    and it may contain other optional content such as "preferred_username",
    `maybe more <https://openid.net/specs/openid-connect-core-1_0.html#Claims>`_
    '''

class Prompt:
    """This class defines the constant strings for prompt parameter.

    The values are based on
    https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest
    """
    NONE: str
    LOGIN: str
    CONSENT: str
    SELECT_ACCOUNT: str
    CREATE: str

class Client(oauth2.Client):
    """OpenID Connect is a layer on top of the OAuth2.

    See its specs at https://openid.net/connect/
    """
    def decode_id_token(self, id_token, nonce: Incomplete | None = None):
        """See :func:`~decode_id_token`."""
    def build_auth_request_uri(self, response_type, nonce: Incomplete | None = None, **kwargs):
        """Generate an authorization uri to be visited by resource owner.

        Return value and all other parameters are the same as
        :func:`oauth2.Client.build_auth_request_uri`, plus new parameter(s):

        :param nonce:
            A hard-to-guess string used to mitigate replay attacks. See also
            `OIDC specs <https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest>`_.
        """
    def obtain_token_by_authorization_code(self, code, nonce: Incomplete | None = None, **kwargs):
        """Get a token via authorization code. a.k.a. Authorization Code Grant.

        Return value and all other parameters are the same as
        :func:`oauth2.Client.obtain_token_by_authorization_code`,
        plus new parameter(s):

        :param nonce:
            If you provided a nonce when calling :func:`build_auth_request_uri`,
            same nonce should also be provided here, so that we'll validate it.
            An exception will be raised if the nonce in id token mismatches.
        """
    def initiate_auth_code_flow(self, scope: Incomplete | None = None, **kwargs):
        '''Initiate an auth code flow.

        It provides nonce protection automatically.

        :param list scope:
            A list of strings, e.g. ["profile", "email", ...].
            This method will automatically send ["openid"] to the wire,
            although it won\'t modify your input list.

        See :func:`oauth2.Client.initiate_auth_code_flow` in parent class
        for descriptions on other parameters and return value.
        '''
    def obtain_token_by_auth_code_flow(self, auth_code_flow, auth_response, **kwargs):
        """Validate the auth_response being redirected back, and then obtain tokens,
        including ID token which can be used for user sign in.

        Internally, it implements nonce to mitigate replay attack.
        It also implements PKCE to mitigate the auth code interception attack.

        See :func:`oauth2.Client.obtain_token_by_auth_code_flow` in parent class
        for descriptions on other parameters and return value.
        """
    def obtain_token_by_browser(self, display: Incomplete | None = None, prompt: Incomplete | None = None, max_age: Incomplete | None = None, ui_locales: Incomplete | None = None, id_token_hint: Incomplete | None = None, login_hint: Incomplete | None = None, acr_values: Incomplete | None = None, **kwargs):
        """A native app can use this method to obtain token via a local browser.

        Internally, it implements nonce to mitigate replay attack.
        It also implements PKCE to mitigate the auth code interception attack.

        :param string display: Defined in
            `OIDC <https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest>`_.
        :param string prompt: Defined in
            `OIDC <https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest>`_.
            You can find the valid string values defined in :class:`oidc.Prompt`.

        :param int max_age: Defined in
            `OIDC <https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest>`_.
        :param string ui_locales: Defined in
            `OIDC <https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest>`_.
        :param string id_token_hint: Defined in
            `OIDC <https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest>`_.
        :param string login_hint: Defined in
            `OIDC <https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest>`_.
        :param string acr_values: Defined in
            `OIDC <https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest>`_.

        See :func:`oauth2.Client.obtain_token_by_browser` in parent class
        for descriptions on other parameters and return value.
        """
