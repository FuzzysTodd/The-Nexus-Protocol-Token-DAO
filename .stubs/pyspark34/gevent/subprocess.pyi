from _typeshed import Incomplete
from gevent import monkey as monkey
from gevent._compat import PY311 as PY311, PYPY as PYPY, PathLike as PathLike, fsdecode as fsdecode, fsencode as fsencode, integer_types as integer_types, string_types as string_types, xrange as xrange
from gevent._util import copy_globals as copy_globals
from gevent.event import AsyncResult as AsyncResult
from gevent.greenlet import Greenlet as Greenlet, joinall as joinall
from gevent.hub import getcurrent as getcurrent, linkproxy as linkproxy, sleep as sleep
from gevent.os import fork_and_watch as fork_and_watch
from gevent.timeout import Timeout as _Timeout

spawn: Incomplete
__implements__: Incomplete
PIPE: str
__imports__: Incomplete
__extra__: Incomplete
MAXFD: Incomplete
actually_imported: Incomplete
__imports__ = actually_imported
value: Incomplete
mswindows: Incomplete

class Handle(int):
    closed: bool
    def Close(self) -> None: ...
    def Detach(self): ...
    __del__ = Close

fork: Incomplete

class BrokenPipeError(Exception):
    """Never raised, never caught."""

def call(*popenargs, **kwargs):
    '''
    call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None) -> returncode

    Run command with arguments. Wait for command to complete or
    timeout, then return the returncode attribute.

    The arguments are the same as for the Popen constructor.  Example::

        retcode = call(["ls", "-l"])

    .. versionchanged:: 1.2a1
       The ``timeout`` keyword argument is now accepted on all supported
       versions of Python (not just Python 3) and if it expires will raise a
       :exc:`TimeoutExpired` exception (under Python 2 this is a subclass of :exc:`~.Timeout`).
    '''
def check_call(*popenargs, **kwargs):
    '''
    check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None) -> 0

    Run command with arguments.  Wait for command to complete.  If
    the exit code was zero then return, otherwise raise
    :exc:`CalledProcessError`.  The ``CalledProcessError`` object will have the
    return code in the returncode attribute.

    The arguments are the same as for the Popen constructor.  Example::

        retcode = check_call(["ls", "-l"])
    '''
def check_output(*popenargs, **kwargs):
    '''
    check_output(args, *, input=None, stdin=None, stderr=None, shell=False, universal_newlines=False, timeout=None) -> output

    Run command with arguments and return its output.

    If the exit code was non-zero it raises a :exc:`CalledProcessError`.  The
    ``CalledProcessError`` object will have the return code in the returncode
    attribute and output in the output attribute.


    The arguments are the same as for the Popen constructor.  Example::

        >>> check_output(["ls", "-1", "/dev/null"])
        \'/dev/null\\n\'

    The ``stdout`` argument is not allowed as it is used internally.

    To capture standard error in the result, use ``stderr=STDOUT``::

        >>> output = check_output(["/bin/sh", "-c",
        ...               "ls -l non_existent_file ; exit 0"],
        ...              stderr=STDOUT).decode(\'ascii\').strip()
        >>> print(output.rsplit(\':\', 1)[1].strip())
        No such file or directory

    There is an additional optional argument, "input", allowing you to
    pass a string to the subprocess\'s stdin.  If you use this argument
    you may not also use the Popen constructor\'s "stdin" argument, as
    it too will be used internally.  Example::

        >>> check_output(["sed", "-e", "s/foo/bar/"],
        ...              input=b"when in the course of fooman events\\n")
        \'when in the course of barman events\\n\'

    If ``universal_newlines=True`` is passed, the return value will be a
    string rather than bytes.

    .. versionchanged:: 1.2a1
       The ``timeout`` keyword argument is now accepted on all supported
       versions of Python (not just Python 3) and if it expires will raise a
       :exc:`TimeoutExpired` exception (under Python 2 this is a subclass of :exc:`~.Timeout`).
    .. versionchanged:: 1.2a1
       The ``input`` keyword argument is now accepted on all supported
       versions of Python, not just Python 3
    .. versionchanged:: 22.08.0
       Passing the ``check`` keyword argument is forbidden, just as in Python 3.11.
    '''

class TimeoutExpired(_Timeout):
    """
        This exception is raised when the timeout expires while waiting for
        a child process in `communicate`.

        Under Python 2, this is a gevent extension with the same name as the
        Python 3 class for source-code forward compatibility. However, it extends
        :class:`gevent.timeout.Timeout` for backwards compatibility (because
        we used to just raise a plain ``Timeout``); note that ``Timeout`` is a
        ``BaseException``, *not* an ``Exception``.

        .. versionadded:: 1.2a1
        """
    cmd: Incomplete
    seconds: Incomplete
    output: Incomplete
    def __init__(self, cmd, timeout, output: Incomplete | None = None) -> None: ...
    @property
    def timeout(self): ...

