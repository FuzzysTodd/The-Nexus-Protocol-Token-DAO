import sentry_sdk.integrations
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING

class TrytondWSGIIntegration(sentry_sdk.integrations.Integration):
    identifier: str
    def __init__(self) -> None: ...
    @staticmethod
    def setup_once() -> None: ...
