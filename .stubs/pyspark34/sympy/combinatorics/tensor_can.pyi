from _typeshed import Incomplete
from sympy.combinatorics.perm_groups import PermutationGroup as PermutationGroup
from sympy.combinatorics.permutations import Permutation as Permutation

def dummy_sgs(dummies, sym, n):
    """
    Return the strong generators for dummy indices.

    Parameters
    ==========

    dummies : List of dummy indices.
        `dummies[2k], dummies[2k+1]` are paired indices.
        In base form, the dummy indices are always in
        consecutive positions.
    sym : symmetry under interchange of contracted dummies::
        * None  no symmetry
        * 0     commuting
        * 1     anticommuting

    n : number of indices

    Examples
    ========

    >>> from sympy.combinatorics.tensor_can import dummy_sgs
    >>> dummy_sgs(list(range(2, 8)), 0, 8)
    [[0, 1, 3, 2, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 5, 4, 6, 7, 8, 9],
     [0, 1, 2, 3, 4, 5, 7, 6, 8, 9], [0, 1, 4, 5, 2, 3, 6, 7, 8, 9],
     [0, 1, 2, 3, 6, 7, 4, 5, 8, 9]]
    """
def transversal2coset(size, base, transversal): ...
def double_coset_can_rep(dummies, sym, b_S, sgens, S_transversals, g):
    """
    Butler-Portugal algorithm for tensor canonicalization with dummy indices.

    Parameters
    ==========

      dummies
        list of lists of dummy indices,
        one list for each type of index;
        the dummy indices are put in order contravariant, covariant
        [d0, -d0, d1, -d1, ...].

      sym
        list of the symmetries of the index metric for each type.

      possible symmetries of the metrics
              * 0     symmetric
              * 1     antisymmetric
              * None  no symmetry

      b_S
        base of a minimal slot symmetry BSGS.

      sgens
        generators of the slot symmetry BSGS.

      S_transversals
        transversals for the slot BSGS.

      g
        permutation representing the tensor.

    Returns
    =======

    Return 0 if the tensor is zero, else return the array form of
    the permutation representing the canonical form of the tensor.

    Notes
    =====

    A tensor with dummy indices can be represented in a number
    of equivalent ways which typically grows exponentially with
    the number of indices. To be able to establish if two tensors
    with many indices are equal becomes computationally very slow
    in absence of an efficient algorithm.

    The Butler-Portugal algorithm [3] is an efficient algorithm to
    put tensors in canonical form, solving the above problem.

    Portugal observed that a tensor can be represented by a permutation,
    and that the class of tensors equivalent to it under slot and dummy
    symmetries is equivalent to the double coset `D*g*S`
    (Note: in this documentation we use the conventions for multiplication
    of permutations p, q with (p*q)(i) = p[q[i]] which is opposite
    to the one used in the Permutation class)

    Using the algorithm by Butler to find a representative of the
    double coset one can find a canonical form for the tensor.

    To see this correspondence,
    let `g` be a permutation in array form; a tensor with indices `ind`
    (the indices including both the contravariant and the covariant ones)
    can be written as

    `t = T(ind[g[0]], \\dots, ind[g[n-1]])`,

    where `n = len(ind)`;
    `g` has size `n + 2`, the last two indices for the sign of the tensor
    (trick introduced in [4]).

    A slot symmetry transformation `s` is a permutation acting on the slots
    `t \\rightarrow T(ind[(g*s)[0]], \\dots, ind[(g*s)[n-1]])`

    A dummy symmetry transformation acts on `ind`
    `t \\rightarrow T(ind[(d*g)[0]], \\dots, ind[(d*g)[n-1]])`

    Being interested only in the transformations of the tensor under
    these symmetries, one can represent the tensor by `g`, which transforms
    as

    `g -> d*g*s`, so it belongs to the coset `D*g*S`, or in other words
    to the set of all permutations allowed by the slot and dummy symmetries.

    Let us explain the conventions by an example.

    Given a tensor `T^{d3 d2 d1}{}_{d1 d2 d3}` with the slot symmetries
          `T^{a0 a1 a2 a3 a4 a5} = -T^{a2 a1 a0 a3 a4 a5}`

          `T^{a0 a1 a2 a3 a4 a5} = -T^{a4 a1 a2 a3 a0 a5}`

    and symmetric metric, find the tensor equivalent to it which
    is the lowest under the ordering of indices:
    lexicographic ordering `d1, d2, d3` and then contravariant
    before covariant index; that is the canonical form of the tensor.

    The canonical form is `-T^{d1 d2 d3}{}_{d1 d2 d3}`
    obtained using `T^{a0 a1 a2 a3 a4 a5} = -T^{a2 a1 a0 a3 a4 a5}`.

    To convert this problem in the input for this function,
    use the following ordering of the index names
    (- for covariant for short) `d1, -d1, d2, -d2, d3, -d3`

    `T^{d3 d2 d1}{}_{d1 d2 d3}` corresponds to `g = [4, 2, 0, 1, 3, 5, 6, 7]`
    where the last two indices are for the sign

    `sgens = [Permutation(0, 2)(6, 7), Permutation(0, 4)(6, 7)]`

    sgens[0] is the slot symmetry `-(0, 2)`
    `T^{a0 a1 a2 a3 a4 a5} = -T^{a2 a1 a0 a3 a4 a5}`

    sgens[1] is the slot symmetry `-(0, 4)`
    `T^{a0 a1 a2 a3 a4 a5} = -T^{a4 a1 a2 a3 a0 a5}`

    The dummy symmetry group D is generated by the strong base generators
    `[(0, 1), (2, 3), (4, 5), (0, 2)(1, 3), (0, 4)(1, 5)]`
    where the first three interchange covariant and contravariant
    positions of the same index (d1 <-> -d1) and the last two interchange
    the dummy indices themselves (d1 <-> d2).

    The dummy symmetry acts from the left
    `d = [1, 0, 2, 3, 4, 5, 6, 7]`  exchange `d1 \\leftrightarrow -d1`
    `T^{d3 d2 d1}{}_{d1 d2 d3} == T^{d3 d2}{}_{d1}{}^{d1}{}_{d2 d3}`

    `g=[4, 2, 0, 1, 3, 5, 6, 7]  -> [4, 2, 1, 0, 3, 5, 6, 7] = _af_rmul(d, g)`
    which differs from `_af_rmul(g, d)`.

    The slot symmetry acts from the right
    `s = [2, 1, 0, 3, 4, 5, 7, 6]`  exchanges slots 0 and 2 and changes sign
    `T^{d3 d2 d1}{}_{d1 d2 d3} == -T^{d1 d2 d3}{}_{d1 d2 d3}`

    `g=[4,2,0,1,3,5,6,7]  -> [0, 2, 4, 1, 3, 5, 7, 6] = _af_rmul(g, s)`

    Example in which the tensor is zero, same slot symmetries as above:
    `T^{d2}{}_{d1 d3}{}^{d1 d3}{}_{d2}`

    `= -T^{d3}{}_{d1 d3}{}^{d1 d2}{}_{d2}`   under slot symmetry `-(0,4)`;

    `= T_{d3 d1}{}^{d3}{}^{d1 d2}{}_{d2}`    under slot symmetry `-(0,2)`;

    `= T^{d3}{}_{d1 d3}{}^{d1 d2}{}_{d2}`    symmetric metric;

    `= 0`  since two of these lines have tensors differ only for the sign.

    The double coset D*g*S consists of permutations `h = d*g*s` corresponding
    to equivalent tensors; if there are two `h` which are the same apart
    from the sign, return zero; otherwise
    choose as representative the tensor with indices
    ordered lexicographically according to `[d1, -d1, d2, -d2, d3, -d3]`
    that is ``rep = min(D*g*S) = min([d*g*s for d in D for s in S])``

    The indices are fixed one by one; first choose the lowest index
    for slot 0, then the lowest remaining index for slot 1, etc.
    Doing this one obtains a chain of stabilizers

    `S \\rightarrow S_{b0} \\rightarrow S_{b0,b1} \\rightarrow \\dots` and
    `D \\rightarrow D_{p0} \\rightarrow D_{p0,p1} \\rightarrow \\dots`

    where ``[b0, b1, ...] = range(b)`` is a base of the symmetric group;
    the strong base `b_S` of S is an ordered sublist of it;
    therefore it is sufficient to compute once the
    strong base generators of S using the Schreier-Sims algorithm;
    the stabilizers of the strong base generators are the
    strong base generators of the stabilizer subgroup.

    ``dbase = [p0, p1, ...]`` is not in general in lexicographic order,
    so that one must recompute the strong base generators each time;
    however this is trivial, there is no need to use the Schreier-Sims
    algorithm for D.

    The algorithm keeps a TAB of elements `(s_i, d_i, h_i)`
    where `h_i = d_i \\times g \\times s_i` satisfying `h_i[j] = p_j` for `0 \\le j < i`
    starting from `s_0 = id, d_0 = id, h_0 = g`.

    The equations `h_0[0] = p_0, h_1[1] = p_1, \\dots` are solved in this order,
    choosing each time the lowest possible value of p_i

    For `j < i`
    `d_i*g*s_i*S_{b_0, \\dots, b_{i-1}}*b_j = D_{p_0, \\dots, p_{i-1}}*p_j`
    so that for dx in `D_{p_0,\\dots,p_{i-1}}` and sx in
    `S_{base[0], \\dots, base[i-1]}` one has `dx*d_i*g*s_i*sx*b_j = p_j`

    Search for dx, sx such that this equation holds for `j = i`;
    it can be written as `s_i*sx*b_j = J, dx*d_i*g*J = p_j`
    `sx*b_j = s_i**-1*J; sx = trace(s_i**-1, S_{b_0,...,b_{i-1}})`
    `dx**-1*p_j = d_i*g*J; dx = trace(d_i*g*J, D_{p_0,...,p_{i-1}})`

    `s_{i+1} = s_i*trace(s_i**-1*J, S_{b_0,...,b_{i-1}})`
    `d_{i+1} = trace(d_i*g*J, D_{p_0,...,p_{i-1}})**-1*d_i`
    `h_{i+1}*b_i = d_{i+1}*g*s_{i+1}*b_i = p_i`

    `h_n*b_j = p_j` for all j, so that `h_n` is the solution.

    Add the found `(s, d, h)` to TAB1.

    At the end of the iteration sort TAB1 with respect to the `h`;
    if there are two consecutive `h` in TAB1 which differ only for the
    sign, the tensor is zero, so return 0;
    if there are two consecutive `h` which are equal, keep only one.

    Then stabilize the slot generators under `i` and the dummy generators
    under `p_i`.

    Assign `TAB = TAB1` at the end of the iteration step.

    At the end `TAB` contains a unique `(s, d, h)`, since all the slots
    of the tensor `h` have been fixed to have the minimum value according
    to the symmetries. The algorithm returns `h`.

    It is important that the slot BSGS has lexicographic minimal base,
    otherwise there is an `i` which does not belong to the slot base
    for which `p_i` is fixed by the dummy symmetry only, while `i`
    is not invariant from the slot stabilizer, so `p_i` is not in
    general the minimal value.

    This algorithm differs slightly from the original algorithm [3]:
      the canonical form is minimal lexicographically, and
      the BSGS has minimal base under lexicographic order.
      Equal tensors `h` are eliminated from TAB.


    Examples
    ========

    >>> from sympy.combinatorics.permutations import Permutation
    >>> from sympy.combinatorics.tensor_can import double_coset_can_rep, get_transversals
    >>> gens = [Permutation(x) for x in [[2, 1, 0, 3, 4, 5, 7, 6], [4, 1, 2, 3, 0, 5, 7, 6]]]
    >>> base = [0, 2]
    >>> g = Permutation([4, 2, 0, 1, 3, 5, 6, 7])
    >>> transversals = get_transversals(base, gens)
    >>> double_coset_can_rep([list(range(6))], [0], base, gens, transversals, g)
    [0, 1, 2, 3, 4, 5, 7, 6]

    >>> g = Permutation([4, 1, 3, 0, 5, 2, 6, 7])
    >>> double_coset_can_rep([list(range(6))], [0], base, gens, transversals, g)
    0
    """
