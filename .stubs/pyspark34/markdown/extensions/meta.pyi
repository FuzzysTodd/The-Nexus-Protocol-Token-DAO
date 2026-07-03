from . import Extension as Extension
from ..preprocessors import Preprocessor as Preprocessor
from _typeshed import Incomplete

log: Incomplete
META_RE: Incomplete
META_MORE_RE: Incomplete
BEGIN_RE: Incomplete
END_RE: Incomplete

class MetaExtension(Extension):
    """ Meta-Data extension for Python-Markdown. """
    md: Incomplete
    def extendMarkdown(self, md) -> None:
        """ Add `MetaPreprocessor` to Markdown instance. """
    def reset(self) -> None: ...

class MetaPreprocessor(Preprocessor):
    """ Get Meta-Data. """
    def run(self, lines):
        """ Parse Meta-Data and store in Markdown.Meta. """

def makeExtension(**kwargs): ...
