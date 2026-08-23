from _typeshed import Incomplete

class UnitDbl:
    """Class UnitDbl in development."""
    allowed: Incomplete
    def __init__(self, value, units) -> None:
        """
        Create a new UnitDbl object.

        Units are internally converted to km, rad, and sec.  The only
        valid inputs for units are [m, km, mile, rad, deg, sec, min, hour].

        The field UnitDbl.value will contain the converted value.  Use
        the convert() method to get a specific type of units back.

        = ERROR CONDITIONS
        - If the input units are not in the allowed list, an error is thrown.

        = INPUT VARIABLES
        - value     The numeric value of the UnitDbl.
        - units     The string name of the units the value is in.
        """
    def convert(self, units):
        """
        Convert the UnitDbl to a specific set of units.

        = ERROR CONDITIONS
        - If the input units are not in the allowed list, an error is thrown.

        = INPUT VARIABLES
        - units     The string name of the units to convert to.

        = RETURN VALUE
        - Returns the value of the UnitDbl in the requested units as a floating
          point number.
        """
    def __abs__(self):
        """Return the absolute value of this UnitDbl."""
    def __neg__(self):
        """Return the negative value of this UnitDbl."""
    def __bool__(self) -> bool:
        """Return the truth value of a UnitDbl."""
    __eq__: Incomplete
    __ne__: Incomplete
    __lt__: Incomplete
    __le__: Incomplete
    __gt__: Incomplete
    __ge__: Incomplete
    __add__: Incomplete
    __sub__: Incomplete
    __mul__: Incomplete
    __rmul__: Incomplete
    def type(self):
        """Return the type of UnitDbl data."""
    @staticmethod
    def range(start, stop, step: Incomplete | None = None):
        """
        Generate a range of UnitDbl objects.

        Similar to the Python range() method.  Returns the range [
        start, stop) at the requested step.  Each element will be a
        UnitDbl object.

        = INPUT VARIABLES
        - start     The starting value of the range.
        - stop      The stop value of the range.
        - step      Optional step to use.  If set to None, then a UnitDbl of
                      value 1 w/ the units of the start is used.

        = RETURN VALUE
        - Returns a list containing the requested UnitDbl values.
        """
    def checkSameUnits(self, rhs, func) -> None:
        """
        Check to see if units are the same.

        = ERROR CONDITIONS
        - If the units of the rhs UnitDbl are not the same as our units,
          an error is thrown.

        = INPUT VARIABLES
        - rhs     The UnitDbl to check for the same units
        - func    The name of the function doing the check.
        """
