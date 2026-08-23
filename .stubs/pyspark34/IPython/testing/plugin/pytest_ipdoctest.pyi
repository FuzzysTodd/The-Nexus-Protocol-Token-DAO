import doctest
import os
import pytest
from _pytest._code.code import ExceptionInfo, ReprFileLocation, TerminalRepr
from _pytest._io import TerminalWriter as TerminalWriter
from _pytest.config import Config as Config
from _pytest.config.argparsing import Parser as Parser
from _pytest.nodes import Collector as Collector
from _typeshed import Incomplete
from pathlib import Path
from typing import Any, Dict, Iterable, Sequence, Tuple, Type

DOCTEST_REPORT_CHOICE_NONE: str
DOCTEST_REPORT_CHOICE_CDIFF: str
DOCTEST_REPORT_CHOICE_NDIFF: str
DOCTEST_REPORT_CHOICE_UDIFF: str
DOCTEST_REPORT_CHOICE_ONLY_FIRST_FAILURE: str
DOCTEST_REPORT_CHOICES: Incomplete
RUNNER_CLASS: Incomplete
CHECKER_CLASS: Type['IPDoctestOutputChecker'] | None

def pytest_addoption(parser: Parser) -> None: ...
def pytest_unconfigure() -> None: ...
def pytest_collect_file(file_path: Path, parent: Collector) -> IPDoctestModule | IPDoctestTextfile | None: ...

class ReprFailDoctest(TerminalRepr):
    reprlocation_lines: Incomplete
    def __init__(self, reprlocation_lines: Sequence[Tuple[ReprFileLocation, Sequence[str]]]) -> None: ...
    def toterminal(self, tw: TerminalWriter) -> None: ...

class MultipleDoctestFailures(Exception):
    failures: Incomplete
    def __init__(self, failures: Sequence['doctest.DocTestFailure']) -> None: ...

class IPDoctestItem(pytest.Item):
    runner: Incomplete
    dtest: Incomplete
    obj: Incomplete
    fixture_request: Incomplete
    def __init__(self, name: str, parent: IPDoctestTextfile | IPDoctestModule, runner: IPDocTestRunner | None = None, dtest: doctest.DocTest | None = None) -> None: ...
    @classmethod
    def from_parent(cls, parent: IPDoctestTextfile | IPDoctestModule, *, name: str, runner: IPDocTestRunner, dtest: doctest.DocTest):
        """The public named constructor."""
    def setup(self) -> None: ...
    def teardown(self) -> None: ...
    def runtest(self) -> None: ...
    def repr_failure(self, excinfo: ExceptionInfo[BaseException]) -> str | TerminalRepr: ...
    def reportinfo(self) -> Tuple[os.PathLike[str] | str, int | None, str]: ...
    @property
    def path(self) -> Path: ...

def get_optionflags(parent): ...

class IPDoctestTextfile(pytest.Module):
    obj: Incomplete
    def collect(self) -> Iterable[IPDoctestItem]: ...
    @property
    def path(self) -> Path: ...
    @classmethod
    def from_parent(cls, parent, *, fspath: Incomplete | None = None, path: Path | None = None, **kw): ...

class IPDoctestModule(pytest.Module):
    def collect(self) -> Iterable[IPDoctestItem]: ...
    @property
    def path(self) -> Path: ...
    @classmethod
    def from_parent(cls, parent, *, fspath: Incomplete | None = None, path: Path | None = None, **kw): ...

def ipdoctest_namespace() -> Dict[str, Any]:
    """Fixture that returns a :py:class:`dict` that will be injected into the
    namespace of ipdoctests."""
