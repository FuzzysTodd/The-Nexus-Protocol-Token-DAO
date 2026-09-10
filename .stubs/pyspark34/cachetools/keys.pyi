__all__ = ['hashkey', 'methodkey', 'typedkey']

class _HashedTuple(tuple):
    """A tuple that ensures that hash() will be called no more than once
    per element, since cache decorators will hash the key multiple
    times on a cache miss.  See also _HashedSeq in the standard
    library functools implementation.

    """
    def __hash__(self, hash=...): ...
    def __add__(self, other, add=...): ...
    def __radd__(self, other, add=...): ...

def hashkey(*args, **kwargs):
    """Return a cache key for the specified hashable arguments."""
def methodkey(self, *args, **kwargs):
    """Return a cache key for use with cached methods."""
def typedkey(*args, **kwargs):
    """Return a typed cache key for the specified hashable arguments."""
