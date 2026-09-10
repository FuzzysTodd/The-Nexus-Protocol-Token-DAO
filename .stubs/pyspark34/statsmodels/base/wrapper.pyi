from _typeshed import Incomplete

class ResultsWrapper:
    """
    Class which wraps a statsmodels estimation Results class and steps in to
    reattach metadata to results (if available)
    """
    __doc__: Incomplete
    def __init__(self, results) -> None: ...
    def __dir__(self): ...
    def __getattribute__(self, attr): ...
    def save(self, fname, remove_data: bool = False) -> None:
        """
        Save a pickle of this instance.

        Parameters
        ----------
        fname : {str, handle}
            Either a filename or a valid file handle.
        remove_data : bool
            If False (default), then the instance is pickled without changes.
            If True, then all arrays with length nobs are set to None before
            pickling. See the remove_data method.
            In some cases not all arrays will be set to None.
        """
    @classmethod
    def load(cls, fname):
        """
        Load a pickled results instance

        .. warning::

           Loading pickled models is not secure against erroneous or
           maliciously constructed data. Never unpickle data received from
           an untrusted or unauthenticated source.

        Parameters
        ----------
        fname : {str, handle}
            A string filename or a file handle.

        Returns
        -------
        Results
            The unpickled results instance.
        """

def union_dicts(*dicts): ...
def make_wrapper(func, how): ...
def populate_wrapper(klass, wrapping) -> None: ...
