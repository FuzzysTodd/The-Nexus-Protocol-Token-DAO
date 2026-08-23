from _typeshed import Incomplete
from sympy.core.expr import Expr as Expr
from sympy.core.sympify import sympify as sympify

class Prefix(Expr):
    """
    This class represent prefixes, with their name, symbol and factor.

    Prefixes are used to create derived units from a given unit. They should
    always be encapsulated into units.

    The factor is constructed from a base (default is 10) to some power, and
    it gives the total multiple or fraction. For example the kilometer km
    is constructed from the meter (factor 1) and the kilo (10 to the power 3,
    i.e. 1000). The base can be changed to allow e.g. binary prefixes.

    A prefix multiplied by something will always return the product of this
    other object times the factor, except if the other object:

    - is a prefix and they can be combined into a new prefix;
    - defines multiplication with prefixes (which is the case for the Unit
      class).
    """
    is_commutative: bool
    def __new__(cls, name, abbrev, exponent, base=..., latex_repr: Incomplete | None = None): ...
    @property
    def name(self): ...
    @property
    def abbrev(self): ...
    @property
    def scale_factor(self): ...
    @property
    def base(self): ...
    def __mul__(self, other): ...
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...

def prefix_unit(unit, prefixes):
    '''
    Return a list of all units formed by unit and the given prefixes.

    You can use the predefined PREFIXES or BIN_PREFIXES, but you can also
    pass as argument a subdict of them if you do not want all prefixed units.

        >>> from sympy.physics.units.prefixes import (PREFIXES,
        ...                                                 prefix_unit)
        >>> from sympy.physics.units import m
        >>> pref = {"m": PREFIXES["m"], "c": PREFIXES["c"], "d": PREFIXES["d"]}
        >>> prefix_unit(m, pref)  # doctest: +SKIP
        [millimeter, centimeter, decimeter]
    '''

yotta: Incomplete
zetta: Incomplete
exa: Incomplete
peta: Incomplete
tera: Incomplete
giga: Incomplete
mega: Incomplete
kilo: Incomplete
hecto: Incomplete
deca: Incomplete
deci: Incomplete
centi: Incomplete
milli: Incomplete
micro: Incomplete
nano: Incomplete
pico: Incomplete
femto: Incomplete
atto: Incomplete
zepto: Incomplete
yocto: Incomplete
PREFIXES: Incomplete
kibi: Incomplete
mebi: Incomplete
gibi: Incomplete
tebi: Incomplete
pebi: Incomplete
exbi: Incomplete
BIN_PREFIXES: Incomplete
