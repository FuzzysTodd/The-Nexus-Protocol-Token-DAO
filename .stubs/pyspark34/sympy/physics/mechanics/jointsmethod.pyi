from _typeshed import Incomplete
from sympy.physics.mechanics.method import _Methods

__all__ = ['JointsMethod']

class JointsMethod(_Methods):
    '''Method for formulating the equations of motion using a set of interconnected bodies with joints.

    Parameters
    ==========

    newtonion : Body or ReferenceFrame
        The newtonion(inertial) frame.
    *joints : Joint
        The joints in the system

    Attributes
    ==========

    q, u : iterable
        Iterable of the generalized coordinates and speeds
    bodies : iterable
        Iterable of Body objects in the system.
    loads : iterable
        Iterable of (Point, vector) or (ReferenceFrame, vector) tuples
        describing the forces on the system.
    mass_matrix : Matrix, shape(n, n)
        The system\'s mass matrix
    forcing : Matrix, shape(n, 1)
        The system\'s forcing vector
    mass_matrix_full : Matrix, shape(2*n, 2*n)
        The "mass matrix" for the u\'s and q\'s
    forcing_full : Matrix, shape(2*n, 1)
        The "forcing vector" for the u\'s and q\'s
    method : KanesMethod or Lagrange\'s method
        Method\'s object.
    kdes : iterable
        Iterable of kde in they system.

    Examples
    ========

    This is a simple example for a one degree of freedom translational
    spring-mass-damper.

    >>> from sympy import symbols
    >>> from sympy.physics.mechanics import Body, JointsMethod, PrismaticJoint
    >>> from sympy.physics.vector import dynamicsymbols
    >>> c, k = symbols(\'c k\')
    >>> x, v = dynamicsymbols(\'x v\')
    >>> wall = Body(\'W\')
    >>> body = Body(\'B\')
    >>> J = PrismaticJoint(\'J\', wall, body, coordinates=x, speeds=v)
    >>> wall.apply_force(c*v*wall.x, reaction_body=body)
    >>> wall.apply_force(k*x*wall.x, reaction_body=body)
    >>> method = JointsMethod(wall, J)
    >>> method.form_eoms()
    Matrix([[-B_mass*Derivative(v(t), t) - c*v(t) - k*x(t)]])
    >>> M = method.mass_matrix_full
    >>> F = method.forcing_full
    >>> rhs = M.LUsolve(F)
    >>> rhs
    Matrix([
    [                     v(t)],
    [(-c*v(t) - k*x(t))/B_mass]])

    Notes
    =====

    ``JointsMethod`` currently only works with systems that do not have any
    configuration or motion constraints.

    '''
    frame: Incomplete
    def __init__(self, newtonion, *joints) -> None: ...
    @property
    def bodies(self):
        """List of bodies in they system."""
    @property
    def loads(self):
        """List of loads on the system."""
    @property
    def q(self):
        """List of the generalized coordinates."""
    @property
    def u(self):
        """List of the generalized speeds."""
    @property
    def kdes(self):
        """List of the generalized coordinates."""
    @property
    def forcing_full(self):
        '''The "forcing vector" for the u\'s and q\'s.'''
    @property
    def mass_matrix_full(self):
        '''The "mass matrix" for the u\'s and q\'s.'''
    @property
    def mass_matrix(self):
        """The system's mass matrix."""
    @property
    def forcing(self):
        """The system's forcing vector."""
    @property
    def method(self):
        """Object of method used to form equations of systems."""
    def form_eoms(self, method=...):
        """Method to form system's equation of motions.

        Parameters
        ==========

        method : Class
            Class name of method.

        Returns
        ========

        Matrix
            Vector of equations of motions.

        Examples
        ========

        This is a simple example for a one degree of freedom translational
        spring-mass-damper.

        >>> from sympy import S, symbols
        >>> from sympy.physics.mechanics import LagrangesMethod, dynamicsymbols, Body
        >>> from sympy.physics.mechanics import PrismaticJoint, JointsMethod
        >>> q = dynamicsymbols('q')
        >>> qd = dynamicsymbols('q', 1)
        >>> m, k, b = symbols('m k b')
        >>> wall = Body('W')
        >>> part = Body('P', mass=m)
        >>> part.potential_energy = k * q**2 / S(2)
        >>> J = PrismaticJoint('J', wall, part, coordinates=q, speeds=qd)
        >>> wall.apply_force(b * qd * wall.x, reaction_body=part)
        >>> method = JointsMethod(wall, J)
        >>> method.form_eoms(LagrangesMethod)
        Matrix([[b*Derivative(q(t), t) + k*q(t) + m*Derivative(q(t), (t, 2))]])

        We can also solve for the states using the 'rhs' method.

        >>> method.rhs()
        Matrix([
        [                Derivative(q(t), t)],
        [(-b*Derivative(q(t), t) - k*q(t))/m]])

        """
    def rhs(self, inv_method: Incomplete | None = None):
        """Returns equations that can be solved numerically.

        Parameters
        ==========

        inv_method : str
            The specific sympy inverse matrix calculation method to use. For a
            list of valid methods, see
            :meth:`~sympy.matrices.matrices.MatrixBase.inv`

        Returns
        ========

        Matrix
            Numerically solvable equations.

        See Also
        ========

        sympy.physics.mechanics.kane.KanesMethod.rhs:
            KanesMethod's rhs function.
        sympy.physics.mechanics.lagrange.LagrangesMethod.rhs:
            LagrangesMethod's rhs function.

        """
