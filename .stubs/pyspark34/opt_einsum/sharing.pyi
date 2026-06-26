from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['currently_sharing', 'get_sharing_cache', 'shared_intermediates', 'count_cached_ops', 'transpose_cache_wrap', 'einsum_cache_wrap', 'to_backend_cache_wrap']

def currently_sharing():
    """Check if we are currently sharing a cache -- thread specific.
    """
def get_sharing_cache():
    """Return the most recent sharing cache -- thread specific.
    """
def shared_intermediates(cache: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """Context in which contract intermediate results are shared.

    Note that intermediate computations will not be garbage collected until
    1. this context exits, and
    2. the yielded cache is garbage collected (if it was captured).

    Parameters
    ----------
    cache : dict
        If specified, a user-stored dict in which intermediate results will
        be stored. This can be used to interleave sharing contexts.

    Returns
    -------
    cache : dict
        A dictionary in which sharing results are stored. If ignored,
        sharing results will be garbage collected when this context is
        exited. This dict can be passed to another context to resume
        sharing.
    """
def count_cached_ops(cache):
    """Returns a counter of the types of each op in the cache.
    This is useful for profiling to increase sharing.
    """
def transpose_cache_wrap(transpose):
    """Decorates a ``transpose()`` implementation to be memoized inside a
    :func:`shared_intermediates` context.
    """
def einsum_cache_wrap(einsum):
    """Decorates an ``einsum()`` implementation to be memoized inside a
    :func:`shared_intermediates` context.
    """
def to_backend_cache_wrap(to_backend: Incomplete | None = None, constants: bool = False):
    """Decorates an ``to_backend()`` implementation to be memoized inside a
    :func:`shared_intermediates` context (e.g. ``to_cupy``, ``to_torch``).
    """
