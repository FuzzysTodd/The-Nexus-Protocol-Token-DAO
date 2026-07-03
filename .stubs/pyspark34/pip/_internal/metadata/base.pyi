import email.message
import pathlib
import zipfile
from ._json import msg_to_json as msg_to_json
from _typeshed import Incomplete
from pip._internal.exceptions import NoneMetadataError as NoneMetadataError
from pip._internal.locations import site_packages as site_packages, user_site as user_site
from pip._internal.models.direct_url import DIRECT_URL_METADATA_NAME as DIRECT_URL_METADATA_NAME, DirectUrl as DirectUrl, DirectUrlValidationError as DirectUrlValidationError
from pip._internal.utils.compat import stdlib_pkgs as stdlib_pkgs
from pip._internal.utils.egg_link import egg_link_path_from_sys_path as egg_link_path_from_sys_path
from pip._internal.utils.misc import is_local as is_local, normalize_path as normalize_path
from pip._internal.utils.urls import url_to_path as url_to_path
from pip._vendor.packaging.requirements import Requirement as Requirement
from pip._vendor.packaging.specifiers import InvalidSpecifier as InvalidSpecifier, SpecifierSet as SpecifierSet
from pip._vendor.packaging.utils import NormalizedName as NormalizedName, canonicalize_name as canonicalize_name
from pip._vendor.packaging.version import LegacyVersion as LegacyVersion, Version as Version
from typing import Any, Collection, Container, Dict, IO, Iterable, Iterator, List, NamedTuple, Protocol

DistributionVersion = LegacyVersion | Version
InfoPath = str | pathlib.PurePath
logger: Incomplete

class BaseEntryPoint(Protocol):
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> str: ...
    @property
    def group(self) -> str: ...

class RequiresEntry(NamedTuple):
    requirement: str
    extra: str
    marker: str

