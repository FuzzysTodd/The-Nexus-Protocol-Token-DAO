from _typeshed import Incomplete
from sympy import default_sort_key as default_sort_key
from sympy.core.add import Add as Add
from sympy.core.containers import Tuple as Tuple
from sympy.core.mul import Mul as Mul
from sympy.core.power import Pow as Pow
from sympy.core.sorting import ordered as ordered
from sympy.core.sympify import sympify as sympify
from sympy.matrices.common import NonInvertibleMatrixError as NonInvertibleMatrixError
from sympy.physics.units.dimensions import Dimension as Dimension, DimensionSystem as DimensionSystem
from sympy.physics.units.prefixes import Prefix as Prefix
from sympy.physics.units.quantities import Quantity as Quantity
from sympy.physics.units.unitsystem import UnitSystem as UnitSystem
from sympy.utilities.iterables import sift as sift

def convert_to(expr, target_units, unit_system: str = 'SI'):
    """
    Convert ``expr`` to the same expression with all of its units and quantities
    represented as factors of ``target_units``, whenever the dimension is compatible.

    ``target_units`` may be a single unit/quantity, or a collection of
    units/quantities.

    Examples
    ========

    >>> from sympy.physics.units import speed_of_light, meter, gram, second, day
    >>> from sympy.physics.units import mile, newton, kilogram, atomic_mass_constant
    >>> from sympy.physics.units import kilometer, centimeter
    >>> from sympy.physics.units import gravitational_constant, hbar
    >>> from sympy.physics.units import convert_to
    >>> convert_to(mile, kilometer)
    25146*kilometer/15625
    >>> convert_to(mile, kilometer).n()
    1.609344*kilometer
    >>> convert_to(speed_of_light, meter/second)
    299792458*meter/second
    >>> convert_to(day, second)
    86400*second
    >>> 3*newton
    3*newton
    >>> convert_to(3*newton, kilogram*meter/second**2)
    3*kilogram*meter/second**2
    >>> convert_to(atomic_mass_constant, gram)
    1.660539060e-24*gram

    Conversion to multiple units:

    >>> convert_to(speed_of_light, [meter, second])
    299792458*meter/second
    >>> convert_to(3*newton, [centimeter, gram, second])
    300000*centimeter*gram/second**2

    Conversion to Planck units:

    >>> convert_to(atomic_mass_constant, [gravitational_constant, speed_of_light, hbar]).n()
    7.62963087839509e-20*hbar**0.5*speed_of_light**0.5/gravitational_constant**0.5

    """
def quantity_simplify(expr, across_dimensions: bool = False, unit_system: Incomplete | None = None):
    '''Return an equivalent expression in which prefixes are replaced
    with numerical values and all units of a given dimension are the
    unified in a canonical manner by default. `across_dimensions` allows
    for units of different dimensions to be simplified together.

    `unit_system` must be specified if `across_dimensions` is True.

    Examples
    ========

    >>> from sympy.physics.units.util import quantity_simplify
    >>> from sympy.physics.units.prefixes import kilo
    >>> from sympy.physics.units import foot, inch, joule, coulomb
    >>> quantity_simplify(kilo*foot*inch)
    250*foot**2/3
    >>> quantity_simplify(foot - 6*inch)
    foot/2
    >>> quantity_simplify(5*joule/coulomb, across_dimensions=True, unit_system="SI")
    5*volt
    '''
def check_dimensions(expr, unit_system: str = 'SI'):
    """Return expr if units in addends have the same
    base dimensions, else raise a ValueError."""
