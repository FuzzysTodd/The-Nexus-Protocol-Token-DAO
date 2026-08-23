from _typeshed import Incomplete
from sympy.polys.agca.modules import FreeModule as FreeModule, Module as Module, QuotientModule as QuotientModule, SubModule as SubModule, SubQuotientModule as SubQuotientModule
from sympy.polys.polyerrors import CoercionFailed as CoercionFailed

class ModuleHomomorphism:
    """
    Abstract base class for module homomoprhisms. Do not instantiate.

    Instead, use the ``homomorphism`` function:

    >>> from sympy import QQ
    >>> from sympy.abc import x
    >>> from sympy.polys.agca import homomorphism

    >>> F = QQ.old_poly_ring(x).free_module(2)
    >>> homomorphism(F, F, [[1, 0], [0, 1]])
    Matrix([
    [1, 0], : QQ[x]**2 -> QQ[x]**2
    [0, 1]])

    Attributes:

    - ring - the ring over which we are considering modules
    - domain - the domain module
    - codomain - the codomain module
    - _ker - cached kernel
    - _img - cached image

    Non-implemented methods:

    - _kernel
    - _image
    - _restrict_domain
    - _restrict_codomain
    - _quotient_domain
    - _quotient_codomain
    - _apply
    - _mul_scalar
    - _compose
    - _add
    """
    domain: Incomplete
    codomain: Incomplete
    ring: Incomplete
    def __init__(self, domain, codomain) -> None: ...
    def kernel(self):
        """
        Compute the kernel of ``self``.

        That is, if ``self`` is the homomorphism `\\phi: M \\to N`, then compute
        `ker(\\phi) = \\{x \\in M | \\phi(x) = 0\\}`.  This is a submodule of `M`.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> homomorphism(F, F, [[1, 0], [x, 0]]).kernel()
        <[x, -1]>
        """
    def image(self):
        """
        Compute the image of ``self``.

        That is, if ``self`` is the homomorphism `\\phi: M \\to N`, then compute
        `im(\\phi) = \\{\\phi(x) | x \\in M \\}`.  This is a submodule of `N`.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> homomorphism(F, F, [[1, 0], [x, 0]]).image() == F.submodule([1, 0])
        True
        """
    def restrict_domain(self, sm):
        """
        Return ``self``, with the domain restricted to ``sm``.

        Here ``sm`` has to be a submodule of ``self.domain``.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> h = homomorphism(F, F, [[1, 0], [x, 0]])
        >>> h
        Matrix([
        [1, x], : QQ[x]**2 -> QQ[x]**2
        [0, 0]])
        >>> h.restrict_domain(F.submodule([1, 0]))
        Matrix([
        [1, x], : <[1, 0]> -> QQ[x]**2
        [0, 0]])

        This is the same as just composing on the right with the submodule
        inclusion:

        >>> h * F.submodule([1, 0]).inclusion_hom()
        Matrix([
        [1, x], : <[1, 0]> -> QQ[x]**2
        [0, 0]])
        """
    def restrict_codomain(self, sm):
        """
        Return ``self``, with codomain restricted to to ``sm``.

        Here ``sm`` has to be a submodule of ``self.codomain`` containing the
        image.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> h = homomorphism(F, F, [[1, 0], [x, 0]])
        >>> h
        Matrix([
        [1, x], : QQ[x]**2 -> QQ[x]**2
        [0, 0]])
        >>> h.restrict_codomain(F.submodule([1, 0]))
        Matrix([
        [1, x], : QQ[x]**2 -> <[1, 0]>
        [0, 0]])
        """
    def quotient_domain(self, sm):
        """
        Return ``self`` with domain replaced by ``domain/sm``.

        Here ``sm`` must be a submodule of ``self.kernel()``.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> h = homomorphism(F, F, [[1, 0], [x, 0]])
        >>> h
        Matrix([
        [1, x], : QQ[x]**2 -> QQ[x]**2
        [0, 0]])
        >>> h.quotient_domain(F.submodule([-x, 1]))
        Matrix([
        [1, x], : QQ[x]**2/<[-x, 1]> -> QQ[x]**2
        [0, 0]])
        """
    def quotient_codomain(self, sm):
        """
        Return ``self`` with codomain replaced by ``codomain/sm``.

        Here ``sm`` must be a submodule of ``self.codomain``.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> h = homomorphism(F, F, [[1, 0], [x, 0]])
        >>> h
        Matrix([
        [1, x], : QQ[x]**2 -> QQ[x]**2
        [0, 0]])
        >>> h.quotient_codomain(F.submodule([1, 1]))
        Matrix([
        [1, x], : QQ[x]**2 -> QQ[x]**2/<[1, 1]>
        [0, 0]])

        This is the same as composing with the quotient map on the left:

        >>> (F/[(1, 1)]).quotient_hom() * h
        Matrix([
        [1, x], : QQ[x]**2 -> QQ[x]**2/<[1, 1]>
        [0, 0]])
        """
    def __call__(self, elem): ...
    def __mul__(self, oth): ...
    __rmul__ = __mul__
    def __truediv__(self, oth): ...
    def __add__(self, oth): ...
    def __sub__(self, oth): ...
    def is_injective(self):
        """
        Return True if ``self`` is injective.

        That is, check if the elements of the domain are mapped to the same
        codomain element.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> h = homomorphism(F, F, [[1, 0], [x, 0]])
        >>> h.is_injective()
        False
        >>> h.quotient_domain(h.kernel()).is_injective()
        True
        """
    def is_surjective(self):
        """
        Return True if ``self`` is surjective.

        That is, check if every element of the codomain has at least one
        preimage.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> h = homomorphism(F, F, [[1, 0], [x, 0]])
        >>> h.is_surjective()
        False
        >>> h.restrict_codomain(h.image()).is_surjective()
        True
        """
    def is_isomorphism(self):
        """
        Return True if ``self`` is an isomorphism.

        That is, check if every element of the codomain has precisely one
        preimage. Equivalently, ``self`` is both injective and surjective.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> h = homomorphism(F, F, [[1, 0], [x, 0]])
        >>> h = h.restrict_codomain(h.image())
        >>> h.is_isomorphism()
        False
        >>> h.quotient_domain(h.kernel()).is_isomorphism()
        True
        """
    def is_zero(self):
        """
        Return True if ``self`` is a zero morphism.

        That is, check if every element of the domain is mapped to zero
        under self.

        Examples
        ========

        >>> from sympy import QQ
        >>> from sympy.abc import x
        >>> from sympy.polys.agca import homomorphism

        >>> F = QQ.old_poly_ring(x).free_module(2)
        >>> h = homomorphism(F, F, [[1, 0], [x, 0]])
        >>> h.is_zero()
        False
        >>> h.restrict_domain(F.submodule()).is_zero()
        True
        >>> h.quotient_codomain(h.image()).is_zero()
        True
        """
    def __eq__(self, oth): ...
    def __ne__(self, oth): ...

