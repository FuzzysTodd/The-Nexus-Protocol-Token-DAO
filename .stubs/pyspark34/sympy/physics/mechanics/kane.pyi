from _typeshed import Incomplete
from sympy.physics.mechanics.method import _Methods

__all__ = ['KanesMethod']

class KanesMethod(_Methods):
    '''Kane\'s method object.

    Explanation
    ===========

    This object is used to do the "book-keeping" as you go through and form
    equations of motion in the way Kane presents in:
    Kane, T., Levinson, D. Dynamics Theory and Applications. 1985 McGraw-Hill

    The attributes are for equations in the form [M] udot = forcing.

    Attributes
    ==========

    q, u : Matrix
        Matrices of the generalized coordinates and speeds
    bodies : iterable
        Iterable of Point and RigidBody objects in the system.
    loads : iterable
        Iterable of (Point, vector) or (ReferenceFrame, vector) tuples
        describing the forces on the system.
    auxiliary_eqs : Matrix
        If applicable, the set of auxiliary Kane\'s
        equations used to solve for non-contributing
        forces.
    mass_matrix : Matrix
        The system\'s dynamics mass matrix: [k_d; k_dnh]
    forcing : Matrix
        The system\'s dynamics forcing vector: -[f_d; f_dnh]
    mass_matrix_kin : Matrix
        The "mass matrix" for kinematic differential equations: k_kqdot
    forcing_kin : Matrix
        The forcing vector for kinematic differential equations: -(k_ku*u + f_k)
    mass_matrix_full : Matrix
        The "mass matrix" for the u\'s and q\'s with dynamics and kinematics
    forcing_full : Matrix
        The "forcing vector" for the u\'s and q\'s with dynamics and kinematics
    explicit_kinematics : bool
        Boolean whether the mass matrices and forcing vectors should use the
        explicit form (default) or implicit form for kinematics.
        See the notes for more details.

    Notes
    =====

    The mass matrices and forcing vectors related to kinematic equations
    are given in the explicit form by default. In other words, the kinematic
    mass matrix is $\\mathbf{k_{k\\dot{q}}} = \\mathbf{I}$.
    In order to get the implicit form of those matrices/vectors, you can set the
    ``explicit_kinematics`` attribute to ``False``. So $\\mathbf{k_{k\\dot{q}}}$ is not
    necessarily an identity matrix. This can provide more compact equations for
    non-simple kinematics (see #22626).

    Examples
    ========

    This is a simple example for a one degree of freedom translational
    spring-mass-damper.

    In this example, we first need to do the kinematics.
    This involves creating generalized speeds and coordinates and their
    derivatives.
    Then we create a point and set its velocity in a frame.

        >>> from sympy import symbols
        >>> from sympy.physics.mechanics import dynamicsymbols, ReferenceFrame
        >>> from sympy.physics.mechanics import Point, Particle, KanesMethod
        >>> q, u = dynamicsymbols(\'q u\')
        >>> qd, ud = dynamicsymbols(\'q u\', 1)
        >>> m, c, k = symbols(\'m c k\')
        >>> N = ReferenceFrame(\'N\')
        >>> P = Point(\'P\')
        >>> P.set_vel(N, u * N.x)

    Next we need to arrange/store information in the way that KanesMethod
    requires.  The kinematic differential equations need to be stored in a
    dict.  A list of forces/torques must be constructed, where each entry in
    the list is a (Point, Vector) or (ReferenceFrame, Vector) tuple, where the
    Vectors represent the Force or Torque.
    Next a particle needs to be created, and it needs to have a point and mass
    assigned to it.
    Finally, a list of all bodies and particles needs to be created.

        >>> kd = [qd - u]
        >>> FL = [(P, (-k * q - c * u) * N.x)]
        >>> pa = Particle(\'pa\', P, m)
        >>> BL = [pa]

    Finally we can generate the equations of motion.
    First we create the KanesMethod object and supply an inertial frame,
    coordinates, generalized speeds, and the kinematic differential equations.
    Additional quantities such as configuration and motion constraints,
    dependent coordinates and speeds, and auxiliary speeds are also supplied
    here (see the online documentation).
    Next we form FR* and FR to complete: Fr + Fr* = 0.
    We have the equations of motion at this point.
    It makes sense to rearrange them though, so we calculate the mass matrix and
    the forcing terms, for E.o.M. in the form: [MM] udot = forcing, where MM is
    the mass matrix, udot is a vector of the time derivatives of the
    generalized speeds, and forcing is a vector representing "forcing" terms.

        >>> KM = KanesMethod(N, q_ind=[q], u_ind=[u], kd_eqs=kd)
        >>> (fr, frstar) = KM.kanes_equations(BL, FL)
        >>> MM = KM.mass_matrix
        >>> forcing = KM.forcing
        >>> rhs = MM.inv() * forcing
        >>> rhs
        Matrix([[(-c*u(t) - k*q(t))/m]])
        >>> KM.linearize(A_and_B=True)[0]
        Matrix([
        [   0,    1],
        [-k/m, -c/m]])

    Please look at the documentation pages for more information on how to
    perform linearization and how to deal with dependent coordinates & speeds,
    and how do deal with bringing non-contributing forces into evidence.

    '''
    explicit_kinematics: Incomplete
    def __init__(self, frame, q_ind, u_ind, kd_eqs: Incomplete | None = None, q_dependent: Incomplete | None = None, configuration_constraints: Incomplete | None = None, u_dependent: Incomplete | None = None, velocity_constraints: Incomplete | None = None, acceleration_constraints: Incomplete | None = None, u_auxiliary: Incomplete | None = None, bodies: Incomplete | None = None, forcelist: Incomplete | None = None, explicit_kinematics: bool = True) -> None:
        """Please read the online documentation. """
    def to_linearizer(self):
        """Returns an instance of the Linearizer class, initiated from the
        data in the KanesMethod class. This may be more desirable than using
        the linearize class method, as the Linearizer object will allow more
        efficient recalculation (i.e. about varying operating points)."""
    def linearize(self, *, new_method: Incomplete | None = None, **kwargs):
        """ Linearize the equations of motion about a symbolic operating point.

        Explanation
        ===========

        If kwarg A_and_B is False (default), returns M, A, B, r for the
        linearized form, M*[q', u']^T = A*[q_ind, u_ind]^T + B*r.

        If kwarg A_and_B is True, returns A, B, r for the linearized form
        dx = A*x + B*r, where x = [q_ind, u_ind]^T. Note that this is
        computationally intensive if there are many symbolic parameters. For
        this reason, it may be more desirable to use the default A_and_B=False,
        returning M, A, and B. Values may then be substituted in to these
        matrices, and the state space form found as
        A = P.T*M.inv()*A, B = P.T*M.inv()*B, where P = Linearizer.perm_mat.

        In both cases, r is found as all dynamicsymbols in the equations of
        motion that are not part of q, u, q', or u'. They are sorted in
        canonical form.

        The operating points may be also entered using the ``op_point`` kwarg.
        This takes a dictionary of {symbol: value}, or a an iterable of such
        dictionaries. The values may be numeric or symbolic. The more values
        you can specify beforehand, the faster this computation will run.

        For more documentation, please see the ``Linearizer`` class."""
    def kanes_equations(self, bodies: Incomplete | None = None, loads: Incomplete | None = None):
        """ Method to form Kane's equations, Fr + Fr* = 0.

        Explanation
        ===========

        Returns (Fr, Fr*). In the case where auxiliary generalized speeds are
        present (say, s auxiliary speeds, o generalized speeds, and m motion
        constraints) the length of the returned vectors will be o - m + s in
        length. The first o - m equations will be the constrained Kane's
        equations, then the s auxiliary Kane's equations. These auxiliary
        equations can be accessed with the auxiliary_eqs property.

        Parameters
        ==========

        bodies : iterable
            An iterable of all RigidBody's and Particle's in the system.
            A system must have at least one body.
        loads : iterable
            Takes in an iterable of (Particle, Vector) or (ReferenceFrame, Vector)
            tuples which represent the force at a point or torque on a frame.
            Must be either a non-empty iterable of tuples or None which corresponds
            to a system with no constraints.
        """
    def rhs(self, inv_method: Incomplete | None = None):
        """Returns the system's equations of motion in first order form. The
        output is the right hand side of::

           x' = |q'| =: f(q, u, r, p, t)
                |u'|

        The right hand side is what is needed by most numerical ODE
        integrators.

        Parameters
        ==========

        inv_method : str
            The specific sympy inverse matrix calculation method to use. For a
            list of valid methods, see
            :meth:`~sympy.matrices.matrices.MatrixBase.inv`

        """
    def kindiffdict(self):
        """Returns a dictionary mapping q' to u."""
    @property
    def auxiliary_eqs(self):
        """A matrix containing the auxiliary equations."""
    @property
    def mass_matrix_kin(self):
        '''The kinematic "mass matrix" $\\mathbf{k_{k\\dot{q}}}$ of the system.'''
    @property
    def forcing_kin(self):
        '''The kinematic "forcing vector" of the system.'''
    @property
    def mass_matrix(self):
        """The mass matrix of the system."""
    @property
    def forcing(self):
        """The forcing vector of the system."""
    @property
    def mass_matrix_full(self):
        """The mass matrix of the system, augmented by the kinematic
        differential equations in explicit or implicit form."""
    @property
    def forcing_full(self):
        """The forcing vector of the system, augmented by the kinematic
        differential equations in explicit or implicit form."""
    @property
    def q(self): ...
    @property
    def u(self): ...
    @property
    def bodylist(self): ...
    @property
    def forcelist(self): ...
    @property
    def bodies(self): ...
    @property
    def loads(self): ...
