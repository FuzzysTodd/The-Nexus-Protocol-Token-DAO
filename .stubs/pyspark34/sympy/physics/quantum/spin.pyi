from _typeshed import Incomplete
from sympy.core.expr import Expr
from sympy.physics.quantum.operator import HermitianOperator, Operator, UnitaryOperator
from sympy.physics.quantum.state import Bra, Ket, State

__all__ = ['m_values', 'Jplus', 'Jminus', 'Jx', 'Jy', 'Jz', 'J2', 'Rotation', 'WignerD', 'JxKet', 'JxBra', 'JyKet', 'JyBra', 'JzKet', 'JzBra', 'JzOp', 'J2Op', 'JxKetCoupled', 'JxBraCoupled', 'JyKetCoupled', 'JyBraCoupled', 'JzKetCoupled', 'JzBraCoupled', 'couple', 'uncouple']

def m_values(j): ...

class SpinOpBase:
    """Base class for spin operators."""
    @property
    def name(self): ...

class JplusOp(SpinOpBase, Operator):
    """The J+ operator."""
    basis: str
    def matrix_element(self, j, m, jp, mp): ...

class JminusOp(SpinOpBase, Operator):
    """The J- operator."""
    basis: str
    def matrix_element(self, j, m, jp, mp): ...

class JxOp(SpinOpBase, HermitianOperator):
    """The Jx operator."""
    basis: str

class JyOp(SpinOpBase, HermitianOperator):
    """The Jy operator."""
    basis: str

class JzOp(SpinOpBase, HermitianOperator):
    """The Jz operator."""
    basis: str
    def matrix_element(self, j, m, jp, mp): ...

class J2Op(SpinOpBase, HermitianOperator):
    """The J^2 operator."""
    def matrix_element(self, j, m, jp, mp): ...

class Rotation(UnitaryOperator):
    """Wigner D operator in terms of Euler angles.

    Defines the rotation operator in terms of the Euler angles defined by
    the z-y-z convention for a passive transformation. That is the coordinate
    axes are rotated first about the z-axis, giving the new x'-y'-z' axes. Then
    this new coordinate system is rotated about the new y'-axis, giving new
    x''-y''-z'' axes. Then this new coordinate system is rotated about the
    z''-axis. Conventions follow those laid out in [1]_.

    Parameters
    ==========

    alpha : Number, Symbol
        First Euler Angle
    beta : Number, Symbol
        Second Euler angle
    gamma : Number, Symbol
        Third Euler angle

    Examples
    ========

    A simple example rotation operator:

        >>> from sympy import pi
        >>> from sympy.physics.quantum.spin import Rotation
        >>> Rotation(pi, 0, pi/2)
        R(pi,0,pi/2)

    With symbolic Euler angles and calculating the inverse rotation operator:

        >>> from sympy import symbols
        >>> a, b, c = symbols('a b c')
        >>> Rotation(a, b, c)
        R(a,b,c)
        >>> Rotation(a, b, c).inverse()
        R(-c,-b,-a)

    See Also
    ========

    WignerD: Symbolic Wigner-D function
    D: Wigner-D function
    d: Wigner small-d function

    References
    ==========

    .. [1] Varshalovich, D A, Quantum Theory of Angular Momentum. 1988.
    """
    @property
    def alpha(self): ...
    @property
    def beta(self): ...
    @property
    def gamma(self): ...
    @classmethod
    def D(cls, j, m, mp, alpha, beta, gamma):
        """Wigner D-function.

        Returns an instance of the WignerD class corresponding to the Wigner-D
        function specified by the parameters.

        Parameters
        ===========

        j : Number
            Total angular momentum
        m : Number
            Eigenvalue of angular momentum along axis after rotation
        mp : Number
            Eigenvalue of angular momentum along rotated axis
        alpha : Number, Symbol
            First Euler angle of rotation
        beta : Number, Symbol
            Second Euler angle of rotation
        gamma : Number, Symbol
            Third Euler angle of rotation

        Examples
        ========

        Return the Wigner-D matrix element for a defined rotation, both
        numerical and symbolic:

            >>> from sympy.physics.quantum.spin import Rotation
            >>> from sympy import pi, symbols
            >>> alpha, beta, gamma = symbols('alpha beta gamma')
            >>> Rotation.D(1, 1, 0,pi, pi/2,-pi)
            WignerD(1, 1, 0, pi, pi/2, -pi)

        See Also
        ========

        WignerD: Symbolic Wigner-D function

        """
    @classmethod
    def d(cls, j, m, mp, beta):
        """Wigner small-d function.

        Returns an instance of the WignerD class corresponding to the Wigner-D
        function specified by the parameters with the alpha and gamma angles
        given as 0.

        Parameters
        ===========

        j : Number
            Total angular momentum
        m : Number
            Eigenvalue of angular momentum along axis after rotation
        mp : Number
            Eigenvalue of angular momentum along rotated axis
        beta : Number, Symbol
            Second Euler angle of rotation

        Examples
        ========

        Return the Wigner-D matrix element for a defined rotation, both
        numerical and symbolic:

            >>> from sympy.physics.quantum.spin import Rotation
            >>> from sympy import pi, symbols
            >>> beta = symbols('beta')
            >>> Rotation.d(1, 1, 0, pi/2)
            WignerD(1, 1, 0, 0, pi/2, 0)

        See Also
        ========

        WignerD: Symbolic Wigner-D function

        """
    def matrix_element(self, j, m, jp, mp): ...

