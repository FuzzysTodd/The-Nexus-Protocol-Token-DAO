from _typeshed import Incomplete

mod_name: str
PYX_EXT: str
PYXDEP_EXT: str
PYXBLD_EXT: str
DEBUG_IMPORT: bool

def get_distutils_extension(modname, pyxfilename, language_level: Incomplete | None = None): ...
def handle_special_build(modname, pyxfilename): ...
def handle_dependencies(pyxfilename) -> None: ...
def build_module(name, pyxfilename, pyxbuild_dir: Incomplete | None = None, inplace: bool = False, language_level: Incomplete | None = None): ...
def load_module(name, pyxfilename, pyxbuild_dir: Incomplete | None = None, is_package: bool = False, build_inplace: bool = False, language_level: Incomplete | None = None, so_path: Incomplete | None = None): ...

class PyxImporter:
    """A meta-path importer for .pyx files.
    """
    extension: Incomplete
    pyxbuild_dir: Incomplete
    inplace: Incomplete
    language_level: Incomplete
    def __init__(self, extension=..., pyxbuild_dir: Incomplete | None = None, inplace: bool = False, language_level: Incomplete | None = None) -> None: ...
    def find_module(self, fullname, package_path: Incomplete | None = None): ...

class PyImporter(PyxImporter):
    """A meta-path importer for normal .py files.
    """
    super: Incomplete
    uncompilable_modules: Incomplete
    blocked_modules: Incomplete
    blocked_packages: Incomplete
    def __init__(self, pyxbuild_dir: Incomplete | None = None, inplace: bool = False, language_level: Incomplete | None = None) -> None: ...
    def find_module(self, fullname, package_path: Incomplete | None = None): ...

class LibLoader:
    def __init__(self) -> None: ...
    def load_module(self, fullname): ...
    def add_lib(self, fullname, path, so_path, is_package) -> None: ...
    def knows(self, fullname): ...

class PyxLoader:
    fullname: Incomplete
    pyxbuild_dir: Incomplete
    inplace: Incomplete
    language_level: Incomplete
    def __init__(self, fullname, path, init_path: Incomplete | None = None, pyxbuild_dir: Incomplete | None = None, inplace: bool = False, language_level: Incomplete | None = None) -> None: ...
    def load_module(self, fullname): ...

class PyxArgs:
    build_dir: bool
    build_in_temp: bool
    setup_args: Incomplete

def install(pyximport: bool = True, pyimport: bool = False, build_dir: Incomplete | None = None, build_in_temp: bool = True, setup_args: Incomplete | None = None, reload_support: bool = False, load_py_module_on_import_failure: bool = False, inplace: bool = False, language_level: Incomplete | None = None):
    """ Main entry point for pyxinstall.

    Call this to install the ``.pyx`` import hook in
    your meta-path for a single Python process.  If you want it to be
    installed whenever you use Python, add it to your ``sitecustomize``
    (as described above).

    :param pyximport: If set to False, does not try to import ``.pyx`` files.

    :param pyimport: You can pass ``pyimport=True`` to also
        install the ``.py`` import hook
        in your meta-path.  Note, however, that it is rather experimental,
        will not work at all for some ``.py`` files and packages, and will
        heavily slow down your imports due to search and compilation.
        Use at your own risk.

    :param build_dir: By default, compiled modules will end up in a ``.pyxbld``
        directory in the user's home directory.  Passing a different path
        as ``build_dir`` will override this.

    :param build_in_temp: If ``False``, will produce the C files locally. Working
        with complex dependencies and debugging becomes more easy. This
        can principally interfere with existing files of the same name.

    :param setup_args: Dict of arguments for Distribution.
        See ``distutils.core.setup()``.

    :param reload_support: Enables support for dynamic
        ``reload(my_module)``, e.g. after a change in the Cython code.
        Additional files ``<so_path>.reloadNN`` may arise on that account, when
        the previously loaded module file cannot be overwritten.

    :param load_py_module_on_import_failure: If the compilation of a ``.py``
        file succeeds, but the subsequent import fails for some reason,
        retry the import with the normal ``.py`` module instead of the
        compiled module.  Note that this may lead to unpredictable results
        for modules that change the system state during their import, as
        the second import will rerun these modifications in whatever state
        the system was left after the import of the compiled module
        failed.

    :param inplace: Install the compiled module
        (``.so`` for Linux and Mac / ``.pyd`` for Windows)
        next to the source file.

    :param language_level: The source language level to use: 2 or 3.
        The default is to use the language level of the current Python
        runtime for .py files and Py2 for ``.pyx`` files.
    """
def uninstall(py_importer, pyx_importer) -> None:
    """
    Uninstall an import hook.
    """
def show_docs() -> None: ...
