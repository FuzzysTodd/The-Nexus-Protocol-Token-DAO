from .runtime_spec import DotnetCoreRuntimeSpec as DotnetCoreRuntimeSpec
from pathlib import Path
from typing import Iterator

def find_dotnet_cli() -> Path | None: ...
def find_dotnet_root() -> Path:
    """Try to discover the .NET Core root directory

    If the environment variable ``DOTNET_ROOT`` is defined, we will use that.
    Otherwise, we probe the default installation paths on Windows and macOS.

    If none of these lead to a result, we try to discover the ``dotnet`` CLI
    tool and use its (real) parent directory.

    Otherwise, this function raises an exception.

    :return: Path to the .NET Core root
    """
def find_runtimes_using_cli(dotnet_cli: Path) -> Iterator[DotnetCoreRuntimeSpec]: ...
def find_runtimes_in_root(dotnet_root: Path) -> Iterator[DotnetCoreRuntimeSpec]: ...
def find_runtimes() -> Iterator[DotnetCoreRuntimeSpec]:
    """Find installed .NET Core runtimes

    If the ``dotnet`` CLI can be found, we will call it as ``dotnet
    --list-runtimes`` and parse the result.

    If it is not available, we try to discover the dotnet root directory using
    :py:func:`find_dotnet_root` and enumerate the runtimes installed in the
    ``shared`` subdirectory.

    :return: Iterable of :py:class:`DotnetCoreRuntimeSpec` objects
    """
def find_libmono(*, assembly_dir: str = None, sgen: bool = True) -> Path:
    """Find a suitable libmono dynamic library

    On Windows and macOS, we check the default installation directories.

    :param sgen:
        Whether to look for an SGen or Boehm GC instance. This parameter is
        ignored on Windows, as only ``sgen`` is installed with the default
        installer
    :return:
        Path to usable ``libmono``
    """
