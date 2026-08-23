from . import paths
from _typeshed import Incomplete

__all__ = ['RandomGreedy', 'random_greedy', 'random_greedy_128']

class RandomOptimizer(paths.PathOptimizer):
    """Base class for running any random path finder that benefits
    from repeated calling, possibly in a parallel fashion. Custom random
    optimizers should subclass this, and the ``setup`` method should be
    implemented with the following signature::

        def setup(self, inputs, output, size_dict):
            # custom preparation here ...
            return trial_fn, trial_args

    Where ``trial_fn`` itself should have the signature::

        def trial_fn(r, *trial_args):
            # custom computation of path here
            return ssa_path, cost, size

    Where ``r`` is the run number and could for example be used to seed a
    random number generator. See ``RandomGreedy`` for an example.


    Parameters
    ----------
    max_repeats : int, optional
        The maximum number of repeat trials to have.
    max_time : float, optional
        The maximum amount of time to run the algorithm for.
    minimize : {'flops', 'size'}, optional
        Whether to favour paths that minimize the total estimated flop-count or
        the size of the largest intermediate created.
    parallel : {bool, int, or executor-pool like}, optional
        Whether to parallelize the random trials, by default ``False``. If
        ``True``, use a ``concurrent.futures.ProcessPoolExecutor`` with the same
        number of processes as cores. If an integer is specified, use that many
        processes instead. Finally, you can supply a custom executor-pool which
        should have an API matching that of the python 3 standard library
        module ``concurrent.futures``. Namely, a ``submit`` method that returns
        ``Future`` objects, themselves with ``result`` and ``cancel`` methods.
    pre_dispatch : int, optional
        If running in parallel, how many jobs to pre-dispatch so as to avoid
        submitting all jobs at once. Should also be more than twice the number
        of workers to avoid under-subscription. Default: 128.

    Attributes
    ----------
    path : list[tuple[int]]
        The best path found so far.
    costs : list[int]
        The list of each trial's costs found so far.
    sizes : list[int]
        The list of each trial's largest intermediate size so far.

    See Also
    --------
    RandomGreedy
    """
    max_repeats: Incomplete
    max_time: Incomplete
    minimize: Incomplete
    better: Incomplete
    pre_dispatch: Incomplete
    costs: Incomplete
    sizes: Incomplete
    best: Incomplete
    def __init__(self, max_repeats: int = 32, max_time: Incomplete | None = None, minimize: str = 'flops', parallel: bool = False, pre_dispatch: int = 128) -> None: ...
    @property
    def path(self):
        """The best path found so far.
        """
    @property
    def parallel(self): ...
    @parallel.setter
    def parallel(self, parallel) -> None: ...
    def setup(self, inputs, output, size_dict) -> None: ...
    def __call__(self, inputs, output, size_dict, memory_limit): ...
    def __del__(self) -> None: ...

class RandomGreedy(RandomOptimizer):
    """

    Parameters
    ----------
    cost_fn : callable, optional
        A function that returns a heuristic 'cost' of a potential contraction
        with which to sort candidates. Should have signature
        ``cost_fn(size12, size1, size2, k12, k1, k2)``.
    temperature : float, optional
        When choosing a possible contraction, its relative probability will be
        proportional to ``exp(-cost / temperature)``. Thus the larger
        ``temperature`` is, the further random paths will stray from the normal
        'greedy' path. Conversely, if set to zero, only paths with exactly the
        same cost as the best at each step will be explored.
    rel_temperature : bool, optional
        Whether to normalize the ``temperature`` at each step to the scale of
        the best cost. This is generally beneficial as the magnitude of costs
        can vary significantly throughout a contraction. If False, the
        algorithm will end up branching when the absolute cost is low, but
        stick to the 'greedy' path when the cost is high - this can also be
        beneficial.
    nbranch : int, optional
        How many potential paths to calculate probability for and choose from
        at each step.
    kwargs
        Supplied to RandomOptimizer.

    See Also
    --------
    RandomOptimizer
    """
    cost_fn: Incomplete
    temperature: Incomplete
    rel_temperature: Incomplete
    nbranch: Incomplete
    def __init__(self, cost_fn: str = 'memory-removed-jitter', temperature: float = 1.0, rel_temperature: bool = True, nbranch: int = 8, **kwargs) -> None: ...
    @property
    def choose_fn(self):
        """The function that chooses which contraction to take - make this a
        property so that ``temperature`` and ``nbranch`` etc. can be updated
        between runs.
        """
    def setup(self, inputs, output, size_dict): ...

def random_greedy(inputs, output, idx_dict, memory_limit: Incomplete | None = None, **optimizer_kwargs):
    """
    """

random_greedy_128: Incomplete
