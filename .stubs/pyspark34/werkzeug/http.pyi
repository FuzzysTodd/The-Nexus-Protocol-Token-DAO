import typing as t
from . import datastructures as ds
from _typeshed import Incomplete
from _typeshed.wsgi import WSGIEnvironment as WSGIEnvironment
from datetime import date, datetime, timedelta
from enum import Enum
from time import struct_time

HTTP_STATUS_CODES: Incomplete

class COEP(Enum):
    """Cross Origin Embedder Policies"""
    UNSAFE_NONE: str
    REQUIRE_CORP: str

class COOP(Enum):
    """Cross Origin Opener Policies"""
    UNSAFE_NONE: str
    SAME_ORIGIN_ALLOW_POPUPS: str
    SAME_ORIGIN: str

def quote_header_value(value: t.Any, allow_token: bool = True) -> str:
    '''Add double quotes around a header value. If the header contains only ASCII token
    characters, it will be returned unchanged. If the header contains ``"`` or ``\\``
    characters, they will be escaped with an additional ``\\`` character.

    This is the reverse of :func:`unquote_header_value`.

    :param value: The value to quote. Will be converted to a string.
    :param allow_token: Disable to quote the value even if it only has token characters.

    .. versionchanged:: 3.0
        Passing bytes is not supported.

    .. versionchanged:: 3.0
        The ``extra_chars`` parameter is removed.

    .. versionchanged:: 2.3
        The value is quoted if it is the empty string.

    .. versionadded:: 0.5
    '''
def unquote_header_value(value: str) -> str:
    '''Remove double quotes and decode slash-escaped ``"`` and ``\\`` characters in a
    header value.

    This is the reverse of :func:`quote_header_value`.

    :param value: The header value to unquote.

    .. versionchanged:: 3.0
        The ``is_filename`` parameter is removed.
    '''
def dump_options_header(header: str | None, options: t.Mapping[str, t.Any]) -> str:
    '''Produce a header value and ``key=value`` parameters separated by semicolons
    ``;``. For example, the ``Content-Type`` header.

    .. code-block:: python

        dump_options_header("text/html", {"charset": "UTF-8"})
        \'text/html; charset=UTF-8\'

    This is the reverse of :func:`parse_options_header`.

    If a value contains non-token characters, it will be quoted.

    If a value is ``None``, the parameter is skipped.

    In some keys for some headers, a UTF-8 value can be encoded using a special
    ``key*=UTF-8\'\'value`` form, where ``value`` is percent encoded. This function will
    not produce that format automatically, but if a given key ends with an asterisk
    ``*``, the value is assumed to have that form and will not be quoted further.

    :param header: The primary header value.
    :param options: Parameters to encode as ``key=value`` pairs.

    .. versionchanged:: 2.3
        Keys with ``None`` values are skipped rather than treated as a bare key.

    .. versionchanged:: 2.2.3
        If a key ends with ``*``, its value will not be quoted.
    '''
def dump_header(iterable: dict[str, t.Any] | t.Iterable[t.Any]) -> str:
    '''Produce a header value from a list of items or ``key=value`` pairs, separated by
    commas ``,``.

    This is the reverse of :func:`parse_list_header`, :func:`parse_dict_header`, and
    :func:`parse_set_header`.

    If a value contains non-token characters, it will be quoted.

    If a value is ``None``, the key is output alone.

    In some keys for some headers, a UTF-8 value can be encoded using a special
    ``key*=UTF-8\'\'value`` form, where ``value`` is percent encoded. This function will
    not produce that format automatically, but if a given key ends with an asterisk
    ``*``, the value is assumed to have that form and will not be quoted further.

    .. code-block:: python

        dump_header(["foo", "bar baz"])
        \'foo, "bar baz"\'

        dump_header({"foo": "bar baz"})
        \'foo="bar baz"\'

    :param iterable: The items to create a header from.

    .. versionchanged:: 3.0
        The ``allow_token`` parameter is removed.

    .. versionchanged:: 2.2.3
        If a key ends with ``*``, its value will not be quoted.
    '''
