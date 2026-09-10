from . import util as util
from .htmlparser import HTMLExtractor as HTMLExtractor

def build_preprocessors(md, **kwargs):
    """ Build the default set of preprocessors used by Markdown. """

class Preprocessor(util.Processor):
    '''
    Preprocessors are run after the text is broken into lines.

    Each preprocessor implements a "run" method that takes a pointer to a
    list of lines of the document, modifies it as necessary and returns
    either the same pointer or a pointer to a new list.

    Preprocessors must extend markdown.Preprocessor.

    '''
    def run(self, lines) -> None:
        """
        Each subclass of Preprocessor should override the `run` method, which
        takes the document as a list of strings split by newlines and returns
        the (possibly modified) list of lines.

        """

class NormalizeWhitespace(Preprocessor):
    """ Normalize whitespace for consistent parsing. """
    def run(self, lines): ...

class HtmlBlockPreprocessor(Preprocessor):
    """Remove html blocks from the text and store them for later retrieval."""
    def run(self, lines): ...
