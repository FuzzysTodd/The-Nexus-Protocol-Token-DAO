from _typeshed import Incomplete
from sympy.core.numbers import I as I, Integer as Integer
from sympy.core.singleton import S as S
from sympy.core.symbol import Symbol as Symbol
from sympy.functions.elementary.miscellaneous import sqrt as sqrt
from sympy.functions.special.tensor_functions import KroneckerDelta as KroneckerDelta
from sympy.physics.quantum.cartesian import Px as Px, X as X
from sympy.physics.quantum.constants import hbar as hbar
from sympy.physics.quantum.hilbert import ComplexSpace as ComplexSpace
from sympy.physics.quantum.matrixutils import matrix_zeros as matrix_zeros
from sympy.physics.quantum.operator import Operator as Operator
from sympy.physics.quantum.qexpr import QExpr as QExpr
from sympy.physics.quantum.state import Bra as Bra, Ket as Ket, State as State

class SHOOp(Operator):
    """A base class for the SHO Operators.

    We are limiting the number of arguments to be 1.

    """
class RaisingOp(SHOOp):
    """The Raising Operator or a^dagger.

    When a^dagger acts on a state it raises the state up by one. Taking
    the adjoint of a^dagger returns 'a', the Lowering Operator. a^dagger
    can be rewritten in terms of position and momentum. We can represent
    a^dagger as a matrix, which will be its default basis.

    Parameters
    ==========

    args : tuple
        The list of numbers or parameters that uniquely specify the
        operator.

    Examples
    ========

    Create a Raising Operator and rewrite it in terms of position and
    momentum, and show that taking its adjoint returns 'a':

        >>> from sympy.physics.quantum.sho1d import RaisingOp
        >>> from sympy.physics.quantum import Dagger

        >>> ad = RaisingOp('a')
        >>> ad.rewrite('xp').doit()
        sqrt(2)*(m*omega*X - I*Px)/(2*sqrt(hbar)*sqrt(m*omega))

        >>> Dagger(ad)
        a

    Taking the commutator of a^dagger with other Operators:

        >>> from sympy.physics.quantum import Commutator
        >>> from sympy.physics.quantum.sho1d import RaisingOp, LoweringOp
        >>> from sympy.physics.quantum.sho1d import NumberOp

        >>> ad = RaisingOp('a')
        >>> a = LoweringOp('a')
        >>> N = NumberOp('N')
        >>> Commutator(ad, a).doit()
        -1
        >>> Commutator(ad, N).doit()
        -RaisingOp(a)

    Apply a^dagger to a state:

        >>> from sympy.physics.quantum import qapply
        >>> from sympy.physics.quantum.sho1d import RaisingOp, SHOKet

        >>> ad = RaisingOp('a')
        >>> k = SHOKet('k')
        >>> qapply(ad*k)
        sqrt(k + 1)*|k + 1>

    Matrix Representation

        >>> from sympy.physics.quantum.sho1d import RaisingOp
        >>> from sympy.physics.quantum.represent import represent
        >>> ad = RaisingOp('a')
        >>> represent(ad, basis=N, ndim=4, format='sympy')
        Matrix([
        [0,       0,       0, 0],
        [1,       0,       0, 0],
        [0, sqrt(2),       0, 0],
        [0,       0, sqrt(3), 0]])

    """
