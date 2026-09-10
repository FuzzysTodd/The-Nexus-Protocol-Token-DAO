from _typeshed import Incomplete
from scipy.stats import distributions

def get_u_argskwargs(**kwargs): ...

class Transf_gen(distributions.rv_continuous):
    """a class for non-linear monotonic transformation of a continuous random variable

    """
    func: Incomplete
    funcinv: Incomplete
    numargs: Incomplete
    decr: Incomplete
    kls: Incomplete
    def __init__(self, kls, func, funcinv, *args, **kwargs) -> None: ...

def inverse(x): ...

mux: Incomplete
stdx: Incomplete

def inversew(x): ...
def inversew_inv(x): ...
def identit(x): ...

invdnormalg: Incomplete
lognormalg: Incomplete
loggammaexpg: Incomplete

class ExpTransf_gen(distributions.rv_continuous):
    """Distribution based on log/exp transformation

    the constructor can be called with a distribution class
    and generates the distribution of the transformed random variable

    """
    numargs: Incomplete
    kls: Incomplete
    def __init__(self, kls, *args, **kwargs) -> None: ...

class LogTransf_gen(distributions.rv_continuous):
    """Distribution based on log/exp transformation

    the constructor can be called with a distribution class
    and generates the distribution of the transformed random variable

    """
    numargs: Incomplete
    kls: Incomplete
    def __init__(self, kls, *args, **kwargs) -> None: ...

def examples_transf() -> None: ...

class TransfTwo_gen(distributions.rv_continuous):
    """Distribution based on a non-monotonic (u- or hump-shaped transformation)

    the constructor can be called with a distribution class, and functions
    that define the non-linear transformation.
    and generates the distribution of the transformed random variable

    Note: the transformation, it's inverse and derivatives need to be fully
    specified: func, funcinvplus, funcinvminus, derivplus,  derivminus.
    Currently no numerical derivatives or inverse are calculated

    This can be used to generate distribution instances similar to the
    distributions in scipy.stats.

    """
    func: Incomplete
    funcinvplus: Incomplete
    funcinvminus: Incomplete
    derivplus: Incomplete
    derivminus: Incomplete
    numargs: Incomplete
    shape: Incomplete
    kls: Incomplete
    def __init__(self, kls, func, funcinvplus, funcinvminus, derivplus, derivminus, *args, **kwargs) -> None: ...

class SquareFunc:
    """class to hold quadratic function with inverse function and derivative

    using instance methods instead of class methods, if we want extension
    to parametrized function
    """
    def inverseplus(self, x): ...
    def inverseminus(self, x): ...
    def derivplus(self, x): ...
    def derivminus(self, x): ...
    def squarefunc(self, x): ...

sqfunc: Incomplete
squarenormalg: Incomplete
squaretg: Incomplete

def inverseplus(x): ...
def inverseminus(x): ...
def derivplus(x): ...
def derivminus(x): ...
def negsquarefunc(x): ...

negsquarenormalg: Incomplete

def absfunc(x): ...

absnormalg: Incomplete
