def acq_max(f_acq, gp, y_max, bounds, space, num_warmup, num_starting_points):
    """
    A function to find the maximum of the acquisition function

    It uses a combination of random sampling (cheap) and the 'L-BFGS-B'
    optimization method. First by sampling ``num_warmup`` points at random,
    and then running L-BFGS-B from ``num_starting_points`` random starting points.

    Parameters
    ----------
    f_acq : UtilityFunction.utility
        The acquisition function object that return its point-wise value.

    gp : GaussianProcessRegressor
        A gaussian process fitted to the relevant data.

    y_max : float
        The current maximum known value of the target function.

    bounds : numpy array
        The variables bounds to limit the search of the acq max.

    num_warmup : int
        number of times to randomly sample the aquisition function

    num_starting_points : int
        number of times to run scipy.minimize

    Returns
    -------
    numpy array
        The parameter which achieves max of the acquisition function.
    """

class UtilityFunction:
    """
    A class to compute different acquisition function values.

    Parameters
    ----------
    kind : string
        specification of utility function to use
    kappa : float
        parameter usedd for 'ucb' acquisition function
    xi : float
        parameter usedd for 'ei' and 'poi' acquisition function
    """
    def __init__(self, kind, kappa, xi) -> None: ...
    def utility(self, x, gp, y_max):
        """
        return utility function

        Parameters
        ----------
        x : numpy array
            parameters
        gp : GaussianProcessRegressor
        y_max : float
            maximum target value observed so far

        Returns
        -------
        function
            return corresponding function, return None if parameter is illegal
        """
