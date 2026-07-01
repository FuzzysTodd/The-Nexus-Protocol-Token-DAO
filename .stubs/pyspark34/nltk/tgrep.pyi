from _typeshed import Incomplete
from collections.abc import Generator

class TgrepException(Exception):
    """Tgrep exception type."""

def ancestors(node):
    """
    Returns the list of all nodes dominating the given tree node.
    This method will not work with leaf nodes, since there is no way
    to recover the parent.
    """
def unique_ancestors(node):
    """
    Returns the list of all nodes dominating the given node, where
    there is only a single path of descent.
    """
def tgrep_tokenize(tgrep_string):
    """
    Tokenizes a TGrep search string into separate tokens.
    """
def tgrep_compile(tgrep_string):
    """
    Parses (and tokenizes, if necessary) a TGrep search string into a
    lambda function.
    """
def treepositions_no_leaves(tree):
    """
    Returns all the tree positions in the given tree which are not
    leaf nodes.
    """
def tgrep_positions(pattern, trees, search_leaves: bool = True) -> Generator[Incomplete, None, None]:
    """
    Return the tree positions in the trees which match the given pattern.

    :param pattern: a tgrep search pattern
    :type pattern: str or output of tgrep_compile()
    :param trees: a sequence of NLTK trees (usually ParentedTrees)
    :type trees: iter(ParentedTree) or iter(Tree)
    :param search_leaves: whether to return matching leaf nodes
    :type search_leaves: bool
    :rtype: iter(tree positions)
    """
def tgrep_nodes(pattern, trees, search_leaves: bool = True) -> Generator[Incomplete, None, None]:
    """
    Return the tree nodes in the trees which match the given pattern.

    :param pattern: a tgrep search pattern
    :type pattern: str or output of tgrep_compile()
    :param trees: a sequence of NLTK trees (usually ParentedTrees)
    :type trees: iter(ParentedTree) or iter(Tree)
    :param search_leaves: whether to return matching leaf nodes
    :type search_leaves: bool
    :rtype: iter(tree nodes)
    """
