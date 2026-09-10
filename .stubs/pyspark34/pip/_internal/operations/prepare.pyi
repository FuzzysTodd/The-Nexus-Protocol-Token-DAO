from _typeshed import Incomplete
from pip._internal.distributions import make_distribution_for_install_requirement as make_distribution_for_install_requirement
from pip._internal.distributions.installed import InstalledDistribution as InstalledDistribution
from pip._internal.exceptions import DirectoryUrlHashUnsupported as DirectoryUrlHashUnsupported, HashMismatch as HashMismatch, HashUnpinned as HashUnpinned, InstallationError as InstallationError, MetadataInconsistent as MetadataInconsistent, NetworkConnectionError as NetworkConnectionError, VcsHashUnsupported as VcsHashUnsupported
from pip._internal.index.package_finder import PackageFinder as PackageFinder
from pip._internal.metadata import BaseDistribution as BaseDistribution, get_metadata_distribution as get_metadata_distribution
from pip._internal.models.direct_url import ArchiveInfo as ArchiveInfo
from pip._internal.models.link import Link as Link
from pip._internal.models.wheel import Wheel as Wheel
from pip._internal.network.download import BatchDownloader as BatchDownloader, Downloader as Downloader
from pip._internal.network.lazy_wheel import HTTPRangeRequestUnsupported as HTTPRangeRequestUnsupported, dist_from_wheel_url as dist_from_wheel_url
from pip._internal.network.session import PipSession as PipSession
from pip._internal.operations.build.build_tracker import BuildTracker as BuildTracker
from pip._internal.req.req_install import InstallRequirement as InstallRequirement
from pip._internal.utils._log import getLogger as getLogger
from pip._internal.utils.direct_url_helpers import direct_url_for_editable as direct_url_for_editable, direct_url_from_link as direct_url_from_link
from pip._internal.utils.hashes import Hashes as Hashes, MissingHashes as MissingHashes
from pip._internal.utils.logging import indent_log as indent_log
from pip._internal.utils.misc import display_path as display_path, hash_file as hash_file, hide_url as hide_url, redact_auth_from_requirement as redact_auth_from_requirement
from pip._internal.utils.temp_dir import TempDirectory as TempDirectory
from pip._internal.utils.unpacking import unpack_file as unpack_file
from pip._internal.vcs import vcs as vcs
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name
from typing import Iterable

logger: Incomplete

def unpack_vcs_link(link: Link, location: str, verbosity: int) -> None: ...

class File:
    path: Incomplete
    content_type: Incomplete
    def __init__(self, path: str, content_type: str | None) -> None: ...

def get_http_url(link: Link, download: Downloader, download_dir: str | None = None, hashes: Hashes | None = None) -> File: ...
def get_file_url(link: Link, download_dir: str | None = None, hashes: Hashes | None = None) -> File:
    """Get file and optionally check its hash."""
def unpack_url(link: Link, location: str, download: Downloader, verbosity: int, download_dir: str | None = None, hashes: Hashes | None = None) -> File | None:
    """Unpack link into location, downloading if required.

    :param hashes: A Hashes object, one of whose embedded hashes must match,
        or HashMismatch will be raised. If the Hashes is empty, no matches are
        required, and unhashable types of requirements (like VCS ones, which
        would ordinarily raise HashUnsupported) are allowed.
    """

class RequirementPreparer:
    """Prepares a Requirement"""
    src_dir: Incomplete
    build_dir: Incomplete
    build_tracker: Incomplete
    finder: Incomplete
    download_dir: Incomplete
    build_isolation: Incomplete
    check_build_deps: Incomplete
    require_hashes: Incomplete
    use_user_site: Incomplete
    use_lazy_wheel: Incomplete
    verbosity: Incomplete
    legacy_resolver: Incomplete
    def __init__(self, build_dir: str, download_dir: str | None, src_dir: str, build_isolation: bool, check_build_deps: bool, build_tracker: BuildTracker, session: PipSession, progress_bar: str, finder: PackageFinder, require_hashes: bool, use_user_site: bool, lazy_wheel: bool, verbosity: int, legacy_resolver: bool) -> None: ...
    def prepare_linked_requirement(self, req: InstallRequirement, parallel_builds: bool = False) -> BaseDistribution:
        """Prepare a requirement to be obtained from req.link."""
    def prepare_linked_requirements_more(self, reqs: Iterable[InstallRequirement], parallel_builds: bool = False) -> None:
        """Prepare linked requirements more, if needed."""
    def save_linked_requirement(self, req: InstallRequirement) -> None: ...
    def prepare_editable_requirement(self, req: InstallRequirement) -> BaseDistribution:
        """Prepare an editable requirement."""
    def prepare_installed_requirement(self, req: InstallRequirement, skip_reason: str) -> BaseDistribution:
        """Prepare an already-installed requirement."""
