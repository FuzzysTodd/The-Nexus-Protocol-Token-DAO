from .exceptions import ClosureFailure as ClosureFailure, MissingUnityError as MissingUnityError, StructureError as StructureError
from .utilities import AlgIntPowers as AlgIntPowers, get_num_denom as get_num_denom, is_rat as is_rat
from _typeshed import Incomplete
from sympy.core.numbers import igcd as igcd, ilcm as ilcm
from sympy.core.symbol import Dummy as Dummy
from sympy.polys.densetools import dup_clear_denoms as dup_clear_denoms
from sympy.polys.domains.algebraicfield import AlgebraicField as AlgebraicField
from sympy.polys.domains.finitefield import FF as FF
from sympy.polys.domains.integerring import ZZ as ZZ
from sympy.polys.domains.rationalfield import QQ as QQ
from sympy.polys.matrices.domainmatrix import DomainMatrix as DomainMatrix
from sympy.polys.matrices.exceptions import DMBadInputError as DMBadInputError
from sympy.polys.matrices.normalforms import hermite_normal_form as hermite_normal_form
from sympy.polys.polyclasses import ANP as ANP
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed, UnificationFailed as UnificationFailed
from sympy.polys.polytools import Poly as Poly
from sympy.polys.polyutils import IntegerPowerable as IntegerPowerable

def to_col(coeffs):
    """Transform a list of integer coefficients into a column vector."""

