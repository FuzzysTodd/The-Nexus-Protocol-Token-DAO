from sympy.core.function import Add as Add, ArgumentIndexError as ArgumentIndexError, Function as Function
from sympy.core.power import Pow as Pow
from sympy.core.singleton import S as S
from sympy.core.sorting import default_sort_key as default_sort_key
from sympy.functions.elementary.exponential import exp as exp, log as log

class logaddexp(Function):
    """ Logarithm of the sum of exponentiations of the inputs.

    Helper class for use with e.g. numpy.logaddexp

    See Also
    ========

    https://numpy.org/doc/stable/reference/generated/numpy.logaddexp.html
    """
    nargs: int
    def __new__(cls, *args): ...
    def fdiff(self, argindex: int = 1):
        """
        Returns the first derivative of this function.
        """

class logaddexp2(Function):
    """ Logarithm of the sum of exponentiations of the inputs in base-2.

    Helper class for use with e.g. numpy.logaddexp2

    See Also
    ========

    https://numpy.org/doc/stable/reference/generated/numpy.logaddexp2.html
    """
    nargs: int
    def __new__(cls, *args): ...
    def fdiff(self, argindex: int = 1):
        """
        Returns the first derivative of this function.
        """
