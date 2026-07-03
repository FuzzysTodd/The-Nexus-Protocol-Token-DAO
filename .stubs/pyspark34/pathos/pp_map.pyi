from pathos.pp import stats as stats

def ppmap(processes, function, sequence, *sequences):
    """Split the work of 'function' across the given number of
    processes.  Set 'processes' to None to let Parallel Python
    autodetect the number of children to use.

    Although the calling semantics should be identical to
    __builtin__.map (even using __builtin__.map to process
    arguments), it differs in that it returns a generator instead of a
    list.  This enables lazy evaluation of the results so that other
    work can be done while the subprocesses are still running.

    >>> def rangetotal(n): return n, sum(range(n))
    >>> list(map(rangetotal, range(1, 6)))
    [(1, 0), (2, 1), (3, 3), (4, 6), (5, 10)]
    >>> list(ppmap(1, rangetotal, range(1, 6)))
    [(1, 0), (2, 1), (3, 3), (4, 6), (5, 10)]
    """
def pp_map(function, sequence, *args, **kwds):
    """extend python's parallel map function to parallel python

Args:
    function - target function
    sequence - sequence to process in parallel
    ncpus - number of 'local' processors to use  [defaut = 'autodetect']
    servers - available distributed parallel python servers  [default = ()]
    """
