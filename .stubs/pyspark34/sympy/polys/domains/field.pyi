from sympy.polys.domains.ring import Ring as Ring
from sympy.polys.polyerrors import DomainError as DomainError, NotReversible as NotReversible
from sympy.utilities import public as public

class Field(Ring):
    """Represents a field domain. """
    is_Field: bool
    is_PID: bool
    def get_ring(self) -> None:
        """Returns a ring associated with ``self``. """
    def get_field(self):
        """Returns a field associated with ``self``. """
    def exquo(self, a, b):
        """Exact quotient of ``a`` and ``b``, implies ``__truediv__``.  """
    def quo(self, a, b):
        """Quotient of ``a`` and ``b``, implies ``__truediv__``. """
    def rem(self, a, b):
        """Remainder of ``a`` and ``b``, implies nothing.  """
    def div(self, a, b):
        """Division of ``a`` and ``b``, implies ``__truediv__``. """
    def gcd(self, a, b):
        """
        Returns GCD of ``a`` and ``b``.

        This definition of GCD over fields allows to clear denominators
        in `primitive()`.

        Examples
        ========

        >>> from sympy.polys.domains import QQ
        >>> from sympy import S, gcd, primitive
        >>> from sympy.abc import x

        >>> QQ.gcd(QQ(2, 3), QQ(4, 9))
        2/9
        >>> gcd(S(2)/3, S(4)/9)
        2/9
        >>> primitive(2*x/3 + S(4)/9)
        (2/9, 3*x + 2)

        """
    def lcm(self, a, b):
        """
        Returns LCM of ``a`` and ``b``.

        >>> from sympy.polys.domains import QQ
        >>> from sympy import S, lcm

        >>> QQ.lcm(QQ(2, 3), QQ(4, 9))
        4/3
        >>> lcm(S(2)/3, S(4)/9)
        4/3

        """
    def revert(self, a):
        """Returns ``a**(-1)`` if possible. """
    def is_unit(self, a):
        """Return true if ``a`` is a invertible"""
