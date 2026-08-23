from ._trustregion import BaseQuadraticSubproblem as BaseQuadraticSubproblem

class CGSteihaugSubproblem(BaseQuadraticSubproblem):
    """Quadratic subproblem solved by a conjugate gradient method"""
    def solve(self, trust_radius):
        """
        Solve the subproblem using a conjugate gradient method.

        Parameters
        ----------
        trust_radius : float
            We are allowed to wander only this far away from the origin.

        Returns
        -------
        p : ndarray
            The proposed step.
        hits_boundary : bool
            True if the proposed step is on the boundary of the trust region.

        Notes
        -----
        This is algorithm (7.2) of Nocedal and Wright 2nd edition.
        Only the function that computes the Hessian-vector product is required.
        The Hessian itself is not required, and the Hessian does
        not need to be positive semidefinite.
        """