class Module:
    '''
    Generic finitely-generated module.

    This is an abstract base class, and should not be instantiated directly.
    The two concrete subclasses are :py:class:`~.PowerBasis` and
    :py:class:`~.Submodule`.

    Every :py:class:`~.Submodule` is derived from another module, referenced
    by its ``parent`` attribute. If ``S`` is a submodule, then we refer to
    ``S.parent``, ``S.parent.parent``, and so on, as the "ancestors" of
    ``S``. Thus, every :py:class:`~.Module` is either a
    :py:class:`~.PowerBasis` or a :py:class:`~.Submodule`, some ancestor of
    which is a :py:class:`~.PowerBasis`.
    '''
    @property
    def n(self) -> None:
        """The number of generators of this module."""
    def mult_tab(self) -> None:
        """
        Get the multiplication table for this module (if closed under mult).

        Explanation
        ===========

        Computes a dictionary ``M`` of dictionaries of lists, representing the
        upper triangular half of the multiplication table.

        In other words, if ``0 <= i <= j < self.n``, then ``M[i][j]`` is the
        list ``c`` of coefficients such that
        ``g[i] * g[j] == sum(c[k]*g[k], k in range(self.n))``,
        where ``g`` is the list of generators of this module.

        If ``j < i`` then ``M[i][j]`` is undefined.

        Examples
        ========

        >>> from sympy.polys import Poly, cyclotomic_poly
        >>> from sympy.polys.numberfields.modules import PowerBasis
        >>> T = Poly(cyclotomic_poly(5))
        >>> A = PowerBasis(T)
        >>> print(A.mult_tab())  # doctest: +SKIP
        {0: {0: [1, 0, 0, 0], 1: [0, 1, 0, 0], 2: [0, 0, 1, 0],     3: [0, 0, 0, 1]},
                          1: {1: [0, 0, 1, 0], 2: [0, 0, 0, 1],     3: [-1, -1, -1, -1]},
                                           2: {2: [-1, -1, -1, -1], 3: [1, 0, 0, 0]},
                                                                3: {3: [0, 1, 0, 0]}}

        Returns
        =======

        dict of dict of lists

        Raises
        ======

        ClosureFailure
            If the module is not closed under multiplication.

        """
    @property
    def parent(self) -> None:
        """
        The parent module, if any, for this module.

        Explanation
        ===========

        For a :py:class:`~.Submodule` this is its ``parent`` attribute; for a
        :py:class:`~.PowerBasis` this is ``None``.

        Returns
        =======

        :py:class:`~.Module`, ``None``

        See Also
        ========

        Module

        """
    def represent(self, elt) -> None:
        '''
        Represent a module element as an integer-linear combination over the
        generators of this module.

        Explanation
        ===========

        In our system, to "represent" always means to write a
        :py:class:`~.ModuleElement` as a :ref:`ZZ`-linear combination over the
        generators of the present :py:class:`~.Module`. Furthermore, the
        incoming :py:class:`~.ModuleElement` must belong to an ancestor of
        the present :py:class:`~.Module` (or to the present
        :py:class:`~.Module` itself).

        The most common application is to represent a
        :py:class:`~.ModuleElement` in a :py:class:`~.Submodule`. For example,
        this is involved in computing multiplication tables.

        On the other hand, representing in a :py:class:`~.PowerBasis` is an
        odd case, and one which tends not to arise in practice, except for
        example when using a :py:class:`~.ModuleEndomorphism` on a
        :py:class:`~.PowerBasis`.

        In such a case, (1) the incoming :py:class:`~.ModuleElement` must
        belong to the :py:class:`~.PowerBasis` itself (since the latter has no
        proper ancestors) and (2) it is "representable" iff it belongs to
        $\\mathbb{Z}[\\theta]$ (although generally a
        :py:class:`~.PowerBasisElement` may represent any element of
        $\\mathbb{Q}(\\theta)$, i.e. any algebraic number).

        Examples
        ========

        >>> from sympy import Poly, cyclotomic_poly
        >>> from sympy.polys.numberfields.modules import PowerBasis, to_col
        >>> from sympy.abc import zeta
        >>> T = Poly(cyclotomic_poly(5))
        >>> A = PowerBasis(T)
        >>> a = A(to_col([2, 4, 6, 8]))

        The :py:class:`~.ModuleElement` ``a`` has all even coefficients.
        If we represent ``a`` in the submodule ``B = 2*A``, the coefficients in
        the column vector will be halved:

        >>> B = A.submodule_from_gens([2*A(i) for i in range(4)])
        >>> b = B.represent(a)
        >>> print(b.transpose())  # doctest: +SKIP
        DomainMatrix([[1, 2, 3, 4]], (1, 4), ZZ)

        However, the element of ``B`` so defined still represents the same
        algebraic number:

        >>> print(a.poly(zeta).as_expr())
        8*zeta**3 + 6*zeta**2 + 4*zeta + 2
        >>> print(B(b).over_power_basis().poly(zeta).as_expr())
        8*zeta**3 + 6*zeta**2 + 4*zeta + 2

        Parameters
        ==========

        elt : :py:class:`~.ModuleElement`
            The module element to be represented. Must belong to some ancestor
            module of this module (including this module itself).

        Returns
        =======

        :py:class:`~.DomainMatrix` over :ref:`ZZ`
            This will be a column vector, representing the coefficients of a
            linear combination of this module\'s generators, which equals the
            given element.

        Raises
        ======

        ClosureFailure
            If the given element cannot be represented as a :ref:`ZZ`-linear
            combination over this module.

        See Also
        ========

        .Submodule.represent
        .PowerBasis.represent

        '''
    def ancestors(self, include_self: bool = False):
        """
        Return the list of ancestor modules of this module, from the
        foundational :py:class:`~.PowerBasis` downward, optionally including
        ``self``.

        See Also
        ========

        Module

        """
    def power_basis_ancestor(self):
        """
        Return the :py:class:`~.PowerBasis` that is an ancestor of this module.

        See Also
        ========

        Module

        """
    def nearest_common_ancestor(self, other):
        """
        Locate the nearest common ancestor of this module and another.

        Returns
        =======

        :py:class:`~.Module`, ``None``

        See Also
        ========

        Module

        """
    @property
    def number_field(self):
        """
        Return the associated :py:class:`~.AlgebraicField`, if any.

        Explanation
        ===========

        A :py:class:`~.PowerBasis` can be constructed on a :py:class:`~.Poly`
        $f$ or on an :py:class:`~.AlgebraicField` $K$. In the latter case, the
        :py:class:`~.PowerBasis` and all its descendant modules will return $K$
        as their ``.number_field`` property, while in the former case they will
        all return ``None``.

        Returns
        =======

        :py:class:`~.AlgebraicField`, ``None``

        """
    def is_compat_col(self, col):
        """Say whether *col* is a suitable column vector for this module."""
    def __call__(self, spec, denom: int = 1):
        """
        Generate a :py:class:`~.ModuleElement` belonging to this module.

        Examples
        ========

        >>> from sympy.polys import Poly, cyclotomic_poly
        >>> from sympy.polys.numberfields.modules import PowerBasis, to_col
        >>> T = Poly(cyclotomic_poly(5))
        >>> A = PowerBasis(T)
        >>> e = A(to_col([1, 2, 3, 4]), denom=3)
        >>> print(e)  # doctest: +SKIP
        [1, 2, 3, 4]/3
        >>> f = A(2)
        >>> print(f)  # doctest: +SKIP
        [0, 0, 1, 0]

        Parameters
        ==========

        spec : :py:class:`~.DomainMatrix`, int
            Specifies the numerators of the coefficients of the
            :py:class:`~.ModuleElement`. Can be either a column vector over
            :ref:`ZZ`, whose length must equal the number $n$ of generators of
            this module, or else an integer ``j``, $0 \\leq j < n$, which is a
            shorthand for column $j$ of $I_n$, the $n \\times n$ identity
            matrix.
        denom : int, optional (default=1)
            Denominator for the coefficients of the
            :py:class:`~.ModuleElement`.

        Returns
        =======

        :py:class:`~.ModuleElement`
            The coefficients are the entries of the *spec* vector, divided by
            *denom*.

        """
    def starts_with_unity(self) -> None:
        """Say whether the module's first generator equals unity."""
    def basis_elements(self):
        """
        Get list of :py:class:`~.ModuleElement` being the generators of this
        module.
        """
    def zero(self):
        """Return a :py:class:`~.ModuleElement` representing zero."""
    def one(self):
        """
        Return a :py:class:`~.ModuleElement` representing unity,
        and belonging to the first ancestor of this module (including
        itself) that starts with unity.
        """
    def element_from_rational(self, a) -> None:
        """
        Return a :py:class:`~.ModuleElement` representing a rational number.

        Explanation
        ===========

        The returned :py:class:`~.ModuleElement` will belong to the first
        module on this module's ancestor chain (including this module
        itself) that starts with unity.

        Examples
        ========

        >>> from sympy.polys import Poly, cyclotomic_poly, QQ
        >>> from sympy.polys.numberfields.modules import PowerBasis
        >>> T = Poly(cyclotomic_poly(5))
        >>> A = PowerBasis(T)
        >>> a = A.element_from_rational(QQ(2, 3))
        >>> print(a)  # doctest: +SKIP
        [2, 0, 0, 0]/3

        Parameters
        ==========

        a : int, :ref:`ZZ`, :ref:`QQ`

        Returns
        =======

        :py:class:`~.ModuleElement`

        """
    def submodule_from_gens(self, gens, hnf: bool = True, hnf_modulus: Incomplete | None = None):
        """
        Form the submodule generated by a list of :py:class:`~.ModuleElement`
        belonging to this module.

        Examples
        ========

        >>> from sympy.polys import Poly, cyclotomic_poly
        >>> from sympy.polys.numberfields.modules import PowerBasis
        >>> T = Poly(cyclotomic_poly(5))
        >>> A = PowerBasis(T)
        >>> gens = [A(0), 2*A(1), 3*A(2), 4*A(3)//5]
        >>> B = A.submodule_from_gens(gens)
        >>> print(B)  # doctest: +SKIP
        Submodule[[5, 0, 0, 0], [0, 10, 0, 0], [0, 0, 15, 0], [0, 0, 0, 4]]/5

        Parameters
        ==========

        gens : list of :py:class:`~.ModuleElement` belonging to this module.
        hnf : boolean, optional (default=True)
            If True, we will reduce the matrix into Hermite Normal Form before
            forming the :py:class:`~.Submodule`.
        hnf_modulus : int, None, optional (default=None)
            Modulus for use in the HNF reduction algorithm. See
            :py:func:`~sympy.polys.matrices.normalforms.hermite_normal_form`.

        Returns
        =======

        :py:class:`~.Submodule`

        See Also
        ========

        submodule_from_matrix

        """
    def submodule_from_matrix(self, B, denom: int = 1):
        """
        Form the submodule generated by the elements of this module indicated
        by the columns of a matrix, with an optional denominator.

        Examples
        ========

        >>> from sympy.polys import Poly, cyclotomic_poly, ZZ
        >>> from sympy.polys.matrices import DM
        >>> from sympy.polys.numberfields.modules import PowerBasis
        >>> T = Poly(cyclotomic_poly(5))
        >>> A = PowerBasis(T)
        >>> B = A.submodule_from_matrix(DM([
        ...     [0, 10, 0, 0],
        ...     [0,  0, 7, 0],
        ... ], ZZ).transpose(), denom=15)
        >>> print(B)  # doctest: +SKIP
        Submodule[[0, 10, 0, 0], [0, 0, 7, 0]]/15

        Parameters
        ==========

        B : :py:class:`~.DomainMatrix` over :ref:`ZZ`
            Each column gives the numerators of the coefficients of one
            generator of the submodule. Thus, the number of rows of *B* must
            equal the number of generators of the present module.
        denom : int, optional (default=1)
            Common denominator for all generators of the submodule.

        Returns
        =======

        :py:class:`~.Submodule`

        Raises
        ======

        ValueError
            If the given matrix *B* is not over :ref:`ZZ` or its number of rows
            does not equal the number of generators of the present module.

        See Also
        ========

        submodule_from_gens

        """
    def whole_submodule(self):
        """
        Return a submodule equal to this entire module.

        Explanation
        ===========

        This is useful when you have a :py:class:`~.PowerBasis` and want to
        turn it into a :py:class:`~.Submodule` (in order to use methods
        belonging to the latter).

        """
    def endomorphism_ring(self):
        """Form the :py:class:`~.EndomorphismRing` for this module."""

