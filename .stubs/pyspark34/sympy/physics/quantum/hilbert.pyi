from _typeshed import Incomplete
from sympy.core.basic import Basic
from sympy.physics.quantum.qexpr import QuantumError

__all__ = ['HilbertSpaceError', 'HilbertSpace', 'TensorProductHilbertSpace', 'TensorPowerHilbertSpace', 'DirectSumHilbertSpace', 'ComplexSpace', 'L2', 'FockSpace']

class HilbertSpaceError(QuantumError): ...

class HilbertSpace(Basic):
    """An abstract Hilbert space for quantum mechanics.

    In short, a Hilbert space is an abstract vector space that is complete
    with inner products defined [1]_.

    Examples
    ========

    >>> from sympy.physics.quantum.hilbert import HilbertSpace
    >>> hs = HilbertSpace()
    >>> hs
    H

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Hilbert_space
    """
    def __new__(cls): ...
    @property
    def dimension(self) -> None:
        """Return the Hilbert dimension of the space."""
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __pow__(self, other, mod: Incomplete | None = None): ...
    def __contains__(self, other) -> bool:
        """Is the operator or state in this Hilbert space.

        This is checked by comparing the classes of the Hilbert spaces, not
        the instances. This is to allow Hilbert Spaces with symbolic
        dimensions.
        """

class ComplexSpace(HilbertSpace):
    """Finite dimensional Hilbert space of complex vectors.

    The elements of this Hilbert space are n-dimensional complex valued
    vectors with the usual inner product that takes the complex conjugate
    of the vector on the right.

    A classic example of this type of Hilbert space is spin-1/2, which is
    ``ComplexSpace(2)``. Generalizing to spin-s, the space is
    ``ComplexSpace(2*s+1)``.  Quantum computing with N qubits is done with the
    direct product space ``ComplexSpace(2)**N``.

    Examples
    ========

    >>> from sympy import symbols
    >>> from sympy.physics.quantum.hilbert import ComplexSpace
    >>> c1 = ComplexSpace(2)
    >>> c1
    C(2)
    >>> c1.dimension
    2

    >>> n = symbols('n')
    >>> c2 = ComplexSpace(n)
    >>> c2
    C(n)
    >>> c2.dimension
    n

    """
    def __new__(cls, dimension): ...
    @classmethod
    def eval(cls, dimension) -> None: ...
    @property
    def dimension(self): ...

class L2(HilbertSpace):
    """The Hilbert space of square integrable functions on an interval.

    An L2 object takes in a single SymPy Interval argument which represents
    the interval its functions (vectors) are defined on.

    Examples
    ========

    >>> from sympy import Interval, oo
    >>> from sympy.physics.quantum.hilbert import L2
    >>> hs = L2(Interval(0,oo))
    >>> hs
    L2(Interval(0, oo))
    >>> hs.dimension
    oo
    >>> hs.interval
    Interval(0, oo)

    """
    def __new__(cls, interval): ...
    @property
    def dimension(self): ...
    @property
    def interval(self): ...

class FockSpace(HilbertSpace):
    """The Hilbert space for second quantization.

    Technically, this Hilbert space is a infinite direct sum of direct
    products of single particle Hilbert spaces [1]_. This is a mess, so we have
    a class to represent it directly.

    Examples
    ========

    >>> from sympy.physics.quantum.hilbert import FockSpace
    >>> hs = FockSpace()
    >>> hs
    F
    >>> hs.dimension
    oo

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Fock_space
    """
    def __new__(cls): ...
    @property
    def dimension(self): ...

class TensorProductHilbertSpace(HilbertSpace):
    """A tensor product of Hilbert spaces [1]_.

    The tensor product between Hilbert spaces is represented by the
    operator ``*`` Products of the same Hilbert space will be combined into
    tensor powers.

    A ``TensorProductHilbertSpace`` object takes in an arbitrary number of
    ``HilbertSpace`` objects as its arguments. In addition, multiplication of
    ``HilbertSpace`` objects will automatically return this tensor product
    object.

    Examples
    ========

    >>> from sympy.physics.quantum.hilbert import ComplexSpace, FockSpace
    >>> from sympy import symbols

    >>> c = ComplexSpace(2)
    >>> f = FockSpace()
    >>> hs = c*f
    >>> hs
    C(2)*F
    >>> hs.dimension
    oo
    >>> hs.spaces
    (C(2), F)

    >>> c1 = ComplexSpace(2)
    >>> n = symbols('n')
    >>> c2 = ComplexSpace(n)
    >>> hs = c1*c2
    >>> hs
    C(2)*C(n)
    >>> hs.dimension
    2*n

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Hilbert_space#Tensor_products
    """
    def __new__(cls, *args): ...
    @classmethod
    def eval(cls, args):
        """Evaluates the direct product."""
    @property
    def dimension(self): ...
    @property
    def spaces(self):
        """A tuple of the Hilbert spaces in this tensor product."""

class DirectSumHilbertSpace(HilbertSpace):
    """A direct sum of Hilbert spaces [1]_.

    This class uses the ``+`` operator to represent direct sums between
    different Hilbert spaces.

    A ``DirectSumHilbertSpace`` object takes in an arbitrary number of
    ``HilbertSpace`` objects as its arguments. Also, addition of
    ``HilbertSpace`` objects will automatically return a direct sum object.

    Examples
    ========

    >>> from sympy.physics.quantum.hilbert import ComplexSpace, FockSpace

    >>> c = ComplexSpace(2)
    >>> f = FockSpace()
    >>> hs = c+f
    >>> hs
    C(2)+F
    >>> hs.dimension
    oo
    >>> list(hs.spaces)
    [C(2), F]

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Hilbert_space#Direct_sums
    """
    def __new__(cls, *args): ...
    @classmethod
    def eval(cls, args):
        """Evaluates the direct product."""
    @property
    def dimension(self): ...
    @property
    def spaces(self):
        """A tuple of the Hilbert spaces in this direct sum."""

class TensorPowerHilbertSpace(HilbertSpace):
    """An exponentiated Hilbert space [1]_.

    Tensor powers (repeated tensor products) are represented by the
    operator ``**`` Identical Hilbert spaces that are multiplied together
    will be automatically combined into a single tensor power object.

    Any Hilbert space, product, or sum may be raised to a tensor power. The
    ``TensorPowerHilbertSpace`` takes two arguments: the Hilbert space; and the
    tensor power (number).

    Examples
    ========

    >>> from sympy.physics.quantum.hilbert import ComplexSpace, FockSpace
    >>> from sympy import symbols

    >>> n = symbols('n')
    >>> c = ComplexSpace(2)
    >>> hs = c**n
    >>> hs
    C(2)**n
    >>> hs.dimension
    2**n

    >>> c = ComplexSpace(2)
    >>> c*c
    C(2)**2
    >>> f = FockSpace()
    >>> c*f*f
    C(2)*F**2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Hilbert_space#Tensor_products
    """
    def __new__(cls, *args): ...
    @classmethod
    def eval(cls, args): ...
    @property
    def base(self): ...
    @property
    def exp(self): ...
    @property
    def dimension(self): ...
