import abc
from _typeshed import Incomplete

class SampleMorris:
    """Computes the optimum `k_choices` of trajectories from the input_sample.

    Parameters
    ----------
    strategy : :class:`Strategy`
    """
    def __init__(self, strategy) -> None: ...
    def sample(self, input_sample, num_samples, num_params, k_choices, num_groups):
        """Computes the optimum k_choices of trajectories
        from the input_sample.

        Parameters
        ----------
        input_sample : numpy.ndarray
        num_samples : int
            The number of samples to generate
        num_params : int
            The number of parameters
        k_choices : int
            The number of optimal trajectories
        num_groups : int
            The number of groups

        Returns
        -------
        numpy.ndarray
            An array of optimal trajectories
        """

class Strategy(metaclass=abc.ABCMeta):
    """
    Declare an interface common to all supported algorithms.
    :class:`SampleMorris` uses this interface to call the algorithm
    defined by a ConcreteStrategy.
    """
    __metaclass__ = abc.ABCMeta
    def sample(self, input_sample, num_samples, num_params, k_choices, num_groups: Incomplete | None = None):
        """Computes the optimum k_choices of trajectories
        from the input_sample.

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
    def run_checks(number_samples, k_choices) -> None:
        """Runs checks on `k_choices`"""
    def compile_output(self, input_sample, num_samples, num_params, maximum_combo, num_groups: Incomplete | None = None):
        """Picks the trajectories from the input

        Parameters
        ----------
        input_sample : numpy.ndarray
        num_samples : int
        num_params : int
        maximum_combo : list
        num_groups : int

        """
    @staticmethod
    def check_input_sample(input_sample, num_params, num_samples) -> None:
        """Check the `input_sample` is valid

        Checks input sample is:
            - the correct size
            - values between 0 and 1

        Parameters
        ----------
        input_sample : numpy.ndarray
        num_params : int
        num_samples : int
        """
    @staticmethod
    def compute_distance(m, l):
        """Compute distance between two trajectories

        Parameters
        ----------
        m : np.ndarray

        l : np.ndarray

        Returns
        -------
        numpy.ndarray
        """
    def compute_distance_matrix(self, input_sample, num_samples, num_params, num_groups: Incomplete | None = None, local_optimization: bool = False):
        """Computes the distance between each and every trajectory

        Each entry in the matrix represents the sum of the geometric distances
        between all the pairs of points of the two trajectories

        If the `groups` argument is filled, then the distances are still
        calculated for each trajectory,

        Parameters
        ----------
        input_sample : numpy.ndarray
            The input sample of trajectories for which to compute
            the distance matrix
        num_samples : int
            The number of trajectories
        num_params : int
            The number of factors
        num_groups : int, default=None
            The number of groups
        local_optimization : bool, default=False
            If True, fills the lower triangle of the distance matrix

        Returns
        -------
        distance_matrix : numpy.ndarray

        """
