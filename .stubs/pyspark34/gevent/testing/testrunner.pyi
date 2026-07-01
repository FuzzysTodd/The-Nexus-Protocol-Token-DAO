from . import travis as travis, util as util
from .resources import parse_resources as parse_resources, setup_resources as setup_resources, unparse_resources as unparse_resources
from .sysinfo import OSX as OSX, PY2 as PY2, PYPY as PYPY, RESOLVER_ARES as RESOLVER_ARES, RUNNING_ON_CI as RUNNING_ON_CI, RUN_LEAKCHECKS as RUN_LEAKCHECKS
from _typeshed import Incomplete
from gevent._util import Lazy as Lazy

TIMEOUT: int
AVAIL_NWORKERS: Incomplete
DEFAULT_NWORKERS: Incomplete
DEFAULT_RUN_OPTIONS: Incomplete

class ResultCollector:
    total: int
    failed: Incomplete
    passed: Incomplete
    total_cases: int
    total_skipped: int
    reran: Incomplete
    def __init__(self) -> None: ...
    def __iadd__(self, result): ...
    def __ilshift__(self, result):
        """
        collector <<= result

        Stores the result, but does not count it towards
        the number of cases run, skipped, passed or failed.
        """
    @property
    def longest_running_tests(self):
        """
        A new list of RunResult objects, sorted from longest running
        to shortest running.
        """

class FailFast(Exception): ...

class Runner:
    TIME_WAIT_REAP: float
    TIME_WAIT_SPAWN: float
    results: Incomplete
    def __init__(self, tests, configured_failing_tests=(), failfast: bool = False, quiet: bool = False, configured_run_alone_tests=(), worker_count=..., second_chance: bool = False) -> None:
        """
        :keyword quiet: Set to True or False to explicitly choose. Set to
            `None` to use the default, which may come from the environment variable
            ``GEVENTTEST_QUIET``.
        """
    def __call__(self) -> None: ...

class TravisFoldingRunner:
    def __init__(self, runner, travis_fold_msg) -> None: ...
    def __call__(self): ...

class Discovery:
    package_dir: Incomplete
    package: Incomplete
    config: Incomplete
    ignore: Incomplete
    tests: Incomplete
    configured_test_options: Incomplete
    allow_combine: Incomplete
    def __init__(self, tests: Incomplete | None = None, ignore_files: Incomplete | None = None, ignored=(), coverage: bool = False, package: Incomplete | None = None, config: Incomplete | None = None, allow_combine: bool = True) -> None: ...
    class Discovered:
        orig_dir: Incomplete
        configured_run_alone: Incomplete
        configured_failing_tests: Incomplete
        package: Incomplete
        configured_test_options: Incomplete
        allow_combine: Incomplete
        ignore: Incomplete
        to_import: Incomplete
        std_monkey_patch_files: Incomplete
        no_monkey_patch_files: Incomplete
        commands: Incomplete
        def __init__(self, package, configured_test_options, ignore, config, allow_combine) -> None: ...
        def visit_file(self, filename) -> None: ...
        def visit_files(self, filenames) -> None: ...
    def discovered(self): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

def load_list_from_file(filename, package): ...
def matches(possibilities, command, include_flaky: bool = True): ...
def format_seconds(seconds): ...
def report(result_collector: ResultCollector, exit: bool = True, took: Incomplete | None = None, configured_failing_tests=()): ...
def print_list(lst) -> None: ...
def main() -> None: ...
