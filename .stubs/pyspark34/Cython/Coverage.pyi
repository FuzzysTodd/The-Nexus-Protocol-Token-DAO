from . import __version__ as __version__
from .Utils import find_root_package_dir as find_root_package_dir, is_cython_generated_file as is_cython_generated_file, is_package_dir as is_package_dir, open_source_file as open_source_file
from _typeshed import Incomplete
from collections.abc import Generator
from coverage.plugin import CoveragePlugin, FileReporter, FileTracer

C_FILE_EXTENSIONS: Incomplete
MODULE_FILE_EXTENSIONS: Incomplete

class Plugin(CoveragePlugin):
    def sys_info(self): ...
    def configure(self, config) -> None: ...
    def file_tracer(self, filename):
        """
        Try to find a C source file for a file path found by the tracer.
        """
    def file_reporter(self, filename): ...

class CythonModuleTracer(FileTracer):
    """
    Find the Python/Cython source file for a Cython module.
    """
    module_file: Incomplete
    py_file: Incomplete
    c_file: Incomplete
    def __init__(self, module_file, py_file, c_file, c_files_map, file_path_map) -> None: ...
    def has_dynamic_source_filename(self): ...
    def dynamic_source_filename(self, filename, frame):
        """
        Determine source file path.  Called by the function call tracer.
        """

class CythonModuleReporter(FileReporter):
    """
    Provide detailed trace information for one source file to coverage.py.
    """
    name: Incomplete
    c_file: Incomplete
    def __init__(self, c_file, source_file, rel_file_path, code, excluded_lines) -> None: ...
    def lines(self):
        """
        Return set of line numbers that are possibly executable.
        """
    def excluded_lines(self):
        """
        Return set of line numbers that are excluded from coverage.
        """
    def source(self):
        """
        Return the source code of the file as a string.
        """
    def source_token_lines(self) -> Generator[Incomplete, None, None]:
        """
        Iterate over the source code tokens.
        """

def coverage_init(reg, options) -> None: ...
