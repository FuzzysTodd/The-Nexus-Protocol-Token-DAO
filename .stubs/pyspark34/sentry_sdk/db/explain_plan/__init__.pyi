from _typeshed import Incomplete
from sentry_sdk._compat import datetime_utcnow as datetime_utcnow
from sentry_sdk.consts import TYPE_CHECKING as TYPE_CHECKING
from typing import Any

EXPLAIN_CACHE: Incomplete
EXPLAIN_CACHE_SIZE: int
EXPLAIN_CACHE_TIMEOUT_SECONDS: Incomplete

def cache_statement(statement: str, options: dict[str, Any]) -> None: ...
def remove_expired_cache_items() -> None:
    """
    Remove expired cache items from the cache.
    """
def should_run_explain_plan(statement: str, options: dict[str, Any]) -> bool:
    """
    Check cache if the explain plan for the given statement should be run.
    """