def dump_csp_header(header: ds.ContentSecurityPolicy) -> str:
    '''Dump a Content Security Policy header.

    These are structured into policies such as "default-src \'self\';
    script-src \'self\'".

    .. versionadded:: 1.0.0
       Support for Content Security Policy headers was added.

    '''
def parse_list_header(value: str) -> list[str]:
    '''Parse a header value that consists of a list of comma separated items according
    to `RFC 9110 <https://httpwg.org/specs/rfc9110.html#abnf.extension>`__.

    This extends :func:`urllib.request.parse_http_list` to remove surrounding quotes
    from values.

    .. code-block:: python

        parse_list_header(\'token, "quoted value"\')
        [\'token\', \'quoted value\']

    This is the reverse of :func:`dump_header`.

    :param value: The header value to parse.
    '''
def parse_dict_header(value: str) -> dict[str, str | None]:
    '''Parse a list header using :func:`parse_list_header`, then parse each item as a
    ``key=value`` pair.

    .. code-block:: python

        parse_dict_header(\'a=b, c="d, e", f\')
        {"a": "b", "c": "d, e", "f": None}

    This is the reverse of :func:`dump_header`.

    If a key does not have a value, it is ``None``.

    This handles charsets for values as described in
    `RFC 2231 <https://www.rfc-editor.org/rfc/rfc2231#section-3>`__. Only ASCII, UTF-8,
    and ISO-8859-1 charsets are accepted, otherwise the value remains quoted.

    :param value: The header value to parse.

    .. versionchanged:: 3.0
        Passing bytes is not supported.

    .. versionchanged:: 3.0
        The ``cls`` argument is removed.

    .. versionchanged:: 2.3
        Added support for ``key*=charset\'\'value`` encoded items.

    .. versionchanged:: 0.9
       The ``cls`` argument was added.
    '''
def parse_options_header(value: str | None) -> tuple[str, dict[str, str]]:
    '''Parse a header that consists of a value with ``key=value`` parameters separated
    by semicolons ``;``. For example, the ``Content-Type`` header.

    .. code-block:: python

        parse_options_header("text/html; charset=UTF-8")
        (\'text/html\', {\'charset\': \'UTF-8\'})

        parse_options_header("")
        ("", {})

    This is the reverse of :func:`dump_options_header`.

    This parses valid parameter parts as described in
    `RFC 9110 <https://httpwg.org/specs/rfc9110.html#parameter>`__. Invalid parts are
    skipped.

    This handles continuations and charsets as described in
    `RFC 2231 <https://www.rfc-editor.org/rfc/rfc2231#section-3>`__, although not as
    strictly as the RFC. Only ASCII, UTF-8, and ISO-8859-1 charsets are accepted,
    otherwise the value remains quoted.

    Clients may not be consistent in how they handle a quote character within a quoted
    value. The `HTML Standard <https://html.spec.whatwg.org/#multipart-form-data>`__
    replaces it with ``%22`` in multipart form data.
    `RFC 9110 <https://httpwg.org/specs/rfc9110.html#quoted.strings>`__ uses backslash
    escapes in HTTP headers. Both are decoded to the ``"`` character.

    Clients may not be consistent in how they handle non-ASCII characters. HTML
    documents must declare ``<meta charset=UTF-8>``, otherwise browsers may replace with
    HTML character references, which can be decoded using :func:`html.unescape`.

    :param value: The header value to parse.
    :return: ``(value, options)``, where ``options`` is a dict

    .. versionchanged:: 2.3
        Invalid parts, such as keys with no value, quoted keys, and incorrectly quoted
        values, are discarded instead of treating as ``None``.

    .. versionchanged:: 2.3
        Only ASCII, UTF-8, and ISO-8859-1 are accepted for charset values.

    .. versionchanged:: 2.3
        Escaped quotes in quoted values, like ``%22`` and ``\\"``, are handled.

    .. versionchanged:: 2.2
        Option names are always converted to lowercase.

    .. versionchanged:: 2.2
        The ``multiple`` parameter was removed.

    .. versionchanged:: 0.15
        :rfc:`2231` parameter continuations are handled.

    .. versionadded:: 0.5
    '''
