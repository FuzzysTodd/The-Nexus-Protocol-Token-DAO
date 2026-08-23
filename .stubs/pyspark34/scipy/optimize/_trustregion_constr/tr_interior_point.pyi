from _typeshed import Incomplete

__all__ = ['tr_interior_point']

class BarrierSubproblem:
    """
    Barrier optimization problem:
        minimize fun(x) - barrier_parameter*sum(log(s))
        subject to: constr_eq(x)     = 0
                  constr_ineq(x) + s = 0
    """
    n_vars: Incomplete
    x0: Incomplete
    s0: Incomplete
    fun: Incomplete
    grad: Incomplete
    lagr_hess: Incomplete
    constr: Incomplete
    jac: Incomplete
    barrier_parameter: Incomplete
    tolerance: Incomplete
    n_eq: Incomplete
    n_ineq: Incomplete
    enforce_feasibility: Incomplete
    global_stop_criteria: Incomplete
    xtol: Incomplete
    fun0: Incomplete
    grad0: Incomplete
    constr0: Incomplete
    jac0: Incomplete
    terminate: bool
    def __init__(self, x0, s0, fun, grad, lagr_hess, n_vars, n_ineq, n_eq, constr, jac, barrier_parameter, tolerance, enforce_feasibility, global_stop_criteria, xtol, fun0, grad0, constr_ineq0, jac_ineq0, constr_eq0, jac_eq0) -> None: ...
    def update(self, barrier_parameter, tolerance) -> None: ...
    def get_slack(self, z): ...
    def get_variables(self, z): ...
    def function_and_constraints(self, z):
        """Returns barrier function and constraints at given point.

        For z = [x, s], returns barrier function:
            function(z) = fun(x) - barrier_parameter*sum(log(s))
        and barrier constraints:
            constraints(z) = [   constr_eq(x)     ]
                             [ constr_ineq(x) + s ]

        """
    def scaling(self, z):
        """Returns scaling vector.
        Given by:
            scaling = [ones(n_vars), s]
        """
    def gradient_and_jacobian(self, z):
        """Returns scaled gradient.

        Return scaled gradient:
            gradient = [             grad(x)             ]
                       [ -barrier_parameter*ones(n_ineq) ]
        and scaled Jacobian matrix:
            jacobian = [  jac_eq(x)  0  ]
                       [ jac_ineq(x) S  ]
        Both of them scaled by the previously defined scaling factor.
        """
    def lagrangian_hessian_x(self, z, v):
        """Returns Lagrangian Hessian (in relation to `x`) -> Hx"""
    def lagrangian_hessian_s(self, z, v):
        """Returns scaled Lagrangian Hessian (in relation to`s`) -> S Hs S"""
    def lagrangian_hessian(self, z, v):
        """Returns scaled Lagrangian Hessian"""
    def stop_criteria(self, state, z, last_iteration_failed, optimality, constr_violation, trust_radius, penalty, cg_info):
        """Stop criteria to the barrier problem.
        The criteria here proposed is similar to formula (2.3)
        from [1]_, p.879.
        """

def tr_interior_point(fun, grad, lagr_hess, n_vars, n_ineq, n_eq, constr, jac, x0, fun0, grad0, constr_ineq0, jac_ineq0, constr_eq0, jac_eq0, stop_criteria, enforce_feasibility, xtol, state, initial_barrier_parameter, initial_tolerance, initial_penalty, initial_trust_radius, factorization_method):
    """Trust-region interior points method.

    Solve problem:
        minimize fun(x)
        subject to: constr_ineq(x) <= 0
                    constr_eq(x) = 0
    using trust-region interior point method described in [1]_.
    """
