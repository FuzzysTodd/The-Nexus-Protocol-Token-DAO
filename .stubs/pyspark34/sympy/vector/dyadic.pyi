from _typeshed import Incomplete
from sympy.core import Pow as Pow, S as S
from sympy.core.expr import AtomicExpr as AtomicExpr
from sympy.vector.basisdependent import BasisDependent as BasisDependent, BasisDependentAdd as BasisDependentAdd, BasisDependentMul as BasisDependentMul, BasisDependentZero as BasisDependentZero

class Dyadic(BasisDependent):
    """
    Super class for all Dyadic-classes.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Dyadic_tensor
    .. [2] Kane, T., Levinson, D. Dynamics Theory and Applications. 1985
           McGraw-Hill

    """
    zero: DyadicZero
    @property
    def components(self):
        """
        Returns the components of this dyadic in the form of a
        Python dictionary mapping BaseDyadic instances to the
        corresponding measure numbers.

        """
    def dot(self, other):
        """
        Returns the dot product(also called inner product) of this
        Dyadic, with another Dyadic or Vector.
        If 'other' is a Dyadic, this returns a Dyadic. Else, it returns
        a Vector (unless an error is encountered).

        Parameters
        ==========

        other : Dyadic/Vector
            The other Dyadic or Vector to take the inner product with

        Examples
        ========

        >>> from sympy.vector import CoordSys3D
        >>> N = CoordSys3D('N')
        >>> D1 = N.i.outer(N.j)
        >>> D2 = N.j.outer(N.j)
        >>> D1.dot(D2)
        (N.i|N.j)
        >>> D1.dot(N.j)
        N.i

        """
    def __and__(self, other): ...
    def cross(self, other):
        """
        Returns the cross product between this Dyadic, and a Vector, as a
        Vector instance.

        Parameters
        ==========

        other : Vector
            The Vector that we are crossing this Dyadic with

        Examples
        ========

        >>> from sympy.vector import CoordSys3D
        >>> N = CoordSys3D('N')
        >>> d = N.i.outer(N.i)
        >>> d.cross(N.j)
        (N.i|N.k)

        """
    def __xor__(self, other): ...
    def to_matrix(self, system, second_system: Incomplete | None = None):
        """
        Returns the matrix form of the dyadic with respect to one or two
        coordinate systems.

        Parameters
        ==========

        system : CoordSys3D
            The coordinate system that the rows and columns of the matrix
            correspond to. If a second system is provided, this
            only corresponds to the rows of the matrix.
        second_system : CoordSys3D, optional, default=None
            The coordinate system that the columns of the matrix correspond
            to.

        Examples
        ========

        >>> from sympy.vector import CoordSys3D
        >>> N = CoordSys3D('N')
        >>> v = N.i + 2*N.j
        >>> d = v.outer(N.i)
        >>> d.to_matrix(N)
        Matrix([
        [1, 0, 0],
        [2, 0, 0],
        [0, 0, 0]])
        >>> from sympy import Symbol
        >>> q = Symbol('q')
        >>> P = N.orient_new_axis('P', q, N.k)
        >>> d.to_matrix(N, P)
        Matrix([
        [  cos(q),   -sin(q), 0],
        [2*cos(q), -2*sin(q), 0],
        [       0,         0, 0]])

        """

class BaseDyadic(Dyadic, AtomicExpr):
    """
    Class to denote a base dyadic tensor component.
    """
    def __new__(cls, vector1, vector2): ...

class DyadicMul(BasisDependentMul, Dyadic):
    """ Products of scalars and BaseDyadics """
    def __new__(cls, *args, **options): ...
    @property
    def base_dyadic(self):
        """ The BaseDyadic involved in the product. """
    @property
    def measure_number(self):
        """ The scalar expression involved in the definition of
        this DyadicMul.
        """

class DyadicAdd(BasisDependentAdd, Dyadic):
    """ Class to hold dyadic sums """
    def __new__(cls, *args, **options): ...

class DyadicZero(BasisDependentZero, Dyadic):
    """
    Class to denote a zero dyadic
    """
    def __new__(cls): ...