class WignerD(Expr):
    """Wigner-D function

    The Wigner D-function gives the matrix elements of the rotation
    operator in the jm-representation. For the Euler angles `\\alpha`,
    `\\beta`, `\\gamma`, the D-function is defined such that:

    .. math ::
        <j,m| \\mathcal{R}(\\alpha, \\beta, \\gamma ) |j',m'> = \\delta_{jj'} D(j, m, m', \\alpha, \\beta, \\gamma)

    Where the rotation operator is as defined by the Rotation class [1]_.

    The Wigner D-function defined in this way gives:

    .. math ::
        D(j, m, m', \\alpha, \\beta, \\gamma) = e^{-i m \\alpha} d(j, m, m', \\beta) e^{-i m' \\gamma}

    Where d is the Wigner small-d function, which is given by Rotation.d.

    The Wigner small-d function gives the component of the Wigner
    D-function that is determined by the second Euler angle. That is the
    Wigner D-function is:

    .. math ::
        D(j, m, m', \\alpha, \\beta, \\gamma) = e^{-i m \\alpha} d(j, m, m', \\beta) e^{-i m' \\gamma}

    Where d is the small-d function. The Wigner D-function is given by
    Rotation.D.

    Note that to evaluate the D-function, the j, m and mp parameters must
    be integer or half integer numbers.

    Parameters
    ==========

    j : Number
        Total angular momentum
    m : Number
        Eigenvalue of angular momentum along axis after rotation
    mp : Number
        Eigenvalue of angular momentum along rotated axis
    alpha : Number, Symbol
        First Euler angle of rotation
    beta : Number, Symbol
        Second Euler angle of rotation
    gamma : Number, Symbol
        Third Euler angle of rotation

    Examples
    ========

    Evaluate the Wigner-D matrix elements of a simple rotation:

        >>> from sympy.physics.quantum.spin import Rotation
        >>> from sympy import pi
        >>> rot = Rotation.D(1, 1, 0, pi, pi/2, 0)
        >>> rot
        WignerD(1, 1, 0, pi, pi/2, 0)
        >>> rot.doit()
        sqrt(2)/2

    Evaluate the Wigner-d matrix elements of a simple rotation

        >>> rot = Rotation.d(1, 1, 0, pi/2)
        >>> rot
        WignerD(1, 1, 0, 0, pi/2, 0)
        >>> rot.doit()
        -sqrt(2)/2

    See Also
    ========

    Rotation: Rotation operator

    References
    ==========

    .. [1] Varshalovich, D A, Quantum Theory of Angular Momentum. 1988.
    """
    is_commutative: bool
    def __new__(cls, *args, **hints): ...
    @property
    def j(self): ...
    @property
    def m(self): ...
    @property
    def mp(self): ...
    @property
    def alpha(self): ...
    @property
    def beta(self): ...
    @property
    def gamma(self): ...
    def doit(self, **hints): ...

