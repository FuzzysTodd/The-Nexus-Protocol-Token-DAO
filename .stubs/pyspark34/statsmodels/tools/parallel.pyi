from statsmodels.tools.sm_exceptions import ModuleUnavailableWarning as ModuleUnavailableWarning, module_unavailable_doc as module_unavailable_doc

def parallel_func(func, n_jobs, verbose: int = 5):
    """Return parallel instance with delayed function

    Util function to use joblib only if available

    Parameters
    ----------
    func : callable
        A function
    n_jobs : int
        Number of jobs to run in parallel
    verbose : int
        Verbosity level

    Returns
    -------
    parallel : instance of joblib.Parallel or list
        The parallel object
    my_func : callable
        func if not parallel or delayed(func)
    n_jobs : int
        Number of jobs >= 0

    Examples
    --------
    >>> from math import sqrt
    >>> from statsmodels.tools.parallel import parallel_func
    >>> parallel, p_func, n_jobs = parallel_func(sqrt, n_jobs=-1, verbose=0)
    >>> print(n_jobs)
    >>> parallel(p_func(i**2) for i in range(10))
    """
