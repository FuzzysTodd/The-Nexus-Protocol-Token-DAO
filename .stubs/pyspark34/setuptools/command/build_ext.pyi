from Cython.Distutils.build_ext import build_ext as _build_ext
from _typeshed import Incomplete
from setuptools.errors import BaseError as BaseError
from setuptools.extension import Extension as Extension, Library as Library
from typing import Dict, List

have_rtld: bool
use_stubs: bool
libtype: str

def if_dl(s): ...
def get_abi3_suffix():
    """Return the file extension for an abi3-compliant Extension()"""

class build_ext(_build_ext):
    editable_mode: bool
    inplace: bool
    def run(self) -> None:
        """Build extensions in build directory, then copy if --inplace"""
    def copy_extensions_to_source(self) -> None: ...
    def get_ext_filename(self, fullname): ...
    shlib_compiler: Incomplete
    shlibs: Incomplete
    ext_map: Incomplete
    def initialize_options(self) -> None: ...
    extensions: Incomplete
    def finalize_options(self) -> None: ...
    def setup_shlib_compiler(self) -> None: ...
    def get_export_symbols(self, ext): ...
    compiler: Incomplete
    def build_extension(self, ext) -> None: ...
    def links_to_dynamic(self, ext):
        """Return true if 'ext' links to a dynamic lib in the same package"""
    def get_source_files(self) -> List[str]: ...
    def get_outputs(self) -> List[str]: ...
    def get_output_mapping(self) -> Dict[str, str]:
        """See :class:`setuptools.commands.build.SubCommand`"""
    def write_stub(self, output_dir, ext, compile: bool = False) -> None: ...

def link_shared_object(self, objects, output_libname, output_dir: Incomplete | None = None, libraries: Incomplete | None = None, library_dirs: Incomplete | None = None, runtime_library_dirs: Incomplete | None = None, export_symbols: Incomplete | None = None, debug: int = 0, extra_preargs: Incomplete | None = None, extra_postargs: Incomplete | None = None, build_temp: Incomplete | None = None, target_lang: Incomplete | None = None) -> None: ...
