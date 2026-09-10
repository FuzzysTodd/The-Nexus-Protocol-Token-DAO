from _typeshed import Incomplete
from llvmlite.utils import get_library_name as get_library_name

LLVMContextRef: Incomplete
LLVMModuleRef: Incomplete
LLVMValueRef: Incomplete
LLVMTypeRef: Incomplete
LLVMExecutionEngineRef: Incomplete
LLVMPassManagerBuilderRef: Incomplete
LLVMPassManagerRef: Incomplete
LLVMTargetDataRef: Incomplete
LLVMTargetLibraryInfoRef: Incomplete
LLVMTargetRef: Incomplete
LLVMTargetMachineRef: Incomplete
LLVMMemoryBufferRef: Incomplete
LLVMAttributeListIterator: Incomplete
LLVMElementIterator: Incomplete
LLVMAttributeSetIterator: Incomplete
LLVMGlobalsIterator: Incomplete
LLVMFunctionsIterator: Incomplete
LLVMBlocksIterator: Incomplete
LLVMArgumentsIterator: Incomplete
LLVMInstructionsIterator: Incomplete
LLVMOperandsIterator: Incomplete
LLVMIncomingBlocksIterator: Incomplete
LLVMTypesIterator: Incomplete
LLVMObjectCacheRef: Incomplete
LLVMObjectFileRef: Incomplete
LLVMSectionIteratorRef: Incomplete
LLVMOrcLLJITRef: Incomplete
LLVMOrcDylibTrackerRef: Incomplete

class _LLVMLock:
    """A Lock to guarantee thread-safety for the LLVM C-API.

    This class implements __enter__ and __exit__ for acquiring and releasing
    the lock as a context manager.

    Also, callbacks can be attached so that every time the lock is acquired
    and released the corresponding callbacks will be invoked.
    """
    def __init__(self) -> None: ...
    def register(self, acq_fn, rel_fn) -> None:
        """Register callbacks that are invoked immediately after the lock is
        acquired (``acq_fn()``) and immediately before the lock is released
        (``rel_fn()``).
        """
    def unregister(self, acq_fn, rel_fn) -> None:
        """Remove the registered callbacks.
        """
    def __enter__(self) -> None: ...
    def __exit__(self, *exc_details) -> None: ...

class _suppress_cleanup_errors:
    def __init__(self, context) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None): ...

class _lib_wrapper:
    """Wrap libllvmlite with a lock such that only one thread may access it at
    a time.

    This class duck-types a CDLL.
    """
    def __init__(self) -> None: ...
    def __getattr__(self, name): ...

class _lib_fn_wrapper:
    """Wraps and duck-types a ctypes.CFUNCTYPE to provide
    automatic locking when the wrapped function is called.

    TODO: we can add methods to mark the function as threadsafe
          and remove the locking-step on call when marked.
    """
    def __init__(self, lock, cfn) -> None: ...
    @property
    def argtypes(self): ...
    @argtypes.setter
    def argtypes(self, argtypes) -> None: ...
    @property
    def restype(self): ...
    @restype.setter
    def restype(self, restype) -> None: ...
    def __call__(self, *args, **kwargs): ...

lib: Incomplete

def register_lock_callback(acq_fn, rel_fn) -> None:
    """Register callback functions for lock acquire and release.
    *acq_fn* and *rel_fn* are callables that take no arguments.
    """
def unregister_lock_callback(acq_fn, rel_fn) -> None:
    """Remove the registered callback functions for lock acquire and release.
    The arguments are the same as used in `register_lock_callback()`.
    """

class _DeadPointer:
    """
    Dummy class to make error messages more helpful.
    """

class OutputString:
    """
    Object for managing the char* output of LLVM APIs.
    """
    @classmethod
    def from_return(cls, ptr):
        """Constructing from a pointer returned from the C-API.
        The pointer must be allocated with LLVMPY_CreateString.

        Note
        ----
        Because ctypes auto-converts *restype* of *c_char_p* into a python
        string, we must use *c_void_p* to obtain the raw pointer.
        """
    def __init__(self, owned: bool = True, init: Incomplete | None = None) -> None: ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def __del__(self, _is_shutting_down=...) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__ = __bool__
    @property
    def bytes(self):
        """Get the raw bytes of content of the char pointer.
        """

def ret_string(ptr):
    """To wrap string return-value from C-API.
    """
def ret_bytes(ptr):
    """To wrap bytes return-value from C-API.
    """

class ObjectRef:
    '''
    A wrapper around a ctypes pointer to a LLVM object ("resource").
    '''
    def __init__(self, ptr) -> None: ...
    def close(self) -> None:
        """
        Close this object and do any required clean-up actions.
        """
    def detach(self) -> None:
        """
        Detach the underlying LLVM resource without disposing of it.
        """
    @property
    def closed(self):
        """
        Whether this object has been closed.  A closed object can't
        be used anymore.
        """
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def __del__(self, _is_shutting_down=...) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other): ...
    __nonzero__ = __bool__
    def __hash__(self): ...
