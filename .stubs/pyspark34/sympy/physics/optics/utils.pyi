from _typeshed import Incomplete

__all__ = ['refraction_angle', 'deviation', 'fresnel_coefficients', 'brewster_angle', 'critical_angle', 'lens_makers_formula', 'mirror_formula', 'lens_formula', 'hyperfocal_distance', 'transverse_magnification']

def refraction_angle(incident, medium1, medium2, normal: Incomplete | None = None, plane: Incomplete | None = None):
    """
    This function calculates transmitted vector after refraction at planar
    surface. ``medium1`` and ``medium2`` can be ``Medium`` or any sympifiable object.
    If ``incident`` is a number then treated as angle of incidence (in radians)
    in which case refraction angle is returned.

    If ``incident`` is an object of `Ray3D`, `normal` also has to be an instance
    of `Ray3D` in order to get the output as a `Ray3D`. Please note that if
    plane of separation is not provided and normal is an instance of `Ray3D`,
    ``normal`` will be assumed to be intersecting incident ray at the plane of
    separation. This will not be the case when `normal` is a `Matrix` or
    any other sequence.
    If ``incident`` is an instance of `Ray3D` and `plane` has not been provided
    and ``normal`` is not `Ray3D`, output will be a `Matrix`.

    Parameters
    ==========

    incident : Matrix, Ray3D, sequence or a number
        Incident vector or angle of incidence
    medium1 : sympy.physics.optics.medium.Medium or sympifiable
        Medium 1 or its refractive index
    medium2 : sympy.physics.optics.medium.Medium or sympifiable
        Medium 2 or its refractive index
    normal : Matrix, Ray3D, or sequence
        Normal vector
    plane : Plane
        Plane of separation of the two media.

    Returns
    =======

    Returns an angle of refraction or a refracted ray depending on inputs.

    Examples
    ========

    >>> from sympy.physics.optics import refraction_angle
    >>> from sympy.geometry import Point3D, Ray3D, Plane
    >>> from sympy.matrices import Matrix
    >>> from sympy import symbols, pi
    >>> n = Matrix([0, 0, 1])
    >>> P = Plane(Point3D(0, 0, 0), normal_vector=[0, 0, 1])
    >>> r1 = Ray3D(Point3D(-1, -1, 1), Point3D(0, 0, 0))
    >>> refraction_angle(r1, 1, 1, n)
    Matrix([
    [ 1],
    [ 1],
    [-1]])
    >>> refraction_angle(r1, 1, 1, plane=P)
    Ray3D(Point3D(0, 0, 0), Point3D(1, 1, -1))

    With different index of refraction of the two media

    >>> n1, n2 = symbols('n1, n2')
    >>> refraction_angle(r1, n1, n2, n)
    Matrix([
    [                                n1/n2],
    [                                n1/n2],
    [-sqrt(3)*sqrt(-2*n1**2/(3*n2**2) + 1)]])
    >>> refraction_angle(r1, n1, n2, plane=P)
    Ray3D(Point3D(0, 0, 0), Point3D(n1/n2, n1/n2, -sqrt(3)*sqrt(-2*n1**2/(3*n2**2) + 1)))
    >>> round(refraction_angle(pi/6, 1.2, 1.5), 5)
    0.41152
    """
def fresnel_coefficients(angle_of_incidence, medium1, medium2):
    """
    This function uses Fresnel equations to calculate reflection and
    transmission coefficients. Those are obtained for both polarisations
    when the electric field vector is in the plane of incidence (labelled 'p')
    and when the electric field vector is perpendicular to the plane of
    incidence (labelled 's'). There are four real coefficients unless the
    incident ray reflects in total internal in which case there are two complex
    ones. Angle of incidence is the angle between the incident ray and the
    surface normal. ``medium1`` and ``medium2`` can be ``Medium`` or any
    sympifiable object.

    Parameters
    ==========

    angle_of_incidence : sympifiable

    medium1 : Medium or sympifiable
        Medium 1 or its refractive index

    medium2 : Medium or sympifiable
        Medium 2 or its refractive index

    Returns
    =======

    Returns a list with four real Fresnel coefficients:
    [reflection p (TM), reflection s (TE),
    transmission p (TM), transmission s (TE)]
    If the ray is undergoes total internal reflection then returns a
    list of two complex Fresnel coefficients:
    [reflection p (TM), reflection s (TE)]

    Examples
    ========

    >>> from sympy.physics.optics import fresnel_coefficients
    >>> fresnel_coefficients(0.3, 1, 2)
    [0.317843553417859, -0.348645229818821,
            0.658921776708929, 0.651354770181179]
    >>> fresnel_coefficients(0.6, 2, 1)
    [-0.235625382192159 - 0.971843958291041*I,
             0.816477005968898 - 0.577377951366403*I]

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Fresnel_equations
    """
