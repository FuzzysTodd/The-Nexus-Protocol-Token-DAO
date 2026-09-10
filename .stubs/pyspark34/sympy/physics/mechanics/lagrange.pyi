from _typeshed import Incomplete
from sympy.physics.mechanics.method import _Methods

__all__ = ['LagrangesMethod']

class LagrangesMethod(_Methods):
    '''Lagrange\'s method object.

    Explanation
    ===========

    This object generates the equations of motion in a two step procedure. The
    first step involves the initialization of LagrangesMethod by supplying the
    Lagrangian and the generalized coordinates, at the bare minimum. If there
    are any constraint equations, they can be supplied as keyword arguments.
    The Lagrange multipliers are automatically generated and are equal in
    number to the constraint equations. Similarly any non-conservative forces
    can be supplied in an iterable (as described below and also shown in the
    example) along with a ReferenceFrame. This is also discussed further in the
    __init__ method.

    Attributes
    ==========

    q, u : Matrix
        Matrices of the generalized coordinates and speeds
    loads : iterable
        Iterable of (Point, vector) or (ReferenceFrame, vector) tuples
        describing the forces on the system.
    bodies : iterable
        Iterable containing the rigid bodies and particles of the system.
    mass_matrix : Matrix
        The system\'s mass matrix
    forcing : Matrix
        The system\'s forcing vector
    mass_matrix_full : Matrix
        The "mass matrix" for the qdot\'s, qdoubledot\'s, and the
        lagrange multipliers (lam)
    forcing_full : Matrix
        The forcing vector for the qdot\'s, qdoubledot\'s and
        lagrange multipliers (lam)

    Examples
    ========

    This is a simple example for a one degree of freedom translational
    spring-mass-damper.

    In this example, we first need to do the kinematics.
    This involves creating generalized coordinates and their derivatives.
    Then we create a point and set its velocity in a frame.

        >>> from sympy.physics.mechanics import LagrangesMethod, Lagrangian
        >>> from sympy.physics.mechanics import ReferenceFrame, Particle, Point
        >>> from sympy.physics.mechanics import dynamicsymbols
        >>> from sympy import symbols
        >>> q = dynamicsymbols(\'q\')
        >>> qd = dynamicsymbols(\'q\', 1)
        >>> m, k, b = symbols(\'m k b\')
        >>> N = ReferenceFrame(\'N\')
        >>> P = Point(\'P\')
        >>> P.set_vel(N, qd * N.x)

    We need to then prepare the information as required by LagrangesMethod to
    generate equations of motion.
    First we create the Particle, which has a point attached to it.
    Following this the lagrangian is created from the kinetic and potential
    energies.
    Then, an iterable of nonconservative forces/torques must be constructed,
    where each item is a (Point, Vector) or (ReferenceFrame, Vector) tuple,
    with the Vectors representing the nonconservative forces or torques.

        >>> Pa = Particle(\'Pa\', P, m)
        >>> Pa.potential_energy = k * q**2 / 2.0
        >>> L = Lagrangian(N, Pa)
        >>> fl = [(P, -b * qd * N.x)]

    Finally we can generate the equations of motion.
    First we create the LagrangesMethod object. To do this one must supply
    the Lagrangian, and the generalized coordinates. The constraint equations,
    the forcelist, and the inertial frame may also be provided, if relevant.
    Next we generate Lagrange\'s equations of motion, such that:
    Lagrange\'s equations of motion = 0.
    We have the equations of motion at this point.

        >>> l = LagrangesMethod(L, [q], forcelist = fl, frame = N)
        >>> print(l.form_lagranges_equations())
        Matrix([[b*Derivative(q(t), t) + 1.0*k*q(t) + m*Derivative(q(t), (t, 2))]])

    We can also solve for the states using the \'rhs\' method.

        >>> print(l.rhs())
        Matrix([[Derivative(q(t), t)], [(-b*Derivative(q(t), t) - 1.0*k*q(t))/m]])

    Please refer to the docstrings on each method for more details.
    '''
    eom: Incomplete
    lam_coeffs: Incomplete
    inertial: Incomplete
    lam_vec: Incomplete
    coneqs: Incomplete
    def __init__(self, Lagrangian, qs, forcelist: Incomplete | None = None, bodies: Incomplete | None = None, frame: Incomplete | None = None, hol_coneqs: Incomplete | None = None, nonhol_coneqs: Incomplete | None = None) -> None:
        """Supply the following for the initialization of LagrangesMethod.

        Lagrangian : Sympifyable

        qs : array_like
            The generalized coordinates

        hol_coneqs : array_like, optional
            The holonomic constraint equations

        nonhol_coneqs : array_like, optional
            The nonholonomic constraint equations

        forcelist : iterable, optional
            Takes an iterable of (Point, Vector) or (ReferenceFrame, Vector)
            tuples which represent the force at a point or torque on a frame.
            This feature is primarily to account for the nonconservative forces
            and/or moments.

        bodies : iterable, optional
            Takes an iterable containing the rigid bodies and particles of the
            system.

        frame : ReferenceFrame, optional
            Supply the inertial frame. This is used to determine the
            generalized forces due to non-conservative forces.
        """
    def form_lagranges_equations(self):
        """Method to form Lagrange's equations of motion.

        Returns a vector of equations of motion using Lagrange's equations of
        the second kind.
        """
    @property
    def mass_matrix(self):
        """Returns the mass matrix, which is augmented by the Lagrange
        multipliers, if necessary.

        Explanation
        ===========

        If the system is described by 'n' generalized coordinates and there are
        no constraint equations then an n X n matrix is returned.

        If there are 'n' generalized coordinates and 'm' constraint equations
        have been supplied during initialization then an n X (n+m) matrix is
        returned. The (n + m - 1)th and (n + m)th columns contain the
        coefficients of the Lagrange multipliers.
        """
    @property
    def mass_matrix_full(self):
        """Augments the coefficients of qdots to the mass_matrix."""
    @property
    def forcing(self):
        """Returns the forcing vector from 'lagranges_equations' method."""
    @property
    def forcing_full(self):
        """Augments qdots to the forcing vector above."""
    def to_linearizer(self, q_ind: Incomplete | None = None, qd_ind: Incomplete | None = None, q_dep: Incomplete | None = None, qd_dep: Incomplete | None = None):
        """Returns an instance of the Linearizer class, initiated from the
        data in the LagrangesMethod class. This may be more desirable than using
        the linearize class method, as the Linearizer object will allow more
        efficient recalculation (i.e. about varying operating points).

        Parameters
        ==========

        q_ind, qd_ind : array_like, optional
            The independent generalized coordinates and speeds.
        q_dep, qd_dep : array_like, optional
            The dependent generalized coordinates and speeds.
        """
    def linearize(self, q_ind: Incomplete | None = None, qd_ind: Incomplete | None = None, q_dep: Incomplete | None = None, qd_dep: Incomplete | None = None, **kwargs):
        """Linearize the equations of motion about a symbolic operating point.

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
    def solve_multipliers(self, op_point: Incomplete | None = None, sol_type: str = 'dict'):
        """Solves for the values of the lagrange multipliers symbolically at
        the specified operating point.

        Parameters
        ==========

        op_point : dict or iterable of dicts, optional
            Point at which to solve at. The operating point is specified as
            a dictionary or iterable of dictionaries of {symbol: value}. The
            value may be numeric or symbolic itself.

        sol_type : str, optional
            Solution return type. Valid options are:
            - 'dict': A dict of {symbol : value} (default)
            - 'Matrix': An ordered column matrix of the solution
        """
    def rhs(self, inv_method: Incomplete | None = None, **kwargs):
        """Returns equations that can be solved numerically.

        Parameters
        ==========

        inv_method : str
            The specific sympy inverse matrix calculation method to use. For a
            list of valid methods, see
            :meth:`~sympy.matrices.matrices.MatrixBase.inv`
        """
    @property
    def q(self): ...
    @property
    def u(self): ...
    @property
    def bodies(self): ...
    @property
    def forcelist(self): ...
    @property
    def loads(self): ...
