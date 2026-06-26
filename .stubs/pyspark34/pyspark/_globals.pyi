from _typeshed import Incomplete

__ALL__: Incomplete

class _NoValueType:
    """Special keyword value.

    The instance of this class may be used as the default value assigned to a
    deprecated keyword in order to check if it has been given a user defined
    value.

    This class was copied from NumPy.
    """
    def __new__(cls): ...
    def __reduce__(self): ...
