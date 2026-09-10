from _typeshed import Incomplete
from html5lib import HTMLParser as _HTMLParser, XHTMLParser as _XHTMLParser
from lxml import etree as etree
from lxml.html import Element as Element, XHTML_NAMESPACE as XHTML_NAMESPACE

class HTMLParser(_HTMLParser):
    """An html5lib HTML parser with lxml as tree."""
    def __init__(self, strict: bool = False, **kwargs) -> None: ...

class XHTMLParser(_XHTMLParser):
    """An html5lib XHTML Parser with lxml as tree."""
    def __init__(self, strict: bool = False, **kwargs) -> None: ...

xhtml_parser: Incomplete

def document_fromstring(html, guess_charset: Incomplete | None = None, parser: Incomplete | None = None):
    """
    Parse a whole document into a string.

    If `guess_charset` is true, or if the input is not Unicode but a
    byte string, the `chardet` library will perform charset guessing
    on the string.
    """
def fragments_fromstring(html, no_leading_text: bool = False, guess_charset: Incomplete | None = None, parser: Incomplete | None = None):
    """Parses several HTML elements, returning a list of elements.

    The first item in the list may be a string.  If no_leading_text is true,
    then it will be an error if there is leading text, and it will always be
    a list of only elements.

    If `guess_charset` is true, the `chardet` library will perform charset
    guessing on the string.
    """
def fragment_fromstring(html, create_parent: bool = False, guess_charset: Incomplete | None = None, parser: Incomplete | None = None):
    """Parses a single HTML element; it is an error if there is more than
    one element, or if anything but whitespace precedes or follows the
    element.

    If 'create_parent' is true (or is a tag name) then a parent node
    will be created to encapsulate the HTML in a single element.  In
    this case, leading or trailing text is allowed.

    If `guess_charset` is true, the `chardet` library will perform charset
    guessing on the string.
    """
def fromstring(html, guess_charset: Incomplete | None = None, parser: Incomplete | None = None):
    """Parse the html, returning a single element/document.

    This tries to minimally parse the chunk of text, without knowing if it
    is a fragment or a document.

    'base_url' will set the document's base_url attribute (and the tree's
    docinfo.URL)

    If `guess_charset` is true, or if the input is not Unicode but a
    byte string, the `chardet` library will perform charset guessing
    on the string.
    """
def parse(filename_url_or_file, guess_charset: Incomplete | None = None, parser: Incomplete | None = None):
    """Parse a filename, URL, or file-like object into an HTML document
    tree.  Note: this returns a tree, not an element.  Use
    ``parse(...).getroot()`` to get the document root.

    If ``guess_charset`` is true, the ``useChardet`` option is passed into
    html5lib to enable character detection.  This option is on by default
    when parsing from URLs, off by default when parsing from file(-like)
    objects (which tend to return Unicode more often than not), and on by
    default when parsing from a file path (which is read in binary mode).
    """

html_parser: Incomplete
