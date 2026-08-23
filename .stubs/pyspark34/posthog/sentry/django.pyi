from _typeshed import Incomplete
from posthog.sentry import POSTHOG_ID_TAG as POSTHOG_ID_TAG

GET_DISTINCT_ID: Incomplete

def get_distinct_id(request): ...

class PosthogDistinctIdMiddleware:
    get_response: Incomplete
    def __init__(self, get_response) -> None: ...
    def __call__(self, request): ...
