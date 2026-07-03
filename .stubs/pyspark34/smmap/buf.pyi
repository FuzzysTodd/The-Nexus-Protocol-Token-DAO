from _typeshed import Incomplete

__all__ = ['SlidingWindowMapBuffer']

class SlidingWindowMapBuffer:
    """A buffer like object which allows direct byte-wise object and slicing into
    memory of a mapped file. The mapping is controlled by the provided cursor.

    The buffer is relative, that is if you map an offset, index 0 will map to the
    first byte at the offset you used during initialization or begin_access

    **Note:** Although this type effectively hides the fact that there are mapped windows
    underneath, it can unfortunately not be used in any non-pure python method which
    needs a buffer or string"""
    def __init__(self, cursor: Incomplete | None = None, offset: int = 0, size=..., flags: int = 0) -> None:
        """Initalize the instance to operate on the given cursor.
        :param cursor: if not None, the associated cursor to the file you want to access
            If None, you have call begin_access before using the buffer and provide a cursor
        :param offset: absolute offset in bytes
        :param size: the total size of the mapping. Defaults to the maximum possible size
            From that point on, the __len__ of the buffer will be the given size or the file size.
            If the size is larger than the mappable area, you can only access the actually available
            area, although the length of the buffer is reported to be your given size.
            Hence it is in your own interest to provide a proper size !
        :param flags: Additional flags to be passed to os.open
        :raise ValueError: if the buffer could not achieve a valid state"""
    def __del__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i): ...
    def __getslice__(self, i, j): ...
    def begin_access(self, cursor: Incomplete | None = None, offset: int = 0, size=..., flags: int = 0):
        """Call this before the first use of this instance. The method was already
        called by the constructor in case sufficient information was provided.

        For more information no the parameters, see the __init__ method
        :param path: if cursor is None the existing one will be used.
        :return: True if the buffer can be used"""
    def end_access(self) -> None:
        """Call this method once you are done using the instance. It is automatically
        called on destruction, and should be called just in time to allow system
        resources to be freed.

        Once you called end_access, you must call begin access before reusing this instance!"""
    def cursor(self):
        """:return: the currently set cursor which provides access to the data"""
