from sympy.physics.quantum.state import Bra, Ket, State

__all__ = ['Qubit', 'QubitBra', 'IntQubit', 'IntQubitBra', 'qubit_to_matrix', 'matrix_to_qubit', 'matrix_to_density', 'measure_all', 'measure_partial', 'measure_partial_oneshot', 'measure_all_oneshot']

class QubitState(State):
    """Base class for Qubit and QubitBra."""
    @property
    def dimension(self):
        """The number of Qubits in the state."""
    @property
    def nqubits(self): ...
    @property
    def qubit_values(self):
        """Returns the values of the qubits as a tuple."""
    def __len__(self) -> int: ...
    def __getitem__(self, bit): ...
    def flip(self, *bits):
        """Flip the bit(s) given."""

class Qubit(QubitState, Ket):
    """A multi-qubit ket in the computational (z) basis.

    We use the normal convention that the least significant qubit is on the
    right, so ``|00001>`` has a 1 in the least significant qubit.

    Parameters
    ==========

    values : list, str
        The qubit values as a list of ints ([0,0,0,1,1,]) or a string ('011').

    Examples
    ========

    Create a qubit in a couple of different ways and look at their attributes:

        >>> from sympy.physics.quantum.qubit import Qubit
        >>> Qubit(0,0,0)
        |000>
        >>> q = Qubit('0101')
        >>> q
        |0101>

        >>> q.nqubits
        4
        >>> len(q)
        4
        >>> q.dimension
        4
        >>> q.qubit_values
        (0, 1, 0, 1)

    We can flip the value of an individual qubit:

        >>> q.flip(1)
        |0111>

    We can take the dagger of a Qubit to get a bra:

        >>> from sympy.physics.quantum.dagger import Dagger
        >>> Dagger(q)
        <0101|
        >>> type(Dagger(q))
        <class 'sympy.physics.quantum.qubit.QubitBra'>

    Inner products work as expected:

        >>> ip = Dagger(q)*q
        >>> ip
        <0101|0101>
        >>> ip.doit()
        1
    """
    @classmethod
    def dual_class(self): ...

class QubitBra(QubitState, Bra):
    """A multi-qubit bra in the computational (z) basis.

    We use the normal convention that the least significant qubit is on the
    right, so ``|00001>`` has a 1 in the least significant qubit.

    Parameters
    ==========

    values : list, str
        The qubit values as a list of ints ([0,0,0,1,1,]) or a string ('011').

    See also
    ========

    Qubit: Examples using qubits

    """
    @classmethod
    def dual_class(self): ...

class IntQubitState(QubitState):
    """A base class for qubits that work with binary representations."""
    def as_int(self):
        """Return the numerical value of the qubit."""

class IntQubit(IntQubitState, Qubit):
    """A qubit ket that store integers as binary numbers in qubit values.

    The differences between this class and ``Qubit`` are:

    * The form of the constructor.
    * The qubit values are printed as their corresponding integer, rather
      than the raw qubit values. The internal storage format of the qubit
      values in the same as ``Qubit``.

    Parameters
    ==========

    values : int, tuple
        If a single argument, the integer we want to represent in the qubit
        values. This integer will be represented using the fewest possible
        number of qubits.
        If a pair of integers and the second value is more than one, the first
        integer gives the integer to represent in binary form and the second
        integer gives the number of qubits to use.
        List of zeros and ones is also accepted to generate qubit by bit pattern.

    nqubits : int
        The integer that represents the number of qubits.
        This number should be passed with keyword ``nqubits=N``.
        You can use this in order to avoid ambiguity of Qubit-style tuple of bits.
        Please see the example below for more details.

    Examples
    ========

    Create a qubit for the integer 5:

        >>> from sympy.physics.quantum.qubit import IntQubit
        >>> from sympy.physics.quantum.qubit import Qubit
        >>> q = IntQubit(5)
        >>> q
        |5>

    We can also create an ``IntQubit`` by passing a ``Qubit`` instance.

        >>> q = IntQubit(Qubit('101'))
        >>> q
        |5>
        >>> q.as_int()
        5
        >>> q.nqubits
        3
        >>> q.qubit_values
        (1, 0, 1)

    We can go back to the regular qubit form.

        >>> Qubit(q)
        |101>

    Please note that ``IntQubit`` also accepts a ``Qubit``-style list of bits.
    So, the code below yields qubits 3, not a single bit ``1``.

        >>> IntQubit(1, 1)
        |3>

    To avoid ambiguity, use ``nqubits`` parameter.
    Use of this keyword is recommended especially when you provide the values by variables.

        >>> IntQubit(1, nqubits=1)
        |1>
        >>> a = 1
        >>> IntQubit(a, nqubits=1)
        |1>
    """
    @classmethod
    def dual_class(self): ...

class IntQubitBra(IntQubitState, QubitBra):
    """A qubit bra that store integers as binary numbers in qubit values."""
    @classmethod
    def dual_class(self): ...