class MatrixHomomorphism(ModuleHomomorphism):
    """
    Helper class for all homomoprhisms which are expressed via a matrix.

    That is, for such homomorphisms ``domain`` is contained in a module
    generated by finitely many elements `e_1, \\ldots, e_n`, so that the
    homomorphism is determined uniquely by its action on the `e_i`. It
    can thus be represented as a vector of elements of the codomain module,
    or potentially a supermodule of the codomain module
    (and hence conventionally as a matrix, if there is a similar interpretation
    for elements of the codomain module).

    Note that this class does *not* assume that the `e_i` freely generate a
    submodule, nor that ``domain`` is even all of this submodule. It exists
    only to unify the interface.

    Do not instantiate.

    Attributes:

    - matrix - the list of images determining the homomorphism.
    NOTE: the elements of matrix belong to either self.codomain or
          self.codomain.container

    Still non-implemented methods:

    - kernel
    - _apply
    """
    matrix: Incomplete
    def __init__(self, domain, codomain, matrix) -> None: ...

class FreeModuleHomomorphism(MatrixHomomorphism):
    """
    Concrete class for homomorphisms with domain a free module or a quotient
    thereof.

    Do not instantiate; the constructor does not check that your data is well
    defined. Use the ``homomorphism`` function instead:

    >>> from sympy import QQ
    >>> from sympy.abc import x
    >>> from sympy.polys.agca import homomorphism

    >>> F = QQ.old_poly_ring(x).free_module(2)
    >>> homomorphism(F, F, [[1, 0], [0, 1]])
    Matrix([
    [1, 0], : QQ[x]**2 -> QQ[x]**2
    [0, 1]])
    """
