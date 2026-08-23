from . import css_types as ct, util as util
from .util import SelectorSyntaxError as SelectorSyntaxError
from _typeshed import Incomplete
from typing import Any, Iterator, Match

UNICODE_REPLACEMENT_CHAR: int
PSEUDO_SIMPLE: Incomplete
PSEUDO_SIMPLE_NO_MATCH: Incomplete
PSEUDO_COMPLEX: Incomplete
PSEUDO_COMPLEX_NO_MATCH: Incomplete
PSEUDO_SPECIAL: Incomplete
PSEUDO_SUPPORTED: Incomplete
NEWLINE: str
WS: Incomplete
COMMENTS: str
WSC: Incomplete
CSS_ESCAPES: Incomplete
CSS_STRING_ESCAPES: Incomplete
IDENTIFIER: Incomplete
NTH: Incomplete
VALUE: Incomplete
ATTR: Incomplete
PAT_ID: Incomplete
PAT_CLASS: Incomplete
PAT_TAG: Incomplete
PAT_ATTR: Incomplete
PAT_PSEUDO_CLASS: Incomplete
PAT_PSEUDO_CLASS_SPECIAL: Incomplete
PAT_PSEUDO_CLASS_CUSTOM: Incomplete
PAT_PSEUDO_CLOSE: Incomplete
PAT_PSEUDO_ELEMENT: Incomplete
PAT_AT_RULE: Incomplete
PAT_PSEUDO_NTH_CHILD: Incomplete
PAT_PSEUDO_NTH_TYPE: Incomplete
PAT_PSEUDO_LANG: Incomplete
PAT_PSEUDO_DIR: Incomplete
PAT_COMBINE: Incomplete
PAT_PSEUDO_CONTAINS: Incomplete
RE_CSS_ESC: Incomplete
RE_CSS_STR_ESC: Incomplete
RE_NTH: Incomplete
RE_VALUES: Incomplete
RE_WS: Incomplete
RE_WS_BEGIN: Incomplete
RE_WS_END: Incomplete
RE_CUSTOM: Incomplete
COMMA_COMBINATOR: str
WS_COMBINATOR: str
FLG_PSEUDO: int
FLG_NOT: int
FLG_RELATIVE: int
FLG_DEFAULT: int
FLG_HTML: int
FLG_INDETERMINATE: int
FLG_OPEN: int
FLG_IN_RANGE: int
FLG_OUT_OF_RANGE: int
FLG_PLACEHOLDER_SHOWN: int
FLG_FORGIVE: int

def process_custom(custom: ct.CustomSelectors | None) -> dict[str, str | ct.SelectorList]:
    """Process custom."""
def css_unescape(content: str, string: bool = False) -> str:
    """
    Unescape CSS value.

    Strings allow for spanning the value on multiple strings by escaping a new line.
    """
def escape(ident: str) -> str:
    """Escape identifier."""

class SelectorPattern:
    """Selector pattern."""
    name: Incomplete
    re_pattern: Incomplete
    def __init__(self, name: str, pattern: str) -> None:
        """Initialize."""
    def get_name(self) -> str:
        """Get name."""
    def match(self, selector: str, index: int, flags: int) -> Match[str] | None:
        """Match the selector."""

class SpecialPseudoPattern(SelectorPattern):
    """Selector pattern."""
    patterns: Incomplete
    matched_name: Incomplete
    re_pseudo_name: Incomplete
    def __init__(self, patterns: tuple[tuple[str, tuple[str, ...], str, type[SelectorPattern]], ...]) -> None:
        """Initialize."""
    def get_name(self) -> str:
        """Get name."""
    def match(self, selector: str, index: int, flags: int) -> Match[str] | None:
        """Match the selector."""

class _Selector:
    """
    Intermediate selector class.

    This stores selector data for a compound selector as we are acquiring them.
    Once we are done collecting the data for a compound selector, we freeze
    the data in an object that can be pickled and hashed.
    """
    tag: Incomplete
    ids: Incomplete
    classes: Incomplete
    attributes: Incomplete
    nth: Incomplete
    selectors: Incomplete
    relations: Incomplete
    rel_type: Incomplete
    contains: Incomplete
    lang: Incomplete
    flags: Incomplete
    no_match: Incomplete
    def __init__(self, **kwargs: Any) -> None:
        """Initialize."""
    def freeze(self) -> ct.Selector | ct.SelectorNull:
        """Freeze self."""

