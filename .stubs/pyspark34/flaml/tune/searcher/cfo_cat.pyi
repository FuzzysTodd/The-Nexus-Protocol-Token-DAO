from .blendsearch import CFO as CFO
from .flow2 import FLOW2 as FLOW2

class FLOW2Cat(FLOW2):
    """Local search algorithm optimized for categorical variables."""

class CFOCat(CFO):
    """CFO optimized for categorical variables."""
    LocalSearch = FLOW2Cat