Jx: Incomplete
Jy: Incomplete
Jz: Incomplete
J2: Incomplete
Jplus: Incomplete
Jminus: Incomplete

class SpinState(State):
    """Base class for angular momentum states."""
    def __new__(cls, j, m): ...
    @property
    def j(self): ...
    @property
    def m(self): ...

class JxKet(SpinState, Ket):
    """Eigenket of Jx.

    See JzKet for the usage of spin eigenstates.

    See Also
    ========

    JzKet: Usage of spin states

    """
    @classmethod
    def dual_class(self): ...
    @classmethod
    def coupled_class(self): ...

class JxBra(SpinState, Bra):
    """Eigenbra of Jx.

    See JzKet for the usage of spin eigenstates.

    See Also
    ========

    JzKet: Usage of spin states

    """
    @classmethod
    def dual_class(self): ...
    @classmethod
    def coupled_class(self): ...

class JyKet(SpinState, Ket):
    """Eigenket of Jy.

    See JzKet for the usage of spin eigenstates.

    See Also
    ========

    JzKet: Usage of spin states

    """
    @classmethod
    def dual_class(self): ...
    @classmethod
    def coupled_class(self): ...

class JyBra(SpinState, Bra):
    """Eigenbra of Jy.

    See JzKet for the usage of spin eigenstates.

    See Also
    ========

    JzKet: Usage of spin states

    """
    @classmethod
    def dual_class(self): ...
    @classmethod
    def coupled_class(self): ...

class JzKet(SpinState, Ket):
    '''Eigenket of Jz.

    Spin state which is an eigenstate of the Jz operator. Uncoupled states,
    that is states representing the interaction of multiple separate spin
    states, are defined as a tensor product of states.

    Parameters
    ==========

    j : Number, Symbol
        Total spin angular momentum
    m : Number, Symbol
        Eigenvalue of the Jz spin operator

    Examples
    ========

    *Normal States:*

    Defining simple spin states, both numerical and symbolic:

        >>> from sympy.physics.quantum.spin import JzKet, JxKet
        >>> from sympy import symbols
        >>> JzKet(1, 0)
        |1,0>
        >>> j, m = symbols(\'j m\')
        >>> JzKet(j, m)
        |j,m>

    Rewriting the JzKet in terms of eigenkets of the Jx operator:
    Note: that the resulting eigenstates are JxKet\'s

        >>> JzKet(1,1).rewrite("Jx")
        |1,-1>/2 - sqrt(2)*|1,0>/2 + |1,1>/2

    Get the vector representation of a state in terms of the basis elements
    of the Jx operator:

        >>> from sympy.physics.quantum.represent import represent
        >>> from sympy.physics.quantum.spin import Jx, Jz
        >>> represent(JzKet(1,-1), basis=Jx)
        Matrix([
        [      1/2],
        [sqrt(2)/2],
        [      1/2]])

    Apply innerproducts between states:

        >>> from sympy.physics.quantum.innerproduct import InnerProduct
        >>> from sympy.physics.quantum.spin import JxBra
        >>> i = InnerProduct(JxBra(1,1), JzKet(1,1))
        >>> i
        <1,1|1,1>
        >>> i.doit()
        1/2

    *Uncoupled States:*

    Define an uncoupled state as a TensorProduct between two Jz eigenkets:

        >>> from sympy.physics.quantum.tensorproduct import TensorProduct
        >>> j1,m1,j2,m2 = symbols(\'j1 m1 j2 m2\')
        >>> TensorProduct(JzKet(1,0), JzKet(1,1))
        |1,0>x|1,1>
        >>> TensorProduct(JzKet(j1,m1), JzKet(j2,m2))
        |j1,m1>x|j2,m2>

    A TensorProduct can be rewritten, in which case the eigenstates that make
    up the tensor product is rewritten to the new basis:

        >>> TensorProduct(JzKet(1,1),JxKet(1,1)).rewrite(\'Jz\')
        |1,1>x|1,-1>/2 + sqrt(2)*|1,1>x|1,0>/2 + |1,1>x|1,1>/2

    The represent method for TensorProduct\'s gives the vector representation of
    the state. Note that the state in the product basis is the equivalent of the
    tensor product of the vector representation of the component eigenstates:

        >>> represent(TensorProduct(JzKet(1,0),JzKet(1,1)))
        Matrix([
        [0],
        [0],
        [0],
        [1],
        [0],
        [0],
        [0],
        [0],
        [0]])
        >>> represent(TensorProduct(JzKet(1,1),JxKet(1,1)), basis=Jz)
        Matrix([
        [      1/2],
        [sqrt(2)/2],
        [      1/2],
        [        0],
        [        0],
        [        0],
        [        0],
        [        0],
        [        0]])

    See Also
    ========

    JzKetCoupled: Coupled eigenstates
    sympy.physics.quantum.tensorproduct.TensorProduct: Used to specify uncoupled states
    uncouple: Uncouples states given coupling parameters
    couple: Couples uncoupled states

    '''
    @classmethod
    def dual_class(self): ...
    @classmethod
    def coupled_class(self): ...

