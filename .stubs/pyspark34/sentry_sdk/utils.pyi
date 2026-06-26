import sentry_sdk
import threading
from _typeshed import Incomplete
from datetime import datetime
from sentry_sdk._compat import PY2 as PY2, PY33 as PY33, PY37 as PY37, implements_str as implements_str, text_type as text_type, urlparse as urlparse
from sentry_sdk._types import EndpointType as EndpointType, ExcInfo as ExcInfo, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import DEFAULT_MAX_VALUE_LENGTH as DEFAULT_MAX_VALUE_LENGTH
from types import FrameType, TracebackType
from typing import Any, Callable, ContextManager, Dict, Iterator, List, NamedTuple, Tuple, Type, TypeVar

epoch: Incomplete
logger: Incomplete
BASE64_ALPHABET: Incomplete
SENSITIVE_DATA_SUBSTITUTE: str

def json_dumps(data: Any) -> bytes:
    """Serialize data into a compact JSON representation encoded as UTF-8."""
def get_default_release() -> str | None:
    """Try to guess a default release."""
def get_sdk_name(installed_integrations: List[str]) -> str:
    """Return the SDK name including the name of the used web framework."""

class CaptureInternalException:
    def __enter__(self) -> ContextManager[Any]: ...
    def __exit__(self, ty: Type[BaseException] | None, value: BaseException | None, tb: TracebackType | None) -> bool: ...

def capture_internal_exceptions() -> ContextManager[Any]: ...
def capture_internal_exception(exc_info: ExcInfo) -> None: ...
def to_timestamp(value: datetime) -> float: ...
def format_timestamp(value: datetime) -> str: ...
def event_hint_with_exc_info(exc_info: ExcInfo | None = None) -> Dict[str, ExcInfo | None]:
    """Creates a hint with the exc info filled in."""

class BadDsn(ValueError):
    """Raised on invalid DSNs."""

class Dsn:
    """Represents a DSN."""
    __dict__: Incomplete
    scheme: Incomplete
    host: Incomplete
    port: Incomplete
    public_key: Incomplete
    secret_key: Incomplete
    project_id: Incomplete
    path: Incomplete
    def __init__(self, value: Dsn | str) -> None: ...
    @property
    def netloc(self) -> str:
        """The netloc part of a DSN."""
    def to_auth(self, client: Any | None = None) -> Auth:
        """Returns the auth info object for this dsn."""

class Auth:
    """Helper object that represents the auth info."""
    scheme: Incomplete
    host: Incomplete
    path: Incomplete
    project_id: Incomplete
    public_key: Incomplete
    secret_key: Incomplete
    version: Incomplete
    client: Incomplete
    def __init__(self, scheme: str, host: str, project_id: str, public_key: str, secret_key: str | None = None, version: int = 7, client: Any | None = None, path: str = '/') -> None: ...
    @property
    def store_api_url(self) -> str:
        """Returns the API url for storing events.

        Deprecated: use get_api_url instead.
        """
    def get_api_url(self, type: EndpointType = 'store') -> str:
        """Returns the API url for storing events."""
    def to_header(self) -> str:
        """Returns the auth header a string."""

class AnnotatedValue:
    """
    Meta information for a data field in the event payload.
    This is to tell Relay that we have tampered with the fields value.
    See:
    https://github.com/getsentry/relay/blob/be12cd49a0f06ea932ed9b9f93a655de5d6ad6d1/relay-general/src/types/meta.rs#L407-L423
    """
    value: Incomplete
    metadata: Incomplete
    def __init__(self, value: Any | None, metadata: Dict[str, Any]) -> None: ...
    @classmethod
    def removed_because_raw_data(cls) -> AnnotatedValue:
        """The value was removed because it could not be parsed. This is done for request body values that are not json nor a form."""
    @classmethod
    def removed_because_over_size_limit(cls) -> AnnotatedValue:
        """The actual value was removed because the size of the field exceeded the configured maximum size (specified with the max_request_body_size sdk option)"""
    @classmethod
    def substituted_because_contains_sensitive_data(cls) -> AnnotatedValue:
        """The actual value was removed because it contained sensitive information."""
T = TypeVar('T')
Annotated = AnnotatedValue | T

def get_type_name(cls) -> str | None: ...
def get_type_module(cls) -> str | None: ...
def should_hide_frame(frame: FrameType) -> bool: ...
def iter_stacks(tb: TracebackType | None) -> Iterator[TracebackType]: ...
def get_lines_from_file(filename: str, lineno: int, max_length: int | None = None, loader: Any | None = None, module: str | None = None) -> Tuple[List[Annotated[str]], Annotated[str] | None, List[Annotated[str]]]: ...
def get_source_context(frame: FrameType, tb_lineno: int, max_value_length: int | None = None) -> Tuple[List[Annotated[str]], Annotated[str] | None, List[Annotated[str]]]: ...
def safe_str(value: Any) -> str: ...
def safe_repr(value: Any) -> str: ...
def filename_for_module(module: str | None, abs_path: str | None) -> str | None: ...
def serialize_frame(frame: FrameType, tb_lineno: int | None = None, include_local_variables: bool = True, include_source_context: bool = True, max_value_length: int | None = None) -> Dict[str, Any]: ...
def current_stacktrace(include_local_variables: bool = True, include_source_context: bool = True, max_value_length: int | None = None) -> Dict[str, Any]: ...
def get_errno(exc_value: BaseException) -> Any | None: ...
def get_error_message(exc_value: BaseException | None) -> str: ...
def single_exception_from_error_tuple(exc_type: type | None, exc_value: BaseException | None, tb: TracebackType | None, client_options: Dict[str, Any] | None = None, mechanism: Dict[str, Any] | None = None, exception_id: int | None = None, parent_id: int | None = None, source: str | None = None) -> Dict[str, Any]:
    """
    Creates a dict that goes into the events `exception.values` list and is ingestible by Sentry.

    See the Exception Interface documentation for more details:
    https://develop.sentry.dev/sdk/event-payloads/exception/
    """

