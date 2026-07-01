from . import base as base
from _typeshed import Incomplete

class Filter(base.Filter):
    """Injects ``<meta charset=ENCODING>`` tag into head of document"""
    encoding: Incomplete
    def __init__(self, source, encoding) -> None:
        """Creates a Filter

        :arg source: the source token stream

        :arg encoding: the encoding to set

        """
    def __iter__(self): ...
