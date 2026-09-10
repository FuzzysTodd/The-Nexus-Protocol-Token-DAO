from _typeshed import Incomplete

__all__ = ['_minimize_trust_krylov']

def _minimize_trust_krylov(fun, x0, args=(), jac: Incomplete | None = None, hess: Incomplete | None = None, hessp: Incomplete | None = None, inexact: bool = True, **trust_region_options):
    """
    Minimization of a scalar function of one or more variables using
    a nearly exact trust-region algorithm that only requires matrix
    vector products with the hessian matrix.

    .. versionadded:: 1.0.0

    Options
    -------
    inexact : bool, optional
        Accuracy to solve subproblems. If True requires less nonlinear
        iterations, but more vector products.
    """
