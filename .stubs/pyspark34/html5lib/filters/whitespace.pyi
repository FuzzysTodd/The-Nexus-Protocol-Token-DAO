from . import base as base
from ..constants import rcdataElements as rcdataElements, spaceCharacters as spaceCharacters
from _typeshed import Incomplete

SPACES_REGEX: Incomplete

class Filter(base.Filter):
    """Collapses whitespace except in pre, textarea, and script elements"""
    spacePreserveElements: Incomplete
    def __iter__(self): ...

def collapse_spaces(text): ...
