import bs4
from . import css_match as cm
from .util import DEBUG as DEBUG, SelectorSyntaxError as SelectorSyntaxError
from typing import Any, Iterable, Iterator

__all__ = ['DEBUG', 'SelectorSyntaxError', 'SoupSieve', 'closest', 'compile', 'filter', 'iselect', 'match', 'select', 'select_one']

SoupSieve = cm.SoupSieve

def compile(pattern: str, namespaces: dict[str, str] | None = None, flags: int = 0, *, custom: dict[str, str] | None = None, **kwargs: Any) -> cm.SoupSieve:
    """Compile CSS pattern."""
def closest(select: str, tag: bs4.Tag, namespaces: dict[str, str] | None = None, flags: int = 0, *, custom: dict[str, str] | None = None, **kwargs: Any) -> bs4.Tag:
    """Match closest ancestor."""
def match(select: str, tag: bs4.Tag, namespaces: dict[str, str] | None = None, flags: int = 0, *, custom: dict[str, str] | None = None, **kwargs: Any) -> bool:
    """Match node."""
def filter(select: str, iterable: Iterable[bs4.Tag], namespaces: dict[str, str] | None = None, flags: int = 0, *, custom: dict[str, str] | None = None, **kwargs: Any) -> list[bs4.Tag]:
    """Filter list of nodes."""
def select_one(select: str, tag: bs4.Tag, namespaces: dict[str, str] | None = None, flags: int = 0, *, custom: dict[str, str] | None = None, **kwargs: Any) -> bs4.Tag:
    """Select a single tag."""
def select(select: str, tag: bs4.Tag, namespaces: dict[str, str] | None = None, limit: int = 0, flags: int = 0, *, custom: dict[str, str] | None = None, **kwargs: Any) -> list[bs4.Tag]:
    """Select the specified tags."""
def iselect(select: str, tag: bs4.Tag, namespaces: dict[str, str] | None = None, limit: int = 0, flags: int = 0, *, custom: dict[str, str] | None = None, **kwargs: Any) -> Iterator[bs4.Tag]:
    """Iterate the specified tags."""
