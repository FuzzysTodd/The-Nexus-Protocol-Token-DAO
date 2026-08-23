from .printing import init_vprinting as init_vprinting, vlatex as vlatex, vpprint as vpprint, vprint as vprint, vsprint as vsprint
from _typeshed import Incomplete

__all__ = ['cross', 'dot', 'express', 'time_derivative', 'outer', 'kinematic_equations', 'get_motion_params', 'partial_velocity', 'dynamicsymbols', 'vprint', 'vsprint', 'vpprint', 'vlatex', 'init_vprinting']

def cross(vec1, vec2):
    """Cross product convenience wrapper for Vector.cross(): 
"""
def dot(vec1, vec2):
    """Dot product convenience wrapper for Vector.dot(): 
"""
def express(expr, frame, frame2: Incomplete | None = None, variables: bool = False):
    """
    Global function for 'express' functionality.

    Re-expresses a Vector, scalar(sympyfiable) or Dyadic in given frame.

    Refer to the local methods of Vector and Dyadic for details.
    If 'variables' is True, then the coordinate variables (CoordinateSym
    instances) of other frames present in the vector/scalar field or
    dyadic expression are also substituted in terms of the base scalars of
    this frame.

    Parameters
    ==========

    expr : Vector/Dyadic/scalar(sympyfiable)
        The expression to re-express in ReferenceFrame 'frame'

    frame: ReferenceFrame
        The reference frame to express expr in

    frame2 : ReferenceFrame
        The other frame required for re-expression(only for Dyadic expr)

    variables : boolean
        Specifies whether to substitute the coordinate variables present
        in expr, in terms of those of frame

    Examples
    ========

    >>> from sympy.physics.vector import ReferenceFrame, outer, dynamicsymbols
    >>> from sympy.physics.vector import init_vprinting
    >>> init_vprinting(pretty_print=False)
    >>> N = ReferenceFrame('N')
    >>> q = dynamicsymbols('q')
    >>> B = N.orientnew('B', 'Axis', [q, N.z])
    >>> d = outer(N.x, N.x)
    >>> from sympy.physics.vector import express
    >>> express(d, B, N)
    cos(q)*(B.x|N.x) - sin(q)*(B.y|N.x)
    >>> express(B.x, N)
    cos(q)*N.x + sin(q)*N.y
    >>> express(N[0], B, variables=True)
    B_x*cos(q) - B_y*sin(q)

    """
def time_derivative(expr, frame, order: int = 1):
    """
    Calculate the time derivative of a vector/scalar field function
    or dyadic expression in given frame.

    References
    ==========

    https://en.wikipedia.org/wiki/Rotating_reference_frame#Time_derivatives_in_the_two_frames

    Parameters
    ==========

    expr : Vector/Dyadic/sympifyable
        The expression whose time derivative is to be calculated

    frame : ReferenceFrame
        The reference frame to calculate the time derivative in

    order : integer
        The order of the derivative to be calculated

    Examples
    ========

    >>> from sympy.physics.vector import ReferenceFrame, dynamicsymbols
    >>> from sympy.physics.vector import init_vprinting
    >>> init_vprinting(pretty_print=False)
    >>> from sympy import Symbol
    >>> q1 = Symbol('q1')
    >>> u1 = dynamicsymbols('u1')
    >>> N = ReferenceFrame('N')
    >>> A = N.orientnew('A', 'Axis', [q1, N.x])
    >>> v = u1 * N.x
    >>> A.set_ang_vel(N, 10*A.x)
    >>> from sympy.physics.vector import time_derivative
    >>> time_derivative(v, N)
    u1'*N.x
    >>> time_derivative(u1*A[0], N)
    N_x*u1'
    >>> B = N.orientnew('B', 'Axis', [u1, N.z])
    >>> from sympy.physics.vector import outer
    >>> d = outer(N.x, N.x)
    >>> time_derivative(d, B)
    - u1'*(N.y|N.x) - u1'*(N.x|N.y)

    """
def outer(vec1, vec2):
    """Outer product convenience wrapper for Vector.outer():
"""
def kinematic_equations(speeds, coords, rot_type, rot_order: str = ''):
    """Gives equations relating the qdot's to u's for a rotation type.

    Supply rotation type and order as in orient. Speeds are assumed to be
    body-fixed; if we are defining the orientation of B in A using by rot_type,
    the angular velocity of B in A is assumed to be in the form: speed[0]*B.x +
    speed[1]*B.y + speed[2]*B.z

    Parameters
    ==========

    speeds : list of length 3
        The body fixed angular velocity measure numbers.
    coords : list of length 3 or 4
        The coordinates used to define the orientation of the two frames.
    rot_type : str
        The type of rotation used to create the equations. Body, Space, or
        Quaternion only
    rot_order : str or int
        If applicable, the order of a series of rotations.

    Examples
    ========

    >>> from sympy.physics.vector import dynamicsymbols
    >>> from sympy.physics.vector import kinematic_equations, vprint
    >>> u1, u2, u3 = dynamicsymbols('u1 u2 u3')
    >>> q1, q2, q3 = dynamicsymbols('q1 q2 q3')
    >>> vprint(kinematic_equations([u1,u2,u3], [q1,q2,q3], 'body', '313'),
    ...     order=None)
    [-(u1*sin(q3) + u2*cos(q3))/sin(q2) + q1', -u1*cos(q3) + u2*sin(q3) + q2', (u1*sin(q3) + u2*cos(q3))*cos(q2)/sin(q2) - u3 + q3']

    """
