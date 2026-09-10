from _typeshed import Incomplete
from sympy.core.basic import Basic

__all__ = ['generate_gate_rules', 'generate_equivalent_ids', 'GateIdentity', 'bfs_identity_search', 'random_identity_search', 'is_scalar_sparse_matrix', 'is_scalar_nonsparse_matrix', 'is_degenerate', 'is_reducible']

def is_scalar_sparse_matrix(circuit, nqubits, identity_only, eps: float = 1e-11):
    """Checks if a given scipy.sparse matrix is a scalar matrix.

    A scalar matrix is such that B = bI, where B is the scalar
    matrix, b is some scalar multiple, and I is the identity
    matrix.  A scalar matrix would have only the element b along
    it's main diagonal and zeroes elsewhere.

    Parameters
    ==========

    circuit : Gate tuple
        Sequence of quantum gates representing a quantum circuit
    nqubits : int
        Number of qubits in the circuit
    identity_only : bool
        Check for only identity matrices
    eps : number
        The tolerance value for zeroing out elements in the matrix.
        Values in the range [-eps, +eps] will be changed to a zero.
    """
def is_scalar_nonsparse_matrix(circuit, nqubits, identity_only, eps: Incomplete | None = None):
    """Checks if a given circuit, in matrix form, is equivalent to
    a scalar value.

    Parameters
    ==========

    circuit : Gate tuple
        Sequence of quantum gates representing a quantum circuit
    nqubits : int
        Number of qubits in the circuit
    identity_only : bool
        Check for only identity matrices
    eps : number
        This argument is ignored. It is just for signature compatibility with
        is_scalar_sparse_matrix.

    Note: Used in situations when is_scalar_sparse_matrix has bugs
    """
is_scalar_matrix = is_scalar_sparse_matrix
is_scalar_matrix = is_scalar_nonsparse_matrix

def generate_gate_rules(gate_seq, return_as_muls: bool = False):
    """Returns a set of gate rules.  Each gate rules is represented
    as a 2-tuple of tuples or Muls.  An empty tuple represents an arbitrary
    scalar value.

    This function uses the four operations (LL, LR, RL, RR)
    to generate the gate rules.

    A gate rule is an expression such as ABC = D or AB = CD, where
    A, B, C, and D are gates.  Each value on either side of the
    equal sign represents a circuit.  The four operations allow
    one to find a set of equivalent circuits from a gate identity.
    The letters denoting the operation tell the user what
    activities to perform on each expression.  The first letter
    indicates which side of the equal sign to focus on.  The
    second letter indicates which gate to focus on given the
    side.  Once this information is determined, the inverse
    of the gate is multiplied on both circuits to create a new
    gate rule.

    For example, given the identity, ABCD = 1, a LL operation
    means look at the left value and multiply both left sides by the
    inverse of the leftmost gate A.  If A is Hermitian, the inverse
    of A is still A.  The resulting new rule is BCD = A.

    The following is a summary of the four operations.  Assume
    that in the examples, all gates are Hermitian.

        LL : left circuit, left multiply
             ABCD = E -> AABCD = AE -> BCD = AE
        LR : left circuit, right multiply
             ABCD = E -> ABCDD = ED -> ABC = ED
        RL : right circuit, left multiply
             ABC = ED -> EABC = EED -> EABC = D
        RR : right circuit, right multiply
             AB = CD -> ABD = CDD -> ABD = C

    The number of gate rules generated is n*(n+1), where n
    is the number of gates in the sequence (unproven).

    Parameters
    ==========

    gate_seq : Gate tuple, Mul, or Number
        A variable length tuple or Mul of Gates whose product is equal to
        a scalar matrix
    return_as_muls : bool
        True to return a set of Muls; False to return a set of tuples

    Examples
    ========

    Find the gate rules of the current circuit using tuples:

    >>> from sympy.physics.quantum.identitysearch import generate_gate_rules
    >>> from sympy.physics.quantum.gate import X, Y, Z
    >>> x = X(0); y = Y(0); z = Z(0)
    >>> generate_gate_rules((x, x))
    {((X(0),), (X(0),)), ((X(0), X(0)), ())}

    >>> generate_gate_rules((x, y, z))
    {((), (X(0), Z(0), Y(0))), ((), (Y(0), X(0), Z(0))),
     ((), (Z(0), Y(0), X(0))), ((X(0),), (Z(0), Y(0))),
     ((Y(0),), (X(0), Z(0))), ((Z(0),), (Y(0), X(0))),
     ((X(0), Y(0)), (Z(0),)), ((Y(0), Z(0)), (X(0),)),
     ((Z(0), X(0)), (Y(0),)), ((X(0), Y(0), Z(0)), ()),
     ((Y(0), Z(0), X(0)), ()), ((Z(0), X(0), Y(0)), ())}

    Find the gate rules of the current circuit using Muls:

    >>> generate_gate_rules(x*x, return_as_muls=True)
    {(1, 1)}

    >>> generate_gate_rules(x*y*z, return_as_muls=True)
    {(1, X(0)*Z(0)*Y(0)), (1, Y(0)*X(0)*Z(0)),
     (1, Z(0)*Y(0)*X(0)), (X(0)*Y(0), Z(0)),
     (Y(0)*Z(0), X(0)), (Z(0)*X(0), Y(0)),
     (X(0)*Y(0)*Z(0), 1), (Y(0)*Z(0)*X(0), 1),
     (Z(0)*X(0)*Y(0), 1), (X(0), Z(0)*Y(0)),
     (Y(0), X(0)*Z(0)), (Z(0), Y(0)*X(0))}
    """
