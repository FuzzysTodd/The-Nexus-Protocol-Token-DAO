from sentry_sdk import Hub as Hub
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from typing import Any, Dict

def capture_checkin(monitor_slug: str | None = None, check_in_id: str | None = None, status: str | None = None, duration: float | None = None, monitor_config: Dict[str, Any] | None = None) -> str: ...
