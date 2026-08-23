from sympy.core.basic import Basic as Basic
from sympy.core.cache import cacheit as cacheit
from sympy.core.symbol import Str as Str
from sympy.core.sympify import sympify as sympify
from sympy.functions.elementary.trigonometric import cos as cos, sin as sin
from sympy.matrices.dense import eye as eye, rot_axis1 as rot_axis1, rot_axis2 as rot_axis2, rot_axis3 as rot_axis3

class Orienter(Basic):
    """
    Super-class for all orienter classes.
    """
    def rotation_matrix(self):
        """
        The rotation matrix corresponding to this orienter
        instance.
        """

class AxisOrienter(Orienter):
    """
    Class to denote an axis orienter.
    """
    def __new__(cls, angle, axis): ...
    def __init__(self, angle, axis) -> None:
        """
        Axis rotation is a rotation about an arbitrary axis by
        some angle. The angle is supplied as a SymPy expr scalar, and
        the axis is supplied as a Vector.

        Parameters
        ==========

        angle : Expr
            The angle by which the new system is to be rotated

        axis : Vector
            The axis around which the rotation has to be performed

        Examples
        ========

        >>> from sympy.vector import CoordSys3D
        >>> from sympy import symbols
        >>> q1 = symbols('q1')
        >>> N = CoordSys3D('N')
        >>> from sympy.vector import AxisOrienter
        >>> orienter = AxisOrienter(q1, N.i + 2 * N.j)
        >>> B = N.orient_new('B', (orienter, ))

        """
    def rotation_matrix(self, system):
        """
        The rotation matrix corresponding to this orienter
        instance.

        Parameters
        ==========

        system : CoordSys3D
            The coordinate system wrt which the rotation matrix
            is to be computed
        """
    @property
    def angle(self): ...
    @property
    def axis(self): ...

class ThreeAngleOrienter(Orienter):
    """
    Super-class for Body and Space orienters.
    """
    def __new__(cls, angle1, angle2, angle3, rot_order): ...
    @property
    def angle1(self): ...
    @property
    def angle2(self): ...
    @property
    def angle3(self): ...
    @property
    def rot_order(self): ...

class BodyOrienter(ThreeAngleOrienter):
    """
    Class to denote a body-orienter.
    """
    def __new__(cls, angle1, angle2, angle3, rot_order): ...
    def __init__(self, angle1, angle2, angle3, rot_order) -> None:
        """
        Body orientation takes this coordinate system through three
        successive simple rotations.

        Body fixed rotations include both Euler Angles and
        Tait-Bryan Angles, see https://en.wikipedia.org/wiki/Euler_angles.

        Parameters
        ==========

        angle1, angle2, angle3 : Expr
            Three successive angles to rotate the coordinate system by

        rotation_order : string
            String defining the order of axes for rotation

        Examples
        ========

        >>> from sympy.vector import CoordSys3D, BodyOrienter
        >>> from sympy import symbols
        >>> q1, q2, q3 = symbols('q1 q2 q3')
        >>> N = CoordSys3D('N')

        A 'Body' fixed rotation is described by three angles and
        three body-fixed rotation axes. To orient a coordinate system D
        with respect to N, each sequential rotation is always about
        the orthogonal unit vectors fixed to D. For example, a '123'
        rotation will specify rotations about N.i, then D.j, then
        D.k. (Initially, D.i is same as N.i)
        Therefore,

        >>> body_orienter = BodyOrienter(q1, q2, q3, '123')
        >>> D = N.orient_new('D', (body_orienter, ))

        is same as

        >>> from sympy.vector import AxisOrienter
        >>> axis_orienter1 = AxisOrienter(q1, N.i)
        >>> D = N.orient_new('D', (axis_orienter1, ))
        >>> axis_orienter2 = AxisOrienter(q2, D.j)
        >>> D = D.orient_new('D', (axis_orienter2, ))
        >>> axis_orienter3 = AxisOrienter(q3, D.k)
        >>> D = D.orient_new('D', (axis_orienter3, ))

        Acceptable rotation orders are of length 3, expressed in XYZ or
        123, and cannot have a rotation about about an axis twice in a row.

        >>> body_orienter1 = BodyOrienter(q1, q2, q3, '123')
        >>> body_orienter2 = BodyOrienter(q1, q2, 0, 'ZXZ')
        >>> body_orienter3 = BodyOrienter(0, 0, 0, 'XYX')

        """

class SpaceOrienter(ThreeAngleOrienter):
    """
    Class to denote a space-orienter.
    """
    def __new__(cls, angle1, angle2, angle3, rot_order): ...
    def __init__(self, angle1, angle2, angle3, rot_order) -> None:
        """
        Space rotation is similar to Body rotation, but the rotations
        are applied in the opposite order.

        Parameters
        ==========

        angle1, angle2, angle3 : Expr
            Three successive angles to rotate the coordinate system by

        rotation_order : string
            String defining the order of axes for rotation

        See Also
        ========

        BodyOrienter : Orienter to orient systems wrt Euler angles.

        Examples
        ========

        >>> from sympy.vector import CoordSys3D, SpaceOrienter
        >>> from sympy import symbols
        >>> q1, q2, q3 = symbols('q1 q2 q3')
        >>> N = CoordSys3D('N')

        To orient a coordinate system D with respect to N, each
        sequential rotation is always about N's orthogonal unit vectors.
        For example, a '123' rotation will specify rotations about
        N.i, then N.j, then N.k.
        Therefore,

        >>> space_orienter = SpaceOrienter(q1, q2, q3, '312')
        >>> D = N.orient_new('D', (space_orienter, ))

        is same as

        >>> from sympy.vector import AxisOrienter
        >>> axis_orienter1 = AxisOrienter(q1, N.i)
        >>> B = N.orient_new('B', (axis_orienter1, ))
        >>> axis_orienter2 = AxisOrienter(q2, N.j)
        >>> C = B.orient_new('C', (axis_orienter2, ))
        >>> axis_orienter3 = AxisOrienter(q3, N.k)
        >>> D = C.orient_new('C', (axis_orienter3, ))

        """

class QuaternionOrienter(Orienter):
    """
    Class to denote a quaternion-orienter.
    """
    def __new__(cls, q0, q1, q2, q3): ...
    def __init__(self, angle1, angle2, angle3, rot_order) -> None:
        """
        Quaternion orientation orients the new CoordSys3D with
        Quaternions, defined as a finite rotation about lambda, a unit
        vector, by some amount theta.

        This orientation is described by four parameters:

        q0 = cos(theta/2)

        q1 = lambda_x sin(theta/2)

        q2 = lambda_y sin(theta/2)

        q3 = lambda_z sin(theta/2)

        Quaternion does not take in a rotation order.

        Parameters
        ==========

        q0, q1, q2, q3 : Expr
            The quaternions to rotate the coordinate system by

        Examples
        ========

        >>> from sympy.vector import CoordSys3D
        >>> from sympy import symbols
        >>> q0, q1, q2, q3 = symbols('q0 q1 q2 q3')
        >>> N = CoordSys3D('N')
        >>> from sympy.vector import QuaternionOrienter
        >>> q_orienter = QuaternionOrienter(q0, q1, q2, q3)
        >>> B = N.orient_new('B', (q_orienter, ))

        """
    @property
    def q0(self): ...
    @property
    def q1(self): ...
    @property
    def q2(self): ...
    @property
    def q3(self): ...
