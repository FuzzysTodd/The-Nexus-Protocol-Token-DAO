from . import SkipTest as SkipTest, resources as resources, support as support, util as util
from .patched_tests_setup import disable_tests_in_source as disable_tests_in_source
from .sysinfo import PY3 as PY3
from _typeshed import Incomplete
from collections.abc import Generator
from gevent import monkey as monkey

test_filename: Incomplete

def threading_setup(): ...
def threading_cleanup(*_args) -> None: ...
def wait_threads_exit(timeout: Incomplete | None = None) -> Generator[None, None, None]: ...

test_name: Incomplete
module_file: Incomplete
module_source: Incomplete
temp_handle: Incomplete
temp_path: Incomplete
module_code: Incomplete
