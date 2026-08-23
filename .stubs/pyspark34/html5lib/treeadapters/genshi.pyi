from _typeshed import Incomplete
from collections.abc import Generator

def to_genshi(walker) -> Generator[Incomplete, None, None]:
    """Convert a tree to a genshi tree

    :arg walker: the treewalker to use to walk the tree to convert it

    :returns: generator of genshi nodes

    """
