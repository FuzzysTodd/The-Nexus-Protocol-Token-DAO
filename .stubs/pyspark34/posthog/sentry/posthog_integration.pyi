from _typeshed import Incomplete
from posthog.request import DEFAULT_HOST as DEFAULT_HOST
from posthog.sentry import POSTHOG_ID_TAG as POSTHOG_ID_TAG
from sentry_sdk._types import Event as Event, Hint as Hint
from sentry_sdk.integrations import Integration

class PostHogIntegration(Integration):
    identifier: str
    organization: Incomplete
    project_id: Incomplete
    prefix: str
    @staticmethod
    def setup_once(): ...
