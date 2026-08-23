from _typeshed import Incomplete
from matplotlib.dates import date2num as date2num

class Epoch:
    allowed: Incomplete
    def __init__(self, frame, sec: Incomplete | None = None, jd: Incomplete | None = None, daynum: Incomplete | None = None, dt: Incomplete | None = None) -> None:
        """
        Create a new Epoch object.

        Build an epoch 1 of 2 ways:

        Using seconds past a Julian date:
        #   Epoch('ET', sec=1e8, jd=2451545)

        or using a matplotlib day number
        #   Epoch('ET', daynum=730119.5)

        = ERROR CONDITIONS
        - If the input units are not in the allowed list, an error is thrown.

        = INPUT VARIABLES
        - frame     The frame of the epoch.  Must be 'ET' or 'UTC'
        - sec        The number of seconds past the input JD.
        - jd         The Julian date of the epoch.
        - daynum    The matplotlib day number of the epoch.
        - dt         A python datetime instance.
        """
    def convert(self, frame): ...
    def frame(self): ...
    def julianDate(self, frame): ...
    def secondsPast(self, frame, jd): ...
    __eq__: Incomplete
    __ne__: Incomplete
    __lt__: Incomplete
    __le__: Incomplete
    __gt__: Incomplete
    __ge__: Incomplete
    def __add__(self, rhs):
        """
        Add a duration to an Epoch.

        = INPUT VARIABLES
        - rhs     The Epoch to subtract.

        = RETURN VALUE
        - Returns the difference of ourselves and the input Epoch.
        """
    def __sub__(self, rhs):
        """
        Subtract two Epoch's or a Duration from an Epoch.

        Valid:
        Duration = Epoch - Epoch
        Epoch = Epoch - Duration

        = INPUT VARIABLES
        - rhs     The Epoch to subtract.

        = RETURN VALUE
        - Returns either the duration between to Epoch's or the a new
          Epoch that is the result of subtracting a duration from an epoch.
        """
    @staticmethod
    def range(start, stop, step):
        """
        Generate a range of Epoch objects.

        Similar to the Python range() method.  Returns the range [
        start, stop) at the requested step.  Each element will be a
        Epoch object.

        = INPUT VARIABLES
        - start     The starting value of the range.
        - stop      The stop value of the range.
        - step      Step to use.

        = RETURN VALUE
        - Returns a list containing the requested Epoch values.
        """
