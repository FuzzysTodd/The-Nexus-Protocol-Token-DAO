from .plot_interval import PlotInterval as PlotInterval
from .plot_object import PlotObject as PlotObject
from .util import parse_option_string as parse_option_string
from _typeshed import Incomplete
from sympy.core.symbol import Symbol as Symbol
from sympy.core.sympify import sympify as sympify
from sympy.geometry.entity import GeometryEntity as GeometryEntity
from sympy.utilities.iterables import is_sequence as is_sequence

class PlotMode(PlotObject):
    """
    Grandparent class for plotting
    modes. Serves as interface for
    registration, lookup, and init
    of modes.

    To create a new plot mode,
    inherit from PlotModeBase
    or one of its children, such
    as PlotSurface or PlotCurve.
    """
    i_vars: Incomplete
    d_vars: Incomplete
    intervals: Incomplete
    aliases: Incomplete
    is_default: bool
    def draw(self) -> None: ...
    def __new__(cls, *args, **kwargs):
        """
        This is the function which interprets
        arguments given to Plot.__init__ and
        Plot.__setattr__. Returns an initialized
        instance of the appropriate child class.
        """

def var_count_error(is_independent, is_plotting):
    """
    Used to format an error message which differs
    slightly in 4 places.
    """
