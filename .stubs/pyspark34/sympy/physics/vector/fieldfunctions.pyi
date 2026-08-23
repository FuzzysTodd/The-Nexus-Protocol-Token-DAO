__all__ = ['curl', 'divergence', 'gradient', 'is_conservative', 'is_solenoidal', 'scalar_potential', 'scalar_potential_difference']

def curl(vect, frame):
    """
    Returns the curl of a vector field computed wrt the coordinate
    symbols of the given frame.

    Parameters
    ==========

    vect : Vector
        The vector operand

    frame : ReferenceFrame
        The reference frame to calculate the curl in

    Examples
    ========

    >>> from sympy.physics.vector import ReferenceFrame
    >>> from sympy.physics.vector import curl
    >>> R = ReferenceFrame('R')
    >>> v1 = R[1]*R[2]*R.x + R[0]*R[2]*R.y + R[0]*R[1]*R.z
    >>> curl(v1, R)
    0
    >>> v2 = R[0]*R[1]*R[2]*R.x
    >>> curl(v2, R)
    R_x*R_y*R.y - R_x*R_z*R.z

    """
def divergence(vect, frame):
    """
    Returns the divergence of a vector field computed wrt the coordinate
    symbols of the given frame.

    Parameters
    ==========

    vect : Vector
        The vector operand

    frame : ReferenceFrame
        The reference frame to calculate the divergence in

    Examples
    ========

    >>> from sympy.physics.vector import ReferenceFrame
    >>> from sympy.physics.vector import divergence
    >>> R = ReferenceFrame('R')
    >>> v1 = R[0]*R[1]*R[2] * (R.x+R.y+R.z)
    >>> divergence(v1, R)
    R_x*R_y + R_x*R_z + R_y*R_z
    >>> v2 = 2*R[1]*R[2]*R.y
    >>> divergence(v2, R)
    2*R_z

    """
def gradient(scalar, frame):
    """
    Returns the vector gradient of a scalar field computed wrt the
    coordinate symbols of the given frame.

    Parameters
    ==========

    scalar : sympifiable
        The scalar field to take the gradient of

    frame : ReferenceFrame
        The frame to calculate the gradient in

    Examples
    ========

    >>> from sympy.physics.vector import ReferenceFrame
    >>> from sympy.physics.vector import gradient
    >>> R = ReferenceFrame('R')
    >>> s1 = R[0]*R[1]*R[2]
    >>> gradient(s1, R)
    R_y*R_z*R.x + R_x*R_z*R.y + R_x*R_y*R.z
    >>> s2 = 5*R[0]**2*R[2]
    >>> gradient(s2, R)
    10*R_x*R_z*R.x + 5*R_x**2*R.z

    """
def is_conservative(field):
    """
    Checks if a field is conservative.

    Parameters
    ==========

    field : Vector
        The field to check for conservative property

    Examples
    ========

    >>> from sympy.physics.vector import ReferenceFrame
    >>> from sympy.physics.vector import is_conservative
    >>> R = ReferenceFrame('R')
    >>> is_conservative(R[1]*R[2]*R.x + R[0]*R[2]*R.y + R[0]*R[1]*R.z)
    True
    >>> is_conservative(R[2] * R.y)
    False

    """
def is_solenoidal(field):
    """
    Checks if a field is solenoidal.

    Parameters
    ==========

    field : Vector
        The field to check for solenoidal property

    Examples
    ========

    >>> from sympy.physics.vector import ReferenceFrame
    >>> from sympy.physics.vector import is_solenoidal
    >>> R = ReferenceFrame('R')
    >>> is_solenoidal(R[1]*R[2]*R.x + R[0]*R[2]*R.y + R[0]*R[1]*R.z)
    True
    >>> is_solenoidal(R[1] * R.y)
    False

    """
def scalar_potential(field, frame):
    """
    Returns the scalar potential function of a field in a given frame
    (without the added integration constant).

    Parameters
    ==========

    field : Vector
        The vector field whose scalar potential function is to be
        calculated

    frame : ReferenceFrame
        The frame to do the calculation in

    Examples
    ========

    >>> from sympy.physics.vector import ReferenceFrame
    >>> from sympy.physics.vector import scalar_potential, gradient
    >>> R = ReferenceFrame('R')
    >>> scalar_potential(R.z, R) == R[2]
    True
    >>> scalar_field = 2*R[0]**2*R[1]*R[2]
    >>> grad_field = gradient(scalar_field, R)
    >>> scalar_potential(grad_field, R)
    2*R_x**2*R_y*R_z

    """
def scalar_potential_difference(field, frame, point1, point2, origin):
    """
    Returns the scalar potential difference between two points in a
    certain frame, wrt a given field.

    If a scalar field is provided, its values at the two points are
    considered. If a conservative vector field is provided, the values
    of its scalar potential function at the two points are used.

    Returns (potential at position 2) - (potential at position 1)

    Parameters
    ==========

    field : Vector/sympyfiable
        The field to calculate wrt

    frame : ReferenceFrame
        The frame to do the calculations in

    point1 : Point
        The initial Point in given frame

    position2 : Point
        The second Point in the given frame

    origin : Point
        The Point to use as reference point for position vector
        calculation

    Examples
    ========

    >>> from sympy.physics.vector import ReferenceFrame, Point
    >>> from sympy.physics.vector import scalar_potential_difference
    >>> R = ReferenceFrame('R')
    >>> O = Point('O')
    >>> P = O.locatenew('P', R[0]*R.x + R[1]*R.y + R[2]*R.z)
    >>> vectfield = 4*R[0]*R[1]*R.x + 2*R[0]**2*R.y
    >>> scalar_potential_difference(vectfield, R, O, P, O)
    2*R_x**2*R_y
    >>> Q = O.locatenew('O', 3*R.x + R.y + 2*R.z)
    >>> scalar_potential_difference(vectfield, R, P, Q, O)
    -2*R_x**2*R_y + 18

    """
