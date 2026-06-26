from . import Extension as Extension
from .. import util as util
from ..blockprocessors import BlockProcessor as BlockProcessor
from ..inlinepatterns import InlineProcessor as InlineProcessor
from ..postprocessors import Postprocessor as Postprocessor
from ..treeprocessors import Treeprocessor as Treeprocessor
from _typeshed import Incomplete

FN_BACKLINK_TEXT: Incomplete
NBSP_PLACEHOLDER: Incomplete
RE_REF_ID: Incomplete

class FootnoteExtension(Extension):
    """ Footnote Extension. """
    config: Incomplete
    unique_prefix: int
    found_refs: Incomplete
    used_refs: Incomplete
    def __init__(self, **kwargs) -> None:
        """ Setup configs. """
    parser: Incomplete
    md: Incomplete
    def extendMarkdown(self, md) -> None:
        """ Add pieces to Markdown. """
    footnotes: Incomplete
    def reset(self) -> None:
        """ Clear footnotes on reset, and prepare for distinct document. """
    def unique_ref(self, reference, found: bool = False):
        """ Get a unique reference if there are duplicates. """
    def findFootnotesPlaceholder(self, root):
        """ Return ElementTree Element that contains Footnote placeholder. """
    def setFootnote(self, id, text) -> None:
        """ Store a footnote for later retrieval. """
    def get_separator(self):
        """ Get the footnote separator. """
    def makeFootnoteId(self, id):
        """ Return footnote link id. """
    def makeFootnoteRefId(self, id, found: bool = False):
        """ Return footnote back-link id. """
    def makeFootnotesDiv(self, root):
        """ Return `div` of footnotes as `etree` Element. """

class FootnoteBlockProcessor(BlockProcessor):
    """ Find all footnote references and store for later use. """
    RE: Incomplete
    footnotes: Incomplete
    def __init__(self, footnotes) -> None: ...
    def test(self, parent, block): ...
    def run(self, parent, blocks):
        """ Find, set, and remove footnote definitions. """
    def detectTabbed(self, blocks):
        """ Find indented text and remove indent before further processing.

        Returns: a list of blocks with indentation removed.
        """
    def detab(self, block):
        """ Remove one level of indent from a block.

        Preserve lazily indented blocks by only removing indent from indented lines.
        """

class FootnoteInlineProcessor(InlineProcessor):
    """ `InlinePattern` for footnote markers in a document's body text. """
    footnotes: Incomplete
    def __init__(self, pattern, footnotes) -> None: ...
    def handleMatch(self, m, data): ...

class FootnotePostTreeprocessor(Treeprocessor):
    """ Amend footnote div with duplicates. """
    footnotes: Incomplete
    def __init__(self, footnotes) -> None: ...
    def add_duplicates(self, li, duplicates) -> None:
        """ Adjust current `li` and add the duplicates: `fnref2`, `fnref3`, etc. """
    def get_num_duplicates(self, li):
        """ Get the number of duplicate refs of the footnote. """
    def handle_duplicates(self, parent) -> None:
        """ Find duplicate footnotes and format and add the duplicates. """
    offset: int
    def run(self, root) -> None:
        """ Crawl the footnote div and add missing duplicate footnotes. """

class FootnoteTreeprocessor(Treeprocessor):
    """ Build and append footnote div to end of document. """
    footnotes: Incomplete
    def __init__(self, footnotes) -> None: ...
    def run(self, root) -> None: ...

class FootnotePostprocessor(Postprocessor):
    """ Replace placeholders with html entities. """
    footnotes: Incomplete
    def __init__(self, footnotes) -> None: ...
    def run(self, text): ...

def makeExtension(**kwargs):
    """ Return an instance of the `FootnoteExtension` """
