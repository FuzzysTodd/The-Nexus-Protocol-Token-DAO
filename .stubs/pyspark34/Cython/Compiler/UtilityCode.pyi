from . import Code as Code, Naming as Naming, Symtab as Symtab
from .TreeFragment import StringParseContext as StringParseContext, parse_from_strings as parse_from_strings
from _typeshed import Incomplete

class NonManglingModuleScope(Symtab.ModuleScope):
    prefix: Incomplete
    cython_scope: Incomplete
    cpp: Incomplete
    def __init__(self, prefix, *args, **kw) -> None: ...
    def add_imported_entry(self, name, entry, pos): ...
    def mangle(self, prefix, name: Incomplete | None = None): ...

class CythonUtilityCodeContext(StringParseContext):
    scope: Incomplete
    def find_module(self, module_name, from_module: Incomplete | None = None, pos: Incomplete | None = None, need_pxd: bool = True, absolute_fallback: bool = True, relative_import: bool = False): ...

class CythonUtilityCode(Code.UtilityCodeBase):
    """
    Utility code written in the Cython language itself.

    The @cname decorator can set the cname for a function, method of cdef class.
    Functions decorated with @cname('c_func_name') get the given cname.

    For cdef classes the rules are as follows:
        obj struct      -> <cname>_obj
        obj type ptr    -> <cname>_type
        methods         -> <class_cname>_<method_cname>

    For methods the cname decorator is optional, but without the decorator the
    methods will not be prototyped. See Cython.Compiler.CythonScope and
    tests/run/cythonscope.pyx for examples.
    """
    is_cython_utility: bool
    impl: Incomplete
    name: Incomplete
    file: Incomplete
    prefix: Incomplete
    requires: Incomplete
    from_scope: Incomplete
    outer_module_scope: Incomplete
    compiler_directives: Incomplete
    context_types: Incomplete
    def __init__(self, impl, name: str = '__pyxutil', prefix: str = '', requires: Incomplete | None = None, file: Incomplete | None = None, from_scope: Incomplete | None = None, context: Incomplete | None = None, compiler_directives: Incomplete | None = None, outer_module_scope: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...
    def __hash__(self): ...
    tree: Incomplete
    def get_tree(self, entries_only: bool = False, cython_scope: Incomplete | None = None): ...
    def put_code(self, output) -> None: ...
    @classmethod
    def load_as_string(cls, util_code_name, from_file: Incomplete | None = None, **kwargs):
        """
        Load a utility code as a string. Returns (proto, implementation)
        """
    def declare_in_scope(self, dest_scope, used: bool = False, cython_scope: Incomplete | None = None, allowlist: Incomplete | None = None):
        """
        Declare all entries from the utility code in dest_scope. Code will only
        be included for used entries. If module_name is given, declare the
        type entries with that name.
        """
    @staticmethod
    def filter_inherited_directives(current_directives):
        """
        Cython utility code should usually only pick up a few directives from the
        environment (those that intentionally control its function) and ignore most
        other compiler directives. This function provides a sensible default list
        of directives to copy.
        """

def declare_declarations_in_scope(declaration_string, env, private_type: bool = True, *args, **kwargs) -> None:
    """
    Declare some declarations given as Cython code in declaration_string
    in scope env.
    """
