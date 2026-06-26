from . import certs as certs
from .__version__ import __version__ as __version__
from ._internal_utils import HEADER_VALIDATORS as HEADER_VALIDATORS, to_native_string as to_native_string
from .compat import Mapping as Mapping, basestring as basestring, bytes as bytes, getproxies as getproxies, getproxies_environment as getproxies_environment, integer_types as integer_types, proxy_bypass as proxy_bypass, proxy_bypass_environment as proxy_bypass_environment, quote as quote, str as str, unquote as unquote, urlparse as urlparse, urlunparse as urlunparse
from .cookies import cookiejar_from_dict as cookiejar_from_dict
from .exceptions import FileModeWarning as FileModeWarning, InvalidHeader as InvalidHeader, InvalidURL as InvalidURL, UnrewindableBodyError as UnrewindableBodyError
from .structures import CaseInsensitiveDict as CaseInsensitiveDict
from _typeshed import Incomplete
from collections.abc import Generator

NETRC_FILES: Incomplete
DEFAULT_CA_BUNDLE_PATH: Incomplete
DEFAULT_PORTS: Incomplete
DEFAULT_ACCEPT_ENCODING: Incomplete

def dict_to_sequence(d):
    """Returns an internal sequence dictionary update."""
def super_len(o): ...
def get_netrc_auth(url, raise_errors: bool = False):
    """Returns the Requests tuple auth for a given url from netrc."""
def guess_filename(obj):
    """Tries to guess the filename of the given object."""
def extract_zipped_paths(path):
    """Replace nonexistent paths that look like they refer to a member of a zip
    archive with the location of an extracted copy of the target, or else
    just return the provided path unchanged.
    """
def atomic_open(filename) -> Generator[Incomplete, None, None]:
    """Write a file to the disk in an atomic fashion"""
def from_key_val_list(value):
    """Take an object and test to see if it can be represented as a
    dictionary. Unless it can not be represented as such, return an
    OrderedDict, e.g.,

    ::

        >>> from_key_val_list([('key', 'val')])
        OrderedDict([('key', 'val')])
        >>> from_key_val_list('string')
        Traceback (most recent call last):
        ...
        ValueError: cannot encode objects that are not 2-tuples
        >>> from_key_val_list({'key': 'val'})
        OrderedDict([('key', 'val')])

    :rtype: OrderedDict
    """
def to_key_val_list(value):
    """Take an object and test to see if it can be represented as a
    dictionary. If it can be, return a list of tuples, e.g.,

    ::

        >>> to_key_val_list([('key', 'val')])
        [('key', 'val')]
        >>> to_key_val_list({'key': 'val'})
        [('key', 'val')]
        >>> to_key_val_list('string')
        Traceback (most recent call last):
        ...
        ValueError: cannot encode objects that are not 2-tuples

    :rtype: list
    """
def parse_list_header(value):
    '''Parse lists as described by RFC 2068 Section 2.

    In particular, parse comma-separated lists where the elements of
    the list may include quoted-strings.  A quoted-string could
    contain a comma.  A non-quoted string could have quotes in the
    middle.  Quotes are removed automatically after parsing.

    It basically works like :func:`parse_set_header` just that items
    may appear multiple times and case sensitivity is preserved.

    The return value is a standard :class:`list`:

    >>> parse_list_header(\'token, "quoted value"\')
    [\'token\', \'quoted value\']

    To create a header from the :class:`list` again, use the
    :func:`dump_header` function.

    :param value: a string with a list header.
    :return: :class:`list`
    :rtype: list
    '''
def parse_dict_header(value):
    '''Parse lists of key, value pairs as described by RFC 2068 Section 2 and
    convert them into a python dict:

    >>> d = parse_dict_header(\'foo="is a fish", bar="as well"\')
    >>> type(d) is dict
    True
    >>> sorted(d.items())
    [(\'bar\', \'as well\'), (\'foo\', \'is a fish\')]

    If there is no value for a key it will be `None`:

    >>> parse_dict_header(\'key_without_value\')
    {\'key_without_value\': None}

    To create a header from the :class:`dict` again, use the
    :func:`dump_header` function.

    :param value: a string with a dict header.
    :return: :class:`dict`
    :rtype: dict
    '''
def unquote_header_value(value, is_filename: bool = False):
    """Unquotes a header value.  (Reversal of :func:`quote_header_value`).
    This does not use the real unquoting but what browsers are actually
    using for quoting.

    :param value: the header value to unquote.
    :rtype: str
    """
def dict_from_cookiejar(cj):
    """Returns a key/value dictionary from a CookieJar.

    :param cj: CookieJar object to extract cookies from.
    :rtype: dict
    """