HAS_CHAINED_EXCEPTIONS: Incomplete

def walk_exception_chain(exc_info: ExcInfo) -> Iterator[ExcInfo]: ...
def exceptions_from_error(exc_type: type | None, exc_value: BaseException | None, tb: TracebackType | None, client_options: Dict[str, Any] | None = None, mechanism: Dict[str, Any] | None = None, exception_id: int = 0, parent_id: int = 0, source: str | None = None) -> Tuple[int, List[Dict[str, Any]]]:
    """
    Creates the list of exceptions.
    This can include chained exceptions and exceptions from an ExceptionGroup.

    See the Exception Interface documentation for more details:
    https://develop.sentry.dev/sdk/event-payloads/exception/
    """
def exceptions_from_error_tuple(exc_info: ExcInfo, client_options: Dict[str, Any] | None = None, mechanism: Dict[str, Any] | None = None) -> List[Dict[str, Any]]: ...
def to_string(value: str) -> str: ...
def iter_event_stacktraces(event: Dict[str, Any]) -> Iterator[Dict[str, Any]]: ...
def iter_event_frames(event: Dict[str, Any]) -> Iterator[Dict[str, Any]]: ...
def handle_in_app(event: Dict[str, Any], in_app_exclude: List[str] | None = None, in_app_include: List[str] | None = None, project_root: str | None = None) -> Dict[str, Any]: ...
def set_in_app_in_frames(frames: Any, in_app_exclude: List[str] | None, in_app_include: List[str] | None, project_root: str | None = None) -> Any | None: ...
def exc_info_from_error(error: BaseException | ExcInfo) -> ExcInfo: ...
def event_from_exception(exc_info: BaseException | ExcInfo, client_options: Dict[str, Any] | None = None, mechanism: Dict[str, Any] | None = None) -> Tuple[Dict[str, Any], Dict[str, Any]]: ...
def strip_string(value: str, max_length: int | None = None) -> AnnotatedValue | str: ...

HAS_REAL_CONTEXTVARS: Incomplete
ContextVar: Incomplete
CONTEXTVARS_ERROR_MESSAGE: str

def qualname_from_function(func: Callable[..., Any]) -> str | None:
    """Return the qualified name of func. Works with regular function, lambda, partial and partialmethod."""
def transaction_from_function(func: Callable[..., Any]) -> str | None: ...

disable_capture_event: Incomplete

class ServerlessTimeoutWarning(Exception):
    """Raised when a serverless method is about to reach its timeout."""

class TimeoutThread(threading.Thread):
    """Creates a Thread which runs (sleeps) for a time duration equal to
    waiting_time and raises a custom ServerlessTimeout exception.
    """
    waiting_time: Incomplete
    configured_timeout: Incomplete
    def __init__(self, waiting_time: float, configured_timeout: int) -> None: ...
    def stop(self) -> None: ...
    def run(self) -> None: ...

def to_base64(original: str) -> str | None:
    """
    Convert a string to base64, via UTF-8. Returns None on invalid input.
    """
def from_base64(base64_string: str) -> str | None:
    """
    Convert a string from base64, via UTF-8. Returns None on invalid input.
    """

class Components(NamedTuple):
    scheme: Incomplete
    netloc: Incomplete
    path: Incomplete
    query: Incomplete
    fragment: Incomplete

def sanitize_url(url: str, remove_authority: bool = True, remove_query_values: bool = True, split: bool = False) -> str | Components:
    """
    Removes the authority and query parameter values from a given URL.
    """

class ParsedUrl(NamedTuple):
    url: Incomplete
    query: Incomplete
    fragment: Incomplete

def parse_url(url: str, sanitize: bool = True) -> ParsedUrl:
    """
    Splits a URL into a url (including path), query and fragment. If sanitize is True, the query
    parameters will be sanitized to remove sensitive data. The autority (username and password)
    in the URL will always be removed.
    """
def is_valid_sample_rate(rate: Any, source: str) -> bool:
    """
    Checks the given sample rate to make sure it is valid type and value (a
    boolean or a number between 0 and 1, inclusive).
    """
def match_regex_list(item: str, regex_list: List[str] | None = None, substring_matching: bool = False) -> bool: ...
def is_sentry_url(hub: sentry_sdk.Hub, url: str) -> bool:
    """
    Determines whether the given URL matches the Sentry DSN.
    """
def parse_version(version: str) -> Tuple[int, ...] | None:
    """
    Parses a version string into a tuple of integers.
    This uses the parsing loging from PEP 440:
    https://peps.python.org/pep-0440/#appendix-b-parsing-version-strings-with-regular-expressions
    """
def nanosecond_time() -> int: ...
def now() -> float: ...
