import contextlib
from _typeshed import Incomplete
from collections.abc import Generator

def pushd(dir) -> Generator[Incomplete, None, None]:
    """
    >>> tmp_path = getfixture('tmp_path')
    >>> with pushd(tmp_path):
    ...     assert os.getcwd() == os.fspath(tmp_path)
    >>> assert os.getcwd() != os.fspath(tmp_path)
    """
def tarball_context(url, target_dir: Incomplete | None = None, runner: Incomplete | None = None, pushd=...) -> Generator[Incomplete, None, None]:
    """
    Get a tarball, extract it, change to that directory, yield, then
    clean up.
    `runner` is the function to invoke commands.
    `pushd` is a context manager for changing the directory.
    """
def infer_compression(url):
    """
    Given a URL or filename, infer the compression code for tar.

    >>> infer_compression('http://foo/bar.tar.gz')
    'z'
    >>> infer_compression('http://foo/bar.tgz')
    'z'
    >>> infer_compression('file.bz')
    'j'
    >>> infer_compression('file.xz')
    'J'
    """
def temp_dir(remover=...) -> Generator[Incomplete, None, None]:
    """
    Create a temporary directory context. Pass a custom remover
    to override the removal behavior.

    >>> import pathlib
    >>> with temp_dir() as the_dir:
    ...     assert os.path.isdir(the_dir)
    ...     _ = pathlib.Path(the_dir).joinpath('somefile').write_text('contents')
    >>> assert not os.path.exists(the_dir)
    """
def repo_context(url, branch: Incomplete | None = None, quiet: bool = True, dest_ctx=...) -> Generator[Incomplete, None, None]:
    """
    Check out the repo indicated by url.

    If dest_ctx is supplied, it should be a context manager
    to yield the target directory for the check out.
    """
def null() -> Generator[None, None, None]:
    """
    A null context suitable to stand in for a meaningful context.

    >>> with null() as value:
    ...     assert value is None
    """

class ExceptionTrap:
    '''
    A context manager that will catch certain exceptions and provide an
    indication they occurred.

    >>> with ExceptionTrap() as trap:
    ...     raise Exception()
    >>> bool(trap)
    True

    >>> with ExceptionTrap() as trap:
    ...     pass
    >>> bool(trap)
    False

    >>> with ExceptionTrap(ValueError) as trap:
    ...     raise ValueError("1 + 1 is not 3")
    >>> bool(trap)
    True
    >>> trap.value
    ValueError(\'1 + 1 is not 3\')
    >>> trap.tb
    <traceback object at ...>

    >>> with ExceptionTrap(ValueError) as trap:
    ...     raise Exception()
    Traceback (most recent call last):
    ...
    Exception

    >>> bool(trap)
    False
    '''
    exc_info: Incomplete
    exceptions: Incomplete
    def __init__(self, exceptions=...) -> None: ...
    def __enter__(self): ...
    @property
    def type(self): ...
    @property
    def value(self): ...
    @property
    def tb(self): ...
    def __exit__(self, *exc_info): ...
    def __bool__(self) -> bool: ...
    def raises(self, func, *, _test=...):
        """
        Wrap func and replace the result with the truth
        value of the trap (True if an exception occurred).

        First, give the decorator an alias to support Python 3.8
        Syntax.

        >>> raises = ExceptionTrap(ValueError).raises

        Now decorate a function that always fails.

        >>> @raises
        ... def fail():
        ...     raise ValueError('failed')
        >>> fail()
        True
        """
    def passes(self, func):
        """
        Wrap func and replace the result with the truth
        value of the trap (True if no exception).

        First, give the decorator an alias to support Python 3.8
        Syntax.

        >>> passes = ExceptionTrap(ValueError).passes

        Now decorate a function that always fails.

        >>> @passes
        ... def fail():
        ...     raise ValueError('failed')

        >>> fail()
        False
        """

class suppress(contextlib.suppress, contextlib.ContextDecorator):
    """
    A version of contextlib.suppress with decorator support.

    >>> @suppress(KeyError)
    ... def key_error():
    ...     {}['']
    >>> key_error()
    """

class on_interrupt(contextlib.ContextDecorator):
    """
    Replace a KeyboardInterrupt with SystemExit(1)

    >>> def do_interrupt():
    ...     raise KeyboardInterrupt()
    >>> on_interrupt('error')(do_interrupt)()
    Traceback (most recent call last):
    ...
    SystemExit: 1
    >>> on_interrupt('error', code=255)(do_interrupt)()
    Traceback (most recent call last):
    ...
    SystemExit: 255
    >>> on_interrupt('suppress')(do_interrupt)()
    >>> with __import__('pytest').raises(KeyboardInterrupt):
    ...     on_interrupt('ignore')(do_interrupt)()
    """
    action: Incomplete
    code: Incomplete
    def __init__(self, action: str = 'error', code: int = 1) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exctype: type[BaseException] | None, excinst: BaseException | None, exctb: types.TracebackType | None): ...
