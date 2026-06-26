from _typeshed import Incomplete
from sympy.physics.quantum.gate import OneQubitGate

__all__ = ['CircuitPlot', 'circuit_plot', 'labeller', 'Mz', 'Mx', 'CreateOneQubitGate', 'CreateCGate']

class CircuitPlot:
    """A class for managing a circuit plot."""
    scale: float
    fontsize: float
    linewidth: float
    control_radius: float
    not_radius: float
    swap_delta: float
    labels: list[str]
    inits: dict[str, str]
    label_buffer: float
    circuit: Incomplete
    ngates: Incomplete
    nqubits: Incomplete
    def __init__(self, c, nqubits, **kwargs) -> None: ...
    def update(self, kwargs) -> None:
        """Load the kwargs into the instance dict."""
    def one_qubit_box(self, t, gate_idx, wire_idx) -> None:
        """Draw a box for a single qubit gate."""
    def two_qubit_box(self, t, gate_idx, wire_idx) -> None:
        """Draw a box for a two qubit gate. Does not work yet.
        """
    def control_line(self, gate_idx, min_wire, max_wire) -> None:
        """Draw a vertical control line."""
    def control_point(self, gate_idx, wire_idx) -> None:
        """Draw a control point."""
    def not_point(self, gate_idx, wire_idx) -> None:
        """Draw a NOT gates as the circle with plus in the middle."""
    def swap_point(self, gate_idx, wire_idx) -> None:
        """Draw a swap point as a cross."""

def circuit_plot(c, nqubits, **kwargs):
    """Draw the circuit diagram for the circuit with nqubits.

    Parameters
    ==========

    c : circuit
        The circuit to plot. Should be a product of Gate instances.
    nqubits : int
        The number of qubits to include in the circuit. Must be at least
        as big as the largest ``min_qubits`` of the gates.
    """
def labeller(n, symbol: str = 'q'):
    """Autogenerate labels for wires of quantum circuits.

    Parameters
    ==========

    n : int
        number of qubits in the circuit.
    symbol : string
        A character string to precede all gate labels. E.g. 'q_0', 'q_1', etc.

    >>> from sympy.physics.quantum.circuitplot import labeller
    >>> labeller(2)
    ['q_1', 'q_0']
    >>> labeller(3,'j')
    ['j_2', 'j_1', 'j_0']
    """

class Mz(OneQubitGate):
    """Mock-up of a z measurement gate.

    This is in circuitplot rather than gate.py because it's not a real
    gate, it just draws one.
    """
    measurement: bool
    gate_name: str
    gate_name_latex: str

class Mx(OneQubitGate):
    """Mock-up of an x measurement gate.

    This is in circuitplot rather than gate.py because it's not a real
    gate, it just draws one.
    """
    measurement: bool
    gate_name: str
    gate_name_latex: str

class CreateOneQubitGate(type):
    def __new__(mcl, name, latexname: Incomplete | None = None): ...

def CreateCGate(name, latexname: Incomplete | None = None):
    """Use a lexical closure to make a controlled gate.
    """
