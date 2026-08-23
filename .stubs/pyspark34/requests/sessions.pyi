import time
from ._internal_utils import to_native_string as to_native_string
from .adapters import HTTPAdapter as HTTPAdapter
from .compat import Mapping as Mapping, cookielib as cookielib, urljoin as urljoin, urlparse as urlparse
from .cookies import RequestsCookieJar as RequestsCookieJar, cookiejar_from_dict as cookiejar_from_dict, extract_cookies_to_jar as extract_cookies_to_jar, merge_cookies as merge_cookies
from .exceptions import ChunkedEncodingError as ChunkedEncodingError, ContentDecodingError as ContentDecodingError, InvalidSchema as InvalidSchema, TooManyRedirects as TooManyRedirects
from .hooks import default_hooks as default_hooks, dispatch_hook as dispatch_hook
from .models import DEFAULT_REDIRECT_LIMIT as DEFAULT_REDIRECT_LIMIT, PreparedRequest as PreparedRequest, REDIRECT_STATI as REDIRECT_STATI, Request as Request
from .status_codes import codes as codes
from .structures import CaseInsensitiveDict as CaseInsensitiveDict
from .utils import DEFAULT_PORTS as DEFAULT_PORTS, default_headers as default_headers, get_auth_from_url as get_auth_from_url, get_environ_proxies as get_environ_proxies, get_netrc_auth as get_netrc_auth, requote_uri as requote_uri, resolve_proxies as resolve_proxies, rewind_body as rewind_body, should_bypass_proxies as should_bypass_proxies, to_key_val_list as to_key_val_list
from _typeshed import Incomplete
from collections.abc import Generator

preferred_clock = time.time

def merge_setting(request_setting, session_setting, dict_class=...):
    """Determines appropriate setting for a given request, taking into account
    the explicit setting on that request, and the setting in the session. If a
    setting is a dictionary, they will be merged together using `dict_class`
    """
def merge_hooks(request_hooks, session_hooks, dict_class=...):
    """Properly merges both requests and session hooks.

    This is necessary because when request_hooks == {'response': []}, the
    merge breaks Session hooks entirely.
    """

class SessionRedirectMixin:
    def get_redirect_target(self, resp):
        """Receives a Response. Returns a redirect URI or ``None``"""
    def should_strip_auth(self, old_url, new_url):
        """Decide whether Authorization header should be removed when redirecting"""
    def resolve_redirects(self, resp, req, stream: bool = False, timeout: Incomplete | None = None, verify: bool = True, cert: Incomplete | None = None, proxies: Incomplete | None = None, yield_requests: bool = False, **adapter_kwargs) -> Generator[Incomplete, None, None]:
        """Receives a Response. Returns a generator of Responses or Requests."""
    def rebuild_auth(self, prepared_request, response) -> None:
        """When being redirected we may want to strip authentication from the
        request to avoid leaking credentials. This method intelligently removes
        and reapplies authentication where possible to avoid credential loss.
        """
    def rebuild_proxies(self, prepared_request, proxies):
        """This method re-evaluates the proxy configuration by considering the
        environment variables. If we are redirected to a URL covered by
        NO_PROXY, we strip the proxy configuration. Otherwise, we set missing
        proxy keys for this URL (in case they were stripped by a previous
        redirect).

        This method also replaces the Proxy-Authorization header where
        necessary.

        :rtype: dict
        """
    def rebuild_method(self, prepared_request, response) -> None:
        """When being redirected we may want to change the method of the request
        based on certain specs or browser behavior.
        """

