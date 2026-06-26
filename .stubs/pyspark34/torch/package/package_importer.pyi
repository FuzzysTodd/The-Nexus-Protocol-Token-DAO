import torch
import types
from .file_structure_representation import Directory
from .glob_group import GlobPattern
from .importer import Importer
from _typeshed import Incomplete
from collections.abc import Generator
from pathlib import Path
from typing import Any, BinaryIO, Callable, Dict

__all__ = ['PackageImporter']

class PackageImporter(Importer):
    '''Importers allow you to load code written to packages by :class:`PackageExporter`.
    Code is loaded in a hermetic way, using files from the package
    rather than the normal python import system. This allows
    for the packaging of PyTorch model code and data so that it can be run
    on a server or used in the future for transfer learning.

    The importer for packages ensures that code in the module can only be loaded from
    within the package, except for modules explicitly listed as external during export.
    The file ``extern_modules`` in the zip archive lists all the modules that a package externally depends on.
    This prevents "implicit" dependencies where the package runs locally because it is importing
    a locally-installed package, but then fails when the package is copied to another machine.
    '''
    modules: Dict[str, types.ModuleType]
    zip_reader: Incomplete
    filename: str
    root: Incomplete
    extern_modules: Incomplete
    patched_builtins: Incomplete
    storage_context: Incomplete
    last_map_location: Incomplete
    Unpickler: Incomplete
    def __init__(self, file_or_buffer: str | torch._C.PyTorchFileReader | Path | BinaryIO, module_allowed: Callable[[str], bool] = ...) -> None:
        """Open ``file_or_buffer`` for importing. This checks that the imported package only requires modules
        allowed by ``module_allowed``

        Args:
            file_or_buffer: a file-like object (has to implement :meth:`read`, :meth:`readline`, :meth:`tell`, and :meth:`seek`),
                a string, or an ``os.PathLike`` object containing a filename.
            module_allowed (Callable[[str], bool], optional): A method to determine if a externally provided module
                should be allowed. Can be used to ensure packages loaded do not depend on modules that the server
                does not support. Defaults to allowing anything.

        Raises:
            ImportError: If the package will use a disallowed module.
        """
    def import_module(self, name: str, package: Incomplete | None = None):
        """Load a module from the package if it hasn't already been loaded, and then return
        the module. Modules are loaded locally
        to the importer and will appear in ``self.modules`` rather than ``sys.modules``.

        Args:
            name (str): Fully qualified name of the module to load.
            package ([type], optional): Unused, but present to match the signature of importlib.import_module. Defaults to ``None``.

        Returns:
            types.ModuleType: The (possibly already) loaded module.
        """
    def load_binary(self, package: str, resource: str) -> bytes:
        '''Load raw bytes.

        Args:
            package (str): The name of module package (e.g. ``"my_package.my_subpackage"``).
            resource (str): The unique name for the resource.

        Returns:
            bytes: The loaded data.
        '''
    def load_text(self, package: str, resource: str, encoding: str = 'utf-8', errors: str = 'strict') -> str:
        '''Load a string.

        Args:
            package (str): The name of module package (e.g. ``"my_package.my_subpackage"``).
            resource (str): The unique name for the resource.
            encoding (str, optional): Passed to ``decode``. Defaults to ``\'utf-8\'``.
            errors (str, optional): Passed to ``decode``. Defaults to ``\'strict\'``.

        Returns:
            str: The loaded text.
        '''
    def load_pickle(self, package: str, resource: str, map_location: Incomplete | None = None) -> Any:
        '''Unpickles the resource from the package, loading any modules that are needed to construct the objects
        using :meth:`import_module`.

        Args:
            package (str): The name of module package (e.g. ``"my_package.my_subpackage"``).
            resource (str): The unique name for the resource.
            map_location: Passed to `torch.load` to determine how tensors are mapped to devices. Defaults to ``None``.

        Returns:
            Any: The unpickled object.
        '''
    def id(self):
        """
        Returns internal identifier that torch.package uses to distinguish :class:`PackageImporter` instances.
        Looks like::

            <torch_package_0>
        """
    def file_structure(self, *, include: GlobPattern = '**', exclude: GlobPattern = ()) -> Directory:
        '''Returns a file structure representation of package\'s zipfile.

        Args:
            include (Union[List[str], str]): An optional string e.g. ``"my_package.my_subpackage"``, or optional list of strings
                for the names of the files to be included in the zipfile representation. This can also be
                a glob-style pattern, as described in :meth:`PackageExporter.mock`

            exclude (Union[List[str], str]): An optional pattern that excludes files whose name match the pattern.

        Returns:
            :class:`Directory`
        '''
    def python_version(self):
        """Returns the version of python that was used to create this package.

        Note: this function is experimental and not Forward Compatible. The plan is to move this into a lock
        file later on.

        Returns:
            :class:`Optional[str]` a python version e.g. 3.8.9 or None if no version was stored with this package
        """
    def get_source(self, module_name) -> str: ...
    def get_resource_reader(self, fullname): ...
    def __import__(self, name, globals: Incomplete | None = None, locals: Incomplete | None = None, fromlist=(), level: int = 0): ...

class _PathNode: ...

class _PackageNode(_PathNode):
    source_file: Incomplete
    children: Incomplete
    def __init__(self, source_file: str | None) -> None: ...

class _ModuleNode(_PathNode):
    source_file: Incomplete
    def __init__(self, source_file: str) -> None: ...

class _ExternNode(_PathNode): ...

class _PackageResourceReader:
    """Private class used to support PackageImporter.get_resource_reader().

    Confirms to the importlib.abc.ResourceReader interface. Allowed to access
    the innards of PackageImporter.
    """
    importer: Incomplete
    fullname: Incomplete
    def __init__(self, importer, fullname) -> None: ...
    def open_resource(self, resource): ...
    def resource_path(self, resource): ...
    def is_resource(self, name): ...
    def contents(self) -> Generator[Incomplete, None, None]: ...
