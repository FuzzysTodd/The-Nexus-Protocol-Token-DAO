import numpy as np
from SALib import ProblemSpec as ProblemSpec

def evaluate(X: np.ndarray, A: np.ndarray, M: np.ndarray) -> np.ndarray:
    """Test function taken from Oakley and O'Hagan (2004) (see Eqn. 21 in [1])


    References
    ----------
    .. [1] Oakley, J.E., O’Hagan, A., 2004.
           Probabilistic sensitivity analysis of complex models: a Bayesian approach.
           Journal of the Royal Statistical Society: Series B
           (Statistical Methodology) 66, 751–769.
           https://doi.org/10.1111/j.1467-9868.2004.05304.x
    """
