from _typeshed import Incomplete

__all__ = ['dotprint']

def dotprint(expr, styles=..., atom=..., maxdepth: Incomplete | None = None, repeat: bool = True, labelfunc=..., **kwargs):
    '''DOT description of a SymPy expression tree

    Parameters
    ==========

    styles : list of lists composed of (Class, mapping), optional
        Styles for different classes.

        The default is

        .. code-block:: python

            (
                (Basic, {\'color\': \'blue\', \'shape\': \'ellipse\'}),
                (Expr,  {\'color\': \'black\'})
            )

    atom : function, optional
        Function used to determine if an arg is an atom.

        A good choice is ``lambda x: not x.args``.

        The default is ``lambda x: not isinstance(x, Basic)``.

    maxdepth : integer, optional
        The maximum depth.

        The default is ``None``, meaning no limit.

    repeat : boolean, optional
        Whether to use different nodes for common subexpressions.

        The default is ``True``.

        For example, for ``x + x*y`` with ``repeat=True``, it will have
        two nodes for ``x``; with ``repeat=False``, it will have one
        node.

        .. warning::
            Even if a node appears twice in the same object like ``x`` in
            ``Pow(x, x)``, it will still only appear once.
            Hence, with ``repeat=False``, the number of arrows out of an
            object might not equal the number of args it has.

    labelfunc : function, optional
        A function to create a label for a given leaf node.

        The default is ``str``.

        Another good option is ``srepr``.

        For example with ``str``, the leaf nodes of ``x + 1`` are labeled,
        ``x`` and ``1``.  With ``srepr``, they are labeled ``Symbol(\'x\')``
        and ``Integer(1)``.

    **kwargs : optional
        Additional keyword arguments are included as styles for the graph.

    Examples
    ========

    >>> from sympy import dotprint
    >>> from sympy.abc import x
    >>> print(dotprint(x+2)) # doctest: +NORMALIZE_WHITESPACE
    digraph{
    <BLANKLINE>
    # Graph style
    "ordering"="out"
    "rankdir"="TD"
    <BLANKLINE>
    #########
    # Nodes #
    #########
    <BLANKLINE>
    "Add(Integer(2), Symbol(\'x\'))_()" ["color"="black", "label"="Add", "shape"="ellipse"];
    "Integer(2)_(0,)" ["color"="black", "label"="2", "shape"="ellipse"];
    "Symbol(\'x\')_(1,)" ["color"="black", "label"="x", "shape"="ellipse"];
    <BLANKLINE>
    #########
    # Edges #
    #########
    <BLANKLINE>
    "Add(Integer(2), Symbol(\'x\'))_()" -> "Integer(2)_(0,)";
    "Add(Integer(2), Symbol(\'x\'))_()" -> "Symbol(\'x\')_(1,)";
    }

    '''
