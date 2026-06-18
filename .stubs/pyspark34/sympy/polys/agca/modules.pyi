from _typeshed import Incomplete
from sympy.polys.agca.ideals import Ideal as Ideal
from sympy.polys.domains.field import Field as Field
from sympy.polys.orderings import ProductOrder as ProductOrder, monomial_key as monomial_key
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed
from sympy.utilities.iterables import iterable as iterable

class Module:
    """
    Abstract base class for modules.

    Do not instantiate - use ring explicit constructors instead:

    >>> from sympy import QQ
    >>> from sympy.abc import x
    >>> QQ.old_poly_ring(x).free_module(2)
    QQ[x]**2

    Attributes:

    - dtype - type of elements
    - ring - containing ring

    Non-implemented methods:

    - submodule
    - quotient_module
    - is_zero
    - is_submodule
    - multiply_ideal

    The method convert likely needs to be changed in subclasses.
    """
    ring: Incomplete
    def __init__(self, ring) -> None: ...
    def convert(self, elem, M: Incomplete | None = None):
        """
        Convert ``elem`` into internal representation of this module.

        If ``M`` is not None, it should be a module containing it.
        """
    def submodule(self, *gens) -> None:
        """Generate a submodule."""
    def quotient_module(self, other) -> None:
        """Generate a quotient module."""
    def __truediv__(self, e): ...
    def contains(self, elem):
        """Return True if ``elem`` is an element of this module."""
    def __contains__(self, elem) -> bool: ...
    def subset(self, other):
        """
        Returns True if ``other`` is is a subset of ``self``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> F.subset([(1, x), (x, 2)])
        True
        >>> F.subset([(1/x, x), (x, 2)])
        False
        """
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def is_zero(self) -> None:
        """Returns True if ``self`` is a zero module."""
    def is_submodule(self, other) -> None:
        """Returns True if ``other`` is a submodule of ``self``."""
    def multiply_ideal(self, other) -> None:
        """
        Multiply ``self`` by the ideal ``other``.
        """
    def __mul__(self, e): ...
    __rmul__ = __mul__
    def identity_hom(self) -> None:
        """Return the identity homomorphism on ``self``."""

class ModuleElement:
    """
    Base class for module element wrappers.

    Use this class to wrap primitive data types as module elements. It stores
    a reference to the containing module, and implements all the arithmetic
    operators.

    Attributes:

    - module - containing module
    - data - internal data

    Methods that likely need change in subclasses:

    - add
    - mul
    - div
    - eq
    """
    module: Incomplete
    data: Incomplete
    def __init__(self, module, data) -> None: ...
    def add(self, d1, d2):
        """Add data ``d1`` and ``d2``."""
    def mul(self, m, d):
        """Multiply module data ``m`` by coefficient d."""
    def div(self, m, d):
        """Divide module data ``m`` by coefficient d."""
    def eq(self, d1, d2):
        """Return true if d1 and d2 represent the same element."""
    def __add__(self, om): ...
    __radd__ = __add__
    def __neg__(self): ...
    def __sub__(self, om): ...
    def __rsub__(self, om): ...
    def __mul__(self, o): ...
    __rmul__ = __mul__
    def __truediv__(self, o): ...
    def __eq__(self, om): ...
    def __ne__(self, om): ...

class FreeModuleElement(ModuleElement):
    """Element of a free module. Data stored as a tuple."""
    def add(self, d1, d2): ...
    def mul(self, d, p): ...
    def div(self, d, p): ...
    def __iter__(self): ...
    def __getitem__(self, idx): ...

