from _typeshed import Incomplete

__all__ = ['Compiler']

class ExportEntry:
    """
    A simple record for exporting symbols.
    """
    symbol: Incomplete
    signature: Incomplete
    function: Incomplete
    def __init__(self, symbol, signature, function) -> None: ...

class _ModuleCompiler:
    """A base class to compile Python modules to a single shared library or
    extension module.

    :param export_entries: a list of ExportEntry instances.
    :param module_name: the name of the exported module.
    """
    method_def_ty: Incomplete
    method_def_ptr: Incomplete
    env_def_ty: Incomplete
    env_def_ptr: Incomplete
    module_name: Incomplete
    export_python_wrap: bool
    dll_exports: Incomplete
    export_entries: Incomplete
    external_init_function: Incomplete
    use_nrt: Incomplete
    typing_context: Incomplete
    context: Incomplete
    def __init__(self, export_entries, module_name, use_nrt: bool = False, **aot_options) -> None: ...
    def write_llvm_bitcode(self, output, wrap: bool = False, **kws) -> None: ...
    def write_native_object(self, output, wrap: bool = False, **kws) -> None: ...
    def emit_type(self, tyobj): ...
    def emit_header(self, output) -> None: ...

class ModuleCompiler(_ModuleCompiler):
    visitproc_ty: Incomplete
    inquiry_ty: Incomplete
    traverseproc_ty: Incomplete
    freefunc_ty: Incomplete
    m_init_ty: Incomplete
    module_def_base_ty: Incomplete
    module_def_ty: Incomplete
    @property
    def module_create_definition(self):
        """
        Return the signature and name of the Python C API function to
        initialize the module.
        """
    @property
    def module_init_definition(self):
        """
        Return the name and signature of the module's initialization function.
        """

# Names in __all__ with no definition:
#   Compiler
