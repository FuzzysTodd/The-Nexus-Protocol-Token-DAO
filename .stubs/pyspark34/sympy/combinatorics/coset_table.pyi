from _typeshed import Incomplete
from sympy.combinatorics.free_groups import free_group as free_group
from sympy.printing.defaults import DefaultPrinting as DefaultPrinting

class CosetTable(DefaultPrinting):
    '''

    Properties
    ==========

    [1] `0 \\in \\Omega` and `\\tau(1) = \\epsilon`
    [2] `\\alpha^x = \\beta \\Leftrightarrow \\beta^{x^{-1}} = \\alpha`
    [3] If `\\alpha^x = \\beta`, then `H \\tau(\\alpha)x = H \\tau(\\beta)`
    [4] `\\forall \\alpha \\in \\Omega, 1^{\\tau(\\alpha)} = \\alpha`

    References
    ==========

    .. [1] Holt, D., Eick, B., O\'Brien, E.
           "Handbook of Computational Group Theory"

    .. [2] John J. Cannon; Lucien A. Dimino; George Havas; Jane M. Watson
           Mathematics of Computation, Vol. 27, No. 123. (Jul., 1973), pp. 463-490.
           "Implementation and Analysis of the Todd-Coxeter Algorithm"

    '''
    coset_table_max_limit: int
    coset_table_limit: Incomplete
    max_stack_size: int
    fp_group: Incomplete
    subgroup: Incomplete
    p: Incomplete
    A: Incomplete
    P: Incomplete
    table: Incomplete
    A_dict: Incomplete
    A_dict_inv: Incomplete
    deduction_stack: Incomplete
    p_p: Incomplete
    def __init__(self, fp_grp, subgroup, max_cosets: Incomplete | None = None) -> None: ...
    @property
    def omega(self):
        """Set of live cosets. """
    def copy(self):
        """
        Return a shallow copy of Coset Table instance ``self``.

        """
    @property
    def n(self):
        """The number `n` represents the length of the sublist containing the
        live cosets.

        """
    def is_complete(self):
        """
        The coset table is called complete if it has no undefined entries
        on the live cosets; that is, `\\alpha^x` is defined for all
        `\\alpha \\in \\Omega` and `x \\in A`.

        """
    def define(self, alpha, x, modified: bool = False) -> None:
        """
        This routine is used in the relator-based strategy of Todd-Coxeter
        algorithm if some `\\alpha^x` is undefined. We check whether there is
        space available for defining a new coset. If there is enough space
        then we remedy this by adjoining a new coset `\\beta` to `\\Omega`
        (i.e to set of live cosets) and put that equal to `\\alpha^x`, then
        make an assignment satisfying Property[1]. If there is not enough space
        then we halt the Coset Table creation. The maximum amount of space that
        can be used by Coset Table can be manipulated using the class variable
        ``CosetTable.coset_table_max_limit``.

        See Also
        ========

        define_c

        """
    def define_c(self, alpha, x) -> None:
        """
        A variation of ``define`` routine, described on Pg. 165 [1], used in
        the coset table-based strategy of Todd-Coxeter algorithm. It differs
        from ``define`` routine in that for each definition it also adds the
        tuple `(\\alpha, x)` to the deduction stack.

        See Also
        ========

        define

        """
    def scan_c(self, alpha, word) -> None:
        """
        A variation of ``scan`` routine, described on pg. 165 of [1], which
        puts at tuple, whenever a deduction occurs, to deduction stack.

        See Also
        ========

        scan, scan_check, scan_and_fill, scan_and_fill_c

        """
    def coincidence_c(self, alpha, beta) -> None:
        """
        A variation of ``coincidence`` routine used in the coset-table based
        method of coset enumeration. The only difference being on addition of
        a new coset in coset table(i.e new coset introduction), then it is
        appended to ``deduction_stack``.

        See Also
        ========

        coincidence

        """
    def scan(self, alpha, word, y: Incomplete | None = None, fill: bool = False, modified: bool = False) -> None:
        """
        ``scan`` performs a scanning process on the input ``word``.
        It first locates the largest prefix ``s`` of ``word`` for which
        `\\alpha^s` is defined (i.e is not ``None``), ``s`` may be empty. Let
        ``word=sv``, let ``t`` be the longest suffix of ``v`` for which
        `\\alpha^{t^{-1}}` is defined, and let ``v=ut``. Then three
        possibilities are there:

        1. If ``t=v``, then we say that the scan completes, and if, in addition
        `\\alpha^s = \\alpha^{t^{-1}}`, then we say that the scan completes
        correctly.

        2. It can also happen that scan does not complete, but `|u|=1`; that
        is, the word ``u`` consists of a single generator `x \\in A`. In that
        case, if `\\alpha^s = \\beta` and `\\alpha^{t^{-1}} = \\gamma`, then we can
        set `\\beta^x = \\gamma` and `\\gamma^{x^{-1}} = \\beta`. These assignments
        are known as deductions and enable the scan to complete correctly.

        3. See ``coicidence`` routine for explanation of third condition.

        Notes
        =====

        The code for the procedure of scanning `\\alpha \\in \\Omega`
        under `w \\in A*` is defined on pg. 155 [1]

        See Also
        ========

        scan_c, scan_check, scan_and_fill, scan_and_fill_c

        Scan and Fill
        =============

        Performed when the default argument fill=True.

        Modified Scan
        =============

        Performed when the default argument modified=True

        """
    def scan_check(self, alpha, word):
        """
        Another version of ``scan`` routine, described on, it checks whether
        `\\alpha` scans correctly under `word`, it is a straightforward
        modification of ``scan``. ``scan_check`` returns ``False`` (rather than
        calling ``coincidence``) if the scan completes incorrectly; otherwise
        it returns ``True``.

        See Also
        ========

        scan, scan_c, scan_and_fill, scan_and_fill_c

        """
    def merge(self, k, lamda, q, w: Incomplete | None = None, modified: bool = False) -> None:
        """
        Merge two classes with representatives ``k`` and ``lamda``, described
        on Pg. 157 [1] (for pseudocode), start by putting ``p[k] = lamda``.
        It is more efficient to choose the new representative from the larger
        of the two classes being merged, i.e larger among ``k`` and ``lamda``.
        procedure ``merge`` performs the merging operation, adds the deleted
        class representative to the queue ``q``.

        Parameters
        ==========

        'k', 'lamda' being the two class representatives to be merged.

        Notes
        =====

        Pg. 86-87 [1] contains a description of this method.

        See Also
        ========

        coincidence, rep

        """
    def rep(self, k, modified: bool = False):
        """
        Parameters
        ==========

        `k \\in [0 \\ldots n-1]`, as for ``self`` only array ``p`` is used

        Returns
        =======

        Representative of the class containing ``k``.

        Returns the representative of `\\sim` class containing ``k``, it also
        makes some modification to array ``p`` of ``self`` to ease further
        computations, described on Pg. 157 [1].

        The information on classes under `\\sim` is stored in array `p` of
        ``self`` argument, which will always satisfy the property:

        `p[\\alpha] \\sim \\alpha` and `p[\\alpha]=\\alpha \\iff \\alpha=rep(\\alpha)`
        `\\forall \\in [0 \\ldots n-1]`.

        So, for `\\alpha \\in [0 \\ldots n-1]`, we find `rep(self, \\alpha)` by
        continually replacing `\\alpha` by `p[\\alpha]` until it becomes
        constant (i.e satisfies `p[\\alpha] = \\alpha`):w

        To increase the efficiency of later ``rep`` calculations, whenever we
        find `rep(self, \\alpha)=\\beta`, we set
        `p[\\gamma] = \\beta \\forall \\gamma \\in p-chain` from `\\alpha` to `\\beta`

        Notes
        =====

        ``rep`` routine is also described on Pg. 85-87 [1] in Atkinson's
        algorithm, this results from the fact that ``coincidence`` routine
        introduces functionality similar to that introduced by the
        ``minimal_block`` routine on Pg. 85-87 [1].

        See Also
        ========

        coincidence, merge

        """
    def coincidence(self, alpha, beta, w: Incomplete | None = None, modified: bool = False) -> None:
        """
        The third situation described in ``scan`` routine is handled by this
        routine, described on Pg. 156-161 [1].

        The unfortunate situation when the scan completes but not correctly,
        then ``coincidence`` routine is run. i.e when for some `i` with
        `1 \\le i \\le r+1`, we have `w=st` with `s = x_1 x_2 \\dots x_{i-1}`,
        `t = x_i x_{i+1} \\dots x_r`, and `\\beta = \\alpha^s` and
        `\\gamma = \\alpha^{t-1}` are defined but unequal. This means that
        `\\beta` and `\\gamma` represent the same coset of `H` in `G`. Described
        on Pg. 156 [1]. ``rep``

        See Also
        ========

        scan

        """
    def scan_and_fill(self, alpha, word) -> None:
        """
        A modified version of ``scan`` routine used in the relator-based
        method of coset enumeration, described on pg. 162-163 [1], which
        follows the idea that whenever the procedure is called and the scan
        is incomplete then it makes new definitions to enable the scan to
        complete; i.e it fills in the gaps in the scan of the relator or
        subgroup generator.

        """
    def scan_and_fill_c(self, alpha, word) -> None:
        """
        A modified version of ``scan`` routine, described on Pg. 165 second
        para. [1], with modification similar to that of ``scan_anf_fill`` the
        only difference being it calls the coincidence procedure used in the
        coset-table based method i.e. the routine ``coincidence_c`` is used.

        See Also
        ========

        scan, scan_and_fill

        """
    def look_ahead(self) -> None:
        '''
        When combined with the HLT method this is known as HLT+Lookahead
        method of coset enumeration, described on pg. 164 [1]. Whenever
        ``define`` aborts due to lack of space available this procedure is
        executed. This routine helps in recovering space resulting from
        "coincidence" of cosets.

        '''
    def process_deductions(self, R_c_x, R_c_x_inv) -> None:
        """
        Processes the deductions that have been pushed onto ``deduction_stack``,
        described on Pg. 166 [1] and is used in coset-table based enumeration.

        See Also
        ========

        deduction_stack

        """
    def process_deductions_check(self, R_c_x, R_c_x_inv):
        """
        A variation of ``process_deductions``, this calls ``scan_check``
        wherever ``process_deductions`` calls ``scan``, described on Pg. [1].

        See Also
        ========

        process_deductions

        """
    def switch(self, beta, gamma) -> None:
        """Switch the elements `\\beta, \\gamma \\in \\Omega` of ``self``, used
        by the ``standardize`` procedure, described on Pg. 167 [1].

        See Also
        ========

        standardize

        """
    def standardize(self) -> None:
        '''
        A coset table is standardized if when running through the cosets and
        within each coset through the generator images (ignoring generator
        inverses), the cosets appear in order of the integers
        `0, 1, \\dots, n`. "Standardize" reorders the elements of `\\Omega`
        such that, if we scan the coset table first by elements of `\\Omega`
        and then by elements of A, then the cosets occur in ascending order.
        ``standardize()`` is used at the end of an enumeration to permute the
        cosets so that they occur in some sort of standard order.

        Notes
        =====

        procedure is described on pg. 167-168 [1], it also makes use of the
        ``switch`` routine to replace by smaller integer value.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> from sympy.combinatorics.fp_groups import FpGroup, coset_enumeration_r
        >>> F, x, y = free_group("x, y")

        # Example 5.3 from [1]
        >>> f = FpGroup(F, [x**2*y**2, x**3*y**5])
        >>> C = coset_enumeration_r(f, [])
        >>> C.compress()
        >>> C.table
        [[1, 3, 1, 3], [2, 0, 2, 0], [3, 1, 3, 1], [0, 2, 0, 2]]
        >>> C.standardize()
        >>> C.table
        [[1, 2, 1, 2], [3, 0, 3, 0], [0, 3, 0, 3], [2, 1, 2, 1]]

        '''
    def compress(self) -> None:
        """Removes the non-live cosets from the coset table, described on
        pg. 167 [1].

        """
    def conjugates(self, R): ...
    def coset_representative(self, coset):
        '''
        Compute the coset representative of a given coset.

        Examples
        ========

        >>> from sympy.combinatorics import free_group
        >>> from sympy.combinatorics.fp_groups import FpGroup, coset_enumeration_r
        >>> F, x, y = free_group("x, y")
        >>> f = FpGroup(F, [x**3, y**3, x**-1*y**-1*x*y])
        >>> C = coset_enumeration_r(f, [x])
        >>> C.compress()
        >>> C.table
        [[0, 0, 1, 2], [1, 1, 2, 0], [2, 2, 0, 1]]
        >>> C.coset_representative(0)
        <identity>
        >>> C.coset_representative(1)
        y
        >>> C.coset_representative(2)
        y**-1

        '''
    def modified_define(self, alpha, x) -> None:
        """
        Define a function p_p from from [1..n] to A* as
        an additional component of the modified coset table.

        Parameters
        ==========

        \\alpha \\in \\Omega
        x \\in A*

        See Also
        ========

        define

        """
    def modified_scan(self, alpha, w, y, fill: bool = False) -> None:
        """
        Parameters
        ==========
        \\alpha \\in \\Omega
        w \\in A*
        y \\in (YUY^-1)
        fill -- `modified_scan_and_fill` when set to True.

        See Also
        ========

        scan
        """
    def modified_scan_and_fill(self, alpha, w, y) -> None: ...
    def modified_merge(self, k, lamda, w, q) -> None:
        """
        Parameters
        ==========

        'k', 'lamda' -- the two class representatives to be merged.
        q -- queue of length l of elements to be deleted from `\\Omega` *.
        w -- Word in (YUY^-1)

        See Also
        ========

        merge
        """
    def modified_rep(self, k) -> None:
        """
        Parameters
        ==========

        `k \\in [0 \\ldots n-1]`

        See Also
        ========

        rep
        """
    def modified_coincidence(self, alpha, beta, w) -> None:
        """
        Parameters
        ==========

        A coincident pair `\\alpha, \\beta \\in \\Omega, w \\in Y \\cup Y^{-1}`

        See Also
        ========

        coincidence

        """

