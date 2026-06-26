import bs4
from . import css_types as ct, util as util
from _typeshed import Incomplete
from typing import Any, Iterable, Iterator, Sequence

RE_NOT_EMPTY: Incomplete
RE_NOT_WS: Incomplete
REL_PARENT: str
REL_CLOSE_PARENT: str
REL_SIBLING: str
REL_CLOSE_SIBLING: str
REL_HAS_PARENT: str
REL_HAS_CLOSE_PARENT: str
REL_HAS_SIBLING: str
REL_HAS_CLOSE_SIBLING: str
NS_XHTML: str
NS_XML: str
DIR_FLAGS: Incomplete
RANGES: Incomplete
DIR_MAP: Incomplete
RE_NUM: Incomplete
RE_TIME: Incomplete
RE_MONTH: Incomplete
RE_WEEK: Incomplete
RE_DATE: Incomplete
RE_DATETIME: Incomplete
RE_WILD_STRIP: Incomplete
MONTHS_30: Incomplete
FEB: int
SHORT_MONTH: int
LONG_MONTH: int
FEB_MONTH: int
FEB_LEAP_MONTH: int
DAYS_IN_WEEK: int

class _FakeParent:
    """
    Fake parent class.

    When we have a fragment with no `BeautifulSoup` document object,
    we can't evaluate `nth` selectors properly.  Create a temporary
    fake parent so we can traverse the root element as a child.
    """
    contents: Incomplete
    def __init__(self, element: bs4.Tag) -> None:
        """Initialize."""
    def __len__(self) -> bs4.PageElement:
        """Length."""

class _DocumentNav:
    """Navigate a Beautiful Soup document."""
    @classmethod
    def assert_valid_input(cls, tag: Any) -> None:
        """Check if valid input tag or document."""
    @staticmethod
    def is_doc(obj: bs4.Tag) -> bool:
        """Is `BeautifulSoup` object."""
    @staticmethod
    def is_tag(obj: bs4.PageElement) -> bool:
        """Is tag."""
    @staticmethod
    def is_declaration(obj: bs4.PageElement) -> bool:
        """Is declaration."""
    @staticmethod
    def is_cdata(obj: bs4.PageElement) -> bool:
        """Is CDATA."""
    @staticmethod
    def is_processing_instruction(obj: bs4.PageElement) -> bool:
        """Is processing instruction."""
    @staticmethod
    def is_navigable_string(obj: bs4.PageElement) -> bool:
        """Is navigable string."""
    @staticmethod
    def is_special_string(obj: bs4.PageElement) -> bool:
        """Is special string."""
    @classmethod
    def is_content_string(cls, obj: bs4.PageElement) -> bool:
        """Check if node is content string."""
    @staticmethod
    def create_fake_parent(el: bs4.Tag) -> _FakeParent:
        """Create fake parent for a given element."""
    @staticmethod
    def is_xml_tree(el: bs4.Tag) -> bool:
        """Check if element (or document) is from a XML tree."""
    def is_iframe(self, el: bs4.Tag) -> bool:
        """Check if element is an `iframe`."""
    def is_root(self, el: bs4.Tag) -> bool:
        """
        Return whether element is a root element.

        We check that the element is the root of the tree (which we have already pre-calculated),
        and we check if it is the root element under an `iframe`.
        """
    def get_contents(self, el: bs4.Tag, no_iframe: bool = False) -> Iterator[bs4.PageElement]:
        """Get contents or contents in reverse."""
    def get_children(self, el: bs4.Tag, start: int | None = None, reverse: bool = False, tags: bool = True, no_iframe: bool = False) -> Iterator[bs4.PageElement]:
        """Get children."""
    def get_descendants(self, el: bs4.Tag, tags: bool = True, no_iframe: bool = False) -> Iterator[bs4.PageElement]:
        """Get descendants."""
    def get_parent(self, el: bs4.Tag, no_iframe: bool = False) -> bs4.Tag:
        """Get parent."""
    @staticmethod
    def get_tag_name(el: bs4.Tag) -> str | None:
        """Get tag."""
    @staticmethod
    def get_prefix_name(el: bs4.Tag) -> str | None:
        """Get prefix."""
    @staticmethod
    def get_uri(el: bs4.Tag) -> str | None:
        """Get namespace `URI`."""
    @classmethod
    def get_next(cls, el: bs4.Tag, tags: bool = True) -> bs4.PageElement:
        """Get next sibling tag."""
    @classmethod
    def get_previous(cls, el: bs4.Tag, tags: bool = True) -> bs4.PageElement:
        """Get previous sibling tag."""
    @staticmethod
    def has_html_ns(el: bs4.Tag) -> bool:
        """
        Check if element has an HTML namespace.

        This is a bit different than whether a element is treated as having an HTML namespace,
        like we do in the case of `is_html_tag`.
        """
    @staticmethod
    def split_namespace(el: bs4.Tag, attr_name: str) -> tuple[str | None, str | None]:
        """Return namespace and attribute name without the prefix."""
    @classmethod
    def normalize_value(cls, value: Any) -> str | Sequence[str]:
        """Normalize the value to be a string or list of strings."""
    @classmethod
    def get_attribute_by_name(cls, el: bs4.Tag, name: str, default: str | Sequence[str] | None = None) -> str | Sequence[str] | None:
        """Get attribute by name."""
    @classmethod
    def iter_attributes(cls, el: bs4.Tag) -> Iterator[tuple[str, str | Sequence[str] | None]]:
        """Iterate attributes."""
    @classmethod
    def get_classes(cls, el: bs4.Tag) -> Sequence[str]:
        """Get classes."""
    def get_text(self, el: bs4.Tag, no_iframe: bool = False) -> str:
        """Get text."""
    def get_own_text(self, el: bs4.Tag, no_iframe: bool = False) -> list[str]:
        """Get Own Text."""

