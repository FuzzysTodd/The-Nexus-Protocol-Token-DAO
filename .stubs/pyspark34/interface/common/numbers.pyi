import numbers as abc
from zope.interface.common import ABCInterface

class INumber(ABCInterface):
    abc = abc.Number

class IComplex(INumber):
    abc = abc.Complex
    def __complex__() -> complex:
        """
        Rarely implemented, even in builtin types.
        """

class IReal(IComplex):
    abc = abc.Real
    def __complex__() -> complex:
        """
        Rarely implemented, even in builtin types.
        """
    __floor__ = __complex__
    __ceil__ = __complex__

class IRational(IReal):
    abc = abc.Rational

class IIntegral(IRational):
    abc = abc.Integral
