from _typeshed import Incomplete
from tensorflow.python.util import compat as compat

class Registry:
    """Provides a registry for saving objects."""
    def __init__(self, name) -> None:
        """Creates a new registry."""
    def register(self, candidate, name: Incomplete | None = None) -> None:
        '''Registers a Python object "candidate" for the given "name".

    Args:
      candidate: The candidate object to add to the registry.
      name: An optional string specifying the registry key for the candidate.
            If None, candidate.__name__ will be used.
    Raises:
      KeyError: If same name is used twice.
    '''
    def list(self):
        """Lists registered items.

    Returns:
      A list of names of registered objects.
    """
    def lookup(self, name):
        '''Looks up "name".

    Args:
      name: a string specifying the registry key for the candidate.
    Returns:
      Registered object if found
    Raises:
      LookupError: if "name" has not been registered.
    '''
