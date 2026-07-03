from _typeshed import Incomplete

__all__ = ['Point']

class Point:
    """This object represents a point in a dynamic system.

    It stores the: position, velocity, and acceleration of a point.
    The position is a vector defined as the vector distance from a parent
    point to this point.

    Parameters
    ==========

    name : string
        The display name of the Point

    Examples
    ========

    >>> from sympy.physics.vector import Point, ReferenceFrame, dynamicsymbols
    >>> from sympy.physics.vector import init_vprinting
    >>> init_vprinting(pretty_print=False)
    >>> N = ReferenceFrame('N')
    >>> O = Point('O')
    >>> P = Point('P')
    >>> u1, u2, u3 = dynamicsymbols('u1 u2 u3')
    >>> O.set_vel(N, u1 * N.x + u2 * N.y + u3 * N.z)
    >>> O.acc(N)
    u1'*N.x + u2'*N.y + u3'*N.z

    ``symbols()`` can be used to create multiple Points in a single step, for
    example:

    >>> from sympy.physics.vector import Point, ReferenceFrame, dynamicsymbols
    >>> from sympy.physics.vector import init_vprinting
    >>> init_vprinting(pretty_print=False)
    >>> from sympy import symbols
    >>> N = ReferenceFrame('N')
    >>> u1, u2 = dynamicsymbols('u1 u2')
    >>> A, B = symbols('A B', cls=Point)
    >>> type(A)
    <class 'sympy.physics.vector.point.Point'>
    >>> A.set_vel(N, u1 * N.x + u2 * N.y)
    >>> B.set_vel(N, u2 * N.x + u1 * N.y)
    >>> A.acc(N) - B.acc(N)
    (u1' - u2')*N.x + (-u1' + u2')*N.y

    """
    name: Incomplete
    def __init__(self, name) -> None:
        """Initialization of a Point object. """
    def a1pt_theory(self, otherpoint, outframe, interframe):
        """Sets the acceleration of this point with the 1-point theory.

        The 1-point theory for point acceleration looks like this:

        ^N a^P = ^B a^P + ^N a^O + ^N alpha^B x r^OP + ^N omega^B x (^N omega^B
        x r^OP) + 2 ^N omega^B x ^B v^P

        where O is a point fixed in B, P is a point moving in B, and B is
        rotating in frame N.

        Parameters
        ==========

        otherpoint : Point
            The first point of the 1-point theory (O)
        outframe : ReferenceFrame
            The frame we want this point's acceleration defined in (N)
        fixedframe : ReferenceFrame
            The intermediate frame in this calculation (B)

        Examples
        ========

        >>> from sympy.physics.vector import Point, ReferenceFrame
        >>> from sympy.physics.vector import dynamicsymbols
        >>> from sympy.physics.vector import init_vprinting
        >>> init_vprinting(pretty_print=False)
        >>> q = dynamicsymbols('q')
        >>> q2 = dynamicsymbols('q2')
        >>> qd = dynamicsymbols('q', 1)
        >>> q2d = dynamicsymbols('q2', 1)
        >>> N = ReferenceFrame('N')
        >>> B = ReferenceFrame('B')
        >>> B.set_ang_vel(N, 5 * B.y)
        >>> O = Point('O')
        >>> P = O.locatenew('P', q * B.x)
        >>> P.set_vel(B, qd * B.x + q2d * B.y)
        >>> O.set_vel(N, 0)
        >>> P.a1pt_theory(O, N, B)
        (-25*q + q'')*B.x + q2''*B.y - 10*q'*B.z

        """
    def a2pt_theory(self, otherpoint, outframe, fixedframe):
        """Sets the acceleration of this point with the 2-point theory.

        The 2-point theory for point acceleration looks like this:

        ^N a^P = ^N a^O + ^N alpha^B x r^OP + ^N omega^B x (^N omega^B x r^OP)

        where O and P are both points fixed in frame B, which is rotating in
        frame N.

        Parameters
        ==========

        otherpoint : Point
            The first point of the 2-point theory (O)
        outframe : ReferenceFrame
            The frame we want this point's acceleration defined in (N)
        fixedframe : ReferenceFrame
            The frame in which both points are fixed (B)

        Examples
        ========

        >>> from sympy.physics.vector import Point, ReferenceFrame, dynamicsymbols
        >>> from sympy.physics.vector import init_vprinting
        >>> init_vprinting(pretty_print=False)
        >>> q = dynamicsymbols('q')
        >>> qd = dynamicsymbols('q', 1)
        >>> N = ReferenceFrame('N')
        >>> B = N.orientnew('B', 'Axis', [q, N.z])
        >>> O = Point('O')
        >>> P = O.locatenew('P', 10 * B.x)
        >>> O.set_vel(N, 5 * N.x)
        >>> P.a2pt_theory(O, N, B)
        - 10*q'**2*B.x + 10*q''*B.y

        """
    def acc(self, frame):
        """The acceleration Vector of this Point in a ReferenceFrame.

        Parameters
        ==========

        frame : ReferenceFrame
            The frame in which the returned acceleration vector will be defined
            in.

        Examples
        ========

        >>> from sympy.physics.vector import Point, ReferenceFrame
        >>> N = ReferenceFrame('N')
        >>> p1 = Point('p1')
        >>> p1.set_acc(N, 10 * N.x)
        >>> p1.acc(N)
        10*N.x

        """
    def locatenew(self, name, value):
        """Creates a new point with a position defined from this point.

        Parameters
        ==========

        name : str
            The name for the new point
        value : Vector
            The position of the new point relative to this point

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame, Point
        >>> N = ReferenceFrame('N')
        >>> P1 = Point('P1')
        >>> P2 = P1.locatenew('P2', 10 * N.x)

        """
    def pos_from(self, otherpoint):
        """Returns a Vector distance between this Point and the other Point.

        Parameters
        ==========

        otherpoint : Point
            The otherpoint we are locating this one relative to

        Examples
        ========

        >>> from sympy.physics.vector import Point, ReferenceFrame
        >>> N = ReferenceFrame('N')
        >>> p1 = Point('p1')
        >>> p2 = Point('p2')
        >>> p1.set_pos(p2, 10 * N.x)
        >>> p1.pos_from(p2)
        10*N.x

        """
    def set_acc(self, frame, value) -> None:
        """Used to set the acceleration of this Point in a ReferenceFrame.

        Parameters
        ==========

        frame : ReferenceFrame
            The frame in which this point's acceleration is defined
        value : Vector
            The vector value of this point's acceleration in the frame

        Examples
        ========

        >>> from sympy.physics.vector import Point, ReferenceFrame
        >>> N = ReferenceFrame('N')
        >>> p1 = Point('p1')
        >>> p1.set_acc(N, 10 * N.x)
        >>> p1.acc(N)
        10*N.x

        """
    def set_pos(self, otherpoint, value) -> None:
        """Used to set the position of this point w.r.t. another point.

        Parameters
        ==========

        otherpoint : Point
            The other point which this point's location is defined relative to
        value : Vector
            The vector which defines the location of this point

        Examples
        ========

        >>> from sympy.physics.vector import Point, ReferenceFrame
        >>> N = ReferenceFrame('N')
        >>> p1 = Point('p1')
        >>> p2 = Point('p2')
        >>> p1.set_pos(p2, 10 * N.x)
        >>> p1.pos_from(p2)
        10*N.x

        """
    def set_vel(self, frame, value) -> None:
        """Sets the velocity Vector of this Point in a ReferenceFrame.

        Parameters
        ==========

        frame : ReferenceFrame
            The frame in which this point's velocity is defined
        value : Vector
            The vector value of this point's velocity in the frame

        Examples
        ========

        >>> from sympy.physics.vector import Point, ReferenceFrame
        >>> N = ReferenceFrame('N')
        >>> p1 = Point('p1')
        >>> p1.set_vel(N, 10 * N.x)
        >>> p1.vel(N)
        10*N.x

        """
    def v1pt_theory(self, otherpoint, outframe, interframe):
        """Sets the velocity of this point with the 1-point theory.

        The 1-point theory for point velocity looks like this:

        ^N v^P = ^B v^P + ^N v^O + ^N omega^B x r^OP

        where O is a point fixed in B, P is a point moving in B, and B is
        rotating in frame N.

        Parameters
        ==========

        otherpoint : Point
            The first point of the 1-point theory (O)
        outframe : ReferenceFrame
            The frame we want this point's velocity defined in (N)
        interframe : ReferenceFrame
            The intermediate frame in this calculation (B)

        Examples
        ========

        >>> from sympy.physics.vector import Point, ReferenceFrame
        >>> from sympy.physics.vector import dynamicsymbols
        >>> from sympy.physics.vector import init_vprinting
        >>> init_vprinting(pretty_print=False)
        >>> q = dynamicsymbols('q')
        >>> q2 = dynamicsymbols('q2')
        >>> qd = dynamicsymbols('q', 1)
        >>> q2d = dynamicsymbols('q2', 1)
        >>> N = ReferenceFrame('N')
        >>> B = ReferenceFrame('B')
        >>> B.set_ang_vel(N, 5 * B.y)
        >>> O = Point('O')
        >>> P = O.locatenew('P', q * B.x)
        >>> P.set_vel(B, qd * B.x + q2d * B.y)
        >>> O.set_vel(N, 0)
        >>> P.v1pt_theory(O, N, B)
        q'*B.x + q2'*B.y - 5*q*B.z

        """
    def v2pt_theory(self, otherpoint, outframe, fixedframe):
        """Sets the velocity of this point with the 2-point theory.

        The 2-point theory for point velocity looks like this:

        ^N v^P = ^N v^O + ^N omega^B x r^OP

        where O and P are both points fixed in frame B, which is rotating in
        frame N.

        Parameters
        ==========

        otherpoint : Point
            The first point of the 2-point theory (O)
        outframe : ReferenceFrame
            The frame we want this point's velocity defined in (N)
        fixedframe : ReferenceFrame
            The frame in which both points are fixed (B)

        Examples
        ========

        >>> from sympy.physics.vector import Point, ReferenceFrame, dynamicsymbols
        >>> from sympy.physics.vector import init_vprinting
        >>> init_vprinting(pretty_print=False)
        >>> q = dynamicsymbols('q')
        >>> qd = dynamicsymbols('q', 1)
        >>> N = ReferenceFrame('N')
        >>> B = N.orientnew('B', 'Axis', [q, N.z])
        >>> O = Point('O')
        >>> P = O.locatenew('P', 10 * B.x)
        >>> O.set_vel(N, 5 * N.x)
        >>> P.v2pt_theory(O, N, B)
        5*N.x + 10*q'*B.y

        """
    def vel(self, frame):
        """The velocity Vector of this Point in the ReferenceFrame.

        Parameters
        ==========

        frame : ReferenceFrame
            The frame in which the returned velocity vector will be defined in

        Examples
        ========

        >>> from sympy.physics.vector import Point, ReferenceFrame, dynamicsymbols
        >>> N = ReferenceFrame('N')
        >>> p1 = Point('p1')
        >>> p1.set_vel(N, 10 * N.x)
        >>> p1.vel(N)
        10*N.x

        Velocities will be automatically calculated if possible, otherwise a
        ``ValueError`` will be returned. If it is possible to calculate
        multiple different velocities from the relative points, the points
        defined most directly relative to this point will be used. In the case
        of inconsistent relative positions of points, incorrect velocities may
        be returned. It is up to the user to define prior relative positions
        and velocities of points in a self-consistent way.

        >>> p = Point('p')
        >>> q = dynamicsymbols('q')
        >>> p.set_vel(N, 10 * N.x)
        >>> p2 = Point('p2')
        >>> p2.set_pos(p, q*N.x)
        >>> p2.vel(N)
        (Derivative(q(t), t) + 10)*N.x

        """
    def partial_velocity(self, frame, *gen_speeds):
        """Returns the partial velocities of the linear velocity vector of this
        point in the given frame with respect to one or more provided
        generalized speeds.

        Parameters
        ==========
        frame : ReferenceFrame
            The frame with which the velocity is defined in.
        gen_speeds : functions of time
            The generalized speeds.

        Returns
        =======
        partial_velocities : tuple of Vector
            The partial velocity vectors corresponding to the provided
            generalized speeds.

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame, Point
        >>> from sympy.physics.vector import dynamicsymbols
        >>> N = ReferenceFrame('N')
        >>> A = ReferenceFrame('A')
        >>> p = Point('p')
        >>> u1, u2 = dynamicsymbols('u1, u2')
        >>> p.set_vel(N, u1 * N.x + u2 * A.y)
        >>> p.partial_velocity(N, u1)
        N.x
        >>> p.partial_velocity(N, u1, u2)
        (N.x, A.y)

        """
