import numpy as np
from SALib.sample.morris.strategy import Strategy as Strategy
from _typeshed import Incomplete
from collections.abc import Generator
from typing import List

class BruteForce(Strategy):
    """Implements the brute force optimisation strategy"""
    def brute_force_most_distant(self, input_sample: np.ndarray, num_samples: int, num_params: int, k_choices: int, num_groups: int = None) -> List:
        """Use brute force method to find most distant trajectories

        Parameters
        ----------
        input_sample : numpy.ndarray
        num_samples : int
            The number of samples to generate
        num_params : int
            The number of parameters
        k_choices : int
            The number of optimal trajectories
        num_groups : int, default=None
            The number of groups

        Returns
        -------
        list
        """
    def find_most_distant(self, input_sample: np.ndarray, num_samples: int, num_params: int, k_choices: int, num_groups: int = None) -> np.ndarray:
        """
        Finds the 'k_choices' most distant choices from the
        'num_samples' trajectories contained in 'input_sample'

        Parameters
        ----------
        input_sample : numpy.ndarray
        num_samples : int
            The number of samples to generate
        num_params : int
            The number of parameters
        k_choices : int
            The number of optimal trajectories
        num_groups : int, default=None
            The number of groups

        Returns
        -------
        numpy.ndarray
        """
    @staticmethod
    def grouper(n, iterable) -> Generator[Incomplete, None, None]: ...
    @staticmethod
    def mappable(combos, pairwise, distance_matrix):
        """
        Obtains scores from the distance_matrix for each pairwise combination
        held in the combos array

        Parameters
        ----------
        combos : numpy.ndarray
        pairwise : numpy.ndarray
        distance_matrix : numpy.ndarray
        """
    def find_maximum(self, scores, N, k_choices):
        """Finds the `k_choices` maximum scores from `scores`

        Parameters
        ----------
        scores : numpy.ndarray
        N : int
        k_choices : int

        Returns
        -------
        list
        """
    @staticmethod
    def nth(iterable, n, default: Incomplete | None = None):
        """Returns the nth item or a default value

        Parameters
        ----------
        iterable : iterable
        n : int
        default : default=None
            The default value to return
        """
