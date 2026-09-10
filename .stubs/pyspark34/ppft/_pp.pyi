import types
from . import transport as pptransport
from _typeshed import Incomplete

user = types
copyright: Incomplete
__version__: Incomplete
version: Incomplete
RECONNECT_WAIT_TIME: int
SHOW_EXPECTED_EXCEPTIONS: bool

class _Task:
    """Class describing single task (job)
    """
    lock: Incomplete
    tid: Incomplete
    server: Incomplete
    callback: Incomplete
    callbackargs: Incomplete
    group: Incomplete
    finished: bool
    unpickled: bool
    def __init__(self, server, tid, callback: Incomplete | None = None, callbackargs=(), group: str = 'default') -> None:
        """Initializes the task"""
    sresult: Incomplete
    def finalize(self, sresult) -> None:
        """Finalizes the task.

           For internal use only"""
    def __call__(self, raw_result: bool = False):
        """Retrieves result of the task"""
    def wait(self) -> None:
        """Waits for the task"""

class _Worker:
    """Local worker class
    """
    command: Incomplete
    restart_on_free: Incomplete
    pickle_proto: Incomplete
    def __init__(self, restart_on_free, pickle_proto) -> None:
        """Initializes local worker"""
    t: Incomplete
    pid: Incomplete
    is_free: bool
    def start(self) -> None:
        """Starts local worker"""
    def stop(self) -> None:
        """Stops local worker"""
    def restart(self) -> None:
        """Restarts local worker"""
    def free(self) -> None:
        """Frees local worker"""

class _RWorker(pptransport.CSocketTransport):
    """Remote worker class
    """
    server: Incomplete
    persistent: Incomplete
    host: Incomplete
    port: Incomplete
    secret: Incomplete
    address: Incomplete
    id: Incomplete
    socket_timeout: Incomplete
    def __init__(self, host, port, secret, server, message, persistent, socket_timeout) -> None:
        """Initializes remote worker"""
    def __del__(self) -> None:
        """Closes connection with remote server"""
    is_free: bool
    def connect(self, message: Incomplete | None = None):
        """Connects to a remote server"""

class _Statistics:
    """Class to hold execution statisitcs for a single node
    """
    ncpus: Incomplete
    time: float
    njobs: int
    rworker: Incomplete
    def __init__(self, ncpus, rworker: Incomplete | None = None) -> None:
        """Initializes statistics for a node"""

class Template:
    """Template class
    """
    job_server: Incomplete
    func: Incomplete
    depfuncs: Incomplete
    modules: Incomplete
    callback: Incomplete
    callbackargs: Incomplete
    group: Incomplete
    globals: Incomplete
    def __init__(self, job_server, func, depfuncs=(), modules=(), callback: Incomplete | None = None, callbackargs=(), group: str = 'default', globals: Incomplete | None = None) -> None:
        """Creates Template instance

           jobs_server - pp server for submitting jobs
           func - function to be executed
           depfuncs - tuple with functions which might be called from 'func'
           modules - tuple with module names to import
           callback - function which will be called with argument list equal                    to callbackargs+(result,) as soon as calculation is done
           callbackargs - additional arguments for callback function
           group - job group, is used when wait(group) is called to wait for                    jobs in a given group to finish
           globals - dictionary from which all modules, functions and classes                    will be imported, for instance: globals=globals()
        """
    def submit(self, *args):
        """Submits function with *arg arguments to the execution queue
        """

class Server:
    """Parallel Python SMP execution server class
    """
    default_port: int
    default_secret: str
    logger: Incomplete
    autopp_list: Incomplete
    ppservers: Incomplete
    auto_ppservers: Incomplete
    socket_timeout: Incomplete
    secret: Incomplete
    def __init__(self, ncpus: str = 'autodetect', ppservers=(), secret: Incomplete | None = None, restart: bool = False, proto: int = 2, socket_timeout: int = 3600) -> None:
        '''Creates Server instance

           ncpus - the number of worker processes to start on the local                    computer, if parameter is omitted it will be set to                    the number of processors in the system
           ppservers - list of active parallel python execution servers                    to connect with
           secret - passphrase for network connections, if omitted a default                    passphrase will be used. It\'s highly recommended to use a                    custom passphrase for all network connections.
           restart - restart the worker process after each task completion
           proto - protocol number for pickle module
           socket_timeout - socket timeout in seconds, which is the maximum                    time a remote job could be executed. Increase this value                    if you have long running jobs or decrease if connectivity                    to remote ppservers is often lost.

           With ncpus = 1 all tasks are executed consequently.
           For the best performance either use the default "autodetect" value
           or set ncpus to the total number of processors in the system.
        '''
    def submit(self, func, args=(), depfuncs=(), modules=(), callback: Incomplete | None = None, callbackargs=(), group: str = 'default', globals: Incomplete | None = None):
        """Submits function to the execution queue

           func - function to be executed
           args - tuple with arguments of the 'func'
           depfuncs - tuple with functions which might be called from 'func'
           modules - tuple with module names to import
           callback - function which will be called with argument list equal                    to callbackargs+(result,) as soon as calculation is done
           callbackargs - additional arguments for callback function
           group - job group, is used when wait(group) is called to wait for                    jobs in a given group to finish
           globals - dictionary from which all modules, functions and classes                    will be imported, for instance: globals=globals()
        """
    def wait(self, group: Incomplete | None = None) -> None:
        """Waits for all jobs in a given group to finish.
           If group is omitted waits for all jobs to finish
        """
    def get_ncpus(self):
        """Returns the number of local worker processes (ppworkers)"""
    def set_ncpus(self, ncpus: str = 'autodetect') -> None:
        """Sets the number of local worker processes (ppworkers)

        ncpus - the number of worker processes, if parammeter is omitted
                it will be set to the number of processors in the system"""
    def get_active_nodes(self):
        """Returns active nodes as a dictionary
        [keys - nodes, values - ncpus]"""
    def get_stats(self):
        """Returns job execution statistics as a dictionary"""
    def print_stats(self) -> None:
        """Prints job execution statistics. Useful for benchmarking on
           clusters"""
    def insert(self, sfunc, sargs, task: Incomplete | None = None):
        """Inserts function into the execution queue. It's intended for
           internal use only (in ppserver).
        """
    def connect1(self, host, port, persistent: bool = True) -> None:
        """Conects to a remote ppserver specified by host and port"""
    def __del__(self) -> None: ...
    def destroy(self) -> None:
        """Kills ppworkers and closes open files"""

class DestroyedServerError(RuntimeError): ...
