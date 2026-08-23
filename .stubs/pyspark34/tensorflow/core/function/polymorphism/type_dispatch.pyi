from tensorflow.core.function.polymorphism import function_type as function_type
from typing import Iterable, Optional

class TypeDispatchTable:
    """Type dispatch table implementation.

  A type dispatch table is a list, L, of target types. Given a request type, R,
  the table selects a target type, T, according to the following dispatch rules:
    1. R == T or R is supertype of T (functions are contravariant on args)
    2. There does not exist O in L such that R is supertype of O and O is a
       supertype of T (in other words, T is the closest to R, within list L).
    3. If the above two rules are satisfied by multiple targets, the earliest
       inserted one is chosen.
  """
    def __init__(self) -> None:
        """Creates a TypeDispatchTable object."""
    def add_target(self, target: function_type.FunctionType) -> None:
        """Adds a new target type."""
    @property
    def targets(self) -> Iterable[function_type.FunctionType]:
        """Returns an iterable to all targets in the table."""
    def delete(self, target: function_type.FunctionType) -> None:
        """Deletes a target in the table if it exists."""
    def clear(self) -> None:
        """Deletes all targets in the table."""
    def dispatch(self, request: function_type.FunctionType) -> Optional[function_type.FunctionType]:
        """Returns the most specific supertype target if it exists in the table."""
    def try_generalizing_function_type(self, target: function_type.FunctionType) -> function_type.FunctionType:
        '''Returns a generalized subtype of the one given.

    This heuristic aims to reduce the number of future traces by computing a
    type that represents more general function inputs.

    The original "experimental_relax_shapes" heuristic identified a known type
    which shared a common subtype with the current unknown type and then
    traced with that common subtype. However, the notion of "common subtype"
    was only limited to shapes. This heuristic extends that to FunctionType.

    Returns `target` if a generalized subtype can not be found.

    Args:
      target: The FunctionType to generalize
    '''
