from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP
from sentry_sdk.hub import Hub as Hub
from sentry_sdk.integrations.django.asgi import wrap_async_view as wrap_async_view

def patch_views() -> None: ...
