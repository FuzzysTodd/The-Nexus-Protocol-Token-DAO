from ..exceptions import LocationParseError as LocationParseError
from _typeshed import Incomplete

url_attrs: Incomplete
NORMALIZABLE_SCHEMES: Incomplete
PERCENT_RE: Incomplete
SCHEME_RE: Incomplete
URI_RE: Incomplete
IPV4_PAT: str
HEX_PAT: str
LS32_PAT: Incomplete
UNRESERVED_PAT: str
IPV6_PAT: Incomplete
ZONE_ID_PAT: Incomplete
IPV6_ADDRZ_PAT: Incomplete
REG_NAME_PAT: str
TARGET_RE: Incomplete
IPV4_RE: Incomplete
IPV6_RE: Incomplete
IPV6_ADDRZ_RE: Incomplete
BRACELESS_IPV6_ADDRZ_RE: Incomplete
ZONE_ID_RE: Incomplete
UNRESERVED_CHARS: Incomplete
SUB_DELIM_CHARS: Incomplete
USERINFO_CHARS: Incomplete
PATH_CHARS: Incomplete
QUERY_CHARS: Incomplete
FRAGMENT_CHARS: Incomplete

class Url(Incomplete):
    """
    Data structure for representing an HTTP URL. Used as a return value for
    :func:`parse_url`. Both the scheme and host are normalized as they are
    both case-insensitive according to RFC 3986.
    """
    def __new__(cls, scheme: Incomplete | None = None, auth: Incomplete | None = None, host: Incomplete | None = None, port: Incomplete | None = None, path: Incomplete | None = None, query: Incomplete | None = None, fragment: Incomplete | None = None): ...
    @property
    def hostname(self):
        """For backwards-compatibility with urlparse. We're nice like that."""
    @property
    def request_uri(self):
        """Absolute path including the query string."""
    @property
    def netloc(self):
        """Network location including host and port"""
    @property
    def url(self):
        """
        Convert self into a url

        This function should more or less round-trip with :func:`.parse_url`. The
        returned url may not be exactly the same as the url inputted to
        :func:`.parse_url`, but it should be equivalent by the RFC (e.g., urls
        with a blank port will have : removed).

        Example: ::

            >>> U = parse_url('http://google.com/mail/')
            >>> U.url
            'http://google.com/mail/'
            >>> Url('http', 'username:password', 'host.com', 80,
            ... '/path', 'query', 'fragment').url
            'http://username:password@host.com:80/path?query#fragment'
        """

def split_first(s, delims):
    """
    .. deprecated:: 1.25

    Given a string and an iterable of delimiters, split on the first found
    delimiter. Return two split parts and the matched delimiter.

    If not found, then the first part is the full input string.

    Example::

        >>> split_first('foo/bar?baz', '?/=')
        ('foo', 'bar?baz', '/')
        >>> split_first('foo/bar?baz', '123')
        ('foo/bar?baz', '', None)

    Scales linearly with number of delims. Not ideal for large number of delims.
    """
def parse_url(url):
    """
    Given a url, return a parsed :class:`.Url` namedtuple. Best-effort is
    performed to parse incomplete urls. Fields not provided will be None.
    This parser is RFC 3986 and RFC 6874 compliant.

    The parser logic and helper functions are based heavily on
    work done in the ``rfc3986`` module.

    :param str url: URL to parse into a :class:`.Url` namedtuple.

    Partly backwards-compatible with :mod:`urlparse`.

    Example::

        >>> parse_url('http://google.com/mail/')
        Url(scheme='http', host='google.com', port=None, path='/mail/', ...)
        >>> parse_url('google.com:80')
        Url(scheme=None, host='google.com', port=80, path=None, ...)
        >>> parse_url('/foo?bar')
        Url(scheme=None, host=None, port=None, path='/foo', query='bar', ...)
    """
def get_host(url):
    """
    Deprecated. Use :func:`parse_url` instead.
    """
