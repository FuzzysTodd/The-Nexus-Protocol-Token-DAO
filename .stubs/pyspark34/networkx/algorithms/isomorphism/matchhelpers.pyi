from _typeshed import Incomplete

__all__ = ['categorical_node_match', 'categorical_edge_match', 'categorical_multiedge_match', 'numerical_node_match', 'numerical_edge_match', 'numerical_multiedge_match', 'generic_node_match', 'generic_edge_match', 'generic_multiedge_match']

def categorical_node_match(attr, default): ...

categorical_edge_match: Incomplete

def categorical_multiedge_match(attr, default): ...
def numerical_node_match(attr, default, rtol: float = 1e-05, atol: float = 1e-08): ...

numerical_edge_match: Incomplete

def numerical_multiedge_match(attr, default, rtol: float = 1e-05, atol: float = 1e-08): ...
def generic_node_match(attr, default, op): ...

generic_edge_match: Incomplete

def generic_multiedge_match(attr, default, op):
    '''Returns a comparison function for a generic attribute.

    The value(s) of the attr(s) are compared using the specified
    operators. If all the attributes are equal, then the constructed
    function returns True. Potentially, the constructed edge_match
    function can be slow since it must verify that no isomorphism
    exists between the multiedges before it returns False.

    Parameters
    ----------
    attr : string | list
        The edge attribute to compare, or a list of node attributes
        to compare.
    default : value | list
        The default value for the edge attribute, or a list of
        default values for the edgeattributes.
    op : callable | list
        The operator to use when comparing attribute values, or a list
        of operators to use when comparing values for each attribute.

    Returns
    -------
    match : function
        The customized, generic `edge_match` function.

    Examples
    --------
    >>> from operator import eq
    >>> from math import isclose
    >>> from networkx.algorithms.isomorphism import generic_node_match
    >>> nm = generic_node_match("weight", 1.0, isclose)
    >>> nm = generic_node_match("color", "red", eq)
    >>> nm = generic_node_match(["weight", "color"], [1.0, "red"], [isclose, eq])
    ...

    '''
