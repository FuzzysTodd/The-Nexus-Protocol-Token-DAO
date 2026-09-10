from _typeshed import Incomplete
from collections.abc import Generator

VENDORED_ROOT: Incomplete

def list_all(resolve: bool = False):
    """Return the list of vendored projects."""
def project_root(project):
    '''Return the path the root dir of the vendored project.

    If "project" is an empty string then the path prefix for vendored
    projects (e.g. "debugpy/_vendored/") will be returned.
    '''
def iter_project_files(project, relative: bool = False, **kwargs) -> Generator[Incomplete, None, None]:
    """Yield (dirname, basename, filename) for all files in the project."""
def iter_packaging_files(project) -> Generator[Incomplete, None, None]:
    '''Yield the filenames for all files in the project.

    The filenames are relative to "debugpy/_vendored".  This is most
    useful for the "package data" in a setup.py.
    '''
def prefix_matcher(*prefixes):
    """Return a module match func that matches any of the given prefixes."""
def check_modules(project, match, root: Incomplete | None = None):
    """Verify that only vendored modules have been imported."""
def vendored(project, root: Incomplete | None = None) -> Generator[Incomplete, None, None]:
    """A context manager under which the vendored project will be imported."""
def preimport(project, modules, **kwargs) -> None:
    """Import each of the named modules out of the vendored project."""
