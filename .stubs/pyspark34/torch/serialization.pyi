import torch
from _typeshed import Incomplete
from collections.abc import Generator
from torch.types import Storage
from typing import Any

__all__ = ['SourceChangeWarning', 'mkdtemp', 'register_package', 'check_module_version_greater_or_equal', 'validate_cuda_device', 'location_tag', 'default_restore_location', 'normalize_storage_type', 'storage_to_tensor_type', 'save', 'load', 'StorageType']

class SourceChangeWarning(Warning): ...

def mkdtemp() -> Generator[Incomplete, None, None]: ...
def register_package(priority, tagger, deserializer) -> None: ...
def check_module_version_greater_or_equal(module, req_version_tuple, error_if_malformed: bool = True):
    """
    Check if a module's version satisfies requirements

    Usually, a module's version string will be like 'x.y.z', which would be represented
    as a tuple (x, y, z), but sometimes it could be an unexpected format. If the version
    string does not match the given tuple's format up to the length of the tuple, then
    error and exit or emit a warning.

    Args:
        module: the module to check the version of
        req_version_tuple: tuple (usually of ints) representing the required version
        error_if_malformed: whether we should exit if module version string is malformed

    Returns:
        requirement_is_met: bool
    """
def validate_cuda_device(location): ...
def location_tag(storage: Storage | torch.storage.TypedStorage | torch.UntypedStorage): ...
def default_restore_location(storage, location): ...
def normalize_storage_type(storage_type): ...
def storage_to_tensor_type(storage): ...

class _opener:
    file_like: Incomplete
    def __init__(self, file_like) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...

class _open_file(_opener):
    def __init__(self, name, mode) -> None: ...
    def __exit__(self, *args) -> None: ...

class _open_buffer_reader(_opener):
    def __init__(self, buffer) -> None: ...

class _open_buffer_writer(_opener):
    def __exit__(self, *args) -> None: ...

class _open_zipfile_reader(_opener):
    def __init__(self, name_or_buffer) -> None: ...

class _open_zipfile_writer_file(_opener):
    def __init__(self, name) -> None: ...
    def __exit__(self, *args) -> None: ...

class _open_zipfile_writer_buffer(_opener):
    buffer: Incomplete
    def __init__(self, buffer) -> None: ...
    def __exit__(self, *args) -> None: ...

def save(obj: object, f: FILE_LIKE, pickle_module: Any = ..., pickle_protocol: int = ..., _use_new_zipfile_serialization: bool = True) -> None:
    '''save(obj, f, pickle_module=pickle, pickle_protocol=DEFAULT_PROTOCOL, _use_new_zipfile_serialization=True)

    Saves an object to a disk file.

    See also: :ref:`saving-loading-tensors`

    Args:
        obj: saved object
        f: a file-like object (has to implement write and flush) or a string or
           os.PathLike object containing a file name
        pickle_module: module used for pickling metadata and objects
        pickle_protocol: can be specified to override the default protocol

    .. note::
        A common PyTorch convention is to save tensors using .pt file extension.

    .. note::
        PyTorch preserves storage sharing across serialization. See
        :ref:`preserve-storage-sharing` for more details.

    .. note::
        The 1.6 release of PyTorch switched ``torch.save`` to use a new
        zipfile-based file format. ``torch.load`` still retains the ability to
        load files in the old format. If for any reason you want ``torch.save``
        to use the old format, pass the kwarg ``_use_new_zipfile_serialization=False``.

    Example:
        >>> # xdoctest: +SKIP("makes cwd dirty")
        >>> # Save to file
        >>> x = torch.tensor([0, 1, 2, 3, 4])
        >>> torch.save(x, \'tensor.pt\')
        >>> # Save to io.BytesIO buffer
        >>> buffer = io.BytesIO()
        >>> torch.save(x, buffer)
    '''
