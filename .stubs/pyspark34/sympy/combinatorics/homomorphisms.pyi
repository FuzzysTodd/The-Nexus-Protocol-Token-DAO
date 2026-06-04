from _typeshed import Incomplete
from sympy.combinatorics.fp_groups import FpGroup as FpGroup, FpSubgroup as FpSubgroup, simplify_presentation as simplify_presentation
from sympy.combinatorics.free_groups import FreeGroup as FreeGroup
from sympy.combinatorics.perm_groups import PermutationGroup as PermutationGroup
from sympy.core.numbers import igcd as igcd
from sympy.core.singleton import S as S
from sympy.ntheory.factor_ import totient as totient

class GroupHomomorphism:
    """
    A class representing group homomorphisms. Instantiate using `homomorphism()`.

    References
    ==========

    .. [1] Holt, D., Eick, B. and O'Brien, E. (2005). Handbook of computational group theory.

    """
    domain: Incomplete
    codomain: Incomplete
    images: Incomplete
    def __init__(self, domain, codomain, images) -> None: ...
    def invert(self, g):
        """
        Return an element of the preimage of ``g`` or of each element
        of ``g`` if ``g`` is a list.

        Explanation
        ===========

        If the codomain is an FpGroup, the inverse for equal
        elements might not always be the same unless the FpGroup's
        rewriting system is confluent. However, making a system
        confluent can be time-consuming. If it's important, try
        `self.codomain.make_confluent()` first.

        """
    def kernel(self):
        """
        Compute the kernel of `self`.

        """
    def image(self):
        """
        Compute the image of `self`.

        """
    def __call__(self, elem): ...
    def is_injective(self):
        """
        Check if the homomorphism is injective

        """
    def is_surjective(self):
        """
        Check if the homomorphism is surjective

        """
    def is_isomorphism(self):
        """
        Check if `self` is an isomorphism.

        """
    def is_trivial(self):
        """
        Check is `self` is a trivial homomorphism, i.e. all elements
        are mapped to the identity.

        """
    def compose(self, other):
        """
        Return the composition of `self` and `other`, i.e.
        the homomorphism phi such that for all g in the domain
        of `other`, phi(g) = self(other(g))

        """
    def restrict_to(self, H):
        """
        Return the restriction of the homomorphism to the subgroup `H`
        of the domain.

        """
    def invert_subgroup(self, H):
        """
        Return the subgroup of the domain that is the inverse image
        of the subgroup ``H`` of the homomorphism image

        """

def homomorphism(domain, codomain, gens, images=(), check: bool = True):
    """
    Create (if possible) a group homomorphism from the group ``domain``
    to the group ``codomain`` defined by the images of the domain's
    generators ``gens``. ``gens`` and ``images`` can be either lists or tuples
    of equal sizes. If ``gens`` is a proper subset of the group's generators,
    the unspecified generators will be mapped to the identity. If the
    images are not specified, a trivial homomorphism will be created.

    If the given images of the generators do not define a homomorphism,
    an exception is raised.

    If ``check`` is ``False``, do not check whether the given images actually
    define a homomorphism.

    """
def orbit_homomorphism(group, omega):
    """
    Return the homomorphism induced by the action of the permutation
    group ``group`` on the set ``omega`` that is closed under the action.

    """
def block_homomorphism(group, blocks):
    """
    Return the homomorphism induced by the action of the permutation
    group ``group`` on the block system ``blocks``. The latter should be
    of the same form as returned by the ``minimal_block`` method for
    permutation groups, namely a list of length ``group.degree`` where
    the i-th entry is a representative of the block i belongs to.

    """
def group_isomorphism(G, H, isomorphism: bool = True):
    '''
    Compute an isomorphism between 2 given groups.

    Parameters
    ==========

    G : A finite ``FpGroup`` or a ``PermutationGroup``.
        First group.

    H : A finite ``FpGroup`` or a ``PermutationGroup``
        Second group.

    isomorphism : bool
        This is used to avoid the computation of homomorphism
        when the user only wants to check if there exists
        an isomorphism between the groups.

    Returns
    =======

    If isomorphism = False -- Returns a boolean.
    If isomorphism = True  -- Returns a boolean and an isomorphism between `G` and `H`.

    Examples
    ========

    >>> from sympy.combinatorics import free_group, Permutation
    >>> from sympy.combinatorics.perm_groups import PermutationGroup
    >>> from sympy.combinatorics.fp_groups import FpGroup
    >>> from sympy.combinatorics.homomorphisms import group_isomorphism
    >>> from sympy.combinatorics.named_groups import DihedralGroup, AlternatingGroup

    >>> D = DihedralGroup(8)
    >>> p = Permutation(0, 1, 2, 3, 4, 5, 6, 7)
    >>> P = PermutationGroup(p)
    >>> group_isomorphism(D, P)
    (False, None)

    >>> F, a, b = free_group("a, b")
    >>> G = FpGroup(F, [a**3, b**3, (a*b)**2])
    >>> H = AlternatingGroup(4)
    >>> (check, T) = group_isomorphism(G, H)
    >>> check
    True
    >>> T(b*a*b**-1*a**-1*b**-1)
    (0 2 3)

    Notes
    =====

    Uses the approach suggested by Robert Tarjan to compute the isomorphism between two groups.
    First, the generators of ``G`` are mapped to the elements of ``H`` and
    we check if the mapping induces an isomorphism.

    '''
def is_isomorphic(G, H):
    """
    Check if the groups are isomorphic to each other

    Parameters
    ==========

    G : A finite ``FpGroup`` or a ``PermutationGroup``
        First group.

    H : A finite ``FpGroup`` or a ``PermutationGroup``
        Second group.

    Returns
    =======

    boolean
    """