class FreeModule(Module):
    """
    Abstract base class for free modules.

    Additional attributes:

    - rank - rank of the free module

    Non-implemented methods:

    - submodule
    """
    dtype = FreeModuleElement
    rank: Incomplete
    def __init__(self, ring, rank) -> None: ...
    def is_submodule(self, other):
        """
        Returns True if ``other`` is a submodule of ``self``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> M = F.submodule([2, x])
        >>> F.is_submodule(F)
        True
        >>> F.is_submodule(M)
        True
        >>> M.is_submodule(F)
        False
        """
    def convert(self, elem, M: Incomplete | None = None):
        """
        Convert ``elem`` into the internal representation.

        This method is called implicitly whenever computations involve elements
        not in the internal representation.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> F.convert([1, 0])
        [1, 0]
        """
    def is_zero(self):
        """
        Returns True if ``self`` is a zero module.

        (If, as this implementation assumes, the coefficient ring is not the
        zero ring, then this is equivalent to the rank being zero.)

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> QQ.old_poly_ring(x).free_module(0).is_zero()
        True
        >>> QQ.old_poly_ring(x).free_module(1).is_zero()
        False
        """
    def basis(self):
        """
        Return a set of basis elements.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> QQ.old_poly_ring(x).free_module(3).basis()
        ([1, 0, 0], [0, 1, 0], [0, 0, 1])
        """
    def quotient_module(self, submodule):
        """
        Return a quotient module.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> M = QQ.old_poly_ring(x).free_module(2)
        >>> M.quotient_module(M.submodule([1, x], [x, 2]))
        QQ[x]**2/<[1, x], [x, 2]>

        Or more conicisely, using the overloaded division operator:

        >>> QQ.old_poly_ring(x).free_module(2) / [[1, x], [x, 2]]
        QQ[x]**2/<[1, x], [x, 2]>
        """
    def multiply_ideal(self, other):
        """
        Multiply ``self`` by the ideal ``other``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> I = QQ.old_poly_ring(x).ideal(x)
        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> F.multiply_ideal(I)
        <[x, 0], [0, x]>
        """
    def identity_hom(self):
        """
        Return the identity homomorphism on ``self``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> QQ.old_poly_ring(x).free_module(2).identity_hom()
        Matrix([
        [1, 0], : QQ[x]**2 -> QQ[x]**2
        [0, 1]])
        """

class FreeModulePolyRing(FreeModule):
    """
    Free module over a generalized polynomial ring.

    Do not instantiate this, use the constructor method of the ring instead:

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy import QQ
    >>> F = QQ.old_poly_ring(x).free_module(3)
    >>> F
    QQ[x]**3
    >>> F.contains([x, 1, 0])
    True
    >>> F.contains([1/x, 0, 1])
    False
    """
    def __init__(self, ring, rank) -> None: ...
    def submodule(self, *gens, **opts):
        """
        Generate a submodule.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import QQ
        >>> M = QQ.old_poly_ring(x, y).free_module(2).submodule([x, x + y])
        >>> M
        <[x, x + y]>
        >>> M.contains([2*x, 2*x + 2*y])
        True
        >>> M.contains([x, y])
        False
        """

class FreeModuleQuotientRing(FreeModule):
    """
    Free module over a quotient ring.

    Do not instantiate this, use the constructor method of the ring instead:

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy import QQ
    >>> F = (QQ.old_poly_ring(x)/[x**2 + 1]).free_module(3)
    >>> F
    (QQ[x]/<x**2 + 1>)**3

    Attributes

    - quot - the quotient module `R^n / IR^n`, where `R/I` is our ring
    """
    quot: Incomplete
    def __init__(self, ring, rank) -> None: ...
    def submodule(self, *gens, **opts):
        """
        Generate a submodule.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import QQ
        >>> M = (QQ.old_poly_ring(x, y)/[x**2 - y**2]).free_module(2).submodule([x, x + y])
        >>> M
        <[x + <x**2 - y**2>, x + y + <x**2 - y**2>]>
        >>> M.contains([y**2, x**2 + x*y])
        True
        >>> M.contains([x, y])
        False
        """
    def lift(self, elem):
        """
        Lift the element ``elem`` of self to the module self.quot.

        Note that self.quot is the same set as self, just as an R-module
        and not as an R/I-module, so this makes sense.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = (QQ.old_poly_ring(x)/[x**2 + 1]).free_module(2)
        >>> e = F.convert([1, 0])
        >>> e
        [1 + <x**2 + 1>, 0 + <x**2 + 1>]
        >>> L = F.quot
        >>> l = F.lift(e)
        >>> l
        [1, 0] + <[x**2 + 1, 0], [0, x**2 + 1]>
        >>> L.contains(l)
        True
        """
    def unlift(self, elem):
        """
        Push down an element of self.quot to self.

        This undoes ``lift``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = (QQ.old_poly_ring(x)/[x**2 + 1]).free_module(2)
        >>> e = F.convert([1, 0])
        >>> l = F.lift(e)
        >>> e == l
        False
        >>> e == F.unlift(l)
        True
        """