def canonical_free(base, gens, g, num_free):
    """
    Canonicalization of a tensor with respect to free indices
    choosing the minimum with respect to lexicographical ordering
    in the free indices.

    Explanation
    ===========

    ``base``, ``gens``  BSGS for slot permutation group
    ``g``               permutation representing the tensor
    ``num_free``        number of free indices
    The indices must be ordered with first the free indices

    See explanation in double_coset_can_rep
    The algorithm is a variation of the one given in [2].

    Examples
    ========

    >>> from sympy.combinatorics import Permutation
    >>> from sympy.combinatorics.tensor_can import canonical_free
    >>> gens = [[1, 0, 2, 3, 5, 4], [2, 3, 0, 1, 4, 5],[0, 1, 3, 2, 5, 4]]
    >>> gens = [Permutation(h) for h in gens]
    >>> base = [0, 2]
    >>> g = Permutation([2, 1, 0, 3, 4, 5])
    >>> canonical_free(base, gens, g, 4)
    [0, 3, 1, 2, 5, 4]

    Consider the product of Riemann tensors
    ``T = R^{a}_{d0}^{d1,d2}*R_{d2,d1}^{d0,b}``
    The order of the indices is ``[a, b, d0, -d0, d1, -d1, d2, -d2]``
    The permutation corresponding to the tensor is
    ``g = [0, 3, 4, 6, 7, 5, 2, 1, 8, 9]``

    In particular ``a`` is position ``0``, ``b`` is in position ``9``.
    Use the slot symmetries to get `T` is a form which is the minimal
    in lexicographic order in the free indices ``a`` and ``b``, e.g.
    ``-R^{a}_{d0}^{d1,d2}*R^{b,d0}_{d2,d1}`` corresponding to
    ``[0, 3, 4, 6, 1, 2, 7, 5, 9, 8]``

    >>> from sympy.combinatorics.tensor_can import riemann_bsgs, tensor_gens
    >>> base, gens = riemann_bsgs
    >>> size, sbase, sgens = tensor_gens(base, gens, [[], []], 0)
    >>> g = Permutation([0, 3, 4, 6, 7, 5, 2, 1, 8, 9])
    >>> canonical_free(sbase, [Permutation(h) for h in sgens], g, 2)
    [0, 3, 4, 6, 1, 2, 7, 5, 9, 8]
    """
