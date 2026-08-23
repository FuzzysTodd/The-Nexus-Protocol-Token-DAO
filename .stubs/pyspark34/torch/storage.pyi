import torch
from _typeshed import Incomplete
from torch.types import Storage as Storage
from typing import TypeVar

HAS_NUMPY: bool
T = TypeVar('T', bound='Union[_StorageBase, TypedStorage]')

class _StorageBase:
    is_sparse: bool
    is_sparse_csr: bool
    device: torch.device
    def __init__(self, *args, **kwargs) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, idx) -> None: ...
    def copy_(self, source: T, non_blocking: bool = None) -> T: ...
    def nbytes(self) -> int: ...
    def size(self) -> int: ...
    def type(self, dtype: str = None, non_blocking: bool = False) -> T: ...
    def cuda(self, device: Incomplete | None = None, non_blocking: bool = False, **kwargs) -> T: ...
    def element_size(self) -> int: ...
    def get_device(self) -> int: ...
    def data_ptr(self) -> int: ...
    @classmethod
    def from_buffer(cls, *args, **kwargs) -> T: ...
    def resize_(self, size: int): ...
    def is_pinned(self) -> bool: ...
    def is_shared(self) -> bool: ...
    @property
    def is_cuda(self) -> None: ...
    @classmethod
    def from_file(cls, filename, shared, nbytes) -> T: ...
    def __iter__(self): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def __reduce__(self): ...
    def __sizeof__(self) -> int: ...
    def clone(self):
        """Returns a copy of this storage"""
    def tolist(self):
        """Returns a list containing the elements of this storage"""
    def cpu(self):
        """Returns a CPU copy of this storage if it's not already on the CPU"""
    def mps(self):
        """Returns a CPU copy of this storage if it's not already on the CPU"""
    def double(self):
        """Casts this storage to double type"""
    def float(self):
        """Casts this storage to float type"""
    def half(self):
        """Casts this storage to half type"""
    def long(self):
        """Casts this storage to long type"""
    def int(self):
        """Casts this storage to int type"""
    def short(self):
        """Casts this storage to short type"""
    def char(self):
        """Casts this storage to char type"""
    def byte(self):
        """Casts this storage to byte type"""
    def bool(self):
        """Casts this storage to bool type"""
    def bfloat16(self):
        """Casts this storage to bfloat16 type"""
    def complex_double(self):
        """Casts this storage to complex double type"""
    def complex_float(self):
        """Casts this storage to complex float type"""
    def pin_memory(self):
        """Copies the storage to pinned memory, if it's not already pinned."""
    def share_memory_(self):
        """Moves the storage to shared memory.

        This is a no-op for storages already in shared memory and for CUDA
        storages, which do not need to be moved for sharing across processes.
        Storages in shared memory cannot be resized.

        Returns: self
        """
    def untyped(self): ...

class UntypedStorage(torch._C.StorageBase, _StorageBase):
    def __getitem__(self, *args, **kwargs): ...
    @property
    def is_cuda(self): ...

class TypedStorage:
    is_sparse: bool
    dtype: torch.dtype
    def fill_(self, value): ...
    def __new__(cls, *args, wrap_storage: Incomplete | None = None, dtype: Incomplete | None = None, device: Incomplete | None = None, _internal: bool = False): ...
    def __init__(self, *args, device: Incomplete | None = None, dtype: Incomplete | None = None, wrap_storage: Incomplete | None = None, _internal: bool = False) -> None: ...
    @property
    def is_cuda(self): ...
    def untyped(self):
        """Returns the internal :class:`torch.UntypedStorage`"""
    def __len__(self) -> int: ...
    def __setitem__(self, idx, value) -> None: ...
    def __getitem__(self, idx): ...
    def copy_(self, source: T, non_blocking: bool = None): ...
    def nbytes(self): ...
    def type(self, dtype: str = None, non_blocking: bool = False) -> T | str: ...
    def cuda(self, device: Incomplete | None = None, non_blocking: bool = False, **kwargs) -> T: ...
    def element_size(self): ...
    def get_device(self) -> int: ...
    def __iter__(self): ...
    def __copy__(self): ...
    def __deepcopy__(self, memo): ...
    def __sizeof__(self) -> int: ...
    def clone(self):
        """Returns a copy of this storage"""
    def tolist(self):
        """Returns a list containing the elements of this storage"""
    def cpu(self):
        """Returns a CPU copy of this storage if it's not already on the CPU"""
    def pin_memory(self):
        """Coppies the  storage to pinned memory, if it's not already pinned."""
    def share_memory_(self):
        """Moves the storage to shared memory.

        This is a no-op for storages already in shared memory and for CUDA
        storages, which do not need to be moved for sharing across processes.
        Storages in shared memory cannot be resized.

        Returns: self
        """
    @property
    def device(self): ...
    def size(self): ...
    def pickle_storage_type(self): ...
    def __reduce__(self): ...
    def data_ptr(self): ...
    def resize_(self, size) -> None: ...
    @classmethod
    def from_buffer(cls, *args, **kwargs): ...
    def double(self):
        """Casts this storage to double type"""
    def float(self):
        """Casts this storage to float type"""
    def half(self):
        """Casts this storage to half type"""
    def long(self):
        """Casts this storage to long type"""
    def int(self):
        """Casts this storage to int type"""
    def short(self):
        """Casts this storage to short type"""
    def char(self):
        """Casts this storage to char type"""
    def byte(self):
        """Casts this storage to byte type"""
    def bool(self):
        """Casts this storage to bool type"""
    def bfloat16(self):
        """Casts this storage to bfloat16 type"""
    def complex_double(self):
        """Casts this storage to complex double type"""
    def complex_float(self):
        """Casts this storage to complex float type"""
    @classmethod
    def from_file(cls, filename, shared, size):
        """
        from_file(filename, shared=False, size=0) -> Storage

        If `shared` is `True`, then memory is shared between all processes.
        All changes are written to the file. If `shared` is `False`, then the changes on
        the storage do not affect the file.

        `size` is the number of elements in the storage. If `shared` is `False`,
        then the file must contain at least `size * sizeof(Type)` bytes
        (`Type` is the type of storage). If `shared` is `True` the file will be
        created if needed.

        Args:
            filename (str): file name to map
            shared (bool): whether to share memory
            size (int): number of elements in the storage
        """
    def is_pinned(self): ...
    def is_shared(self): ...

class _LegacyStorageMeta(type):
    dtype: torch.dtype
    def __instancecheck__(cls, instance): ...

class _LegacyStorage(TypedStorage, metaclass=_LegacyStorageMeta): ...
