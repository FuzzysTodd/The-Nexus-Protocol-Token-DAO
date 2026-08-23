from ..Compiler import Errors as Errors
from ..Compiler.StringEncoding import EncodedString as EncodedString
from _typeshed import Incomplete

have_lxml: bool

def is_valid_tag(name):
    """
    Names like '.0' are used internally for arguments
    to functions creating generator expressions,
    however they are not identifiers.

    See https://github.com/cython/cython/issues/5552
    """

class CythonDebugWriter:
    """
    Class to output debugging information for cygdb

    It writes debug information to cython_debug/cython_debug_info_<modulename>
    in the build directory.
    """
    output_dir: Incomplete
    tb: Incomplete
    module_name: Incomplete
    def __init__(self, output_dir) -> None: ...
    def start(self, name, attrs: Incomplete | None = None) -> None: ...
    def end(self, name) -> None: ...
    def add_entry(self, name, **attrs) -> None: ...
    def serialize(self) -> None: ...