def load(f: FILE_LIKE, map_location: MAP_LOCATION = None, pickle_module: Any = None, *, weights_only: bool = False, **pickle_load_args: Any) -> Any:
    '''load(f, map_location=None, pickle_module=pickle, *, weights_only=False, **pickle_load_args)

    Loads an object saved with :func:`torch.save` from a file.

    :func:`torch.load` uses Python\'s unpickling facilities but treats storages,
    which underlie tensors, specially. They are first deserialized on the
    CPU and are then moved to the device they were saved from. If this fails
    (e.g. because the run time system doesn\'t have certain devices), an exception
    is raised. However, storages can be dynamically remapped to an alternative
    set of devices using the :attr:`map_location` argument.

    If :attr:`map_location` is a callable, it will be called once for each serialized
    storage with two arguments: storage and location. The storage argument
    will be the initial deserialization of the storage, residing on the CPU.
    Each serialized storage has a location tag associated with it which
    identifies the device it was saved from, and this tag is the second
    argument passed to :attr:`map_location`. The builtin location tags are ``\'cpu\'``
    for CPU tensors and ``\'cuda:device_id\'`` (e.g. ``\'cuda:2\'``) for CUDA tensors.
    :attr:`map_location` should return either ``None`` or a storage. If
    :attr:`map_location` returns a storage, it will be used as the final deserialized
    object, already moved to the right device. Otherwise, :func:`torch.load` will
    fall back to the default behavior, as if :attr:`map_location` wasn\'t specified.

    If :attr:`map_location` is a :class:`torch.device` object or a string containing
    a device tag, it indicates the location where all tensors should be loaded.

    Otherwise, if :attr:`map_location` is a dict, it will be used to remap location tags
    appearing in the file (keys), to ones that specify where to put the
    storages (values).

    User extensions can register their own location tags and tagging and
    deserialization methods using :func:`torch.serialization.register_package`.

    Args:
        f: a file-like object (has to implement :meth:`read`, :meth:`readline`, :meth:`tell`, and :meth:`seek`),
            or a string or os.PathLike object containing a file name
        map_location: a function, :class:`torch.device`, string or a dict specifying how to remap storage
            locations
        pickle_module: module used for unpickling metadata and objects (has to
            match the :attr:`pickle_module` used to serialize file)
        weights_only: Indicates whether unpickler should be restricted to
            loading only tensors, primitive types and dictionaries
        pickle_load_args: (Python 3 only) optional keyword arguments passed over to
            :func:`pickle_module.load` and :func:`pickle_module.Unpickler`, e.g.,
            :attr:`errors=...`.

    .. warning::
        :func:`torch.load()` unless `weights_only` parameter is set to `True`,
        uses ``pickle`` module implicitly, which is known to be insecure.
        It is possible to construct malicious pickle data which will execute arbitrary code
        during unpickling. Never load data that could have come from an untrusted
        source in an unsafe mode, or that could have been tampered with. **Only load data you trust**.

    .. note::
        When you call :func:`torch.load()` on a file which contains GPU tensors, those tensors
        will be loaded to GPU by default. You can call ``torch.load(.., map_location=\'cpu\')``
        and then :meth:`load_state_dict` to avoid GPU RAM surge when loading a model checkpoint.

    .. note::
        By default, we decode byte strings as ``utf-8``.  This is to avoid a common error
        case ``UnicodeDecodeError: \'ascii\' codec can\'t decode byte 0x...``
        when loading files saved by Python 2 in Python 3.  If this default
        is incorrect, you may use an extra :attr:`encoding` keyword argument to specify how
        these objects should be loaded, e.g., :attr:`encoding=\'latin1\'` decodes them
        to strings using ``latin1`` encoding, and :attr:`encoding=\'bytes\'` keeps them
        as byte arrays which can be decoded later with ``byte_array.decode(...)``.

    Example:
        >>> # xdoctest: +SKIP("undefined filepaths")
        >>> torch.load(\'tensors.pt\')
        # Load all tensors onto the CPU
        >>> torch.load(\'tensors.pt\', map_location=torch.device(\'cpu\'))
        # Load all tensors onto the CPU, using a function
        >>> torch.load(\'tensors.pt\', map_location=lambda storage, loc: storage)
        # Load all tensors onto GPU 1
        >>> torch.load(\'tensors.pt\', map_location=lambda storage, loc: storage.cuda(1))
        # Map tensors from GPU 1 to GPU 0
        >>> torch.load(\'tensors.pt\', map_location={\'cuda:1\': \'cuda:0\'})
        # Load tensor from io.BytesIO object
        >>> with open(\'tensor.pt\', \'rb\') as f:
        ...     buffer = io.BytesIO(f.read())
        >>> torch.load(buffer)
        # Load a module with \'ascii\' encoding for unpickling
        >>> torch.load(\'module.pt\', encoding=\'ascii\')
    '''

class StorageType:
    dtype: Incomplete
    def __init__(self, name) -> None: ...
