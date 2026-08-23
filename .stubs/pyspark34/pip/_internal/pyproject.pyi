from _typeshed import Incomplete
from pip._internal.exceptions import InstallationError as InstallationError, InvalidPyProjectBuildRequires as InvalidPyProjectBuildRequires, MissingPyProjectBuildRequires as MissingPyProjectBuildRequires
from pip._vendor import tomli as tomli
from pip._vendor.packaging.requirements import InvalidRequirement as InvalidRequirement, Requirement as Requirement
from typing import NamedTuple

def make_pyproject_path(unpacked_source_directory: str) -> str: ...

class BuildSystemDetails(NamedTuple):
    requires: Incomplete
    backend: Incomplete
    check: Incomplete
    backend_path: Incomplete

def load_pyproject_toml(use_pep517: bool | None, pyproject_toml: str, setup_py: str, req_name: str) -> BuildSystemDetails | None:
    """Load the pyproject.toml file.

    Parameters:
        use_pep517 - Has the user requested PEP 517 processing? None
                     means the user hasn't explicitly specified.
        pyproject_toml - Location of the project's pyproject.toml file
        setup_py - Location of the project's setup.py file
        req_name - The name of the requirement we're processing (for
                   error reporting)

    Returns:
        None if we should use the legacy code path, otherwise a tuple
        (
            requirements from pyproject.toml,
            name of PEP 517 backend,
            requirements we should check are installed after setting
                up the build environment
            directory paths to import the backend from (backend-path),
                relative to the project root.
        )
    """
