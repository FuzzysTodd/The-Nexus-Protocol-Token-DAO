import collections
from ..asyn import AsyncFileSystem as AsyncFileSystem
from ..core import filesystem as filesystem, open as open, split_protocol as split_protocol
from ..utils import isfilelike as isfilelike, merge_offset_ranges as merge_offset_ranges, other_paths as other_paths
from _typeshed import Incomplete

logger: Incomplete

class ReferenceNotReachable(RuntimeError):
    reference: Incomplete
    target: Incomplete
    def __init__(self, reference, target, *args) -> None: ...

class RefsValuesView(collections.abc.ValuesView):
    def __iter__(self): ...

class RefsItemsView(collections.abc.ItemsView):
    def __iter__(self): ...

def ravel_multi_index(idx, sizes): ...

class LazyReferenceMapper(collections.abc.MutableMapping):
    """This interface can be used to read/write references from Parquet stores.
    It is not intended for other types of references.
    It can be used with Kerchunk's MultiZarrToZarr method to combine
    references into a parquet store.
    Examples of this use-case can be found here:
    https://fsspec.github.io/kerchunk/advanced.html?highlight=parquet#parquet-storage"""
    @property
    def np(self): ...
    @property
    def pd(self): ...
    root: Incomplete
    chunk_sizes: Incomplete
    dirs: Incomplete
    fs: Incomplete
    record_size: Incomplete
    zmetadata: Incomplete
    url: Incomplete
    out_root: Incomplete
    cat_thresh: Incomplete
    open_refs: Incomplete
    def __init__(self, root, fs: Incomplete | None = None, out_root: Incomplete | None = None, cache_size: int = 128, categorical_threshold: int = 10) -> None:
        """
        Parameters
        ----------
        root : str
            Root of parquet store
        fs : fsspec.AbstractFileSystem
            fsspec filesystem object, default is local filesystem.
        cache_size : int, default=128
            Maximum size of LRU cache, where cache_size*record_size denotes
            the total number of references that can be loaded in memory at once.
        categorical_threshold : int
            Encode urls as pandas.Categorical to reduce memory footprint if the ratio
            of the number of unique urls to total number of refs for each variable
            is greater than or equal to this number. (default 10)


        """
    @staticmethod
    def create(record_size, root, fs, **kwargs): ...
    def listdir(self, basename: bool = True):
        """List top-level directories"""
    def ls(self, path: str = '', detail: bool = True):
        """Shortcut file listings"""
    def values(self): ...
    def items(self): ...
    def __hash__(self): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def write(self, field, record, base_url: Incomplete | None = None, storage_options: Incomplete | None = None) -> None: ...
    def flush(self, base_url: Incomplete | None = None, storage_options: Incomplete | None = None) -> None:
        """Output any modified or deleted keys

        Parameters
        ----------
        base_url: str
            Location of the output
        """
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __contains__(self, item) -> bool: ...

class ReferenceFileSystem(AsyncFileSystem):
    """View byte ranges of some other file as a file system
    Initial version: single file system target, which must support
    async, and must allow start and end args in _cat_file. Later versions
    may allow multiple arbitrary URLs for the targets.
    This FileSystem is read-only. It is designed to be used with async
    targets (for now). This FileSystem only allows whole-file access, no
    ``open``. We do not get original file details from the target FS.
    Configuration is by passing a dict of references at init, or a URL to
    a JSON file containing the same; this dict
    can also contain concrete data for some set of paths.
    Reference dict format:
    {path0: bytes_data, path1: (target_url, offset, size)}
    https://github.com/fsspec/kerchunk/blob/main/README.md
    """
    protocol: str
    target: Incomplete
    template_overrides: Incomplete
    simple_templates: Incomplete
    templates: Incomplete
    fss: Incomplete
    max_gap: Incomplete
    max_block: Incomplete
    references: Incomplete
    def __init__(self, fo, target: Incomplete | None = None, ref_storage_args: Incomplete | None = None, target_protocol: Incomplete | None = None, target_options: Incomplete | None = None, remote_protocol: Incomplete | None = None, remote_options: Incomplete | None = None, fs: Incomplete | None = None, template_overrides: Incomplete | None = None, simple_templates: bool = True, max_gap: int = 64000, max_block: int = 256000000, cache_size: int = 128, **kwargs) -> None:
        """
        Parameters
        ----------
        fo : dict or str
            The set of references to use for this instance, with a structure as above.
            If str referencing a JSON file, will use fsspec.open, in conjunction
            with target_options and target_protocol to open and parse JSON at this
            location. If a directory, then assume references are a set of parquet
            files to be loaded lazily.
        target : str
            For any references having target_url as None, this is the default file
            target to use
        ref_storage_args : dict
            If references is a str, use these kwargs for loading the JSON file.
            Deprecated: use target_options instead.
        target_protocol : str
            Used for loading the reference file, if it is a path. If None, protocol
            will be derived from the given path
        target_options : dict
            Extra FS options for loading the reference file ``fo``, if given as a path
        remote_protocol : str
            The protocol of the filesystem on which the references will be evaluated
            (unless fs is provided). If not given, will be derived from the first
            URL that has a protocol in the templates or in the references, in that
            order.
        remote_options : dict
            kwargs to go with remote_protocol
        fs : AbstractFileSystem | dict(str, (AbstractFileSystem | dict))
            Directly provide a file system(s):
                - a single filesystem instance
                - a dict of protocol:filesystem, where each value is either a filesystem
                  instance, or a dict of kwargs that can be used to create in
                  instance for the given protocol

            If this is given, remote_options and remote_protocol are ignored.
        template_overrides : dict
            Swap out any templates in the references file with these - useful for
            testing.
        simple_templates: bool
            Whether templates can be processed with simple replace (True) or if
            jinja  is needed (False, much slower). All reference sets produced by
            ``kerchunk`` are simple in this sense, but the spec allows for complex.
        max_gap, max_block: int
            For merging multiple concurrent requests to the same remote file.
            Neighboring byte ranges will only be merged when their
            inter-range gap is <= ``max_gap``. Default is 64KB. Set to 0
            to only merge when it requires no extra bytes. Pass a negative
            number to disable merging, appropriate for local target files.
            Neighboring byte ranges will only be merged when the size of
            the aggregated range is <= ``max_block``. Default is 256MB.
        cache_size : int
            Maximum size of LRU cache, where cache_size*record_size denotes
            the total number of references that can be loaded in memory at once.
            Only used for lazily loaded references.
        kwargs : passed to parent class
        """
    def cat_file(self, path, start: Incomplete | None = None, end: Incomplete | None = None, **kwargs): ...
    def pipe_file(self, path, value, **_) -> None:
        """Temporarily add binary data or reference as a file"""
    def get_file(self, rpath, lpath, callback=..., **kwargs): ...
    def get(self, rpath, lpath, recursive: bool = False, **kwargs) -> None: ...
    def cat(self, path, recursive: bool = False, on_error: str = 'raise', **kwargs): ...
    def ls(self, path, detail: bool = True, **kwargs): ...
    def exists(self, path, **kwargs): ...
    def isdir(self, path): ...
    def isfile(self, path): ...
    def find(self, path, maxdepth: Incomplete | None = None, withdirs: bool = False, detail: bool = False, **kwargs): ...
    def info(self, path, **kwargs): ...
    def save_json(self, url, **storage_options) -> None:
        """Write modified references into new location"""
