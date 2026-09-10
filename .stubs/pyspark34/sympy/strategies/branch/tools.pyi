from .core import exhaust as exhaust, multiplex as multiplex
from .traverse import top_down as top_down

def canon(*rules):
    """ Strategy for canonicalization

    Apply each branching rule in a top-down fashion through the tree.
    Multiplex through all branching rule traversals
    Keep doing this until there is no change.
    """
