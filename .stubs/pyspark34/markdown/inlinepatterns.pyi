from . import util as util
from _typeshed import Incomplete
from typing import NamedTuple

def build_inlinepatterns(md, **kwargs):
    """ Build the default set of inline patterns for Markdown. """

NOIMG: str
BACKTICK_RE: str
ESCAPE_RE: str
EMPHASIS_RE: str
STRONG_RE: str
SMART_STRONG_RE: str
SMART_EMPHASIS_RE: str
SMART_STRONG_EM_RE: str
EM_STRONG_RE: str
EM_STRONG2_RE: str
STRONG_EM_RE: str
STRONG_EM2_RE: str
STRONG_EM3_RE: str
LINK_RE: Incomplete
IMAGE_LINK_RE: str
REFERENCE_RE = LINK_RE
IMAGE_REFERENCE_RE = IMAGE_LINK_RE
NOT_STRONG_RE: str
AUTOLINK_RE: str
AUTOMAIL_RE: str
HTML_RE: str
ENTITY_RE: str
LINE_BREAK_RE: str

def dequote(string):
    """Remove quotes from around a string."""

class EmStrongItem(NamedTuple('EmStrongItem', [('pattern', Incomplete), ('builder', Incomplete), ('tags', Incomplete)])):
    """Emphasis/strong pattern item."""

class Pattern:
    """Base class that inline patterns subclass. """
    ANCESTOR_EXCLUDES: Incomplete
    pattern: Incomplete
    compiled_re: Incomplete
    md: Incomplete
    def __init__(self, pattern, md: Incomplete | None = None) -> None:
        """
        Create an instant of an inline pattern.

        Keyword arguments:

        * pattern: A regular expression that matches a pattern

        """
    def getCompiledRegExp(self):
        """ Return a compiled regular expression. """
    def handleMatch(self, m) -> None:
        """Return a ElementTree element from the given match.

        Subclasses should override this method.

        Keyword arguments:

        * m: A re match object containing a match of the pattern.

        """
    def type(self):
        """ Return class name, to define pattern type """
    def unescape(self, text):
        """ Return unescaped text given text with an inline placeholder. """

class InlineProcessor(Pattern):
    """
    Base class that inline patterns subclass.

    This is the newer style inline processor that uses a more
    efficient and flexible search approach.
    """
    pattern: Incomplete
    compiled_re: Incomplete
    safe_mode: bool
    md: Incomplete
    def __init__(self, pattern, md: Incomplete | None = None) -> None:
        """
        Create an instant of an inline pattern.

        Keyword arguments:

        * pattern: A regular expression that matches a pattern

        """
    def handleMatch(self, m, data) -> None:
        """Return a ElementTree element from the given match and the
        start and end index of the matched text.

        If `start` and/or `end` are returned as `None`, it will be
        assumed that the processor did not find a valid region of text.

        Subclasses should override this method.

        Keyword arguments:

        * m: A re match object containing a match of the pattern.
        * data: The buffer current under analysis

        Returns:

        * el: The ElementTree element, text or None.
        * start: The start of the region that has been matched or None.
        * end: The end of the region that has been matched or None.

        """

class SimpleTextPattern(Pattern):
    """ Return a simple text of group(2) of a Pattern. """
    def handleMatch(self, m): ...

class SimpleTextInlineProcessor(InlineProcessor):
    """ Return a simple text of group(1) of a Pattern. """
    def handleMatch(self, m, data): ...

class EscapeInlineProcessor(InlineProcessor):
    """ Return an escaped character. """
    def handleMatch(self, m, data): ...

class SimpleTagPattern(Pattern):
    """
    Return element of type `tag` with a text attribute of group(3)
    of a Pattern.

    """
    tag: Incomplete
    def __init__(self, pattern, tag) -> None: ...
    def handleMatch(self, m): ...

class SimpleTagInlineProcessor(InlineProcessor):
    """
    Return element of type `tag` with a text attribute of group(2)
    of a Pattern.

    """
    tag: Incomplete
    def __init__(self, pattern, tag) -> None: ...
    def handleMatch(self, m, data): ...

class SubstituteTagPattern(SimpleTagPattern):
    """ Return an element of type `tag` with no children. """
    def handleMatch(self, m): ...

