from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from _typeshed import Incomplete
from urllib import urlencode as urlencode

logger: Incomplete

def obtain_auth_code(listen_port, auth_uri: Incomplete | None = None): ...
def is_wsl(): ...

class _AuthCodeHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None: ...
    def log_message(self, format, *args) -> None: ...

class _AuthCodeHttpServer(HTTPServer):
    allow_reuse_address: bool
    def __init__(self, server_address, *args, **kwargs) -> None: ...
    def handle_timeout(self) -> None: ...

class _AuthCodeHttpServer6(_AuthCodeHttpServer):
    address_family: Incomplete

class AuthCodeReceiver:
    def __init__(self, port: Incomplete | None = None, scheduled_actions: Incomplete | None = None) -> None:
        '''Create a Receiver waiting for incoming auth response.

        :param port:
            The local web server will listen at http://...:<port>
            You need to use the same port when you register with your app.
            If your Identity Provider supports dynamic port, you can use port=0 here.
            Port 0 means to use an arbitrary unused port, per this official example:
            https://docs.python.org/2.7/library/socketserver.html#asynchronous-mixins

        :param scheduled_actions:
            For example, if the input is
            ``[(10, lambda: print("Got stuck during sign in? Call 800-000-0000"))]``
            then the receiver would call that lambda function after
            waiting the response for 10 seconds.
        '''
    def get_port(self):
        """The port this server actually listening to"""
    def get_auth_response(self, timeout: Incomplete | None = None, **kwargs):
        '''Wait and return the auth response. Raise RuntimeError when timeout.

        :param str auth_uri:
            If provided, this function will try to open a local browser.
        :param int timeout: In seconds. None means wait indefinitely.
        :param str state:
            You may provide the state you used in auth_uri,
            then we will use it to validate incoming response.
        :param str welcome_template:
            If provided, your end user will see it instead of the auth_uri.
            When present, it shall be a plaintext or html template following
            `Python Template string syntax <https://docs.python.org/3/library/string.html#template-strings>`_,
            and include some of these placeholders: $auth_uri and $abort_uri.
        :param str success_template:
            The page will be displayed when authentication was largely successful.
            Placeholders can be any of these:
            https://tools.ietf.org/html/rfc6749#section-5.1
        :param str error_template:
            The page will be displayed when authentication encountered error.
            Placeholders can be any of these:
            https://tools.ietf.org/html/rfc6749#section-5.2
        :param callable auth_uri_callback:
            A function with the shape of lambda auth_uri: ...
            When a browser was unable to be launch, this function will be called,
            so that the app could tell user to manually visit the auth_uri.
        :param str browser_name:
            If you did
            ``webbrowser.register("xyz", None, BackgroundBrowser("/path/to/browser"))``
            beforehand, you can pass in the name "xyz" to use that browser.
            The default value ``None`` means using default browser,
            which is customizable by env var $BROWSER.
        :return:
            The auth response of the first leg of Auth Code flow,
            typically {"code": "...", "state": "..."} or {"error": "...", ...}
            See https://tools.ietf.org/html/rfc6749#section-4.1.2
            and https://openid.net/specs/openid-connect-core-1_0.html#AuthResponse
            Returns None when the state was mismatched, or when timeout occurred.
        '''
    def close(self) -> None:
        """Either call this eventually; or use the entire class as context manager"""
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
