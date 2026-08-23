from sympy.core.mul import Mul as Mul
from sympy.core.numbers import igcd as igcd
from sympy.core.singleton import S as S
from sympy.functions.elementary.exponential import log as log
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.physics.quantum.gate import Gate as Gate
from sympy.physics.quantum.qapply import qapply as qapply
from sympy.physics.quantum.qexpr import QuantumError as QuantumError
from sympy.physics.quantum.qft import QFT as QFT
from sympy.physics.quantum.qubit import Qubit as Qubit, measure_partial_oneshot as measure_partial_oneshot
from sympy.utilities.iterables import variations as variations

class OrderFindingException(QuantumError): ...

class CMod(Gate):
    """A controlled mod gate.

    This is black box controlled Mod function for use by shor's algorithm.
    TODO: implement a decompose property that returns how to do this in terms
    of elementary gates
    """
    @property
    def t(self):
        """Size of 1/2 input register.  First 1/2 holds output."""
    @property
    def a(self):
        """Base of the controlled mod function."""
    @property
    def N(self):
        """N is the type of modular arithmetic we are doing."""

def shor(N):
    """This function implements Shor's factoring algorithm on the Integer N

    The algorithm starts by picking a random number (a) and seeing if it is
    coprime with N. If it is not, then the gcd of the two numbers is a factor
    and we are done. Otherwise, it begins the period_finding subroutine which
    finds the period of a in modulo N arithmetic. This period, if even, can
    be used to calculate factors by taking a**(r/2)-1 and a**(r/2)+1.
    These values are returned.
    """
def getr(x, y, N): ...
def ratioize(list, N): ...
def period_find(a, N):
    """Finds the period of a in modulo N arithmetic

    This is quantum part of Shor's algorithm. It takes two registers,
    puts first in superposition of states with Hadamards so: ``|k>|0>``
    with k being all possible choices. It then does a controlled mod and
    a QFT to determine the order of a.
    """
