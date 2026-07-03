from sympy.polys.domains.domain import Domain as Domain
from sympy.polys.polyerrors import ExactQuotientFailed as ExactQuotientFailed, NotInvertible as NotInvertible, NotReversible as NotReversible
from sympy.utilities import public as public

class Ring(Domain):
    """Represents a ring domain. """
    is_Ring: bool
    def get_ring(self):
        """Returns a ring associated with ``self``. """
    def exquo(self, a, b):
        """Exact quotient of ``a`` and ``b``, implies ``__floordiv__``.  """
    def quo(self, a, b):
        """Quotient of ``a`` and ``b``, implies ``__floordiv__``. """
    def rem(self, a, b):
        """Remainder of ``a`` and ``b``, implies ``__mod__``.  """
    def div(self, a, b):
        """Division of ``a`` and ``b``, implies ``__divmod__``. """
    def invert(self, a, b):
        """Returns inversion of ``a mod b``. """
    def revert(self, a):
        """Returns ``a**(-1)`` if possible. """
    def is_unit(self, a): ...
    def numer(self, a):
        """Returns numerator of ``a``. """
    def denom(self, a):
        """Returns denominator of `a`. """
    def free_module(self, rank) -> None:
        """
        Generate a free module of rank ``rank`` over self.

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> QQ.old_poly_ring(x).free_module(2)
        QQ[x]**2
        """
    def ideal(self, *gens):
        """
        Generate an ideal of ``self``.

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> QQ.old_poly_ring(x).ideal(x**2)
        <x**2>
        """
    def quotient_ring(self, e):
        """
        Form a quotient ring of ``self``.

        Here ``e`` can be an ideal or an iterable.

        >>> from sympy.abc import x
        >>> from sympy import QQ
        >>> QQ.old_poly_ring(x).quotient_ring(QQ.old_poly_ring(x).ideal(x**2))
        QQ[x]/<x**2>
        >>> QQ.old_poly_ring(x).quotient_ring([x**2])
        QQ[x]/<x**2>

        The division operator has been overloaded for this:

        >>> QQ.old_poly_ring(x)/[x**2]
        QQ[x]/<x**2>
        """
    def __truediv__(self, e): ...
