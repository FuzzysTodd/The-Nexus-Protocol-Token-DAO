from _typeshed import Incomplete
from gevent._config import config as config
from gevent._util import copy_globals as copy_globals
from gevent.hub import reinit as reinit

EAGAIN: Incomplete
__implements__: Incomplete
__extensions__: Incomplete
ignored_errors: Incomplete

def make_nonblocking(fd):
    """Put the file descriptor *fd* into non-blocking mode if
        possible.

        :return: A boolean value that evaluates to True if successful.
        """
def nb_read(fd, n):
    """
        Read up to *n* bytes from file descriptor *fd*. Return a
        byte string containing the bytes read, which may be shorter than
        *n*. If end-of-file is reached, an empty string is returned.

        The descriptor must be in non-blocking mode.
        """
def nb_write(fd, buf):
    """
        Write some number of bytes from buffer *buf* to file
        descriptor *fd*. Return the number of bytes written, which may
        be less than the length of *buf*.

        The file descriptor must be in non-blocking mode.
        """
def tp_read(fd, n):
    """Read up to *n* bytes from file descriptor *fd*. Return a string
    containing the bytes read. If end-of-file is reached, an empty string
    is returned.

    Reading is done using the threadpool.
    """
def tp_write(fd, buf):
    """Write bytes from buffer *buf* to file descriptor *fd*. Return the
    number of bytes written.

    Writing is done using the threadpool.
    """
def fork_gevent():
    """
        Forks the process using :func:`os.fork` and prepares the
        child process to continue using gevent before returning.

        .. note::

            The PID returned by this function may not be waitable with
            either the original :func:`os.waitpid` or this module's
            :func:`waitpid` and it may not generate SIGCHLD signals if
            libev child watchers are or ever have been in use. For
            example, the :mod:`gevent.subprocess` module uses libev
            child watchers (which parts of gevent use libev child
            watchers is subject to change at any time). Most
            applications should use :func:`fork_and_watch`, which is
            monkey-patched as the default replacement for
            :func:`os.fork` and implements the ``fork`` function of
            this module by default, unless the environment variable
            ``GEVENT_NOWAITPID`` is defined before this module is
            imported.

        .. versionadded:: 1.1b2
        """
def fork():
    """
        A wrapper for :func:`fork_gevent` for non-POSIX platforms.
        """
def forkpty_gevent():
    """
            Forks the process using :func:`os.forkpty` and prepares the
            child process to continue using gevent before returning.

            Returns a tuple (pid, master_fd). The `master_fd` is *not* put into
            non-blocking mode.

            Availability: Some Unix systems.

            .. seealso:: This function has the same limitations as :func:`fork_gevent`.

            .. versionadded:: 1.1b5
            """
forkpty = forkpty_gevent

def waitpid(pid, options):
    """
            Wait for a child process to finish.

            If the child process was spawned using
            :func:`fork_and_watch`, then this function behaves
            cooperatively. If not, it *may* have race conditions; see
            :func:`fork_gevent` for more information.

            The arguments are as for the underlying
            :func:`os.waitpid`. Some combinations of *options* may not
            be supported cooperatively (as of 1.1 that includes
            WUNTRACED). Using a *pid* of 0 to request waiting on only processes
            from the current process group is not cooperative. A *pid* of -1
            to wait for any child is non-blocking, but may or may not
            require a trip around the event loop, depending on whether any children
            have already terminated but not been waited on.

            Availability: POSIX.

            .. versionadded:: 1.1b1
            .. versionchanged:: 1.2a1
               More cases are handled in a cooperative manner.
            """
def fork_and_watch(callback: Incomplete | None = None, loop: Incomplete | None = None, ref: bool = False, fork=...):
    """
            Fork a child process and start a child watcher for it in the parent process.

            This call cooperates with :func:`waitpid` to enable cooperatively waiting
            for children to finish. When monkey-patching, these functions are patched in as
            :func:`os.fork` and :func:`os.waitpid`, respectively.

            In the child process, this function calls :func:`gevent.hub.reinit` before returning.

            Availability: POSIX.

            :keyword callback: If given, a callable that will be called with the child watcher
                when the child finishes.
            :keyword loop: The loop to start the watcher in. Defaults to the
                loop of the current hub.
            :keyword fork: The fork function. Defaults to :func:`the one defined in this
                module <gevent.os.fork_gevent>` (which automatically calls :func:`gevent.hub.reinit`).
                Pass the builtin :func:`os.fork` function if you do not need to
                initialize gevent in the child process.

            .. versionadded:: 1.1b1
            .. seealso::
                :func:`gevent.monkey.get_original` To access the builtin :func:`os.fork`.
            """
def forkpty_and_watch(callback: Incomplete | None = None, loop: Incomplete | None = None, ref: bool = False, forkpty=...):
    """
                Like :func:`fork_and_watch`, except using :func:`forkpty_gevent`.

                Availability: Some Unix systems.

                .. versionadded:: 1.1b5
                """
def posix_spawn(*args, **kwargs): ...
def posix_spawnp(*args, **kwargs): ...

__imports__: Incomplete
