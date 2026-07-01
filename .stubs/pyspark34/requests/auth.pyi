from ._internal_utils import to_native_string as to_native_string
from .compat import basestring as basestring, str as str, urlparse as urlparse
from .cookies import extract_cookies_to_jar as extract_cookies_to_jar
from .utils import parse_dict_header as parse_dict_header
from _typeshed import Incomplete

CONTENT_TYPE_FORM_URLENCODED: str
CONTENT_TYPE_MULTI_PART: str

class AuthBase:
    """Base class that all auth implementations derive from"""
    def __call__(self, r) -> None: ...

class HTTPBasicAuth(AuthBase):
    """Attaches HTTP Basic Authentication to the given Request object."""
    username: Incomplete
    password: Incomplete
    def __init__(self, username, password) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __call__(self, r): ...

class HTTPProxyAuth(HTTPBasicAuth):
    """Attaches HTTP Proxy Authentication to a given Request object."""
    def __call__(self, r): ...

class HTTPDigestAuth(AuthBase):
    """Attaches HTTP Digest Authentication to the given Request object."""
    username: Incomplete
    password: Incomplete
    def __init__(self, username, password) -> None: ...
    def init_per_thread_state(self) -> None: ...
    def build_digest_header(self, method, url):
        """
        :rtype: str
        """
    def handle_redirect(self, r, **kwargs) -> None:
        """Reset num_401_calls counter on redirects."""
    def handle_401(self, r, **kwargs):
        """
        Takes the given response and tries digest-auth, if needed.

        :rtype: requests.Response
        """
    def __call__(self, r): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