def get_motion_params(frame, **kwargs):
    """
    Returns the three motion parameters - (acceleration, velocity, and
    position) as vectorial functions of time in the given frame.

    If a higher order differential function is provided, the lower order
    functions are used as boundary conditions. For example, given the
    acceleration, the velocity and position parameters are taken as
    boundary conditions.

    The values of time at which the boundary conditions are specified
    are taken from timevalue1(for position boundary condition) and
    timevalue2(for velocity boundary condition).

    If any of the boundary conditions are not provided, they are taken
    to be zero by default (zero vectors, in case of vectorial inputs). If
    the boundary conditions are also functions of time, they are converted
    to constants by substituting the time values in the dynamicsymbols._t
    time Symbol.

    This function can also be used for calculating rotational motion
    parameters. Have a look at the Parameters and Examples for more clarity.

    Parameters
    ==========

    frame : ReferenceFrame
        The frame to express the motion parameters in

    acceleration : Vector
        Acceleration of the object/frame as a function of time

    velocity : Vector
        Velocity as function of time or as boundary condition
        of velocity at time = timevalue1

    position : Vector
        Velocity as function of time or as boundary condition
        of velocity at time = timevalue1

    timevalue1 : sympyfiable
        Value of time for position boundary condition

    timevalue2 : sympyfiable
        Value of time for velocity boundary condition

    Examples
    ========

    >>> from sympy.physics.vector import ReferenceFrame, get_motion_params, dynamicsymbols
    >>> from sympy.physics.vector import init_vprinting
    >>> init_vprinting(pretty_print=False)
    >>> from sympy import symbols
    >>> R = ReferenceFrame('R')
    >>> v1, v2, v3 = dynamicsymbols('v1 v2 v3')
    >>> v = v1*R.x + v2*R.y + v3*R.z
    >>> get_motion_params(R, position = v)
    (v1''*R.x + v2''*R.y + v3''*R.z, v1'*R.x + v2'*R.y + v3'*R.z, v1*R.x + v2*R.y + v3*R.z)
    >>> a, b, c = symbols('a b c')
    >>> v = a*R.x + b*R.y + c*R.z
    >>> get_motion_params(R, velocity = v)
    (0, a*R.x + b*R.y + c*R.z, a*t*R.x + b*t*R.y + c*t*R.z)
    >>> parameters = get_motion_params(R, acceleration = v)
    >>> parameters[1]
    a*t*R.x + b*t*R.y + c*t*R.z
    >>> parameters[2]
    a*t**2/2*R.x + b*t**2/2*R.y + c*t**2/2*R.z

    """
def partial_velocity(vel_vecs, gen_speeds, frame):
    """Returns a list of partial velocities with respect to the provided
    generalized speeds in the given reference frame for each of the supplied
    velocity vectors.

    The output is a list of lists. The outer list has a number of elements
    equal to the number of supplied velocity vectors. The inner lists are, for
    each velocity vector, the partial derivatives of that velocity vector with
    respect to the generalized speeds supplied.

    Parameters
    ==========

    vel_vecs : iterable
        An iterable of velocity vectors (angular or linear).
    gen_speeds : iterable
        An iterable of generalized speeds.
    frame : ReferenceFrame
        The reference frame that the partial derivatives are going to be taken
        in.

    Examples
    ========

    >>> from sympy.physics.vector import Point, ReferenceFrame
    >>> from sympy.physics.vector import dynamicsymbols
    >>> from sympy.physics.vector import partial_velocity
    >>> u = dynamicsymbols('u')
    >>> N = ReferenceFrame('N')
    >>> P = Point('P')
    >>> P.set_vel(N, u * N.x)
    >>> vel_vecs = [P.vel(N)]
    >>> gen_speeds = [u]
    >>> partial_velocity(vel_vecs, gen_speeds, N)
    [[N.x]]

    """
def dynamicsymbols(names, level: int = 0, **assumptions):
    """Uses symbols and Function for functions of time.

    Creates a SymPy UndefinedFunction, which is then initialized as a function
    of a variable, the default being Symbol('t').

    Parameters
    ==========

    names : str
        Names of the dynamic symbols you want to create; works the same way as
        inputs to symbols
    level : int
        Level of differentiation of the returned function; d/dt once of t,
        twice of t, etc.
    assumptions :
        - real(bool) : This is used to set the dynamicsymbol as real,
                    by default is False.
        - positive(bool) : This is used to set the dynamicsymbol as positive,
                    by default is False.
        - commutative(bool) : This is used to set the commutative property of
                    a dynamicsymbol, by default is True.
        - integer(bool) : This is used to set the dynamicsymbol as integer,
                    by default is False.

    Examples
    ========

    >>> from sympy.physics.vector import dynamicsymbols
    >>> from sympy import diff, Symbol
    >>> q1 = dynamicsymbols('q1')
    >>> q1
    q1(t)
    >>> q2 = dynamicsymbols('q2', real=True)
    >>> q2.is_real
    True
    >>> q3 = dynamicsymbols('q3', positive=True)
    >>> q3.is_positive
    True
    >>> q4, q5 = dynamicsymbols('q4,q5', commutative=False)
    >>> bool(q4*q5 != q5*q4)
    True
    >>> q6 = dynamicsymbols('q6', integer=True)
    >>> q6.is_integer
    True
    >>> diff(q1, Symbol('t'))
    Derivative(q1(t), t)

    """
