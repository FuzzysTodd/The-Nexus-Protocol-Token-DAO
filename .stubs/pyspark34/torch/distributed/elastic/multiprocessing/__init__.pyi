from _typeshed import Incomplete
from torch.distributed.elastic.multiprocessing.api import MultiprocessContext as MultiprocessContext, PContext as PContext, ProcessFailure as ProcessFailure, RunProcsResult as RunProcsResult, SignalException as SignalException, Std as Std, SubprocessContext as SubprocessContext, to_map as to_map
from torch.distributed.elastic.utils.logging import get_logger as get_logger
from typing import Callable, Dict, Tuple

log: Incomplete

def start_processes(name: str, entrypoint: Callable | str, args: Dict[int, Tuple], envs: Dict[int, Dict[str, str]], log_dir: str, start_method: str = 'spawn', redirects: Std | Dict[int, Std] = ..., tee: Std | Dict[int, Std] = ...) -> PContext:
    '''
    Starts ``n`` copies of ``entrypoint`` processes with the provided options.
    ``entrypoint`` is either a ``Callable`` (function) or a ``str`` (binary).
    The number of copies is determined by the number of entries for ``args`` and
    ``envs`` arguments, which need to have the same key set.

    ``args`` and ``env`` parameters are the arguments and environment variables
    to pass down to the entrypoint mapped by the replica index (local rank).
    All local ranks must be accounted for.
    That is, the keyset should be ``{0,1,...,(nprocs-1)}``.

    .. note:: When the ``entrypoint`` is a binary (``str``), ``args`` can only be strings.
              If any other type is given, then it is casted to a string representation
              (e.g. ``str(arg1)``). Furthermore, a binary failure will only write
              an ``error.json`` error file if the main function is annotated with
              ``torch.distributed.elastic.multiprocessing.errors.record``. For function launches,
              this is done by default and there is no need to manually annotate
              with the ``@record`` annotation.

    ``redirects`` and ``tee`` are bitmasks specifying which std stream(s) to redirect
    to a log file in the ``log_dir``. Valid mask values are defined in ``Std``.
    To redirect/tee only certain local ranks, pass ``redirects`` as a map with the key as
    the local rank to specify the redirect behavior for.
    Any missing local ranks will default to ``Std.NONE``.

    ``tee`` acts like the unix "tee" command in that it redirects + prints to console.
    To avoid worker stdout/stderr from printing to console, use the ``redirects`` parameter.

    For each process, the ``log_dir`` will contain:

    #. ``{local_rank}/error.json``: if the process failed, a file with the error info
    #. ``{local_rank}/stdout.json``: if ``redirect & STDOUT == STDOUT``
    #. ``{local_rank}/stderr.json``: if ``redirect & STDERR == STDERR``

    .. note:: It is expected that the ``log_dir`` exists, is empty, and is a directory.

    Example:

    ::

     log_dir = "/tmp/test"

     # ok; two copies of foo: foo("bar0"), foo("bar1")
     start_processes(
        name="trainer",
        entrypoint=foo,
        args:{0:("bar0",), 1:("bar1",),
        envs:{0:{}, 1:{}},
        log_dir=log_dir
     )

     # invalid; envs missing for local rank 1
     start_processes(
        name="trainer",
        entrypoint=foo,
        args:{0:("bar0",), 1:("bar1",),
        envs:{0:{}},
        log_dir=log_dir
     )

     # ok; two copies of /usr/bin/touch: touch file1, touch file2
     start_processes(
        name="trainer",
        entrypoint="/usr/bin/touch",
        args:{0:("file1",), 1:("file2",),
        envs:{0:{}, 1:{}},
        log_dir=log_dir
      )

     # caution; arguments casted to string, runs:
     # echo "1" "2" "3" and echo "[1, 2, 3]"
     start_processes(
        name="trainer",
        entrypoint="/usr/bin/echo",
        args:{0:(1,2,3), 1:([1,2,3],),
        envs:{0:{}, 1:{}},
        log_dir=log_dir
      )

    Args:
        name: a human readable short name that describes what the processes are
              (used as header when tee\'ing stdout/stderr outputs)
        entrypoint: either a ``Callable`` (function) or ``cmd`` (binary)
        args: arguments to each replica
        envs: env vars to each replica
        log_dir: directory used to write log files
        start_method: multiprocessing start method (spawn, fork, forkserver)
                      ignored for binaries
        redirects: which std streams to redirect to a log file
        tee: which std streams to redirect + print to console

    '''
