import abc
from _typeshed import Incomplete
from argparse import Namespace
from collections.abc import Generator
from sqlalchemy.testing import asyncio as asyncio
from typing import Any

bootstrapped_as_sqlalchemy: bool
log: Incomplete
fixtures: Incomplete
engines: Incomplete
exclusions: Incomplete
warnings: Incomplete
profiling: Incomplete
provision: Incomplete
assertions: Incomplete
requirements: Incomplete
config: Incomplete
testing: Incomplete
util: Incomplete
file_config: Incomplete
include_tags: Incomplete
exclude_tags: Incomplete
options: Namespace

def setup_options(make_option) -> None: ...
def configure_follower(follower_ident) -> None:
    """Configure required state for a follower.

    This invokes in the parent process and typically includes
    database creation.

    """
def memoize_important_follower_config(dict_) -> None:
    """Store important configuration we will need to send to a follower.

    This invokes in the parent process after normal config is set up.

    Hook is currently not used.

    """
def restore_important_follower_config(dict_) -> None:
    """Restore important configuration needed by a follower.

    This invokes in the follower process.

    Hook is currently not used.

    """
def read_config(root_path) -> None: ...
def pre_begin(opt) -> None:
    """things to set up early, before coverage might be setup."""
def set_coverage_flag(value) -> None: ...
def post_begin() -> None:
    """things to set up later, once we know coverage is running."""

pre_configure: Incomplete
post_configure: Incomplete

def pre(fn): ...
def post(fn): ...
def want_class(name, cls): ...
def want_method(cls, fn): ...
def generate_sub_tests(cls, module, markers) -> Generator[Incomplete, None, None]: ...
def start_test_class_outside_fixtures(cls) -> None: ...
def stop_test_class(cls) -> None: ...
def stop_test_class_outside_fixtures(cls) -> None: ...
def final_process_cleanup() -> None: ...
def before_test(test, test_module_name, test_class, test_name) -> None: ...
def after_test(test) -> None: ...
def after_test_fixtures(test) -> None: ...

class FixtureFunctions(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def skip_test_exception(self, *arg, **kw): ...
    @abc.abstractmethod
    def combinations(self, *args, **kw): ...
    @abc.abstractmethod
    def param_ident(self, *args, **kw): ...
    @abc.abstractmethod
    def fixture(self, *arg, **kw): ...
    def get_current_test_name(self) -> None: ...
    @abc.abstractmethod
    def mark_base_test_class(self) -> Any: ...
    @property
    @abc.abstractmethod
    def add_to_marker(self): ...

def set_fixture_functions(fixture_fn_class) -> None: ...