class SubModule(Module):
    """
    Base class for submodules.

    Attributes:

    - container - containing module
    - gens - generators (subset of containing module)
    - rank - rank of containing module

    Non-implemented methods:

    - _contains
    - _syzygies
    - _in_terms_of_generators
    - _intersect
    - _module_quotient

    Methods that likely need change in subclasses:

    - reduce_element
    """
    gens: Incomplete
    container: Incomplete
    rank: Incomplete
    ring: Incomplete
    dtype: Incomplete
    def __init__(self, gens, container) -> None: ...
    def convert(self, elem, M: Incomplete | None = None):
        """
        Convert ``elem`` into the internal represantition.

        Mostly called implicitly.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> M = QQ.old_poly_ring(x).free_module(2).submodule([1, x])
        >>> M.convert([2, 2*x])
        [2, 2*x]
        """
    def intersect(self, other, **options):
        """
        Returns the intersection of ``self`` with submodule ``other``.

        Examples
        ========

        >>> from sympy.abc import x, y
        >>> from sympy import QQ
        >>> F = QQ.old_poly_ring(x, y).free_module(2)
        >>> F.submodule([x, x]).intersect(F.submodule([y, y]))
        <[x*y, x*y]>

        Some implementation allow further options to be passed. Currently, to
        only one implemented is ``relations=True``, in which case the function
        will return a triple ``(res, rela, relb)``, where ``res`` is the
        intersection module, and ``rela`` and ``relb`` are lists of coefficient
        vectors, expressing the generators of ``res`` in terms of the
        generators of ``self`` (``rela``) and ``other`` (``relb``).

        >>> F.submodule([x, x]).intersect(F.submodule([y, y]), relations=True)
        (<[x*y, x*y]>, [(y,)], [(x,)])

        The above result says: the intersection module is generated by the
        single element `(-xy, -xy) = -y (x, x) = -x (y, y)`, where
        `(x, x)` and `(y, y)` respectively are the unique generators of
        the two modules being intersected.
        """
    def module_quotient(self, other, **options):
        """
        Returns the module quotient of ``self`` by submodule ``other``.

        That is, if ``self`` is the module `M` and ``other`` is `N`, then
        return the ideal `\\{f \\in R | fN \\subset M\\}`.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x, y
        >>> F = QQ.old_poly_ring(x, y).free_module(2)
        >>> S = F.submodule([x*y, x*y])
        >>> T = F.submodule([x, x])
        >>> S.module_quotient(T)
        <y>

        Some implementations allow further options to be passed. Currently, the
        only one implemented is ``relations=True``, which may only be passed
        if ``other`` is principal. In this case the function
        will return a pair ``(res, rel)`` where ``res`` is the ideal, and
        ``rel`` is a list of coefficient vectors, expressing the generators of
        the ideal, multiplied by the generator of ``other`` in terms of
        generators of ``self``.

        >>> S.module_quotient(T, relations=True)
        (<y>, [[1]])

        This means that the quotient ideal is generated by the single element
        `y`, and that `y (x, x) = 1 (xy, xy)`, `(x, x)` and `(xy, xy)` being
        the generators of `T` and `S`, respectively.
        """
    def union(self, other):
        """
        Returns the module generated by the union of ``self`` and ``other``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = QQ.old_poly_ring(x).free_module(1)
        >>> M = F.submodule([x**2 + x]) # <x(x+1)>
        >>> N = F.submodule([x**2 - 1]) # <(x-1)(x+1)>
        >>> M.union(N) == F.submodule([x+1])
        True
        """
    def is_zero(self):
        """
        Return True if ``self`` is a zero module.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> F.submodule([x, 1]).is_zero()
        False
        >>> F.submodule([0, 0]).is_zero()
        True
        """
    def submodule(self, *gens):
        """
        Generate a submodule.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> M = QQ.old_poly_ring(x).free_module(2).submodule([x, 1])
        >>> M.submodule([x**2, x])
        <[x**2, x]>
        """
    def is_full_module(self):
        """
        Return True if ``self`` is the entire free module.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> F.submodule([x, 1]).is_full_module()
        False
        >>> F.submodule([1, 1], [1, 2]).is_full_module()
        True
        """
    def is_submodule(self, other):
        """
        Returns True if ``other`` is a submodule of ``self``.

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> M = F.submodule([2, x])
        >>> N = M.submodule([2*x, x**2])
        >>> M.is_submodule(M)
        True
        >>> M.is_submodule(N)
        True
        >>> N.is_submodule(M)
        False
        """
    def syzygy_module(self, **opts):
        """
        Compute the syzygy module of the generators of ``self``.

        Suppose `M` is generated by `f_1, \\ldots, f_n` over the ring
        `R`. Consider the homomorphism `\\phi: R^n \\to M`, given by
        sending `(r_1, \\ldots, r_n) \\to r_1 f_1 + \\cdots + r_n f_n`.
        The syzygy module is defined to be the kernel of `\\phi`.

        Examples
        ========

        The syzygy module is zero iff the generators generate freely a free
        submodule:

        >>> from sympy.abc import x, y
        >>> from sympy import QQ
        >>> QQ.old_poly_ring(x).free_module(2).submodule([1, 0], [1, 1]).syzygy_module().is_zero()
        True

        A slightly more interesting example:

        >>> M = QQ.old_poly_ring(x, y).free_module(2).submodule([x, 2*x], [y, 2*y])
        >>> S = QQ.old_poly_ring(x, y).free_module(2).submodule([y, -x])
        >>> M.syzygy_module() == S
        True
        """
    def in_terms_of_generators(self, e):
        """
        Express element ``e`` of ``self`` in terms of the generators.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> M = F.submodule([1, 0], [1, 1])
        >>> M.in_terms_of_generators([x, x**2])
        [-x**2 + x, x**2]
        """
    def reduce_element(self, x):
        '''
        Reduce the element ``x`` of our ring modulo the ideal ``self``.

        Here "reduce" has no specific meaning, it could return a unique normal
        form, simplify the expression a bit, or just do nothing.
        '''
    def quotient_module(self, other, **opts):
        """
        Return a quotient module.

        This is the same as taking a submodule of a quotient of the containing
        module.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> S1 = F.submodule([x, 1])
        >>> S2 = F.submodule([x**2, x])
        >>> S1.quotient_module(S2)
        <[x, 1] + <[x**2, x]>>

        Or more coincisely, using the overloaded division operator:

        >>> F.submodule([x, 1]) / [(x**2, x)]
        <[x, 1] + <[x**2, x]>>
        """
    def __add__(self, oth): ...
    __radd__ = __add__
    def multiply_ideal(self, I):
        """
        Multiply ``self`` by the ideal ``I``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> I = QQ.old_poly_ring(x).ideal(x**2)
        >>> M = QQ.old_poly_ring(x).free_module(2).submodule([1, 1])
        >>> I*M
        <[x**2, x**2]>
        """
    def inclusion_hom(self):
        """
        Return a homomorphism representing the inclusion map of ``self``.

        That is, the natural map from ``self`` to ``self.container``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> QQ.old_poly_ring(x).free_module(2).submodule([x, x]).inclusion_hom()
        Matrix([
        [1, 0], : <[x, x]> -> QQ[x]**2
        [0, 1]])
        """
    def identity_hom(self):
        """
        Return the identity homomorphism on ``self``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> QQ.old_poly_ring(x).free_module(2).submodule([x, x]).identity_hom()
        Matrix([
        [1, 0], : <[x, x]> -> <[x, x]>
        [0, 1]])
        """

