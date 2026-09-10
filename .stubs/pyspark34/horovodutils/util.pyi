from _typeshed import Incomplete
from horovod.spark.common.store import FilesystemStore

class AdlsStore(FilesystemStore):
    """
    Concrete Azure Filesystem store.
    
    Parameters
    ----------
    prefix_path: str
        Absolute or relative path in adls where store would be created
    *args: 
        Variable number of arguments
    **kwargs: dict
        Extra options that make sense to a particular storage connection, e.g.
        account_name, account_key, credential, etc.

    Examples
    --------
    Create a AdlsStore in primary storage
    >>> store = AdlsStore(prefix_path, train_path = train_path, runs_path = run_path, save_runs = bool)

    Create a AdlsStore by passing linked_service name
    >>> store = AdlsStore(prefix_path, train_path = train_path, runs_path = run_path, save_runs = bool, 
                storage_options = {'linked_service': Linked_Service_Name})

    Create a AdlsStore by passing account_key
    >>> store = AdlsStore(prefix_path, train_path = train_path, runs_path = run_path, save_runs = bool, 
                storage_options = {'account_name': XXXX, 'account_key': XXXX})

    Create a AdlsStore by passing credential
    >>> store = AdlsStore(prefix_path, train_path = train_path, runs_path = run_path, save_runs = bool, 
                storage_options = {'account_name': XXXX, 'credential': XXXX})
    """
    prefix_path: Incomplete
    sparkconf: Incomplete
    def __init__(self, prefix_path, *args, **kwargs) -> None: ...
