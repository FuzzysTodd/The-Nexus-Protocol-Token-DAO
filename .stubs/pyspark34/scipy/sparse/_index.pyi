from ._sputils import isintlike as isintlike
from _typeshed import Incomplete

INT_TYPES: Incomplete

class IndexMixin:
    """
    This class provides common dispatching and validation logic for indexing.
    """
    def __getitem__(self, key): ...
    def __setitem__(self, key, x) -> None: ...
    def getrow(self, i):
        """Return a copy of row i of the matrix, as a (1 x n) row vector.
        """
    def getcol(self, i):
        """Return a copy of column i of the matrix, as a (m x 1) column vector.
        """