class SubQuotientModule(SubModule):
    """
    Submodule of a quotient module.

    Equivalently, quotient module of a submodule.

    Do not instantiate this, instead use the submodule or quotient_module
    constructing methods:

    >>> from sympy.abc import x
    >>> from sympy import QQ
    >>> F = QQ.old_poly_ring(x).free_module(2)
    >>> S = F.submodule([1, 0], [1, x])
    >>> Q = F/[(1, 0)]
    >>> S/[(1, 0)] == Q.submodule([5, x])
    True

    Attributes:

    - base - base module we are quotient of
    - killed_module - submodule used to form the quotient
    """
    killed_module: Incomplete
    base: Incomplete
    def __init__(self, gens, container, **opts) -> None: ...
    def is_full_module(self):
        """
        Return True if ``self`` is the entire free module.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> F.submodule([x, 1]).is_full_module()
        False
        >>> F.submodule([1, 1], [1, 2]).is_full_module()
        True
        """
    def quotient_hom(self):
        """
        Return the quotient homomorphism to self.

        That is, return the natural map from ``self.base`` to ``self``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> M = (QQ.old_poly_ring(x).free_module(2) / [(1, x)]).submodule([1, 0])
        >>> M.quotient_hom()
        Matrix([
        [1, 0], : <[1, 0], [1, x]> -> <[1, 0] + <[1, x]>, [1, x] + <[1, x]>>
        [0, 1]])
        """

class ModuleOrder(ProductOrder):
    """A product monomial order with a zeroth term as module index."""
    def __init__(self, o1, o2, TOP) -> None: ...

