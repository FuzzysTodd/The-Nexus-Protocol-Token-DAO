from .util import MapRegion, MapRegionList, MapWindow
from _typeshed import Incomplete

__all__ = ['StaticWindowMapManager', 'SlidingWindowMapManager', 'WindowCursor']

class WindowCursor:
    """
    Pointer into the mapped region of the memory manager, keeping the map
    alive until it is destroyed and no other client uses it.

    Cursors should not be created manually, but are instead returned by the SlidingWindowMapManager

    **Note:**: The current implementation is suited for static and sliding window managers, but it also means
    that it must be suited for the somewhat quite different sliding manager. It could be improved, but
    I see no real need to do so."""
    def __init__(self, manager: Incomplete | None = None, regions: Incomplete | None = None) -> None: ...
    def __del__(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def __copy__(self):
        """copy module interface"""
    def assign(self, rhs) -> None:
        """Assign rhs to this instance. This is required in order to get a real copy.
        Alternativly, you can copy an existing instance using the copy module"""
    def use_region(self, offset: int = 0, size: int = 0, flags: int = 0):
        """Assure we point to a window which allows access to the given offset into the file

        :param offset: absolute offset in bytes into the file
        :param size: amount of bytes to map. If 0, all available bytes will be mapped
        :param flags: additional flags to be given to os.open in case a file handle is initially opened
            for mapping. Has no effect if a region can actually be reused.
        :return: this instance - it should be queried for whether it points to a valid memory region.
            This is not the case if the mapping failed because we reached the end of the file

        **Note:**: The size actually mapped may be smaller than the given size. If that is the case,
        either the file has reached its end, or the map was created between two existing regions"""
    def unuse_region(self) -> None:
        """Unuse the current region. Does nothing if we have no current region

        **Note:** the cursor unuses the region automatically upon destruction. It is recommended
        to un-use the region once you are done reading from it in persistent cursors as it
        helps to free up resource more quickly"""
    def buffer(self):
        """Return a buffer object which allows access to our memory region from our offset
        to the window size. Please note that it might be smaller than you requested when calling use_region()

        **Note:** You can only obtain a buffer if this instance is_valid() !

        **Note:** buffers should not be cached passed the duration of your access as it will
        prevent resources from being freed even though they might not be accounted for anymore !"""
    def map(self):
        """
        :return: the underlying raw memory map. Please not that the offset and size is likely to be different
            to what you set as offset and size. Use it only if you are sure about the region it maps, which is the whole
            file in case of StaticWindowMapManager"""
    def is_valid(self):
        """:return: True if we have a valid and usable region"""
    def is_associated(self):
        """:return: True if we are associated with a specific file already"""
    def ofs_begin(self):
        """:return: offset to the first byte pointed to by our cursor

        **Note:** only if is_valid() is True"""
    def ofs_end(self):
        """:return: offset to one past the last available byte"""
    def size(self):
        """:return: amount of bytes we point to"""
    def region(self):
        """:return: our mapped region, or None if nothing is mapped yet
        :raise AssertionError: if we have no current region. This is only useful for debugging"""
    def includes_ofs(self, ofs):
        """:return: True if the given absolute offset is contained in the cursors
            current region

        **Note:** cursor must be valid for this to work"""
    def file_size(self):
        """:return: size of the underlying file"""
    def path_or_fd(self):
        """:return: path or file descriptor of the underlying mapped file"""
    def path(self):
        """:return: path of the underlying mapped file
        :raise ValueError: if attached path is not a path"""
    def fd(self):
        """:return: file descriptor used to create the underlying mapping.

        **Note:** it is not required to be valid anymore
        :raise ValueError: if the mapping was not created by a file descriptor"""

class StaticWindowMapManager:
    """Provides a manager which will produce single size cursors that are allowed
    to always map the whole file.

    Clients must be written to specifically know that they are accessing their data
    through a StaticWindowMapManager, as they otherwise have to deal with their window size.

    These clients would have to use a SlidingWindowMapBuffer to hide this fact.

    This type will always use a maximum window size, and optimize certain methods to
    accommodate this fact"""
    MapRegionListCls = MapRegionList
    MapWindowCls = MapWindow
    MapRegionCls = MapRegion
    WindowCursorCls = WindowCursor
    def __init__(self, window_size: int = 0, max_memory_size: int = 0, max_open_handles=...) -> None:
        """initialize the manager with the given parameters.
        :param window_size: if -1, a default window size will be chosen depending on
            the operating system's architecture. It will internally be quantified to a multiple of the page size
            If 0, the window may have any size, which basically results in mapping the whole file at one
        :param max_memory_size: maximum amount of memory we may map at once before releasing mapped regions.
            If 0, a viable default will be set depending on the system's architecture.
            It is a soft limit that is tried to be kept, but nothing bad happens if we have to over-allocate
        :param max_open_handles: if not maxint, limit the amount of open file handles to the given number.
            Otherwise the amount is only limited by the system itself. If a system or soft limit is hit,
            the manager will free as many handles as possible"""
    def make_cursor(self, path_or_fd):
        """
        :return: a cursor pointing to the given path or file descriptor.
            It can be used to map new regions of the file into memory

        **Note:** if a file descriptor is given, it is assumed to be open and valid,
        but may be closed afterwards. To refer to the same file, you may reuse
        your existing file descriptor, but keep in mind that new windows can only
        be mapped as long as it stays valid. This is why the using actual file paths
        are preferred unless you plan to keep the file descriptor open.

        **Note:** file descriptors are problematic as they are not necessarily unique, as two
        different files opened and closed in succession might have the same file descriptor id.

        **Note:** Using file descriptors directly is faster once new windows are mapped as it
        prevents the file to be opened again just for the purpose of mapping it."""
    def collect(self):
        """Collect all available free-to-collect mapped regions
        :return: Amount of freed handles"""
    def num_file_handles(self):
        """:return: amount of file handles in use. Each mapped region uses one file handle"""
    def num_open_files(self):
        """Amount of opened files in the system"""
    def window_size(self):
        """:return: size of each window when allocating new regions"""
    def mapped_memory_size(self):
        """:return: amount of bytes currently mapped in total"""
    def max_file_handles(self):
        """:return: maximium amount of handles we may have opened"""
    def max_mapped_memory_size(self):
        """:return: maximum amount of memory we may allocate"""
    def force_map_handle_removal_win(self, base_path):
        """ONLY AVAILABLE ON WINDOWS
        On windows removing files is not allowed if anybody still has it opened.
        If this process is ourselves, and if the whole process uses this memory
        manager (as far as the parent framework is concerned) we can enforce
        closing all memory maps whose path matches the given base path to
        allow the respective operation after all.
        The respective system must NOT access the closed memory regions anymore !
        This really may only be used if you know that the items which keep
        the cursors alive will not be using it anymore. They need to be recreated !
        :return: Amount of closed handles

        **Note:** does nothing on non-windows platforms"""

class SlidingWindowMapManager(StaticWindowMapManager):
    """Maintains a list of ranges of mapped memory regions in one or more files and allows to easily
    obtain additional regions assuring there is no overlap.
    Once a certain memory limit is reached globally, or if there cannot be more open file handles
    which result from each mmap call, the least recently used, and currently unused mapped regions
    are unloaded automatically.

    **Note:** currently not thread-safe !

    **Note:** in the current implementation, we will automatically unload windows if we either cannot
        create more memory maps (as the open file handles limit is hit) or if we have allocated more than
        a safe amount of memory already, which would possibly cause memory allocations to fail as our address
        space is full."""
    def __init__(self, window_size: int = -1, max_memory_size: int = 0, max_open_handles=...) -> None:
        """Adjusts the default window size to -1"""