def coset_enumeration_r(fp_grp, Y, max_cosets: Incomplete | None = None, draft: Incomplete | None = None, incomplete: bool = False, modified: bool = False):
    '''
    This is easier of the two implemented methods of coset enumeration.
    and is often called the HLT method, after Hazelgrove, Leech, Trotter
    The idea is that we make use of ``scan_and_fill`` makes new definitions
    whenever the scan is incomplete to enable the scan to complete; this way
    we fill in the gaps in the scan of the relator or subgroup generator,
    that\'s why the name relator-based method.

    An instance of `CosetTable` for `fp_grp` can be passed as the keyword
    argument `draft` in which case the coset enumeration will start with
    that instance and attempt to complete it.

    When `incomplete` is `True` and the function is unable to complete for
    some reason, the partially complete table will be returned.

    # TODO: complete the docstring

    See Also
    ========

    scan_and_fill,

    Examples
    ========

    >>> from sympy.combinatorics.free_groups import free_group
    >>> from sympy.combinatorics.fp_groups import FpGroup, coset_enumeration_r
    >>> F, x, y = free_group("x, y")

    # Example 5.1 from [1]
    >>> f = FpGroup(F, [x**3, y**3, x**-1*y**-1*x*y])
    >>> C = coset_enumeration_r(f, [x])
    >>> for i in range(len(C.p)):
    ...     if C.p[i] == i:
    ...         print(C.table[i])
    [0, 0, 1, 2]
    [1, 1, 2, 0]
    [2, 2, 0, 1]
    >>> C.p
    [0, 1, 2, 1, 1]

    # Example from exercises Q2 [1]
    >>> f = FpGroup(F, [x**2*y**2, y**-1*x*y*x**-3])
    >>> C = coset_enumeration_r(f, [])
    >>> C.compress(); C.standardize()
    >>> C.table
    [[1, 2, 3, 4],
    [5, 0, 6, 7],
    [0, 5, 7, 6],
    [7, 6, 5, 0],
    [6, 7, 0, 5],
    [2, 1, 4, 3],
    [3, 4, 2, 1],
    [4, 3, 1, 2]]

    # Example 5.2
    >>> f = FpGroup(F, [x**2, y**3, (x*y)**3])
    >>> Y = [x*y]
    >>> C = coset_enumeration_r(f, Y)
    >>> for i in range(len(C.p)):
    ...     if C.p[i] == i:
    ...         print(C.table[i])
    [1, 1, 2, 1]
    [0, 0, 0, 2]
    [3, 3, 1, 0]
    [2, 2, 3, 3]

    # Example 5.3
    >>> f = FpGroup(F, [x**2*y**2, x**3*y**5])
    >>> Y = []
    >>> C = coset_enumeration_r(f, Y)
    >>> for i in range(len(C.p)):
    ...     if C.p[i] == i:
    ...         print(C.table[i])
    [1, 3, 1, 3]
    [2, 0, 2, 0]
    [3, 1, 3, 1]
    [0, 2, 0, 2]

    # Example 5.4
    >>> F, a, b, c, d, e = free_group("a, b, c, d, e")
    >>> f = FpGroup(F, [a*b*c**-1, b*c*d**-1, c*d*e**-1, d*e*a**-1, e*a*b**-1])
    >>> Y = [a]
    >>> C = coset_enumeration_r(f, Y)
    >>> for i in range(len(C.p)):
    ...     if C.p[i] == i:
    ...         print(C.table[i])
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # example of "compress" method
    >>> C.compress()
    >>> C.table
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # Exercises Pg. 161, Q2.
    >>> F, x, y = free_group("x, y")
    >>> f = FpGroup(F, [x**2*y**2, y**-1*x*y*x**-3])
    >>> Y = []
    >>> C = coset_enumeration_r(f, Y)
    >>> C.compress()
    >>> C.standardize()
    >>> C.table
    [[1, 2, 3, 4],
    [5, 0, 6, 7],
    [0, 5, 7, 6],
    [7, 6, 5, 0],
    [6, 7, 0, 5],
    [2, 1, 4, 3],
    [3, 4, 2, 1],
    [4, 3, 1, 2]]

    # John J. Cannon; Lucien A. Dimino; George Havas; Jane M. Watson
    # Mathematics of Computation, Vol. 27, No. 123. (Jul., 1973), pp. 463-490
    # from 1973chwd.pdf
    # Table 1. Ex. 1
    >>> F, r, s, t = free_group("r, s, t")
    >>> E1 = FpGroup(F, [t**-1*r*t*r**-2, r**-1*s*r*s**-2, s**-1*t*s*t**-2])
    >>> C = coset_enumeration_r(E1, [r])
    >>> for i in range(len(C.p)):
    ...     if C.p[i] == i:
    ...         print(C.table[i])
    [0, 0, 0, 0, 0, 0]

    Ex. 2
    >>> F, a, b = free_group("a, b")
    >>> Cox = FpGroup(F, [a**6, b**6, (a*b)**2, (a**2*b**2)**2, (a**3*b**3)**5])
    >>> C = coset_enumeration_r(Cox, [a])
    >>> index = 0
    >>> for i in range(len(C.p)):
    ...     if C.p[i] == i:
    ...         index += 1
    >>> index
    500

    # Ex. 3
    >>> F, a, b = free_group("a, b")
    >>> B_2_4 = FpGroup(F, [a**4, b**4, (a*b)**4, (a**-1*b)**4, (a**2*b)**4,             (a*b**2)**4, (a**2*b**2)**4, (a**-1*b*a*b)**4, (a*b**-1*a*b)**4])
    >>> C = coset_enumeration_r(B_2_4, [a])
    >>> index = 0
    >>> for i in range(len(C.p)):
    ...     if C.p[i] == i:
    ...         index += 1
    >>> index
    1024

    References
    ==========

    .. [1] Holt, D., Eick, B., O\'Brien, E.
           "Handbook of computational group theory"

    '''