class JzBra(SpinState, Bra):
    """Eigenbra of Jz.

    See the JzKet for the usage of spin eigenstates.

    See Also
    ========

    JzKet: Usage of spin states

    """
    @classmethod
    def dual_class(self): ...
    @classmethod
    def coupled_class(self): ...

class CoupledSpinState(SpinState):
    """Base class for coupled angular momentum states."""
    def __new__(cls, j, m, jn, *jcoupling): ...
    @property
    def jn(self): ...
    @property
    def coupling(self): ...
    @property
    def coupled_jn(self): ...
    @property
    def coupled_n(self): ...

class JxKetCoupled(CoupledSpinState, Ket):
    """Coupled eigenket of Jx.

    See JzKetCoupled for the usage of coupled spin eigenstates.

    See Also
    ========

    JzKetCoupled: Usage of coupled spin states

    """
    @classmethod
    def dual_class(self): ...
    @classmethod
    def uncoupled_class(self): ...

class JxBraCoupled(CoupledSpinState, Bra):
    """Coupled eigenbra of Jx.

    See JzKetCoupled for the usage of coupled spin eigenstates.

    See Also
    ========

    JzKetCoupled: Usage of coupled spin states

    """
    @classmethod
    def dual_class(self): ...
    @classmethod
    def uncoupled_class(self): ...

class JyKetCoupled(CoupledSpinState, Ket):
    """Coupled eigenket of Jy.

    See JzKetCoupled for the usage of coupled spin eigenstates.

    See Also
    ========

    JzKetCoupled: Usage of coupled spin states

    """
    @classmethod
    def dual_class(self): ...
    @classmethod
    def uncoupled_class(self): ...

class JyBraCoupled(CoupledSpinState, Bra):
    """Coupled eigenbra of Jy.

    See JzKetCoupled for the usage of coupled spin eigenstates.

    See Also
    ========

    JzKetCoupled: Usage of coupled spin states

    """
    @classmethod
    def dual_class(self): ...
    @classmethod
    def uncoupled_class(self): ...

