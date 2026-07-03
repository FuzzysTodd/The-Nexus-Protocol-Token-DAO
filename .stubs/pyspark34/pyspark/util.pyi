import threading
from py4j.java_gateway import JavaObject as JavaObject
from types import TracebackType
from typing import Any, Callable, Iterator, TextIO, Tuple

def print_exec(stream: TextIO) -> None: ...

class VersionUtils:
    """
    Provides utility method to determine Spark versions with given input string.
    """
    @staticmethod
    def majorMinorVersion(sparkVersion: str) -> Tuple[int, int]:
        '''
        Given a Spark version string, return the (major version number, minor version number).
        E.g., for 2.0.1-SNAPSHOT, return (2, 0).

        Examples
        --------
        >>> sparkVersion = "2.4.0"
        >>> VersionUtils.majorMinorVersion(sparkVersion)
        (2, 4)
        >>> sparkVersion = "2.3.0-SNAPSHOT"
        >>> VersionUtils.majorMinorVersion(sparkVersion)
        (2, 3)
        '''

def fail_on_stopiteration(f: Callable) -> Callable:
    """
    Wraps the input function to fail on 'StopIteration' by raising a 'RuntimeError'
    prevents silent loss of data when 'f' is used in a for loop in Spark code
    """
def walk_tb(tb: TracebackType | None) -> Iterator[TracebackType]: ...
def try_simplify_traceback(tb: TracebackType) -> TracebackType | None:
    '''
    Simplify the traceback. It removes the tracebacks in the current package, and only
    shows the traceback that is related to the thirdparty and user-specified codes.

    Returns
    -------
    TracebackType or None
      Simplified traceback instance. It returns None if it fails to simplify.

    Notes
    -----
    This keeps the tracebacks once it sees they are from a different file even
    though the following tracebacks are from the current package.

    Examples
    --------
    >>> import importlib
    >>> import sys
    >>> import traceback
    >>> import tempfile
    >>> with tempfile.TemporaryDirectory() as tmp_dir:
    ...     with open("%s/dummy_module.py" % tmp_dir, "w") as f:
    ...         _ = f.write(
    ...             \'def raise_stop_iteration():\\n\'
    ...             \'    raise StopIteration()\\n\\n\'
    ...             \'def simple_wrapper(f):\\n\'
    ...             \'    def wrapper(*a, **k):\\n\'
    ...             \'        return f(*a, **k)\\n\'
    ...             \'    return wrapper\\n\')
    ...         f.flush()
    ...         spec = importlib.util.spec_from_file_location(
    ...             "dummy_module", "%s/dummy_module.py" % tmp_dir)
    ...         dummy_module = importlib.util.module_from_spec(spec)
    ...         spec.loader.exec_module(dummy_module)
    >>> def skip_doctest_traceback(tb):
    ...     import pyspark
    ...     root = os.path.dirname(pyspark.__file__)
    ...     pairs = zip(walk_tb(tb), traceback.extract_tb(tb))
    ...     for cur_tb, cur_frame in pairs:
    ...         if cur_frame.filename.startswith(root):
    ...             return cur_tb

    Regular exceptions should show the file name of the current package as below.

    >>> exc_info = None
    >>> try:
    ...     fail_on_stopiteration(dummy_module.raise_stop_iteration)()
    ... except Exception as e:
    ...     tb = sys.exc_info()[-1]
    ...     e.__cause__ = None
    ...     exc_info = "".join(
    ...         traceback.format_exception(type(e), e, tb))
    >>> print(exc_info)  # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    Traceback (most recent call last):
      File ...
        ...
      File "/.../pyspark/util.py", line ...
        ...
    RuntimeError: ...
    >>> "pyspark/util.py" in exc_info
    True

    If the traceback is simplified with this method, it hides the current package file name:

    >>> exc_info = None
    >>> try:
    ...     fail_on_stopiteration(dummy_module.raise_stop_iteration)()
    ... except Exception as e:
    ...     tb = try_simplify_traceback(sys.exc_info()[-1])
    ...     e.__cause__ = None
    ...     exc_info = "".join(
    ...         traceback.format_exception(
    ...             type(e), e, try_simplify_traceback(skip_doctest_traceback(tb))))
    >>> print(exc_info)  # doctest: +NORMALIZE_WHITESPACE, +ELLIPSIS
    RuntimeError: ...
    >>> "pyspark/util.py" in exc_info
    False

    In the case below, the traceback contains the current package in the middle.
    In this case, it just hides the top occurrence only.

    >>> exc_info = None
    >>> try:
    ...     fail_on_stopiteration(dummy_module.simple_wrapper(
    ...         fail_on_stopiteration(dummy_module.raise_stop_iteration)))()
    ... except Exception as e:
    ...     tb = sys.exc_info()[-1]
    ...     e.__cause__ = None
    ...     exc_info_a = "".join(
    ...         traceback.format_exception(type(e), e, tb))
    ...     exc_info_b = "".join(
    ...         traceback.format_exception(
    ...             type(e), e, try_simplify_traceback(skip_doctest_traceback(tb))))
    >>> exc_info_a.count("pyspark/util.py")
    2
    >>> exc_info_b.count("pyspark/util.py")
    1
    '''
def inheritable_thread_target(f: Callable) -> Callable:
    """
    Return thread target wrapper which is recommended to be used in PySpark when the
    pinned thread mode is enabled. The wrapper function, before calling original
    thread target, it inherits the inheritable properties specific
    to JVM thread such as ``InheritableThreadLocal``.

    Also, note that pinned thread mode does not close the connection from Python
    to JVM when the thread is finished in the Python side. With this wrapper, Python
    garbage-collects the Python thread instance and also closes the connection
    which finishes JVM thread correctly.

    When the pinned thread mode is off, it return the original ``f``.

    .. versionadded:: 3.2.0

    Parameters
    ----------
    f : function
        the original thread target.

    Notes
    -----
    This API is experimental.

    It is important to know that it captures the local properties when you decorate it
    whereas :class:`InheritableThread` captures when the thread is started.
    Therefore, it is encouraged to decorate it when you want to capture the local
    properties.

    For example, the local properties from the current Spark context is captured
    when you define a function here instead of the invocation:

    >>> @inheritable_thread_target
    ... def target_func():
    ...     pass  # your codes.

    If you have any updates on local properties afterwards, it would not be reflected to
    the Spark context in ``target_func()``.

    The example below mimics the behavior of JVM threads as close as possible:

    >>> Thread(target=inheritable_thread_target(target_func)).start()  # doctest: +SKIP
    """

class InheritableThread(threading.Thread):
    """
    Thread that is recommended to be used in PySpark instead of :class:`threading.Thread`
    when the pinned thread mode is enabled. The usage of this class is exactly same as
    :class:`threading.Thread` but correctly inherits the inheritable properties specific
    to JVM thread such as ``InheritableThreadLocal``.

    Also, note that pinned thread mode does not close the connection from Python
    to JVM when the thread is finished in the Python side. With this class, Python
    garbage-collects the Python thread instance and also closes the connection
    which finishes JVM thread correctly.

    When the pinned thread mode is off, this works as :class:`threading.Thread`.

    .. versionadded:: 3.1.0

    Notes
    -----
    This API is experimental.
    """
    def __init__(self, target: Callable, *args: Any, **kwargs: Any) -> None: ...
    def start(self) -> None: ...
