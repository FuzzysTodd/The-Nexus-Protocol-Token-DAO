from arrow import locales as locales
from arrow.constants import DEFAULT_LOCALE as DEFAULT_LOCALE
from datetime import datetime
from typing import Final

FORMAT_ATOM: Final[str]
FORMAT_COOKIE: Final[str]
FORMAT_RFC822: Final[str]
FORMAT_RFC850: Final[str]
FORMAT_RFC1036: Final[str]
FORMAT_RFC1123: Final[str]
FORMAT_RFC2822: Final[str]
FORMAT_RFC3339: Final[str]
FORMAT_RSS: Final[str]
FORMAT_W3C: Final[str]

class DateTimeFormatter:
    locale: locales.Locale
    def __init__(self, locale: str = ...) -> None: ...
    def format(cls, dt: datetime, fmt: str) -> str: ...