class PowerBasis(Module):
    """The module generated by the powers of an algebraic integer."""
    K: Incomplete
    T: Incomplete
    def __init__(self, T) -> None:
        """
        Parameters
        ==========

        T : :py:class:`~.Poly`, :py:class:`~.AlgebraicField`
            Either (1) the monic, irreducible, univariate polynomial over
            :ref:`ZZ`, a root of which is the generator of the power basis,
            or (2) an :py:class:`~.AlgebraicField` whose primitive element
            is the generator of the power basis.

        """
    @property
    def number_field(self): ...
    def __eq__(self, other): ...
    @property
    def n(self): ...
    def mult_tab(self): ...
    def compute_mult_tab(self) -> None: ...
    def represent(self, elt):
        """
        Represent a module element as an integer-linear combination over the
        generators of this module.

        See Also
        ========

        .Module.represent
        .Submodule.represent

        """
    def starts_with_unity(self): ...
    def element_from_rational(self, a): ...
    def element_from_poly(self, f):
        """
        Produce an element of this module, representing *f* after reduction mod
        our defining minimal polynomial.

        Parameters
        ==========

        f : :py:class:`~.Poly` over :ref:`ZZ` in same var as our defining poly.

        Returns
        =======

        :py:class:`~.PowerBasisElement`

        """
    def element_from_ANP(self, a):
        """Convert an ANP into a PowerBasisElement. """
    def element_from_alg_num(self, a):
        """Convert an AlgebraicNumber into a PowerBasisElement. """

