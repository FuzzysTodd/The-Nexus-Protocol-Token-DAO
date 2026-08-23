import requests
from . import logging as logging
from ._typing import HTTP_METHOD_T as HTTP_METHOD_T
from _typeshed import Incomplete
from requests import Response as Response
from requests.adapters import HTTPAdapter
from requests.models import PreparedRequest as PreparedRequest
from typing import Tuple, Type

logger: Incomplete
X_AMZN_TRACE_ID: str
X_REQUEST_ID: str

class UniqueRequestIdAdapter(HTTPAdapter):
    X_AMZN_TRACE_ID: str
    def add_headers(self, request, **kwargs) -> None: ...
    def send(self, request: PreparedRequest, *args, **kwargs) -> Response:
        """Catch any RequestException to append request id to the error message for debugging."""

BACKEND_FACTORY_T: Incomplete

def configure_http_backend(backend_factory: BACKEND_FACTORY_T = ...) -> None:
    '''
    Configure the HTTP backend by providing a `backend_factory`. Any HTTP calls made by `huggingface_hub` will use a
    Session object instantiated by this factory. This can be useful if you are running your scripts in a specific
    environment requiring custom configuration (e.g. custom proxy or certifications).

    Use [`get_session`] to get a configured Session. Since `requests.Session` is not guaranteed to be thread-safe,
    `huggingface_hub` creates 1 Session instance per thread. They are all instantiated using the same `backend_factory`
    set in [`configure_http_backend`]. A LRU cache is used to cache the created sessions (and connections) between
    calls. Max size is 128 to avoid memory leaks if thousands of threads are spawned.

    See [this issue](https://github.com/psf/requests/issues/2766) to know more about thread-safety in `requests`.

    Example:
    ```py
    import requests
    from huggingface_hub import configure_http_backend, get_session

    # Create a factory function that returns a Session with configured proxies
    def backend_factory() -> requests.Session:
        session = requests.Session()
        session.proxies = {"http": "http://10.10.1.10:3128", "https": "https://10.10.1.11:1080"}
        return session

    # Set it as the default session factory
    configure_http_backend(backend_factory=backend_factory)

    # In practice, this is mostly done internally in `huggingface_hub`
    session = get_session()
    ```
    '''
def get_session() -> requests.Session:
    '''
    Get a `requests.Session` object, using the session factory from the user.

    Use [`get_session`] to get a configured Session. Since `requests.Session` is not guaranteed to be thread-safe,
    `huggingface_hub` creates 1 Session instance per thread. They are all instantiated using the same `backend_factory`
    set in [`configure_http_backend`]. A LRU cache is used to cache the created sessions (and connections) between
    calls. Max size is 128 to avoid memory leaks if thousands of threads are spawned.

    See [this issue](https://github.com/psf/requests/issues/2766) to know more about thread-safety in `requests`.

    Example:
    ```py
    import requests
    from huggingface_hub import configure_http_backend, get_session

    # Create a factory function that returns a Session with configured proxies
    def backend_factory() -> requests.Session:
        session = requests.Session()
        session.proxies = {"http": "http://10.10.1.10:3128", "https": "https://10.10.1.11:1080"}
        return session

    # Set it as the default session factory
    configure_http_backend(backend_factory=backend_factory)

    # In practice, this is mostly done internally in `huggingface_hub`
    session = get_session()
    ```
    '''
def http_backoff(method: HTTP_METHOD_T, url: str, *, max_retries: int = 5, base_wait_time: float = 1, max_wait_time: float = 8, retry_on_exceptions: Type[Exception] | Tuple[Type[Exception], ...] = ..., retry_on_status_codes: int | Tuple[int, ...] = ..., **kwargs) -> Response:
    '''Wrapper around requests to retry calls on an endpoint, with exponential backoff.

    Endpoint call is retried on exceptions (ex: connection timeout, proxy error,...)
    and/or on specific status codes (ex: service unavailable). If the call failed more
    than `max_retries`, the exception is thrown or `raise_for_status` is called on the
    response object.

    Re-implement mechanisms from the `backoff` library to avoid adding an external
    dependencies to `hugging_face_hub`. See https://github.com/litl/backoff.

    Args:
        method (`Literal["GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"]`):
            HTTP method to perform.
        url (`str`):
            The URL of the resource to fetch.
        max_retries (`int`, *optional*, defaults to `5`):
            Maximum number of retries, defaults to 5 (no retries).
        base_wait_time (`float`, *optional*, defaults to `1`):
            Duration (in seconds) to wait before retrying the first time.
            Wait time between retries then grows exponentially, capped by
            `max_wait_time`.
        max_wait_time (`float`, *optional*, defaults to `8`):
            Maximum duration (in seconds) to wait before retrying.
        retry_on_exceptions (`Type[Exception]` or `Tuple[Type[Exception]]`, *optional*, defaults to `(Timeout, ProxyError,)`):
            Define which exceptions must be caught to retry the request. Can be a single
            type or a tuple of types.
            By default, retry on `Timeout` and `ProxyError`.
        retry_on_status_codes (`int` or `Tuple[int]`, *optional*, defaults to `503`):
            Define on which status codes the request must be retried. By default, only
            HTTP 503 Service Unavailable is retried.
        **kwargs (`dict`, *optional*):
            kwargs to pass to `requests.request`.

    Example:
    ```
    >>> from huggingface_hub.utils import http_backoff

    # Same usage as "requests.request".
    >>> response = http_backoff("GET", "https://www.google.com")
    >>> response.raise_for_status()

    # If you expect a Gateway Timeout from time to time
    >>> http_backoff("PUT", upload_url, data=data, retry_on_status_codes=504)
    >>> response.raise_for_status()
    ```

    <Tip warning={true}>

    When using `requests` it is possible to stream data by passing an iterator to the
    `data` argument. On http backoff this is a problem as the iterator is not reset
    after a failed call. This issue is mitigated for file objects or any IO streams
    by saving the initial position of the cursor (with `data.tell()`) and resetting the
    cursor between each call (with `data.seek()`). For arbitrary iterators, http backoff
    will fail. If this is a hard constraint for you, please let us know by opening an
    issue on [Github](https://github.com/huggingface/huggingface_hub).

    </Tip>
    '''
