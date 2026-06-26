import threading
from typing import Dict

class _ThreadLocalApiSettings(threading.local):
    api_key: str | None
    cookies: Dict | None
    headers: Dict | None
    def __init__(self) -> None: ...
