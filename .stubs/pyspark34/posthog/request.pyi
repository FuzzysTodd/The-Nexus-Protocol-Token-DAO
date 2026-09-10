import json
import requests
from _typeshed import Incomplete
from posthog.utils import remove_trailing_slash as remove_trailing_slash
from posthog.version import VERSION as VERSION
from typing import Any

DEFAULT_HOST: str
USER_AGENT: Incomplete

def post(api_key: str, host: str | None = None, path: Incomplete | None = None, gzip: bool = False, timeout: int = 15, **kwargs) -> requests.Response:
    """Post the `kwargs` to the API"""
def decide(api_key: str, host: str | None = None, gzip: bool = False, timeout: int = 15, **kwargs) -> Any:
    """Post the `kwargs to the decide API endpoint"""
def batch_post(api_key: str, host: str | None = None, gzip: bool = False, timeout: int = 15, **kwargs) -> requests.Response:
    """Post the `kwargs` to the batch API endpoint for events"""
def get(api_key: str, url: str, host: str | None = None, timeout: int | None = None) -> requests.Response: ...

class APIError(Exception):
    message: Incomplete
    status: Incomplete
    def __init__(self, status: int | str, message: str) -> None: ...

class DatetimeSerializer(json.JSONEncoder):
    def default(self, obj: Any): ...