@t.overload
def parse_accept_header(value: str | None) -> ds.Accept: ...
@t.overload
def parse_accept_header(value: str | None, cls: type[_TAnyAccept]) -> _TAnyAccept: ...
@t.overload
def parse_cache_control_header(value: str | None, on_update: _t_cc_update, cls: None = None) -> ds.RequestCacheControl: ...
@t.overload
def parse_cache_control_header(value: str | None, on_update: _t_cc_update, cls: type[_TAnyCC]) -> _TAnyCC: ...
@t.overload
def parse_csp_header(value: str | None, on_update: _t_csp_update, cls: None = None) -> ds.ContentSecurityPolicy: ...
@t.overload
def parse_csp_header(value: str | None, on_update: _t_csp_update, cls: type[_TAnyCSP]) -> _TAnyCSP: ...
def parse_set_header(value: str | None, on_update: t.Callable[[ds.HeaderSet], None] | None = None) -> ds.HeaderSet:
    '''Parse a set-like header and return a
    :class:`~werkzeug.datastructures.HeaderSet` object:

    >>> hs = parse_set_header(\'token, "quoted value"\')

    The return value is an object that treats the items case-insensitively
    and keeps the order of the items:

    >>> \'TOKEN\' in hs
    True
    >>> hs.index(\'quoted value\')
    1
    >>> hs
    HeaderSet([\'token\', \'quoted value\'])

    To create a header from the :class:`HeaderSet` again, use the
    :func:`dump_header` function.

    :param value: a set header to be parsed.
    :param on_update: an optional callable that is called every time a
                      value on the :class:`~werkzeug.datastructures.HeaderSet`
                      object is changed.
    :return: a :class:`~werkzeug.datastructures.HeaderSet`
    '''
def parse_if_range_header(value: str | None) -> ds.IfRange:
    """Parses an if-range header which can be an etag or a date.  Returns
    a :class:`~werkzeug.datastructures.IfRange` object.

    .. versionchanged:: 2.0
        If the value represents a datetime, it is timezone-aware.

    .. versionadded:: 0.7
    """
def parse_range_header(value: str | None, make_inclusive: bool = True) -> ds.Range | None:
    """Parses a range header into a :class:`~werkzeug.datastructures.Range`
    object.  If the header is missing or malformed `None` is returned.
    `ranges` is a list of ``(start, stop)`` tuples where the ranges are
    non-inclusive.

    .. versionadded:: 0.7
    """
def parse_content_range_header(value: str | None, on_update: t.Callable[[ds.ContentRange], None] | None = None) -> ds.ContentRange | None:
    """Parses a range header into a
    :class:`~werkzeug.datastructures.ContentRange` object or `None` if
    parsing is not possible.

    .. versionadded:: 0.7

    :param value: a content range header to be parsed.
    :param on_update: an optional callable that is called every time a value
                      on the :class:`~werkzeug.datastructures.ContentRange`
                      object is changed.
    """
def quote_etag(etag: str, weak: bool = False) -> str:
    '''Quote an etag.

    :param etag: the etag to quote.
    :param weak: set to `True` to tag it "weak".
    '''
def unquote_etag(etag: str | None) -> tuple[str, bool] | tuple[None, None]:
    '''Unquote a single etag:

    >>> unquote_etag(\'W/"bar"\')
    (\'bar\', True)
    >>> unquote_etag(\'"bar"\')
    (\'bar\', False)

    :param etag: the etag identifier to unquote.
    :return: a ``(etag, weak)`` tuple.
    '''
def parse_etags(value: str | None) -> ds.ETags:
    """Parse an etag header.

    :param value: the tag header to parse
    :return: an :class:`~werkzeug.datastructures.ETags` object.
    """
