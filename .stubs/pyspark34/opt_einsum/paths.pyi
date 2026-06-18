from _typeshed import Incomplete

__all__ = ['optimal', 'BranchBound', 'branch', 'greedy', 'auto', 'auto_hq', 'get_path_fn', 'DynamicProgramming', 'dynamic_programming']

class PathOptimizer:
    '''Base class for different path optimizers to inherit from.

    Subclassed optimizers should define a call method with signature::

        def __call__(self, inputs, output, size_dict, memory_limit=None):
            """
            Parameters
            ----------
            inputs : list[set[str]]
                The indices of each input array.
            outputs : set[str]
                The output indices
            size_dict : dict[str, int]
                The size of each index
            memory_limit : int, optional
                If given, the maximum allowed memory.
            """
            # ... compute path here ...
            return path

    where ``path`` is a list of int-tuples specifiying a contraction order.
    '''
    def __call__(self, inputs, output, size_dict, memory_limit: Incomplete | None = None) -> None: ...

def optimal(inputs, output, size_dict, memory_limit: Incomplete | None = None):
    """
    Computes all possible pair contractions in a depth-first recursive manner,
    sieving results based on ``memory_limit`` and the best path found so far.
    Returns the lowest cost path. This algorithm scales factoriallly with
    respect to the elements in the list ``input_sets``.

    Parameters
    ----------
    inputs : list
        List of sets that represent the lhs side of the einsum subscript.
    output : set
        Set that represents the rhs side of the overall einsum subscript.
    size_dict : dictionary
        Dictionary of index sizes.
    memory_limit : int
        The maximum number of elements in a temporary array.

    Returns
    -------
    path : list
        The optimal contraction order within the memory limit constraint.

    Examples
    --------
    >>> isets = [set('abd'), set('ac'), set('bdc')]
    >>> oset = set('')
    >>> idx_sizes = {'a': 1, 'b':2, 'c':3, 'd':4}
    >>> optimal(isets, oset, idx_sizes, 5000)
    [(0, 2), (0, 1)]
    """

class BranchBound(PathOptimizer):
    """
    Explores possible pair contractions in a depth-first recursive manner like
    the ``optimal`` approach, but with extra heuristic early pruning of branches
    as well sieving by ``memory_limit`` and the best path found so far. Returns
    the lowest cost path. This algorithm still scales factorially with respect
    to the elements in the list ``input_sets`` if ``nbranch`` is not set, but it
    scales exponentially like ``nbranch**len(input_sets)`` otherwise.

    Parameters
    ----------
    nbranch : None or int, optional
        How many branches to explore at each contraction step. If None, explore
        all possible branches. If an integer, branch into this many paths at
        each step. Defaults to None.
    cutoff_flops_factor : float, optional
        If at any point, a path is doing this much worse than the best path
        found so far was, terminate it. The larger this is made, the more paths
        will be fully explored and the slower the algorithm. Defaults to 4.
    minimize : {'flops', 'size'}, optional
        Whether to optimize the path with regard primarily to the total
        estimated flop-count, or the size of the largest intermediate. The
        option not chosen will still be used as a secondary criterion.
    cost_fn : callable, optional
        A function that returns a heuristic 'cost' of a potential contraction
        with which to sort candidates. Should have signature
        ``cost_fn(size12, size1, size2, k12, k1, k2)``.
    """
    nbranch: Incomplete
    cutoff_flops_factor: Incomplete
    minimize: Incomplete
    cost_fn: Incomplete
    better: Incomplete
    best: Incomplete
    best_progress: Incomplete
    def __init__(self, nbranch: Incomplete | None = None, cutoff_flops_factor: int = 4, minimize: str = 'flops', cost_fn: str = 'memory-removed') -> None: ...
    @property
    def path(self): ...
    def __call__(self, inputs, output, size_dict, memory_limit: Incomplete | None = None):
        """

        Parameters
        ----------
        input_sets : list
            List of sets that represent the lhs side of the einsum subscript
        output_set : set
            Set that represents the rhs side of the overall einsum subscript
        idx_dict : dictionary
            Dictionary of index sizes
        memory_limit : int
            The maximum number of elements in a temporary array

        Returns
        -------
        path : list
            The contraction order within the memory limit constraint.

        Examples
        --------
        >>> isets = [set('abd'), set('ac'), set('bdc')]
        >>> oset = set('')
        >>> idx_sizes = {'a': 1, 'b':2, 'c':3, 'd':4}
        >>> optimal(isets, oset, idx_sizes, 5000)
        [(0, 2), (0, 1)]
        """

