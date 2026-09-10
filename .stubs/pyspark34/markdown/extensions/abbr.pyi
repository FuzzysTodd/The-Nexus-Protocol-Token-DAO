from . import Extension as Extension
from ..blockprocessors import BlockProcessor as BlockProcessor
from ..inlinepatterns import InlineProcessor as InlineProcessor
from ..util import AtomicString as AtomicString
from _typeshed import Incomplete

class AbbrExtension(Extension):
    """ Abbreviation Extension for Python-Markdown. """
    def extendMarkdown(self, md) -> None:
        """ Insert `AbbrPreprocessor` before `ReferencePreprocessor`. """

class AbbrPreprocessor(BlockProcessor):
    """ Abbreviation Preprocessor - parse text for abbr references. """
    RE: Incomplete
    def test(self, parent, block): ...
    def run(self, parent, blocks):
        """
        Find and remove all Abbreviation references from the text.
        Each reference is set as a new `AbbrPattern` in the markdown instance.

        """

class AbbrInlineProcessor(InlineProcessor):
    """ Abbreviation inline pattern. """
    title: Incomplete
    def __init__(self, pattern, title) -> None: ...
    def handleMatch(self, m, data): ...

def makeExtension(**kwargs): ...
