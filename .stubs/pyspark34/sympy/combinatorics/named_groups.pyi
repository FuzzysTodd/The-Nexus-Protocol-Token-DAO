from sympy.combinatorics.group_constructs import DirectProduct as DirectProduct
from sympy.combinatorics.perm_groups import PermutationGroup as PermutationGroup
from sympy.combinatorics.permutations import Permutation as Permutation

def AbelianGroup(*cyclic_orders):
    """
    Returns the direct product of cyclic groups with the given orders.

    Explanation
    ===========

    According to the structure theorem for finite abelian groups ([1]),
    every finite abelian group can be written as the direct product of
    finitely many cyclic groups.

    Examples
    ========

    >>> from sympy.combinatorics.named_groups import AbelianGroup
    >>> AbelianGroup(3, 4)
    PermutationGroup([
            (6)(0 1 2),
            (3 4 5 6)])
    >>> _.is_group
    True

    See Also
    ========

    DirectProduct

    References
    ==========

    .. [1] https://groupprops.subwiki.org/wiki/Structure_theorem_for_finitely_generated_abelian_groups

    """
def AlternatingGroup(n):
    '''
    Generates the alternating group on ``n`` elements as a permutation group.

    Explanation
    ===========

    For ``n > 2``, the generators taken are ``(0 1 2), (0 1 2 ... n-1)`` for
    ``n`` odd
    and ``(0 1 2), (1 2 ... n-1)`` for ``n`` even (See [1], p.31, ex.6.9.).
    After the group is generated, some of its basic properties are set.
    The cases ``n = 1, 2`` are handled separately.

    Examples
    ========

    >>> from sympy.combinatorics.named_groups import AlternatingGroup
    >>> G = AlternatingGroup(4)
    >>> G.is_group
    True
    >>> a = list(G.generate_dimino())
    >>> len(a)
    12
    >>> all(perm.is_even for perm in a)
    True

    See Also
    ========

    SymmetricGroup, CyclicGroup, DihedralGroup

    References
    ==========

    .. [1] Armstrong, M. "Groups and Symmetry"

    '''
def set_alternating_group_properties(G, n, degree) -> None:
    """Set known properties of an alternating group. """
def CyclicGroup(n):
    """
    Generates the cyclic group of order ``n`` as a permutation group.

    Explanation
    ===========

    The generator taken is the ``n``-cycle ``(0 1 2 ... n-1)``
    (in cycle notation). After the group is generated, some of its basic
    properties are set.

    Examples
    ========

    >>> from sympy.combinatorics.named_groups import CyclicGroup
    >>> G = CyclicGroup(6)
    >>> G.is_group
    True
    >>> G.order()
    6
    >>> list(G.generate_schreier_sims(af=True))
    [[0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 0], [2, 3, 4, 5, 0, 1],
    [3, 4, 5, 0, 1, 2], [4, 5, 0, 1, 2, 3], [5, 0, 1, 2, 3, 4]]

    See Also
    ========

    SymmetricGroup, DihedralGroup, AlternatingGroup

    """
def DihedralGroup(n):
    """
    Generates the dihedral group `D_n` as a permutation group.

    Explanation
    ===========

    The dihedral group `D_n` is the group of symmetries of the regular
    ``n``-gon. The generators taken are the ``n``-cycle ``a = (0 1 2 ... n-1)``
    (a rotation of the ``n``-gon) and ``b = (0 n-1)(1 n-2)...``
    (a reflection of the ``n``-gon) in cycle rotation. It is easy to see that
    these satisfy ``a**n = b**2 = 1`` and ``bab = ~a`` so they indeed generate
    `D_n` (See [1]). After the group is generated, some of its basic properties
    are set.

    Examples
    ========

    >>> from sympy.combinatorics.named_groups import DihedralGroup
    >>> G = DihedralGroup(5)
    >>> G.is_group
    True
    >>> a = list(G.generate_dimino())
    >>> [perm.cyclic_form for perm in a]
    [[], [[0, 1, 2, 3, 4]], [[0, 2, 4, 1, 3]],
    [[0, 3, 1, 4, 2]], [[0, 4, 3, 2, 1]], [[0, 4], [1, 3]],
    [[1, 4], [2, 3]], [[0, 1], [2, 4]], [[0, 2], [3, 4]],
    [[0, 3], [1, 2]]]

    See Also
    ========

    SymmetricGroup, CyclicGroup, AlternatingGroup

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Dihedral_group

    """
def SymmetricGroup(n):
    """
    Generates the symmetric group on ``n`` elements as a permutation group.

    Explanation
    ===========

    The generators taken are the ``n``-cycle
    ``(0 1 2 ... n-1)`` and the transposition ``(0 1)`` (in cycle notation).
    (See [1]). After the group is generated, some of its basic properties
    are set.

    Examples
    ========

    >>> from sympy.combinatorics.named_groups import SymmetricGroup
    >>> G = SymmetricGroup(4)
    >>> G.is_group
    True
    >>> G.order()
    24
    >>> list(G.generate_schreier_sims(af=True))
    [[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1], [3, 1, 2, 0], [0, 2, 3, 1],
    [1, 3, 0, 2], [2, 0, 1, 3], [3, 2, 0, 1], [0, 3, 1, 2], [1, 0, 2, 3],
    [2, 1, 3, 0], [3, 0, 1, 2], [0, 1, 3, 2], [1, 2, 0, 3], [2, 3, 1, 0],
    [3, 1, 0, 2], [0, 2, 1, 3], [1, 3, 2, 0], [2, 0, 3, 1], [3, 2, 1, 0],
    [0, 3, 2, 1], [1, 0, 3, 2], [2, 1, 0, 3], [3, 0, 2, 1]]

    See Also
    ========

    CyclicGroup, DihedralGroup, AlternatingGroup

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Symmetric_group#Generators_and_relations

    """
def set_symmetric_group_properties(G, n, degree) -> None:
    """Set known properties of a symmetric group. """
def RubikGroup(n):
    """Return a group of Rubik's cube generators

    >>> from sympy.combinatorics.named_groups import RubikGroup
    >>> RubikGroup(2).is_group
    True
    """
