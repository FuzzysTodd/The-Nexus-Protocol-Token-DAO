from .common import CL_scaling_vector as CL_scaling_vector, EPS as EPS, build_quadratic_1d as build_quadratic_1d, compute_grad as compute_grad, evaluate_quadratic as evaluate_quadratic, find_active_constraints as find_active_constraints, in_bounds as in_bounds, make_strictly_feasible as make_strictly_feasible, minimize_quadratic_1d as minimize_quadratic_1d, print_header_linear as print_header_linear, print_iteration_linear as print_iteration_linear, reflective_transformation as reflective_transformation, regularized_lsq_operator as regularized_lsq_operator, right_multiplied_operator as right_multiplied_operator, step_size_to_bound as step_size_to_bound
from .givens_elimination import givens_elimination as givens_elimination
from _typeshed import Incomplete
from scipy.linalg import qr as qr, solve_triangular as solve_triangular
from scipy.optimize import OptimizeResult as OptimizeResult
from scipy.sparse.linalg import lsmr as lsmr

def regularized_lsq_with_qr(m, n, R, QTb, perm, diag, copy_R: bool = True):
    """Solve regularized least squares using information from QR-decomposition.

    The initial problem is to solve the following system in a least-squares
    sense::

        A x = b
        D x = 0

    where D is diagonal matrix. The method is based on QR decomposition
    of the form A P = Q R, where P is a column permutation matrix, Q is an
    orthogonal matrix and R is an upper triangular matrix.

    Parameters
    ----------
    m, n : int
        Initial shape of A.
    R : ndarray, shape (n, n)
        Upper triangular matrix from QR decomposition of A.
    QTb : ndarray, shape (n,)
        First n components of Q^T b.
    perm : ndarray, shape (n,)
        Array defining column permutation of A, such that ith column of
        P is perm[i]-th column of identity matrix.
    diag : ndarray, shape (n,)
        Array containing diagonal elements of D.

    Returns
    -------
    x : ndarray, shape (n,)
        Found least-squares solution.
    """
def backtracking(A, g, x, p, theta, p_dot_g, lb, ub):
    """Find an appropriate step size using backtracking line search."""
def select_step(x, A_h, g_h, c_h, p, p_h, d, lb, ub, theta):
    """Select the best step according to Trust Region Reflective algorithm."""
def trf_linear(A, b, x_lsq, lb, ub, tol, lsq_solver, lsmr_tol, max_iter, verbose, *, lsmr_maxiter: Incomplete | None = None): ...