class BaseDistribution(Protocol):
    @classmethod
    def from_directory(cls, directory: str) -> BaseDistribution:
        """Load the distribution from a metadata directory.

        :param directory: Path to a metadata directory, e.g. ``.dist-info``.
        """
    @classmethod
    def from_metadata_file_contents(cls, metadata_contents: bytes, filename: str, project_name: str) -> BaseDistribution:
        '''Load the distribution from the contents of a METADATA file.

        This is used to implement PEP 658 by generating a "shallow" dist object that can
        be used for resolution without downloading or building the actual dist yet.

        :param metadata_contents: The contents of a METADATA file.
        :param filename: File name for the dist with this metadata.
        :param project_name: Name of the project this dist represents.
        '''
    @classmethod
    def from_wheel(cls, wheel: Wheel, name: str) -> BaseDistribution:
        """Load the distribution from a given wheel.

        :param wheel: A concrete wheel definition.
        :param name: File name of the wheel.

        :raises InvalidWheel: Whenever loading of the wheel causes a
            :py:exc:`zipfile.BadZipFile` exception to be thrown.
        :raises UnsupportedWheel: If the wheel is a valid zip, but malformed
            internally.
        """
    @property
    def location(self) -> str | None:
        """Where the distribution is loaded from.

        A string value is not necessarily a filesystem path, since distributions
        can be loaded from other sources, e.g. arbitrary zip archives. ``None``
        means the distribution is created in-memory.

        Do not canonicalize this value with e.g. ``pathlib.Path.resolve()``. If
        this is a symbolic link, we want to preserve the relative path between
        it and files in the distribution.
        """
    @property
    def editable_project_location(self) -> str | None:
        """The project location for editable distributions.

        This is the directory where pyproject.toml or setup.py is located.
        None if the distribution is not installed in editable mode.
        """
    @property
    def installed_location(self) -> str | None:
        '''The distribution\'s "installed" location.

        This should generally be a ``site-packages`` directory. This is
        usually ``dist.location``, except for legacy develop-installed packages,
        where ``dist.location`` is the source code location, and this is where
        the ``.egg-link`` file is.

        The returned location is normalized (in particular, with symlinks removed).
        '''
    @property
    def info_location(self) -> str | None:
        """Location of the .[egg|dist]-info directory or file.

        Similarly to ``location``, a string value is not necessarily a
        filesystem path. ``None`` means the distribution is created in-memory.

        For a modern .dist-info installation on disk, this should be something
        like ``{location}/{raw_name}-{version}.dist-info``.

        Do not canonicalize this value with e.g. ``pathlib.Path.resolve()``. If
        this is a symbolic link, we want to preserve the relative path between
        it and other files in the distribution.
        """
    @property
    def installed_by_distutils(self) -> bool:
        '''Whether this distribution is installed with legacy distutils format.

        A distribution installed with "raw" distutils not patched by setuptools
        uses one single file at ``info_location`` to store metadata. We need to
        treat this specially on uninstallation.
        '''
    @property
    def installed_as_egg(self) -> bool:
        """Whether this distribution is installed as an egg.

        This usually indicates the distribution was installed by (older versions
        of) easy_install.
        """
    @property
    def installed_with_setuptools_egg_info(self) -> bool:
        """Whether this distribution is installed with the ``.egg-info`` format.

        This usually indicates the distribution was installed with setuptools
        with an old pip version or with ``single-version-externally-managed``.

        Note that this ensure the metadata store is a directory. distutils can
        also installs an ``.egg-info``, but as a file, not a directory. This
        property is *False* for that case. Also see ``installed_by_distutils``.
        """
    @property
    def installed_with_dist_info(self) -> bool:
        '''Whether this distribution is installed with the "modern format".

        This indicates a "modern" installation, e.g. storing metadata in the
        ``.dist-info`` directory. This applies to installations made by
        setuptools (but through pip, not directly), or anything using the
        standardized build backend interface (PEP 517).
        '''
    @property
    def canonical_name(self) -> NormalizedName: ...
    @property
    def version(self) -> DistributionVersion: ...
    @property
    def setuptools_filename(self) -> str:
        """Convert a project name to its setuptools-compatible filename.

        This is a copy of ``pkg_resources.to_filename()`` for compatibility.
        """
    @property
    def direct_url(self) -> DirectUrl | None:
        """Obtain a DirectUrl from this distribution.

        Returns None if the distribution has no `direct_url.json` metadata,
        or if `direct_url.json` is invalid.
        """
    @property
    def installer(self) -> str: ...
    @property
    def requested(self) -> bool: ...
    @property
    def editable(self) -> bool: ...
    @property
    def local(self) -> bool:
        """If distribution is installed in the current virtual environment.

        Always True if we're not in a virtualenv.
        """
    @property
    def in_usersite(self) -> bool: ...
    @property
    def in_site_packages(self) -> bool: ...
    def is_file(self, path: InfoPath) -> bool:
        """Check whether an entry in the info directory is a file."""
    def iter_distutils_script_names(self) -> Iterator[str]:
        """Find distutils 'scripts' entries metadata.

        If 'scripts' is supplied in ``setup.py``, distutils records those in the
        installed distribution's ``scripts`` directory, a file for each script.
        """
    def read_text(self, path: InfoPath) -> str:
        """Read a file in the info directory.

        :raise FileNotFoundError: If ``path`` does not exist in the directory.
        :raise NoneMetadataError: If ``path`` exists in the info directory, but
            cannot be read.
        """
    def iter_entry_points(self) -> Iterable[BaseEntryPoint]: ...
    @property
    def metadata(self) -> email.message.Message:
        """Metadata of distribution parsed from e.g. METADATA or PKG-INFO.

        This should return an empty message if the metadata file is unavailable.

        :raises NoneMetadataError: If the metadata file is available, but does
            not contain valid metadata.
        """
    @property
    def metadata_dict(self) -> Dict[str, Any]:
        """PEP 566 compliant JSON-serializable representation of METADATA or PKG-INFO.

        This should return an empty dict if the metadata file is unavailable.

        :raises NoneMetadataError: If the metadata file is available, but does
            not contain valid metadata.
        """
    @property
    def metadata_version(self) -> str | None:
        '''Value of "Metadata-Version:" in distribution metadata, if available.'''
    @property
    def raw_name(self) -> str:
        '''Value of "Name:" in distribution metadata.'''
    @property
    def requires_python(self) -> SpecifierSet:
        '''Value of "Requires-Python:" in distribution metadata.

        If the key does not exist or contains an invalid value, an empty
        SpecifierSet should be returned.
        '''
    def iter_dependencies(self, extras: Collection[str] = ()) -> Iterable[Requirement]:
        '''Dependencies of this distribution.

        For modern .dist-info distributions, this is the collection of
        "Requires-Dist:" entries in distribution metadata.
        '''
    def iter_provided_extras(self) -> Iterable[str]:
        '''Extras provided by this distribution.

        For modern .dist-info distributions, this is the collection of
        "Provides-Extra:" entries in distribution metadata.

        The return value of this function is not particularly useful other than
        display purposes due to backward compatibility issues and the extra
        names being poorly normalized prior to PEP 685. If you want to perform
        logic operations on extras, use :func:`is_extra_provided` instead.
        '''
    def is_extra_provided(self, extra: str) -> bool:
        """Check whether an extra is provided by this distribution.

        This is needed mostly for compatibility issues with pkg_resources not
        following the extra normalization rules defined in PEP 685.
        """
    def iter_declared_entries(self) -> Iterator[str] | None:
        """Iterate through file entries declared in this distribution.

        For modern .dist-info distributions, this is the files listed in the
        ``RECORD`` metadata file. For legacy setuptools distributions, this
        comes from ``installed-files.txt``, with entries normalized to be
        compatible with the format used by ``RECORD``.

        :return: An iterator for listed entries, or None if the distribution
            contains neither ``RECORD`` nor ``installed-files.txt``.
        """

