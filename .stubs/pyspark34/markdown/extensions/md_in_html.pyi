from . import Extension as Extension
from .. import util as util
from ..blockprocessors import BlockProcessor as BlockProcessor
from ..htmlparser import HTMLExtractor as HTMLExtractor, blank_line_re as blank_line_re
from ..postprocessors import RawHtmlPostprocessor as RawHtmlPostprocessor
from ..preprocessors import Preprocessor as Preprocessor
from _typeshed import Incomplete

class HTMLExtractorExtra(HTMLExtractor):
    """
    Override `HTMLExtractor` and create `etree` `Elements` for any elements which should have content parsed as
    Markdown.
    """
    block_level_tags: Incomplete
    span_tags: Incomplete
    raw_tags: Incomplete
    block_tags: Incomplete
    span_and_blocks_tags: Incomplete
    def __init__(self, md, *args, **kwargs) -> None: ...
    mdstack: Incomplete
    treebuilder: Incomplete
    mdstate: Incomplete
    def reset(self) -> None:
        """Reset this instance.  Loses all unprocessed data."""
    def close(self) -> None:
        """Handle any buffered data."""
    def get_element(self):
        """ Return element from `treebuilder` and reset `treebuilder` for later use. """
    def get_state(self, tag, attrs):
        """ Return state from tag and `markdown` attribute. One of 'block', 'span', or 'off'. """
    def handle_starttag(self, tag, attrs) -> None: ...
    state: Incomplete
    intail: bool
    def handle_endtag(self, tag) -> None: ...
    def handle_startendtag(self, tag, attrs) -> None: ...
    def handle_data(self, data) -> None: ...
    def handle_empty_tag(self, data, is_block) -> None: ...
    def parse_pi(self, i): ...
    def parse_html_declaration(self, i): ...

class HtmlBlockPreprocessor(Preprocessor):
    """Remove html blocks from the text and store them for later retrieval."""
    def run(self, lines): ...

class MarkdownInHtmlProcessor(BlockProcessor):
    """Process Markdown Inside HTML Blocks which have been stored in the `HtmlStash`."""
    def test(self, parent, block): ...
    def parse_element_content(self, element) -> None:
        """
        Recursively parse the text content of an `etree` Element as Markdown.

        Any block level elements generated from the Markdown will be inserted as children of the element in place
        of the text content. All `markdown` attributes are removed. For any elements in which Markdown parsing has
        been disabled, the text content of it and its children are wrapped in an `AtomicString`.
        """
    def run(self, parent, blocks): ...

class MarkdownInHTMLPostprocessor(RawHtmlPostprocessor):
    def stash_to_string(self, text):
        """ Override default to handle any `etree` elements still in the stash. """

class MarkdownInHtmlExtension(Extension):
    """Add Markdown parsing in HTML to Markdown class."""
    def extendMarkdown(self, md) -> None:
        """ Register extension instances. """

def makeExtension(**kwargs): ...
