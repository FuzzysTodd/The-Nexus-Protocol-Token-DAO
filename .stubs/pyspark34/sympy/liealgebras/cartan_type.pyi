from _typeshed import Incomplete
from sympy.core import Atom as Atom, Basic as Basic

class CartanType_generator:
    """
    Constructor for actually creating things
    """
    def __call__(self, *args): ...

CartanType: Incomplete

class Standard_Cartan(Atom):
    """
    Concrete base class for Cartan types such as A4, etc
    """
    def __new__(cls, series, n): ...
    def rank(self):
        """
        Returns the rank of the Lie algebra
        """
    def series(self):
        """
        Returns the type of the Lie algebra
        """
