import numpy.typing as npt
from _typeshed import Incomplete
from typing import Any

__all__ = ['Avogadro', 'Boltzmann', 'Btu', 'Btu_IT', 'Btu_th', 'G', 'Julian_year', 'N_A', 'Planck', 'R', 'Rydberg', 'Stefan_Boltzmann', 'Wien', 'acre', 'alpha', 'angstrom', 'arcmin', 'arcminute', 'arcsec', 'arcsecond', 'astronomical_unit', 'atm', 'atmosphere', 'atomic_mass', 'atto', 'au', 'bar', 'barrel', 'bbl', 'blob', 'c', 'calorie', 'calorie_IT', 'calorie_th', 'carat', 'centi', 'convert_temperature', 'day', 'deci', 'degree', 'degree_Fahrenheit', 'deka', 'dyn', 'dyne', 'e', 'eV', 'electron_mass', 'electron_volt', 'elementary_charge', 'epsilon_0', 'erg', 'exa', 'exbi', 'femto', 'fermi', 'fine_structure', 'fluid_ounce', 'fluid_ounce_US', 'fluid_ounce_imp', 'foot', 'g', 'gallon', 'gallon_US', 'gallon_imp', 'gas_constant', 'gibi', 'giga', 'golden', 'golden_ratio', 'grain', 'gram', 'gravitational_constant', 'h', 'hbar', 'hectare', 'hecto', 'horsepower', 'hour', 'hp', 'inch', 'k', 'kgf', 'kibi', 'kilo', 'kilogram_force', 'kmh', 'knot', 'lambda2nu', 'lb', 'lbf', 'light_year', 'liter', 'litre', 'long_ton', 'm_e', 'm_n', 'm_p', 'm_u', 'mach', 'mebi', 'mega', 'metric_ton', 'micro', 'micron', 'mil', 'mile', 'milli', 'minute', 'mmHg', 'mph', 'mu_0', 'nano', 'nautical_mile', 'neutron_mass', 'nu2lambda', 'ounce', 'oz', 'parsec', 'pebi', 'peta', 'pi', 'pico', 'point', 'pound', 'pound_force', 'proton_mass', 'psi', 'pt', 'short_ton', 'sigma', 'slinch', 'slug', 'speed_of_light', 'speed_of_sound', 'stone', 'survey_foot', 'survey_mile', 'tebi', 'tera', 'ton_TNT', 'torr', 'troy_ounce', 'troy_pound', 'u', 'week', 'yard', 'year', 'yobi', 'yocto', 'yotta', 'zebi', 'zepto', 'zero_Celsius', 'zetta']

pi: Incomplete
golden: Incomplete
golden_ratio: Incomplete
yotta: float
zetta: float
exa: float
peta: float
tera: float
giga: float
mega: float
kilo: float
hecto: float
deka: float
deci: float
centi: float
milli: float
micro: float
nano: float
pico: float
femto: float
atto: float
zepto: float
yocto: float
kibi: Incomplete
mebi: Incomplete
gibi: Incomplete
tebi: Incomplete
pebi: Incomplete
exbi: Incomplete
zebi: Incomplete
yobi: Incomplete
c: Incomplete
speed_of_light: Incomplete
mu_0: Incomplete
epsilon_0: Incomplete
h: Incomplete
Planck: Incomplete
hbar: Incomplete
G: Incomplete
gravitational_constant: Incomplete
g: Incomplete
e: Incomplete
elementary_charge: Incomplete
R: Incomplete
gas_constant: Incomplete
alpha: Incomplete
fine_structure: Incomplete
N_A: Incomplete
Avogadro: Incomplete
k: Incomplete
Boltzmann: Incomplete
sigma: Incomplete
Stefan_Boltzmann: Incomplete
Wien: Incomplete
Rydberg: Incomplete
gram: float
metric_ton: float
grain: float
lb: Incomplete
pound: Incomplete
blob: Incomplete
slinch: Incomplete
slug: Incomplete
oz: Incomplete
ounce: Incomplete
stone: Incomplete
long_ton: Incomplete
short_ton: Incomplete
troy_ounce: Incomplete
troy_pound: Incomplete
carat: float
m_e: Incomplete
electron_mass: Incomplete
m_p: Incomplete
proton_mass: Incomplete
m_n: Incomplete
neutron_mass: Incomplete
m_u: Incomplete
u: Incomplete
atomic_mass: Incomplete
degree: Incomplete
arcmin: Incomplete
arcminute: Incomplete
arcsec: Incomplete
arcsecond: Incomplete
minute: float
hour: Incomplete
day: Incomplete
week: Incomplete
year: Incomplete
Julian_year: Incomplete
inch: float
foot: Incomplete
yard: Incomplete
mile: Incomplete
mil: Incomplete
pt: Incomplete
point: Incomplete
survey_foot: Incomplete
survey_mile: Incomplete
nautical_mile: float
fermi: float
angstrom: float
micron: float
au: float
astronomical_unit: float
light_year: Incomplete
parsec: Incomplete
atm: Incomplete
atmosphere: Incomplete
bar: float
torr: Incomplete
mmHg: Incomplete
psi: Incomplete
hectare: float
acre: Incomplete
litre: float
liter: float
gallon: Incomplete
gallon_US: Incomplete
fluid_ounce: Incomplete
fluid_ounce_US: Incomplete
bbl: Incomplete
barrel: Incomplete
gallon_imp: float
fluid_ounce_imp: Incomplete
kmh: Incomplete
mph: Incomplete
mach: float
speed_of_sound: float
knot: Incomplete
zero_Celsius: float
degree_Fahrenheit: Incomplete
eV = elementary_charge
electron_volt = elementary_charge
calorie: float
calorie_th: float
calorie_IT: float
erg: float
Btu_th: Incomplete
Btu: Incomplete
Btu_IT: Incomplete
ton_TNT: Incomplete
hp: Incomplete
horsepower: Incomplete
dyn: float
dyne: float
lbf: Incomplete
pound_force: Incomplete
kgf = g
kilogram_force = g

