from . import flaky as flaky
from .sysinfo import CFFI_BACKEND as CFFI_BACKEND, LIBUV as LIBUV, OSX as OSX, PY310 as PY310, PY311 as PY311, PY312 as PY312, PY38 as PY38, PY39 as PY39, PYPY as PYPY, PYPY3 as PYPY3, RESOLVER_ARES as RESOLVER_ARES, RESOLVER_DNSPYTHON as RESOLVER_DNSPYTHON, RUNNING_ON_CI as RUNNING_ON_CI, RUNNING_ON_MUSLLINUX as RUNNING_ON_MUSLLINUX, RUN_COVERAGE as RUN_COVERAGE, WIN as WIN
from _typeshed import Incomplete

CPYTHON: Incomplete
no_switch_tests: str
ignore_switch_tests: str

def make_re(tests): ...
def get_switch_expected(fullname):
    '''
    >>> get_switch_expected(\'test_patched_select.SelectTestCase.test_error_conditions\')
    False
    >>> get_switch_expected(\'test_patched_socket.GeneralModuleTests.testCrucialConstants\')
    False
    >>> get_switch_expected(\'test_patched_socket.SomeOtherTest.testHello\')
    True
    >>> get_switch_expected("test_patched_httplib.BasicTest.test_bad_status_repr")
    False
    '''

disabled_tests: Incomplete
wrapped_tests: Incomplete

class _PatchedTest:
    def __init__(self, test_fqn) -> None: ...
    def __call__(self, orig_test_fn): ...

def disable_tests_in_source(source, filename): ...
