from _typeshed import Incomplete
from html.parser import HTMLParser

__all__ = ['citation2latex']

def citation2latex(s):
    '''Parse citations in Markdown cells.

    This looks for HTML tags having a data attribute names ``data-cite``
    and replaces it by the call to LaTeX cite command. The transformation
    looks like this::

        <cite data-cite="granger">(Granger, 2013)</cite>

    Becomes ::

        \\cite{granger}

    Any HTML tag can be used, which allows the citations to be formatted
    in HTML in any manner.
    '''

class CitationParser(HTMLParser):
    """Citation Parser

    Replaces html tags with data-cite attribute with respective latex \\cite.

    Inherites from HTMLParser, overrides:
     - handle_starttag
     - handle_endtag
    """
    opentags: Incomplete
    citelist: Incomplete
    citetag: Incomplete
    def __init__(self) -> None:
        """Initialize the parser."""
    def get_offset(self):
        """Get the offset position."""
    def handle_starttag(self, tag, attrs) -> None:
        """Handle a start tag."""
    def handle_endtag(self, tag) -> None:
        """Handle an end tag."""
    data: Incomplete
    def feed(self, data) -> None:
        """Handle a feed."""
