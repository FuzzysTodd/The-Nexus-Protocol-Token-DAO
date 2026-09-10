import numpy as np
from _typeshed import Incomplete

__all__ = ['ProblemSpec']

class ProblemSpec(dict):
    """Dictionary-like object representing an SALib Problem specification.

    Attributes
    ----------
    samples : np.array, of generated samples
    results : np.array, of evaluations (i.e., model outputs)
    analysis : np.array or dict, of sensitivity indices
    """
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def samples(self): ...
    @samples.setter
    def samples(self, vals) -> None: ...
    @property
    def results(self): ...
    @results.setter
    def results(self, vals) -> None: ...
    @property
    def analysis(self): ...
    def sample(self, func, *args, **kwargs):
        """Create sample using given function.

        Parameters
        ----------
        func : function,
            Sampling method to use. The given function must accept the SALib
            problem specification as the first parameter and return a numpy
            array.

        *args : list,
            Additional arguments to be passed to `func`

        **kwargs : dict,
            Additional keyword arguments passed to `func`

        Returns
        -------
        self : ProblemSpec object
        """
    def set_samples(self, samples: np.ndarray):
        """Set previous samples used."""
    def set_results(self, results: np.ndarray):
        """Set previously available model results."""
    def evaluate(self, func, *args, **kwargs):
        """Evaluate a given model.

        Parameters
        ----------
        func : function,
            Model, or function that wraps a model, to be run/evaluated.
            The provided function is required to accept a numpy array of
            inputs as its first parameter and must return a numpy array of
            results.

        *args : list,
            Additional arguments to be passed to `func`

        nprocs : int,
            If specified, attempts to parallelize model evaluations

        **kwargs : dict,
            Additional keyword arguments passed to `func`

        Returns
        -------
        self : ProblemSpec object
        """
    def evaluate_parallel(self, func, *args, nprocs: Incomplete | None = None, **kwargs):
        """Evaluate model locally in parallel.

        All detected processors will be used if `nprocs` is not specified.

        Parameters
        ----------
        func : function,
            Model, or function that wraps a model, to be run in parallel.
            The provided function needs to accept a numpy array of inputs as
            its first parameter and must return a numpy array of results.

        nprocs : int,
            Number of processors to use.
            Capped to the number of available processors.

        *args : list,
            Additional arguments to be passed to `func`

        **kwargs : dict,
            Additional keyword arguments passed to `func`

        Returns
        -------
        self : ProblemSpec object
        """
    def evaluate_distributed(self, func, *args, nprocs: int = 1, servers: Incomplete | None = None, verbose: bool = False, **kwargs):
        """Distribute model evaluation across a cluster.

        Usage Conditions:

        * The provided function needs to accept a numpy array of inputs as
          its first parameter
        * The provided function must return a numpy array of results


        Parameters
        ----------
        func : function,
            Model, or function that wraps a model, to be run in parallel

        nprocs : int,
            Number of processors to use for each node. Defaults to 1.

        servers : list[str] or None,
            IP addresses or alias for each server/node to use.

        verbose : bool,
            Display job execution statistics. Defaults to False.

        *args : list,
            Additional arguments to be passed to `func`

        **kwargs : dict,
            Additional keyword arguments passed to `func`

        Returns
        -------
        self : ProblemSpec object
        """
    def analyze(self, func, *args, **kwargs):
        """Analyze sampled results using given function.

        Parameters
        ----------
        func : function,
            Analysis method to use. The provided function must accept the
            problem specification as the first parameter, X values if needed,
            Y values, and return a numpy array.

        *args : list,
            Additional arguments to be passed to `func`

        nprocs : int,
            If specified, attempts to parallelize model evaluations

        **kwargs : dict,
            Additional keyword arguments passed to `func`

        Returns
        -------
        self : ProblemSpec object
        """
    def analyze_parallel(self, func, *args, nprocs: Incomplete | None = None, **kwargs):
        """Analyze sampled results using the given function in parallel.

        Parameters
        ----------
        func : function,
            Analysis method to use. The provided function must accept the
            problem specification as the first parameter, X values if needed,
            Y values, and return a numpy array.

        *args : list,
            Additional arguments to be passed to `func`

        nprocs : int,
            Number of processors to use.
            Capped to the number of outputs or available processors.

        **kwargs : dict,
            Additional keyword arguments passed to `func`

        Returns
        -------
        self : ProblemSpec object
        """
    def to_df(self):
        """Convert results to Pandas DataFrame."""
    def plot(self, **kwargs):
        """Plot results as a bar chart.

        Returns
        -------
        axes : matplotlib axes object
        """
    def heatmap(self, metric: str = None, index: str = None, title: str = None, ax: Incomplete | None = None):
        """Plot results as a heatmap.

        Parameters
        ----------
        metric : str or None, name of output to analyze (display all if `None`)
        index : str or None, name of index to plot, dependent on what
                    analysis was conducted (ST, S1, etc; displays all if `None`)
        title : str, title of plot to use (defaults to the same as `metric`)
        ax : axes object, matplotlib axes object to use for plot.
                Creates a new figure if not provided.

        Returns
        -------
        ax : matplotlib axes object
        """
