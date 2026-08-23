from tornado import escape as escape, httpclient as httpclient
from tornado.httputil import url_concat as url_concat
from tornado.util import unicode_type as unicode_type
from tornado.web import RequestHandler as RequestHandler
from typing import Any, Dict, List

class AuthError(Exception): ...

class OpenIdMixin:
    """Abstract implementation of OpenID and Attribute Exchange.

    Class attributes:

    * ``_OPENID_ENDPOINT``: the identity provider's URI.
    """
    def authenticate_redirect(self, callback_uri: str | None = None, ax_attrs: List[str] = ['name', 'email', 'language', 'username']) -> None:
        """Redirects to the authentication URL for this service.

        After authentication, the service will redirect back to the given
        callback URI with additional parameters including ``openid.mode``.

        We request the given attributes for the authenticated user by
        default (name, email, language, and username). If you don't need
        all those attributes for your app, you can request fewer with
        the ax_attrs keyword argument.

        .. versionchanged:: 6.0

            The ``callback`` argument was removed and this method no
            longer returns an awaitable object. It is now an ordinary
            synchronous function.
        """
    async def get_authenticated_user(self, http_client: httpclient.AsyncHTTPClient | None = None) -> Dict[str, Any]:
        """Fetches the authenticated user data upon redirect.

        This method should be called by the handler that receives the
        redirect from the `authenticate_redirect()` method (which is
        often the same as the one that calls it; in that case you would
        call `get_authenticated_user` if the ``openid.mode`` parameter
        is present and `authenticate_redirect` if it is not).

        The result of this method will generally be used to set a cookie.

        .. versionchanged:: 6.0

            The ``callback`` argument was removed. Use the returned
            awaitable object instead.
        """
    def get_auth_http_client(self) -> httpclient.AsyncHTTPClient:
        """Returns the `.AsyncHTTPClient` instance to be used for auth requests.

        May be overridden by subclasses to use an HTTP client other than
        the default.
        """

class OAuthMixin:
    '''Abstract implementation of OAuth 1.0 and 1.0a.

    See `TwitterMixin` below for an example implementation.

    Class attributes:

    * ``_OAUTH_AUTHORIZE_URL``: The service\'s OAuth authorization url.
    * ``_OAUTH_ACCESS_TOKEN_URL``: The service\'s OAuth access token url.
    * ``_OAUTH_VERSION``: May be either "1.0" or "1.0a".
    * ``_OAUTH_NO_CALLBACKS``: Set this to True if the service requires
      advance registration of callbacks.

    Subclasses must also override the `_oauth_get_user_future` and
    `_oauth_consumer_token` methods.
    '''
    async def authorize_redirect(self, callback_uri: str | None = None, extra_params: Dict[str, Any] | None = None, http_client: httpclient.AsyncHTTPClient | None = None) -> None:
        """Redirects the user to obtain OAuth authorization for this service.

        The ``callback_uri`` may be omitted if you have previously
        registered a callback URI with the third-party service. For
        some services, you must use a previously-registered callback
        URI and cannot specify a callback via this method.

        This method sets a cookie called ``_oauth_request_token`` which is
        subsequently used (and cleared) in `get_authenticated_user` for
        security purposes.

        This method is asynchronous and must be called with ``await``
        or ``yield`` (This is different from other ``auth*_redirect``
        methods defined in this module). It calls
        `.RequestHandler.finish` for you so you should not write any
        other response after it returns.

        .. versionchanged:: 3.1
           Now returns a `.Future` and takes an optional callback, for
           compatibility with `.gen.coroutine`.

        .. versionchanged:: 6.0

           The ``callback`` argument was removed. Use the returned
           awaitable object instead.

        """
    async def get_authenticated_user(self, http_client: httpclient.AsyncHTTPClient | None = None) -> Dict[str, Any]:
        """Gets the OAuth authorized user and access token.

        This method should be called from the handler for your
        OAuth callback URL to complete the registration process. We run the
        callback with the authenticated user dictionary.  This dictionary
        will contain an ``access_key`` which can be used to make authorized
        requests to this service on behalf of the user.  The dictionary will
        also contain other fields such as ``name``, depending on the service
        used.

        .. versionchanged:: 6.0

           The ``callback`` argument was removed. Use the returned
           awaitable object instead.
        """
    def get_auth_http_client(self) -> httpclient.AsyncHTTPClient:
        """Returns the `.AsyncHTTPClient` instance to be used for auth requests.

        May be overridden by subclasses to use an HTTP client other than
        the default.
        """

