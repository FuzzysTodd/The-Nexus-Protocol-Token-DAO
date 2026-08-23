import matplotlib.units as units

__all__ = ['StrConverter']

class StrConverter(units.ConversionInterface):
    """
    A Matplotlib converter class for string data values.

    Valid units for string are:
    - 'indexed' : Values are indexed as they are specified for plotting.
    - 'sorted'  : Values are sorted alphanumerically.
    - 'inverted' : Values are inverted so that the first value is on top.
    - 'sorted-inverted' :  A combination of 'sorted' and 'inverted'
    """
    @staticmethod
    def axisinfo(unit, axis) -> None: ...
    @staticmethod
    def convert(value, unit, axis): ...
    @staticmethod
    def default_units(value, axis): ...