def modified_coset_enumeration_r(fp_grp, Y, max_cosets: Incomplete | None = None, draft: Incomplete | None = None, incomplete: bool = False):
    '''
    Introduce a new set of symbols y \\in Y that correspond to the
    generators of the subgroup. Store the elements of Y as a
    word P[\\alpha, x] and compute the coset table similar to that of
    the regular coset enumeration methods.

    Examples
    ========

    >>> from sympy.combinatorics.free_groups import free_group
    >>> from sympy.combinatorics.fp_groups import FpGroup
    >>> from sympy.combinatorics.coset_table import modified_coset_enumeration_r
    >>> F, x, y = free_group("x, y")
    >>> f = FpGroup(F, [x**3, y**3, x**-1*y**-1*x*y])
    >>> C = modified_coset_enumeration_r(f, [x])
    >>> C.table
    [[0, 0, 1, 2], [1, 1, 2, 0], [2, 2, 0, 1], [None, 1, None, None], [1, 3, None, None]]

    See Also
    ========

    coset_enumertation_r

    References
    ==========

    .. [1] Holt, D., Eick, B., O\'Brien, E.,
           "Handbook of Computational Group Theory",
           Section 5.3.2
    '''
def coset_enumeration_c(fp_grp, Y, max_cosets: Incomplete | None = None, draft: Incomplete | None = None, incomplete: bool = False):
    '''
    >>> from sympy.combinatorics.free_groups import free_group
    >>> from sympy.combinatorics.fp_groups import FpGroup, coset_enumeration_c
    >>> F, x, y = free_group("x, y")
    >>> f = FpGroup(F, [x**3, y**3, x**-1*y**-1*x*y])
    >>> C = coset_enumeration_c(f, [x])
    >>> C.table
    [[0, 0, 1, 2], [1, 1, 2, 0], [2, 2, 0, 1]]

    '''