def FileObject(*args, **kwargs): ...

class _CommunicatingGreenlets:
    stdin: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    def __init__(self, popen, input_data) -> None: ...
    def __iter__(self): ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    def __len__(self) -> int: ...

class Popen:
    '''
    The underlying process creation and management in this module is
    handled by the Popen class. It offers a lot of flexibility so that
    developers are able to handle the less common cases not covered by
    the convenience functions.

    .. seealso:: :class:`subprocess.Popen`
       This class should have the same interface as the standard library class.

    .. caution::

       The default values of some arguments, notably ``buffering``, differ
       between Python 2 and Python 3. For the most consistent behaviour across
       versions, it\'s best to explicitly pass the desired values.

    .. caution::

       On Python 2, the ``read`` method of the ``stdout`` and ``stderr`` attributes
       will not be buffered unless buffering is explicitly requested (e.g., `bufsize=-1`).
       This is different than the ``read`` method of the standard library attributes,
       which will buffer internally even if no buffering has been requested. This
       matches the Python 3 behaviour. For portability, please explicitly request
       buffering if you want ``read(n)`` to return all ``n`` bytes, making more than
       one system call if needed. See `issue 1701 <https://github.com/gevent/gevent/issues/1701>`_
       for more context.

    .. versionchanged:: 1.2a1
       Instances can now be used as context managers under Python 2.7. Previously
       this was restricted to Python 3.

    .. versionchanged:: 1.2a1
       Instances now save the ``args`` attribute under Python 2.7. Previously this was
       restricted to Python 3.

    .. versionchanged:: 1.2b1
        Add the ``encoding`` and ``errors`` parameters for Python 3.

    .. versionchanged:: 1.3a1
       Accept "path-like" objects for the *cwd* parameter on all platforms.
       This was added to Python 3.6. Previously with gevent, it only worked
       on POSIX platforms on 3.6.

    .. versionchanged:: 1.3a1
       Add the ``text`` argument as a synonym for ``universal_newlines``,
       as added on Python 3.7.

    .. versionchanged:: 1.3a2
       Allow the same keyword arguments under Python 2 as Python 3:
       ``pass_fds``, ``start_new_session``, ``restore_signals``, ``encoding``
       and ``errors``. Under Python 2, ``encoding`` and ``errors`` are ignored
       because native handling of universal newlines is used.

    .. versionchanged:: 1.3a2
       Under Python 2, ``restore_signals`` defaults to ``False``. Previously it
       defaulted to ``True``, the same as it did in Python 3.

    .. versionchanged:: 20.6.0
       Add the *group*, *extra_groups*, *user*, and *umask* arguments. These
       were added to Python 3.9, but are available in any gevent version, provided
       the underlying platform support is present.

    .. versionchanged:: 20.12.0
       On Python 2 only, if unbuffered binary communication is requested,
       the ``stdin`` attribute of this object will have a ``write`` method that
       actually performs internal buffering and looping, similar to the standard library.
       It guarantees to write all the data given to it in a single call (but internally
       it may make many system calls and/or trips around the event loop to accomplish this).
       See :issue:`1711`.

    .. versionchanged:: 21.12.0
       Added the ``pipesize`` argument for compatibility with Python 3.10.
       This is ignored on all platforms.

    .. versionchanged:: 22.08.0
       Added the ``process_group`` and ``check`` arguments for compatibility with
       Python 3.11.
    '''
    __class_getitem__: Incomplete
    encoding: Incomplete
    errors: Incomplete
    threadpool: Incomplete
    args: Incomplete
    stdin: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    pid: Incomplete
    returncode: Incomplete
    universal_newlines: Incomplete
    result: Incomplete
    def __init__(self, args, bufsize: int = -1, executable: Incomplete | None = None, stdin: Incomplete | None = None, stdout: Incomplete | None = None, stderr: Incomplete | None = None, preexec_fn: Incomplete | None = None, close_fds=..., shell: bool = False, cwd: Incomplete | None = None, env: Incomplete | None = None, universal_newlines: Incomplete | None = None, startupinfo: Incomplete | None = None, creationflags: int = 0, restore_signals: bool = True, start_new_session: bool = False, pass_fds=(), encoding: Incomplete | None = None, errors: Incomplete | None = None, text: Incomplete | None = None, group: Incomplete | None = None, extra_groups: Incomplete | None = None, user: Incomplete | None = None, umask: int = -1, pipesize: int = -1, process_group: Incomplete | None = None, threadpool: Incomplete | None = None) -> None: ...
    def communicate(self, input: Incomplete | None = None, timeout: Incomplete | None = None):
        """
        Interact with process and return its output and error.

        - Send *input* data to stdin.
        - Read data from stdout and stderr, until end-of-file is reached.
        - Wait for process to terminate.

        The optional *input* argument should be a
        string to be sent to the child process, or None, if no data
        should be sent to the child.

        communicate() returns a tuple (stdout, stderr).

        :keyword timeout: Under Python 2, this is a gevent extension; if
           given and it expires, we will raise :exc:`TimeoutExpired`, which
           extends :exc:`gevent.timeout.Timeout` (note that this only extends :exc:`BaseException`,
           *not* :exc:`Exception`)
           Under Python 3, this raises the standard :exc:`TimeoutExpired` exception.

        .. versionchanged:: 1.1a2
           Under Python 2, if the *timeout* elapses, raise the :exc:`gevent.timeout.Timeout`
           exception. Previously, we silently returned.
        .. versionchanged:: 1.1b5
           Honor a *timeout* even if there's no way to communicate with the child
           (stdin, stdout, and stderr are not pipes).
        """
    def poll(self):
        """Check if child process has terminated. Set and return :attr:`returncode` attribute."""
    def __enter__(self): ...
    def __exit__(self, t: type[BaseException] | None, v: BaseException | None, tb: types.TracebackType | None) -> None: ...
    def rawlink(self, callback) -> None: ...
    def wait(self, timeout: Incomplete | None = None, _raise_exc: bool = True):
        """Wait for child process to terminate.  Returns returncode
            attribute."""
    def send_signal(self, sig) -> None:
        """Send a signal to the process
            """
    def terminate(self) -> None:
        """Terminates the process
            """
    kill = terminate
    def rawlink(self, callback) -> None: ...
    def pipe_cloexec(self):
        """Create a pipe with FDs set CLOEXEC."""
    def wait(self, timeout: Incomplete | None = None, _raise_exc: bool = True):
        """
            Wait for child process to terminate.  Returns :attr:`returncode`
            attribute.

            :keyword timeout: The floating point number of seconds to
                wait. Under Python 2, this is a gevent extension, and
                we simply return if it expires. Under Python 3, if
                this time elapses without finishing the process,
                :exc:`TimeoutExpired` is raised.
            """
    def send_signal(self, sig) -> None:
        """Send a signal to the process
            """
    def terminate(self) -> None:
        """Terminate the process with SIGTERM
            """
    def kill(self) -> None:
        """Kill the process with SIGKILL
            """

