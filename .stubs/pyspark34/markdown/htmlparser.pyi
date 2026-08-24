from _typeshed import Incomplete

spec: Incomplete
htmlparser: Incomplete
blank_line_re: Incomplete

class HTMLExtractor(htmlparser.HTMLParser):
    """
    Extract raw HTML from text.

    The raw HTML is stored in the `htmlStash` of the Markdown instance passed
    to `md` and the remaining text is stored in `cleandoc` as a list of strings.
    """
    empty_tags: Incomplete
    md: Incomplete
    def __init__(self, md, *args, **kwargs) -> None: ...
    inraw: bool
    intail: bool
    stack: Incomplete
    cleandoc: Incomplete
    def reset(self) -> None:
        """Reset this instance.  Loses all unprocessed data."""
    def close(self) -> None:
        """Handle any buffered data."""
    @property
    def line_offset(self):
        """Returns char index in `self.rawdata` for the start of the current line. """
    def at_line_start(self):
        """
        Returns True if current position is at start of line.

        Allows for up to three blank spaces at start of line.
        """
    def get_endtag_text(self, tag):
        """
        Returns the text of the end tag.

        If it fails to extract the actual text from the raw data, it builds a closing tag with `tag`.
        """
    def handle_starttag(self, tag, attrs) -> None: ...
    def handle_endtag(self, tag) -> None: ...
    def handle_data(self, data) -> None: ...
    def handle_empty_tag(self, data, is_block) -> None:
        """ Handle empty tags (`<data>`). """
    def handle_startendtag(self, tag, attrs) -> None: ...
    def handle_charref(self, name) -> None: ...
    def handle_entityref(self, name) -> None: ...
    def handle_comment(self, data) -> None: ...
    def handle_decl(self, data) -> None: ...
    def handle_pi(self, data) -> None: ...
    def unknown_decl(self, data) -> None: ...
    def parse_pi(self, i): ...
    def parse_html_declaration(self, i): ...
    def get_starttag_text(self):
        """Return full source of start tag: `<...>`."""
    lasttag: Incomplete
    def parse_starttag(self, i): ...
