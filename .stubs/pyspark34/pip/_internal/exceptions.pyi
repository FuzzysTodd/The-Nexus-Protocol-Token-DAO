import configparser
import pathlib
from _typeshed import Incomplete
from hashlib import _Hash
from pip._internal.metadata import BaseDistribution as BaseDistribution
from pip._internal.req.req_install import InstallRequirement as InstallRequirement
from pip._vendor.requests.models import Request as Request, Response as Response
from pip._vendor.rich.console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult
from pip._vendor.rich.markup import escape as escape
from pip._vendor.rich.text import Text as Text
from typing import Dict, List, Literal

logger: Incomplete

class PipError(Exception):
    """The base pip error."""

class DiagnosticPipError(PipError):
    """An error, that presents diagnostic information to the user.

    This contains a bunch of logic, to enable pretty presentation of our error
    messages. Each error gets a unique reference. Each error can also include
    additional context, a hint and/or a note -- which are presented with the
    main error message in a consistent style.

    This is adapted from the error output styling in `sphinx-theme-builder`.
    """
    reference: str
    kind: Incomplete
    message: Incomplete
    context: Incomplete
    note_stmt: Incomplete
    hint_stmt: Incomplete
    link: Incomplete
    def __init__(self, *, kind: Literal['error', 'warning'] = 'error', reference: str | None = None, message: str | Text, context: str | Text | None, hint_stmt: str | Text | None, note_stmt: str | Text | None = None, link: str | None = None) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class ConfigurationError(PipError):
    """General exception in configuration"""
class InstallationError(PipError):
    """General exception during installation"""
class UninstallationError(PipError):
    """General exception during uninstallation"""

class MissingPyProjectBuildRequires(DiagnosticPipError):
    """Raised when pyproject.toml has `build-system`, but no `build-system.requires`."""
    reference: str
    def __init__(self, *, package: str) -> None: ...

class InvalidPyProjectBuildRequires(DiagnosticPipError):
    """Raised when pyproject.toml an invalid `build-system.requires`."""
    reference: str
    def __init__(self, *, package: str, reason: str) -> None: ...

class NoneMetadataError(PipError):
    '''Raised when accessing a Distribution\'s "METADATA" or "PKG-INFO".

    This signifies an inconsistency, when the Distribution claims to have
    the metadata file (if not, raise ``FileNotFoundError`` instead), but is
    not actually able to produce its content. This may be due to permission
    errors.
    '''
    dist: Incomplete
    metadata_name: Incomplete
    def __init__(self, dist: BaseDistribution, metadata_name: str) -> None:
        '''
        :param dist: A Distribution object.
        :param metadata_name: The name of the metadata being accessed
            (can be "METADATA" or "PKG-INFO").
        '''

class UserInstallationInvalid(InstallationError):
    """A --user install is requested on an environment without user site."""
class InvalidSchemeCombination(InstallationError): ...
class DistributionNotFound(InstallationError):
    """Raised when a distribution cannot be found to satisfy a requirement"""
class RequirementsFileParseError(InstallationError):
    """Raised when a general error occurs parsing a requirements file line."""
class BestVersionAlreadyInstalled(PipError):
    """Raised when the most up-to-date version of a package is already
    installed."""
class BadCommand(PipError):
    """Raised when virtualenv or a command is not found"""
class CommandError(PipError):
    """Raised when there is an error in command-line arguments"""
class PreviousBuildDirError(PipError):
    """Raised when there's a previous conflicting build directory"""

class NetworkConnectionError(PipError):
    """HTTP connection error"""
    response: Incomplete
    request: Incomplete
    error_msg: Incomplete
    def __init__(self, error_msg: str, response: Response | None = None, request: Request | None = None) -> None:
        """
        Initialize NetworkConnectionError with  `request` and `response`
        objects.
        """

class InvalidWheelFilename(InstallationError):
    """Invalid wheel filename."""
class UnsupportedWheel(InstallationError):
    """Unsupported wheel."""

class InvalidWheel(InstallationError):
    """Invalid (e.g. corrupt) wheel."""
    location: Incomplete
    name: Incomplete
    def __init__(self, location: str, name: str) -> None: ...

