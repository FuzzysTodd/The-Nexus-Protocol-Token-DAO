import numpy as np
from . import common_args as common_args, sobol_sequence as sobol_sequence
from ..util import read_param_file as read_param_file, scale_samples as scale_samples
from typing import Dict

def sample(problem: Dict, N: int, delta: float = 0.01, seed: int = None, skip_values: int = 1024) -> np.ndarray:
    """
    Generate matrix of samples for Derivative-based Global Sensitivity Measure (DGSM).

    Start from a QMC (Sobol') sequence and finite difference with delta % steps

    Parameters
    ----------
    problem : dict
        SALib problem specification
    N : int
        Number of samples
    delta : float
        Finite difference step size (percent)
    seed : int or None
        Random seed value
    skip_values : int
        How many values of the Sobol sequence to skip

    Returns
    -------
    np.array : DGSM sequence

    References
    ----------
    1. Sobol', I.M., Kucherenko, S., 2009.
       Derivative based global sensitivity measures and their link with
       global sensitivity indices.
       Mathematics and Computers in Simulation 79, 3009-3017.
       https://doi.org/10.1016/j.matcom.2009.01.023

    2. Sobol', I.M., Kucherenko, S., 2010.
       Derivative based global sensitivity measures.
       Procedia - Social and Behavioral Sciences 2, 7745-7746.
       https://doi.org/10.1016/j.sbspro.2010.05.208
    """
def cli_parse(parser):
    """Add method specific options to CLI parser.

    Parameters
    ----------
    parser : argparse object

    Returns
    -------
    Updated argparse object
    """
def cli_action(args) -> None:
    """Run sampling method

    Parameters
    ----------
    args : argparse namespace
    """