def generate_equivalent_ids(gate_seq, return_as_muls: bool = False):
    """Returns a set of equivalent gate identities.

    A gate identity is a quantum circuit such that the product
    of the gates in the circuit is equal to a scalar value.
    For example, XYZ = i, where X, Y, Z are the Pauli gates and
    i is the imaginary value, is considered a gate identity.

    This function uses the four operations (LL, LR, RL, RR)
    to generate the gate rules and, subsequently, to locate equivalent
    gate identities.

    Note that all equivalent identities are reachable in n operations
    from the starting gate identity, where n is the number of gates
    in the sequence.

    The max number of gate identities is 2n, where n is the number
    of gates in the sequence (unproven).

    Parameters
    ==========

    gate_seq : Gate tuple, Mul, or Number
        A variable length tuple or Mul of Gates whose product is equal to
        a scalar matrix.
    return_as_muls: bool
        True to return as Muls; False to return as tuples

    Examples
    ========

    Find equivalent gate identities from the current circuit with tuples:

    >>> from sympy.physics.quantum.identitysearch import generate_equivalent_ids
    >>> from sympy.physics.quantum.gate import X, Y, Z
    >>> x = X(0); y = Y(0); z = Z(0)
    >>> generate_equivalent_ids((x, x))
    {(X(0), X(0))}

    >>> generate_equivalent_ids((x, y, z))
    {(X(0), Y(0), Z(0)), (X(0), Z(0), Y(0)), (Y(0), X(0), Z(0)),
     (Y(0), Z(0), X(0)), (Z(0), X(0), Y(0)), (Z(0), Y(0), X(0))}

    Find equivalent gate identities from the current circuit with Muls:

    >>> generate_equivalent_ids(x*x, return_as_muls=True)
    {1}

    >>> generate_equivalent_ids(x*y*z, return_as_muls=True)
    {X(0)*Y(0)*Z(0), X(0)*Z(0)*Y(0), Y(0)*X(0)*Z(0),
     Y(0)*Z(0)*X(0), Z(0)*X(0)*Y(0), Z(0)*Y(0)*X(0)}
    """

class GateIdentity(Basic):
    """Wrapper class for circuits that reduce to a scalar value.

    A gate identity is a quantum circuit such that the product
    of the gates in the circuit is equal to a scalar value.
    For example, XYZ = i, where X, Y, Z are the Pauli gates and
    i is the imaginary value, is considered a gate identity.

    Parameters
    ==========

    args : Gate tuple
        A variable length tuple of Gates that form an identity.

    Examples
    ========

    Create a GateIdentity and look at its attributes:

    >>> from sympy.physics.quantum.identitysearch import GateIdentity
    >>> from sympy.physics.quantum.gate import X, Y, Z
    >>> x = X(0); y = Y(0); z = Z(0)
    >>> an_identity = GateIdentity(x, y, z)
    >>> an_identity.circuit
    X(0)*Y(0)*Z(0)

    >>> an_identity.equivalent_ids
    {(X(0), Y(0), Z(0)), (X(0), Z(0), Y(0)), (Y(0), X(0), Z(0)),
     (Y(0), Z(0), X(0)), (Z(0), X(0), Y(0)), (Z(0), Y(0), X(0))}
    """
    def __new__(cls, *args): ...
    @property
    def circuit(self): ...
    @property
    def gate_rules(self): ...
    @property
    def equivalent_ids(self): ...
    @property
    def sequence(self): ...