def matrix_to_qubit(matrix):
    """Convert from the matrix repr. to a sum of Qubit objects.

    Parameters
    ----------
    matrix : Matrix, numpy.matrix, scipy.sparse
        The matrix to build the Qubit representation of. This works with
        SymPy matrices, numpy matrices and scipy.sparse sparse matrices.

    Examples
    ========

    Represent a state and then go back to its qubit form:

        >>> from sympy.physics.quantum.qubit import matrix_to_qubit, Qubit
        >>> from sympy.physics.quantum.represent import represent
        >>> q = Qubit('01')
        >>> matrix_to_qubit(represent(q))
        |01>
    """
def matrix_to_density(mat):
    """
    Works by finding the eigenvectors and eigenvalues of the matrix.
    We know we can decompose rho by doing:
    sum(EigenVal*|Eigenvect><Eigenvect|)
    """
def qubit_to_matrix(qubit, format: str = 'sympy'):
    """Converts an Add/Mul of Qubit objects into it's matrix representation

    This function is the inverse of ``matrix_to_qubit`` and is a shorthand
    for ``represent(qubit)``.
    """
def measure_all(qubit, format: str = 'sympy', normalize: bool = True):
    """Perform an ensemble measurement of all qubits.

    Parameters
    ==========

    qubit : Qubit, Add
        The qubit to measure. This can be any Qubit or a linear combination
        of them.
    format : str
        The format of the intermediate matrices to use. Possible values are
        ('sympy','numpy','scipy.sparse'). Currently only 'sympy' is
        implemented.

    Returns
    =======

    result : list
        A list that consists of primitive states and their probabilities.

    Examples
    ========

        >>> from sympy.physics.quantum.qubit import Qubit, measure_all
        >>> from sympy.physics.quantum.gate import H
        >>> from sympy.physics.quantum.qapply import qapply

        >>> c = H(0)*H(1)*Qubit('00')
        >>> c
        H(0)*H(1)*|00>
        >>> q = qapply(c)
        >>> measure_all(q)
        [(|00>, 1/4), (|01>, 1/4), (|10>, 1/4), (|11>, 1/4)]
    """
def measure_partial(qubit, bits, format: str = 'sympy', normalize: bool = True):
    """Perform a partial ensemble measure on the specified qubits.

    Parameters
    ==========

    qubits : Qubit
        The qubit to measure.  This can be any Qubit or a linear combination
        of them.
    bits : tuple
        The qubits to measure.
    format : str
        The format of the intermediate matrices to use. Possible values are
        ('sympy','numpy','scipy.sparse'). Currently only 'sympy' is
        implemented.

    Returns
    =======

    result : list
        A list that consists of primitive states and their probabilities.

    Examples
    ========

        >>> from sympy.physics.quantum.qubit import Qubit, measure_partial
        >>> from sympy.physics.quantum.gate import H
        >>> from sympy.physics.quantum.qapply import qapply

        >>> c = H(0)*H(1)*Qubit('00')
        >>> c
        H(0)*H(1)*|00>
        >>> q = qapply(c)
        >>> measure_partial(q, (0,))
        [(sqrt(2)*|00>/2 + sqrt(2)*|10>/2, 1/2), (sqrt(2)*|01>/2 + sqrt(2)*|11>/2, 1/2)]
    """
def measure_partial_oneshot(qubit, bits, format: str = 'sympy'):
    """Perform a partial oneshot measurement on the specified qubits.

    A oneshot measurement is equivalent to performing a measurement on a
    quantum system. This type of measurement does not return the probabilities
    like an ensemble measurement does, but rather returns *one* of the
    possible resulting states. The exact state that is returned is determined
    by picking a state randomly according to the ensemble probabilities.

    Parameters
    ----------
    qubits : Qubit
        The qubit to measure.  This can be any Qubit or a linear combination
        of them.
    bits : tuple
        The qubits to measure.
    format : str
        The format of the intermediate matrices to use. Possible values are
        ('sympy','numpy','scipy.sparse'). Currently only 'sympy' is
        implemented.

    Returns
    -------
    result : Qubit
        The qubit that the system collapsed to upon measurement.
    """
def measure_all_oneshot(qubit, format: str = 'sympy'):
    """Perform a oneshot ensemble measurement on all qubits.

    A oneshot measurement is equivalent to performing a measurement on a
    quantum system. This type of measurement does not return the probabilities
    like an ensemble measurement does, but rather returns *one* of the
    possible resulting states. The exact state that is returned is determined
    by picking a state randomly according to the ensemble probabilities.

    Parameters
    ----------
    qubits : Qubit
        The qubit to measure.  This can be any Qubit or a linear combination
        of them.
    format : str
        The format of the intermediate matrices to use. Possible values are
        ('sympy','numpy','scipy.sparse'). Currently only 'sympy' is
        implemented.

    Returns
    -------
    result : Qubit
        The qubit that the system collapsed to upon measurement.
    """
