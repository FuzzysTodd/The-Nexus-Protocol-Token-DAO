from _typeshed import Incomplete
from django.urls.resolvers import URLPattern as URLPattern, URLResolver as URLResolver
from re import Pattern
from sentry_sdk._types import TYPE_CHECKING as TYPE_CHECKING
from typing import Tuple

def get_regex(resolver_or_pattern: URLPattern | URLResolver) -> Pattern[str]:
    """Utility method for django's deprecated resolver.regex"""

class RavenResolver:
    def resolve(self, path: str, urlconf: None | Tuple[URLPattern, URLPattern, URLResolver] | Tuple[URLPattern] = None) -> str | None: ...

LEGACY_RESOLVER: Incomplete
