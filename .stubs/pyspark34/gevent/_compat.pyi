from _typeshed import Incomplete
from os import PathLike as PathLike, fsdecode as fsdecode, fsencode as fsencode
from time import get_clock_info, monotonic, perf_counter

PY39: Incomplete
PY311: Incomplete
PY312: Incomplete
PYPY: Incomplete
WIN: Incomplete
LINUX: Incomplete
OSX: Incomplete
MAC: Incomplete
PURE_PYTHON: Incomplete
string_types: Incomplete
integer_types: Incomplete
text_type = str
native_path_types: Incomplete
thread_mod_name: str
hostname_types: Incomplete

def NativeStrIO(): ...
def reraise(t, value, tb: Incomplete | None = None) -> None: ...
def exc_clear() -> None: ...

imp_acquire_lock: Incomplete
imp_release_lock: Incomplete
iteritems: Incomplete
itervalues: Incomplete
xrange = range
izip = zip
perf_counter = perf_counter
monotonic = monotonic
get_clock_info = get_clock_info

def get_this_psutil_process(): ...
