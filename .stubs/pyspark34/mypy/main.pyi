import argparse
import os
from _typeshed import Incomplete
from mypy import build as build, defaults as defaults, state as state, util as util
from mypy.config_parser import get_config_module_names as get_config_module_names, parse_config_file as parse_config_file, parse_version as parse_version
from mypy.errorcodes import error_codes as error_codes
from mypy.errors import CompileError as CompileError
from mypy.find_sources import InvalidSourceList as InvalidSourceList, create_source_list as create_source_list
from mypy.fscache import FileSystemCache as FileSystemCache
from mypy.modulefinder import BuildSource as BuildSource, FindModuleCache as FindModuleCache, SearchPaths as SearchPaths, get_search_dirs as get_search_dirs, mypy_path as mypy_path
from mypy.options import BuildType as BuildType, INCOMPLETE_FEATURES as INCOMPLETE_FEATURES, Options as Options
from mypy.split_namespace import SplitNamespace as SplitNamespace
from mypy.version import __version__ as __version__
from typing import Any, IO, NoReturn, Sequence, TextIO
from typing_extensions import Final

orig_stat: Final[Incomplete]
MEM_PROFILE: Final[bool]

def stat_proxy(path: str) -> os.stat_result: ...
def main(*, args: list[str] | None = None, stdout: TextIO = ..., stderr: TextIO = ..., clean_exit: bool = False) -> None:
    """Main entry point to the type checker.

    Args:
        args: Custom command-line arguments.  If not given, sys.argv[1:] will
            be used.
        clean_exit: Don't hard kill the process on exit. This allows catching
            SystemExit.
    """
def run_build(sources: list[BuildSource], options: Options, fscache: FileSystemCache, t0: float, stdout: TextIO, stderr: TextIO) -> tuple[build.BuildResult | None, list[str], bool]: ...
def show_messages(messages: list[str], f: TextIO, formatter: util.FancyFormatter, options: Options) -> None: ...

class AugmentedHelpFormatter(argparse.RawDescriptionHelpFormatter):
    def __init__(self, prog: str) -> None: ...

flag_prefix_pairs: Final[Incomplete]
flag_prefix_map: Final[dict[str, str]]

def invert_flag_name(flag: str) -> str: ...

class PythonExecutableInferenceError(Exception):
    """Represents a failure to infer the version or executable while searching."""

def python_executable_prefix(v: str) -> list[str]: ...
def infer_python_executable(options: Options, special_opts: argparse.Namespace) -> None:
    """Infer the Python executable from the given version.

    This function mutates options based on special_opts to infer the correct Python executable
    to use.
    """

HEADER: Final[str]
DESCRIPTION: Final[str]
FOOTER: Final[str]

class CapturableArgumentParser(argparse.ArgumentParser):
    """Override ArgumentParser methods that use sys.stdout/sys.stderr directly.

    This is needed because hijacking sys.std* is not thread-safe,
    yet output must be captured to properly support mypy.api.run.
    """
    stdout: Incomplete
    stderr: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def print_usage(self, file: IO[str] | None = None) -> None: ...
    def print_help(self, file: IO[str] | None = None) -> None: ...
    def exit(self, status: int = 0, message: str | None = None) -> NoReturn: ...
    def error(self, message: str) -> NoReturn:
        """error(message: string)

        Prints a usage message incorporating the message to stderr and
        exits.

        If you override this in a subclass, it should not return -- it
        should either exit or raise an exception.
        """

class CapturableVersionAction(argparse.Action):
    """Supplement CapturableArgumentParser to handle --version.

    This is nearly identical to argparse._VersionAction except,
    like CapturableArgumentParser, it allows output to be captured.

    Another notable difference is that version is mandatory.
    This allows removing a line in __call__ that falls back to parser.version
    (which does not appear to exist).
    """
    version: Incomplete
    stdout: Incomplete
    def __init__(self, option_strings: Sequence[str], version: str, dest: str = ..., default: str = ..., help: str = "show program's version number and exit", stdout: IO[str] | None = None) -> None: ...
    def __call__(self, parser: argparse.ArgumentParser, namespace: argparse.Namespace, values: str | Sequence[Any] | None, option_string: str | None = None) -> NoReturn: ...

def process_options(args: list[str], stdout: TextIO | None = None, stderr: TextIO | None = None, require_targets: bool = True, server_options: bool = False, fscache: FileSystemCache | None = None, program: str = 'mypy', header: str = ...) -> tuple[list[BuildSource], Options]:
    """Parse command line arguments.

    If a FileSystemCache is passed in, and package_root options are given,
    call fscache.set_package_root() to set the cache's package root.
    """
def process_package_roots(fscache: FileSystemCache | None, parser: argparse.ArgumentParser, options: Options) -> None:
    """Validate and normalize package_root."""
def process_cache_map(parser: argparse.ArgumentParser, special_opts: argparse.Namespace, options: Options) -> None:
    """Validate cache_map and copy into options.cache_map."""
def maybe_write_junit_xml(td: float, serious: bool, messages: list[str], options: Options) -> None: ...
def fail(msg: str, stderr: TextIO, options: Options) -> NoReturn:
    """Fail with a serious error."""
def read_types_packages_to_install(cache_dir: str, after_run: bool) -> list[str]: ...
def install_types(formatter: util.FancyFormatter, options: Options, *, after_run: bool = False, non_interactive: bool = False) -> bool:
    """Install stub packages using pip if some missing stubs were detected."""
