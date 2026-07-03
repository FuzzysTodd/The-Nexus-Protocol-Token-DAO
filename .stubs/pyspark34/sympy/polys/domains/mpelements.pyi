from _typeshed import Incomplete
from mpmath.ctx_mp_python import PythonMPContext, _mpc, _mpf
from sympy.polys.domains.domainelement import DomainElement as DomainElement
from sympy.utilities import public as public

class RealElement(_mpf, DomainElement):
    """An element of a real domain. """
    def parent(self): ...

class ComplexElement(_mpc, DomainElement):
    """An element of a complex domain. """
    def parent(self): ...

new: Incomplete

class MPContext(PythonMPContext):
    def __init__(ctx, prec: int = 53, dps: Incomplete | None = None, tol: Incomplete | None = None, real: bool = False) -> None: ...
    def make_tol(ctx): ...
    def to_rational(ctx, s, limit: bool = True): ...
    def almosteq(ctx, s, t, rel_eps: Incomplete | None = None, abs_eps: Incomplete | None = None): ...
