from IPython.core.compilerop import CachingCompiler
from _typeshed import Incomplete

def murmur2_x86(data, seed):
    """Get the murmur2 hash."""

convert_to_long_pathname: Incomplete

def get_tmp_directory():
    """Get a temp directory."""
def get_tmp_hash_seed():
    """Get a temp hash seed."""
def get_file_name(code):
    """Get a file name."""

class XCachingCompiler(CachingCompiler):
    """A custom caching compiler."""
    log: Incomplete
    def __init__(self, *args, **kwargs) -> None:
        """Initialize the compiler."""
    def get_code_name(self, raw_code, code, number):
        """Get the code name."""