class OAuth2Mixin:
    """Abstract implementation of OAuth 2.0.

    See `FacebookGraphMixin` or `GoogleOAuth2Mixin` below for example
    implementations.

    Class attributes:

    * ``_OAUTH_AUTHORIZE_URL``: The service's authorization url.
    * ``_OAUTH_ACCESS_TOKEN_URL``:  The service's access token url.
    """
    def authorize_redirect(self, redirect_uri: str | None = None, client_id: str | None = None, client_secret: str | None = None, extra_params: Dict[str, Any] | None = None, scope: List[str] | None = None, response_type: str = 'code') -> None:
        """Redirects the user to obtain OAuth authorization for this service.

        Some providers require that you register a redirect URL with
        your application instead of passing one via this method. You
        should call this method to log the user in, and then call
        ``get_authenticated_user`` in the handler for your
        redirect URL to complete the authorization process.

        .. versionchanged:: 6.0

           The ``callback`` argument and returned awaitable were removed;
           this is now an ordinary synchronous function.
        """
    async def oauth2_request(self, url: str, access_token: str | None = None, post_args: Dict[str, Any] | None = None, **args: Any) -> Any:
        '''Fetches the given URL auth an OAuth2 access token.

        If the request is a POST, ``post_args`` should be provided. Query
        string arguments should be given as keyword arguments.

        Example usage:

        ..testcode::

            class MainHandler(tornado.web.RequestHandler,
                              tornado.auth.FacebookGraphMixin):
                @tornado.web.authenticated
                async def get(self):
                    new_entry = await self.oauth2_request(
                        "https://graph.facebook.com/me/feed",
                        post_args={"message": "I am posting from my Tornado application!"},
                        access_token=self.current_user["access_token"])

                    if not new_entry:
                        # Call failed; perhaps missing permission?
                        self.authorize_redirect()
                        return
                    self.finish("Posted a message!")

        .. testoutput::
           :hide:

        .. versionadded:: 4.3

        .. versionchanged::: 6.0

           The ``callback`` argument was removed. Use the returned awaitable object instead.
        '''
    def get_auth_http_client(self) -> httpclient.AsyncHTTPClient:
        """Returns the `.AsyncHTTPClient` instance to be used for auth requests.

        May be overridden by subclasses to use an HTTP client other than
        the default.

        .. versionadded:: 4.3
        """