class SubModulePolyRing(SubModule):
    """
    Submodule of a free module over a generalized polynomial ring.

    Do not instantiate this, use the constructor method of FreeModule instead:

    >>> from sympy.abc import x, y
    >>> from sympy import QQ
    >>> F = QQ.old_poly_ring(x, y).free_module(2)
    >>> F.submodule([x, y], [1, 0])
    <[x, y], [1, 0]>

    Attributes:

    - order - monomial order used
    """
    order: Incomplete
    def __init__(self, gens, container, order: str = 'lex', TOP: bool = True) -> None: ...
    def __eq__(self, other): ...
    def reduce_element(self, x, NF: Incomplete | None = None):
        """
        Reduce the element ``x`` of our container modulo ``self``.

        This applies the normal form ``NF`` to ``x``. If ``NF`` is passed
        as none, the default Mora normal form is used (which is not unique!).
        """

class SubModuleQuotientRing(SubModule):
    """
    Class for submodules of free modules over quotient rings.

    Do not instantiate this. Instead use the submodule methods.

    >>> from sympy.abc import x, y
    >>> from sympy import QQ
    >>> M = (QQ.old_poly_ring(x, y)/[x**2 - y**2]).free_module(2).submodule([x, x + y])
    >>> M
    <[x + <x**2 - y**2>, x + y + <x**2 - y**2>]>
    >>> M.contains([y**2, x**2 + x*y])
    True
    >>> M.contains([x, y])
    False

    Attributes:

    - quot - the subquotient of `R^n/IR^n` generated by lifts of our generators
    """
    quot: Incomplete
    def __init__(self, gens, container) -> None: ...

class QuotientModuleElement(ModuleElement):
    """Element of a quotient module."""
    def eq(self, d1, d2):
        """Equality comparison."""

class QuotientModule(Module):
    """
    Class for quotient modules.

    Do not instantiate this directly. For subquotients, see the
    SubQuotientModule class.

    Attributes:

    - base - the base module we are a quotient of
    - killed_module - the submodule used to form the quotient
    - rank of the base
    """
    dtype = QuotientModuleElement
    base: Incomplete
    killed_module: Incomplete
    rank: Incomplete
    def __init__(self, ring, base, submodule) -> None: ...
    def is_zero(self):
        """
        Return True if ``self`` is a zero module.

        This happens if and only if the base module is the same as the
        submodule being killed.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> (F/[(1, 0)]).is_zero()
        False
        >>> (F/[(1, 0), (0, 1)]).is_zero()
        True
        """
    def is_submodule(self, other):
        """
        Return True if ``other`` is a submodule of ``self``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> Q = QQ.old_poly_ring(x).free_module(2) / [(x, x)]
        >>> S = Q.submodule([1, 0])
        >>> Q.is_submodule(S)
        True
        >>> S.is_submodule(Q)
        False
        """
    def submodule(self, *gens, **opts):
        """
        Generate a submodule.

        This is the same as taking a quotient of a submodule of the base
        module.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> Q = QQ.old_poly_ring(x).free_module(2) / [(x, x)]
        >>> Q.submodule([x, 0])
        <[x, 0] + <[x, x]>>
        """
    def convert(self, elem, M: Incomplete | None = None):
        """
        Convert ``elem`` into the internal representation.

        This method is called implicitly whenever computations involve elements
        not in the internal representation.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> F = QQ.old_poly_ring(x).free_module(2) / [(1, 2), (1, x)]
        >>> F.convert([1, 0])
        [1, 0] + <[1, 2], [1, x]>
        """
    def identity_hom(self):
        """
        Return the identity homomorphism on ``self``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> M = QQ.old_poly_ring(x).free_module(2) / [(1, 2), (1, x)]
        >>> M.identity_hom()
        Matrix([
        [1, 0], : QQ[x]**2/<[1, 2], [1, x]> -> QQ[x]**2/<[1, 2], [1, x]>
        [0, 1]])
        """
    def quotient_hom(self):
        """
        Return the quotient homomorphism to ``self``.

        That is, return a homomorphism representing the natural map from
        ``self.base`` to ``self``.

        Examples
        ========

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> M = QQ.old_poly_ring(x).free_module(2) / [(1, 2), (1, x)]
        >>> M.quotient_hom()
        Matrix([
        [1, 0], : QQ[x]**2 -> QQ[x]**2/<[1, 2], [1, x]>
        [0, 1]])
        """