def generate_etag(data: bytes) -> str:
    """Generate an etag for some data.

    .. versionchanged:: 2.0
        Use SHA-1. MD5 may not be available in some environments.
    """
def parse_date(value: str | None) -> datetime | None:
    """Parse an :rfc:`2822` date into a timezone-aware
    :class:`datetime.datetime` object, or ``None`` if parsing fails.

    This is a wrapper for :func:`email.utils.parsedate_to_datetime`. It
    returns ``None`` if parsing fails instead of raising an exception,
    and always returns a timezone-aware datetime object. If the string
    doesn't have timezone information, it is assumed to be UTC.

    :param value: A string with a supported date format.

    .. versionchanged:: 2.0
        Return a timezone-aware datetime object. Use
        ``email.utils.parsedate_to_datetime``.
    """
def http_date(timestamp: datetime | date | int | float | struct_time | None = None) -> str:
    """Format a datetime object or timestamp into an :rfc:`2822` date
    string.

    This is a wrapper for :func:`email.utils.format_datetime`. It
    assumes naive datetime objects are in UTC instead of raising an
    exception.

    :param timestamp: The datetime or timestamp to format. Defaults to
        the current time.

    .. versionchanged:: 2.0
        Use ``email.utils.format_datetime``. Accept ``date`` objects.
    """
def parse_age(value: str | None = None) -> timedelta | None:
    """Parses a base-10 integer count of seconds into a timedelta.

    If parsing fails, the return value is `None`.

    :param value: a string consisting of an integer represented in base-10
    :return: a :class:`datetime.timedelta` object or `None`.
    """
def dump_age(age: timedelta | int | None = None) -> str | None:
    """Formats the duration as a base-10 integer.

    :param age: should be an integer number of seconds,
                a :class:`datetime.timedelta` object, or,
                if the age is unknown, `None` (default).
    """
def is_resource_modified(environ: WSGIEnvironment, etag: str | None = None, data: bytes | None = None, last_modified: datetime | str | None = None, ignore_if_range: bool = True) -> bool:
    """Convenience method for conditional requests.

    :param environ: the WSGI environment of the request to be checked.
    :param etag: the etag for the response for comparison.
    :param data: or alternatively the data of the response to automatically
                 generate an etag using :func:`generate_etag`.
    :param last_modified: an optional date of the last modification.
    :param ignore_if_range: If `False`, `If-Range` header will be taken into
                            account.
    :return: `True` if the resource was modified, otherwise `False`.

    .. versionchanged:: 2.0
        SHA-1 is used to generate an etag value for the data. MD5 may
        not be available in some environments.

    .. versionchanged:: 1.0.0
        The check is run for methods other than ``GET`` and ``HEAD``.
    """
def remove_entity_headers(headers: ds.Headers | list[tuple[str, str]], allowed: t.Iterable[str] = ('expires', 'content-location')) -> None:
    """Remove all entity headers from a list or :class:`Headers` object.  This
    operation works in-place.  `Expires` and `Content-Location` headers are
    by default not removed.  The reason for this is :rfc:`2616` section
    10.3.5 which specifies some entity headers that should be sent.

    .. versionchanged:: 0.5
       added `allowed` parameter.

    :param headers: a list or :class:`Headers` object.
    :param allowed: a list of headers that should still be allowed even though
                    they are entity headers.
    """
def remove_hop_by_hop_headers(headers: ds.Headers | list[tuple[str, str]]) -> None:
    '''Remove all HTTP/1.1 "Hop-by-Hop" headers from a list or
    :class:`Headers` object.  This operation works in-place.

    .. versionadded:: 0.5

    :param headers: a list or :class:`Headers` object.
    '''
def is_entity_header(header: str) -> bool:
    """Check if a header is an entity header.

    .. versionadded:: 0.5

    :param header: the header to test.
    :return: `True` if it's an entity header, `False` otherwise.
    """