class LoweringOp(SHOOp):
    """The Lowering Operator or 'a'.

    When 'a' acts on a state it lowers the state up by one. Taking
    the adjoint of 'a' returns a^dagger, the Raising Operator. 'a'
    can be rewritten in terms of position and momentum. We can
    represent 'a' as a matrix, which will be its default basis.

    Parameters
    ==========

    args : tuple
        The list of numbers or parameters that uniquely specify the
        operator.

    Examples
    ========

    Create a Lowering Operator and rewrite it in terms of position and
    momentum, and show that taking its adjoint returns a^dagger:

        >>> from sympy.physics.quantum.sho1d import LoweringOp
        >>> from sympy.physics.quantum import Dagger

        >>> a = LoweringOp('a')
        >>> a.rewrite('xp').doit()
        sqrt(2)*(m*omega*X + I*Px)/(2*sqrt(hbar)*sqrt(m*omega))

        >>> Dagger(a)
        RaisingOp(a)

    Taking the commutator of 'a' with other Operators:

        >>> from sympy.physics.quantum import Commutator
        >>> from sympy.physics.quantum.sho1d import LoweringOp, RaisingOp
        >>> from sympy.physics.quantum.sho1d import NumberOp

        >>> a = LoweringOp('a')
        >>> ad = RaisingOp('a')
        >>> N = NumberOp('N')
        >>> Commutator(a, ad).doit()
        1
        >>> Commutator(a, N).doit()
        a

    Apply 'a' to a state:

        >>> from sympy.physics.quantum import qapply
        >>> from sympy.physics.quantum.sho1d import LoweringOp, SHOKet

        >>> a = LoweringOp('a')
        >>> k = SHOKet('k')
        >>> qapply(a*k)
        sqrt(k)*|k - 1>

    Taking 'a' of the lowest state will return 0:

        >>> from sympy.physics.quantum import qapply
        >>> from sympy.physics.quantum.sho1d import LoweringOp, SHOKet

        >>> a = LoweringOp('a')
        >>> k = SHOKet(0)
        >>> qapply(a*k)
        0

    Matrix Representation

        >>> from sympy.physics.quantum.sho1d import LoweringOp
        >>> from sympy.physics.quantum.represent import represent
        >>> a = LoweringOp('a')
        >>> represent(a, basis=N, ndim=4, format='sympy')
        Matrix([
        [0, 1,       0,       0],
        [0, 0, sqrt(2),       0],
        [0, 0,       0, sqrt(3)],
        [0, 0,       0,       0]])

    """
class NumberOp(SHOOp):
    """The Number Operator is simply a^dagger*a

    It is often useful to write a^dagger*a as simply the Number Operator
    because the Number Operator commutes with the Hamiltonian. And can be
    expressed using the Number Operator. Also the Number Operator can be
    applied to states. We can represent the Number Operator as a matrix,
    which will be its default basis.

    Parameters
    ==========

    args : tuple
        The list of numbers or parameters that uniquely specify the
        operator.

    Examples
    ========

    Create a Number Operator and rewrite it in terms of the ladder
    operators, position and momentum operators, and Hamiltonian:

        >>> from sympy.physics.quantum.sho1d import NumberOp

        >>> N = NumberOp('N')
        >>> N.rewrite('a').doit()
        RaisingOp(a)*a
        >>> N.rewrite('xp').doit()
        -1/2 + (m**2*omega**2*X**2 + Px**2)/(2*hbar*m*omega)
        >>> N.rewrite('H').doit()
        -1/2 + H/(hbar*omega)

    Take the Commutator of the Number Operator with other Operators:

        >>> from sympy.physics.quantum import Commutator
        >>> from sympy.physics.quantum.sho1d import NumberOp, Hamiltonian
        >>> from sympy.physics.quantum.sho1d import RaisingOp, LoweringOp

        >>> N = NumberOp('N')
        >>> H = Hamiltonian('H')
        >>> ad = RaisingOp('a')
        >>> a = LoweringOp('a')
        >>> Commutator(N,H).doit()
        0
        >>> Commutator(N,ad).doit()
        RaisingOp(a)
        >>> Commutator(N,a).doit()
        -a

    Apply the Number Operator to a state:

        >>> from sympy.physics.quantum import qapply
        >>> from sympy.physics.quantum.sho1d import NumberOp, SHOKet

        >>> N = NumberOp('N')
        >>> k = SHOKet('k')
        >>> qapply(N*k)
        k*|k>

    Matrix Representation

        >>> from sympy.physics.quantum.sho1d import NumberOp
        >>> from sympy.physics.quantum.represent import represent
        >>> N = NumberOp('N')
        >>> represent(N, basis=N, ndim=4, format='sympy')
        Matrix([
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 2, 0],
        [0, 0, 0, 3]])

    """
