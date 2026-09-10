from ._optimize import OptimizeResult as OptimizeResult
from _typeshed import Incomplete
from scipy.optimize._differentiable_functions import FD_METHODS as FD_METHODS
from scipy.optimize._hessian_update_strategy import HessianUpdateStrategy as HessianUpdateStrategy

class BaseQuadraticSubproblem:
    """
    Base/abstract class defining the quadratic model for trust-region
    minimization. Child classes must implement the ``solve`` method.

    Values of the objective function, Jacobian and Hessian (if provided) at
    the current iterate ``x`` are evaluated on demand and then stored as
    attributes ``fun``, ``jac``, ``hess``.
    """
    def __init__(self, x, fun, jac, hess: Incomplete | None = None, hessp: Incomplete | None = None) -> None: ...
    def __call__(self, p): ...
    @property
    def fun(self):
        """Value of objective function at current iteration."""
    @property
    def jac(self):
        """Value of Jacobian of objective function at current iteration."""
    @property
    def hess(self):
        """Value of Hessian of objective function at current iteration."""
    def hessp(self, p): ...
    @property
    def jac_mag(self):
        """Magnitude of jacobian of objective function at current iteration."""
    def get_boundaries_intersections(self, z, d, trust_radius):
        """
        Solve the scalar quadratic equation ||z + t d|| == trust_radius.
        This is like a line-sphere intersection.
        Return the two values of t, sorted from low to high.
        """
    def solve(self, trust_radius) -> None: ...
