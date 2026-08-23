from _typeshed import Incomplete

class Math:
    """
  Additional math routines for GeographicLib.

  This defines constants:
    epsilon, difference between 1 and the next bigger number
    digits, the number of digits in the fraction of a real number
    minval, minimum normalized positive number
    maxval, maximum finite number
    nan, not a number
    inf, infinity
  """
    digits: int
    epsilon: Incomplete
    minval: Incomplete
    maxval: Incomplete
    inf: Incomplete
    nan: Incomplete
    def sq(x):
        """Square a number"""
    sq: Incomplete
    def cbrt(x):
        """Real cube root of a number"""
    cbrt: Incomplete
    def log1p(x):
        """log(1 + x) accurate for small x (missing from python 2.5.2)"""
    log1p: Incomplete
    def atanh(x):
        """atanh(x) (missing from python 2.5.2)"""
    atanh: Incomplete
    def copysign(x, y):
        """return x with the sign of y (missing from python 2.5.2)"""
    copysign: Incomplete
    def norm(x, y):
        """Private: Normalize a two-vector."""
    norm: Incomplete
    def sum(u, v):
        """Error free transformation of a sum."""
    sum: Incomplete
    def polyval(N, p, s, x):
        """Evaluate a polynomial."""
    polyval: Incomplete
    def AngRound(x):
        """Private: Round an angle so that small values underflow to zero."""
    AngRound: Incomplete
    def remainder(x, y):
        """remainder of x/y in the range [-y/2, y/2]."""
    remainder: Incomplete
    def AngNormalize(x):
        """reduce angle to (-180,180]"""
    AngNormalize: Incomplete
    def LatFix(x):
        """replace angles outside [-90,90] by NaN"""
    LatFix: Incomplete
    def AngDiff(x, y):
        """compute y - x and reduce to [-180,180] accurately"""
    AngDiff: Incomplete
    def sincosd(x):
        """Compute sine and cosine of x in degrees."""
    sincosd: Incomplete
    def atan2d(y, x):
        """compute atan2(y, x) with the result in degrees"""
    atan2d: Incomplete
    def isfinite(x):
        """Test for finiteness"""
    isfinite: Incomplete
    def isnan(x):
        """Test if nan"""
    isnan: Incomplete