class Hamiltonian(SHOOp):
    """The Hamiltonian Operator.

    The Hamiltonian is used to solve the time-independent Schrodinger
    equation. The Hamiltonian can be expressed using the ladder operators,
    as well as by position and momentum. We can represent the Hamiltonian
    Operator as a matrix, which will be its default basis.

    Parameters
    ==========

    args : tuple
        The list of numbers or parameters that uniquely specify the
        operator.

    Examples
    ========

    Create a Hamiltonian Operator and rewrite it in terms of the ladder
    operators, position and momentum, and the Number Operator:

        >>> from sympy.physics.quantum.sho1d import Hamiltonian

        >>> H = Hamiltonian('H')
        >>> H.rewrite('a').doit()
        hbar*omega*(1/2 + RaisingOp(a)*a)
        >>> H.rewrite('xp').doit()
        (m**2*omega**2*X**2 + Px**2)/(2*m)
        >>> H.rewrite('N').doit()
        hbar*omega*(1/2 + N)

    Take the Commutator of the Hamiltonian and the Number Operator:

        >>> from sympy.physics.quantum import Commutator
        >>> from sympy.physics.quantum.sho1d import Hamiltonian, NumberOp

        >>> H = Hamiltonian('H')
        >>> N = NumberOp('N')
        >>> Commutator(H,N).doit()
        0

    Apply the Hamiltonian Operator to a state:

        >>> from sympy.physics.quantum import qapply
        >>> from sympy.physics.quantum.sho1d import Hamiltonian, SHOKet

        >>> H = Hamiltonian('H')
        >>> k = SHOKet('k')
        >>> qapply(H*k)
        hbar*k*omega*|k> + hbar*omega*|k>/2

    Matrix Representation

        >>> from sympy.physics.quantum.sho1d import Hamiltonian
        >>> from sympy.physics.quantum.represent import represent

        >>> H = Hamiltonian('H')
        >>> represent(H, basis=N, ndim=4, format='sympy')
        Matrix([
        [hbar*omega/2,              0,              0,              0],
        [           0, 3*hbar*omega/2,              0,              0],
        [           0,              0, 5*hbar*omega/2,              0],
        [           0,              0,              0, 7*hbar*omega/2]])

    """

class SHOState(State):
    """State class for SHO states"""
    @property
    def n(self): ...

class SHOKet(SHOState, Ket):
    """1D eigenket.

    Inherits from SHOState and Ket.

    Parameters
    ==========

    args : tuple
        The list of numbers or parameters that uniquely specify the ket
        This is usually its quantum numbers or its symbol.

    Examples
    ========

    Ket's know about their associated bra:

        >>> from sympy.physics.quantum.sho1d import SHOKet

        >>> k = SHOKet('k')
        >>> k.dual
        <k|
        >>> k.dual_class()
        <class 'sympy.physics.quantum.sho1d.SHOBra'>

    Take the Inner Product with a bra:

        >>> from sympy.physics.quantum import InnerProduct
        >>> from sympy.physics.quantum.sho1d import SHOKet, SHOBra

        >>> k = SHOKet('k')
        >>> b = SHOBra('b')
        >>> InnerProduct(b,k).doit()
        KroneckerDelta(b, k)

    Vector representation of a numerical state ket:

        >>> from sympy.physics.quantum.sho1d import SHOKet, NumberOp
        >>> from sympy.physics.quantum.represent import represent

        >>> k = SHOKet(3)
        >>> N = NumberOp('N')
        >>> represent(k, basis=N, ndim=4)
        Matrix([
        [0],
        [0],
        [0],
        [1]])

    """
    @classmethod
    def dual_class(self): ...

class SHOBra(SHOState, Bra):
    """A time-independent Bra in SHO.

    Inherits from SHOState and Bra.

    Parameters
    ==========

    args : tuple
        The list of numbers or parameters that uniquely specify the ket
        This is usually its quantum numbers or its symbol.

    Examples
    ========

    Bra's know about their associated ket:

        >>> from sympy.physics.quantum.sho1d import SHOBra

        >>> b = SHOBra('b')
        >>> b.dual
        |b>
        >>> b.dual_class()
        <class 'sympy.physics.quantum.sho1d.SHOKet'>

    Vector representation of a numerical state bra:

        >>> from sympy.physics.quantum.sho1d import SHOBra, NumberOp
        >>> from sympy.physics.quantum.represent import represent

        >>> b = SHOBra(3)
        >>> N = NumberOp('N')
        >>> represent(b, basis=N, ndim=4)
        Matrix([[0, 0, 0, 1]])

    """
    @classmethod
    def dual_class(self): ...

ad: Incomplete
a: Incomplete
H: Incomplete
N: Incomplete
omega: Incomplete
m: Incomplete
