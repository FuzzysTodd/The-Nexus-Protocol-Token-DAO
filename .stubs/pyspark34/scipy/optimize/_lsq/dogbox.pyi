from .common import build_quadratic_1d as build_quadratic_1d, check_termination as check_termination, compute_grad as compute_grad, compute_jac_scale as compute_jac_scale, evaluate_quadratic as evaluate_quadratic, in_bounds as in_bounds, minimize_quadratic_1d as minimize_quadratic_1d, print_header_nonlinear as print_header_nonlinear, print_iteration_nonlinear as print_iteration_nonlinear, scale_for_robust_loss_function as scale_for_robust_loss_function, step_size_to_bound as step_size_to_bound, update_tr_radius as update_tr_radius
from scipy.optimize import OptimizeResult as OptimizeResult
from scipy.sparse.linalg import LinearOperator as LinearOperator, aslinearoperator as aslinearoperator, lsmr as lsmr

def lsmr_operator(Jop, d, active_set):
    """Compute LinearOperator to use in LSMR by dogbox algorithm.

    `active_set` mask is used to excluded active variables from computations
    of matrix-vector products.
    """
def find_intersection(x, tr_bounds, lb, ub):
    """Find intersection of trust-region bounds and initial bounds.

    Returns
    -------
    lb_total, ub_total : ndarray with shape of x
        Lower and upper bounds of the intersection region.
    orig_l, orig_u : ndarray of bool with shape of x
        True means that an original bound is taken as a corresponding bound
        in the intersection region.
    tr_l, tr_u : ndarray of bool with shape of x
        True means that a trust-region bound is taken as a corresponding bound
        in the intersection region.
    """
def dogleg_step(x, newton_step, g, a, b, tr_bounds, lb, ub):
    """Find dogleg step in a rectangular region.

    Returns
    -------
    step : ndarray, shape (n,)
        Computed dogleg step.
    bound_hits : ndarray of int, shape (n,)
        Each component shows whether a corresponding variable hits the
        initial bound after the step is taken:
            *  0 - a variable doesn't hit the bound.
            * -1 - lower bound is hit.
            *  1 - upper bound is hit.
    tr_hit : bool
        Whether the step hit the boundary of the trust-region.
    """
def dogbox(fun, jac, x0, f0, J0, lb, ub, ftol, xtol, gtol, max_nfev, x_scale, loss_function, tr_solver, tr_options, verbose): ...
