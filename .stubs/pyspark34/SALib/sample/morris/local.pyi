import numpy as np
from .strategy import Strategy as Strategy
from typing import List, Tuple

class LocalOptimisation(Strategy):
    """Implements the local optimisation algorithm using the Strategy interface"""
    def find_local_maximum(self, input_sample: np.ndarray, N: int, num_params: int, k_choices: int, num_groups: int = None) -> List:
        """Find the most different trajectories in the input sample using a
        local approach

        An alternative by Ruano et al. (2012) for the brute force approach as
        originally proposed by Campolongo et al. (2007). The method should
        improve the speed with which an optimal set of trajectories is
        found tremendously for larger sample sizes.

        Parameters
        ----------
        input_sample : np.ndarray
        N : int
            The number of trajectories
        num_params : int
            The number of factors
        k_choices : int
            The number of optimal trajectories to return
        num_groups : int, default=None
            The number of groups

        Returns
        -------
        list
        """
    def sum_distances(self, indices: Tuple, distance_matrix: np.ndarray) -> np.ndarray:
        """Calculate combinatorial distance between a select group of
        trajectories, indicated by indices

        Parameters
        ----------
        indices : tuple
        distance_matrix : numpy.ndarray (M,M)

        Returns
        -------
        numpy.ndarray

        Notes
        -----
        This function can perhaps be quickened by calculating the sum of the
        distances. The calculated distances, as they are right now,
        are only used in a relative way. Purely summing distances would lead
        to the same result, at a perhaps quicker rate.
        """
    def get_max_sum_ind(self, indices_list: List[Tuple], distances: np.ndarray, i: str | int, m: str | int) -> Tuple:
        """Get the indices that belong to the maximum distance in `distances`

        Parameters
        ----------
        indices_list : list
            list of tuples
        distances : numpy.ndarray
            size M
        i : int
        m : int

        Returns
        -------
        list
        """
    def add_indices(self, indices: Tuple, distance_matrix: np.ndarray) -> List:
        """Adds extra indices for the combinatorial problem.

        Parameters
        ----------
        indices : tuple
        distance_matrix : numpy.ndarray (M,M)

        Examples
        --------
        >>> add_indices((1,2), numpy.array((5,5)))
        [(1, 2, 3), (1, 2, 4), (1, 2, 5)]

        """