def canonicalize(g, dummies, msym, *v):
    """
    canonicalize tensor formed by tensors

    Parameters
    ==========

    g : permutation representing the tensor

    dummies : list representing the dummy indices
      it can be a list of dummy indices of the same type
      or a list of lists of dummy indices, one list for each
      type of index;
      the dummy indices must come after the free indices,
      and put in order contravariant, covariant
      [d0, -d0, d1,-d1,...]

    msym :  symmetry of the metric(s)
        it can be an integer or a list;
        in the first case it is the symmetry of the dummy index metric;
        in the second case it is the list of the symmetries of the
        index metric for each type

    v : list, (base_i, gens_i, n_i, sym_i) for tensors of type `i`

    base_i, gens_i : BSGS for tensors of this type.
        The BSGS should have minimal base under lexicographic ordering;
        if not, an attempt is made do get the minimal BSGS;
        in case of failure,
        canonicalize_naive is used, which is much slower.

    n_i :    number of tensors of type `i`.

    sym_i :  symmetry under exchange of component tensors of type `i`.

        Both for msym and sym_i the cases are
            * None  no symmetry
            * 0     commuting
            * 1     anticommuting

    Returns
    =======

    0 if the tensor is zero, else return the array form of
    the permutation representing the canonical form of the tensor.

    Algorithm
    =========

    First one uses canonical_free to get the minimum tensor under
    lexicographic order, using only the slot symmetries.
    If the component tensors have not minimal BSGS, it is attempted
    to find it; if the attempt fails canonicalize_naive
    is used instead.

    Compute the residual slot symmetry keeping fixed the free indices
    using tensor_gens(base, gens, list_free_indices, sym).

    Reduce the problem eliminating the free indices.

    Then use double_coset_can_rep and lift back the result reintroducing
    the free indices.

    Examples
    ========

    one type of index with commuting metric;

    `A_{a b}` and `B_{a b}` antisymmetric and commuting

    `T = A_{d0 d1} * B^{d0}{}_{d2} * B^{d2 d1}`

    `ord = [d0,-d0,d1,-d1,d2,-d2]` order of the indices

    g = [1, 3, 0, 5, 4, 2, 6, 7]

    `T_c = 0`

    >>> from sympy.combinatorics.tensor_can import get_symmetric_group_sgs, canonicalize, bsgs_direct_product
    >>> from sympy.combinatorics import Permutation
    >>> base2a, gens2a = get_symmetric_group_sgs(2, 1)
    >>> t0 = (base2a, gens2a, 1, 0)
    >>> t1 = (base2a, gens2a, 2, 0)
    >>> g = Permutation([1, 3, 0, 5, 4, 2, 6, 7])
    >>> canonicalize(g, range(6), 0, t0, t1)
    0

    same as above, but with `B_{a b}` anticommuting

    `T_c = -A^{d0 d1} * B_{d0}{}^{d2} * B_{d1 d2}`

    can = [0,2,1,4,3,5,7,6]

    >>> t1 = (base2a, gens2a, 2, 1)
    >>> canonicalize(g, range(6), 0, t0, t1)
    [0, 2, 1, 4, 3, 5, 7, 6]

    two types of indices `[a,b,c,d,e,f]` and `[m,n]`, in this order,
    both with commuting metric

    `f^{a b c}` antisymmetric, commuting

    `A_{m a}` no symmetry, commuting

    `T = f^c{}_{d a} * f^f{}_{e b} * A_m{}^d * A^{m b} * A_n{}^a * A^{n e}`

    ord = [c,f,a,-a,b,-b,d,-d,e,-e,m,-m,n,-n]

    g = [0,7,3, 1,9,5, 11,6, 10,4, 13,2, 12,8, 14,15]

    The canonical tensor is
    `T_c = -f^{c a b} * f^{f d e} * A^m{}_a * A_{m d} * A^n{}_b * A_{n e}`

    can = [0,2,4, 1,6,8, 10,3, 11,7, 12,5, 13,9, 15,14]

    >>> base_f, gens_f = get_symmetric_group_sgs(3, 1)
    >>> base1, gens1 = get_symmetric_group_sgs(1)
    >>> base_A, gens_A = bsgs_direct_product(base1, gens1, base1, gens1)
    >>> t0 = (base_f, gens_f, 2, 0)
    >>> t1 = (base_A, gens_A, 4, 0)
    >>> dummies = [range(2, 10), range(10, 14)]
    >>> g = Permutation([0, 7, 3, 1, 9, 5, 11, 6, 10, 4, 13, 2, 12, 8, 14, 15])
    >>> canonicalize(g, dummies, [0, 0], t0, t1)
    [0, 2, 4, 1, 6, 8, 10, 3, 11, 7, 12, 5, 13, 9, 15, 14]
    """
