import gevent
from . import leakcheck as leakcheck, sysinfo as sysinfo
from .testcase import TestCase as TestCase
from _typeshed import Incomplete
from gevent._compat import perf_counter as perf_counter

SMALLEST_RELIABLE_DELAY: float
SMALL_TICK: float
SMALL_TICK_MIN_ADJ = SMALLEST_RELIABLE_DELAY
SMALL_TICK_MAX_ADJ: float
LARGE_TICK: float
LARGE_TICK_MIN_ADJ: Incomplete
LARGE_TICK_MAX_ADJ = SMALL_TICK_MAX_ADJ

class _DelayWaitMixin:
    def wait(self, timeout) -> None: ...
    def test_outer_timeout_is_not_lost(self) -> None: ...

class AbstractGenericWaitTestCase(_DelayWaitMixin, TestCase):
    def test_returns_none_after_timeout(self) -> None: ...

class AbstractGenericGetTestCase(_DelayWaitMixin, TestCase):
    Timeout = gevent.Timeout
    def cleanup(self) -> None: ...
    def test_raises_timeout_number(self) -> None: ...
    def test_raises_timeout_Timeout(self) -> None: ...
    def test_raises_timeout_Timeout_exc_customized(self) -> None: ...
