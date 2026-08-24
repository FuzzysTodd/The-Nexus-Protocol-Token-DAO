from .Duration import Duration as Duration
from .Epoch import Epoch as Epoch
from .UnitDbl import UnitDbl as UnitDbl
from .UnitDblFormatter import UnitDblFormatter as UnitDblFormatter

__all__ = ['register', 'Duration', 'Epoch', 'UnitDbl', 'UnitDblFormatter']

def register() -> None:
    """Register the unit conversion classes with matplotlib."""