class TwitterMixin(OAuthMixin):
    '''Twitter OAuth authentication.

    To authenticate with Twitter, register your application with
    Twitter at http://twitter.com/apps. Then copy your Consumer Key
    and Consumer Secret to the application
    `~tornado.web.Application.settings` ``twitter_consumer_key`` and
    ``twitter_consumer_secret``. Use this mixin on the handler for the
    URL you registered as your application\'s callback URL.

    When your application is set up, you can use this mixin like this
    to authenticate the user with Twitter and get access to their stream:

    .. testcode::

        class TwitterLoginHandler(tornado.web.RequestHandler,
                                  tornado.auth.TwitterMixin):
            async def get(self):
                if self.get_argument("oauth_token", None):
                    user = await self.get_authenticated_user()
                    # Save the user using e.g. set_signed_cookie()
                else:
                    await self.authorize_redirect()

    .. testoutput::
       :hide:

    The user object returned by `~OAuthMixin.get_authenticated_user`
    includes the attributes ``username``, ``name``, ``access_token``,
    and all of the custom Twitter user attributes described at
    https://dev.twitter.com/docs/api/1.1/get/users/show
    '''
    async def authenticate_redirect(self, callback_uri: str | None = None) -> None:
        """Just like `~OAuthMixin.authorize_redirect`, but
        auto-redirects if authorized.

        This is generally the right interface to use if you are using
        Twitter for single-sign on.

        .. versionchanged:: 3.1
           Now returns a `.Future` and takes an optional callback, for
           compatibility with `.gen.coroutine`.

        .. versionchanged:: 6.0

           The ``callback`` argument was removed. Use the returned
           awaitable object instead.
        """
    async def twitter_request(self, path: str, access_token: Dict[str, Any], post_args: Dict[str, Any] | None = None, **args: Any) -> Any:
        '''Fetches the given API path, e.g., ``statuses/user_timeline/btaylor``

        The path should not include the format or API version number.
        (we automatically use JSON format and API version 1).

        If the request is a POST, ``post_args`` should be provided. Query
        string arguments should be given as keyword arguments.

        All the Twitter methods are documented at http://dev.twitter.com/

        Many methods require an OAuth access token which you can
        obtain through `~OAuthMixin.authorize_redirect` and
        `~OAuthMixin.get_authenticated_user`. The user returned through that
        process includes an \'access_token\' attribute that can be used
        to make authenticated requests via this method. Example
        usage:

        .. testcode::

            class MainHandler(tornado.web.RequestHandler,
                              tornado.auth.TwitterMixin):
                @tornado.web.authenticated
                async def get(self):
                    new_entry = await self.twitter_request(
                        "/statuses/update",
                        post_args={"status": "Testing Tornado Web Server"},
                        access_token=self.current_user["access_token"])
                    if not new_entry:
                        # Call failed; perhaps missing permission?
                        await self.authorize_redirect()
                        return
                    self.finish("Posted a message!")

        .. testoutput::
           :hide:

        .. versionchanged:: 6.0

           The ``callback`` argument was removed. Use the returned
           awaitable object instead.
        '''

class GoogleOAuth2Mixin(OAuth2Mixin):
    '''Google authentication using OAuth2.

    In order to use, register your application with Google and copy the
    relevant parameters to your application settings.

    * Go to the Google Dev Console at http://console.developers.google.com
    * Select a project, or create a new one.
    * In the sidebar on the left, select Credentials.
    * Click CREATE CREDENTIALS and click OAuth client ID.
    * Under Application type, select Web application.
    * Name OAuth 2.0 client and click Create.
    * Copy the "Client secret" and "Client ID" to the application settings as
      ``{"google_oauth": {"key": CLIENT_ID, "secret": CLIENT_SECRET}}``

    .. versionadded:: 3.2
    '''
    def get_google_oauth_settings(self) -> Dict[str, str]:
        '''Return the Google OAuth 2.0 credentials that you created with
        [Google Cloud
        Platform](https://console.cloud.google.com/apis/credentials). The dict
        format is::

            {
                "key": "your_client_id", "secret": "your_client_secret"
            }

        If your credentials are stored differently (e.g. in a db) you can
        override this method for custom provision.
        '''
    async def get_authenticated_user(self, redirect_uri: str, code: str, client_id: str | None = None, client_secret: str | None = None) -> Dict[str, Any]:
        '''Handles the login for the Google user, returning an access token.

        The result is a dictionary containing an ``access_token`` field
        ([among others](https://developers.google.com/identity/protocols/OAuth2WebServer#handlingtheresponse)).
        Unlike other ``get_authenticated_user`` methods in this package,
        this method does not return any additional information about the user.
        The returned access token can be used with `OAuth2Mixin.oauth2_request`
        to request additional information (perhaps from
        ``https://www.googleapis.com/oauth2/v2/userinfo``)

        Example usage:

        .. testcode::

            class GoogleOAuth2LoginHandler(tornado.web.RequestHandler,
                                           tornado.auth.GoogleOAuth2Mixin):
                async def get(self):
                    if self.get_argument(\'code\', False):
                        access = await self.get_authenticated_user(
                            redirect_uri=\'http://your.site.com/auth/google\',
                            code=self.get_argument(\'code\'))
                        user = await self.oauth2_request(
                            "https://www.googleapis.com/oauth2/v1/userinfo",
                            access_token=access["access_token"])
                        # Save the user and access token with
                        # e.g. set_signed_cookie.
                    else:
                        self.authorize_redirect(
                            redirect_uri=\'http://your.site.com/auth/google\',
                            client_id=self.get_google_oauth_settings()[\'key\'],
                            scope=[\'profile\', \'email\'],
                            response_type=\'code\',
                            extra_params={\'approval_prompt\': \'auto\'})

        .. testoutput::
           :hide:

        .. versionchanged:: 6.0

           The ``callback`` argument was removed. Use the returned awaitable object instead.
        '''