class Submodule(Module, IntegerPowerable):
    """A submodule of another module."""
    def __init__(self, parent, matrix, denom: int = 1, mult_tab: Incomplete | None = None) -> None:
        """
        Parameters
        ==========

        parent : :py:class:`~.Module`
            The module from which this one is derived.
        matrix : :py:class:`~.DomainMatrix` over :ref:`ZZ`
            The matrix whose columns define this submodule's generators as
            linear combinations over the parent's generators.
        denom : int, optional (default=1)
            Denominator for the coefficients given by the matrix.
        mult_tab : dict, ``None``, optional
            If already known, the multiplication table for this module may be
            supplied.

        """
    def reduced(self):
        """
        Produce a reduced version of this submodule.

        Explanation
        ===========

        In the reduced version, it is guaranteed that 1 is the only positive
        integer dividing both the submodule's denominator, and every entry in
        the submodule's matrix.

        Returns
        =======

        :py:class:`~.Submodule`

        """
    def discard_before(self, r):
        """
        Produce a new module by discarding all generators before a given
        index *r*.
        """
    @property
    def n(self): ...
    def mult_tab(self): ...
    def compute_mult_tab(self) -> None: ...
    @property
    def parent(self): ...
    @property
    def matrix(self): ...
    @property
    def coeffs(self): ...
    @property
    def denom(self): ...
    @property
    def QQ_matrix(self):
        """
        :py:class:`~.DomainMatrix` over :ref:`QQ`, equal to
        ``self.matrix / self.denom``, and guaranteed to be dense.

        Explanation
        ===========

        Depending on how it is formed, a :py:class:`~.DomainMatrix` may have
        an internal representation that is sparse or dense. We guarantee a
        dense representation here, so that tests for equivalence of submodules
        always come out as expected.

        Examples
        ========

        >>> from sympy.polys import Poly, cyclotomic_poly, ZZ
        >>> from sympy.abc import x
        >>> from sympy.polys.matrices import DomainMatrix
        >>> from sympy.polys.numberfields.modules import PowerBasis
        >>> T = Poly(cyclotomic_poly(5, x))
        >>> A = PowerBasis(T)
        >>> B = A.submodule_from_matrix(3*DomainMatrix.eye(4, ZZ), denom=6)
        >>> C = A.submodule_from_matrix(DomainMatrix.eye(4, ZZ), denom=2)
        >>> print(B.QQ_matrix == C.QQ_matrix)
        True

        Returns
        =======

        :py:class:`~.DomainMatrix` over :ref:`QQ`

        """
    def starts_with_unity(self): ...
    def is_sq_maxrank_HNF(self): ...
    def is_power_basis_submodule(self): ...
    def element_from_rational(self, a): ...
    def basis_element_pullbacks(self):
        """
        Return list of this submodule's basis elements as elements of the
        submodule's parent module.
        """
    def represent(self, elt):
        """
        Represent a module element as an integer-linear combination over the
        generators of this module.

        See Also
        ========

        .Module.represent
        .PowerBasis.represent

        """
    def is_compat_submodule(self, other): ...
    def __eq__(self, other): ...
    def add(self, other, hnf: bool = True, hnf_modulus: Incomplete | None = None):
        """
        Add this :py:class:`~.Submodule` to another.

        Explanation
        ===========

        This represents the module generated by the union of the two modules'
        sets of generators.

        Parameters
        ==========

        other : :py:class:`~.Submodule`
        hnf : boolean, optional (default=True)
            If ``True``, reduce the matrix of the combined module to its
            Hermite Normal Form.
        hnf_modulus : :ref:`ZZ`, None, optional
            If a positive integer is provided, use this as modulus in the
            HNF reduction. See
            :py:func:`~sympy.polys.matrices.normalforms.hermite_normal_form`.

        Returns
        =======

        :py:class:`~.Submodule`

        """
    def __add__(self, other): ...
    __radd__ = __add__
    def mul(self, other, hnf: bool = True, hnf_modulus: Incomplete | None = None):
        """
        Multiply this :py:class:`~.Submodule` by a rational number, a
        :py:class:`~.ModuleElement`, or another :py:class:`~.Submodule`.

        Explanation
        ===========

        To multiply by a rational number or :py:class:`~.ModuleElement` means
        to form the submodule whose generators are the products of this
        quantity with all the generators of the present submodule.

        To multiply by another :py:class:`~.Submodule` means to form the
        submodule whose generators are all the products of one generator from
        the one submodule, and one generator from the other.

        Parameters
        ==========

        other : int, :ref:`ZZ`, :ref:`QQ`, :py:class:`~.ModuleElement`, :py:class:`~.Submodule`
        hnf : boolean, optional (default=True)
            If ``True``, reduce the matrix of the product module to its
            Hermite Normal Form.
        hnf_modulus : :ref:`ZZ`, None, optional
            If a positive integer is provided, use this as modulus in the
            HNF reduction. See
            :py:func:`~sympy.polys.matrices.normalforms.hermite_normal_form`.

        Returns
        =======

        :py:class:`~.Submodule`

        """
    def __mul__(self, other): ...
    __rmul__ = __mul__
    def reduce_element(self, elt):
        '''
        If this submodule $B$ has defining matrix $W$ in square, maximal-rank
        Hermite normal form, then, given an element $x$ of the parent module
        $A$, we produce an element $y \\in A$ such that $x - y \\in B$, and the
        $i$th coordinate of $y$ satisfies $0 \\leq y_i < w_{i,i}$. This
        representative $y$ is unique, in the sense that every element of
        the coset $x + B$ reduces to it under this procedure.

        Explanation
        ===========

        In the special case where $A$ is a power basis for a number field $K$,
        and $B$ is a submodule representing an ideal $I$, this operation
        represents one of a few important ways of reducing an element of $K$
        modulo $I$ to obtain a "small" representative. See [Cohen00]_ Section
        1.4.3.

        Examples
        ========

        >>> from sympy import QQ, Poly, symbols
        >>> t = symbols(\'t\')
        >>> k = QQ.alg_field_from_poly(Poly(t**3 + t**2 - 2*t + 8))
        >>> Zk = k.maximal_order()
        >>> A = Zk.parent
        >>> B = (A(2) - 3*A(0))*Zk
        >>> B.reduce_element(A(2))
        [3, 0, 0]

        Parameters
        ==========

        elt : :py:class:`~.ModuleElement`
            An element of this submodule\'s parent module.

        Returns
        =======

        elt : :py:class:`~.ModuleElement`
            An element of this submodule\'s parent module.

        Raises
        ======

        NotImplementedError
            If the given :py:class:`~.ModuleElement` does not belong to this
            submodule\'s parent module.
        StructureError
            If this submodule\'s defining matrix is not in square, maximal-rank
            Hermite normal form.

        References
        ==========

        .. [Cohen00] Cohen, H. *Advanced Topics in Computational Number
           Theory.*

        '''

