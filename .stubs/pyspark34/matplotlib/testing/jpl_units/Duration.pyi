from _typeshed import Incomplete

class Duration:
    """Class Duration in development."""
    allowed: Incomplete
    def __init__(self, frame, seconds) -> None:
        """
        Create a new Duration object.

        = ERROR CONDITIONS
        - If the input frame is not in the allowed list, an error is thrown.

        = INPUT VARIABLES
        - frame     The frame of the duration.  Must be 'ET' or 'UTC'
        - seconds  The number of seconds in the Duration.
        """
    def frame(self):
        """Return the frame the duration is in."""
    def __abs__(self):
        """Return the absolute value of the duration."""
    def __neg__(self):
        """Return the negative value of this Duration."""
    def seconds(self):
        """Return the number of seconds in the Duration."""
    def __bool__(self) -> bool: ...
    __eq__: Incomplete
    __ne__: Incomplete
    __lt__: Incomplete
    __le__: Incomplete
    __gt__: Incomplete
    __ge__: Incomplete
    def __add__(self, rhs):
        """
        Add two Durations.

        = ERROR CONDITIONS
        - If the input rhs is not in the same frame, an error is thrown.

        = INPUT VARIABLES
        - rhs     The Duration to add.

        = RETURN VALUE
        - Returns the sum of ourselves and the input Duration.
        """
    def __sub__(self, rhs):
        """
        Subtract two Durations.

        = ERROR CONDITIONS
        - If the input rhs is not in the same frame, an error is thrown.

        = INPUT VARIABLES
        - rhs     The Duration to subtract.

        = RETURN VALUE
        - Returns the difference of ourselves and the input Duration.
        """
    def __mul__(self, rhs):
        """
        Scale a UnitDbl by a value.

        = INPUT VARIABLES
        - rhs     The scalar to multiply by.

        = RETURN VALUE
        - Returns the scaled Duration.
        """
    __rmul__ = __mul__
    def checkSameFrame(self, rhs, func) -> None:
        """
        Check to see if frames are the same.

        = ERROR CONDITIONS
        - If the frame of the rhs Duration is not the same as our frame,
          an error is thrown.

        = INPUT VARIABLES
        - rhs     The Duration to check for the same frame
        - func    The name of the function doing the check.
        """
