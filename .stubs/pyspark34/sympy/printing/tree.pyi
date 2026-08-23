def pprint_nodes(subtrees):
    '''
    Prettyprints systems of nodes.

    Examples
    ========

    >>> from sympy.printing.tree import pprint_nodes
    >>> print(pprint_nodes(["a", "b1\\nb2", "c"]))
    +-a
    +-b1
    | b2
    +-c

    '''
def print_node(node, assumptions: bool = True):
    '''
    Returns information about the "node".

    This includes class name, string representation and assumptions.

    Parameters
    ==========

    assumptions : bool, optional
        See the ``assumptions`` keyword in ``tree``
    '''
def tree(node, assumptions: bool = True):
    '''
    Returns a tree representation of "node" as a string.

    It uses print_node() together with pprint_nodes() on node.args recursively.

    Parameters
    ==========

    asssumptions : bool, optional
        The flag to decide whether to print out all the assumption data
        (such as ``is_integer`, ``is_real``) associated with the
        expression or not.

        Enabling the flag makes the result verbose, and the printed
        result may not be determinisitic because of the randomness used
        in backtracing the assumptions.

    See Also
    ========

    print_tree

    '''
def print_tree(node, assumptions: bool = True) -> None:
    '''
    Prints a tree representation of "node".

    Parameters
    ==========

    asssumptions : bool, optional
        The flag to decide whether to print out all the assumption data
        (such as ``is_integer`, ``is_real``) associated with the
        expression or not.

        Enabling the flag makes the result verbose, and the printed
        result may not be determinisitic because of the randomness used
        in backtracing the assumptions.

    Examples
    ========

    >>> from sympy.printing import print_tree
    >>> from sympy import Symbol
    >>> x = Symbol(\'x\', odd=True)
    >>> y = Symbol(\'y\', even=True)

    Printing with full assumptions information:

    >>> print_tree(y**x)
    Pow: y**x
    +-Symbol: y
    | algebraic: True
    | commutative: True
    | complex: True
    | even: True
    | extended_real: True
    | finite: True
    | hermitian: True
    | imaginary: False
    | infinite: False
    | integer: True
    | irrational: False
    | noninteger: False
    | odd: False
    | rational: True
    | real: True
    | transcendental: False
    +-Symbol: x
      algebraic: True
      commutative: True
      complex: True
      even: False
      extended_nonzero: True
      extended_real: True
      finite: True
      hermitian: True
      imaginary: False
      infinite: False
      integer: True
      irrational: False
      noninteger: False
      nonzero: True
      odd: True
      rational: True
      real: True
      transcendental: False
      zero: False

    Hiding the assumptions:

    >>> print_tree(y**x, assumptions=False)
    Pow: y**x
    +-Symbol: y
    +-Symbol: x

    See Also
    ========

    tree

    '''
