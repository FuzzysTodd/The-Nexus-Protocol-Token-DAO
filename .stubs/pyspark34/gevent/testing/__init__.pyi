import mock
import unittest
from .exception import ExpectedException as ExpectedException
from .flaky import reraiseFlakyTestRaceCondition as reraiseFlakyTestRaceCondition, reraiseFlakyTestTimeout as reraiseFlakyTestTimeout, reraises_flaky_race_condition as reraises_flaky_race_condition, reraises_flaky_timeout as reraises_flaky_timeout
from .hub import QuietHub as QuietHub
from .leakcheck import ignores_leakcheck as ignores_leakcheck
from .modules import walk_modules as walk_modules
from .openfiles import get_number_open_files as get_number_open_files, get_open_files as get_open_files
from .params import DEFAULT_BIND_ADDR as DEFAULT_BIND_ADDR, DEFAULT_BIND_ADDR_TUPLE as DEFAULT_BIND_ADDR_TUPLE, DEFAULT_CONNECT_HOST as DEFAULT_CONNECT_HOST, DEFAULT_LOCAL_HOST_ADDR as DEFAULT_LOCAL_HOST_ADDR, DEFAULT_LOCAL_HOST_ADDR6 as DEFAULT_LOCAL_HOST_ADDR6, DEFAULT_SOCKET_TIMEOUT as DEFAULT_SOCKET_TIMEOUT, DEFAULT_XPC_SOCKET_TIMEOUT as DEFAULT_XPC_SOCKET_TIMEOUT, LARGE_TIMEOUT as LARGE_TIMEOUT
from .skipping import skipIf as skipIf, skipOnAppVeyor as skipOnAppVeyor, skipOnCI as skipOnCI, skipOnLibev as skipOnLibev, skipOnLibuv as skipOnLibuv, skipOnLibuvOnCI as skipOnLibuvOnCI, skipOnLibuvOnCIOnPyPy as skipOnLibuvOnCIOnPyPy, skipOnLibuvOnPyPyOnWin as skipOnLibuvOnPyPyOnWin, skipOnLibuvOnTravisOnCPython27 as skipOnLibuvOnTravisOnCPython27, skipOnLibuvOnWin as skipOnLibuvOnWin, skipOnMacOnCI as skipOnMacOnCI, skipOnManylinux as skipOnManylinux, skipOnPurePython as skipOnPurePython, skipOnPy3 as skipOnPy3, skipOnPy310 as skipOnPy310, skipOnPy312 as skipOnPy312, skipOnPy37 as skipOnPy37, skipOnPyPy as skipOnPyPy, skipOnPyPy3 as skipOnPyPy3, skipOnPyPy3OnCI as skipOnPyPy3OnCI, skipOnPyPyOnCI as skipOnPyPyOnCI, skipOnPyPyOnWindows as skipOnPyPyOnWindows, skipOnWindows as skipOnWindows, skipUnless as skipUnless, skipWithCExtensions as skipWithCExtensions, skipWithoutExternalNetwork as skipWithoutExternalNetwork, skipWithoutResource as skipWithoutResource
from .sockets import bind_and_listen as bind_and_listen, tcp_listener as tcp_listener
from .sysinfo import CFFI_BACKEND as CFFI_BACKEND, CONN_ABORTED_ERRORS as CONN_ABORTED_ERRORS, CPYTHON as CPYTHON, DEBUG as DEBUG, EXPECT_POOR_TIMER_RESOLUTION as EXPECT_POOR_TIMER_RESOLUTION, LIBUV as LIBUV, LINUX as LINUX, NON_APPLICABLE_SUFFIXES as NON_APPLICABLE_SUFFIXES, OSX as OSX, PLATFORM_SPECIFIC_SUFFIXES as PLATFORM_SPECIFIC_SUFFIXES, PY2 as PY2, PY3 as PY3, PY310 as PY310, PY36 as PY36, PY37 as PY37, PY38 as PY38, PY39 as PY39, PYPY as PYPY, PYPY3 as PYPY3, RESOLVER_ARES as RESOLVER_ARES, RESOLVER_DNSPYTHON as RESOLVER_DNSPYTHON, RESOLVER_NOT_SYSTEM as RESOLVER_NOT_SYSTEM, RUNNING_ON_APPVEYOR as RUNNING_ON_APPVEYOR, RUNNING_ON_CI as RUNNING_ON_CI, RUNNING_ON_TRAVIS as RUNNING_ON_TRAVIS, RUN_COVERAGE as RUN_COVERAGE, RUN_LEAKCHECKS as RUN_LEAKCHECKS, SHARED_OBJECT_EXTENSION as SHARED_OBJECT_EXTENSION, VERBOSE as VERBOSE, WIN as WIN, resolver_dnspython_available as resolver_dnspython_available
from .testcase import TestCase as TestCase
from _typeshed import Incomplete
from zope.interface import verify as verify

main: Incomplete
SkipTest = unittest.SkipTest
BaseTestCase = unittest.TestCase

def gc_collect_if_needed() -> None:
    """Collect garbage if necessary for destructors to run"""

class mock:
    @staticmethod
    def patch(reason): ...
mock = mock
