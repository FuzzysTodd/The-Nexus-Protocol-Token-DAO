from _typeshed import Incomplete

string_types: Incomplete

class BaseClient:
    @staticmethod
    def encode_saml_assertion(assertion): ...
    CLIENT_ASSERTION_TYPE_JWT: str
    CLIENT_ASSERTION_TYPE_SAML2: str
    client_assertion_encoders: Incomplete
    @property
    def session(self): ...
    @session.setter
    def session(self, value) -> None: ...
    configuration: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    client_assertion: Incomplete
    default_headers: Incomplete
    default_body: Incomplete
    logger: Incomplete
    def __init__(self, server_configuration: dict, client_id: str, http_client: Incomplete | None = None, client_secret: Optional[str] = None, client_assertion: Union[bytes, callable, None] = None, client_assertion_type: Optional[str] = None, default_headers: Optional[dict] = None, default_body: Optional[dict] = None, verify: Union[str, True, False, None] = None, proxies: Optional[dict] = None, timeout: Union[tuple, float, None] = None) -> None:
        '''Initialize a client object to talk all the OAuth2 grants to the server.

        Args:
            server_configuration (dict):
                It contains the configuration (i.e. metadata) of the auth server.
                The actual content typically contains keys like
                "authorization_endpoint", "token_endpoint", etc..
                Based on RFC 8414 (https://tools.ietf.org/html/rfc8414),
                you can probably fetch it online from either
                https://example.com/.../.well-known/oauth-authorization-server
                or
                https://example.com/.../.well-known/openid-configuration
            client_id (str): The client\'s id, issued by the authorization server

            http_client (http.HttpClient):
                Your implementation of abstract class :class:`http.HttpClient`.
                Defaults to a requests session instance.

                There is no session-wide `timeout` parameter defined here.
                Timeout behavior is determined by the actual http client you use.
                If you happen to use Requests, it disallows session-wide timeout
                (https://github.com/psf/requests/issues/3341). The workaround is:

                    s = requests.Session()
                    s.request = functools.partial(s.request, timeout=3)

                and then feed that patched session instance to this class.

            client_secret (str):  Triggers HTTP AUTH for Confidential Client
            client_assertion (bytes, callable):
                The client assertion to authenticate this client, per RFC 7521.
                It can be a raw SAML2 assertion (we will base64 encode it for you),
                or a raw JWT assertion in bytes (which we will relay to http layer).
                It can also be a callable (recommended),
                so that we will do lazy creation of an assertion.
            client_assertion_type (str):
                The type of your :attr:`client_assertion` parameter.
                It is typically the value of :attr:`CLIENT_ASSERTION_TYPE_SAML2` or
                :attr:`CLIENT_ASSERTION_TYPE_JWT`, the only two defined in RFC 7521.
            default_headers (dict):
                A dict to be sent in each request header.
                It is not required by OAuth2 specs, but you may use it for telemetry.
            default_body (dict):
                A dict to be sent in each token request body. For example,
                you could choose to set this as {"client_secret": "your secret"}
                if your authorization server wants it to be in the request body
                (rather than in the request header).

            verify (boolean):
                It will be passed to the
                `verify parameter in the underlying requests library
                <http://docs.python-requests.org/en/v2.9.1/user/advanced/#ssl-cert-verification>`_.
                When leaving it with default value (None), we will use True instead.

                This does not apply if you have chosen to pass your own Http client.

            proxies (dict):
                It will be passed to the
                `proxies parameter in the underlying requests library
                <http://docs.python-requests.org/en/v2.9.1/user/advanced/#proxies>`_.

                This does not apply if you have chosen to pass your own Http client.

            timeout (object):
                It will be passed to the
                `timeout parameter in the underlying requests library
                <http://docs.python-requests.org/en/v2.9.1/user/advanced/#timeouts>`_.

                This does not apply if you have chosen to pass your own Http client.

        '''
    def obtain_token_by_refresh_token(self, refresh_token, scope: Incomplete | None = None, **kwargs):
        """Obtain an access token via a refresh token.

        :param refresh_token: The refresh token issued to the client
        :param scope: If omitted, is treated as equal to the scope originally
            granted by the resource owner,
            according to https://tools.ietf.org/html/rfc6749#section-6
        """