class Inputs:
    """Class for parsing and validating input items."""
    @staticmethod
    def validate_day(year: int, month: int, day: int) -> bool:
        """Validate day."""
    @staticmethod
    def validate_week(year: int, week: int) -> bool:
        """Validate week."""
    @staticmethod
    def validate_month(month: int) -> bool:
        """Validate month."""
    @staticmethod
    def validate_year(year: int) -> bool:
        """Validate year."""
    @staticmethod
    def validate_hour(hour: int) -> bool:
        """Validate hour."""
    @staticmethod
    def validate_minutes(minutes: int) -> bool:
        """Validate minutes."""
    @classmethod
    def parse_value(cls, itype: str, value: str | None) -> tuple[float, ...] | None:
        """Parse the input value."""

class CSSMatch(_DocumentNav):
    """Perform CSS matching."""
    tag: Incomplete
    cached_meta_lang: Incomplete
    cached_default_forms: Incomplete
    cached_indeterminate_forms: Incomplete
    selectors: Incomplete
    namespaces: Incomplete
    flags: Incomplete
    iframe_restrict: bool
    root: Incomplete
    scope: Incomplete
    has_html_namespace: Incomplete
    is_xml: Incomplete
    is_html: Incomplete
    def __init__(self, selectors: ct.SelectorList, scope: bs4.Tag, namespaces: ct.Namespaces | None, flags: int) -> None:
        """Initialize."""
    def supports_namespaces(self) -> bool:
        """Check if namespaces are supported in the HTML type."""
    def get_tag_ns(self, el: bs4.Tag) -> str:
        """Get tag namespace."""
    def is_html_tag(self, el: bs4.Tag) -> bool:
        """Check if tag is in HTML namespace."""
    def get_tag(self, el: bs4.Tag) -> str | None:
        """Get tag."""
    def get_prefix(self, el: bs4.Tag) -> str | None:
        """Get prefix."""
    def find_bidi(self, el: bs4.Tag) -> int | None:
        """Get directionality from element text."""
    def extended_language_filter(self, lang_range: str, lang_tag: str) -> bool:
        """Filter the language tags."""
    def match_attribute_name(self, el: bs4.Tag, attr: str, prefix: str | None) -> str | Sequence[str] | None:
        """Match attribute name and return value if it exists."""
    def match_namespace(self, el: bs4.Tag, tag: ct.SelectorTag) -> bool:
        """Match the namespace of the element."""
    def match_attributes(self, el: bs4.Tag, attributes: tuple[ct.SelectorAttribute, ...]) -> bool:
        """Match attributes."""
    def match_tagname(self, el: bs4.Tag, tag: ct.SelectorTag) -> bool:
        """Match tag name."""
    def match_tag(self, el: bs4.Tag, tag: ct.SelectorTag | None) -> bool:
        """Match the tag."""
    def match_past_relations(self, el: bs4.Tag, relation: ct.SelectorList) -> bool:
        """Match past relationship."""
    def match_future_child(self, parent: bs4.Tag, relation: ct.SelectorList, recursive: bool = False) -> bool:
        """Match future child."""
    def match_future_relations(self, el: bs4.Tag, relation: ct.SelectorList) -> bool:
        """Match future relationship."""
    def match_relations(self, el: bs4.Tag, relation: ct.SelectorList) -> bool:
        """Match relationship to other elements."""
    def match_id(self, el: bs4.Tag, ids: tuple[str, ...]) -> bool:
        """Match element's ID."""
    def match_classes(self, el: bs4.Tag, classes: tuple[str, ...]) -> bool:
        """Match element's classes."""
    def match_root(self, el: bs4.Tag) -> bool:
        """Match element as root."""
    def match_scope(self, el: bs4.Tag) -> bool:
        """Match element as scope."""
    def match_nth_tag_type(self, el: bs4.Tag, child: bs4.Tag) -> bool:
        """Match tag type for `nth` matches."""
    def match_nth(self, el: bs4.Tag, nth: bs4.Tag) -> bool:
        """Match `nth` elements."""
    def match_empty(self, el: bs4.Tag) -> bool:
        """Check if element is empty (if requested)."""
    def match_subselectors(self, el: bs4.Tag, selectors: tuple[ct.SelectorList, ...]) -> bool:
        """Match selectors."""
    def match_contains(self, el: bs4.Tag, contains: tuple[ct.SelectorContains, ...]) -> bool:
        """Match element if it contains text."""
    def match_default(self, el: bs4.Tag) -> bool:
        """Match default."""
    def match_indeterminate(self, el: bs4.Tag) -> bool:
        """Match default."""
    def match_lang(self, el: bs4.Tag, langs: tuple[ct.SelectorLang, ...]) -> bool:
        """Match languages."""
    def match_dir(self, el: bs4.Tag, directionality: int) -> bool:
        """Check directionality."""
    def match_range(self, el: bs4.Tag, condition: int) -> bool:
        """
        Match range.

        Behavior is modeled after what we see in browsers. Browsers seem to evaluate
        if the value is out of range, and if not, it is in range. So a missing value
        will not evaluate out of range; therefore, value is in range. Personally, I
        feel like this should evaluate as neither in or out of range.
        """
    def match_defined(self, el: bs4.Tag) -> bool:
        """
        Match defined.

        `:defined` is related to custom elements in a browser.

        - If the document is XML (not XHTML), all tags will match.
        - Tags that are not custom (don't have a hyphen) are marked defined.
        - If the tag has a prefix (without or without a namespace), it will not match.

        This is of course requires the parser to provide us with the proper prefix and namespace info,
        if it doesn't, there is nothing we can do.
        """
    def match_placeholder_shown(self, el: bs4.Tag) -> bool:
        """
        Match placeholder shown according to HTML spec.

        - text area should be checked if they have content. A single newline does not count as content.

        """
    def match_selectors(self, el: bs4.Tag, selectors: ct.SelectorList) -> bool:
        """Check if element matches one of the selectors."""
    def select(self, limit: int = 0) -> Iterator[bs4.Tag]:
        """Match all tags under the targeted tag."""
    def closest(self) -> bs4.Tag | None:
        """Match closest ancestor."""
    def filter(self) -> list[bs4.Tag]:
        """Filter tag's children."""
    def match(self, el: bs4.Tag) -> bool:
        """Match."""

