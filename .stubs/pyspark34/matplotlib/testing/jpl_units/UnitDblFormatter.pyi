import matplotlib.ticker as ticker
from _typeshed import Incomplete

__all__ = ['UnitDblFormatter']

class UnitDblFormatter(ticker.ScalarFormatter):
    """
    The formatter for UnitDbl data types.

    This allows for formatting with the unit string.
    """
    def __call__(self, x, pos: Incomplete | None = None): ...
    def format_data_short(self, value): ...
    def format_data(self, value): ...
