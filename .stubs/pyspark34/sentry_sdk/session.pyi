import uuid
from _typeshed import Incomplete
from datetime import datetime
from sentry_sdk._compat import datetime_utcnow as datetime_utcnow
from sentry_sdk._types import SessionStatus as SessionStatus, TYPE_CHECKING as TYPE_CHECKING
from sentry_sdk.utils import format_timestamp as format_timestamp
from typing import Any

class Session:
    status: Incomplete
    did: Incomplete
    started: Incomplete
    release: Incomplete
    environment: Incomplete
    duration: Incomplete
    user_agent: Incomplete
    ip_address: Incomplete
    session_mode: Incomplete
    errors: int
    def __init__(self, sid: str | uuid.UUID | None = None, did: str | None = None, timestamp: datetime | None = None, started: datetime | None = None, duration: float | None = None, status: SessionStatus | None = None, release: str | None = None, environment: str | None = None, user_agent: str | None = None, ip_address: str | None = None, errors: int | None = None, user: Any | None = None, session_mode: str = 'application') -> None: ...
    @property
    def truncated_started(self) -> datetime: ...
    sid: Incomplete
    timestamp: Incomplete
    def update(self, sid: str | uuid.UUID | None = None, did: str | None = None, timestamp: datetime | None = None, started: datetime | None = None, duration: float | None = None, status: SessionStatus | None = None, release: str | None = None, environment: str | None = None, user_agent: str | None = None, ip_address: str | None = None, errors: int | None = None, user: Any | None = None) -> None: ...
    def close(self, status: SessionStatus | None = None) -> Any: ...
    def get_json_attrs(self, with_user_info: bool | None = True) -> Any: ...
    def to_json(self) -> Any: ...
