from _typeshed import Incomplete
from matplotlib import cbook as cbook

class ConversionError(TypeError): ...

class AxisInfo:
    """
    Information to support default axis labeling, tick labeling, and limits.

    An instance of this class must be returned by
    `ConversionInterface.axisinfo`.
    """
    majloc: Incomplete
    minloc: Incomplete
    majfmt: Incomplete
    minfmt: Incomplete
    label: Incomplete
    default_limits: Incomplete
    def __init__(self, majloc: Incomplete | None = None, minloc: Incomplete | None = None, majfmt: Incomplete | None = None, minfmt: Incomplete | None = None, label: Incomplete | None = None, default_limits: Incomplete | None = None) -> None:
        """
        Parameters
        ----------
        majloc, minloc : Locator, optional
            Tick locators for the major and minor ticks.
        majfmt, minfmt : Formatter, optional
            Tick formatters for the major and minor ticks.
        label : str, optional
            The default axis label.
        default_limits : optional
            The default min and max limits of the axis if no data has
            been plotted.

        Notes
        -----
        If any of the above are ``None``, the axis will simply use the
        default value.
        """

class ConversionInterface:
    """
    The minimal interface for a converter to take custom data types (or
    sequences) and convert them to values Matplotlib can use.
    """
    @staticmethod
    def axisinfo(unit, axis) -> None:
        """Return an `.AxisInfo` for the axis with the specified units."""
    @staticmethod
    def default_units(x, axis) -> None:
        """Return the default unit for *x* or ``None`` for the given axis."""
    @staticmethod
    def convert(obj, unit, axis):
        """
        Convert *obj* using *unit* for the specified *axis*.

        If *obj* is a sequence, return the converted sequence.  The output must
        be a sequence of scalars that can be used by the numpy array layer.
        """

class DecimalConverter(ConversionInterface):
    """Converter for decimal.Decimal data to float."""
    @staticmethod
    def convert(value, unit, axis):
        """
        Convert Decimals to floats.

        The *unit* and *axis* arguments are not used.

        Parameters
        ----------
        value : decimal.Decimal or iterable
            Decimal or list of Decimal need to be converted
        """

class Registry(dict):
    """Register types with conversion interface."""
    def get_converter(self, x):
        """Get the converter interface instance for *x*, or None."""

registry: Incomplete