class SoupSieve(ct.Immutable):
    """Compiled Soup Sieve selector matching object."""
    pattern: str
    selectors: ct.SelectorList
    namespaces: ct.Namespaces | None
    custom: dict[str, str]
    flags: int
    def __init__(self, pattern: str, selectors: ct.SelectorList, namespaces: ct.Namespaces | None, custom: ct.CustomSelectors | None, flags: int) -> None:
        """Initialize."""
    def match(self, tag: bs4.Tag) -> bool:
        """Match."""
    def closest(self, tag: bs4.Tag) -> bs4.Tag:
        """Match closest ancestor."""
    def filter(self, iterable: Iterable[bs4.Tag]) -> list[bs4.Tag]:
        """
        Filter.

        `CSSMatch` can cache certain searches for tags of the same document,
        so if we are given a tag, all tags are from the same document,
        and we can take advantage of the optimization.

        Any other kind of iterable could have tags from different documents or detached tags,
        so for those, we use a new `CSSMatch` for each item in the iterable.
        """
    def select_one(self, tag: bs4.Tag) -> bs4.Tag:
        """Select a single tag."""
    def select(self, tag: bs4.Tag, limit: int = 0) -> list[bs4.Tag]:
        """Select the specified tags."""
    def iselect(self, tag: bs4.Tag, limit: int = 0) -> Iterator[bs4.Tag]:
        """Iterate the specified tags."""