class Client(BaseClient):
    """This is the main API for oauth2 client.

    Its methods define and document parameters mentioned in OAUTH2 RFC 6749.
    """
    DEVICE_FLOW: Incomplete
    DEVICE_FLOW_RETRIABLE_ERRORS: Incomplete
    GRANT_TYPE_SAML2: str
    GRANT_TYPE_JWT: str
    grant_assertion_encoders: Incomplete
    def initiate_device_flow(self, scope: list = None, **kwargs: dict) -> dict:
        """Initiate a device flow.

        Returns the data defined in Device Flow specs.
        https://tools.ietf.org/html/draft-ietf-oauth-device-flow-12#section-3.2

        You should then orchestrate the User Interaction as defined in here
        https://tools.ietf.org/html/draft-ietf-oauth-device-flow-12#section-3.3

        And possibly here
        https://tools.ietf.org/html/draft-ietf-oauth-device-flow-12#section-3.3.1
        """
    def obtain_token_by_device_flow(self, flow, exit_condition=..., **kwargs):
        '''Obtain token by a device flow object, with customizable polling effect.

        Args:
            flow (dict):
                An object previously generated by initiate_device_flow(...).
                Its content WILL BE CHANGED by this method during each run.
                We share this object with you, so that you could implement
                your own loop, should you choose to do so.

            exit_condition (Callable):
                This method implements a loop to provide polling effect.
                The loop\'s exit condition is calculated by this callback.

                The default callback makes the loop run until the flow expires.
                Therefore, one of the ways to exit the polling early,
                is to change the flow["expires_at"] to a small number such as 0.

                In case you are doing async programming, you may want to
                completely turn off the loop. You can do so by using a callback as:

                    exit_condition = lambda flow: True

                to make the loop run only once, i.e. no polling, hence non-block.
        '''
    def build_auth_request_uri(self, response_type, redirect_uri: Incomplete | None = None, scope: Incomplete | None = None, state: Incomplete | None = None, **kwargs):
        """Generate an authorization uri to be visited by resource owner.

        Parameters are the same as another method :func:`initiate_auth_code_flow()`,
        whose functionality is a superset of this method.

        :return: The auth uri as a string.
        """
    def initiate_auth_code_flow(self, scope: Incomplete | None = None, redirect_uri: Incomplete | None = None, state: Incomplete | None = None, **kwargs):
        '''Initiate an auth code flow.

        Later when the response reaches your redirect_uri,
        you can use :func:`~obtain_token_by_auth_code_flow()`
        to complete the authentication/authorization.

        This method also provides PKCE protection automatically.

        :param list scope:
            It is a list of case-sensitive strings.
            Some ID provider can accept empty string to represent default scope.
        :param str redirect_uri:
            Optional. If not specified, server will use the pre-registered one.
        :param str state:
            An opaque value used by the client to
            maintain state between the request and callback.
            If absent, this library will automatically generate one internally.
        :param kwargs: Other parameters, typically defined in OpenID Connect.

        :return:
            The auth code flow. It is a dict in this form::

                {
                    "auth_uri": "https://...",  // Guide user to visit this
                    "state": "...",  // You may choose to verify it by yourself,
                                     // or just let obtain_token_by_auth_code_flow()
                                     // do that for you.
                    "...": "...",  // Everything else are reserved and internal
                }

            The caller is expected to::

            1. somehow store this content, typically inside the current session,
            2. guide the end user (i.e. resource owner) to visit that auth_uri,
            3. and then relay this dict and subsequent auth response to
               :func:`~obtain_token_by_auth_code_flow()`.
        '''
    def obtain_token_by_auth_code_flow(self, auth_code_flow, auth_response, scope: Incomplete | None = None, **kwargs):
        '''With the auth_response being redirected back,
        validate it against auth_code_flow, and then obtain tokens.

        Internally, it implements PKCE to mitigate the auth code interception attack.

        :param dict auth_code_flow:
            The same dict returned by :func:`~initiate_auth_code_flow()`.
        :param dict auth_response:
            A dict based on query string received from auth server.

        :param scope:
            You don\'t usually need to use scope parameter here.
            Some Identity Provider allows you to provide
            a subset of what you specified during :func:`~initiate_auth_code_flow`.
        :type scope: collections.Iterable[str]

        :return:
            * A dict containing "access_token" and/or "id_token", among others,
              depends on what scope was used.
              (See https://tools.ietf.org/html/rfc6749#section-5.1)
            * A dict containing "error", optionally "error_description", "error_uri".
              (It is either `this <https://tools.ietf.org/html/rfc6749#section-4.1.2.1>`_
              or `that <https://tools.ietf.org/html/rfc6749#section-5.2>`_
            * Most client-side data error would result in ValueError exception.
              So the usage pattern could be without any protocol details::

                def authorize():  # A controller in a web app
                    try:
                        result = client.obtain_token_by_auth_code_flow(
                            session.get("flow", {}), auth_resp)
                        if "error" in result:
                            return render_template("error.html", result)
                        store_tokens()
                    except ValueError:  # Usually caused by CSRF
                        pass  # Simply ignore them
                    return redirect(url_for("index"))
        '''
    def obtain_token_by_browser(self, redirect_uri: Incomplete | None = None, auth_code_receiver: Incomplete | None = None, **kwargs):
        '''A native app can use this method to obtain token via a local browser.

        Internally, it implements PKCE to mitigate the auth code interception attack.

        :param scope: A list of scopes that you would like to obtain token for.
        :type scope: collections.Iterable[str]

        :param extra_scope_to_consent:
            Some IdP allows you to include more scopes for end user to consent.
            The access token returned by this method will NOT include those scopes,
            but the refresh token would record those extra consent,
            so that your future :func:`~obtain_token_by_refresh_token()` call
            would be able to obtain token for those additional scopes, silently.
        :type scope: collections.Iterable[str]

        :param string redirect_uri:
            The redirect_uri to be sent via auth request to Identity Provider (IdP),
            to indicate where an auth response would come back to.
            Such as ``http://127.0.0.1:0`` (default) or ``http://localhost:1234``.

            If port 0 is specified, this method will choose a system-allocated port,
            then the actual redirect_uri will contain that port.
            To use this behavior, your IdP would need to accept such dynamic port.

            Per HTTP convention, if port number is absent, it would mean port 80,
            although you probably want to specify port 0 in this context.

        :param dict auth_params:
            These parameters will be sent to authorization_endpoint.

        :param int timeout: In seconds. None means wait indefinitely.

        :param str browser_name:
            If you did
            ``webbrowser.register("xyz", None, BackgroundBrowser("/path/to/browser"))``
            beforehand, you can pass in the name "xyz" to use that browser.
            The default value ``None`` means using default browser,
            which is customizable by env var $BROWSER.

        :return: Same as :func:`~obtain_token_by_auth_code_flow()`
        '''
    @staticmethod
    def parse_auth_response(params, state: Incomplete | None = None):
        """Parse the authorization response being redirected back.

        :param params: A string or dict of the query string
        :param state: REQUIRED if the state parameter was present in the client
            authorization request. This function will compare it with response.
        """
    def obtain_token_by_authorization_code(self, code, redirect_uri: Incomplete | None = None, scope: Incomplete | None = None, **kwargs):
        '''Get a token via authorization code. a.k.a. Authorization Code Grant.

        This is typically used by a server-side app (Confidential Client),
        but it can also be used by a device-side native app (Public Client).
        See more detail at https://tools.ietf.org/html/rfc6749#section-4.1.3

        You are encouraged to use its higher level method
        :func:`~obtain_token_by_auth_code_flow` instead.

        :param code: The authorization code received from authorization server.
        :param redirect_uri:
            Required, if the "redirect_uri" parameter was included in the
            authorization request, and their values MUST be identical.
        :param scope:
            It is both unnecessary and harmless to use scope here, per RFC 6749.
            We suggest to use the same scope already used in auth request uri,
            so that this library can link the obtained tokens with their scope.
        '''
    def obtain_token_by_username_password(self, username, password, scope: Incomplete | None = None, **kwargs):
        """The Resource Owner Password Credentials Grant, used by legacy app."""
    def obtain_token_for_client(self, scope: Incomplete | None = None, **kwargs):
        """Obtain token for this client (rather than for an end user),
        a.k.a. the Client Credentials Grant, used by Backend Applications.

        We don't name it obtain_token_by_client_credentials(...) because those
        credentials are typically already provided in class constructor, not here.
        You can still explicitly provide an optional client_secret parameter,
        or you can provide such extra parameters as `default_body` during the
        class initialization.
        """
    on_obtaining_tokens: Incomplete
    on_removing_rt: Incomplete
    on_updating_rt: Incomplete
    def __init__(self, server_configuration, client_id, on_obtaining_tokens=..., on_removing_rt=..., on_updating_rt=..., **kwargs) -> None: ...
    def obtain_token_by_refresh_token(self, token_item, scope: Incomplete | None = None, rt_getter=..., on_removing_rt: Incomplete | None = None, on_updating_rt: Incomplete | None = None, **kwargs):
        """This is an overload which will trigger token storage callbacks.

        :param token_item:
            A refresh token (RT) item, in flexible format. It can be a string,
            or a whatever data structure containing RT string and its metadata,
            in such case the `rt_getter` callable must be able to
            extract the RT string out from the token item data structure.

            Either way, this token_item will be passed into other callbacks as-is.

        :param scope: If omitted, is treated as equal to the scope originally
            granted by the resource owner,
            according to https://tools.ietf.org/html/rfc6749#section-6
        :param rt_getter: A callable to translate the token_item to a raw RT string
        :param on_removing_rt: If absent, fall back to the one defined in initialization

        :param on_updating_rt:
            Default to None, it will fall back to the one defined in initialization.
            This is the most common case.

            As a special case, you can pass in a False,
            then this function will NOT trigger on_updating_rt() for RT UPDATE,
            instead it will allow the RT to be added by on_obtaining_tokens().
            This behavior is useful when you are migrating RTs from elsewhere
            into a token storage managed by this library.
        """
    def obtain_token_by_assertion(self, assertion, grant_type, scope: Incomplete | None = None, **kwargs):
        """This method implements Assertion Framework for OAuth2 (RFC 7521).
        See details at https://tools.ietf.org/html/rfc7521#section-4.1

        :param assertion:
            The assertion bytes can be a raw SAML2 assertion, or a JWT assertion.
        :param grant_type:
            It is typically either the value of :attr:`GRANT_TYPE_SAML2`,
            or :attr:`GRANT_TYPE_JWT`, the only two profiles defined in RFC 7521.
        :param scope: Optional. It must be a subset of previously granted scopes.
        """
