from . import util as util
from _typeshed import Incomplete

def build_postprocessors(md, **kwargs):
    """ Build the default postprocessors for Markdown. """

class Postprocessor(util.Processor):
    '''
    Postprocessors are run after the ElementTree it converted back into text.

    Each Postprocessor implements a "run" method that takes a pointer to a
    text string, modifies it as necessary and returns a text string.

    Postprocessors must extend markdown.Postprocessor.

    '''
    def run(self, text) -> None:
        """
        Subclasses of Postprocessor should implement a `run` method, which
        takes the html document as a single text string and returns a
        (possibly modified) string.

        """

class RawHtmlPostprocessor(Postprocessor):
    """ Restore raw html to the document. """
    BLOCK_LEVEL_REGEX: Incomplete
    def run(self, text):
        """ Iterate over html stash and restore html. """
    def isblocklevel(self, html): ...
    def stash_to_string(self, text):
        """ Convert a stashed object to a string. """

class AndSubstitutePostprocessor(Postprocessor):
    """ Restore valid entities """
    def run(self, text): ...

class UnescapePostprocessor(Postprocessor):
    """ Restore escaped chars """
    RE: Incomplete
    def unescape(self, m): ...
    def run(self, text): ...