class Session(SessionRedirectMixin):
    """A Requests session.

    Provides cookie persistence, connection-pooling, and configuration.

    Basic Usage::

      >>> import requests
      >>> s = requests.Session()
      >>> s.get('https://httpbin.org/get')
      <Response [200]>

    Or as a context manager::

      >>> with requests.Session() as s:
      ...     s.get('https://httpbin.org/get')
      <Response [200]>
    """
    __attrs__: Incomplete
    headers: Incomplete
    auth: Incomplete
    proxies: Incomplete
    hooks: Incomplete
    params: Incomplete
    stream: bool
    verify: bool
    cert: Incomplete
    max_redirects: Incomplete
    trust_env: bool
    cookies: Incomplete
    adapters: Incomplete
    def __init__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def prepare_request(self, request):
        """Constructs a :class:`PreparedRequest <PreparedRequest>` for
        transmission and returns it. The :class:`PreparedRequest` has settings
        merged from the :class:`Request <Request>` instance and those of the
        :class:`Session`.

        :param request: :class:`Request` instance to prepare with this
            session's settings.
        :rtype: requests.PreparedRequest
        """
    def request(self, method, url, params: Incomplete | None = None, data: Incomplete | None = None, headers: Incomplete | None = None, cookies: Incomplete | None = None, files: Incomplete | None = None, auth: Incomplete | None = None, timeout: Incomplete | None = None, allow_redirects: bool = True, proxies: Incomplete | None = None, hooks: Incomplete | None = None, stream: Incomplete | None = None, verify: Incomplete | None = None, cert: Incomplete | None = None, json: Incomplete | None = None):
        """Constructs a :class:`Request <Request>`, prepares it and sends it.
        Returns :class:`Response <Response>` object.

        :param method: method for the new :class:`Request` object.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary or bytes to be sent in the query
            string for the :class:`Request`.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the
            :class:`Request`.
        :param headers: (optional) Dictionary of HTTP Headers to send with the
            :class:`Request`.
        :param cookies: (optional) Dict or CookieJar object to send with the
            :class:`Request`.
        :param files: (optional) Dictionary of ``'filename': file-like-objects``
            for multipart encoding upload.
        :param auth: (optional) Auth tuple or callable to enable
            Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float, or a :ref:`(connect timeout,
            read timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        :param allow_redirects: (optional) Set to True by default.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol or protocol and
            hostname to the URL of the proxy.
        :param stream: (optional) whether to immediately download the response
            content. Defaults to ``False``.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to ``True``. When set to
            ``False``, requests will accept any TLS certificate presented by
            the server, and will ignore hostname mismatches and/or expired
            certificates, which will make your application vulnerable to
            man-in-the-middle (MitM) attacks. Setting verify to ``False``
            may be useful during local development or testing.
        :param cert: (optional) if String, path to ssl client cert file (.pem).
            If Tuple, ('cert', 'key') pair.
        :rtype: requests.Response
        """
    def get(self, url, **kwargs):
        """Sends a GET request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \\*\\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
    def options(self, url, **kwargs):
        """Sends a OPTIONS request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \\*\\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
    def head(self, url, **kwargs):
        """Sends a HEAD request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \\*\\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
    def post(self, url, data: Incomplete | None = None, json: Incomplete | None = None, **kwargs):
        """Sends a POST request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json to send in the body of the :class:`Request`.
        :param \\*\\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
    def put(self, url, data: Incomplete | None = None, **kwargs):
        """Sends a PUT request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \\*\\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
    def patch(self, url, data: Incomplete | None = None, **kwargs):
        """Sends a PATCH request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param \\*\\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
    def delete(self, url, **kwargs):
        """Sends a DELETE request. Returns :class:`Response` object.

        :param url: URL for the new :class:`Request` object.
        :param \\*\\*kwargs: Optional arguments that ``request`` takes.
        :rtype: requests.Response
        """
    def send(self, request, **kwargs):
        """Send a given PreparedRequest.

        :rtype: requests.Response
        """
    def merge_environment_settings(self, url, proxies, stream, verify, cert):
        """
        Check the environment and merge it with some settings.

        :rtype: dict
        """
    def get_adapter(self, url):
        """
        Returns the appropriate connection adapter for the given URL.

        :rtype: requests.adapters.BaseAdapter
        """
    def close(self) -> None:
        """Closes all adapters and as such the session"""
    def mount(self, prefix, adapter) -> None:
        """Registers a connection adapter to a prefix.

        Adapters are sorted in descending order by prefix length.
        """

def session():
    """
    Returns a :class:`Session` for context-management.

    .. deprecated:: 1.0.0

        This method has been deprecated since version 1.0.0 and is only kept for
        backwards compatibility. New code should use :class:`~requests.sessions.Session`
        to create a session. This may be removed at a future date.

    :rtype: Session
    """
