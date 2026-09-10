from . import Extension as Extension
from ..inlinepatterns import InlineProcessor as InlineProcessor
from _typeshed import Incomplete

def build_url(label, base, end):
    """ Build a URL from the label, a base, and an end. """

class WikiLinkExtension(Extension):
    config: Incomplete
    def __init__(self, **kwargs) -> None: ...
    md: Incomplete
    def extendMarkdown(self, md) -> None: ...

class WikiLinksInlineProcessor(InlineProcessor):
    config: Incomplete
    def __init__(self, pattern, config) -> None: ...
    def handleMatch(self, m, data): ...

def makeExtension(**kwargs): ...
