from botocore.awsrequest import AWSRequest as AWSRequest
from sentry_sdk import Hub as Hub
from sentry_sdk._functools import partial as partial
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP, SPANDATA as SPANDATA
from sentry_sdk.integrations import DidNotEnable as DidNotEnable, Integration as Integration
from sentry_sdk.tracing import Span as Span
from sentry_sdk.utils import capture_internal_exceptions as capture_internal_exceptions, parse_url as parse_url, parse_version as parse_version

class Boto3Integration(Integration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...
