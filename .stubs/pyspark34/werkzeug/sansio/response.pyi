import typing as t
from ..datastructures import HeaderSet as HeaderSet, Headers as Headers
from ..http import HTTP_STATUS_CODES as HTTP_STATUS_CODES, dump_cookie as dump_cookie
from ..utils import get_content_type as get_content_type
from _typeshed import Incomplete
from datetime import datetime, timedelta
from http import HTTPStatus
from werkzeug.datastructures import CallbackDict as CallbackDict, ContentRange as ContentRange, ContentSecurityPolicy as ContentSecurityPolicy, ResponseCacheControl as ResponseCacheControl, WWWAuthenticate as WWWAuthenticate
from werkzeug.http import COEP as COEP, COOP as COOP, dump_age as dump_age, dump_header as dump_header, dump_options_header as dump_options_header, http_date as http_date, parse_age as parse_age, parse_cache_control_header as parse_cache_control_header, parse_content_range_header as parse_content_range_header, parse_csp_header as parse_csp_header, parse_date as parse_date, parse_options_header as parse_options_header, parse_set_header as parse_set_header, quote_etag as quote_etag, unquote_etag as unquote_etag
from werkzeug.utils import header_property as header_property

class Response:
    """Represents the non-IO parts of an HTTP response, specifically the
    status and headers but not the body.

    This class is not meant for general use. It should only be used when
    implementing WSGI, ASGI, or another HTTP application spec. Werkzeug
    provides a WSGI implementation at :cls:`werkzeug.wrappers.Response`.

    :param status: The status code for the response. Either an int, in
        which case the default status message is added, or a string in
        the form ``{code} {message}``, like ``404 Not Found``. Defaults
        to 200.
    :param headers: A :class:`~werkzeug.datastructures.Headers` object,
        or a list of ``(key, value)`` tuples that will be converted to a
        ``Headers`` object.
    :param mimetype: The mime type (content type without charset or
        other parameters) of the response. If the value starts with
        ``text/`` (or matches some other special cases), the charset
        will be added to create the ``content_type``.
    :param content_type: The full content type of the response.
        Overrides building the value from ``mimetype``.

    .. versionchanged:: 3.0
        The ``charset`` attribute was removed.

    .. versionadded:: 2.0
    """
    default_status: int
    default_mimetype: str | None
    max_cookie_size: int
    headers: Headers
    def __init__(self, status: int | str | HTTPStatus | None = None, headers: t.Mapping[str, str | t.Iterable[str]] | t.Iterable[tuple[str, str]] | None = None, mimetype: str | None = None, content_type: str | None = None) -> None: ...
    @property
    def status_code(self) -> int:
        """The HTTP status code as a number."""
    @status_code.setter
    def status_code(self, code: int) -> None: ...
    @property
    def status(self) -> str:
        """The HTTP status code as a string."""
    @status.setter
    def status(self, value: str | int | HTTPStatus) -> None: ...
    def set_cookie(self, key: str, value: str = '', max_age: timedelta | int | None = None, expires: str | datetime | int | float | None = None, path: str | None = '/', domain: str | None = None, secure: bool = False, httponly: bool = False, samesite: str | None = None) -> None:
        '''Sets a cookie.

        A warning is raised if the size of the cookie header exceeds
        :attr:`max_cookie_size`, but the header will still be set.

        :param key: the key (name) of the cookie to be set.
        :param value: the value of the cookie.
        :param max_age: should be a number of seconds, or `None` (default) if
                        the cookie should last only as long as the client\'s
                        browser session.
        :param expires: should be a `datetime` object or UNIX timestamp.
        :param path: limits the cookie to a given path, per default it will
                     span the whole domain.
        :param domain: if you want to set a cross-domain cookie.  For example,
                       ``domain="example.com"`` will set a cookie that is
                       readable by the domain ``www.example.com``,
                       ``foo.example.com`` etc.  Otherwise, a cookie will only
                       be readable by the domain that set it.
        :param secure: If ``True``, the cookie will only be available
            via HTTPS.
        :param httponly: Disallow JavaScript access to the cookie.
        :param samesite: Limit the scope of the cookie to only be
            attached to requests that are "same-site".
        '''
    def delete_cookie(self, key: str, path: str | None = '/', domain: str | None = None, secure: bool = False, httponly: bool = False, samesite: str | None = None) -> None:
        '''Delete a cookie.  Fails silently if key doesn\'t exist.

        :param key: the key (name) of the cookie to be deleted.
        :param path: if the cookie that should be deleted was limited to a
                     path, the path has to be defined here.
        :param domain: if the cookie that should be deleted was limited to a
                       domain, that domain has to be defined here.
        :param secure: If ``True``, the cookie will only be available
            via HTTPS.
        :param httponly: Disallow JavaScript access to the cookie.
        :param samesite: Limit the scope of the cookie to only be
            attached to requests that are "same-site".
        '''
    @property
    def is_json(self) -> bool:
        """Check if the mimetype indicates JSON data, either
        :mimetype:`application/json` or :mimetype:`application/*+json`.
        """
    @property
    def mimetype(self) -> str | None:
        """The mimetype (content type without charset etc.)"""
    @mimetype.setter
    def mimetype(self, value: str) -> None: ...
    @property
    def mimetype_params(self) -> dict[str, str]:
        """The mimetype parameters as dict. For example if the
        content type is ``text/html; charset=utf-8`` the params would be
        ``{'charset': 'utf-8'}``.

        .. versionadded:: 0.5
        """
    location: Incomplete
    age: Incomplete
    content_type: Incomplete
    content_length: Incomplete
    content_location: Incomplete
    content_encoding: Incomplete
    content_md5: Incomplete
    date: Incomplete
    expires: Incomplete
    last_modified: Incomplete
    @property
    def retry_after(self) -> datetime | None:
        """The Retry-After response-header field can be used with a
        503 (Service Unavailable) response to indicate how long the
        service is expected to be unavailable to the requesting client.

        Time in seconds until expiration or date.

        .. versionchanged:: 2.0
            The datetime object is timezone-aware.
        """
    @retry_after.setter
    def retry_after(self, value: datetime | int | str | None) -> None: ...
    vary: Incomplete
    content_language: Incomplete
    allow: Incomplete
    @property
    def cache_control(self) -> ResponseCacheControl:
        """The Cache-Control general-header field is used to specify
        directives that MUST be obeyed by all caching mechanisms along the
        request/response chain.
        """
    def set_etag(self, etag: str, weak: bool = False) -> None:
        """Set the etag, and override the old one if there was one."""
    def get_etag(self) -> tuple[str, bool] | tuple[None, None]:
        """Return a tuple in the form ``(etag, is_weak)``.  If there is no
        ETag the return value is ``(None, None)``.
        """
    accept_ranges: Incomplete
    @property
    def content_range(self) -> ContentRange:
        """The ``Content-Range`` header as a
        :class:`~werkzeug.datastructures.ContentRange` object. Available
        even if the header is not set.

        .. versionadded:: 0.7
        """
    @content_range.setter
    def content_range(self, value: ContentRange | str | None) -> None: ...
    @property
    def www_authenticate(self) -> WWWAuthenticate:
        '''The ``WWW-Authenticate`` header parsed into a :class:`.WWWAuthenticate`
        object. Modifying the object will modify the header value.

        This header is not set by default. To set this header, assign an instance of
        :class:`.WWWAuthenticate` to this attribute.

        .. code-block:: python

            response.www_authenticate = WWWAuthenticate(
                "basic", {"realm": "Authentication Required"}
            )

        Multiple values for this header can be sent to give the client multiple options.
        Assign a list to set multiple headers. However, modifying the items in the list
        will not automatically update the header values, and accessing this attribute
        will only ever return the first value.

        To unset this header, assign ``None`` or use ``del``.

        .. versionchanged:: 2.3
            This attribute can be assigned to to set the header. A list can be assigned
            to set multiple header values. Use ``del`` to unset the header.

        .. versionchanged:: 2.3
            :class:`WWWAuthenticate` is no longer a ``dict``. The ``token`` attribute
            was added for auth challenges that use a token instead of parameters.
        '''
    @www_authenticate.setter
    def www_authenticate(self, value: WWWAuthenticate | list[WWWAuthenticate] | None) -> None: ...
    @www_authenticate.deleter
    def www_authenticate(self) -> None: ...
    @property
    def content_security_policy(self) -> ContentSecurityPolicy:
        """The ``Content-Security-Policy`` header as a
        :class:`~werkzeug.datastructures.ContentSecurityPolicy` object. Available
        even if the header is not set.

        The Content-Security-Policy header adds an additional layer of
        security to help detect and mitigate certain types of attacks.
        """
    @content_security_policy.setter
    def content_security_policy(self, value: ContentSecurityPolicy | str | None) -> None: ...
    @property
    def content_security_policy_report_only(self) -> ContentSecurityPolicy:
        """The ``Content-Security-policy-report-only`` header as a
        :class:`~werkzeug.datastructures.ContentSecurityPolicy` object. Available
        even if the header is not set.

        The Content-Security-Policy-Report-Only header adds a csp policy
        that is not enforced but is reported thereby helping detect
        certain types of attacks.
        """
    @content_security_policy_report_only.setter
    def content_security_policy_report_only(self, value: ContentSecurityPolicy | str | None) -> None: ...
    @property
    def access_control_allow_credentials(self) -> bool:
        """Whether credentials can be shared by the browser to
        JavaScript code. As part of the preflight request it indicates
        whether credentials can be used on the cross origin request.
        """
    @access_control_allow_credentials.setter
    def access_control_allow_credentials(self, value: bool | None) -> None: ...
    access_control_allow_headers: Incomplete
    access_control_allow_methods: Incomplete
    access_control_allow_origin: Incomplete
    access_control_expose_headers: Incomplete
    access_control_max_age: Incomplete
    cross_origin_opener_policy: Incomplete
    cross_origin_embedder_policy: Incomplete