class MetadataInconsistent(InstallationError):
    """Built metadata contains inconsistent information.

    This is raised when the metadata contains values (e.g. name and version)
    that do not match the information previously obtained from sdist filename,
    user-supplied ``#egg=`` value, or an install requirement name.
    """
    ireq: Incomplete
    field: Incomplete
    f_val: Incomplete
    m_val: Incomplete
    def __init__(self, ireq: InstallRequirement, field: str, f_val: str, m_val: str) -> None: ...

class InstallationSubprocessError(DiagnosticPipError, InstallationError):
    """A subprocess call failed."""
    reference: str
    command_description: Incomplete
    exit_code: Incomplete
    def __init__(self, *, command_description: str, exit_code: int, output_lines: List[str] | None) -> None: ...

class MetadataGenerationFailed(InstallationSubprocessError, InstallationError):
    reference: str
    def __init__(self, *, package_details: str) -> None: ...

class HashErrors(InstallationError):
    """Multiple HashError instances rolled into one for reporting"""
    errors: Incomplete
    def __init__(self) -> None: ...
    def append(self, error: HashError) -> None: ...
    def __bool__(self) -> bool: ...

class HashError(InstallationError):
    """
    A failure to verify a package against known-good hashes

    :cvar order: An int sorting hash exception classes by difficulty of
        recovery (lower being harder), so the user doesn't bother fretting
        about unpinned packages when he has deeper issues, like VCS
        dependencies, to deal with. Also keeps error reports in a
        deterministic order.
    :cvar head: A section heading for display above potentially many
        exceptions of this kind
    :ivar req: The InstallRequirement that triggered this error. This is
        pasted on after the exception is instantiated, because it's not
        typically available earlier.

    """
    req: InstallRequirement | None
    head: str
    order: int
    def body(self) -> str:
        """Return a summary of me for display under the heading.

        This default implementation simply prints a description of the
        triggering requirement.

        :param req: The InstallRequirement that provoked this error, with
            its link already populated by the resolver's _populate_link().

        """

class VcsHashUnsupported(HashError):
    """A hash was provided for a version-control-system-based requirement, but
    we don't have a method for hashing those."""
    order: int
    head: str

class DirectoryUrlHashUnsupported(HashError):
    """A hash was provided for a version-control-system-based requirement, but
    we don't have a method for hashing those."""
    order: int
    head: str

class HashMissing(HashError):
    """A hash was needed for a requirement but is absent."""
    order: int
    head: str
    gotten_hash: Incomplete
    def __init__(self, gotten_hash: str) -> None:
        """
        :param gotten_hash: The hash of the (possibly malicious) archive we
            just downloaded
        """
    def body(self) -> str: ...

class HashUnpinned(HashError):
    """A requirement had a hash specified but was not pinned to a specific
    version."""
    order: int
    head: str

class HashMismatch(HashError):
    """
    Distribution file hash values don't match.

    :ivar package_name: The name of the package that triggered the hash
        mismatch. Feel free to write to this after the exception is raise to
        improve its error message.

    """
    order: int
    head: str
    allowed: Incomplete
    gots: Incomplete
    def __init__(self, allowed: Dict[str, List[str]], gots: Dict[str, '_Hash']) -> None:
        """
        :param allowed: A dict of algorithm names pointing to lists of allowed
            hex digests
        :param gots: A dict of algorithm names pointing to hashes we
            actually got from the files under suspicion
        """
    def body(self) -> str: ...

class UnsupportedPythonVersion(InstallationError):
    """Unsupported python version according to Requires-Python package
    metadata."""

class ConfigurationFileCouldNotBeLoaded(ConfigurationError):
    """When there are errors while loading a configuration file"""
    reason: Incomplete
    fname: Incomplete
    error: Incomplete
    def __init__(self, reason: str = 'could not be loaded', fname: str | None = None, error: configparser.Error | None = None) -> None: ...

class ExternallyManagedEnvironment(DiagnosticPipError):
    """The current environment is externally managed.

    This is raised when the current environment is externally managed, as
    defined by `PEP 668`_. The ``EXTERNALLY-MANAGED`` configuration is checked
    and displayed when the error is bubbled up to the user.

    :param error: The error message read from ``EXTERNALLY-MANAGED``.
    """
    reference: str
    def __init__(self, error: str | None) -> None: ...
    @classmethod
    def from_config(cls, config: pathlib.Path | str) -> ExternallyManagedEnvironment: ...
