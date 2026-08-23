from _typeshed import Incomplete
from sympy.core.evalf import EvalfMixin
from sympy.printing.defaults import Printable

__all__ = ['Vector']

class Vector(Printable, EvalfMixin):
    """The class used to define vectors.

    It along with ReferenceFrame are the building blocks of describing a
    classical mechanics system in PyDy and sympy.physics.vector.

    Attributes
    ==========

    simp : Boolean
        Let certain methods use trigsimp on their outputs

    """
    simp: bool
    is_number: bool
    args: Incomplete
    def __init__(self, inlist) -> None:
        """This is the constructor for the Vector class.  You should not be
        calling this, it should only be used by other functions. You should be
        treating Vectors like you would with if you were doing the math by
        hand, and getting the first 3 from the standard basis vectors from a
        ReferenceFrame.

        The only exception is to create a zero vector:
        zv = Vector(0)

        """
    @property
    def func(self):
        """Returns the class Vector. """
    def __hash__(self): ...
    def __add__(self, other):
        """The add operator for Vector. """
    def __and__(self, other):
        """Dot product of two vectors.

        Returns a scalar, the dot product of the two Vectors

        Parameters
        ==========

        other : Vector
            The Vector which we are dotting with

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame, dot
        >>> from sympy import symbols
        >>> q1 = symbols('q1')
        >>> N = ReferenceFrame('N')
        >>> dot(N.x, N.x)
        1
        >>> dot(N.x, N.y)
        0
        >>> A = N.orientnew('A', 'Axis', [q1, N.x])
        >>> dot(N.y, A.y)
        cos(q1)

        """
    def __truediv__(self, other):
        """This uses mul and inputs self and 1 divided by other. """
    def __eq__(self, other):
        """Tests for equality.

        It is very import to note that this is only as good as the SymPy
        equality test; False does not always mean they are not equivalent
        Vectors.
        If other is 0, and self is empty, returns True.
        If other is 0 and self is not empty, returns False.
        If none of the above, only accepts other as a Vector.

        """
    def __mul__(self, other):
        """Multiplies the Vector by a sympifyable expression.

        Parameters
        ==========

        other : Sympifyable
            The scalar to multiply this Vector with

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame
        >>> from sympy import Symbol
        >>> N = ReferenceFrame('N')
        >>> b = Symbol('b')
        >>> V = 10 * b * N.x
        >>> print(V)
        10*b*N.x

        """
    def __neg__(self): ...
    def __or__(self, other):
        """Outer product between two Vectors.

        A rank increasing operation, which returns a Dyadic from two Vectors

        Parameters
        ==========

        other : Vector
            The Vector to take the outer product with

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame, outer
        >>> N = ReferenceFrame('N')
        >>> outer(N.x, N.x)
        (N.x|N.x)

        """
    def __ror__(self, other):
        """Outer product between two Vectors.

        A rank increasing operation, which returns a Dyadic from two Vectors

        Parameters
        ==========

        other : Vector
            The Vector to take the outer product with

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame, outer
        >>> N = ReferenceFrame('N')
        >>> outer(N.x, N.x)
        (N.x|N.x)

        """
    def __rsub__(self, other): ...
    def __sub__(self, other):
        """The subtraction operator. """
    def __xor__(self, other):
        """The cross product operator for two Vectors.

        Returns a Vector, expressed in the same ReferenceFrames as self.

        Parameters
        ==========

        other : Vector
            The Vector which we are crossing with

        Examples
        ========

        >>> from sympy import symbols
        >>> from sympy.physics.vector import ReferenceFrame, cross
        >>> q1 = symbols('q1')
        >>> N = ReferenceFrame('N')
        >>> cross(N.x, N.y)
        N.z
        >>> A = ReferenceFrame('A')
        >>> A.orient_axis(N, q1, N.x)
        >>> cross(A.x, N.y)
        N.z
        >>> cross(N.y, A.x)
        - sin(q1)*A.y - cos(q1)*A.z

        """
    __radd__ = __add__
    __rand__ = __and__
    __rmul__ = __mul__
    def separate(self):
        """
        The constituents of this vector in different reference frames,
        as per its definition.

        Returns a dict mapping each ReferenceFrame to the corresponding
        constituent Vector.

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame
        >>> R1 = ReferenceFrame('R1')
        >>> R2 = ReferenceFrame('R2')
        >>> v = R1.x + R2.x
        >>> v.separate() == {R1: R1.x, R2: R2.x}
        True

        """
    def dot(self, other): ...
    def cross(self, other): ...
    def outer(self, other): ...
    def diff(self, var, frame, var_in_dcm: bool = True):
        """Returns the partial derivative of the vector with respect to a
        variable in the provided reference frame.

        Parameters
        ==========
        var : Symbol
            What the partial derivative is taken with respect to.
        frame : ReferenceFrame
            The reference frame that the partial derivative is taken in.
        var_in_dcm : boolean
            If true, the differentiation algorithm assumes that the variable
            may be present in any of the direction cosine matrices that relate
            the frame to the frames of any component of the vector. But if it
            is known that the variable is not present in the direction cosine
            matrices, false can be set to skip full reexpression in the desired
            frame.

        Examples
        ========

        >>> from sympy import Symbol
        >>> from sympy.physics.vector import dynamicsymbols, ReferenceFrame
        >>> from sympy.physics.vector import Vector
        >>> from sympy.physics.vector import init_vprinting
        >>> init_vprinting(pretty_print=False)
        >>> Vector.simp = True
        >>> t = Symbol('t')
        >>> q1 = dynamicsymbols('q1')
        >>> N = ReferenceFrame('N')
        >>> A = N.orientnew('A', 'Axis', [q1, N.y])
        >>> A.x.diff(t, N)
        - sin(q1)*q1'*N.x - cos(q1)*q1'*N.z
        >>> A.x.diff(t, N).express(A)
        - q1'*A.z
        >>> B = ReferenceFrame('B')
        >>> u1, u2 = dynamicsymbols('u1, u2')
        >>> v = u1 * A.x + u2 * B.y
        >>> v.diff(u2, N, var_in_dcm=False)
        B.y

        """
    def express(self, otherframe, variables: bool = False):
        """
        Returns a Vector equivalent to this one, expressed in otherframe.
        Uses the global express method.

        Parameters
        ==========

        otherframe : ReferenceFrame
            The frame for this Vector to be described in

        variables : boolean
            If True, the coordinate symbols(if present) in this Vector
            are re-expressed in terms otherframe

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame, dynamicsymbols
        >>> from sympy.physics.vector import init_vprinting
        >>> init_vprinting(pretty_print=False)
        >>> q1 = dynamicsymbols('q1')
        >>> N = ReferenceFrame('N')
        >>> A = N.orientnew('A', 'Axis', [q1, N.y])
        >>> A.x.express(N)
        cos(q1)*N.x - sin(q1)*N.z

        """
    def to_matrix(self, reference_frame):
        """Returns the matrix form of the vector with respect to the given
        frame.

        Parameters
        ----------
        reference_frame : ReferenceFrame
            The reference frame that the rows of the matrix correspond to.

        Returns
        -------
        matrix : ImmutableMatrix, shape(3,1)
            The matrix that gives the 1D vector.

        Examples
        ========

        >>> from sympy import symbols
        >>> from sympy.physics.vector import ReferenceFrame
        >>> a, b, c = symbols('a, b, c')
        >>> N = ReferenceFrame('N')
        >>> vector = a * N.x + b * N.y + c * N.z
        >>> vector.to_matrix(N)
        Matrix([
        [a],
        [b],
        [c]])
        >>> beta = symbols('beta')
        >>> A = N.orientnew('A', 'Axis', (beta, N.x))
        >>> vector.to_matrix(A)
        Matrix([
        [                         a],
        [ b*cos(beta) + c*sin(beta)],
        [-b*sin(beta) + c*cos(beta)]])

        """
    def doit(self, **hints):
        """Calls .doit() on each term in the Vector"""
    def dt(self, otherframe):
        """
        Returns a Vector which is the time derivative of
        the self Vector, taken in frame otherframe.

        Calls the global time_derivative method

        Parameters
        ==========

        otherframe : ReferenceFrame
            The frame to calculate the time derivative in

        """
    def simplify(self):
        """Returns a simplified Vector."""
    def subs(self, *args, **kwargs):
        """Substitution on the Vector.

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame
        >>> from sympy import Symbol
        >>> N = ReferenceFrame('N')
        >>> s = Symbol('s')
        >>> a = N.x * s
        >>> a.subs({s: 2})
        2*N.x

        """
    def magnitude(self):
        """Returns the magnitude (Euclidean norm) of self.

        Warnings
        ========

        Python ignores the leading negative sign so that might
        give wrong results.
        ``-A.x.magnitude()`` would be treated as ``-(A.x.magnitude())``,
        instead of ``(-A.x).magnitude()``.

        """
    def normalize(self):
        """Returns a Vector of magnitude 1, codirectional with self."""
    def applyfunc(self, f):
        """Apply a function to each component of a vector."""
    def angle_between(self, vec):
        '''
        Returns the smallest angle between Vector \'vec\' and self.

        Parameter
        =========

        vec : Vector
            The Vector between which angle is needed.

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame
        >>> A = ReferenceFrame("A")
        >>> v1 = A.x
        >>> v2 = A.y
        >>> v1.angle_between(v2)
        pi/2

        >>> v3 = A.x + A.y + A.z
        >>> v1.angle_between(v3)
        acos(sqrt(3)/3)

        Warnings
        ========

        Python ignores the leading negative sign so that might give wrong
        results. ``-A.x.angle_between()`` would be treated as
        ``-(A.x.angle_between())``, instead of ``(-A.x).angle_between()``.

        '''
    def free_symbols(self, reference_frame):
        """Returns the free symbols in the measure numbers of the vector
        expressed in the given reference frame.

        Parameters
        ==========
        reference_frame : ReferenceFrame
            The frame with respect to which the free symbols of the given
            vector is to be determined.

        Returns
        =======
        set of Symbol
            set of symbols present in the measure numbers of
            ``reference_frame``.

        """
    def free_dynamicsymbols(self, reference_frame):
        """Returns the free dynamic symbols (functions of time ``t``) in the
        measure numbers of the vector expressed in the given reference frame.

        Parameters
        ==========
        reference_frame : ReferenceFrame
            The frame with respect to which the free dynamic symbols of the
            given vector is to be determined.

        Returns
        =======
        set
            Set of functions of time ``t``, e.g.
            ``Function('f')(me.dynamicsymbols._t)``.

        """
    def xreplace(self, rule):
        """Replace occurrences of objects within the measure numbers of the
        vector.

        Parameters
        ==========

        rule : dict-like
            Expresses a replacement rule.

        Returns
        =======

        Vector
            Result of the replacement.

        Examples
        ========

        >>> from sympy import symbols, pi
        >>> from sympy.physics.vector import ReferenceFrame
        >>> A = ReferenceFrame('A')
        >>> x, y, z = symbols('x y z')
        >>> ((1 + x*y) * A.x).xreplace({x: pi})
        (pi*y + 1)*A.x
        >>> ((1 + x*y) * A.x).xreplace({x: pi, y: 2})
        (1 + 2*pi)*A.x

        Replacements occur only if an entire node in the expression tree is
        matched:

        >>> ((x*y + z) * A.x).xreplace({x*y: pi})
        (z + pi)*A.x
        >>> ((x*y*z) * A.x).xreplace({x*y: pi})
        x*y*z*A.x

        """

class VectorTypeError(TypeError):
    def __init__(self, other, want) -> None: ...