class FacebookGraphMixin(OAuth2Mixin):
    """Facebook authentication using the new Graph API and OAuth2."""
    async def get_authenticated_user(self, redirect_uri: str, client_id: str, client_secret: str, code: str, extra_fields: Dict[str, Any] | None = None) -> Dict[str, Any] | None:
        '''Handles the login for the Facebook user, returning a user object.

        Example usage:

        .. testcode::

            class FacebookGraphLoginHandler(tornado.web.RequestHandler,
                                            tornado.auth.FacebookGraphMixin):
              async def get(self):
                  if self.get_argument("code", False):
                      user = await self.get_authenticated_user(
                          redirect_uri=\'/auth/facebookgraph/\',
                          client_id=self.settings["facebook_api_key"],
                          client_secret=self.settings["facebook_secret"],
                          code=self.get_argument("code"))
                      # Save the user with e.g. set_signed_cookie
                  else:
                      self.authorize_redirect(
                          redirect_uri=\'/auth/facebookgraph/\',
                          client_id=self.settings["facebook_api_key"],
                          extra_params={"scope": "read_stream,offline_access"})

        .. testoutput::
           :hide:

        This method returns a dictionary which may contain the following fields:

        * ``access_token``, a string which may be passed to `facebook_request`
        * ``session_expires``, an integer encoded as a string representing
          the time until the access token expires in seconds. This field should
          be used like ``int(user[\'session_expires\'])``; in a future version of
          Tornado it will change from a string to an integer.
        * ``id``, ``name``, ``first_name``, ``last_name``, ``locale``, ``picture``,
          ``link``, plus any fields named in the ``extra_fields`` argument. These
          fields are copied from the Facebook graph API
          `user object <https://developers.facebook.com/docs/graph-api/reference/user>`_

        .. versionchanged:: 4.5
           The ``session_expires`` field was updated to support changes made to the
           Facebook API in March 2017.

        .. versionchanged:: 6.0

           The ``callback`` argument was removed. Use the returned awaitable object instead.
        '''
    async def facebook_request(self, path: str, access_token: str | None = None, post_args: Dict[str, Any] | None = None, **args: Any) -> Any:
        '''Fetches the given relative API path, e.g., "/btaylor/picture"

        If the request is a POST, ``post_args`` should be provided. Query
        string arguments should be given as keyword arguments.

        An introduction to the Facebook Graph API can be found at
        http://developers.facebook.com/docs/api

        Many methods require an OAuth access token which you can
        obtain through `~OAuth2Mixin.authorize_redirect` and
        `get_authenticated_user`. The user returned through that
        process includes an ``access_token`` attribute that can be
        used to make authenticated requests via this method.

        Example usage:

        .. testcode::

            class MainHandler(tornado.web.RequestHandler,
                              tornado.auth.FacebookGraphMixin):
                @tornado.web.authenticated
                async def get(self):
                    new_entry = await self.facebook_request(
                        "/me/feed",
                        post_args={"message": "I am posting from my Tornado application!"},
                        access_token=self.current_user["access_token"])

                    if not new_entry:
                        # Call failed; perhaps missing permission?
                        self.authorize_redirect()
                        return
                    self.finish("Posted a message!")

        .. testoutput::
           :hide:

        The given path is relative to ``self._FACEBOOK_BASE_URL``,
        by default "https://graph.facebook.com".

        This method is a wrapper around `OAuth2Mixin.oauth2_request`;
        the only difference is that this method takes a relative path,
        while ``oauth2_request`` takes a complete url.

        .. versionchanged:: 3.1
           Added the ability to override ``self._FACEBOOK_BASE_URL``.

        .. versionchanged:: 6.0

           The ``callback`` argument was removed. Use the returned awaitable object instead.
        '''
