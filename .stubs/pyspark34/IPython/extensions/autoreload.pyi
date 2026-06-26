from IPython.core import magic_arguments as magic_arguments
from IPython.core.magic import Magics as Magics, line_magic as line_magic, magics_class as magics_class
from _typeshed import Incomplete

__skip_doctest__: bool

class ModuleReloader:
    enabled: bool
    check_all: bool
    autoload_obj: bool
    failed: Incomplete
    modules: Incomplete
    skip_modules: Incomplete
    old_objects: Incomplete
    modules_mtimes: Incomplete
    shell: Incomplete
    hide_errors: bool
    def __init__(self, shell: Incomplete | None = None) -> None: ...
    def mark_module_skipped(self, module_name) -> None:
        """Skip reloading the named module in the future"""
    def mark_module_reloadable(self, module_name) -> None:
        """Reload the named module in the future (if it is imported)"""
    def aimport_module(self, module_name):
        """Import a module, and mark it reloadable

        Returns
        -------
        top_module : module
            The imported module if it is top-level, or the top-level
        top_name : module
            Name of top_module

        """
    def filename_and_mtime(self, module): ...
    def check(self, check_all: bool = False, do_reload: bool = True) -> None:
        """Check whether some modules need to be reloaded."""

func_attrs: Incomplete

def update_function(old, new) -> None:
    """Upgrade the code object of a function"""
def update_instances(old, new) -> None:
    """Use garbage collector to find all instances that refer to the old
    class definition and update their __class__ to point to the new class
    definition"""
def update_class(old, new) -> None:
    """Replace stuff in the __dict__ of a class, and upgrade
    method code objects, and add new methods, if any"""
def update_property(old, new) -> None:
    """Replace get/set/del functions of a property"""
def isinstance2(a, b, typ): ...

UPDATE_RULES: Incomplete

def update_generic(a, b): ...

class StrongRef:
    obj: Incomplete
    def __init__(self, obj) -> None: ...
    def __call__(self): ...

mod_attrs: Incomplete

def append_obj(module, d, name, obj, autoload: bool = False): ...
def superreload(module, reload=..., old_objects: Incomplete | None = None, shell: Incomplete | None = None):
    """Enhanced version of the builtin reload function.

    superreload remembers objects previously in the module, and

    - upgrades the class dictionary of every old class in the module
    - upgrades the code object of every old function and method
    - clears the module's namespace before reloading

    """

class AutoreloadMagics(Magics):
    loaded_modules: Incomplete
    def __init__(self, *a, **kw) -> None: ...
    def autoreload(self, line: str = '') -> None:
        """%autoreload => Reload modules automatically

        %autoreload or %autoreload now
        Reload all modules (except those excluded by %aimport) automatically
        now.

        %autoreload 0 or %autoreload off
        Disable automatic reloading.

        %autoreload 1 or %autoreload explicit
        Reload only modules imported with %aimport every time before executing
        the Python code typed.

        %autoreload 2 or %autoreload all
        Reload all modules (except those excluded by %aimport) every time
        before executing the Python code typed.

        %autoreload 3 or %autoreload complete
        Same as 2/all, but also but also adds any new objects in the module. See
        unit test at IPython/extensions/tests/test_autoreload.py::test_autoload_newly_added_objects

        The optional arguments --print and --log control display of autoreload activity. The default
        is to act silently; --print (or -p) will print out the names of modules that are being
        reloaded, and --log (or -l) outputs them to the log at INFO level.

        The optional argument --hide-errors hides any errors that can happen when trying to
        reload code.

        Reloading Python modules in a reliable way is in general
        difficult, and unexpected things may occur. %autoreload tries to
        work around common pitfalls by replacing function code objects and
        parts of classes previously in the module with new versions. This
        makes the following things to work:

        - Functions and classes imported via 'from xxx import foo' are upgraded
          to new versions when 'xxx' is reloaded.

        - Methods and properties of classes are upgraded on reload, so that
          calling 'c.foo()' on an object 'c' created before the reload causes
          the new code for 'foo' to be executed.

        Some of the known remaining caveats are:

        - Replacing code objects does not always succeed: changing a @property
          in a class to an ordinary method or a method to a member variable
          can cause problems (but in old objects only).

        - Functions that are removed (eg. via monkey-patching) from a module
          before it is reloaded are not upgraded.

        - C extension modules cannot be reloaded, and so cannot be
          autoreloaded.

        """
    def aimport(self, parameter_s: str = '', stream: Incomplete | None = None) -> None:
        """%aimport => Import modules for automatic reloading.

        %aimport
        List modules to automatically import and not to import.

        %aimport foo
        Import module 'foo' and mark it to be autoreloaded for %autoreload explicit

        %aimport foo, bar
        Import modules 'foo', 'bar' and mark them to be autoreloaded for %autoreload explicit

        %aimport -foo, bar
        Mark module 'foo' to not be autoreloaded for %autoreload explicit, all, or complete, and 'bar'
        to be autoreloaded for mode explicit.
        """
    def pre_run_cell(self) -> None: ...
    def post_execute_hook(self) -> None:
        """Cache the modification times of any modules imported in this execution"""

def load_ipython_extension(ip) -> None:
    """Load the extension in IPython."""
