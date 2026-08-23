from _typeshed import Incomplete
from collections.abc import Generator
from typing import NamedTuple

__all__ = ['vf2pp_isomorphism', 'vf2pp_is_isomorphic', 'vf2pp_all_isomorphisms']

class _GraphParameters(NamedTuple):
    G1: Incomplete
    G2: Incomplete
    G1_labels: Incomplete
    G2_labels: Incomplete
    nodes_of_G1Labels: Incomplete
    nodes_of_G2Labels: Incomplete
    G2_nodes_of_degree: Incomplete

class _StateParameters(NamedTuple):
    mapping: Incomplete
    reverse_mapping: Incomplete
    T1: Incomplete
    T1_in: Incomplete
    T1_tilde: Incomplete
    T1_tilde_in: Incomplete
    T2: Incomplete
    T2_in: Incomplete
    T2_tilde: Incomplete
    T2_tilde_in: Incomplete

def vf2pp_isomorphism(G1, G2, node_label: Incomplete | None = None, default_label: Incomplete | None = None):
    """Return an isomorphic mapping between `G1` and `G2` if it exists.

    Parameters
    ----------
    G1, G2 : NetworkX Graph or MultiGraph instances.
        The two graphs to check for isomorphism.

    node_label : str, optional
        The name of the node attribute to be used when comparing nodes.
        The default is `None`, meaning node attributes are not considered
        in the comparison. Any node that doesn't have the `node_label`
        attribute uses `default_label` instead.

    default_label : scalar
        Default value to use when a node doesn't have an attribute
        named `node_label`. Default is `None`.

    Returns
    -------
    dict or None
        Node mapping if the two graphs are isomorphic. None otherwise.
    """
def vf2pp_is_isomorphic(G1, G2, node_label: Incomplete | None = None, default_label: Incomplete | None = None):
    """Examines whether G1 and G2 are isomorphic.

    Parameters
    ----------
    G1, G2 : NetworkX Graph or MultiGraph instances.
        The two graphs to check for isomorphism.

    node_label : str, optional
        The name of the node attribute to be used when comparing nodes.
        The default is `None`, meaning node attributes are not considered
        in the comparison. Any node that doesn't have the `node_label`
        attribute uses `default_label` instead.

    default_label : scalar
        Default value to use when a node doesn't have an attribute
        named `node_label`. Default is `None`.

    Returns
    -------
    bool
        True if the two graphs are isomorphic, False otherwise.
    """
def vf2pp_all_isomorphisms(G1, G2, node_label: Incomplete | None = None, default_label: Incomplete | None = None) -> Generator[Incomplete, None, Incomplete]:
    """Yields all the possible mappings between G1 and G2.

    Parameters
    ----------
    G1, G2 : NetworkX Graph or MultiGraph instances.
        The two graphs to check for isomorphism.

    node_label : str, optional
        The name of the node attribute to be used when comparing nodes.
        The default is `None`, meaning node attributes are not considered
        in the comparison. Any node that doesn't have the `node_label`
        attribute uses `default_label` instead.

    default_label : scalar
        Default value to use when a node doesn't have an attribute
        named `node_label`. Default is `None`.

    Yields
    ------
    dict
        Isomorphic mapping between the nodes in `G1` and `G2`.
    """