def perm_af_direct_product(gens1, gens2, signed: bool = True):
    """
    Direct products of the generators gens1 and gens2.

    Examples
    ========

    >>> from sympy.combinatorics.tensor_can import perm_af_direct_product
    >>> gens1 = [[1, 0, 2, 3], [0, 1, 3, 2]]
    >>> gens2 = [[1, 0]]
    >>> perm_af_direct_product(gens1, gens2, False)
    [[1, 0, 2, 3, 4, 5], [0, 1, 3, 2, 4, 5], [0, 1, 2, 3, 5, 4]]
    >>> gens1 = [[1, 0, 2, 3, 5, 4], [0, 1, 3, 2, 4, 5]]
    >>> gens2 = [[1, 0, 2, 3]]
    >>> perm_af_direct_product(gens1, gens2, True)
    [[1, 0, 2, 3, 4, 5, 7, 6], [0, 1, 3, 2, 4, 5, 6, 7], [0, 1, 2, 3, 5, 4, 6, 7]]
    """
def bsgs_direct_product(base1, gens1, base2, gens2, signed: bool = True):
    """
    Direct product of two BSGS.

    Parameters
    ==========

    base1 : base of the first BSGS.

    gens1 : strong generating sequence of the first BSGS.

    base2, gens2 : similarly for the second BSGS.

    signed : flag for signed permutations.

    Examples
    ========

    >>> from sympy.combinatorics.tensor_can import (get_symmetric_group_sgs, bsgs_direct_product)
    >>> base1, gens1 = get_symmetric_group_sgs(1)
    >>> base2, gens2 = get_symmetric_group_sgs(2)
    >>> bsgs_direct_product(base1, gens1, base2, gens2)
    ([1], [(4)(1 2)])
    """
