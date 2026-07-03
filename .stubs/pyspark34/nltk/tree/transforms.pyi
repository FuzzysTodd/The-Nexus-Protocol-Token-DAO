from _typeshed import Incomplete

__all__ = ['chomsky_normal_form', 'un_chomsky_normal_form', 'collapse_unary']

def chomsky_normal_form(tree, factor: str = 'right', horzMarkov: Incomplete | None = None, vertMarkov: int = 0, childChar: str = '|', parentChar: str = '^') -> None: ...
def un_chomsky_normal_form(tree, expandUnary: bool = True, childChar: str = '|', parentChar: str = '^', unaryChar: str = '+') -> None: ...
def collapse_unary(tree, collapsePOS: bool = False, collapseRoot: bool = False, joinChar: str = '+') -> None:
    '''
    Collapse subtrees with a single child (ie. unary productions)
    into a new non-terminal (Tree node) joined by \'joinChar\'.
    This is useful when working with algorithms that do not allow
    unary productions, and completely removing the unary productions
    would require loss of useful information.  The Tree is modified
    directly (since it is passed by reference) and no value is returned.

    :param tree: The Tree to be collapsed
    :type  tree: Tree
    :param collapsePOS: \'False\' (default) will not collapse the parent of leaf nodes (ie.
                        Part-of-Speech tags) since they are always unary productions
    :type  collapsePOS: bool
    :param collapseRoot: \'False\' (default) will not modify the root production
                         if it is unary.  For the Penn WSJ treebank corpus, this corresponds
                         to the TOP -> productions.
    :type collapseRoot: bool
    :param joinChar: A string used to connect collapsed node values (default = "+")
    :type  joinChar: str
    '''