def is_sq_maxrank_HNF(dm):
    """
    Say whether a :py:class:`~.DomainMatrix` is in that special case of Hermite
    Normal Form, in which the matrix is also square and of maximal rank.

    Explanation
    ===========

    We commonly work with :py:class:`~.Submodule` instances whose matrix is in
    this form, and it can be useful to be able to check that this condition is
    satisfied.

    For example this is the case with the :py:class:`~.Submodule` ``ZK``
    returned by :py:func:`~sympy.polys.numberfields.basis.round_two`, which
    represents the maximal order in a number field, and with ideals formed
    therefrom, such as ``2 * ZK``.

    """
def make_mod_elt(module, col, denom: int = 1):
    """
    Factory function which builds a :py:class:`~.ModuleElement`, but ensures
    that it is a :py:class:`~.PowerBasisElement` if the module is a
    :py:class:`~.PowerBasis`.
    """

class ModuleElement(IntegerPowerable):
    """
    Represents an element of a :py:class:`~.Module`.

    NOTE: Should not be constructed directly. Use the
    :py:meth:`~.Module.__call__` method or the :py:func:`make_mod_elt()`
    factory function instead.
    """
    module: Incomplete
    col: Incomplete
    denom: Incomplete
    def __init__(self, module, col, denom: int = 1) -> None:
        """
        Parameters
        ==========

        module : :py:class:`~.Module`
            The module to which this element belongs.
        col : :py:class:`~.DomainMatrix` over :ref:`ZZ`
            Column vector giving the numerators of the coefficients of this
            element.
        denom : int, optional (default=1)
            Denominator for the coefficients of this element.

        """
    def reduced(self):
        """
        Produce a reduced version of this ModuleElement, i.e. one in which the
        gcd of the denominator together with all numerator coefficients is 1.
        """
    def reduced_mod_p(self, p):
        """
        Produce a version of this :py:class:`~.ModuleElement` in which all
        numerator coefficients have been reduced mod *p*.
        """
    @classmethod
    def from_int_list(cls, module, coeffs, denom: int = 1):
        """
        Make a :py:class:`~.ModuleElement` from a list of ints (instead of a
        column vector).
        """
    @property
    def n(self):
        """The length of this element's column."""
    def __len__(self) -> int: ...
    def column(self, domain: Incomplete | None = None):
        """
        Get a copy of this element's column, optionally converting to a domain.
        """
    @property
    def coeffs(self): ...
    @property
    def QQ_col(self):
        """
        :py:class:`~.DomainMatrix` over :ref:`QQ`, equal to
        ``self.col / self.denom``, and guaranteed to be dense.

        See Also
        ========

        .Submodule.QQ_matrix

        """
    def to_parent(self):
        """
        Transform into a :py:class:`~.ModuleElement` belonging to the parent of
        this element's module.
        """
    def to_ancestor(self, anc):
        """
        Transform into a :py:class:`~.ModuleElement` belonging to a given
        ancestor of this element's module.

        Parameters
        ==========

        anc : :py:class:`~.Module`

        """
    def over_power_basis(self):
        """
        Transform into a :py:class:`~.PowerBasisElement` over our
        :py:class:`~.PowerBasis` ancestor.
        """
    def is_compat(self, other):
        """
        Test whether other is another :py:class:`~.ModuleElement` with same
        module.
        """
    def unify(self, other):
        """
        Try to make a compatible pair of :py:class:`~.ModuleElement`, one
        equivalent to this one, and one equivalent to the other.

        Explanation
        ===========

        We search for the nearest common ancestor module for the pair of
        elements, and represent each one there.

        Returns
        =======

        Pair ``(e1, e2)``
            Each ``ei`` is a :py:class:`~.ModuleElement`, they belong to the
            same :py:class:`~.Module`, ``e1`` is equivalent to ``self``, and
            ``e2`` is equivalent to ``other``.

        Raises
        ======

        UnificationFailed
            If ``self`` and ``other`` have no common ancestor module.

        """
    def __eq__(self, other): ...
    def equiv(self, other):
        """
        A :py:class:`~.ModuleElement` may test as equivalent to a rational
        number or another :py:class:`~.ModuleElement`, if they represent the
        same algebraic number.

        Explanation
        ===========

        This method is intended to check equivalence only in those cases in
        which it is easy to test; namely, when *other* is either a
        :py:class:`~.ModuleElement` that can be unified with this one (i.e. one
        which shares a common :py:class:`~.PowerBasis` ancestor), or else a
        rational number (which is easy because every :py:class:`~.PowerBasis`
        represents every rational number).

        Parameters
        ==========

        other : int, :ref:`ZZ`, :ref:`QQ`, :py:class:`~.ModuleElement`

        Returns
        =======

        bool

        Raises
        ======

        UnificationFailed
            If ``self`` and ``other`` do not share a common
            :py:class:`~.PowerBasis` ancestor.

        """
    def __add__(self, other):
        """
        A :py:class:`~.ModuleElement` can be added to a rational number, or to
        another :py:class:`~.ModuleElement`.

        Explanation
        ===========

        When the other summand is a rational number, it will be converted into
        a :py:class:`~.ModuleElement` (belonging to the first ancestor of this
        module that starts with unity).

        In all cases, the sum belongs to the nearest common ancestor (NCA) of
        the modules of the two summands. If the NCA does not exist, we return
        ``NotImplemented``.
        """
    __radd__ = __add__
    def __neg__(self): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other):
        """
        A :py:class:`~.ModuleElement` can be multiplied by a rational number,
        or by another :py:class:`~.ModuleElement`.

        Explanation
        ===========

        When the multiplier is a rational number, the product is computed by
        operating directly on the coefficients of this
        :py:class:`~.ModuleElement`.

        When the multiplier is another :py:class:`~.ModuleElement`, the product
        will belong to the nearest common ancestor (NCA) of the modules of the
        two operands, and that NCA must have a multiplication table. If the NCA
        does not exist, we return ``NotImplemented``. If the NCA does not have
        a mult. table, ``ClosureFailure`` will be raised.
        """
    __rmul__ = __mul__
    def __floordiv__(self, a): ...
    def __rfloordiv__(self, a): ...
    def __mod__(self, m):
        """
        Reduce this :py:class:`~.ModuleElement` mod a :py:class:`~.Submodule`.

        Parameters
        ==========

        m : int, :ref:`ZZ`, :ref:`QQ`, :py:class:`~.Submodule`
            If a :py:class:`~.Submodule`, reduce ``self`` relative to this.
            If an integer or rational, reduce relative to the
            :py:class:`~.Submodule` that is our own module times this constant.

        See Also
        ========

        .Submodule.reduce_element

        """