def get_symmetric_group_sgs(n, antisym: bool = False):
    """
    Return base, gens of the minimal BSGS for (anti)symmetric tensor

    Parameters
    ==========

    n : rank of the tensor
    antisym : bool
        ``antisym = False`` symmetric tensor
        ``antisym = True``  antisymmetric tensor

    Examples
    ========

    >>> from sympy.combinatorics.tensor_can import get_symmetric_group_sgs
    >>> get_symmetric_group_sgs(3)
    ([0, 1], [(4)(0 1), (4)(1 2)])
    """

riemann_bsgs: Incomplete

def get_transversals(base, gens):
    """
    Return transversals for the group with BSGS base, gens
    """
def get_minimal_bsgs(base, gens):
    """
    Compute a minimal GSGS

    base, gens BSGS

    If base, gens is a minimal BSGS return it; else return a minimal BSGS
    if it fails in finding one, it returns None

    TODO: use baseswap in the case in which if it fails in finding a
    minimal BSGS

    Examples
    ========

    >>> from sympy.combinatorics import Permutation
    >>> from sympy.combinatorics.tensor_can import get_minimal_bsgs
    >>> riemann_bsgs1 = ([2, 0], ([Permutation(5)(0, 1)(4, 5), Permutation(5)(0, 2)(1, 3)]))
    >>> get_minimal_bsgs(*riemann_bsgs1)
    ([0, 2], [(0 1)(4 5), (5)(0 2)(1 3), (2 3)(4 5)])
    """
