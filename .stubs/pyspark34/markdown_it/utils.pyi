from collections.abc import MutableMapping as MutableMappingABC
from pathlib import Path
from typing import Any, Callable, Iterable, MutableMapping, TypedDict

EnvType = MutableMapping[str, Any]

class OptionsType(TypedDict):
    """Options for parsing."""
    maxNesting: int
    html: bool
    linkify: bool
    typographer: bool
    quotes: str
    xhtmlOut: bool
    breaks: bool
    langPrefix: str
    highlight: Callable[[str, str, str], str] | None

class PresetType(TypedDict):
    """Preset configuration for markdown-it."""
    options: OptionsType
    components: MutableMapping[str, MutableMapping[str, list[str]]]

class OptionsDict(MutableMappingABC):
    """A dictionary, with attribute access to core markdownit configuration options."""
    def __init__(self, options: OptionsType) -> None: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> Iterable[str]: ...
    def __len__(self) -> int: ...
    @property
    def maxNesting(self) -> int:
        """Internal protection, recursion limit."""
    @maxNesting.setter
    def maxNesting(self, value: int) -> None: ...
    @property
    def html(self) -> bool:
        """Enable HTML tags in source."""
    @html.setter
    def html(self, value: bool) -> None: ...
    @property
    def linkify(self) -> bool:
        """Enable autoconversion of URL-like texts to links."""
    @linkify.setter
    def linkify(self, value: bool) -> None: ...
    @property
    def typographer(self) -> bool:
        """Enable smartquotes and replacements."""
    @typographer.setter
    def typographer(self, value: bool) -> None: ...
    @property
    def quotes(self) -> str:
        """Quote characters."""
    @quotes.setter
    def quotes(self, value: str) -> None: ...
    @property
    def xhtmlOut(self) -> bool:
        """Use '/' to close single tags (<br />)."""
    @xhtmlOut.setter
    def xhtmlOut(self, value: bool) -> None: ...
    @property
    def breaks(self) -> bool:
        """Convert newlines in paragraphs into <br>."""
    @breaks.setter
    def breaks(self, value: bool) -> None: ...
    @property
    def langPrefix(self) -> str:
        """CSS language prefix for fenced blocks."""
    @langPrefix.setter
    def langPrefix(self, value: str) -> None: ...
    @property
    def highlight(self) -> Callable[[str, str, str], str] | None:
        """Highlighter function: (content, langName, langAttrs) -> escaped HTML."""
    @highlight.setter
    def highlight(self, value: Callable[[str, str, str], str] | None) -> None: ...

def read_fixture_file(path: str | Path) -> list[list[Any]]: ...