class PowerBasisElement(ModuleElement):
    """
    Subclass for :py:class:`~.ModuleElement` instances whose module is a
    :py:class:`~.PowerBasis`.
    """
    @property
    def T(self):
        """Access the defining polynomial of the :py:class:`~.PowerBasis`."""
    def numerator(self, x: Incomplete | None = None):
        """Obtain the numerator as a polynomial over :ref:`ZZ`."""
    def poly(self, x: Incomplete | None = None):
        """Obtain the number as a polynomial over :ref:`QQ`."""
    @property
    def is_rational(self):
        """Say whether this element represents a rational number."""
    @property
    def generator(self):
        """
        Return a :py:class:`~.Symbol` to be used when expressing this element
        as a polynomial.

        If we have an associated :py:class:`~.AlgebraicField` whose primitive
        element has an alias symbol, we use that. Otherwise we use the variable
        of the minimal polynomial defining the power basis to which we belong.
        """
    def as_expr(self, x: Incomplete | None = None):
        """Create a Basic expression from ``self``. """
    def norm(self, T: Incomplete | None = None):
        """Compute the norm of this number."""
    def inverse(self): ...
    def __rfloordiv__(self, a): ...
    def to_ANP(self):
        """Convert to an equivalent :py:class:`~.ANP`. """
    def to_alg_num(self):
        """
        Try to convert to an equivalent :py:class:`~.AlgebraicNumber`.

        Explanation
        ===========

        In general, the conversion from an :py:class:`~.AlgebraicNumber` to a
        :py:class:`~.PowerBasisElement` throws away information, because an
        :py:class:`~.AlgebraicNumber` specifies a complex embedding, while a
        :py:class:`~.PowerBasisElement` does not. However, in some cases it is
        possible to convert a :py:class:`~.PowerBasisElement` back into an
        :py:class:`~.AlgebraicNumber`, namely when the associated
        :py:class:`~.PowerBasis` has a reference to an
        :py:class:`~.AlgebraicField`.

        Returns
        =======

        :py:class:`~.AlgebraicNumber`

        Raises
        ======

        StructureError
            If the :py:class:`~.PowerBasis` to which this element belongs does
            not have an associated :py:class:`~.AlgebraicField`.

        """

