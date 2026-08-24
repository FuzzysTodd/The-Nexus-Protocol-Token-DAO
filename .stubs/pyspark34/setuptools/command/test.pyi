from .._importlib import metadata as metadata
from _typeshed import Incomplete
from collections.abc import Generator
from setuptools import Command as Command
from setuptools.extern.jaraco.functools import pass_none as pass_none
from setuptools.extern.more_itertools import unique_everseen as unique_everseen
from unittest import TestLoader

class ScanningLoader(TestLoader):
    def __init__(self) -> None: ...
    def loadTestsFromModule(self, module, pattern: Incomplete | None = None):
        """Return a suite of all tests cases contained in the given module

        If the module is a package, load tests from all the modules in it.
        If the module has an ``additional_tests`` function, call it and add
        the return value to the tests.
        """

class NonDataProperty:
    fget: Incomplete
    def __init__(self, fget) -> None: ...
    def __get__(self, obj, objtype: Incomplete | None = None): ...

class test(Command):
    """Command to run unit tests after in-place build"""
    description: str
    user_options: Incomplete
    test_suite: Incomplete
    test_module: Incomplete
    test_loader: Incomplete
    test_runner: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def test_args(self): ...
    def with_project_on_sys_path(self, func) -> None:
        """
        Backward compatibility for project_on_sys_path context.
        """
    def project_on_sys_path(self, include_dists=[]) -> Generator[None, None, Incomplete]: ...
    @staticmethod
    def paths_on_pythonpath(paths) -> Generator[None, None, None]:
        """
        Add the indicated paths to the head of the PYTHONPATH environment
        variable so that subprocesses will also see the packages at
        these paths.

        Do this in a context that restores the value on exit.
        """
    @staticmethod
    def install_dists(dist):
        """
        Install the requirements indicated by self.distribution and
        return an iterable of the dists that were built.
        """
    def run(self) -> None: ...
    def run_tests(self) -> None: ...
