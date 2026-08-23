from _typeshed import Incomplete
from sympy.core.expr import Expr as Expr
from sympy.core.logic import fuzzy_not as fuzzy_not, fuzzy_or as fuzzy_or
from sympy.core.numbers import Rational as Rational
from sympy.core.relational import is_eq as is_eq
from sympy.core.singleton import S as S
from sympy.core.sympify import sympify as sympify
from sympy.functions.elementary.complexes import conjugate as conjugate, im as im, re as re, sign as sign
from sympy.functions.elementary.exponential import exp as exp
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.elementary.trigonometric import acos as acos, asin as asin, atan2 as atan2, cos as cos, sin as sin
from sympy.integrals.integrals import integrate as integrate
from sympy.simplify.trigsimp import trigsimp as trigsimp

class Quaternion(Expr):
    """Provides basic quaternion operations.
    Quaternion objects can be instantiated as Quaternion(a, b, c, d)
    as in (a + b*i + c*j + d*k).

    Parameters
    ==========

    norm : None or number
        Pre-defined quaternion norm. If a value is given, Quaternion.norm
        returns this pre-defined value instead of calculating the norm

    Examples
    ========

    >>> from sympy import Quaternion
    >>> q = Quaternion(1, 2, 3, 4)
    >>> q
    1 + 2*i + 3*j + 4*k

    Quaternions over complex fields can be defined as :

    >>> from sympy import Quaternion
    >>> from sympy import symbols, I
    >>> x = symbols('x')
    >>> q1 = Quaternion(x, x**3, x, x**2, real_field = False)
    >>> q2 = Quaternion(3 + 4*I, 2 + 5*I, 0, 7 + 8*I, real_field = False)
    >>> q1
    x + x**3*i + x*j + x**2*k
    >>> q2
    (3 + 4*I) + (2 + 5*I)*i + 0*j + (7 + 8*I)*k

    Defining symbolic unit quaternions:
    >>> from sympy import Quaternion
    >>> from sympy.abc import w, x, y, z
    >>> q = Quaternion(w, x, y, z, norm=1)
    >>> q
    w + x*i + y*j + z*k
    >>> q.norm()
    1

    References
    ==========

    .. [1] https://www.euclideanspace.com/maths/algebra/realNormedAlgebra/quaternions/
    .. [2] https://en.wikipedia.org/wiki/Quaternion

    """
    is_commutative: bool
    def __new__(cls, a: int = 0, b: int = 0, c: int = 0, d: int = 0, real_field: bool = True, norm: Incomplete | None = None): ...
    def set_norm(self, norm) -> None:
        """Sets norm of an already instantiated quaternion.

        Parameters
        ==========

        norm : None or number
            Pre-defined quaternion norm. If a value is given, Quaternion.norm
            returns this pre-defined value instead of calculating the norm

        Examples
        ========

        >>> from sympy import Quaternion
        >>> from sympy.abc import a, b, c, d
        >>> q = Quaternion(a, b, c, d)
        >>> q.norm()
        sqrt(a**2 + b**2 + c**2 + d**2)

        Setting the norm:

        >>> q.set_norm(1)
        >>> q.norm()
        1

        Removing set norm:

        >>> q.set_norm(None)
        >>> q.norm()
        sqrt(a**2 + b**2 + c**2 + d**2)

        """
    @property
    def a(self): ...
    @property
    def b(self): ...
    @property
    def c(self): ...
    @property
    def d(self): ...
    @property
    def real_field(self): ...
    @property
    def product_matrix_left(self):
        """Returns 4 x 4 Matrix equivalent to a Hamilton product from the
        left. This can be useful when treating quaternion elements as column
        vectors. Given a quaternion $q = a + bi + cj + dk$ where a, b, c and d
        are real numbers, the product matrix from the left is:

        .. math::

            M  =  \\begin{bmatrix} a  &-b  &-c  &-d \\\\\n                                  b  & a  &-d  & c \\\\\n                                  c  & d  & a  &-b \\\\\n                                  d  &-c  & b  & a \\end{bmatrix}

        Examples
        ========

        >>> from sympy import Quaternion
        >>> from sympy.abc import a, b, c, d
        >>> q1 = Quaternion(1, 0, 0, 1)
        >>> q2 = Quaternion(a, b, c, d)
        >>> q1.product_matrix_left
        Matrix([
        [1, 0,  0, -1],
        [0, 1, -1,  0],
        [0, 1,  1,  0],
        [1, 0,  0,  1]])

        >>> q1.product_matrix_left * q2.to_Matrix()
        Matrix([
        [a - d],
        [b - c],
        [b + c],
        [a + d]])

        This is equivalent to:

        >>> (q1 * q2).to_Matrix()
        Matrix([
        [a - d],
        [b - c],
        [b + c],
        [a + d]])
        """
    @property
    def product_matrix_right(self):
        """Returns 4 x 4 Matrix equivalent to a Hamilton product from the
        right. This can be useful when treating quaternion elements as column
        vectors. Given a quaternion $q = a + bi + cj + dk$ where a, b, c and d
        are real numbers, the product matrix from the left is:

        .. math::

            M  =  \\begin{bmatrix} a  &-b  &-c  &-d \\\\\n                                  b  & a  & d  &-c \\\\\n                                  c  &-d  & a  & b \\\\\n                                  d  & c  &-b  & a \\end{bmatrix}


        Examples
        ========

        >>> from sympy import Quaternion
        >>> from sympy.abc import a, b, c, d
        >>> q1 = Quaternion(a, b, c, d)
        >>> q2 = Quaternion(1, 0, 0, 1)
        >>> q2.product_matrix_right
        Matrix([
        [1, 0, 0, -1],
        [0, 1, 1, 0],
        [0, -1, 1, 0],
        [1, 0, 0, 1]])

        Note the switched arguments: the matrix represents the quaternion on
        the right, but is still considered as a matrix multiplication from the
        left.

        >>> q2.product_matrix_right * q1.to_Matrix()
        Matrix([
        [ a - d],
        [ b + c],
        [-b + c],
        [ a + d]])

        This is equivalent to:

        >>> (q1 * q2).to_Matrix()
        Matrix([
        [ a - d],
        [ b + c],
        [-b + c],
        [ a + d]])
        """
    def to_Matrix(self, vector_only: bool = False):
        """Returns elements of quaternion as a column vector.
        By default, a Matrix of length 4 is returned, with the real part as the
        first element.
        If vector_only is True, returns only imaginary part as a Matrix of
        length 3.

        Parameters
        ==========

        vector_only : bool
            If True, only imaginary part is returned.
            Default value: False

        Returns
        =======

        Matrix
            A column vector constructed by the elements of the quaternion.

        Examples
        ========

        >>> from sympy import Quaternion
        >>> from sympy.abc import a, b, c, d
        >>> q = Quaternion(a, b, c, d)
        >>> q
        a + b*i + c*j + d*k

        >>> q.to_Matrix()
        Matrix([
        [a],
        [b],
        [c],
        [d]])


        >>> q.to_Matrix(vector_only=True)
        Matrix([
        [b],
        [c],
        [d]])

        """
    @classmethod
    def from_Matrix(cls, elements):
        """Returns quaternion from elements of a column vector`.
        If vector_only is True, returns only imaginary part as a Matrix of
        length 3.

        Parameters
        ==========

        elements : Matrix, list or tuple of length 3 or 4. If length is 3,
            assume real part is zero.
            Default value: False

        Returns
        =======

        Quaternion
            A quaternion created from the input elements.

        Examples
        ========

        >>> from sympy import Quaternion
        >>> from sympy.abc import a, b, c, d
        >>> q = Quaternion.from_Matrix([a, b, c, d])
        >>> q
        a + b*i + c*j + d*k

        >>> q = Quaternion.from_Matrix([b, c, d])
        >>> q
        0 + b*i + c*j + d*k

        """
    @classmethod
    def from_euler(cls, angles, seq):
        """Returns quaternion equivalent to rotation represented by the Euler
        angles, in the sequence defined by ``seq``.

        Parameters
        ==========

        angles : list, tuple or Matrix of 3 numbers
            The Euler angles (in radians).
        seq : string of length 3
            Represents the sequence of rotations.
            For intrinsic rotations, seq must be all lowercase and its elements
            must be from the set ``{'x', 'y', 'z'}``
            For extrinsic rotations, seq must be all uppercase and its elements
            must be from the set ``{'X', 'Y', 'Z'}``

        Returns
        =======

        Quaternion
            The normalized rotation quaternion calculated from the Euler angles
            in the given sequence.

        Examples
        ========

        >>> from sympy import Quaternion
        >>> from sympy import pi
        >>> q = Quaternion.from_euler([pi/2, 0, 0], 'xyz')
        >>> q
        sqrt(2)/2 + sqrt(2)/2*i + 0*j + 0*k

        >>> q = Quaternion.from_euler([0, pi/2, pi] , 'zyz')
        >>> q
        0 + (-sqrt(2)/2)*i + 0*j + sqrt(2)/2*k

        >>> q = Quaternion.from_euler([0, pi/2, pi] , 'ZYZ')
        >>> q
        0 + sqrt(2)/2*i + 0*j + sqrt(2)/2*k

        """
    def to_euler(self, seq, angle_addition: bool = True, avoid_square_root: bool = False):
        """Returns Euler angles representing same rotation as the quaternion,
        in the sequence given by ``seq``. This implements the method described
        in [1]_.

        For degenerate cases (gymbal lock cases), the third angle is
        set to zero.

        Parameters
        ==========

        seq : string of length 3
            Represents the sequence of rotations.
            For intrinsic rotations, seq must be all lowercase and its elements
            must be from the set ``{'x', 'y', 'z'}``
            For extrinsic rotations, seq must be all uppercase and its elements
            must be from the set ``{'X', 'Y', 'Z'}``

        angle_addition : bool
            When True, first and third angles are given as an addition and
            subtraction of two simpler ``atan2`` expressions. When False, the
            first and third angles are each given by a single more complicated
            ``atan2`` expression. This equivalent expression is given by:

            .. math::

                \\operatorname{atan_2} (b,a) \\pm \\operatorname{atan_2} (d,c) =
                \\operatorname{atan_2} (bc\\pm ad, ac\\mp bd)

            Default value: True

        avoid_square_root : bool
            When True, the second angle is calculated with an expression based
            on ``acos``, which is slightly more complicated but avoids a square
            root. When False, second angle is calculated with ``atan2``, which
            is simpler and can be better for numerical reasons (some
            numerical implementations of ``acos`` have problems near zero).
            Default value: False


        Returns
        =======

        Tuple
            The Euler angles calculated from the quaternion

        Examples
        ========

        >>> from sympy import Quaternion
        >>> from sympy.abc import a, b, c, d
        >>> euler = Quaternion(a, b, c, d).to_euler('zyz')
        >>> euler
        (-atan2(-b, c) + atan2(d, a),
         2*atan2(sqrt(b**2 + c**2), sqrt(a**2 + d**2)),
         atan2(-b, c) + atan2(d, a))


        References
        ==========

        .. [1] https://doi.org/10.1371/journal.pone.0276302

        """
    @classmethod
    def from_axis_angle(cls, vector, angle):
        """Returns a rotation quaternion given the axis and the angle of rotation.

        Parameters
        ==========

        vector : tuple of three numbers
            The vector representation of the given axis.
        angle : number
            The angle by which axis is rotated (in radians).

        Returns
        =======

        Quaternion
            The normalized rotation quaternion calculated from the given axis and the angle of rotation.

        Examples
        ========

        >>> from sympy import Quaternion
        >>> from sympy import pi, sqrt
        >>> q = Quaternion.from_axis_angle((sqrt(3)/3, sqrt(3)/3, sqrt(3)/3), 2*pi/3)
        >>> q
        1/2 + 1/2*i + 1/2*j + 1/2*k

        """
    @classmethod
    def from_rotation_matrix(cls, M):
        """Returns the equivalent quaternion of a matrix. The quaternion will be normalized
        only if the matrix is special orthogonal (orthogonal and det(M) = 1).

        Parameters
        ==========

        M : Matrix
            Input matrix to be converted to equivalent quaternion. M must be special
            orthogonal (orthogonal and det(M) = 1) for the quaternion to be normalized.

        Returns
        =======

        Quaternion
            The quaternion equivalent to given matrix.

        Examples
        ========

        >>> from sympy import Quaternion
        >>> from sympy import Matrix, symbols, cos, sin, trigsimp
        >>> x = symbols('x')
        >>> M = Matrix([[cos(x), -sin(x), 0], [sin(x), cos(x), 0], [0, 0, 1]])
        >>> q = trigsimp(Quaternion.from_rotation_matrix(M))
        >>> q
        sqrt(2)*sqrt(cos(x) + 1)/2 + 0*i + 0*j + sqrt(2 - 2*cos(x))*sign(sin(x))/2*k

        """
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __pow__(self, p): ...
    def __neg__(self): ...
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    def diff(self, *symbols, **kwargs): ...
    def add(self, other):
        """Adds quaternions.

        Parameters
        ==========

        other : Quaternion
            The quaternion to add to current (self) quaternion.

        Returns
        =======

        Quaternion
            The resultant quaternion after adding self to other

        Examples
        ========

        >>> from sympy import Quaternion
        >>> from sympy import symbols
        >>> q1 = Quaternion(1, 2, 3, 4)
        >>> q2 = Quaternion(5, 6, 7, 8)
        >>> q1.add(q2)
        6 + 8*i + 10*j + 12*k
        >>> q1 + 5
        6 + 2*i + 3*j + 4*k
        >>> x = symbols('x', real = True)
        >>> q1.add(x)
        (x + 1) + 2*i + 3*j + 4*k

        Quaternions over complex fields :

        >>> from sympy import Quaternion
        >>> from sympy import I
        >>> q3 = Quaternion(3 + 4*I, 2 + 5*I, 0, 7 + 8*I, real_field = False)
        >>> q3.add(2 + 3*I)
        (5 + 7*I) + (2 + 5*I)*i + 0*j + (7 + 8*I)*k

        """
    def mul(self, other):
        """Multiplies quaternions.

        Parameters
        ==========

        other : Quaternion or symbol
            The quaternion to multiply to current (self) quaternion.

        Returns
        =======

        Quaternion
            The resultant quaternion after multiplying self with other

        Examples
        ========

        >>> from sympy import Quaternion
        >>> from sympy import symbols
        >>> q1 = Quaternion(1, 2, 3, 4)
        >>> q2 = Quaternion(5, 6, 7, 8)
        >>> q1.mul(q2)
        (-60) + 12*i + 30*j + 24*k
        >>> q1.mul(2)
        2 + 4*i + 6*j + 8*k
        >>> x = symbols('x', real = True)
        >>> q1.mul(x)
        x + 2*x*i + 3*x*j + 4*x*k

        Quaternions over complex fields :

        >>> from sympy import Quaternion
        >>> from sympy import I
        >>> q3 = Quaternion(3 + 4*I, 2 + 5*I, 0, 7 + 8*I, real_field = False)
        >>> q3.mul(2 + 3*I)
        (2 + 3*I)*(3 + 4*I) + (2 + 3*I)*(2 + 5*I)*i + 0*j + (2 + 3*I)*(7 + 8*I)*k

        """
    def norm(self):
        """Returns the norm of the quaternion."""
    def normalize(self):
        """Returns the normalized form of the quaternion."""
    def inverse(self):
        """Returns the inverse of the quaternion."""
    def pow(self, p):
        """Finds the pth power of the quaternion.

        Parameters
        ==========

        p : int
            Power to be applied on quaternion.

        Returns
        =======

        Quaternion
            Returns the p-th power of the current quaternion.
            Returns the inverse if p = -1.

        Examples
        ========

        >>> from sympy import Quaternion
        >>> q = Quaternion(1, 2, 3, 4)
        >>> q.pow(4)
        668 + (-224)*i + (-336)*j + (-448)*k

        """
    def exp(self):
        """Returns the exponential of q (e^q).

        Returns
        =======

        Quaternion
            Exponential of q (e^q).

        Examples
        ========

        >>> from sympy import Quaternion
        >>> q = Quaternion(1, 2, 3, 4)
        >>> q.exp()
        E*cos(sqrt(29))
        + 2*sqrt(29)*E*sin(sqrt(29))/29*i
        + 3*sqrt(29)*E*sin(sqrt(29))/29*j
        + 4*sqrt(29)*E*sin(sqrt(29))/29*k

        """
    def pow_cos_sin(self, p):
        """Computes the pth power in the cos-sin form.

        Parameters
        ==========

        p : int
            Power to be applied on quaternion.

        Returns
        =======

        Quaternion
            The p-th power in the cos-sin form.

        Examples
        ========

        >>> from sympy import Quaternion
        >>> q = Quaternion(1, 2, 3, 4)
        >>> q.pow_cos_sin(4)
        900*cos(4*acos(sqrt(30)/30))
        + 1800*sqrt(29)*sin(4*acos(sqrt(30)/30))/29*i
        + 2700*sqrt(29)*sin(4*acos(sqrt(30)/30))/29*j
        + 3600*sqrt(29)*sin(4*acos(sqrt(30)/30))/29*k

        """
    def integrate(self, *args):
        """Computes integration of quaternion.

        Returns
        =======

        Quaternion
            Integration of the quaternion(self) with the given variable.

        Examples
        ========

        Indefinite Integral of quaternion :

        >>> from sympy import Quaternion
        >>> from sympy.abc import x
        >>> q = Quaternion(1, 2, 3, 4)
        >>> q.integrate(x)
        x + 2*x*i + 3*x*j + 4*x*k

        Definite integral of quaternion :

        >>> from sympy import Quaternion
        >>> from sympy.abc import x
        >>> q = Quaternion(1, 2, 3, 4)
        >>> q.integrate((x, 1, 5))
        4 + 8*i + 12*j + 16*k

        """
    @staticmethod
    def rotate_point(pin, r):
        """Returns the coordinates of the point pin(a 3 tuple) after rotation.

        Parameters
        ==========

        pin : tuple
            A 3-element tuple of coordinates of a point which needs to be
            rotated.
        r : Quaternion or tuple
            Axis and angle of rotation.

            It's important to note that when r is a tuple, it must be of the form
            (axis, angle)

        Returns
        =======

        tuple
            The coordinates of the point after rotation.

        Examples
        ========

        >>> from sympy import Quaternion
        >>> from sympy import symbols, trigsimp, cos, sin
        >>> x = symbols('x')
        >>> q = Quaternion(cos(x/2), 0, 0, sin(x/2))
        >>> trigsimp(Quaternion.rotate_point((1, 1, 1), q))
        (sqrt(2)*cos(x + pi/4), sqrt(2)*sin(x + pi/4), 1)
        >>> (axis, angle) = q.to_axis_angle()
        >>> trigsimp(Quaternion.rotate_point((1, 1, 1), (axis, angle)))
        (sqrt(2)*cos(x + pi/4), sqrt(2)*sin(x + pi/4), 1)

        """
    def to_axis_angle(self):
        """Returns the axis and angle of rotation of a quaternion.

        Returns
        =======

        tuple
            Tuple of (axis, angle)

        Examples
        ========

        >>> from sympy import Quaternion
        >>> q = Quaternion(1, 1, 1, 1)
        >>> (axis, angle) = q.to_axis_angle()
        >>> axis
        (sqrt(3)/3, sqrt(3)/3, sqrt(3)/3)
        >>> angle
        2*pi/3

        """
    def to_rotation_matrix(self, v: Incomplete | None = None, homogeneous: bool = True):
        """Returns the equivalent rotation transformation matrix of the quaternion
        which represents rotation about the origin if v is not passed.

        Parameters
        ==========

        v : tuple or None
            Default value: None
        homogeneous : bool
            When True, gives an expression that may be more efficient for
            symbolic calculations but less so for direct evaluation. Both
            formulas are mathematically equivalent.
            Default value: True

        Returns
        =======

        tuple
            Returns the equivalent rotation transformation matrix of the quaternion
            which represents rotation about the origin if v is not passed.

        Examples
        ========

        >>> from sympy import Quaternion
        >>> from sympy import symbols, trigsimp, cos, sin
        >>> x = symbols('x')
        >>> q = Quaternion(cos(x/2), 0, 0, sin(x/2))
        >>> trigsimp(q.to_rotation_matrix())
        Matrix([
        [cos(x), -sin(x), 0],
        [sin(x),  cos(x), 0],
        [     0,       0, 1]])

        Generates a 4x4 transformation matrix (used for rotation about a point
        other than the origin) if the point(v) is passed as an argument.
        """
    def scalar_part(self):
        """Returns scalar part($\\mathbf{S}(q)$) of the quaternion q.

        Explanation
        ===========

        Given a quaternion $q = a + bi + cj + dk$, returns $\\mathbf{S}(q) = a$.

        Examples
        ========

        >>> from sympy.algebras.quaternion import Quaternion
        >>> q = Quaternion(4, 8, 13, 12)
        >>> q.scalar_part()
        4

        """
    def vector_part(self):
        """
        Returns vector part($\\mathbf{V}(q)$) of the quaternion q.

        Explanation
        ===========

        Given a quaternion $q = a + bi + cj + dk$, returns $\\mathbf{V}(q) = bi + cj + dk$.

        Examples
        ========

        >>> from sympy.algebras.quaternion import Quaternion
        >>> q = Quaternion(1, 1, 1, 1)
        >>> q.vector_part()
        0 + 1*i + 1*j + 1*k

        >>> q = Quaternion(4, 8, 13, 12)
        >>> q.vector_part()
        0 + 8*i + 13*j + 12*k

        """
    def axis(self):
        """
        Returns the axis($\\mathbf{Ax}(q)$) of the quaternion.

        Explanation
        ===========

        Given a quaternion $q = a + bi + cj + dk$, returns $\\mathbf{Ax}(q)$  i.e., the versor of the vector part of that quaternion
        equal to $\\mathbf{U}[\\mathbf{V}(q)]$.
        The axis is always an imaginary unit with square equal to $-1 + 0i + 0j + 0k$.

        Examples
        ========

        >>> from sympy.algebras.quaternion import Quaternion
        >>> q = Quaternion(1, 1, 1, 1)
        >>> q.axis()
        0 + sqrt(3)/3*i + sqrt(3)/3*j + sqrt(3)/3*k

        See Also
        ========

        vector_part

        """
    def is_pure(self):
        """
        Returns true if the quaternion is pure, false if the quaternion is not pure
        or returns none if it is unknown.

        Explanation
        ===========

        A pure quaternion (also a vector quaternion) is a quaternion with scalar
        part equal to 0.

        Examples
        ========

        >>> from sympy.algebras.quaternion import Quaternion
        >>> q = Quaternion(0, 8, 13, 12)
        >>> q.is_pure()
        True

        See Also
        ========
        scalar_part

        """
    def is_zero_quaternion(self):
        """
        Returns true if the quaternion is a zero quaternion or false if it is not a zero quaternion
        and None if the value is unknown.

        Explanation
        ===========

        A zero quaternion is a quaternion with both scalar part and
        vector part equal to 0.

        Examples
        ========

        >>> from sympy.algebras.quaternion import Quaternion
        >>> q = Quaternion(1, 0, 0, 0)
        >>> q.is_zero_quaternion()
        False

        >>> q = Quaternion(0, 0, 0, 0)
        >>> q.is_zero_quaternion()
        True

        See Also
        ========
        scalar_part
        vector_part

        """
    def angle(self):
        """
        Returns the angle of the quaternion measured in the real-axis plane.

        Explanation
        ===========

        Given a quaternion $q = a + bi + cj + dk$ where a, b, c and d
        are real numbers, returns the angle of the quaternion given by

        .. math::
            angle := atan2(\\sqrt{b^2 + c^2 + d^2}, {a})

        Examples
        ========

        >>> from sympy.algebras.quaternion import Quaternion
        >>> q = Quaternion(1, 4, 4, 4)
        >>> q.angle()
        atan(4*sqrt(3))

        """
    def arc_coplanar(self, other):
        """
        Returns True if the transformation arcs represented by the input quaternions happen in the same plane.

        Explanation
        ===========

        Two quaternions are said to be coplanar (in this arc sense) when their axes are parallel.
        The plane of a quaternion is the one normal to its axis.

        Parameters
        ==========

        other : a Quaternion

        Returns
        =======

        True : if the planes of the two quaternions are the same, apart from its orientation/sign.
        False : if the planes of the two quaternions are not the same, apart from its orientation/sign.
        None : if plane of either of the quaternion is unknown.

        Examples
        ========

        >>> from sympy.algebras.quaternion import Quaternion
        >>> q1 = Quaternion(1, 4, 4, 4)
        >>> q2 = Quaternion(3, 8, 8, 8)
        >>> Quaternion.arc_coplanar(q1, q2)
        True

        >>> q1 = Quaternion(2, 8, 13, 12)
        >>> Quaternion.arc_coplanar(q1, q2)
        False

        See Also
        ========

        vector_coplanar
        is_pure

        """
    @classmethod
    def vector_coplanar(cls, q1, q2, q3):
        """
        Returns True if the axis of the pure quaternions seen as 3D vectors
        q1, q2, and q3 are coplanar.

        Explanation
        ===========

        Three pure quaternions are vector coplanar if the quaternions seen as 3D vectors are coplanar.

        Parameters
        ==========

        q1
            A pure Quaternion.
        q2
            A pure Quaternion.
        q3
            A pure Quaternion.

        Returns
        =======

        True : if the axis of the pure quaternions seen as 3D vectors
        q1, q2, and q3 are coplanar.
        False : if the axis of the pure quaternions seen as 3D vectors
        q1, q2, and q3 are not coplanar.
        None : if the axis of the pure quaternions seen as 3D vectors
        q1, q2, and q3 are coplanar is unknown.

        Examples
        ========

        >>> from sympy.algebras.quaternion import Quaternion
        >>> q1 = Quaternion(0, 4, 4, 4)
        >>> q2 = Quaternion(0, 8, 8, 8)
        >>> q3 = Quaternion(0, 24, 24, 24)
        >>> Quaternion.vector_coplanar(q1, q2, q3)
        True

        >>> q1 = Quaternion(0, 8, 16, 8)
        >>> q2 = Quaternion(0, 8, 3, 12)
        >>> Quaternion.vector_coplanar(q1, q2, q3)
        False

        See Also
        ========

        axis
        is_pure

        """
    def parallel(self, other):
        """
        Returns True if the two pure quaternions seen as 3D vectors are parallel.

        Explanation
        ===========

        Two pure quaternions are called parallel when their vector product is commutative which
        implies that the quaternions seen as 3D vectors have same direction.

        Parameters
        ==========

        other : a Quaternion

        Returns
        =======

        True : if the two pure quaternions seen as 3D vectors are parallel.
        False : if the two pure quaternions seen as 3D vectors are not parallel.
        None : if the two pure quaternions seen as 3D vectors are parallel is unknown.

        Examples
        ========

        >>> from sympy.algebras.quaternion import Quaternion
        >>> q = Quaternion(0, 4, 4, 4)
        >>> q1 = Quaternion(0, 8, 8, 8)
        >>> q.parallel(q1)
        True

        >>> q1 = Quaternion(0, 8, 13, 12)
        >>> q.parallel(q1)
        False

        """
    def orthogonal(self, other):
        """
        Returns the orthogonality of two quaternions.

        Explanation
        ===========

        Two pure quaternions are called orthogonal when their product is anti-commutative.

        Parameters
        ==========

        other : a Quaternion

        Returns
        =======

        True : if the two pure quaternions seen as 3D vectors are orthogonal.
        False : if the two pure quaternions seen as 3D vectors are not orthogonal.
        None : if the two pure quaternions seen as 3D vectors are orthogonal is unknown.

        Examples
        ========

        >>> from sympy.algebras.quaternion import Quaternion
        >>> q = Quaternion(0, 4, 4, 4)
        >>> q1 = Quaternion(0, 8, 8, 8)
        >>> q.orthogonal(q1)
        False

        >>> q1 = Quaternion(0, 2, 2, 0)
        >>> q = Quaternion(0, 2, -2, 0)
        >>> q.orthogonal(q1)
        True

        """
    def index_vector(self):
        """
        Returns the index vector of the quaternion.

        Explanation
        ===========

        Index vector is given by $\\mathbf{T}(q)$ multiplied by $\\mathbf{Ax}(q)$ where $\\mathbf{Ax}(q)$ is the axis of the quaternion q,
        and mod(q) is the $\\mathbf{T}(q)$ (magnitude) of the quaternion.

        Returns
        =======

        Quaternion: representing index vector of the provided quaternion.

        Examples
        ========

        >>> from sympy.algebras.quaternion import Quaternion
        >>> q = Quaternion(2, 4, 2, 4)
        >>> q.index_vector()
        0 + 4*sqrt(10)/3*i + 2*sqrt(10)/3*j + 4*sqrt(10)/3*k

        See Also
        ========

        axis
        norm

        """
    def mensor(self):
        """
        Returns the natural logarithm of the norm(magnitude) of the quaternion.

        Examples
        ========

        >>> from sympy.algebras.quaternion import Quaternion
        >>> q = Quaternion(2, 4, 2, 4)
        >>> q.mensor()
        log(2*sqrt(10))
        >>> q.norm()
        2*sqrt(10)

        See Also
        ========

        norm

        """
