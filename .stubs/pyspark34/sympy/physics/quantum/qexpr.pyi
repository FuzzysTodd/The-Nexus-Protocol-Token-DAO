from sympy.core.expr import Expr

__all__ = ['QuantumError', 'QExpr']

class QuantumError(Exception): ...

class QExpr(Expr):
    """A base class for all quantum object like operators and states."""
    is_commutative: bool
    @property
    def free_symbols(self): ...
    def __new__(cls, *args, **kwargs):
        """Construct a new quantum object.

        Parameters
        ==========

        args : tuple
            The list of numbers or parameters that uniquely specify the
            quantum object. For a state, this will be its symbol or its
            set of quantum numbers.

        Examples
        ========

        >>> from sympy.physics.quantum.qexpr import QExpr
        >>> q = QExpr(0)
        >>> q
        0
        >>> q.label
        (0,)
        >>> q.hilbert_space
        H
        >>> q.args
        (0,)
        >>> q.is_commutative
        False
        """
    @property
    def label(self):
        """The label is the unique set of identifiers for the object.

        Usually, this will include all of the information about the state
        *except* the time (in the case of time-dependent objects).

        This must be a tuple, rather than a Tuple.
        """
    @property
    def is_symbolic(self): ...
    @classmethod
    def default_args(self) -> None:
        """If no arguments are specified, then this will return a default set
        of arguments to be run through the constructor.

        NOTE: Any classes that override this MUST return a tuple of arguments.
        Should be overridden by subclasses to specify the default arguments for kets and operators
        """
