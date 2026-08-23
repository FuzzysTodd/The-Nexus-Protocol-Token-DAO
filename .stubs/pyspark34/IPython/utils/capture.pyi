from _typeshed import Incomplete

class RichOutput:
    data: Incomplete
    metadata: Incomplete
    transient: Incomplete
    update: Incomplete
    def __init__(self, data: Incomplete | None = None, metadata: Incomplete | None = None, transient: Incomplete | None = None, update: bool = False) -> None: ...
    def display(self) -> None: ...

class CapturedIO:
    """Simple object for containing captured stdout/err and rich display StringIO objects

    Each instance `c` has three attributes:

    - ``c.stdout`` : standard output as a string
    - ``c.stderr`` : standard error as a string
    - ``c.outputs``: a list of rich display outputs

    Additionally, there's a ``c.show()`` method which will print all of the
    above in the same order, and can be invoked simply via ``c()``.
    """
    def __init__(self, stdout, stderr, outputs: Incomplete | None = None) -> None: ...
    @property
    def stdout(self):
        """Captured standard output"""
    @property
    def stderr(self):
        """Captured standard error"""
    @property
    def outputs(self):
        """A list of the captured rich display outputs, if any.

        If you have a CapturedIO object ``c``, these can be displayed in IPython
        using::

            from IPython.display import display
            for o in c.outputs:
                display(o)
        """
    def show(self) -> None:
        """write my output to sys.stdout/err as appropriate"""
    __call__ = show

class capture_output:
    """context manager for capturing stdout/err"""
    stdout: bool
    stderr: bool
    display: bool
    shell: Incomplete
    def __init__(self, stdout: bool = True, stderr: bool = True, display: bool = True) -> None: ...
    sys_stdout: Incomplete
    sys_stderr: Incomplete
    save_display_pub: Incomplete
    save_display_hook: Incomplete
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