class ModuleHomomorphism:
    """A homomorphism from one module to another."""
    domain: Incomplete
    codomain: Incomplete
    mapping: Incomplete
    def __init__(self, domain, codomain, mapping) -> None:
        """
        Parameters
        ==========

        domain : :py:class:`~.Module`
            The domain of the mapping.

        codomain : :py:class:`~.Module`
            The codomain of the mapping.

        mapping : callable
            An arbitrary callable is accepted, but should be chosen so as
            to represent an actual module homomorphism. In particular, should
            accept elements of *domain* and return elements of *codomain*.

        Examples
        ========

        >>> from sympy import Poly, cyclotomic_poly
        >>> from sympy.polys.numberfields.modules import PowerBasis, ModuleHomomorphism
        >>> T = Poly(cyclotomic_poly(5))
        >>> A = PowerBasis(T)
        >>> B = A.submodule_from_gens([2*A(j) for j in range(4)])
        >>> phi = ModuleHomomorphism(A, B, lambda x: 6*x)
        >>> print(phi.matrix())  # doctest: +SKIP
        DomainMatrix([[3, 0, 0, 0], [0, 3, 0, 0], [0, 0, 3, 0], [0, 0, 0, 3]], (4, 4), ZZ)

        """
    def matrix(self, modulus: Incomplete | None = None):
        """
        Compute the matrix of this homomorphism.

        Parameters
        ==========

        modulus : int, optional
            A positive prime number $p$ if the matrix should be reduced mod
            $p$.

        Returns
        =======

        :py:class:`~.DomainMatrix`
            The matrix is over :ref:`ZZ`, or else over :ref:`GF(p)` if a
            modulus was given.

        """
    def kernel(self, modulus: Incomplete | None = None):
        """
        Compute a Submodule representing the kernel of this homomorphism.

        Parameters
        ==========

        modulus : int, optional
            A positive prime number $p$ if the kernel should be computed mod
            $p$.

        Returns
        =======

        :py:class:`~.Submodule`
            This submodule's generators span the kernel of this
            homomorphism over :ref:`ZZ`, or else over :ref:`GF(p)` if a
            modulus was given.

        """

class ModuleEndomorphism(ModuleHomomorphism):
    """A homomorphism from one module to itself."""
    def __init__(self, domain, mapping) -> None:
        """
        Parameters
        ==========

        domain : :py:class:`~.Module`
            The common domain and codomain of the mapping.

        mapping : callable
            An arbitrary callable is accepted, but should be chosen so as
            to represent an actual module endomorphism. In particular, should
            accept and return elements of *domain*.

        """

class InnerEndomorphism(ModuleEndomorphism):
    """
    An inner endomorphism on a module, i.e. the endomorphism corresponding to
    multiplication by a fixed element.
    """
    multiplier: Incomplete
    def __init__(self, domain, multiplier) -> None:
        """
        Parameters
        ==========

        domain : :py:class:`~.Module`
            The domain and codomain of the endomorphism.

        multiplier : :py:class:`~.ModuleElement`
            The element $a$ defining the mapping as $x \\mapsto a x$.

        """

