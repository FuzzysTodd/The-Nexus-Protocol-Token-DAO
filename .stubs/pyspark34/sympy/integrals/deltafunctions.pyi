from .integrals import Integral as Integral, integrate as integrate
from sympy.core.mul import Mul as Mul
from sympy.core.singleton import S as S
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.functions import DiracDelta as DiracDelta, Heaviside as Heaviside

def change_mul(node, x):
    """change_mul(node, x)

       Rearranges the operands of a product, bringing to front any simple
       DiracDelta expression.

       Explanation
       ===========

       If no simple DiracDelta expression was found, then all the DiracDelta
       expressions are simplified (using DiracDelta.expand(diracdelta=True, wrt=x)).

       Return: (dirac, new node)
       Where:
         o dirac is either a simple DiracDelta expression or None (if no simple
           expression was found);
         o new node is either a simplified DiracDelta expressions or None (if it
           could not be simplified).

       Examples
       ========

       >>> from sympy import DiracDelta, cos
       >>> from sympy.integrals.deltafunctions import change_mul
       >>> from sympy.abc import x, y
       >>> change_mul(x*y*DiracDelta(x)*cos(x), x)
       (DiracDelta(x), x*y*cos(x))
       >>> change_mul(x*y*DiracDelta(x**2 - 1)*cos(x), x)
       (None, x*y*cos(x)*DiracDelta(x - 1)/2 + x*y*cos(x)*DiracDelta(x + 1)/2)
       >>> change_mul(x*y*DiracDelta(cos(x))*cos(x), x)
       (None, None)

       See Also
       ========

       sympy.functions.special.delta_functions.DiracDelta
       deltaintegrate
    """
def deltaintegrate(f, x):
    """
    deltaintegrate(f, x)

    Explanation
    ===========

    The idea for integration is the following:

    - If we are dealing with a DiracDelta expression, i.e. DiracDelta(g(x)),
      we try to simplify it.

      If we could simplify it, then we integrate the resulting expression.
      We already know we can integrate a simplified expression, because only
      simple DiracDelta expressions are involved.

      If we couldn't simplify it, there are two cases:

      1) The expression is a simple expression: we return the integral,
         taking care if we are dealing with a Derivative or with a proper
         DiracDelta.

      2) The expression is not simple (i.e. DiracDelta(cos(x))): we can do
         nothing at all.

    - If the node is a multiplication node having a DiracDelta term:

      First we expand it.

      If the expansion did work, then we try to integrate the expansion.

      If not, we try to extract a simple DiracDelta term, then we have two
      cases:

      1) We have a simple DiracDelta term, so we return the integral.

      2) We didn't have a simple term, but we do have an expression with
         simplified DiracDelta terms, so we integrate this expression.

    Examples
    ========

        >>> from sympy.abc import x, y, z
        >>> from sympy.integrals.deltafunctions import deltaintegrate
        >>> from sympy import sin, cos, DiracDelta
        >>> deltaintegrate(x*sin(x)*cos(x)*DiracDelta(x - 1), x)
        sin(1)*cos(1)*Heaviside(x - 1)
        >>> deltaintegrate(y**2*DiracDelta(x - z)*DiracDelta(y - z), y)
        z**2*DiracDelta(x - z)*Heaviside(y - z)

    See Also
    ========

    sympy.functions.special.delta_functions.DiracDelta
    sympy.integrals.integrals.Integral
    """