def is_degenerate(identity_set, gate_identity):
    """Checks if a gate identity is a permutation of another identity.

    Parameters
    ==========

    identity_set : set
        A Python set with GateIdentity objects.
    gate_identity : GateIdentity
        The GateIdentity to check for existence in the set.

    Examples
    ========

    Check if the identity is a permutation of another identity:

    >>> from sympy.physics.quantum.identitysearch import (
    ...     GateIdentity, is_degenerate)
    >>> from sympy.physics.quantum.gate import X, Y, Z
    >>> x = X(0); y = Y(0); z = Z(0)
    >>> an_identity = GateIdentity(x, y, z)
    >>> id_set = {an_identity}
    >>> another_id = (y, z, x)
    >>> is_degenerate(id_set, another_id)
    True

    >>> another_id = (x, x)
    >>> is_degenerate(id_set, another_id)
    False
    """
def is_reducible(circuit, nqubits, begin, end):
    """Determines if a circuit is reducible by checking
    if its subcircuits are scalar values.

    Parameters
    ==========

    circuit : Gate tuple
        A tuple of Gates representing a circuit.  The circuit to check
        if a gate identity is contained in a subcircuit.
    nqubits : int
        The number of qubits the circuit operates on.
    begin : int
        The leftmost gate in the circuit to include in a subcircuit.
    end : int
        The rightmost gate in the circuit to include in a subcircuit.

    Examples
    ========

    Check if the circuit can be reduced:

    >>> from sympy.physics.quantum.identitysearch import is_reducible
    >>> from sympy.physics.quantum.gate import X, Y, Z
    >>> x = X(0); y = Y(0); z = Z(0)
    >>> is_reducible((x, y, z), 1, 0, 3)
    True

    Check if an interval in the circuit can be reduced:

    >>> is_reducible((x, y, z), 1, 1, 3)
    False

    >>> is_reducible((x, y, y), 1, 1, 3)
    True
    """
def bfs_identity_search(gate_list, nqubits, max_depth: Incomplete | None = None, identity_only: bool = False):
    """Constructs a set of gate identities from the list of possible gates.

    Performs a breadth first search over the space of gate identities.
    This allows the finding of the shortest gate identities first.

    Parameters
    ==========

    gate_list : list, Gate
        A list of Gates from which to search for gate identities.
    nqubits : int
        The number of qubits the quantum circuit operates on.
    max_depth : int
        The longest quantum circuit to construct from gate_list.
    identity_only : bool
        True to search for gate identities that reduce to identity;
        False to search for gate identities that reduce to a scalar.

    Examples
    ========

    Find a list of gate identities:

    >>> from sympy.physics.quantum.identitysearch import bfs_identity_search
    >>> from sympy.physics.quantum.gate import X, Y, Z
    >>> x = X(0); y = Y(0); z = Z(0)
    >>> bfs_identity_search([x], 1, max_depth=2)
    {GateIdentity(X(0), X(0))}

    >>> bfs_identity_search([x, y, z], 1)
    {GateIdentity(X(0), X(0)), GateIdentity(Y(0), Y(0)),
     GateIdentity(Z(0), Z(0)), GateIdentity(X(0), Y(0), Z(0))}

    Find a list of identities that only equal to 1:

    >>> bfs_identity_search([x, y, z], 1, identity_only=True)
    {GateIdentity(X(0), X(0)), GateIdentity(Y(0), Y(0)),
     GateIdentity(Z(0), Z(0))}
    """
def random_identity_search(gate_list, numgates, nqubits):
    """Randomly selects numgates from gate_list and checks if it is
    a gate identity.

    If the circuit is a gate identity, the circuit is returned;
    Otherwise, None is returned.
    """