class BaseEnvironment:
    """An environment containing distributions to introspect."""
    @classmethod
    def default(cls) -> BaseEnvironment: ...
    @classmethod
    def from_paths(cls, paths: List[str] | None) -> BaseEnvironment: ...
    def get_distribution(self, name: str) -> BaseDistribution | None:
        """Given a requirement name, return the installed distributions.

        The name may not be normalized. The implementation must canonicalize
        it for lookup.
        """
    def iter_all_distributions(self) -> Iterator[BaseDistribution]:
        """Iterate through all installed distributions without any filtering."""
    def iter_installed_distributions(self, local_only: bool = True, skip: Container[str] = ..., include_editables: bool = True, editables_only: bool = False, user_only: bool = False) -> Iterator[BaseDistribution]:
        """Return a list of installed distributions.

        This is based on ``iter_all_distributions()`` with additional filtering
        options. Note that ``iter_installed_distributions()`` without arguments
        is *not* equal to ``iter_all_distributions()``, since some of the
        configurations exclude packages by default.

        :param local_only: If True (default), only return installations
        local to the current virtualenv, if in a virtualenv.
        :param skip: An iterable of canonicalized project names to ignore;
            defaults to ``stdlib_pkgs``.
        :param include_editables: If False, don't report editables.
        :param editables_only: If True, only report editables.
        :param user_only: If True, only report installations in the user
        site directory.
        """

class Wheel(Protocol):
    location: str
    def as_zipfile(self) -> zipfile.ZipFile: ...

class FilesystemWheel(Wheel):
    location: Incomplete
    def __init__(self, location: str) -> None: ...
    def as_zipfile(self) -> zipfile.ZipFile: ...

class MemoryWheel(Wheel):
    location: Incomplete
    stream: Incomplete
    def __init__(self, location: str, stream: IO[bytes]) -> None: ...
    def as_zipfile(self) -> zipfile.ZipFile: ...
