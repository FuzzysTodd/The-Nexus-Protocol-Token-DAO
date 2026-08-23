from sympy.core.add import Add as Add
from sympy.core.containers import Tuple as Tuple
from sympy.core.function import expand as expand
from sympy.core.mul import Mul as Mul
from sympy.core.singleton import S as S
from sympy.functions.elementary.exponential import log as log
from sympy.physics.quantum.dagger import Dagger as Dagger
from sympy.physics.quantum.matrixutils import numpy_ndarray as numpy_ndarray, scipy_sparse_matrix as scipy_sparse_matrix, to_numpy as to_numpy
from sympy.physics.quantum.operator import HermitianOperator as HermitianOperator
from sympy.physics.quantum.represent import represent as represent
from sympy.physics.quantum.tensorproduct import TensorProduct as TensorProduct, tensor_product_simp as tensor_product_simp
from sympy.physics.quantum.trace import Tr as Tr
from sympy.printing.pretty.stringpict import prettyForm as prettyForm

class Density(HermitianOperator):
    """Density operator for representing mixed states.

    TODO: Density operator support for Qubits

    Parameters
    ==========

    values : tuples/lists
    Each tuple/list should be of form (state, prob) or [state,prob]

    Examples
    ========

    Create a density operator with 2 states represented by Kets.

    >>> from sympy.physics.quantum.state import Ket
    >>> from sympy.physics.quantum.density import Density
    >>> d = Density([Ket(0), 0.5], [Ket(1),0.5])
    >>> d
    Density((|0>, 0.5),(|1>, 0.5))

    """
    def states(self):
        """Return list of all states.

        Examples
        ========

        >>> from sympy.physics.quantum.state import Ket
        >>> from sympy.physics.quantum.density import Density
        >>> d = Density([Ket(0), 0.5], [Ket(1),0.5])
        >>> d.states()
        (|0>, |1>)

        """
    def probs(self):
        """Return list of all probabilities.

        Examples
        ========

        >>> from sympy.physics.quantum.state import Ket
        >>> from sympy.physics.quantum.density import Density
        >>> d = Density([Ket(0), 0.5], [Ket(1),0.5])
        >>> d.probs()
        (0.5, 0.5)

        """
    def get_state(self, index):
        """Return specific state by index.

        Parameters
        ==========

        index : index of state to be returned

        Examples
        ========

        >>> from sympy.physics.quantum.state import Ket
        >>> from sympy.physics.quantum.density import Density
        >>> d = Density([Ket(0), 0.5], [Ket(1),0.5])
        >>> d.states()[1]
        |1>

        """
    def get_prob(self, index):
        """Return probability of specific state by index.

        Parameters
        ===========

        index : index of states whose probability is returned.

        Examples
        ========

        >>> from sympy.physics.quantum.state import Ket
        >>> from sympy.physics.quantum.density import Density
        >>> d = Density([Ket(0), 0.5], [Ket(1),0.5])
        >>> d.probs()[1]
        0.500000000000000

        """
    def apply_op(self, op):
        """op will operate on each individual state.

        Parameters
        ==========

        op : Operator

        Examples
        ========

        >>> from sympy.physics.quantum.state import Ket
        >>> from sympy.physics.quantum.density import Density
        >>> from sympy.physics.quantum.operator import Operator
        >>> A = Operator('A')
        >>> d = Density([Ket(0), 0.5], [Ket(1),0.5])
        >>> d.apply_op(A)
        Density((A*|0>, 0.5),(A*|1>, 0.5))

        """
    def doit(self, **hints):
        """Expand the density operator into an outer product format.

        Examples
        ========

        >>> from sympy.physics.quantum.state import Ket
        >>> from sympy.physics.quantum.density import Density
        >>> from sympy.physics.quantum.operator import Operator
        >>> A = Operator('A')
        >>> d = Density([Ket(0), 0.5], [Ket(1),0.5])
        >>> d.doit()
        0.5*|0><0| + 0.5*|1><1|

        """
    def entropy(self):
        """ Compute the entropy of a density matrix.

        Refer to density.entropy() method  for examples.
        """

def entropy(density):
    """Compute the entropy of a matrix/density object.

    This computes -Tr(density*ln(density)) using the eigenvalue decomposition
    of density, which is given as either a Density instance or a matrix
    (numpy.ndarray, sympy.Matrix or scipy.sparse).

    Parameters
    ==========

    density : density matrix of type Density, SymPy matrix,
    scipy.sparse or numpy.ndarray

    Examples
    ========

    >>> from sympy.physics.quantum.density import Density, entropy
    >>> from sympy.physics.quantum.spin import JzKet
    >>> from sympy import S
    >>> up = JzKet(S(1)/2,S(1)/2)
    >>> down = JzKet(S(1)/2,-S(1)/2)
    >>> d = Density((up,S(1)/2),(down,S(1)/2))
    >>> entropy(d)
    log(2)/2

    """
def fidelity(state1, state2):
    """ Computes the fidelity [1]_ between two quantum states

    The arguments provided to this function should be a square matrix or a
    Density object. If it is a square matrix, it is assumed to be diagonalizable.

    Parameters
    ==========

    state1, state2 : a density matrix or Matrix


    Examples
    ========

    >>> from sympy import S, sqrt
    >>> from sympy.physics.quantum.dagger import Dagger
    >>> from sympy.physics.quantum.spin import JzKet
    >>> from sympy.physics.quantum.density import fidelity
    >>> from sympy.physics.quantum.represent import represent
    >>>
    >>> up = JzKet(S(1)/2,S(1)/2)
    >>> down = JzKet(S(1)/2,-S(1)/2)
    >>> amp = 1/sqrt(2)
    >>> updown = (amp*up) + (amp*down)
    >>>
    >>> # represent turns Kets into matrices
    >>> up_dm = represent(up*Dagger(up))
    >>> down_dm = represent(down*Dagger(down))
    >>> updown_dm = represent(updown*Dagger(updown))
    >>>
    >>> fidelity(up_dm, up_dm)
    1
    >>> fidelity(up_dm, down_dm) #orthogonal states
    0
    >>> fidelity(up_dm, updown_dm).evalf().round(3)
    0.707

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Fidelity_of_quantum_states

    """