class JzKetCoupled(CoupledSpinState, Ket):
    '''Coupled eigenket of Jz

    Spin state that is an eigenket of Jz which represents the coupling of
    separate spin spaces.

    The arguments for creating instances of JzKetCoupled are ``j``, ``m``,
    ``jn`` and an optional ``jcoupling`` argument. The ``j`` and ``m`` options
    are the total angular momentum quantum numbers, as used for normal states
    (e.g. JzKet).

    The other required parameter in ``jn``, which is a tuple defining the `j_n`
    angular momentum quantum numbers of the product spaces. So for example, if
    a state represented the coupling of the product basis state
    `\\left|j_1,m_1\\right\\rangle\\times\\left|j_2,m_2\\right\\rangle`, the ``jn``
    for this state would be ``(j1,j2)``.

    The final option is ``jcoupling``, which is used to define how the spaces
    specified by ``jn`` are coupled, which includes both the order these spaces
    are coupled together and the quantum numbers that arise from these
    couplings. The ``jcoupling`` parameter itself is a list of lists, such that
    each of the sublists defines a single coupling between the spin spaces. If
    there are N coupled angular momentum spaces, that is ``jn`` has N elements,
    then there must be N-1 sublists. Each of these sublists making up the
    ``jcoupling`` parameter have length 3. The first two elements are the
    indices of the product spaces that are considered to be coupled together.
    For example, if we want to couple `j_1` and `j_4`, the indices would be 1
    and 4. If a state has already been coupled, it is referenced by the
    smallest index that is coupled, so if `j_2` and `j_4` has already been
    coupled to some `j_{24}`, then this value can be coupled by referencing it
    with index 2. The final element of the sublist is the quantum number of the
    coupled state. So putting everything together, into a valid sublist for
    ``jcoupling``, if `j_1` and `j_2` are coupled to an angular momentum space
    with quantum number `j_{12}` with the value ``j12``, the sublist would be
    ``(1,2,j12)``, N-1 of these sublists are used in the list for
    ``jcoupling``.

    Note the ``jcoupling`` parameter is optional, if it is not specified, the
    default coupling is taken. This default value is to coupled the spaces in
    order and take the quantum number of the coupling to be the maximum value.
    For example, if the spin spaces are `j_1`, `j_2`, `j_3`, `j_4`, then the
    default coupling couples `j_1` and `j_2` to `j_{12}=j_1+j_2`, then,
    `j_{12}` and `j_3` are coupled to `j_{123}=j_{12}+j_3`, and finally
    `j_{123}` and `j_4` to `j=j_{123}+j_4`. The jcoupling value that would
    correspond to this is:

        ``((1,2,j1+j2),(1,3,j1+j2+j3))``

    Parameters
    ==========

    args : tuple
        The arguments that must be passed are ``j``, ``m``, ``jn``, and
        ``jcoupling``. The ``j`` value is the total angular momentum. The ``m``
        value is the eigenvalue of the Jz spin operator. The ``jn`` list are
        the j values of argular momentum spaces coupled together. The
        ``jcoupling`` parameter is an optional parameter defining how the spaces
        are coupled together. See the above description for how these coupling
        parameters are defined.

    Examples
    ========

    Defining simple spin states, both numerical and symbolic:

        >>> from sympy.physics.quantum.spin import JzKetCoupled
        >>> from sympy import symbols
        >>> JzKetCoupled(1, 0, (1, 1))
        |1,0,j1=1,j2=1>
        >>> j, m, j1, j2 = symbols(\'j m j1 j2\')
        >>> JzKetCoupled(j, m, (j1, j2))
        |j,m,j1=j1,j2=j2>

    Defining coupled spin states for more than 2 coupled spaces with various
    coupling parameters:

        >>> JzKetCoupled(2, 1, (1, 1, 1))
        |2,1,j1=1,j2=1,j3=1,j(1,2)=2>
        >>> JzKetCoupled(2, 1, (1, 1, 1), ((1,2,2),(1,3,2)) )
        |2,1,j1=1,j2=1,j3=1,j(1,2)=2>
        >>> JzKetCoupled(2, 1, (1, 1, 1), ((2,3,1),(1,2,2)) )
        |2,1,j1=1,j2=1,j3=1,j(2,3)=1>

    Rewriting the JzKetCoupled in terms of eigenkets of the Jx operator:
    Note: that the resulting eigenstates are JxKetCoupled

        >>> JzKetCoupled(1,1,(1,1)).rewrite("Jx")
        |1,-1,j1=1,j2=1>/2 - sqrt(2)*|1,0,j1=1,j2=1>/2 + |1,1,j1=1,j2=1>/2

    The rewrite method can be used to convert a coupled state to an uncoupled
    state. This is done by passing coupled=False to the rewrite function:

        >>> JzKetCoupled(1, 0, (1, 1)).rewrite(\'Jz\', coupled=False)
        -sqrt(2)*|1,-1>x|1,1>/2 + sqrt(2)*|1,1>x|1,-1>/2

    Get the vector representation of a state in terms of the basis elements
    of the Jx operator:

        >>> from sympy.physics.quantum.represent import represent
        >>> from sympy.physics.quantum.spin import Jx
        >>> from sympy import S
        >>> represent(JzKetCoupled(1,-1,(S(1)/2,S(1)/2)), basis=Jx)
        Matrix([
        [        0],
        [      1/2],
        [sqrt(2)/2],
        [      1/2]])

    See Also
    ========

    JzKet: Normal spin eigenstates
    uncouple: Uncoupling of coupling spin states
    couple: Coupling of uncoupled spin states

    '''
    @classmethod
    def dual_class(self): ...
    @classmethod
    def uncoupled_class(self): ...