def branch(inputs, output, size_dict, memory_limit: Incomplete | None = None, **optimizer_kwargs): ...
def greedy(inputs, output, size_dict, memory_limit: Incomplete | None = None, choose_fn: Incomplete | None = None, cost_fn: str = 'memory-removed'):
    """
    Finds the path by a three stage algorithm:

    1. Eagerly compute Hadamard products.
    2. Greedily compute contractions to maximize ``removed_size``
    3. Greedily compute outer products.

    This algorithm scales quadratically with respect to the
    maximum number of elements sharing a common dim.

    Parameters
    ----------
    inputs : list
        List of sets that represent the lhs side of the einsum subscript
    output : set
        Set that represents the rhs side of the overall einsum subscript
    size_dict : dictionary
        Dictionary of index sizes
    memory_limit : int
        The maximum number of elements in a temporary array
    choose_fn : callable, optional
        A function that chooses which contraction to perform from the queu
    cost_fn : callable, optional
        A function that assigns a potential contraction a cost.

    Returns
    -------
    path : list
        The contraction order (a list of tuples of ints).

    Examples
    --------
    >>> isets = [set('abd'), set('ac'), set('bdc')]
    >>> oset = set('')
    >>> idx_sizes = {'a': 1, 'b':2, 'c':3, 'd':4}
    >>> greedy(isets, oset, idx_sizes)
    [(0, 2), (0, 1)]
    """

class DynamicProgramming(PathOptimizer):
    """
    Finds the optimal path of pairwise contractions without intermediate outer
    products based a dynamic programming approach presented in
    Phys. Rev. E 90, 033315 (2014) (the corresponding preprint is publically
    available at https://arxiv.org/abs/1304.6112). This method is especially
    well-suited in the area of tensor network states, where it usually
    outperforms all the other optimization strategies.

    This algorithm shows exponential scaling with the number of inputs
    in the worst case scenario (see example below). If the graph to be
    contracted consists of disconnected subgraphs, the algorithm scales
    linearly in the number of disconnected subgraphs and only exponentially
    with the number of inputs per subgraph.

    Parameters
    ----------
    minimize : {'flops', 'size'}, optional
        Whether to find the contraction that minimizes the number of
        operations or the size of the largest intermediate tensor.
    cost_cap : {True, False, int}, optional
        How to implement cost-capping:

            * True - iteratively increase the cost-cap
            * False - implement no cost-cap at all
            * int - use explicit cost cap

    search_outer : bool, optional
        In rare circumstances the optimal contraction may involve an outer
        product, this option allows searching such contractions but may well
        slow down the path finding considerably on all but very small graphs.
    """
    minimize: Incomplete
    search_outer: Incomplete
    cost_cap: Incomplete
    def __init__(self, minimize: str = 'flops', cost_cap: bool = True, search_outer: bool = False) -> None: ...
    def __call__(self, inputs, output, size_dict, memory_limit: Incomplete | None = None):
        """
        Parameters
        ----------
        inputs : list
            List of sets that represent the lhs side of the einsum subscript
        output : set
            Set that represents the rhs side of the overall einsum subscript
        size_dict : dictionary
            Dictionary of index sizes
        memory_limit : int
            The maximum number of elements in a temporary array

        Returns
        -------
        path : list
            The contraction order (a list of tuples of ints).

        Examples
        --------
        >>> n_in = 3  # exponential scaling
        >>> n_out = 2 # linear scaling
        >>> s = dict()
        >>> i_all = []
        >>> for _ in range(n_out):
        >>>     i = [set() for _ in range(n_in)]
        >>>     for j in range(n_in):
        >>>         for k in range(j+1, n_in):
        >>>             c = oe.get_symbol(len(s))
        >>>             i[j].add(c)
        >>>             i[k].add(c)
        >>>             s[c] = 2
        >>>     i_all.extend(i)
        >>> o = DynamicProgramming()
        >>> o(i_all, set(), s)
        [(1, 2), (0, 4), (1, 2), (0, 2), (0, 1)]
        """

def dynamic_programming(inputs, output, size_dict, memory_limit: Incomplete | None = None, **kwargs): ...
def auto(inputs, output, size_dict, memory_limit: Incomplete | None = None):
    """Finds the contraction path by automatically choosing the method based on
    how many input arguments there are.
    """
def auto_hq(inputs, output, size_dict, memory_limit: Incomplete | None = None):
    """Finds the contraction path by automatically choosing the method based on
    how many input arguments there are, but targeting a more generous
    amount of search time than ``'auto'``.
    """
def get_path_fn(path_type):
    """Get the correct path finding function from str ``path_type``.
    """
