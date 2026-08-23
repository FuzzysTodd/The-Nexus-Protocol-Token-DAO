from geographiclib.geomath import Math as Math

class Accumulator:
    """Like math.fsum, but allows a running sum"""
    def Set(self, y) -> None:
        """Set value from argument"""
    def __init__(self, y: float = 0.0) -> None:
        """Constructor"""
    def Add(self, y) -> None:
        """Add a value"""
    def Sum(self, y: float = 0.0):
        """Return sum + y"""
    def Negate(self) -> None:
        """Negate sum"""
    def Remainder(self, y) -> None:
        """Remainder on division by y"""