class EndomorphismRing:
    """The ring of endomorphisms on a module."""
    domain: Incomplete
    def __init__(self, domain) -> None:
        """
        Parameters
        ==========

        domain : :py:class:`~.Module`
            The domain and codomain of the endomorphisms.

        """
    def inner_endomorphism(self, multiplier):
        """
        Form an inner endomorphism belonging to this endomorphism ring.

        Parameters
        ==========

        multiplier : :py:class:`~.ModuleElement`
            Element $a$ defining the inner endomorphism $x \\mapsto a x$.

        Returns
        =======

        :py:class:`~.InnerEndomorphism`

        """
    def represent(self, element):
        """
        Represent an element of this endomorphism ring, as a single column
        vector.

        Explanation
        ===========

        Let $M$ be a module, and $E$ its ring of endomorphisms. Let $N$ be
        another module, and consider a homomorphism $\\varphi: N \\rightarrow E$.
        In the event that $\\varphi$ is to be represented by a matrix $A$, each
        column of $A$ must represent an element of $E$. This is possible when
        the elements of $E$ are themselves representable as matrices, by
        stacking the columns of such a matrix into a single column.

        This method supports calculating such matrices $A$, by representing
        an element of this endomorphism ring first as a matrix, and then
        stacking that matrix's columns into a single column.

        Examples
        ========

        Note that in these examples we print matrix transposes, to make their
        columns easier to inspect.

        >>> from sympy import Poly, cyclotomic_poly
        >>> from sympy.polys.numberfields.modules import PowerBasis
        >>> from sympy.polys.numberfields.modules import ModuleHomomorphism
        >>> T = Poly(cyclotomic_poly(5))
        >>> M = PowerBasis(T)
        >>> E = M.endomorphism_ring()

        Let $\\zeta$ be a primitive 5th root of unity, a generator of our field,
        and consider the inner endomorphism $\\tau$ on the ring of integers,
        induced by $\\zeta$:

        >>> zeta = M(1)
        >>> tau = E.inner_endomorphism(zeta)
        >>> tau.matrix().transpose()  # doctest: +SKIP
        DomainMatrix(
            [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [-1, -1, -1, -1]],
            (4, 4), ZZ)

        The matrix representation of $\\tau$ is as expected. The first column
        shows that multiplying by $\\zeta$ carries $1$ to $\\zeta$, the second
        column that it carries $\\zeta$ to $\\zeta^2$, and so forth.

        The ``represent`` method of the endomorphism ring ``E`` stacks these
        into a single column:

        >>> E.represent(tau).transpose()  # doctest: +SKIP
        DomainMatrix(
            [[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, -1, -1, -1, -1]],
            (1, 16), ZZ)

        This is useful when we want to consider a homomorphism $\\varphi$ having
        ``E`` as codomain:

        >>> phi = ModuleHomomorphism(M, E, lambda x: E.inner_endomorphism(x))

        and we want to compute the matrix of such a homomorphism:

        >>> phi.matrix().transpose()  # doctest: +SKIP
        DomainMatrix(
            [[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, -1, -1, -1, -1],
            [0, 0, 1, 0, 0, 0, 0, 1, -1, -1, -1, -1, 1, 0, 0, 0],
            [0, 0, 0, 1, -1, -1, -1, -1, 1, 0, 0, 0, 0, 1, 0, 0]],
            (4, 16), ZZ)

        Note that the stacked matrix of $\\tau$ occurs as the second column in
        this example. This is because $\\zeta$ is the second basis element of
        ``M``, and $\\varphi(\\zeta) = \\tau$.

        Parameters
        ==========

        element : :py:class:`~.ModuleEndomorphism` belonging to this ring.

        Returns
        =======

        :py:class:`~.DomainMatrix`
            Column vector equalling the vertical stacking of all the columns
            of the matrix that represents the given *element* as a mapping.

        """

def find_min_poly(alpha, domain, x: Incomplete | None = None, powers: Incomplete | None = None):
    """
    Find a polynomial of least degree (not necessarily irreducible) satisfied
    by an element of a finitely-generated ring with unity.

    Examples
    ========

    For the $n$th cyclotomic field, $n$ an odd prime, consider the quadratic
    equation whose roots are the two periods of length $(n-1)/2$. Article 356
    of Gauss tells us that we should get $x^2 + x - (n-1)/4$ or
    $x^2 + x + (n+1)/4$ according to whether $n$ is 1 or 3 mod 4, respectively.

    >>> from sympy import Poly, cyclotomic_poly, primitive_root, QQ
    >>> from sympy.abc import x
    >>> from sympy.polys.numberfields.modules import PowerBasis, find_min_poly
    >>> n = 13
    >>> g = primitive_root(n)
    >>> C = PowerBasis(Poly(cyclotomic_poly(n, x)))
    >>> ee = [g**(2*k+1) % n for k in range((n-1)//2)]
    >>> eta = sum(C(e) for e in ee)
    >>> print(find_min_poly(eta, QQ, x=x).as_expr())
    x**2 + x - 3
    >>> n = 19
    >>> g = primitive_root(n)
    >>> C = PowerBasis(Poly(cyclotomic_poly(n, x)))
    >>> ee = [g**(2*k+2) % n for k in range((n-1)//2)]
    >>> eta = sum(C(e) for e in ee)
    >>> print(find_min_poly(eta, QQ, x=x).as_expr())
    x**2 + x + 5

    Parameters
    ==========

    alpha : :py:class:`~.ModuleElement`
        The element whose min poly is to be found, and whose module has
        multiplication and starts with unity.

    domain : :py:class:`~.Domain`
        The desired domain of the polynomial.

    x : :py:class:`~.Symbol`, optional
        The desired variable for the polynomial.

    powers : list, optional
        If desired, pass an empty list. The powers of *alpha* (as
        :py:class:`~.ModuleElement` instances) from the zeroth up to the degree
        of the min poly will be recorded here, as we compute them.

    Returns
    =======

    :py:class:`~.Poly`, ``None``
        The minimal polynomial for alpha, or ``None`` if no polynomial could be
        found over the desired domain.

    Raises
    ======

    MissingUnityError
        If the module to which alpha belongs does not start with unity.
    ClosureFailure
        If the module to which alpha belongs is not closed under
        multiplication.

    """