def tensor_gens(base, gens, list_free_indices, sym: int = 0):
    """
    Returns size, res_base, res_gens BSGS for n tensors of the
    same type.

    Explanation
    ===========

    base, gens BSGS for tensors of this type
    list_free_indices  list of the slots occupied by fixed indices
                       for each of the tensors

    sym symmetry under commutation of two tensors
    sym   None  no symmetry
    sym   0     commuting
    sym   1     anticommuting

    Examples
    ========

    >>> from sympy.combinatorics.tensor_can import tensor_gens, get_symmetric_group_sgs

    two symmetric tensors with 3 indices without free indices

    >>> base, gens = get_symmetric_group_sgs(3)
    >>> tensor_gens(base, gens, [[], []])
    (8, [0, 1, 3, 4], [(7)(0 1), (7)(1 2), (7)(3 4), (7)(4 5), (7)(0 3)(1 4)(2 5)])

    two symmetric tensors with 3 indices with free indices in slot 1 and 0

    >>> tensor_gens(base, gens, [[1], [0]])
    (8, [0, 4], [(7)(0 2), (7)(4 5)])

    four symmetric tensors with 3 indices, two of which with free indices

    """
def gens_products(*v):
    """
    Returns size, res_base, res_gens BSGS for n tensors of different types.

    Explanation
    ===========

    v is a sequence of (base_i, gens_i, free_i, sym_i)
    where
    base_i, gens_i  BSGS of tensor of type `i`
    free_i          list of the fixed slots for each of the tensors
                    of type `i`; if there are `n_i` tensors of type `i`
                    and none of them have fixed slots, `free = [[]]*n_i`
    sym   0 (1) if the tensors of type `i` (anti)commute among themselves

    Examples
    ========

    >>> from sympy.combinatorics.tensor_can import get_symmetric_group_sgs, gens_products
    >>> base, gens = get_symmetric_group_sgs(2)
    >>> gens_products((base, gens, [[], []], 0))
    (6, [0, 2], [(5)(0 1), (5)(2 3), (5)(0 2)(1 3)])
    >>> gens_products((base, gens, [[1], []], 0))
    (6, [2], [(5)(2 3)])
    """
