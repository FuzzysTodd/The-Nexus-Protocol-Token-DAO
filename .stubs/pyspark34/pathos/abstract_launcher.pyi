__all__ = ['AbstractPipeConnection', 'AbstractWorkerPool']

class AbstractPipeConnection:
    """
AbstractPipeConnection base class for pathos pipes.
    """
    def __init__(self, *args, **kwds) -> None:
        """
Required input:
    ???

Additional inputs:
    ???

Important class members:
    ???

Other class members:
    ???
        """

class AbstractWorkerPool:
    """
AbstractWorkerPool base class for pathos pools.
    """
    def __init__(self, *args, **kwds) -> None:
        """
Important class members:
    nodes\t- number (and potentially description) of workers
    ncpus       - number of worker processors
    servers     - list of worker servers
    scheduler   - the associated scheduler
    workdir     - associated $WORKDIR for scratch calculations/files

Other class members:
    scatter     - True, if uses 'scatter-gather' (instead of 'worker-pool')
    source      - False, if minimal use of TemporaryFiles is desired
    timeout\t- number of seconds to wait for return value from scheduler
        """
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def clear(self) -> None:
        """Remove server with matching state"""
    def map(self, f, *args, **kwds) -> None:
        """run a batch of jobs with a blocking and ordered map

Returns a list of results of applying the function f to the items of
the argument sequence(s). If more than one sequence is given, the
function is called with an argument list consisting of the corresponding
item of each sequence. Some maps accept the `chunksize` keyword, which
causes the sequence to be split into tasks of approximately the given size.
        """
    def imap(self, f, *args, **kwds) -> None:
        """run a batch of jobs with a non-blocking and ordered map

Returns a list iterator of results of applying the function f to the items
of the argument sequence(s). If more than one sequence is given, the
function is called with an argument list consisting of the corresponding
item of each sequence. Some maps accept the `chunksize` keyword, which
causes the sequence to be split into tasks of approximately the given size.
        """
    def uimap(self, f, *args, **kwds) -> None:
        """run a batch of jobs with a non-blocking and unordered map

Returns a list iterator of results of applying the function f to the items
of the argument sequence(s). If more than one sequence is given, the
function is called with an argument list consisting of the corresponding
item of each sequence. The order of the resulting sequence is not guaranteed.
Some maps accept the `chunksize` keyword, which causes the sequence to be
split into tasks of approximately the given size.
        """
    def amap(self, f, *args, **kwds) -> None:
        """run a batch of jobs with an asynchronous map

Returns a results object which containts the results of applying the
function f to the items of the argument sequence(s). If more than one
sequence is given, the function is called with an argument list consisting
of the corresponding item of each sequence. To retrieve the results, call
the get() method on the returned results object. The call to get() is
blocking, until all results are retrieved. Use the ready() method on the
result object to check if all results are ready. Some maps accept the
`chunksize` keyword, which causes the sequence to be split into tasks of
approximately the given size.
        """
    def pipe(self, f, *args, **kwds) -> None:
        """submit a job and block until results are available

Returns result of calling the function f on a selected worker.  This function
will block until results are available.
        """
    def apipe(self, f, *args, **kwds) -> None:
        """submit a job asynchronously to a queue

Returns a results object which containts the result of calling the
function f on a selected worker. To retrieve the results, call the
get() method on the returned results object. The call to get() is
blocking, until the result is available. Use the ready() method on the
results object to check if the result is ready.
        """
