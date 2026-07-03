from . import Extension as Extension
from _typeshed import Incomplete

extensions: Incomplete

class ExtraExtension(Extension):
    """ Add various extensions to Markdown class."""
    config: Incomplete
    def __init__(self, **kwargs) -> None:
        """ `config` is a dumb holder which gets passed to the actual extension later. """
    def extendMarkdown(self, md) -> None:
        """ Register extension instances. """

def makeExtension(**kwargs): ...
