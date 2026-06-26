import numpy as np
from .util_funcs import avail_approaches as avail_approaches, read_param_file as read_param_file
from typing import Dict

__all__ = ['scale_samples', 'read_param_file', 'avail_approaches']

def scale_samples(params: np.ndarray, problem: Dict):
    """Scale samples based on specified distribution (defaulting to uniform).

    Adds an entry to the problem specification to indicate samples have been
    scaled to maintain backwards compatibility (`sample_scaled`).

    Parameters
    ----------
    params : np.ndarray,
        numpy array of dimensions `num_params`-by-:math:`N`,
        where :math:`N` is the number of samples
    problem : dictionary,
        SALib problem specification

    Returns
    -------
    np.ndarray, scaled samples
    """