def add_dict_to_cookiejar(cj, cookie_dict):
    """Returns a CookieJar from a key/value dictionary.

    :param cj: CookieJar to insert cookies into.
    :param cookie_dict: Dict of key/values to insert into CookieJar.
    :rtype: CookieJar
    """
def get_encodings_from_content(content):
    """Returns encodings from given content string.

    :param content: bytestring to extract encodings from.
    """
def get_encoding_from_headers(headers):
    """Returns encodings from given HTTP Header Dict.

    :param headers: dictionary to extract encoding from.
    :rtype: str
    """
def stream_decode_response_unicode(iterator, r) -> Generator[Incomplete, Incomplete, None]:
    """Stream decodes an iterator."""
def iter_slices(string, slice_length) -> Generator[Incomplete, None, None]:
    """Iterate over slices of a string."""
def get_unicode_from_response(r):
    """Returns the requested content back in unicode.

    :param r: Response object to get unicode content from.

    Tried:

    1. charset from content-type
    2. fall back and replace all unicode characters

    :rtype: str
    """

UNRESERVED_SET: Incomplete

def unquote_unreserved(uri):
    """Un-escape any percent-escape sequences in a URI that are unreserved
    characters. This leaves all reserved, illegal and non-ASCII bytes encoded.

    :rtype: str
    """
def requote_uri(uri):
    """Re-quote the given URI.

    This function passes the given URI through an unquote/quote cycle to
    ensure that it is fully and consistently quoted.

    :rtype: str
    """
def address_in_network(ip, net):
    """This function allows you to check if an IP belongs to a network subnet

    Example: returns True if ip = 192.168.1.1 and net = 192.168.1.0/24
             returns False if ip = 192.168.1.1 and net = 192.168.100.0/24

    :rtype: bool
    """
def dotted_netmask(mask):
    """Converts mask from /xx format to xxx.xxx.xxx.xxx

    Example: if mask is 24 function returns 255.255.255.0

    :rtype: str
    """
def is_ipv4_address(string_ip):
    """
    :rtype: bool
    """
def is_valid_cidr(string_network):
    """
    Very simple check of the cidr format in no_proxy variable.

    :rtype: bool
    """
def set_environ(env_name, value) -> Generator[None, None, None]:
    """Set the environment variable 'env_name' to 'value'

    Save previous value, yield, and then restore the previous value stored in
    the environment variable 'env_name'.

    If 'value' is None, do nothing"""
def should_bypass_proxies(url, no_proxy):
    """
    Returns whether we should bypass proxies or not.

    :rtype: bool
    """
def get_environ_proxies(url, no_proxy: Incomplete | None = None):
    """
    Return a dict of environment proxies.

    :rtype: dict
    """
def select_proxy(url, proxies):
    """Select a proxy for the url, if applicable.

    :param url: The url being for the request
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
    """
def resolve_proxies(request, proxies, trust_env: bool = True):
    """This method takes proxy information from a request and configuration
    input to resolve a mapping of target proxies. This will consider settings
    such a NO_PROXY to strip proxy configurations.

    :param request: Request or PreparedRequest
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
    :param trust_env: Boolean declaring whether to trust environment configs

    :rtype: dict
    """
def default_user_agent(name: str = 'python-requests'):
    """
    Return a string representing the default user agent.

    :rtype: str
    """
def default_headers():
    """
    :rtype: requests.structures.CaseInsensitiveDict
    """
def parse_header_links(value):
    '''Return a list of parsed link headers proxies.

    i.e. Link: <http:/.../front.jpeg>; rel=front; type="image/jpeg",<http://.../back.jpeg>; rel=back;type="image/jpeg"

    :rtype: list
    '''
def guess_json_utf(data):
    """
    :rtype: str
    """
def prepend_scheme_if_needed(url, new_scheme):
    """Given a URL that may or may not have a scheme, prepend the given scheme.
    Does not replace a present scheme with the one provided as an argument.

    :rtype: str
    """
def get_auth_from_url(url):
    """Given a url with authentication components, extract them into a tuple of
    username,password.

    :rtype: (str,str)
    """
def check_header_validity(header) -> None:
    """Verifies that header parts don't contain leading whitespace
    reserved characters, or return characters.

    :param header: tuple, in the format (name, value).
    """
def urldefragauth(url):
    """
    Given a url remove the fragment and the authentication part.

    :rtype: str
    """
def rewind_body(prepared_request) -> None:
    """Move file pointer back to its recorded starting position
    so it can be read again on redirect.
    """
