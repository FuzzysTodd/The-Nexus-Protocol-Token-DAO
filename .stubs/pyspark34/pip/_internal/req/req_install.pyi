from _typeshed import Incomplete
from optparse import Values
from pathlib import Path
from pip._internal.build_env import BuildEnvironment as BuildEnvironment, NoOpBuildEnvironment as NoOpBuildEnvironment
from pip._internal.exceptions import InstallationError as InstallationError, PreviousBuildDirError as PreviousBuildDirError
from pip._internal.locations import get_scheme as get_scheme
from pip._internal.metadata import BaseDistribution as BaseDistribution, get_default_environment as get_default_environment, get_directory_distribution as get_directory_distribution, get_wheel_distribution as get_wheel_distribution
from pip._internal.metadata.base import FilesystemWheel as FilesystemWheel
from pip._internal.models.direct_url import DirectUrl as DirectUrl
from pip._internal.models.link import Link as Link
from pip._internal.operations.build.metadata import generate_metadata as generate_metadata
from pip._internal.operations.build.metadata_editable import generate_editable_metadata as generate_editable_metadata
from pip._internal.operations.install.wheel import install_wheel as install_wheel
from pip._internal.pyproject import load_pyproject_toml as load_pyproject_toml, make_pyproject_path as make_pyproject_path
from pip._internal.req.req_uninstall import UninstallPathSet as UninstallPathSet
from pip._internal.utils.deprecation import deprecated as deprecated
from pip._internal.utils.hashes import Hashes as Hashes
from pip._internal.utils.misc import ConfiguredBuildBackendHookCaller as ConfiguredBuildBackendHookCaller, ask_path_exists as ask_path_exists, backup_dir as backup_dir, display_path as display_path, hide_url as hide_url, is_installable_dir as is_installable_dir, redact_auth_from_requirement as redact_auth_from_requirement, redact_auth_from_url as redact_auth_from_url
from pip._internal.utils.packaging import safe_extra as safe_extra
from pip._internal.utils.subprocess import runner_with_spinner_message as runner_with_spinner_message
from pip._internal.utils.temp_dir import TempDirectory as TempDirectory, tempdir_kinds as tempdir_kinds
from pip._internal.utils.unpacking import unpack_file as unpack_file
from pip._internal.utils.virtualenv import running_under_virtualenv as running_under_virtualenv
from pip._internal.vcs import vcs as vcs
from pip._vendor.packaging.markers import Marker as Marker
from pip._vendor.packaging.requirements import Requirement as Requirement
from pip._vendor.packaging.specifiers import SpecifierSet as SpecifierSet
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name
from pip._vendor.packaging.version import Version as Version
from pip._vendor.pyproject_hooks import BuildBackendHookCaller as BuildBackendHookCaller
from typing import Any, Collection, Dict, Iterable, List, Sequence

logger: Incomplete

