from _typeshed import Incomplete

__all__ = ['patch_all', 'patch_builtins', 'patch_dns', 'patch_os', 'patch_queue', 'patch_select', 'patch_signal', 'patch_socket', 'patch_ssl', 'patch_subprocess', 'patch_sys', 'patch_thread', 'patch_time', 'get_original', 'is_module_patched', 'is_object_patched', 'patch_module', 'main']

class _BadImplements(AttributeError):
    """
    Raised when ``__implements__`` is incorrect.
    """
    def __init__(self, module) -> None: ...

class MonkeyPatchWarning(RuntimeWarning):
    """
    The type of warnings we issue.

    .. versionadded:: 1.3a2
    """

def is_module_patched(mod_name):
    """
    Check if a module has been replaced with a cooperative version.

    :param str mod_name: The name of the standard library module,
        e.g., ``'socket'``.

    """
def is_object_patched(mod_name, item_name):
    """
    Check if an object in a module has been replaced with a
    cooperative version.

    :param str mod_name: The name of the standard library module,
        e.g., ``'socket'``.
    :param str item_name: The name of the attribute in the module,
        e.g., ``'create_connection'``.

    """
def get_original(mod_name, item_name):
    """
    Retrieve the original object from a module.

    If the object has not been patched, then that object will still be
    retrieved.

    :param str mod_name: The name of the standard library module,
        e.g., ``'socket'``. Can also be a sequence of standard library
        modules giving alternate names to try, e.g., ``('thread', '_thread')``;
        the first importable module will supply all *item_name* items.
    :param item_name: A string or sequence of strings naming the
        attribute(s) on the module ``mod_name`` to return.

    :return: The original value if a string was given for
             ``item_name`` or a sequence of original values if a
             sequence was passed.
    """

class _GeventDoPatchRequest:
    get_original: Incomplete
    target_module: Incomplete
    source_module: Incomplete
    items: Incomplete
    patch_kwargs: Incomplete
    def __init__(self, target_module, source_module, items, patch_kwargs) -> None: ...
    def default_patch_items(self) -> None: ...
    def remove_item(self, target_module, *items) -> None: ...

def patch_module(target_module, source_module, items: Incomplete | None = None, _warnings: Incomplete | None = None, _patch_kwargs: Incomplete | None = None, _notify_will_subscribers: bool = True, _notify_did_subscribers: bool = True, _call_hooks: bool = True):
    '''
    patch_module(target_module, source_module, items=None)

    Replace attributes in *target_module* with the attributes of the
    same name in *source_module*.

    The *source_module* can provide some attributes to customize the process:

    * ``__implements__`` is a list of attribute names to copy; if not present,
      the *items* keyword argument is mandatory. ``__implements__`` must only have
      names from the standard library module in it.
    * ``_gevent_will_monkey_patch(target_module, items, warn, **kwargs)``
    * ``_gevent_did_monkey_patch(target_module, items, warn, **kwargs)``
      These two functions in the *source_module* are called *if* they exist,
      before and after copying attributes, respectively. The "will" function
      may modify *items*. The value of *warn* is a function that should be called
      with a single string argument to issue a warning to the user. If the "will"
      function raises :exc:`gevent.events.DoNotPatch`, no patching will be done. These functions
      are called before any event subscribers or plugins.

    :keyword list items: A list of attribute names to replace. If
       not given, this will be taken from the *source_module* ``__implements__``
       attribute.
    :return: A true value if patching was done, a false value if patching was canceled.

    .. versionadded:: 1.3b1
    '''
def patch_sys(stdin: bool = True, stdout: bool = True, stderr: bool = True) -> None:
    """
    Patch sys.std[in,out,err] to use a cooperative IO via a
    threadpool.

    This is relatively dangerous and can have unintended consequences
    such as hanging the process or `misinterpreting control keys`_
    when :func:`input` and :func:`raw_input` are used. :func:`patch_all`
    does *not* call this function by default.

    This method does nothing on Python 3. The Python 3 interpreter
    wants to flush the TextIOWrapper objects that make up
    stderr/stdout at shutdown time, but using a threadpool at that
    time leads to a hang.

    .. _`misinterpreting control keys`: https://github.com/gevent/gevent/issues/274

    .. deprecated:: 23.7.0
       Does nothing on any supported version.
    """
def patch_os() -> None:
    """
    Replace :func:`os.fork` with :func:`gevent.fork`, and, on POSIX,
    :func:`os.waitpid` with :func:`gevent.os.waitpid` (if the
    environment variable ``GEVENT_NOWAITPID`` is not defined). Does
    nothing if fork is not available.

    .. caution:: This method must be used with :func:`patch_signal` to have proper `SIGCHLD`
         handling and thus correct results from ``waitpid``.
         :func:`patch_all` calls both by default.

    .. caution:: For `SIGCHLD` handling to work correctly, the event loop must run.
         The easiest way to help ensure this is to use :func:`patch_all`.
    """
def patch_queue() -> None:
    """
    On Python 3.7 and above, replace :class:`queue.SimpleQueue` (implemented
    in C) with its Python counterpart.

    .. versionadded:: 1.3.5
    """
def patch_time() -> None:
    """
    Replace :func:`time.sleep` with :func:`gevent.sleep`.
    """
