from _typeshed import Incomplete

__all__ = ['LinearConstraint']

class LinearConstraint:
    """A linear constraint in matrix form.

    This object represents a linear constraint of the form `Ax = b`.

    Usually you won't be constructing these by hand, but instead get them as
    the return value from :meth:`DesignInfo.linear_constraint`.

    .. attribute:: coefs

       A 2-dimensional ndarray with float dtype, representing `A`.

    .. attribute:: constants

       A 2-dimensional single-column ndarray with float dtype, representing
       `b`.

    .. attribute:: variable_names

       A list of strings giving the names of the variables being
       constrained. (Used only for consistency checking.)
    """
    variable_names: Incomplete
    coefs: Incomplete
    constants: Incomplete
    def __init__(self, variable_names, coefs, constants: Incomplete | None = None) -> None: ...
    @classmethod
    def combine(cls, constraints):
        """Create a new LinearConstraint by ANDing together several existing
        LinearConstraints.

        :arg constraints: An iterable of LinearConstraint objects. Their
          :attr:`variable_names` attributes must all match.
        :returns: A new LinearConstraint object.
        """

class _EvalConstraint:
    def __init__(self, variable_names) -> None: ...
    def is_constant(self, coefs): ...
    def eval(self, tree, constraint: bool = False): ...