class InstallRequirement:
    """
    Represents something that may be installed later on, may have information
    about where to fetch the relevant requirement and also contains logic for
    installing the said requirement.
    """
    req: Incomplete
    comes_from: Incomplete
    constraint: Incomplete
    editable: Incomplete
    permit_editable_wheels: Incomplete
    source_dir: Incomplete
    link: Incomplete
    cached_wheel_source_link: Incomplete
    download_info: Incomplete
    local_file_path: Incomplete
    extras: Incomplete
    markers: Incomplete
    satisfied_by: Incomplete
    should_reinstall: bool
    install_succeeded: Incomplete
    global_options: Incomplete
    hash_options: Incomplete
    config_settings: Incomplete
    prepared: bool
    user_supplied: Incomplete
    isolated: Incomplete
    build_env: Incomplete
    metadata_directory: Incomplete
    pyproject_requires: Incomplete
    requirements_to_check: Incomplete
    pep517_backend: Incomplete
    use_pep517: Incomplete
    needs_more_preparation: bool
    def __init__(self, req: Requirement | None, comes_from: str | InstallRequirement | None, editable: bool = False, link: Link | None = None, markers: Marker | None = None, use_pep517: bool | None = None, isolated: bool = False, *, global_options: List[str] | None = None, hash_options: Dict[str, List[str]] | None = None, config_settings: Dict[str, str | List[str]] | None = None, constraint: bool = False, extras: Collection[str] = (), user_supplied: bool = False, permit_editable_wheels: bool = False) -> None: ...
    def format_debug(self) -> str:
        """An un-tested helper for getting state, for debugging."""
    @property
    def name(self) -> str | None: ...
    def supports_pyproject_editable(self) -> bool: ...
    @property
    def specifier(self) -> SpecifierSet: ...
    @property
    def is_direct(self) -> bool:
        """Whether this requirement was specified as a direct URL."""
    @property
    def is_pinned(self) -> bool:
        """Return whether I am pinned to an exact version.

        For example, some-package==1.2 is pinned; some-package>1.2 is not.
        """
    def match_markers(self, extras_requested: Iterable[str] | None = None) -> bool: ...
    @property
    def has_hash_options(self) -> bool:
        """Return whether any known-good hashes are specified as options.

        These activate --require-hashes mode; hashes specified as part of a
        URL do not.

        """
    def hashes(self, trust_internet: bool = True) -> Hashes:
        """Return a hash-comparer that considers my option- and URL-based
        hashes to be known-good.

        Hashes in URLs--ones embedded in the requirements file, not ones
        downloaded from an index server--are almost peers with ones from
        flags. They satisfy --require-hashes (whether it was implicitly or
        explicitly activated) but do not activate it. md5 and sha224 are not
        allowed in flags, which should nudge people toward good algos. We
        always OR all hashes together, even ones from URLs.

        :param trust_internet: Whether to trust URL-based (#md5=...) hashes
            downloaded from the internet, as by populate_link()

        """
    def from_path(self) -> str | None:
        '''Format a nice indicator to show where this "comes from" '''
    def ensure_build_location(self, build_dir: str, autodelete: bool, parallel_builds: bool) -> str: ...
    def warn_on_mismatching_name(self) -> None: ...
    def check_if_exists(self, use_user_site: bool) -> None:
        """Find an installed distribution that satisfies or conflicts
        with this requirement, and set self.satisfied_by or
        self.should_reinstall appropriately.
        """
    @property
    def is_wheel(self) -> bool: ...
    @property
    def is_wheel_from_cache(self) -> bool: ...
    @property
    def unpacked_source_directory(self) -> str: ...
    @property
    def setup_py_path(self) -> str: ...
    @property
    def setup_cfg_path(self) -> str: ...
    @property
    def pyproject_toml_path(self) -> str: ...
    def load_pyproject_toml(self) -> None:
        """Load the pyproject.toml file.

        After calling this routine, all of the attributes related to PEP 517
        processing for this requirement have been set. In particular, the
        use_pep517 attribute can be used to determine whether we should
        follow the PEP 517 or legacy (setup.py) code path.
        """
    def isolated_editable_sanity_check(self) -> None:
        """Check that an editable requirement if valid for use with PEP 517/518.

        This verifies that an editable that has a pyproject.toml either supports PEP 660
        or as a setup.py or a setup.cfg
        """
    def prepare_metadata(self) -> None:
        """Ensure that project metadata is available.

        Under PEP 517 and PEP 660, call the backend hook to prepare the metadata.
        Under legacy processing, call setup.py egg-info.
        """
    @property
    def metadata(self) -> Any: ...
    def get_dist(self) -> BaseDistribution: ...
    def assert_source_matches_version(self) -> None: ...
    def ensure_has_source_dir(self, parent_dir: str, autodelete: bool = False, parallel_builds: bool = False) -> None:
        """Ensure that a source_dir is set.

        This will create a temporary build dir if the name of the requirement
        isn't known yet.

        :param parent_dir: The ideal pip parent_dir for the source_dir.
            Generally src_dir for editables and build_dir for sdists.
        :return: self.source_dir
        """
    def needs_unpacked_archive(self, archive_source: Path) -> None: ...
    def ensure_pristine_source_checkout(self) -> None:
        """Ensure the source directory has not yet been built in."""
    def update_editable(self) -> None: ...
    def uninstall(self, auto_confirm: bool = False, verbose: bool = False) -> UninstallPathSet | None:
        """
        Uninstall the distribution currently satisfying this requirement.

        Prompts before removing or modifying files unless
        ``auto_confirm`` is True.

        Refuses to delete or modify files outside of ``sys.prefix`` -
        thus uninstallation within a virtual environment can only
        modify that virtual environment, even if the virtualenv is
        linked to global site-packages.

        """
    def archive(self, build_dir: str | None) -> None:
        """Saves archive to provided build_dir.

        Used for saving downloaded VCS requirements as part of `pip download`.
        """
    def install(self, global_options: Sequence[str] | None = None, root: str | None = None, home: str | None = None, prefix: str | None = None, warn_script_location: bool = True, use_user_site: bool = False, pycompile: bool = True) -> None: ...

def check_invalid_constraint_type(req: InstallRequirement) -> str: ...
def check_legacy_setup_py_options(options: Values, reqs: List[InstallRequirement]) -> None: ...
