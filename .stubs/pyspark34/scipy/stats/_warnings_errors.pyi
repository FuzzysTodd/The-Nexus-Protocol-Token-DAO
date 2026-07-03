from _typeshed import Incomplete

class DegenerateDataWarning(RuntimeWarning):
    """Warns when data is degenerate and results may not be reliable."""
    args: Incomplete
    def __init__(self, msg: Incomplete | None = None) -> None: ...

class ConstantInputWarning(DegenerateDataWarning):
    """Warns when all values in data are exactly equal."""
    args: Incomplete
    def __init__(self, msg: Incomplete | None = None) -> None: ...

class NearConstantInputWarning(DegenerateDataWarning):
    """Warns when all values in data are nearly equal."""
    args: Incomplete
    def __init__(self, msg: Incomplete | None = None) -> None: ...

class FitError(RuntimeError):
    """Represents an error condition when fitting a distribution to data."""
    args: Incomplete
    def __init__(self, msg: Incomplete | None = None) -> None: ...
