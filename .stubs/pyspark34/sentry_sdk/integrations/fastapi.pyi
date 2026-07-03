from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations import DidNotEnable as DidNotEnable
from sentry_sdk.integrations.starlette import StarletteIntegration as StarletteIntegration, StarletteRequestExtractor as StarletteRequestExtractor
from sentry_sdk.scope import Scope as Scope
from sentry_sdk.tracing import SOURCE_FOR_STYLE as SOURCE_FOR_STYLE, TRANSACTION_SOURCE_ROUTE as TRANSACTION_SOURCE_ROUTE
from sentry_sdk.utils import logger as logger, transaction_from_function as transaction_from_function

class FastApiIntegration(StarletteIntegration):
    identifier: str
    @staticmethod
    def setup_once() -> None: ...

def patch_get_request_handler() -> None: ...