class CompletedProcess:
    """
    A process that has finished running.

    This is returned by run().

    Attributes:
      - args: The list or str args passed to run().
      - returncode: The exit code of the process, negative for signals.
      - stdout: The standard output (None if not captured).
      - stderr: The standard error (None if not captured).

    .. versionadded:: 1.2a1
       This first appeared in Python 3.5 and is available to all
       Python versions in gevent.
    """
    __class_getitem__: Incomplete
    args: Incomplete
    returncode: Incomplete
    stdout: Incomplete
    stderr: Incomplete
    def __init__(self, args, returncode, stdout: Incomplete | None = None, stderr: Incomplete | None = None) -> None: ...
    def check_returncode(self) -> None:
        """Raise CalledProcessError if the exit code is non-zero."""

def run(*popenargs, **kwargs):
    '''
    run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False) -> CompletedProcess

    Run command with arguments and return a CompletedProcess instance.

    The returned instance will have attributes args, returncode, stdout and
    stderr. By default, stdout and stderr are not captured, and those attributes
    will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them.
    If check is True and the exit code was non-zero, it raises a
    CalledProcessError. The CalledProcessError object will have the return code
    in the returncode attribute, and output & stderr attributes if those streams
    were captured.

    If timeout is given, and the process takes too long, a TimeoutExpired
    exception will be raised.

    There is an optional argument "input", allowing you to
    pass a string to the subprocess\'s stdin.  If you use this argument
    you may not also use the Popen constructor\'s "stdin" argument, as
    it will be used internally.
    The other arguments are the same as for the Popen constructor.
    If universal_newlines=True is passed, the "input" argument must be a
    string and stdout/stderr in the returned object will be strings rather than
    bytes.

    .. versionadded:: 1.2a1
       This function first appeared in Python 3.5. It is available on all Python
       versions gevent supports.

    .. versionchanged:: 1.3a2
       Add the ``capture_output`` argument from Python 3.7. It automatically sets
       ``stdout`` and ``stderr`` to ``PIPE``. It is an error to pass either
       of those arguments along with ``capture_output``.
    '''
