from _typeshed import Incomplete
from sympy.physics.mechanics import Particle, RigidBody

__all__ = ['Body']

class Body(RigidBody, Particle):
    """
    Body is a common representation of either a RigidBody or a Particle SymPy
    object depending on what is passed in during initialization. If a mass is
    passed in and central_inertia is left as None, the Particle object is
    created. Otherwise a RigidBody object will be created.

    Explanation
    ===========

    The attributes that Body possesses will be the same as a Particle instance
    or a Rigid Body instance depending on which was created. Additional
    attributes are listed below.

    Attributes
    ==========

    name : string
        The body's name
    masscenter : Point
        The point which represents the center of mass of the rigid body
    frame : ReferenceFrame
        The reference frame which the body is fixed in
    mass : Sympifyable
        The body's mass
    inertia : (Dyadic, Point)
        The body's inertia around its center of mass. This attribute is specific
        to the rigid body form of Body and is left undefined for the Particle
        form
    loads : iterable
        This list contains information on the different loads acting on the
        Body. Forces are listed as a (point, vector) tuple and torques are
        listed as (reference frame, vector) tuples.

    Parameters
    ==========

    name : String
        Defines the name of the body. It is used as the base for defining
        body specific properties.
    masscenter : Point, optional
        A point that represents the center of mass of the body or particle.
        If no point is given, a point is generated.
    mass : Sympifyable, optional
        A Sympifyable object which represents the mass of the body. If no
        mass is passed, one is generated.
    frame : ReferenceFrame, optional
        The ReferenceFrame that represents the reference frame of the body.
        If no frame is given, a frame is generated.
    central_inertia : Dyadic, optional
        Central inertia dyadic of the body. If none is passed while creating
        RigidBody, a default inertia is generated.

    Examples
    ========

    Default behaviour. This results in the creation of a RigidBody object for
    which the mass, mass center, frame and inertia attributes are given default
    values. ::

        >>> from sympy.physics.mechanics import Body
        >>> body = Body('name_of_body')

    This next example demonstrates the code required to specify all of the
    values of the Body object. Note this will also create a RigidBody version of
    the Body object. ::

        >>> from sympy import Symbol
        >>> from sympy.physics.mechanics import ReferenceFrame, Point, inertia
        >>> from sympy.physics.mechanics import Body
        >>> mass = Symbol('mass')
        >>> masscenter = Point('masscenter')
        >>> frame = ReferenceFrame('frame')
        >>> ixx = Symbol('ixx')
        >>> body_inertia = inertia(frame, ixx, 0, 0)
        >>> body = Body('name_of_body', masscenter, mass, frame, body_inertia)

    The minimal code required to create a Particle version of the Body object
    involves simply passing in a name and a mass. ::

        >>> from sympy import Symbol
        >>> from sympy.physics.mechanics import Body
        >>> mass = Symbol('mass')
        >>> body = Body('name_of_body', mass=mass)

    The Particle version of the Body object can also receive a masscenter point
    and a reference frame, just not an inertia.
    """
    name: Incomplete
    frame: Incomplete
    masscenter: Incomplete
    def __init__(self, name, masscenter: Incomplete | None = None, mass: Incomplete | None = None, frame: Incomplete | None = None, central_inertia: Incomplete | None = None) -> None: ...
    @property
    def loads(self): ...
    @property
    def x(self):
        """The basis Vector for the Body, in the x direction."""
    @property
    def y(self):
        """The basis Vector for the Body, in the y direction."""
    @property
    def z(self):
        """The basis Vector for the Body, in the z direction."""
    @property
    def inertia(self):
        """The body's inertia about a point; stored as (Dyadic, Point)."""
    @inertia.setter
    def inertia(self, I) -> None: ...
    @property
    def is_rigidbody(self): ...
    def kinetic_energy(self, frame):
        """Kinetic energy of the body.

        Parameters
        ==========

        frame : ReferenceFrame or Body
            The Body's angular velocity and the velocity of it's mass
            center are typically defined with respect to an inertial frame but
            any relevant frame in which the velocities are known can be supplied.

        Examples
        ========

        >>> from sympy.physics.mechanics import Body, ReferenceFrame, Point
        >>> from sympy import symbols
        >>> m, v, r, omega = symbols('m v r omega')
        >>> N = ReferenceFrame('N')
        >>> O = Point('O')
        >>> P = Body('P', masscenter=O, mass=m)
        >>> P.masscenter.set_vel(N, v * N.y)
        >>> P.kinetic_energy(N)
        m*v**2/2

        >>> N = ReferenceFrame('N')
        >>> b = ReferenceFrame('b')
        >>> b.set_ang_vel(N, omega * b.x)
        >>> P = Point('P')
        >>> P.set_vel(N, v * N.x)
        >>> B = Body('B', masscenter=P, frame=b)
        >>> B.kinetic_energy(N)
        B_ixx*omega**2/2 + B_mass*v**2/2

        See Also
        ========

        sympy.physics.mechanics : Particle, RigidBody

        """
    def apply_force(self, force, point: Incomplete | None = None, reaction_body: Incomplete | None = None, reaction_point: Incomplete | None = None) -> None:
        """Add force to the body(s).

        Explanation
        ===========

        Applies the force on self or equal and oppposite forces on
        self and other body if both are given on the desried point on the bodies.
        The force applied on other body is taken opposite of self, i.e, -force.

        Parameters
        ==========

        force: Vector
            The force to be applied.
        point: Point, optional
            The point on self on which force is applied.
            By default self's masscenter.
        reaction_body: Body, optional
            Second body on which equal and opposite force
            is to be applied.
        reaction_point : Point, optional
            The point on other body on which equal and opposite
            force is applied. By default masscenter of other body.

        Example
        =======

        >>> from sympy import symbols
        >>> from sympy.physics.mechanics import Body, Point, dynamicsymbols
        >>> m, g = symbols('m g')
        >>> B = Body('B')
        >>> force1 = m*g*B.z
        >>> B.apply_force(force1) #Applying force on B's masscenter
        >>> B.loads
        [(B_masscenter, g*m*B_frame.z)]

        We can also remove some part of force from any point on the body by
        adding the opposite force to the body on that point.

        >>> f1, f2 = dynamicsymbols('f1 f2')
        >>> P = Point('P') #Considering point P on body B
        >>> B.apply_force(f1*B.x + f2*B.y, P)
        >>> B.loads
        [(B_masscenter, g*m*B_frame.z), (P, f1(t)*B_frame.x + f2(t)*B_frame.y)]

        Let's remove f1 from point P on body B.

        >>> B.apply_force(-f1*B.x, P)
        >>> B.loads
        [(B_masscenter, g*m*B_frame.z), (P, f2(t)*B_frame.y)]

        To further demonstrate the use of ``apply_force`` attribute,
        consider two bodies connected through a spring.

        >>> from sympy.physics.mechanics import Body, dynamicsymbols
        >>> N = Body('N') #Newtonion Frame
        >>> x = dynamicsymbols('x')
        >>> B1 = Body('B1')
        >>> B2 = Body('B2')
        >>> spring_force = x*N.x

        Now let's apply equal and opposite spring force to the bodies.

        >>> P1 = Point('P1')
        >>> P2 = Point('P2')
        >>> B1.apply_force(spring_force, point=P1, reaction_body=B2, reaction_point=P2)

        We can check the loads(forces) applied to bodies now.

        >>> B1.loads
        [(P1, x(t)*N_frame.x)]
        >>> B2.loads
        [(P2, - x(t)*N_frame.x)]

        Notes
        =====

        If a new force is applied to a body on a point which already has some
        force applied on it, then the new force is added to the already applied
        force on that point.

        """
    def apply_torque(self, torque, reaction_body: Incomplete | None = None) -> None:
        """Add torque to the body(s).

        Explanation
        ===========

        Applies the torque on self or equal and oppposite torquess on
        self and other body if both are given.
        The torque applied on other body is taken opposite of self,
        i.e, -torque.

        Parameters
        ==========

        torque: Vector
            The torque to be applied.
        reaction_body: Body, optional
            Second body on which equal and opposite torque
            is to be applied.

        Example
        =======

        >>> from sympy import symbols
        >>> from sympy.physics.mechanics import Body, dynamicsymbols
        >>> t = symbols('t')
        >>> B = Body('B')
        >>> torque1 = t*B.z
        >>> B.apply_torque(torque1)
        >>> B.loads
        [(B_frame, t*B_frame.z)]

        We can also remove some part of torque from the body by
        adding the opposite torque to the body.

        >>> t1, t2 = dynamicsymbols('t1 t2')
        >>> B.apply_torque(t1*B.x + t2*B.y)
        >>> B.loads
        [(B_frame, t1(t)*B_frame.x + t2(t)*B_frame.y + t*B_frame.z)]

        Let's remove t1 from Body B.

        >>> B.apply_torque(-t1*B.x)
        >>> B.loads
        [(B_frame, t2(t)*B_frame.y + t*B_frame.z)]

        To further demonstrate the use, let us consider two bodies such that
        a torque `T` is acting on one body, and `-T` on the other.

        >>> from sympy.physics.mechanics import Body, dynamicsymbols
        >>> N = Body('N') #Newtonion frame
        >>> B1 = Body('B1')
        >>> B2 = Body('B2')
        >>> v = dynamicsymbols('v')
        >>> T = v*N.y #Torque

        Now let's apply equal and opposite torque to the bodies.

        >>> B1.apply_torque(T, B2)

        We can check the loads (torques) applied to bodies now.

        >>> B1.loads
        [(B1_frame, v(t)*N_frame.y)]
        >>> B2.loads
        [(B2_frame, - v(t)*N_frame.y)]

        Notes
        =====

        If a new torque is applied on body which already has some torque applied on it,
        then the new torque is added to the previous torque about the body's frame.

        """
    def clear_loads(self) -> None:
        """
        Clears the Body's loads list.

        Example
        =======

        >>> from sympy.physics.mechanics import Body
        >>> B = Body('B')
        >>> force = B.x + B.y
        >>> B.apply_force(force)
        >>> B.loads
        [(B_masscenter, B_frame.x + B_frame.y)]
        >>> B.clear_loads()
        >>> B.loads
        []

        """
    def remove_load(self, about: Incomplete | None = None) -> None:
        """
        Remove load about a point or frame.

        Parameters
        ==========

        about : Point or ReferenceFrame, optional
            The point about which force is applied,
            and is to be removed.
            If about is None, then the torque about
            self's frame is removed.

        Example
        =======

        >>> from sympy.physics.mechanics import Body, Point
        >>> B = Body('B')
        >>> P = Point('P')
        >>> f1 = B.x
        >>> f2 = B.y
        >>> B.apply_force(f1)
        >>> B.apply_force(f2, P)
        >>> B.loads
        [(B_masscenter, B_frame.x), (P, B_frame.y)]

        >>> B.remove_load(P)
        >>> B.loads
        [(B_masscenter, B_frame.x)]

        """
    def masscenter_vel(self, body):
        """
        Returns the velocity of the mass center with respect to the provided
        rigid body or reference frame.

        Parameters
        ==========

        body: Body or ReferenceFrame
            The rigid body or reference frame to calculate the velocity in.

        Example
        =======

        >>> from sympy.physics.mechanics import Body
        >>> A = Body('A')
        >>> B = Body('B')
        >>> A.masscenter.set_vel(B.frame, 5*B.frame.x)
        >>> A.masscenter_vel(B)
        5*B_frame.x
        >>> A.masscenter_vel(B.frame)
        5*B_frame.x

        """
    def ang_vel_in(self, body):
        """
        Returns this body's angular velocity with respect to the provided
        rigid body or reference frame.

        Parameters
        ==========

        body: Body or ReferenceFrame
            The rigid body or reference frame to calculate the angular velocity in.

        Example
        =======

        >>> from sympy.physics.mechanics import Body, ReferenceFrame
        >>> A = Body('A')
        >>> N = ReferenceFrame('N')
        >>> B = Body('B', frame=N)
        >>> A.frame.set_ang_vel(N, 5*N.x)
        >>> A.ang_vel_in(B)
        5*N.x
        >>> A.ang_vel_in(N)
        5*N.x

        """
    def dcm(self, body):
        """
        Returns the direction cosine matrix of this body relative to the
        provided rigid body or reference frame.

        Parameters
        ==========

        body: Body or ReferenceFrame
            The rigid body or reference frame to calculate the dcm.

        Example
        =======

        >>> from sympy.physics.mechanics import Body
        >>> A = Body('A')
        >>> B = Body('B')
        >>> A.frame.orient_axis(B.frame, B.frame.x, 5)
        >>> A.dcm(B)
        Matrix([
        [1,       0,      0],
        [0,  cos(5), sin(5)],
        [0, -sin(5), cos(5)]])
        >>> A.dcm(B.frame)
        Matrix([
        [1,       0,      0],
        [0,  cos(5), sin(5)],
        [0, -sin(5), cos(5)]])

        """
    def parallel_axis(self, point, frame: Incomplete | None = None):
        """Returns the inertia dyadic of the body with respect to another
        point.

        Parameters
        ==========

        point : sympy.physics.vector.Point
            The point to express the inertia dyadic about.
        frame : sympy.physics.vector.ReferenceFrame
            The reference frame used to construct the dyadic.

        Returns
        =======

        inertia : sympy.physics.vector.Dyadic
            The inertia dyadic of the rigid body expressed about the provided
            point.

        Example
        =======

        >>> from sympy.physics.mechanics import Body
        >>> A = Body('A')
        >>> P = A.masscenter.locatenew('point', 3 * A.x + 5 * A.y)
        >>> A.parallel_axis(P).to_matrix(A.frame)
        Matrix([
        [A_ixx + 25*A_mass, A_ixy - 15*A_mass,             A_izx],
        [A_ixy - 15*A_mass,  A_iyy + 9*A_mass,             A_iyz],
        [            A_izx,             A_iyz, A_izz + 34*A_mass]])

        """
