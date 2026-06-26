from sentry_sdk import Hub as Hub
from sentry_sdk._functools import wraps as wraps
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.consts import OP as OP

def patch_signals() -> None:
    """Patch django signal receivers to create a span"""
