from ._struct import Struct as Struct

class NotebookNode(Struct):
    """A dict-like node with attribute-access"""
    def __setitem__(self, key, value) -> None:
        """Set an item on the notebook."""
    def update(self, *args, **kwargs) -> None:
        """
        A dict-like update method based on CPython's MutableMapping `update`
        method.
        """

def from_dict(d):
    """Convert dict to dict-like NotebookNode

    Recursively converts any dict in the container to a NotebookNode.
    This does not check that the contents of the dictionary make a valid
    notebook or part of a notebook.
    """
