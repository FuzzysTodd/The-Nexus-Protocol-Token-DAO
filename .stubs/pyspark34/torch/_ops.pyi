import types
from _typeshed import Incomplete
from abc import ABC
from collections.abc import Generator
from torch._functorch.pyfunctorch import dispatch_functorch as dispatch_functorch

def dl_open_guard() -> Generator[None, None, None]:
    """
    Context manager to set the RTLD_GLOBAL dynamic linker flag while we open a
    shared library to load custom operators.
    """
def has_key(op, k): ...

class PyOperatorABC(ABC):
    def __call__(self, *args, **kwargs) -> None: ...
    def py_impl(self, dispatch_key, fn) -> None: ...
    def name(self) -> None: ...

is_included_in_alias: Incomplete
DispatchKey: Incomplete

def resolve_key(op: PyOperatorABC, k: DispatchKey): ...

pyop_namespace: Incomplete

class PyOperator(PyOperatorABC):
    table: Incomplete
    python_key_mode_table: Incomplete
    functorch_table: Incomplete
    def __init__(self, name) -> None: ...
    def fallthrough(self, dispatch_key) -> None: ...
    def py_impl(self, dispatch_key_or_mode_or_transform): ...
    def dispatch(self, dispatch_key, *args, **kwargs): ...
    def __call__(self, *args, **kwargs): ...
    def name(self): ...

def key_extractor(tensors): ...

class OpOverload(PyOperatorABC):
    py_kernels: Incomplete
    python_key_mode_table: Incomplete
    __module__: Incomplete
    __qualname__: Incomplete
    __annotations__: Incomplete
    is_view: Incomplete
    def __init__(self, overloadpacket, op, op_dk, schema, tags) -> None: ...
    def __deepcopy__(self, memo: Incomplete | None = None): ...
    def __call__(self, *args, **kwargs): ...
    def __hash__(self): ...
    @property
    def namespace(self): ...
    def decompose(self, *args, **kwargs): ...
    def py_impl(self, dispatch_key_or_mode): ...
    def name(self): ...
    @property
    def overloadpacket(self): ...
    @property
    def op(self): ...
    @property
    def tags(self): ...

class OpOverloadPacket:
    def __init__(self, qualified_op_name, op_name, op, overload_names) -> None: ...
    def __deepcopy__(self, memo: Incomplete | None = None): ...
    def __hash__(self): ...
    @property
    def op(self): ...
    def __getattr__(self, key): ...
    def __iter__(self): ...
    def __call__(self, *args, **kwargs): ...
    def overloads(self): ...

class _OpNamespace(types.ModuleType):
    '''
    An op namespace to dynamically bind Operators into Python.

    Say a user has created a custom Operator called "my_namespace::my_op". To
    call this op, the user will write torch.ops.my_namespace.my_op(...).
    At startup, this operation will not yet be bound into Python. Instead, the
    following sequence of magic tricks will occur:
    1. `torch.ops.my_namespace` will invoke the `__getattr__` magic method
       on the `torch.ops` object, which will create a new `_OpNamespace`
       object called `my_namespace` and set it as an attribute on the `ops`
       object.
    2. `torch.ops.my_namespace.my_op` will then invoke `__getattr__` on
       the `my_namespace` object, which will retrieve the operation via
       `torch.get_operation`, a function bound from C++, and then in a similar
       fashion bind this new object onto the `my_namespace` object.
    3. `torch.ops.my_namespace.my_op(...)` then calls this new operation
        and subsequent accesses will incur no further lookup (the namespace and
        operation will already exist).
    '''
    name: Incomplete
    def __init__(self, name) -> None: ...
    def __iter__(self): ...
    def __getattr__(self, op_name): ...

class _PyOpNamespace(_OpNamespace):
    pyop_namespace: Incomplete
    def __init__(self) -> None: ...

class _Ops(types.ModuleType):
    loaded_libraries: Incomplete
    pyops: Incomplete
    def __init__(self) -> None: ...
    def __getattr__(self, name): ...
    def __iter__(self): ...
    def load_library(self, path) -> None:
        """
        Loads a shared library from the given path into the current process.

        The library being loaded may run global initialization code to register
        custom operators with the PyTorch JIT runtime. This allows dynamically
        loading custom operators. For this, you should compile your operator
        and the static registration code into a shared library object, and then
        call ``torch.ops.load_library('path/to/libcustom.so')`` to load the
        shared object.

        After the library is loaded, it is added to the
        ``torch.ops.loaded_libraries`` attribute, a set that may be inspected
        for the paths of all libraries loaded using this function.

        Args:
            path (str): A path to a shared library to load.
        """

ops: Incomplete
