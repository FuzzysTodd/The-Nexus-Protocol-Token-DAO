__all__ = ['get_flinalg_funcs']

def get_flinalg_funcs(names, arrays=(), debug: int = 0):
    """Return optimal available _flinalg function objects with
    names. Arrays are used to determine optimal prefix."""
