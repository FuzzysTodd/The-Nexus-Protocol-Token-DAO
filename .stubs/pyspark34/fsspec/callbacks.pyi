from _typeshed import Incomplete
from collections.abc import Generator

class Callback:
    """
    Base class and interface for callback mechanism

    This class can be used directly for monitoring file transfers by
    providing ``callback=Callback(hooks=...)`` (see the ``hooks`` argument,
    below), or subclassed for more specialised behaviour.

    Parameters
    ----------
    size: int (optional)
        Nominal quantity for the value that corresponds to a complete
        transfer, e.g., total number of tiles or total number of
        bytes
    value: int (0)
        Starting internal counter value
    hooks: dict or None
        A dict of named functions to be called on each update. The signature
        of these must be ``f(size, value, **kwargs)``
    """
    size: Incomplete
    value: Incomplete
    hooks: Incomplete
    kw: Incomplete
    def __init__(self, size: Incomplete | None = None, value: int = 0, hooks: Incomplete | None = None, **kwargs) -> None: ...
    def set_size(self, size) -> None:
        """
        Set the internal maximum size attribute

        Usually called if not initially set at instantiation. Note that this
        triggers a ``call()``.

        Parameters
        ----------
        size: int
        """
    def absolute_update(self, value) -> None:
        """
        Set the internal value state

        Triggers ``call()``

        Parameters
        ----------
        value: int
        """
    def relative_update(self, inc: int = 1) -> None:
        """
        Delta increment the internal counter

        Triggers ``call()``

        Parameters
        ----------
        inc: int
        """
    def call(self, hook_name: Incomplete | None = None, **kwargs):
        """
        Execute hook(s) with current state

        Each function is passed the internal size and current value

        Parameters
        ----------
        hook_name: str or None
            If given, execute on this hook
        kwargs: passed on to (all) hook(s)
        """
    def wrap(self, iterable) -> Generator[Incomplete, None, None]:
        """
        Wrap an iterable to call ``relative_update`` on each iterations

        Parameters
        ----------
        iterable: Iterable
            The iterable that is being wrapped
        """
    def branch(self, path_1, path_2, kwargs) -> None:
        """
        Set callbacks for child transfers

        If this callback is operating at a higher level, e.g., put, which may
        trigger transfers that can also be monitored. The passed kwargs are
        to be *mutated* to add ``callback=``, if this class supports branching
        to children.

        Parameters
        ----------
        path_1: str
            Child's source path
        path_2: str
            Child's destination path
        kwargs: dict
            arguments passed to child method, e.g., put_file.

        Returns
        -------

        """
    def no_op(self, *_, **__) -> None: ...
    def __getattr__(self, item):
        """
        If undefined methods are called on this class, nothing happens
        """
    @classmethod
    def as_callback(cls, maybe_callback: Incomplete | None = None):
        """Transform callback=... into Callback instance

        For the special value of ``None``, return the global instance of
        ``NoOpCallback``. This is an alternative to including
        ``callback=_DEFAULT_CALLBACK`` directly in a method signature.
        """

class NoOpCallback(Callback):
    """
    This implementation of Callback does exactly nothing
    """
    def call(self, *args, **kwargs) -> None: ...

class DotPrinterCallback(Callback):
    '''
    Simple example Callback implementation

    Almost identical to Callback with a hook that prints a char; here we
    demonstrate how the outer layer may print "#" and the inner layer "."
    '''
    chr: Incomplete
    def __init__(self, chr_to_print: str = '#', **kwargs) -> None: ...
    def branch(self, path_1, path_2, kwargs) -> None:
        """Mutate kwargs to add new instance with different print char"""
    def call(self, **kwargs) -> None:
        """Just outputs a character"""

class TqdmCallback(Callback):
    '''
    A callback to display a progress bar using tqdm

    Parameters
    ----------
    tqdm_kwargs : dict, (optional)
        Any argument accepted by the tqdm constructor.
        See the `tqdm doc <https://tqdm.github.io/docs/tqdm/#__init__>`_.
        Will be forwarded to tqdm.

    Examples
    --------
    >>> import fsspec
    >>> from fsspec.callbacks import TqdmCallback
    >>> fs = fsspec.filesystem("memory")
    >>> path2distant_data = "/your-path"
    >>> fs.upload(
            ".",
            path2distant_data,
            recursive=True,
            callback=TqdmCallback(),
        )

    You can forward args to tqdm using the ``tqdm_kwargs`` parameter.

    >>> fs.upload(
            ".",
            path2distant_data,
            recursive=True,
            callback=TqdmCallback(tqdm_kwargs={"desc": "Your tqdm description"}),
        )
    '''
    def __init__(self, tqdm_kwargs: Incomplete | None = None, *args, **kwargs) -> None: ...
    tqdm: Incomplete
    def set_size(self, size) -> None: ...
    def relative_update(self, inc: int = 1) -> None: ...
    def __del__(self) -> None: ...