class SubstituteTagInlineProcessor(SimpleTagInlineProcessor):
    """ Return an element of type `tag` with no children. """
    def handleMatch(self, m, data): ...

class BacktickInlineProcessor(InlineProcessor):
    """ Return a `<code>` element containing the matching text. """
    ESCAPED_BSLASH: Incomplete
    tag: str
    def __init__(self, pattern) -> None: ...
    def handleMatch(self, m, data): ...

class DoubleTagPattern(SimpleTagPattern):
    """Return a ElementTree element nested in tag2 nested in tag1.

    Useful for strong emphasis etc.

    """
    def handleMatch(self, m): ...

class DoubleTagInlineProcessor(SimpleTagInlineProcessor):
    """Return a ElementTree element nested in tag2 nested in tag1.

    Useful for strong emphasis etc.

    """
    def handleMatch(self, m, data): ...

class HtmlInlineProcessor(InlineProcessor):
    """ Store raw inline html and return a placeholder. """
    def handleMatch(self, m, data): ...
    def unescape(self, text):
        """ Return unescaped text given text with an inline placeholder. """
    def backslash_unescape(self, text):
        """ Return text with backslash escapes undone (backslashes are restored). """

class AsteriskProcessor(InlineProcessor):
    """Emphasis processor for handling strong and em matches inside asterisks."""
    PATTERNS: Incomplete
    def build_single(self, m, tag, idx):
        """Return single tag."""
    def build_double(self, m, tags, idx):
        """Return double tag."""
    def build_double2(self, m, tags, idx):
        """Return double tags (variant 2): `<strong>text <em>text</em></strong>`."""
    def parse_sub_patterns(self, data, parent, last, idx) -> None:
        """
        Parses sub patterns.

        `data` (`str`):
            text to evaluate.

        `parent` (`etree.Element`):
            Parent to attach text and sub elements to.

        `last` (`etree.Element`):
            Last appended child to parent. Can also be None if parent has no children.

        `idx` (`int`):
            Current pattern index that was used to evaluate the parent.

        """
    def build_element(self, m, builder, tags, index):
        """Element builder."""
    def handleMatch(self, m, data):
        """Parse patterns."""

class UnderscoreProcessor(AsteriskProcessor):
    """Emphasis processor for handling strong and em matches inside underscores."""
    PATTERNS: Incomplete

class LinkInlineProcessor(InlineProcessor):
    """ Return a link element from the given match. """
    RE_LINK: Incomplete
    RE_TITLE_CLEAN: Incomplete
    def handleMatch(self, m, data): ...
    def getLink(self, data, index):
        """Parse data between `()` of `[Text]()` allowing recursive `()`. """
    def getText(self, data, index):
        """Parse the content between `[]` of the start of an image or link
        resolving nested square brackets.

        """

class ImageInlineProcessor(LinkInlineProcessor):
    """ Return a `img` element from the given match. """
    def handleMatch(self, m, data): ...

class ReferenceInlineProcessor(LinkInlineProcessor):
    """ Match to a stored reference and return link element. """
    NEWLINE_CLEANUP_RE: Incomplete
    RE_LINK: Incomplete
    def handleMatch(self, m, data): ...
    def evalId(self, data, index, text):
        """
        Evaluate the id portion of [ref][id].

        If [ref][] use [ref].
        """
    def makeTag(self, href, title, text): ...

class ShortReferenceInlineProcessor(ReferenceInlineProcessor):
    """Short form of reference: [google]. """
    def evalId(self, data, index, text):
        """Evaluate the id from of [ref]  """

class ImageReferenceInlineProcessor(ReferenceInlineProcessor):
    """ Match to a stored reference and return `img` element. """
    def makeTag(self, href, title, text): ...

class ShortImageReferenceInlineProcessor(ImageReferenceInlineProcessor):
    """ Short form of image reference: `![ref]`. """
    def evalId(self, data, index, text):
        """Evaluate the id from of [ref]  """

class AutolinkInlineProcessor(InlineProcessor):
    """ Return a link Element given an auto-link (`<http://example/com>`). """
    def handleMatch(self, m, data): ...

class AutomailInlineProcessor(InlineProcessor):
    """
    Return a `mailto` link Element given an auto-mail link (`<foo@example.com>`).
    """
    def handleMatch(self, m, data): ...
