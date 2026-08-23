from _typeshed import Incomplete
from datetime import datetime
from typing import Any

next_attr_name: str
ISO8601: str
ISO8601_PAT: Incomplete

def parse_date(s: str | None) -> str | datetime | None:
    """parse an ISO8601 date string

    If it is None or not a valid ISO8601 timestamp,
    it will be returned unmodified.
    Otherwise, it will return a datetime object.
    """
def extract_dates(obj: Any) -> Any:
    """extract ISO8601 dates from unpacked JSON"""
def squash_dates(obj: Any) -> Any:
    """squash datetime objects into ISO8601 strings"""
def date_default(obj: Any) -> Any:
    """DEPRECATED: Use jupyter_client.jsonutil.json_default"""
def json_default(obj: Any) -> Any:
    """default function for packing objects in JSON."""
def json_clean(obj: Any) -> Any: ...
