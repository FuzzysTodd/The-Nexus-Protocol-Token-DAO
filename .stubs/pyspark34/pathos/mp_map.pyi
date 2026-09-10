__all__ = ['mp_map']

def mp_map(function, sequence, *args, **kwds):
    """extend python's parallel map function to multiprocessing

Args:
    function - target function
    sequence - sequence to process in parallel
    nproc - number of 'local' cpus to use  [defaut = 'autodetect']
    type - processing type ['blocking', 'non-blocking', 'unordered']
    threads - if True, use threading instead of multiprocessing
    """