class SubModuleHomomorphism(MatrixHomomorphism):
    """
    Concrete class for homomorphism with domain a submodule of a free module
    or a quotient thereof.

    Do not instantiate; the constructor does not check that your data is well
    defined. Use the ``homomorphism`` function instead:

    >>> from sympy import QQ
    >>> from sympy.abc import x
    >>> from sympy.polys.agca import homomorphism

    >>> M = QQ.old_poly_ring(x).free_module(2)*x
    >>> homomorphism(M, M, [[1, 0], [0, 1]])
    Matrix([
    [1, 0], : <[x, 0], [0, x]> -> <[x, 0], [0, x]>
    [0, 1]])
    """

def homomorphism(domain, codomain, matrix):
    """
    Create a homomorphism object.

    This function tries to build a homomorphism from ``domain`` to ``codomain``
    via the matrix ``matrix``.

    Examples
    ========

    >>> from sympy import QQ
    >>> from sympy.abc import x
    >>> from sympy.polys.agca import homomorphism

    >>> R = QQ.old_poly_ring(x)
    >>> T = R.free_module(2)

    If ``domain`` is a free module generated by `e_1, \\ldots, e_n`, then
    ``matrix`` should be an n-element iterable `(b_1, \\ldots, b_n)` where
    the `b_i` are elements of ``codomain``. The constructed homomorphism is the
    unique homomorphism sending `e_i` to `b_i`.

    >>> F = R.free_module(2)
    >>> h = homomorphism(F, T, [[1, x], [x**2, 0]])
    >>> h
    Matrix([
    [1, x**2], : QQ[x]**2 -> QQ[x]**2
    [x,    0]])
    >>> h([1, 0])
    [1, x]
    >>> h([0, 1])
    [x**2, 0]
    >>> h([1, 1])
    [x**2 + 1, x]

    If ``domain`` is a submodule of a free module, them ``matrix`` determines
    a homomoprhism from the containing free module to ``codomain``, and the
    homomorphism returned is obtained by restriction to ``domain``.

    >>> S = F.submodule([1, 0], [0, x])
    >>> homomorphism(S, T, [[1, x], [x**2, 0]])
    Matrix([
    [1, x**2], : <[1, 0], [0, x]> -> QQ[x]**2
    [x,    0]])

    If ``domain`` is a (sub)quotient `N/K`, then ``matrix`` determines a
    homomorphism from `N` to ``codomain``. If the kernel contains `K`, this
    homomorphism descends to ``domain`` and is returned; otherwise an exception
    is raised.

    >>> homomorphism(S/[(1, 0)], T, [0, [x**2, 0]])
    Matrix([
    [0, x**2], : <[1, 0] + <[1, 0]>, [0, x] + <[1, 0]>, [1, 0] + <[1, 0]>> -> QQ[x]**2
    [0,    0]])
    >>> homomorphism(S/[(0, x)], T, [0, [x**2, 0]])
    Traceback (most recent call last):
    ...
    ValueError: kernel <[1, 0], [0, 0]> must contain sm, got <[0,x]>

    """
