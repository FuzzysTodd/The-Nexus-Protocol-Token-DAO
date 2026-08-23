from sympy.core.cache import cacheit as cacheit
from sympy.core.expr import Expr as Expr
from sympy.core.singleton import S as S

class SeriesBase(Expr):
    """Base Class for series"""
    @property
    def interval(self) -> None:
        """The interval on which the series is defined"""
    @property
    def start(self) -> None:
        """The starting point of the series. This point is included"""
    @property
    def stop(self) -> None:
        """The ending point of the series. This point is included"""
    @property
    def length(self) -> None:
        """Length of the series expansion"""
    @property
    def variables(self):
        """Returns a tuple of variables that are bounded"""
    @property
    def free_symbols(self):
        """
        This method returns the symbols in the object, excluding those
        that take on a specific value (i.e. the dummy symbols).
        """
    def term(self, pt):
        """Term at point pt of a series"""
    def __iter__(self): ...
    def __getitem__(self, index): ...
