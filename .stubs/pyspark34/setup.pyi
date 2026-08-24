from _typeshed import Incomplete
from distutils.command.build_ext import build_ext
from typing import Any

kwargs: dict[str, Any]
compile_args: Incomplete

class build_ext_custom(build_ext):
    def get_library_names(self): ...
    library_dirs: Incomplete
    def run(self): ...