def is_hop_by_hop_header(header: str) -> bool:
    '''Check if a header is an HTTP/1.1 "Hop-by-Hop" header.

    .. versionadded:: 0.5

    :param header: the header to test.
    :return: `True` if it\'s an HTTP/1.1 "Hop-by-Hop" header, `False` otherwise.
    '''
def parse_cookie(header: WSGIEnvironment | str | None, cls: type[ds.MultiDict] | None = None) -> ds.MultiDict[str, str]:
    """Parse a cookie from a string or WSGI environ.

    The same key can be provided multiple times, the values are stored
    in-order. The default :class:`MultiDict` will have the first value
    first, and all values can be retrieved with
    :meth:`MultiDict.getlist`.

    :param header: The cookie header as a string, or a WSGI environ dict
        with a ``HTTP_COOKIE`` key.
    :param cls: A dict-like class to store the parsed cookies in.
        Defaults to :class:`MultiDict`.

    .. versionchanged:: 3.0
        Passing bytes, and the ``charset`` and ``errors`` parameters, were removed.

    .. versionchanged:: 1.0
        Returns a :class:`MultiDict` instead of a ``TypeConversionDict``.

    .. versionchanged:: 0.5
        Returns a :class:`TypeConversionDict` instead of a regular dict. The ``cls``
        parameter was added.
    """
def dump_cookie(key: str, value: str = '', max_age: timedelta | int | None = None, expires: str | datetime | int | float | None = None, path: str | None = '/', domain: str | None = None, secure: bool = False, httponly: bool = False, sync_expires: bool = True, max_size: int = 4093, samesite: str | None = None) -> str:
    '''Create a Set-Cookie header without the ``Set-Cookie`` prefix.

    The return value is usually restricted to ascii as the vast majority
    of values are properly escaped, but that is no guarantee. It\'s
    tunneled through latin1 as required by :pep:`3333`.

    The return value is not ASCII safe if the key contains unicode
    characters.  This is technically against the specification but
    happens in the wild.  It\'s strongly recommended to not use
    non-ASCII values for the keys.

    :param max_age: should be a number of seconds, or `None` (default) if
                    the cookie should last only as long as the client\'s
                    browser session.  Additionally `timedelta` objects
                    are accepted, too.
    :param expires: should be a `datetime` object or unix timestamp.
    :param path: limits the cookie to a given path, per default it will
                 span the whole domain.
    :param domain: Use this if you want to set a cross-domain cookie. For
                   example, ``domain="example.com"`` will set a cookie
                   that is readable by the domain ``www.example.com``,
                   ``foo.example.com`` etc. Otherwise, a cookie will only
                   be readable by the domain that set it.
    :param secure: The cookie will only be available via HTTPS
    :param httponly: disallow JavaScript to access the cookie.  This is an
                     extension to the cookie standard and probably not
                     supported by all browsers.
    :param charset: the encoding for string values.
    :param sync_expires: automatically set expires if max_age is defined
                         but expires not.
    :param max_size: Warn if the final header value exceeds this size. The
        default, 4093, should be safely `supported by most browsers
        <cookie_>`_. Set to 0 to disable this check.
    :param samesite: Limits the scope of the cookie such that it will
        only be attached to requests if those requests are same-site.

    .. _`cookie`: http://browsercookielimits.squawky.net/

    .. versionchanged:: 3.0
        Passing bytes, and the ``charset`` parameter, were removed.

    .. versionchanged:: 2.3.3
        The ``path`` parameter is ``/`` by default.

    .. versionchanged:: 2.3.1
        The value allows more characters without quoting.

    .. versionchanged:: 2.3
        ``localhost`` and other names without a dot are allowed for the domain. A
        leading dot is ignored.

    .. versionchanged:: 2.3
        The ``path`` parameter is ``None`` by default.

    .. versionchanged:: 1.0.0
        The string ``\'None\'`` is accepted for ``samesite``.
    '''
def is_byte_range_valid(start: int | None, stop: int | None, length: int | None) -> bool:
    """Checks if a given byte content range is valid for the given length.

    .. versionadded:: 0.7
    """
