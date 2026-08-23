from typing import Any, Iterable, Iterator, Mapping, Pattern

__all__ = ['Selector', 'SelectorNull', 'SelectorTag', 'SelectorAttribute', 'SelectorContains', 'SelectorNth', 'SelectorLang', 'SelectorList', 'Namespaces', 'CustomSelectors']

class Immutable:
    """Immutable."""
    def __init__(self, **kwargs: Any) -> None:
        """Initialize."""
    @classmethod
    def __base__(cls) -> type[Immutable]:
        """Get base class."""
    def __eq__(self, other: Any) -> bool:
        """Equal."""
    def __ne__(self, other: Any) -> bool:
        """Equal."""
    def __hash__(self) -> int:
        """Hash."""
    def __setattr__(self, name: str, value: Any) -> None:
        """Prevent mutability."""
    def pretty(self) -> None:
        """Pretty print."""

class ImmutableDict(Mapping[Any, Any]):
    """Hashable, immutable dictionary."""
    def __init__(self, arg: dict[Any, Any] | Iterable[tuple[Any, Any]]) -> None:
        """Initialize."""
    def __iter__(self) -> Iterator[Any]:
        """Iterator."""
    def __len__(self) -> int:
        """Length."""
    def __getitem__(self, key: Any) -> Any:
        """Get item: `namespace['key']`."""
    def __hash__(self) -> int:
        """Hash."""

class Namespaces(ImmutableDict):
    """Namespaces."""
    def __init__(self, arg: dict[str, str] | Iterable[tuple[str, str]]) -> None:
        """Initialize."""

class CustomSelectors(ImmutableDict):
    """Custom selectors."""
    def __init__(self, arg: dict[str, str] | Iterable[tuple[str, str]]) -> None:
        """Initialize."""

class Selector(Immutable):
    """Selector."""
    tag: SelectorTag | None
    ids: tuple[str, ...]
    classes: tuple[str, ...]
    attributes: tuple[SelectorAttribute, ...]
    nth: tuple[SelectorNth, ...]
    selectors: tuple[SelectorList, ...]
    relation: SelectorList
    rel_type: str | None
    contains: tuple[SelectorContains, ...]
    lang: tuple[SelectorLang, ...]
    flags: int
    def __init__(self, tag: SelectorTag | None, ids: tuple[str, ...], classes: tuple[str, ...], attributes: tuple[SelectorAttribute, ...], nth: tuple[SelectorNth, ...], selectors: tuple[SelectorList, ...], relation: SelectorList, rel_type: str | None, contains: tuple[SelectorContains, ...], lang: tuple[SelectorLang, ...], flags: int) -> None:
        """Initialize."""

class SelectorNull(Immutable):
    """Null Selector."""
    def __init__(self) -> None:
        """Initialize."""

class SelectorTag(Immutable):
    """Selector tag."""
    name: str
    prefix: str | None
    def __init__(self, name: str, prefix: str | None) -> None:
        """Initialize."""

class SelectorAttribute(Immutable):
    """Selector attribute rule."""
    attribute: str
    prefix: str
    pattern: Pattern[str] | None
    xml_type_pattern: Pattern[str] | None
    def __init__(self, attribute: str, prefix: str, pattern: Pattern[str] | None, xml_type_pattern: Pattern[str] | None) -> None:
        """Initialize."""

class SelectorContains(Immutable):
    """Selector contains rule."""
    text: tuple[str, ...]
    own: bool
    def __init__(self, text: Iterable[str], own: bool) -> None:
        """Initialize."""

class SelectorNth(Immutable):
    """Selector nth type."""
    a: int
    n: bool
    b: int
    of_type: bool
    last: bool
    selectors: SelectorList
    def __init__(self, a: int, n: bool, b: int, of_type: bool, last: bool, selectors: SelectorList) -> None:
        """Initialize."""

class SelectorLang(Immutable):
    """Selector language rules."""
    languages: tuple[str, ...]
    def __init__(self, languages: Iterable[str]) -> None:
        """Initialize."""
    def __iter__(self) -> Iterator[str]:
        """Iterator."""
    def __len__(self) -> int:
        """Length."""
    def __getitem__(self, index: int) -> str:
        """Get item."""

class SelectorList(Immutable):
    """Selector list."""
    selectors: tuple[Selector | SelectorNull, ...]
    is_not: bool
    is_html: bool
    def __init__(self, selectors: Iterable[Selector | SelectorNull] | None = None, is_not: bool = False, is_html: bool = False) -> None:
        """Initialize."""
    def __iter__(self) -> Iterator[Selector | SelectorNull]:
        """Iterator."""
    def __len__(self) -> int:
        """Length."""
    def __getitem__(self, index: int) -> Selector | SelectorNull:
        """Get item."""
