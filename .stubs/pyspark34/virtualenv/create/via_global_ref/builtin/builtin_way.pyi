from abc import ABCMeta
from virtualenv.create.creator import Creator
from virtualenv.create.describe import Describe

__all__ = ['VirtualenvBuiltin']

class VirtualenvBuiltin(Creator, Describe, metaclass=ABCMeta):
    """A creator that does operations itself without delegation, if we can create it we can also describe it."""
    def __init__(self, options, interpreter) -> None: ...
