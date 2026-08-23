from .utils import sympy_str as sympy_str, sympy_symbol as sympy_symbol
from _typeshed import Incomplete
from torch._inductor.utils import IndentedBuffer as IndentedBuffer
from torch.fx.graph import inplace_methods as inplace_methods, magic_methods as magic_methods

threadlocal: Incomplete

class Virtualized:
    """
    A global variable that redirects via thread local variable

    This allows us to swap in different op implementations in codegen.
    """
    def __init__(self, vname, default) -> None: ...
    def __getattr__(self, name): ...

class NullHandler: ...

class MockHandler:
    def __getattr__(self, name): ...
    @staticmethod
    def masked(mask, body, other): ...
    @staticmethod
    def indirect_indexing(index_var): ...

class KernelFormatterHandler:
    parent_handler: Incomplete
    output: Incomplete
    var_counter: Incomplete
    def __init__(self, parent_handler) -> None: ...
    def __getattr__(self, name): ...
    def getvalue(self, result): ...

class WrapperHandler:
    def __init__(self, inner) -> None: ...
    def __getattr__(self, item): ...

ops: Incomplete

class _V:
    MockHandler = MockHandler
    KernelFormatterHandler = KernelFormatterHandler
    WrapperHandler = WrapperHandler
    set_ops_handler: Incomplete
    get_ops_handler: Incomplete
    set_graph_handler: Incomplete
    set_fake_mode: Incomplete
    set_kernel_handler: Incomplete
    set_debug_handler: Incomplete
    set_interpreter_handler: Incomplete
    @property
    def ops(self) -> MockHandler:
        """The operator handler specific to the current codegen task"""
    @property
    def graph(self):
        """The graph currently being generated"""
    @property
    def fake_mode(self):
        """The graph currently being generated"""
    @property
    def kernel(self):
        """The kernel currently being generated"""
    @property
    def debug(self): ...
    @property
    def interpreter(self): ...

V: Incomplete