class CSSParser:
    """Parse CSS selectors."""
    css_tokens: Incomplete
    pattern: Incomplete
    flags: Incomplete
    debug: Incomplete
    custom: Incomplete
    def __init__(self, selector: str, custom: dict[str, str | ct.SelectorList] | None = None, flags: int = 0) -> None:
        """Initialize."""
    def parse_attribute_selector(self, sel: _Selector, m: Match[str], has_selector: bool) -> bool:
        """Create attribute selector from the returned regex match."""
    def parse_tag_pattern(self, sel: _Selector, m: Match[str], has_selector: bool) -> bool:
        """Parse tag pattern from regex match."""
    def parse_pseudo_class_custom(self, sel: _Selector, m: Match[str], has_selector: bool) -> bool:
        """
        Parse custom pseudo class alias.

        Compile custom selectors as we need them. When compiling a custom selector,
        set it to `None` in the dictionary so we can avoid an infinite loop.
        """
    def parse_pseudo_class(self, sel: _Selector, m: Match[str], has_selector: bool, iselector: Iterator[tuple[str, Match[str]]], is_html: bool) -> tuple[bool, bool]:
        """Parse pseudo class."""
    def parse_pseudo_nth(self, sel: _Selector, m: Match[str], has_selector: bool, iselector: Iterator[tuple[str, Match[str]]]) -> bool:
        """Parse `nth` pseudo."""
    def parse_pseudo_open(self, sel: _Selector, name: str, has_selector: bool, iselector: Iterator[tuple[str, Match[str]]], index: int) -> bool:
        """Parse pseudo with opening bracket."""
    def parse_has_combinator(self, sel: _Selector, m: Match[str], has_selector: bool, selectors: list[_Selector], rel_type: str, index: int) -> tuple[bool, _Selector, str]:
        """Parse combinator tokens."""
    def parse_combinator(self, sel: _Selector, m: Match[str], has_selector: bool, selectors: list[_Selector], relations: list[_Selector], is_pseudo: bool, is_forgive: bool, index: int) -> tuple[bool, _Selector]:
        """Parse combinator tokens."""
    def parse_class_id(self, sel: _Selector, m: Match[str], has_selector: bool) -> bool:
        """Parse HTML classes and ids."""
    def parse_pseudo_contains(self, sel: _Selector, m: Match[str], has_selector: bool) -> bool:
        """Parse contains."""
    def parse_pseudo_lang(self, sel: _Selector, m: Match[str], has_selector: bool) -> bool:
        """Parse pseudo language."""
    def parse_pseudo_dir(self, sel: _Selector, m: Match[str], has_selector: bool) -> bool:
        """Parse pseudo direction."""
    def parse_selectors(self, iselector: Iterator[tuple[str, Match[str]]], index: int = 0, flags: int = 0) -> ct.SelectorList:
        """Parse selectors."""
    def selector_iter(self, pattern: str) -> Iterator[tuple[str, Match[str]]]:
        """Iterate selector tokens."""
    def process_selectors(self, index: int = 0, flags: int = 0) -> ct.SelectorList:
        """Process selectors."""

CSS_LINK: Incomplete
CSS_CHECKED: Incomplete
CSS_DEFAULT: Incomplete
CSS_INDETERMINATE: Incomplete
CSS_DISABLED: Incomplete
CSS_ENABLED: Incomplete
CSS_REQUIRED: Incomplete
CSS_OPTIONAL: Incomplete
CSS_PLACEHOLDER_SHOWN: Incomplete
CSS_NTH_OF_S_DEFAULT: Incomplete
CSS_READ_WRITE: Incomplete
CSS_READ_ONLY: Incomplete
CSS_IN_RANGE: Incomplete
CSS_OUT_OF_RANGE: Incomplete
