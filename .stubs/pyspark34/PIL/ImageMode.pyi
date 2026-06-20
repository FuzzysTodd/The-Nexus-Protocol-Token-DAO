from _typeshed import Incomplete

class ModeDescriptor:
    """Wrapper for mode strings."""
    mode: Incomplete
    bands: Incomplete
    basemode: Incomplete
    basetype: Incomplete
    typestr: Incomplete
    def __init__(self, mode, bands, basemode, basetype, typestr) -> None: ...

def getmode(mode):
    """Gets a mode descriptor for the given mode."""
