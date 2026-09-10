from sympy.utilities import public as public

class DomainElement:
    """
    Represents an element of a domain.

    Mix in this trait into a class whose instances should be recognized as
    elements of a domain. Method ``parent()`` gives that domain.
    """
    def parent(self) -> None:
        """Get the domain associated with ``self``

        Examples
        ========

        >>> from sympy import ZZ, symbols
        >>> x, y = symbols('x, y')
        >>> K = ZZ[x,y]
        >>> p = K(x)**2 + K(y)**2
        >>> p
        x**2 + y**2
        >>> p.parent()
        ZZ[x,y]

        Notes
        =====

        This is used by :py:meth:`~.Domain.convert` to identify the domain
        associated with a domain element.
        """