def convert_temperature(val: npt.ArrayLike, old_scale: str, new_scale: str) -> Any:
    """
    Convert from a temperature scale to another one among Celsius, Kelvin,
    Fahrenheit, and Rankine scales.

    Parameters
    ----------
    val : array_like
        Value(s) of the temperature(s) to be converted expressed in the
        original scale.
    old_scale : str
        Specifies as a string the original scale from which the temperature
        value(s) will be converted. Supported scales are Celsius ('Celsius',
        'celsius', 'C' or 'c'), Kelvin ('Kelvin', 'kelvin', 'K', 'k'),
        Fahrenheit ('Fahrenheit', 'fahrenheit', 'F' or 'f'), and Rankine
        ('Rankine', 'rankine', 'R', 'r').
    new_scale : str
        Specifies as a string the new scale to which the temperature
        value(s) will be converted. Supported scales are Celsius ('Celsius',
        'celsius', 'C' or 'c'), Kelvin ('Kelvin', 'kelvin', 'K', 'k'),
        Fahrenheit ('Fahrenheit', 'fahrenheit', 'F' or 'f'), and Rankine
        ('Rankine', 'rankine', 'R', 'r').

    Returns
    -------
    res : float or array of floats
        Value(s) of the converted temperature(s) expressed in the new scale.

    Notes
    -----
    .. versionadded:: 0.18.0

    Examples
    --------
    >>> from scipy.constants import convert_temperature
    >>> import numpy as np
    >>> convert_temperature(np.array([-40, 40]), 'Celsius', 'Kelvin')
    array([ 233.15,  313.15])

    """
def lambda2nu(lambda_: npt.ArrayLike) -> Any:
    """
    Convert wavelength to optical frequency

    Parameters
    ----------
    lambda_ : array_like
        Wavelength(s) to be converted.

    Returns
    -------
    nu : float or array of floats
        Equivalent optical frequency.

    Notes
    -----
    Computes ``nu = c / lambda`` where c = 299792458.0, i.e., the
    (vacuum) speed of light in meters/second.

    Examples
    --------
    >>> from scipy.constants import lambda2nu, speed_of_light
    >>> import numpy as np
    >>> lambda2nu(np.array((1, speed_of_light)))
    array([  2.99792458e+08,   1.00000000e+00])

    """
def nu2lambda(nu: npt.ArrayLike) -> Any:
    """
    Convert optical frequency to wavelength.

    Parameters
    ----------
    nu : array_like
        Optical frequency to be converted.

    Returns
    -------
    lambda : float or array of floats
        Equivalent wavelength(s).

    Notes
    -----
    Computes ``lambda = c / nu`` where c = 299792458.0, i.e., the
    (vacuum) speed of light in meters/second.

    Examples
    --------
    >>> from scipy.constants import nu2lambda, speed_of_light
    >>> import numpy as np
    >>> nu2lambda(np.array((1, speed_of_light)))
    array([  2.99792458e+08,   1.00000000e+00])

    """
