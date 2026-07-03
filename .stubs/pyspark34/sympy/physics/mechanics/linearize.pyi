from _typeshed import Incomplete

__all__ = ['Linearizer']

class Linearizer:
    """This object holds the general model form for a dynamic system.
    This model is used for computing the linearized form of the system,
    while properly dealing with constraints leading to  dependent
    coordinates and speeds.

    Attributes
    ==========

    f_0, f_1, f_2, f_3, f_4, f_c, f_v, f_a : Matrix
        Matrices holding the general system form.
    q, u, r : Matrix
        Matrices holding the generalized coordinates, speeds, and
        input vectors.
    q_i, u_i : Matrix
        Matrices of the independent generalized coordinates and speeds.
    q_d, u_d : Matrix
        Matrices of the dependent generalized coordinates and speeds.
    perm_mat : Matrix
        Permutation matrix such that [q_ind, u_ind]^T = perm_mat*[q, u]^T
    """
    f_0: Incomplete
    f_1: Incomplete
    f_2: Incomplete
    f_3: Incomplete
    f_4: Incomplete
    f_c: Incomplete
    f_v: Incomplete
    f_a: Incomplete
    q: Incomplete
    u: Incomplete
    q_i: Incomplete
    q_d: Incomplete
    u_i: Incomplete
    u_d: Incomplete
    r: Incomplete
    lams: Incomplete
    perm_mat: Incomplete
    def __init__(self, f_0, f_1, f_2, f_3, f_4, f_c, f_v, f_a, q, u, q_i: Incomplete | None = None, q_d: Incomplete | None = None, u_i: Incomplete | None = None, u_d: Incomplete | None = None, r: Incomplete | None = None, lams: Incomplete | None = None) -> None:
        """
        Parameters
        ==========

        f_0, f_1, f_2, f_3, f_4, f_c, f_v, f_a : array_like
            System of equations holding the general system form.
            Supply empty array or Matrix if the parameter
            does not exist.
        q : array_like
            The generalized coordinates.
        u : array_like
            The generalized speeds
        q_i, u_i : array_like, optional
            The independent generalized coordinates and speeds.
        q_d, u_d : array_like, optional
            The dependent generalized coordinates and speeds.
        r : array_like, optional
            The input variables.
        lams : array_like, optional
            The lagrange multipliers
        """
    def linearize(self, op_point: Incomplete | None = None, A_and_B: bool = False, simplify: bool = False):
        """Linearize the system about the operating point. Note that
        q_op, u_op, qd_op, ud_op must satisfy the equations of motion.
        These may be either symbolic or numeric.

        Parameters
        ==========

        op_point : dict or iterable of dicts, optional
            Dictionary or iterable of dictionaries containing the operating
            point conditions. These will be substituted in to the linearized
            system before the linearization is complete. Leave blank if you
            want a completely symbolic form. Note that any reduction in
            symbols (whether substituted for numbers or expressions with a
            common parameter) will result in faster runtime.

        A_and_B : bool, optional
            If A_and_B=False (default), (M, A, B) is returned for forming
            [M]*[q, u]^T = [A]*[q_ind, u_ind]^T + [B]r. If A_and_B=True,
            (A, B) is returned for forming dx = [A]x + [B]r, where
            x = [q_ind, u_ind]^T.

        simplify : bool, optional
            Determines if returned values are simplified before return.
            For large expressions this may be time consuming. Default is False.

        Potential Issues
        ================

            Note that the process of solving with A_and_B=True is
            computationally intensive if there are many symbolic parameters.
            For this reason, it may be more desirable to use the default
            A_and_B=False, returning M, A, and B. More values may then be
            substituted in to these matrices later on. The state space form can
            then be found as A = P.T*M.LUsolve(A), B = P.T*M.LUsolve(B), where
            P = Linearizer.perm_mat.
        """
