import abc
from jedi.inference.names import AbstractArbitraryName as AbstractArbitraryName
from typing import Dict

pydoc_topics: Dict[str, str] | None

class KeywordName(AbstractArbitraryName, metaclass=abc.ABCMeta):
    api_type: str
    def py__doc__(self): ...

def imitate_pydoc(string):
    """
    It's not possible to get the pydoc's without starting the annoying pager
    stuff.
    """
