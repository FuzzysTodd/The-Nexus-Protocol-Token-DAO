import typing as t
from ..datastructures import Accept as Accept, Authorization as Authorization, CharsetAccept as CharsetAccept, ETags as ETags, HeaderSet as HeaderSet, Headers as Headers, IfRange as IfRange, ImmutableList as ImmutableList, ImmutableMultiDict as ImmutableMultiDict, LanguageAccept as LanguageAccept, MIMEAccept as MIMEAccept, MultiDict as MultiDict, Range as Range, RequestCacheControl as RequestCacheControl
from ..http import parse_accept_header as parse_accept_header, parse_cache_control_header as parse_cache_control_header, parse_date as parse_date, parse_etags as parse_etags, parse_if_range_header as parse_if_range_header, parse_list_header as parse_list_header, parse_options_header as parse_options_header, parse_range_header as parse_range_header, parse_set_header as parse_set_header
from ..user_agent import UserAgent as UserAgent
from ..utils import cached_property as cached_property, header_property as header_property
from .http import parse_cookie as parse_cookie
from .utils import get_content_length as get_content_length, get_current_url as get_current_url, get_host as get_host
from _typeshed import Incomplete
from datetime import datetime

class Request:
    '''Represents the non-IO parts of a HTTP request, including the
    method, URL info, and headers.

    This class is not meant for general use. It should only be used when
    implementing WSGI, ASGI, or another HTTP application spec. Werkzeug
    provides a WSGI implementation at :cls:`werkzeug.wrappers.Request`.

    :param method: The method the request was made with, such as
        ``GET``.
    :param scheme: The URL scheme of the protocol the request used, such
        as ``https`` or ``wss``.
    :param server: The address of the server. ``(host, port)``,
        ``(path, None)`` for unix sockets, or ``None`` if not known.
    :param root_path: The prefix that the application is mounted under.
        This is prepended to generated URLs, but is not part of route
        matching.
    :param path: The path part of the URL after ``root_path``.
    :param query_string: The part of the URL after the "?".
    :param headers: The headers received with the request.
    :param remote_addr: The address of the client sending the request.

    .. versionchanged:: 3.0
        The ``charset``, ``url_charset``, and ``encoding_errors`` attributes
        were removed.

    .. versionadded:: 2.0
    '''
    parameter_storage_class: type[MultiDict]
    dict_storage_class: type[MultiDict]
    list_storage_class: type[t.List]
    user_agent_class: type[UserAgent]
    trusted_hosts: list[str] | None
    method: Incomplete
    scheme: Incomplete
    server: Incomplete
    root_path: Incomplete
    path: Incomplete
    query_string: Incomplete
    headers: Incomplete
    remote_addr: Incomplete
    def __init__(self, method: str, scheme: str, server: tuple[str, int | None] | None, root_path: str, path: str, query_string: bytes, headers: Headers, remote_addr: str | None) -> None: ...
    def args(self) -> MultiDict[str, str]:
        """The parsed URL parameters (the part in the URL after the question
        mark).

        By default an
        :class:`~werkzeug.datastructures.ImmutableMultiDict`
        is returned from this function.  This can be changed by setting
        :attr:`parameter_storage_class` to a different type.  This might
        be necessary if the order of the form data is important.

        .. versionchanged:: 2.3
            Invalid bytes remain percent encoded.
        """
    def access_route(self) -> list[str]:
        """If a forwarded header exists this is a list of all ip addresses
        from the client ip to the last proxy server.
        """
    def full_path(self) -> str:
        """Requested path, including the query string."""
    @property
    def is_secure(self) -> bool:
        """``True`` if the request was made with a secure protocol
        (HTTPS or WSS).
        """
    def url(self) -> str:
        """The full request URL with the scheme, host, root path, path,
        and query string."""
    def base_url(self) -> str:
        """Like :attr:`url` but without the query string."""
    def root_url(self) -> str:
        """The request URL scheme, host, and root path. This is the root
        that the application is accessed from.
        """
    def host_url(self) -> str:
        """The request URL scheme and host only."""
    def host(self) -> str:
        """The host name the request was made to, including the port if
        it's non-standard. Validated with :attr:`trusted_hosts`.
        """
    def cookies(self) -> ImmutableMultiDict[str, str]:
        """A :class:`dict` with the contents of all cookies transmitted with
        the request."""
    content_type: Incomplete
    def content_length(self) -> int | None:
        """The Content-Length entity-header field indicates the size of the
        entity-body in bytes or, in the case of the HEAD method, the size of
        the entity-body that would have been sent had the request been a
        GET.
        """
    content_encoding: Incomplete
    content_md5: Incomplete
    referrer: Incomplete
    date: Incomplete
    max_forwards: Incomplete
    @property
    def mimetype(self) -> str:
        """Like :attr:`content_type`, but without parameters (eg, without
        charset, type etc.) and always lowercase.  For example if the content
        type is ``text/HTML; charset=utf-8`` the mimetype would be
        ``'text/html'``.
        """
    @property
    def mimetype_params(self) -> dict[str, str]:
        """The mimetype parameters as dict.  For example if the content
        type is ``text/html; charset=utf-8`` the params would be
        ``{'charset': 'utf-8'}``.
        """
    def pragma(self) -> HeaderSet:
        """The Pragma general-header field is used to include
        implementation-specific directives that might apply to any recipient
        along the request/response chain.  All pragma directives specify
        optional behavior from the viewpoint of the protocol; however, some
        systems MAY require that behavior be consistent with the directives.
        """
    def accept_mimetypes(self) -> MIMEAccept:
        """List of mimetypes this client supports as
        :class:`~werkzeug.datastructures.MIMEAccept` object.
        """
    def accept_charsets(self) -> CharsetAccept:
        """List of charsets this client supports as
        :class:`~werkzeug.datastructures.CharsetAccept` object.
        """
    def accept_encodings(self) -> Accept:
        """List of encodings this client accepts.  Encodings in a HTTP term
        are compression encodings such as gzip.  For charsets have a look at
        :attr:`accept_charset`.
        """
    def accept_languages(self) -> LanguageAccept:
        """List of languages this client accepts as
        :class:`~werkzeug.datastructures.LanguageAccept` object.

        .. versionchanged 0.5
           In previous versions this was a regular
           :class:`~werkzeug.datastructures.Accept` object.
        """
    def cache_control(self) -> RequestCacheControl:
        """A :class:`~werkzeug.datastructures.RequestCacheControl` object
        for the incoming cache control headers.
        """
    def if_match(self) -> ETags:
        """An object containing all the etags in the `If-Match` header.

        :rtype: :class:`~werkzeug.datastructures.ETags`
        """
    def if_none_match(self) -> ETags:
        """An object containing all the etags in the `If-None-Match` header.

        :rtype: :class:`~werkzeug.datastructures.ETags`
        """
    def if_modified_since(self) -> datetime | None:
        """The parsed `If-Modified-Since` header as a datetime object.

        .. versionchanged:: 2.0
            The datetime object is timezone-aware.
        """
    def if_unmodified_since(self) -> datetime | None:
        """The parsed `If-Unmodified-Since` header as a datetime object.

        .. versionchanged:: 2.0
            The datetime object is timezone-aware.
        """
    def if_range(self) -> IfRange:
        """The parsed ``If-Range`` header.

        .. versionchanged:: 2.0
            ``IfRange.date`` is timezone-aware.

        .. versionadded:: 0.7
        """
    def range(self) -> Range | None:
        """The parsed `Range` header.

        .. versionadded:: 0.7

        :rtype: :class:`~werkzeug.datastructures.Range`
        """
    def user_agent(self) -> UserAgent:
        """The user agent. Use ``user_agent.string`` to get the header
        value. Set :attr:`user_agent_class` to a subclass of
        :class:`~werkzeug.user_agent.UserAgent` to provide parsing for
        the other properties or other extended data.

        .. versionchanged:: 2.1
            The built-in parser was removed. Set ``user_agent_class`` to a ``UserAgent``
            subclass to parse data from the string.
        """
    def authorization(self) -> Authorization | None:
        """The ``Authorization`` header parsed into an :class:`.Authorization` object.
        ``None`` if the header is not present.

        .. versionchanged:: 2.3
            :class:`Authorization` is no longer a ``dict``. The ``token`` attribute
            was added for auth schemes that use a token instead of parameters.
        """
    origin: Incomplete
    access_control_request_headers: Incomplete
    access_control_request_method: Incomplete
    @property
    def is_json(self) -> bool:
        """Check if the mimetype indicates JSON data, either
        :mimetype:`application/json` or :mimetype:`application/*+json`.
        """