class JzBraCoupled(CoupledSpinState, Bra):
    """Coupled eigenbra of Jz.

    See the JzKetCoupled for the usage of coupled spin eigenstates.

    See Also
    ========

    JzKetCoupled: Usage of coupled spin states

    """
    @classmethod
    def dual_class(self): ...
    @classmethod
    def uncoupled_class(self): ...

def couple(expr, jcoupling_list: Incomplete | None = None):
    """ Couple a tensor product of spin states

    This function can be used to couple an uncoupled tensor product of spin
    states. All of the eigenstates to be coupled must be of the same class. It
    will return a linear combination of eigenstates that are subclasses of
    CoupledSpinState determined by Clebsch-Gordan angular momentum coupling
    coefficients.

    Parameters
    ==========

    expr : Expr
        An expression involving TensorProducts of spin states to be coupled.
        Each state must be a subclass of SpinState and they all must be the
        same class.

    jcoupling_list : list or tuple
        Elements of this list are sub-lists of length 2 specifying the order of
        the coupling of the spin spaces. The length of this must be N-1, where N
        is the number of states in the tensor product to be coupled. The
        elements of this sublist are the same as the first two elements of each
        sublist in the ``jcoupling`` parameter defined for JzKetCoupled. If this
        parameter is not specified, the default value is taken, which couples
        the first and second product basis spaces, then couples this new coupled
        space to the third product space, etc

    Examples
    ========

    Couple a tensor product of numerical states for two spaces:

        >>> from sympy.physics.quantum.spin import JzKet, couple
        >>> from sympy.physics.quantum.tensorproduct import TensorProduct
        >>> couple(TensorProduct(JzKet(1,0), JzKet(1,1)))
        -sqrt(2)*|1,1,j1=1,j2=1>/2 + sqrt(2)*|2,1,j1=1,j2=1>/2


    Numerical coupling of three spaces using the default coupling method, i.e.
    first and second spaces couple, then this couples to the third space:

        >>> couple(TensorProduct(JzKet(1,1), JzKet(1,1), JzKet(1,0)))
        sqrt(6)*|2,2,j1=1,j2=1,j3=1,j(1,2)=2>/3 + sqrt(3)*|3,2,j1=1,j2=1,j3=1,j(1,2)=2>/3

    Perform this same coupling, but we define the coupling to first couple
    the first and third spaces:

        >>> couple(TensorProduct(JzKet(1,1), JzKet(1,1), JzKet(1,0)), ((1,3),(1,2)) )
        sqrt(2)*|2,2,j1=1,j2=1,j3=1,j(1,3)=1>/2 - sqrt(6)*|2,2,j1=1,j2=1,j3=1,j(1,3)=2>/6 + sqrt(3)*|3,2,j1=1,j2=1,j3=1,j(1,3)=2>/3

    Couple a tensor product of symbolic states:

        >>> from sympy import symbols
        >>> j1,m1,j2,m2 = symbols('j1 m1 j2 m2')
        >>> couple(TensorProduct(JzKet(j1,m1), JzKet(j2,m2)))
        Sum(CG(j1, m1, j2, m2, j, m1 + m2)*|j,m1 + m2,j1=j1,j2=j2>, (j, m1 + m2, j1 + j2))

    """
