from _typeshed import Incomplete
from sentry_sdk import Hub as Hub
from sentry_sdk._compat import text_type as text_type
from sentry_sdk.consts import OP as OP, SPANDATA as SPANDATA

METHODS_TO_INSTRUMENT: Incomplete

def patch_caching() -> None: ...