def deviation(incident, medium1, medium2, normal: Incomplete | None = None, plane: Incomplete | None = None):
    """
    This function calculates the angle of deviation of a ray
    due to refraction at planar surface.

    Parameters
    ==========

    incident : Matrix, Ray3D, sequence or float
        Incident vector or angle of incidence
    medium1 : sympy.physics.optics.medium.Medium or sympifiable
        Medium 1 or its refractive index
    medium2 : sympy.physics.optics.medium.Medium or sympifiable
        Medium 2 or its refractive index
    normal : Matrix, Ray3D, or sequence
        Normal vector
    plane : Plane
        Plane of separation of the two media.

    Returns angular deviation between incident and refracted rays

    Examples
    ========

    >>> from sympy.physics.optics import deviation
    >>> from sympy.geometry import Point3D, Ray3D, Plane
    >>> from sympy.matrices import Matrix
    >>> from sympy import symbols
    >>> n1, n2 = symbols('n1, n2')
    >>> n = Matrix([0, 0, 1])
    >>> P = Plane(Point3D(0, 0, 0), normal_vector=[0, 0, 1])
    >>> r1 = Ray3D(Point3D(-1, -1, 1), Point3D(0, 0, 0))
    >>> deviation(r1, 1, 1, n)
    0
    >>> deviation(r1, n1, n2, plane=P)
    -acos(-sqrt(-2*n1**2/(3*n2**2) + 1)) + acos(-sqrt(3)/3)
    >>> round(deviation(0.1, 1.2, 1.5), 5)
    -0.02005
    """
def brewster_angle(medium1, medium2):
    """
    This function calculates the Brewster's angle of incidence to Medium 2 from
    Medium 1 in radians.

    Parameters
    ==========

    medium 1 : Medium or sympifiable
        Refractive index of Medium 1
    medium 2 : Medium or sympifiable
        Refractive index of Medium 1

    Examples
    ========

    >>> from sympy.physics.optics import brewster_angle
    >>> brewster_angle(1, 1.33)
    0.926093295503462

    """
def critical_angle(medium1, medium2):
    """
    This function calculates the critical angle of incidence (marking the onset
    of total internal) to Medium 2 from Medium 1 in radians.

    Parameters
    ==========

    medium 1 : Medium or sympifiable
        Refractive index of Medium 1.
    medium 2 : Medium or sympifiable
        Refractive index of Medium 1.

    Examples
    ========

    >>> from sympy.physics.optics import critical_angle
    >>> critical_angle(1.33, 1)
    0.850908514477849

    """
def lens_makers_formula(n_lens, n_surr, r1, r2, d: int = 0):
    """
    This function calculates focal length of a lens.
    It follows cartesian sign convention.

    Parameters
    ==========

    n_lens : Medium or sympifiable
        Index of refraction of lens.
    n_surr : Medium or sympifiable
        Index of reflection of surrounding.
    r1 : sympifiable
        Radius of curvature of first surface.
    r2 : sympifiable
        Radius of curvature of second surface.
    d : sympifiable, optional
        Thickness of lens, default value is 0.

    Examples
    ========

    >>> from sympy.physics.optics import lens_makers_formula
    >>> from sympy import S
    >>> lens_makers_formula(1.33, 1, 10, -10)
    15.1515151515151
    >>> lens_makers_formula(1.2, 1, 10, S.Infinity)
    50.0000000000000
    >>> lens_makers_formula(1.33, 1, 10, -10, d=1)
    15.3418463277618

    """
def mirror_formula(focal_length: Incomplete | None = None, u: Incomplete | None = None, v: Incomplete | None = None):
    """
    This function provides one of the three parameters
    when two of them are supplied.
    This is valid only for paraxial rays.

    Parameters
    ==========

    focal_length : sympifiable
        Focal length of the mirror.
    u : sympifiable
        Distance of object from the pole on
        the principal axis.
    v : sympifiable
        Distance of the image from the pole
        on the principal axis.

    Examples
    ========

    >>> from sympy.physics.optics import mirror_formula
    >>> from sympy.abc import f, u, v
    >>> mirror_formula(focal_length=f, u=u)
    f*u/(-f + u)
    >>> mirror_formula(focal_length=f, v=v)
    f*v/(-f + v)
    >>> mirror_formula(u=u, v=v)
    u*v/(u + v)

    """
def lens_formula(focal_length: Incomplete | None = None, u: Incomplete | None = None, v: Incomplete | None = None):
    """
    This function provides one of the three parameters
    when two of them are supplied.
    This is valid only for paraxial rays.

    Parameters
    ==========

    focal_length : sympifiable
        Focal length of the mirror.
    u : sympifiable
        Distance of object from the optical center on
        the principal axis.
    v : sympifiable
        Distance of the image from the optical center
        on the principal axis.

    Examples
    ========

    >>> from sympy.physics.optics import lens_formula
    >>> from sympy.abc import f, u, v
    >>> lens_formula(focal_length=f, u=u)
    f*u/(f + u)
    >>> lens_formula(focal_length=f, v=v)
    f*v/(f - v)
    >>> lens_formula(u=u, v=v)
    u*v/(u - v)

    """
def hyperfocal_distance(f, N, c):
    """

    Parameters
    ==========

    f: sympifiable
        Focal length of a given lens.

    N: sympifiable
        F-number of a given lens.

    c: sympifiable
        Circle of Confusion (CoC) of a given image format.

    Example
    =======

    >>> from sympy.physics.optics import hyperfocal_distance
    >>> round(hyperfocal_distance(f = 0.5, N = 8, c = 0.0033), 2)
    9.47
    """
def transverse_magnification(si, so):
    """

    Calculates the transverse magnification, which is the ratio of the
    image size to the object size.

    Parameters
    ==========

    so: sympifiable
        Lens-object distance.

    si: sympifiable
        Lens-image distance.

    Example
    =======

    >>> from sympy.physics.optics import transverse_magnification
    >>> transverse_magnification(30, 15)
    -2

    """
