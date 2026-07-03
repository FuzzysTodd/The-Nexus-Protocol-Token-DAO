from .typedefs import LooseHeaders, StrOrURL
from .web_response import Response
from _typeshed import Incomplete
from typing import Any, Iterable

__all__ = ['HTTPException', 'HTTPError', 'HTTPRedirection', 'HTTPSuccessful', 'HTTPOk', 'HTTPCreated', 'HTTPAccepted', 'HTTPNonAuthoritativeInformation', 'HTTPNoContent', 'HTTPResetContent', 'HTTPPartialContent', 'HTTPMultipleChoices', 'HTTPMovedPermanently', 'HTTPFound', 'HTTPSeeOther', 'HTTPNotModified', 'HTTPUseProxy', 'HTTPTemporaryRedirect', 'HTTPPermanentRedirect', 'HTTPClientError', 'HTTPBadRequest', 'HTTPUnauthorized', 'HTTPPaymentRequired', 'HTTPForbidden', 'HTTPNotFound', 'HTTPMethodNotAllowed', 'HTTPNotAcceptable', 'HTTPProxyAuthenticationRequired', 'HTTPRequestTimeout', 'HTTPConflict', 'HTTPGone', 'HTTPLengthRequired', 'HTTPPreconditionFailed', 'HTTPRequestEntityTooLarge', 'HTTPRequestURITooLong', 'HTTPUnsupportedMediaType', 'HTTPRequestRangeNotSatisfiable', 'HTTPExpectationFailed', 'HTTPMisdirectedRequest', 'HTTPUnprocessableEntity', 'HTTPFailedDependency', 'HTTPUpgradeRequired', 'HTTPPreconditionRequired', 'HTTPTooManyRequests', 'HTTPRequestHeaderFieldsTooLarge', 'HTTPUnavailableForLegalReasons', 'HTTPServerError', 'HTTPInternalServerError', 'HTTPNotImplemented', 'HTTPBadGateway', 'HTTPServiceUnavailable', 'HTTPGatewayTimeout', 'HTTPVersionNotSupported', 'HTTPVariantAlsoNegotiates', 'HTTPInsufficientStorage', 'HTTPNotExtended', 'HTTPNetworkAuthenticationRequired']

class HTTPException(Response, Exception):
    status_code: int
    empty_body: bool
    __http_exception__: bool
    text: Incomplete
    def __init__(self, *, headers: LooseHeaders | None = None, reason: str | None = None, body: Any = None, text: str | None = None, content_type: str | None = None) -> None: ...
    def __bool__(self) -> bool: ...

class HTTPError(HTTPException):
    """Base class for exceptions with status codes in the 400s and 500s."""
class HTTPRedirection(HTTPException):
    """Base class for exceptions with status codes in the 300s."""
class HTTPSuccessful(HTTPException):
    """Base class for exceptions with status codes in the 200s."""

class HTTPOk(HTTPSuccessful):
    status_code: int

class HTTPCreated(HTTPSuccessful):
    status_code: int

class HTTPAccepted(HTTPSuccessful):
    status_code: int

class HTTPNonAuthoritativeInformation(HTTPSuccessful):
    status_code: int

class HTTPNoContent(HTTPSuccessful):
    status_code: int
    empty_body: bool

class HTTPResetContent(HTTPSuccessful):
    status_code: int
    empty_body: bool

class HTTPPartialContent(HTTPSuccessful):
    status_code: int

class _HTTPMove(HTTPRedirection):
    location: Incomplete
    def __init__(self, location: StrOrURL, *, headers: LooseHeaders | None = None, reason: str | None = None, body: Any = None, text: str | None = None, content_type: str | None = None) -> None: ...

class HTTPMultipleChoices(_HTTPMove):
    status_code: int

class HTTPMovedPermanently(_HTTPMove):
    status_code: int

class HTTPFound(_HTTPMove):
    status_code: int

class HTTPSeeOther(_HTTPMove):
    status_code: int

class HTTPNotModified(HTTPRedirection):
    status_code: int
    empty_body: bool

class HTTPUseProxy(_HTTPMove):
    status_code: int

class HTTPTemporaryRedirect(_HTTPMove):
    status_code: int

class HTTPPermanentRedirect(_HTTPMove):
    status_code: int

class HTTPClientError(HTTPError): ...

class HTTPBadRequest(HTTPClientError):
    status_code: int

class HTTPUnauthorized(HTTPClientError):
    status_code: int

class HTTPPaymentRequired(HTTPClientError):
    status_code: int

class HTTPForbidden(HTTPClientError):
    status_code: int

class HTTPNotFound(HTTPClientError):
    status_code: int

class HTTPMethodNotAllowed(HTTPClientError):
    status_code: int
    allowed_methods: Incomplete
    method: Incomplete
    def __init__(self, method: str, allowed_methods: Iterable[str], *, headers: LooseHeaders | None = None, reason: str | None = None, body: Any = None, text: str | None = None, content_type: str | None = None) -> None: ...

class HTTPNotAcceptable(HTTPClientError):
    status_code: int

class HTTPProxyAuthenticationRequired(HTTPClientError):
    status_code: int

class HTTPRequestTimeout(HTTPClientError):
    status_code: int

class HTTPConflict(HTTPClientError):
    status_code: int

class HTTPGone(HTTPClientError):
    status_code: int

class HTTPLengthRequired(HTTPClientError):
    status_code: int

class HTTPPreconditionFailed(HTTPClientError):
    status_code: int

class HTTPRequestEntityTooLarge(HTTPClientError):
    status_code: int
    def __init__(self, max_size: float, actual_size: float, **kwargs: Any) -> None: ...

class HTTPRequestURITooLong(HTTPClientError):
    status_code: int

class HTTPUnsupportedMediaType(HTTPClientError):
    status_code: int

class HTTPRequestRangeNotSatisfiable(HTTPClientError):
    status_code: int

class HTTPExpectationFailed(HTTPClientError):
    status_code: int

class HTTPMisdirectedRequest(HTTPClientError):
    status_code: int

class HTTPUnprocessableEntity(HTTPClientError):
    status_code: int

class HTTPFailedDependency(HTTPClientError):
    status_code: int

class HTTPUpgradeRequired(HTTPClientError):
    status_code: int

class HTTPPreconditionRequired(HTTPClientError):
    status_code: int

class HTTPTooManyRequests(HTTPClientError):
    status_code: int

class HTTPRequestHeaderFieldsTooLarge(HTTPClientError):
    status_code: int

class HTTPUnavailableForLegalReasons(HTTPClientError):
    status_code: int
    link: Incomplete
    def __init__(self, link: str, *, headers: LooseHeaders | None = None, reason: str | None = None, body: Any = None, text: str | None = None, content_type: str | None = None) -> None: ...

class HTTPServerError(HTTPError): ...

class HTTPInternalServerError(HTTPServerError):
    status_code: int

class HTTPNotImplemented(HTTPServerError):
    status_code: int

class HTTPBadGateway(HTTPServerError):
    status_code: int

class HTTPServiceUnavailable(HTTPServerError):
    status_code: int

class HTTPGatewayTimeout(HTTPServerError):
    status_code: int

class HTTPVersionNotSupported(HTTPServerError):
    status_code: int

class HTTPVariantAlsoNegotiates(HTTPServerError):
    status_code: int

class HTTPInsufficientStorage(HTTPServerError):
    status_code: int

class HTTPNotExtended(HTTPServerError):
    status_code: int

class HTTPNetworkAuthenticationRequired(HTTPServerError):
    status_code: int
