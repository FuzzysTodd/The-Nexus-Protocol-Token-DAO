from .PyrexTypes import *
from . import MemoryView as MemoryView
from .Errors import error as error
from .Scanning import StringSourceDescriptor as StringSourceDescriptor
from .StringEncoding import EncodedString as EncodedString
from .Symtab import ModuleScope as ModuleScope
from .UtilityCode import CythonUtilityCode as CythonUtilityCode
from _typeshed import Incomplete

class CythonScope(ModuleScope):
    is_cython_builtin: int
    pxd_file_loaded: bool
    context: Incomplete
    def __init__(self, context) -> None: ...
    def is_cpp(self): ...
    def lookup_type(self, name): ...
    def lookup(self, name): ...
    def find_module(self, module_name, pos) -> None: ...
    def find_submodule(self, module_name, as_package: bool = False): ...
    def lookup_qualified_name(self, qname): ...
    def populate_cython_scope(self) -> None: ...
    viewscope: Incomplete
    def load_cythonscope(self) -> None:
        """
        Creates some entries for testing purposes and entries for
        cython.array() and for cython.view.*.
        """

def create_cython_scope(context): ...
def load_testscope_utility(cy_util_name, **kwargs): ...

undecorated_methods_protos: Incomplete
cython_testscope_utility_code: Incomplete
test_cython_utility_dep: Incomplete
cython_test_extclass_utility_code: Incomplete
cythonview_testscope_utility_code: Incomplete
