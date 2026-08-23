from _typeshed import Incomplete
from sympy.core.basic import Basic

__all__ = ['Medium']

class Medium(Basic):
    """
    This class represents an optical medium. The prime reason to implement this is
    to facilitate refraction, Fermat's principle, etc.

    Explanation
    ===========

    An optical medium is a material through which electromagnetic waves propagate.
    The permittivity and permeability of the medium define how electromagnetic
    waves propagate in it.


    Parameters
    ==========

    name: string
        The display name of the Medium.

    permittivity: Sympifyable
        Electric permittivity of the space.

    permeability: Sympifyable
        Magnetic permeability of the space.

    n: Sympifyable
        Index of refraction of the medium.


    Examples
    ========

    >>> from sympy.abc import epsilon, mu
    >>> from sympy.physics.optics import Medium
    >>> m1 = Medium('m1')
    >>> m2 = Medium('m2', epsilon, mu)
    >>> m1.intrinsic_impedance
    149896229*pi*kilogram*meter**2/(1250000*ampere**2*second**3)
    >>> m2.refractive_index
    299792458*meter*sqrt(epsilon*mu)/second


    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Optical_medium

    """
    def __new__(cls, name, permittivity: Incomplete | None = None, permeability: Incomplete | None = None, n: Incomplete | None = None): ...
    @property
    def name(self): ...
    @property
    def speed(self):
        """
        Returns speed of the electromagnetic wave travelling in the medium.

        Examples
        ========

        >>> from sympy.physics.optics import Medium
        >>> m = Medium('m')
        >>> m.speed
        299792458*meter/second
        >>> m2 = Medium('m2', n=1)
        >>> m.speed == m2.speed
        True

        """
    @property
    def refractive_index(self):
        """
        Returns refractive index of the medium.

        Examples
        ========

        >>> from sympy.physics.optics import Medium
        >>> m = Medium('m')
        >>> m.refractive_index
        1

        """

class MediumN(Medium):
    """
    Represents an optical medium for which only the refractive index is known.
    Useful for simple ray optics.

    This class should never be instantiated directly.
    Instead it should be instantiated indirectly by instantiating Medium with
    only n specified.

    Examples
    ========
    >>> from sympy.physics.optics import Medium
    >>> m = Medium('m', n=2)
    >>> m
    MediumN(Str('m'), 2)
    """
    def __new__(cls, name, n): ...
    @property
    def n(self): ...

class MediumPP(Medium):
    """
    Represents an optical medium for which the permittivity and permeability are known.

    This class should never be instantiated directly. Instead it should be
    instantiated indirectly by instantiating Medium with any two of
    permittivity, permeability, and n specified, or by not specifying any
    of permittivity, permeability, or n, in which case default values for
    permittivity and permeability will be used.

    Examples
    ========
    >>> from sympy.physics.optics import Medium
    >>> from sympy.abc import epsilon, mu
    >>> m1 = Medium('m1', permittivity=epsilon, permeability=mu)
    >>> m1
    MediumPP(Str('m1'), epsilon, mu)
    >>> m2 = Medium('m2')
    >>> m2
    MediumPP(Str('m2'), 625000*ampere**2*second**4/(22468879468420441*pi*kilogram*meter**3), pi*kilogram*meter/(2500000*ampere**2*second**2))
    """
    def __new__(cls, name, permittivity, permeability): ...
    @property
    def intrinsic_impedance(self):
        """
        Returns intrinsic impedance of the medium.

        Explanation
        ===========

        The intrinsic impedance of a medium is the ratio of the
        transverse components of the electric and magnetic fields
        of the electromagnetic wave travelling in the medium.
        In a region with no electrical conductivity it simplifies
        to the square root of ratio of magnetic permeability to
        electric permittivity.

        Examples
        ========

        >>> from sympy.physics.optics import Medium
        >>> m = Medium('m')
        >>> m.intrinsic_impedance
        149896229*pi*kilogram*meter**2/(1250000*ampere**2*second**3)

        """
    @property
    def permittivity(self):
        """
        Returns electric permittivity of the medium.

        Examples
        ========

        >>> from sympy.physics.optics import Medium
        >>> m = Medium('m')
        >>> m.permittivity
        625000*ampere**2*second**4/(22468879468420441*pi*kilogram*meter**3)

        """
    @property
    def permeability(self):
        """
        Returns magnetic permeability of the medium.

        Examples
        ========

        >>> from sympy.physics.optics import Medium
        >>> m = Medium('m')
        >>> m.permeability
        pi*kilogram*meter/(2500000*ampere**2*second**2)

        """
    @property
    def n(self): ...
