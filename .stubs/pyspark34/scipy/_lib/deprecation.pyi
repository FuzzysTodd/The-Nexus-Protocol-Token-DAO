__all__ = ['_deprecated']

def _deprecated(msg, stacklevel: int = 2):
    """Deprecate a function by emitting a warning on use."""

class _DeprecationHelperStr:
    """
    Helper class used by deprecate_cython_api
    """
    def __init__(self, content, message) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
