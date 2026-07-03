from _typeshed import Incomplete
from matplotlib import units

__all__ = ['UnitDblConverter']

class UnitDblConverter(units.ConversionInterface):
    """
    Provides Matplotlib conversion functionality for the Monte UnitDbl class.
    """
    defaults: Incomplete
    @staticmethod
    def axisinfo(unit, axis): ...
    @staticmethod
    def convert(value, unit, axis): ...
    @staticmethod
    def default_units(value, axis): ...