def uncouple(expr, jn: Incomplete | None = None, jcoupling_list: Incomplete | None = None):
    """ Uncouple a coupled spin state

    Gives the uncoupled representation of a coupled spin state. Arguments must
    be either a spin state that is a subclass of CoupledSpinState or a spin
    state that is a subclass of SpinState and an array giving the j values
    of the spaces that are to be coupled

    Parameters
    ==========

    expr : Expr
        The expression containing states that are to be coupled. If the states
        are a subclass of SpinState, the ``jn`` and ``jcoupling`` parameters
        must be defined. If the states are a subclass of CoupledSpinState,
        ``jn`` and ``jcoupling`` will be taken from the state.

    jn : list or tuple
        The list of the j-values that are coupled. If state is a
        CoupledSpinState, this parameter is ignored. This must be defined if
        state is not a subclass of CoupledSpinState. The syntax of this
        parameter is the same as the ``jn`` parameter of JzKetCoupled.

    jcoupling_list : list or tuple
        The list defining how the j-values are coupled together. If state is a
        CoupledSpinState, this parameter is ignored. This must be defined if
        state is not a subclass of CoupledSpinState. The syntax of this
        parameter is the same as the ``jcoupling`` parameter of JzKetCoupled.

    Examples
    ========

    Uncouple a numerical state using a CoupledSpinState state:

        >>> from sympy.physics.quantum.spin import JzKetCoupled, uncouple
        >>> from sympy import S
        >>> uncouple(JzKetCoupled(1, 0, (S(1)/2, S(1)/2)))
        sqrt(2)*|1/2,-1/2>x|1/2,1/2>/2 + sqrt(2)*|1/2,1/2>x|1/2,-1/2>/2

    Perform the same calculation using a SpinState state:

        >>> from sympy.physics.quantum.spin import JzKet
        >>> uncouple(JzKet(1, 0), (S(1)/2, S(1)/2))
        sqrt(2)*|1/2,-1/2>x|1/2,1/2>/2 + sqrt(2)*|1/2,1/2>x|1/2,-1/2>/2

    Uncouple a numerical state of three coupled spaces using a CoupledSpinState state:

        >>> uncouple(JzKetCoupled(1, 1, (1, 1, 1), ((1,3,1),(1,2,1)) ))
        |1,-1>x|1,1>x|1,1>/2 - |1,0>x|1,0>x|1,1>/2 + |1,1>x|1,0>x|1,0>/2 - |1,1>x|1,1>x|1,-1>/2

    Perform the same calculation using a SpinState state:

        >>> uncouple(JzKet(1, 1), (1, 1, 1), ((1,3,1),(1,2,1)) )
        |1,-1>x|1,1>x|1,1>/2 - |1,0>x|1,0>x|1,1>/2 + |1,1>x|1,0>x|1,0>/2 - |1,1>x|1,1>x|1,-1>/2

    Uncouple a symbolic state using a CoupledSpinState state:

        >>> from sympy import symbols
        >>> j,m,j1,j2 = symbols('j m j1 j2')
        >>> uncouple(JzKetCoupled(j, m, (j1, j2)))
        Sum(CG(j1, m1, j2, m2, j, m)*|j1,m1>x|j2,m2>, (m1, -j1, j1), (m2, -j2, j2))

    Perform the same calculation using a SpinState state

        >>> uncouple(JzKet(j, m), (j1, j2))
        Sum(CG(j1, m1, j2, m2, j, m)*|j1,m1>x|j2,m2>, (m1, -j1, j1), (m2, -j2, j2))

    """
