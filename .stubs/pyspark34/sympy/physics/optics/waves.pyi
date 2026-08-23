from _typeshed import Incomplete
from sympy.core.expr import Expr

__all__ = ['TWave']

class TWave(Expr):
    """
    This is a simple transverse sine wave travelling in a one-dimensional space.
    Basic properties are required at the time of creation of the object,
    but they can be changed later with respective methods provided.

    Explanation
    ===========

    It is represented as :math:`A \\times cos(k*x - \\omega \\times t + \\phi )`,
    where :math:`A` is the amplitude, :math:`\\omega` is the angular frequency,
    :math:`k` is the wavenumber (spatial frequency), :math:`x` is a spatial variable
    to represent the position on the dimension on which the wave propagates,
    and :math:`\\phi` is the phase angle of the wave.


    Arguments
    =========

    amplitude : Sympifyable
        Amplitude of the wave.
    frequency : Sympifyable
        Frequency of the wave.
    phase : Sympifyable
        Phase angle of the wave.
    time_period : Sympifyable
        Time period of the wave.
    n : Sympifyable
        Refractive index of the medium.

    Raises
    =======

    ValueError : When neither frequency nor time period is provided
        or they are not consistent.
    TypeError : When anything other than TWave objects is added.


    Examples
    ========

    >>> from sympy import symbols
    >>> from sympy.physics.optics import TWave
    >>> A1, phi1, A2, phi2, f = symbols('A1, phi1, A2, phi2, f')
    >>> w1 = TWave(A1, f, phi1)
    >>> w2 = TWave(A2, f, phi2)
    >>> w3 = w1 + w2  # Superposition of two waves
    >>> w3
    TWave(sqrt(A1**2 + 2*A1*A2*cos(phi1 - phi2) + A2**2), f,
        atan2(A1*sin(phi1) + A2*sin(phi2), A1*cos(phi1) + A2*cos(phi2)), 1/f, n)
    >>> w3.amplitude
    sqrt(A1**2 + 2*A1*A2*cos(phi1 - phi2) + A2**2)
    >>> w3.phase
    atan2(A1*sin(phi1) + A2*sin(phi2), A1*cos(phi1) + A2*cos(phi2))
    >>> w3.speed
    299792458*meter/(second*n)
    >>> w3.angular_velocity
    2*pi*f

    """
    def __new__(cls, amplitude, frequency: Incomplete | None = None, phase=..., time_period: Incomplete | None = None, n=...): ...
    @property
    def amplitude(self):
        """
        Returns the amplitude of the wave.

        Examples
        ========

        >>> from sympy import symbols
        >>> from sympy.physics.optics import TWave
        >>> A, phi, f = symbols('A, phi, f')
        >>> w = TWave(A, f, phi)
        >>> w.amplitude
        A
        """
    @property
    def frequency(self):
        """
        Returns the frequency of the wave,
        in cycles per second.

        Examples
        ========

        >>> from sympy import symbols
        >>> from sympy.physics.optics import TWave
        >>> A, phi, f = symbols('A, phi, f')
        >>> w = TWave(A, f, phi)
        >>> w.frequency
        f
        """
    @property
    def phase(self):
        """
        Returns the phase angle of the wave,
        in radians.

        Examples
        ========

        >>> from sympy import symbols
        >>> from sympy.physics.optics import TWave
        >>> A, phi, f = symbols('A, phi, f')
        >>> w = TWave(A, f, phi)
        >>> w.phase
        phi
        """
    @property
    def time_period(self):
        """
        Returns the temporal period of the wave,
        in seconds per cycle.

        Examples
        ========

        >>> from sympy import symbols
        >>> from sympy.physics.optics import TWave
        >>> A, phi, f = symbols('A, phi, f')
        >>> w = TWave(A, f, phi)
        >>> w.time_period
        1/f
        """
    @property
    def n(self):
        """
        Returns the refractive index of the medium
        """
    @property
    def wavelength(self):
        """
        Returns the wavelength (spatial period) of the wave,
        in meters per cycle.
        It depends on the medium of the wave.

        Examples
        ========

        >>> from sympy import symbols
        >>> from sympy.physics.optics import TWave
        >>> A, phi, f = symbols('A, phi, f')
        >>> w = TWave(A, f, phi)
        >>> w.wavelength
        299792458*meter/(second*f*n)
        """
    @property
    def speed(self):
        """
        Returns the propagation speed of the wave,
        in meters per second.
        It is dependent on the propagation medium.

        Examples
        ========

        >>> from sympy import symbols
        >>> from sympy.physics.optics import TWave
        >>> A, phi, f = symbols('A, phi, f')
        >>> w = TWave(A, f, phi)
        >>> w.speed
        299792458*meter/(second*n)
        """
    @property
    def angular_velocity(self):
        """
        Returns the angular velocity of the wave,
        in radians per second.

        Examples
        ========

        >>> from sympy import symbols
        >>> from sympy.physics.optics import TWave
        >>> A, phi, f = symbols('A, phi, f')
        >>> w = TWave(A, f, phi)
        >>> w.angular_velocity
        2*pi*f
        """
    @property
    def wavenumber(self):
        """
        Returns the wavenumber of the wave,
        in radians per meter.

        Examples
        ========

        >>> from sympy import symbols
        >>> from sympy.physics.optics import TWave
        >>> A, phi, f = symbols('A, phi, f')
        >>> w = TWave(A, f, phi)
        >>> w.wavenumber
        pi*second*f*n/(149896229*meter)
        """
    def __add__(self, other):
        """
        Addition of two waves will result in their superposition.
        The type of interference will depend on their phase angles.
        """
    def __mul__(self, other):
        """
        Multiplying a wave by a scalar rescales the amplitude of the wave.
        """
    def __sub__(self, other): ...
    def __neg__(self): ...
    def __radd__(self, other): ...
    def __rmul__(self, other): ...
    def __rsub__(self, other): ...
