from _typeshed import Incomplete
from matplotlib import units

__all__ = ['EpochConverter']

class EpochConverter(units.ConversionInterface):
    """
    Provides Matplotlib conversion functionality for Monte Epoch and Duration
    classes.
    """
    jdRef: Incomplete
    @staticmethod
    def axisinfo(unit, axis): ...
    @staticmethod
    def float2epoch(value, unit):
        """
        Convert a Matplotlib floating-point date into an Epoch of the specified
        units.

        = INPUT VARIABLES
        - value     The Matplotlib floating-point date.
        - unit      The unit system to use for the Epoch.

        = RETURN VALUE
        - Returns the value converted to an Epoch in the specified time system.
        """
    @staticmethod
    def epoch2float(value, unit):
        """
        Convert an Epoch value to a float suitable for plotting as a python
        datetime object.

        = INPUT VARIABLES
        - value    An Epoch or list of Epochs that need to be converted.
        - unit     The units to use for an axis with Epoch data.

        = RETURN VALUE
        - Returns the value parameter converted to floats.
        """
    @staticmethod
    def duration2float(value):
        """
        Convert a Duration value to a float suitable for plotting as a python
        datetime object.

        = INPUT VARIABLES
        - value    A Duration or list of Durations that need to be converted.

        = RETURN VALUE
        - Returns the value parameter converted to floats.
        """
    @staticmethod
    def convert(value, unit, axis): ...
    @staticmethod
    def default_units(value, axis): ...