def patch_thread(threading: bool = True, _threading_local: bool = True, Event: bool = True, logging: bool = True, existing_locks: bool = True, _warnings: Incomplete | None = None):
    """
    patch_thread(threading=True, _threading_local=True, Event=True, logging=True, existing_locks=True) -> None

    Replace the standard :mod:`thread` module to make it greenlet-based.

    :keyword bool threading: When True (the default),
        also patch :mod:`threading`.
    :keyword bool _threading_local: When True (the default),
        also patch :class:`_threading_local.local`.
    :keyword bool logging: When True (the default), also patch locks
        taken if the logging module has been configured.

    :keyword bool existing_locks: When True (the default), and the
        process is still single threaded, make sure that any
        :class:`threading.RLock` (and, under Python 3, :class:`importlib._bootstrap._ModuleLock`)
        instances that are currently locked can be properly unlocked. **Important**: This is a
        best-effort attempt and, on certain implementations, may not detect all
        locks. It is important to monkey-patch extremely early in the startup process.
        Setting this to False is not recommended, especially on Python 2.

    .. caution::
        Monkey-patching :mod:`thread` and using
        :class:`multiprocessing.Queue` or
        :class:`concurrent.futures.ProcessPoolExecutor` (which uses a
        ``Queue``) will hang the process.

        Monkey-patching with this function and using
        sub-interpreters (and advanced C-level API) and threads may be
        unstable on certain platforms.

    .. versionchanged:: 1.1b1
        Add *logging* and *existing_locks* params.
    .. versionchanged:: 1.3a2
        ``Event`` defaults to True.
    """
def patch_socket(dns: bool = True, aggressive: bool = True) -> None:
    """
    Replace the standard socket object with gevent's cooperative
    sockets.

    :keyword bool dns: When true (the default), also patch address
        resolution functions in :mod:`socket`. See :doc:`/dns` for details.
    """
def patch_dns() -> None:
    """
    Replace :doc:`DNS functions </dns>` in :mod:`socket` with
    cooperative versions.

    This is only useful if :func:`patch_socket` has been called and is
    done automatically by that method if requested.
    """
def patch_ssl(_warnings: Incomplete | None = None, _first_time: bool = True) -> None:
    """
    patch_ssl() -> None

    Replace :class:`ssl.SSLSocket` object and socket wrapping functions in
    :mod:`ssl` with cooperative versions.

    This is only useful if :func:`patch_socket` has been called.
    """
def patch_select(aggressive: bool = True) -> None:
    """
    Replace :func:`select.select` with :func:`gevent.select.select`
    and :func:`select.poll` with :class:`gevent.select.poll` (where available).

    If ``aggressive`` is true (the default), also remove other
    blocking functions from :mod:`select` .

    - :func:`select.epoll`
    - :func:`select.kqueue`
    - :func:`select.kevent`
    - :func:`select.devpoll` (Python 3.5+)
    """
def patch_subprocess() -> None:
    """
    Replace :func:`subprocess.call`, :func:`subprocess.check_call`,
    :func:`subprocess.check_output` and :class:`subprocess.Popen` with
    :mod:`cooperative versions <gevent.subprocess>`.

    .. note::
       On Windows under Python 3, the API support may not completely match
       the standard library.

    """
def patch_builtins() -> None:
    """
    Make the builtin :func:`__import__` function `greenlet safe`_ under Python 2.

    .. note::
       This does nothing under Python 3 as it is not necessary. Python 3 features
       improved import locks that are per-module, not global.

    .. _greenlet safe: https://github.com/gevent/gevent/issues/108

    .. deprecated:: 23.7.0
       Does nothing on any supported platform.
    """
def patch_signal() -> None:
    """
    Make the :func:`signal.signal` function work with a :func:`monkey-patched os <patch_os>`.

    .. caution:: This method must be used with :func:`patch_os` to have proper ``SIGCHLD``
         handling. :func:`patch_all` calls both by default.

    .. caution:: For proper ``SIGCHLD`` handling, you must yield to the event loop.
         Using :func:`patch_all` is the easiest way to ensure this.

    .. seealso:: :mod:`gevent.signal`
    """
def patch_all(socket: bool = True, dns: bool = True, time: bool = True, select: bool = True, thread: bool = True, os: bool = True, ssl: bool = True, subprocess: bool = True, sys: bool = False, aggressive: bool = True, Event: bool = True, builtins: bool = True, signal: bool = True, queue: bool = True, contextvars: bool = True, **kwargs):
    """
    Do all of the default monkey patching (calls every other applicable
    function in this module).

    :return: A true value if patching all modules wasn't cancelled, a false
      value if it was.

    .. versionchanged:: 1.1
       Issue a :mod:`warning <warnings>` if this function is called multiple times
       with different arguments. The second and subsequent calls will only add more
       patches, they can never remove existing patches by setting an argument to ``False``.
    .. versionchanged:: 1.1
       Issue a :mod:`warning <warnings>` if this function is called with ``os=False``
       and ``signal=True``. This will cause SIGCHLD handlers to not be called. This may
       be an error in the future.
    .. versionchanged:: 1.3a2
       ``Event`` defaults to True.
    .. versionchanged:: 1.3b1
       Defined the return values.
    .. versionchanged:: 1.3b1
       Add ``**kwargs`` for the benefit of event subscribers. CAUTION: gevent may add
       and interpret additional arguments in the future, so it is suggested to use prefixes
       for kwarg values to be interpreted by plugins, for example, `patch_all(mylib_futures=True)`.
    .. versionchanged:: 1.3.5
       Add *queue*, defaulting to True, for Python 3.7.
    .. versionchanged:: 1.5
       Remove the ``httplib`` argument. Previously, setting it raised a ``ValueError``.
    .. versionchanged:: 1.5a3
       Add the ``contextvars`` argument.
    .. versionchanged:: 1.5
       Better handling of patching more than once.
    """
def main(): ...
