from ..exceptions import HTTPError as HTTPError, HTTPWarning as HTTPWarning, MaxRetryError as MaxRetryError, ProtocolError as ProtocolError, SSLError as SSLError, TimeoutError as TimeoutError
from ..packages.six.moves.urllib.parse import urljoin as urljoin
from ..request import RequestMethods as RequestMethods
from ..response import HTTPResponse as HTTPResponse
from ..util.retry import Retry as Retry
from ..util.timeout import Timeout as Timeout
from _typeshed import Incomplete

log: Incomplete

class AppEnginePlatformWarning(HTTPWarning): ...
class AppEnginePlatformError(HTTPError): ...

class AppEngineManager(RequestMethods):
    """
    Connection manager for Google App Engine sandbox applications.

    This manager uses the URLFetch service directly instead of using the
    emulated httplib, and is subject to URLFetch limitations as described in
    the App Engine documentation `here
    <https://cloud.google.com/appengine/docs/python/urlfetch>`_.

    Notably it will raise an :class:`AppEnginePlatformError` if:
        * URLFetch is not available.
        * If you attempt to use this on App Engine Flexible, as full socket
          support is available.
        * If a request size is more than 10 megabytes.
        * If a response size is more than 32 megabytes.
        * If you use an unsupported request method such as OPTIONS.

    Beyond those cases, it will raise normal urllib3 errors.
    """
    validate_certificate: Incomplete
    urlfetch_retries: Incomplete
    retries: Incomplete
    def __init__(self, headers: Incomplete | None = None, retries: Incomplete | None = None, validate_certificate: bool = True, urlfetch_retries: bool = True) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None): ...
    def urlopen(self, method, url, body: Incomplete | None = None, headers: Incomplete | None = None, retries: Incomplete | None = None, redirect: bool = True, timeout=..., **response_kw): ...

is_appengine: Incomplete
is_appengine_sandbox: Incomplete
is_local_appengine: Incomplete
is_prod_appengine: Incomplete
is_prod_appengine_mvms: Incomplete
