from _typeshed import Incomplete

__all__ = ['fromstring', 'parse', 'convert_tree']

def fromstring(data, beautifulsoup: Incomplete | None = None, makeelement: Incomplete | None = None, **bsargs):
    """Parse a string of HTML data into an Element tree using the
    BeautifulSoup parser.

    Returns the root ``<html>`` Element of the tree.

    You can pass a different BeautifulSoup parser through the
    `beautifulsoup` keyword, and a diffent Element factory function
    through the `makeelement` keyword.  By default, the standard
    ``BeautifulSoup`` class and the default factory of `lxml.html` are
    used.
    """
def parse(file, beautifulsoup: Incomplete | None = None, makeelement: Incomplete | None = None, **bsargs):
    """Parse a file into an ElemenTree using the BeautifulSoup parser.

    You can pass a different BeautifulSoup parser through the
    `beautifulsoup` keyword, and a diffent Element factory function
    through the `makeelement` keyword.  By default, the standard
    ``BeautifulSoup`` class and the default factory of `lxml.html` are
    used.
    """
def convert_tree(beautiful_soup_tree, makeelement: Incomplete | None = None):
    """Convert a BeautifulSoup tree to a list of Element trees.

    Returns a list instead of a single root Element to support
    HTML-like soup with more than one root element.

    You can pass a different Element factory through the `makeelement`
    keyword.
    """

class _PseudoTag:
    name: str
    attrs: Incomplete
    contents: Incomplete
    def __init__(self, contents) -> None: ...
    def __iter__(self): ...
unichr = chr
