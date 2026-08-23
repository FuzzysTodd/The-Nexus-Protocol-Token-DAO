import math
from _typeshed import Incomplete

pi: float
e: float
sqrt2: float
sqrt5: float
phi: float
ln2: float
ln10: float
euler: float
catalan: float
khinchin: float
apery: float
logpi: float

def math_log(x): ...
def math_sqrt(x): ...
math_log = math.log
math_sqrt = math.sqrt
pow: Incomplete
log: Incomplete
sqrt: Incomplete
exp: Incomplete
cos: Incomplete
sin: Incomplete
tan: Incomplete
acos: Incomplete
asin: Incomplete
atan: Incomplete
cosh: Incomplete
sinh: Incomplete
tanh: Incomplete
floor: Incomplete
ceil: Incomplete
cos_sin: Incomplete
cbrt: Incomplete

def nthroot(x, n): ...

cospi: Incomplete
sinpi: Incomplete

def tanpi(x): ...
def cotpi(x): ...

INF: Incomplete
NINF: Incomplete
NAN: Incomplete
EPS: float
gamma: Incomplete

def rgamma(x): ...
def factorial(x): ...
def arg(x): ...
def loggamma(x): ...

digamma: Incomplete

def erf(x):
    """
    erf of a real number.
    """
def erfc(x):
    """
    erfc of a real number.
    """

gauss42: Incomplete
EI_ASYMP_CONVERGENCE_RADIUS: float

def ei_asymp(z, _e1: bool = False): ...
def ei_taylor(z, _e1: bool = False): ...
def ei(z, _e1: bool = False): ...
def e1(z): ...
def zeta(s):
    """
    Riemann zeta function, real argument
    """
