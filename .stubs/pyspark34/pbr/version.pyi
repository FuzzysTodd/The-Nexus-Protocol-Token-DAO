from _typeshed import Incomplete

use_importlib: bool

class SemanticVersion:
    """A pure semantic version independent of serialisation.

    See the pbr doc 'semver' for details on the semantics.
    """
    def __init__(self, major, minor: int = 0, patch: int = 0, prerelease_type: Incomplete | None = None, prerelease: Incomplete | None = None, dev_count: Incomplete | None = None) -> None:
        """Create a SemanticVersion.

        :param major: Major component of the version.
        :param minor: Minor component of the version. Defaults to 0.
        :param patch: Patch level component. Defaults to 0.
        :param prerelease_type: What sort of prerelease version this is -
            one of a(alpha), b(beta) or rc(release candidate).
        :param prerelease: For prerelease versions, what number prerelease.
            Defaults to 0.
        :param dev_count: How many commits since the last release.
        """
    def __eq__(self, other): ...
    def __hash__(self): ...
    def __lt__(self, other):
        """Compare self and other, another Semantic Version."""
    def __le__(self, other): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def __ne__(self, other): ...
    @classmethod
    def from_pip_string(klass, version_string):
        """Create a SemanticVersion from a pip version string.

        This method will parse a version like 1.3.0 into a SemanticVersion.

        This method is responsible for accepting any version string that any
        older version of pbr ever created.

        Therefore: versions like 1.3.0a1 versions are handled, parsed into a
        canonical form and then output - resulting in 1.3.0.0a1.
        Pre pbr-semver dev versions like 0.10.1.3.g83bef74 will be parsed but
        output as 0.10.1.dev3.g83bef74.

        :raises ValueError: Never tagged versions sdisted by old pbr result in
            just the git hash, e.g. '1234567' which poses a substantial problem
            since they collide with the semver versions when all the digits are
            numerals. Such versions will result in a ValueError being thrown if
            any non-numeric digits are present. They are an exception to the
            general case of accepting anything we ever output, since they were
            never intended and would permanently mess up versions on PyPI if
            ever released - we're treating that as a critical bug that we ever
            made them and have stopped doing that.
        """
    def brief_string(self):
        """Return the short version minus any alpha/beta tags."""
    def debian_string(self):
        """Return the version number to use when building a debian package.

        This translates the PEP440/semver precedence rules into Debian version
        sorting operators.
        """
    def decrement(self):
        """Return a decremented SemanticVersion.

        Decrementing versions doesn't make a lot of sense - this method only
        exists to support rendering of pre-release versions strings into
        serialisations (such as rpm) with no sort-before operator.

        The 9999 magic version component is from the spec on this - pbr-semver.

        :return: A new SemanticVersion object.
        """
    def increment(self, minor: bool = False, major: bool = False):
        """Return an incremented SemanticVersion.

        The default behaviour is to perform a patch level increment. When
        incrementing a prerelease version, the patch level is not changed
        - the prerelease serial is changed (e.g. beta 0 -> beta 1).

        Incrementing non-pre-release versions will not introduce pre-release
        versions - except when doing a patch incremental to a pre-release
        version the new version will only consist of major/minor/patch.

        :param minor: Increment the minor version.
        :param major: Increment the major version.
        :return: A new SemanticVersion object.
        """
    def release_string(self):
        """Return the full version of the package.

        This including suffixes indicating VCS status.
        """
    def rpm_string(self):
        """Return the version number to use when building an RPM package.

        This translates the PEP440/semver precedence rules into RPM version
        sorting operators. Because RPM has no sort-before operator (such as the
        ~ operator in dpkg),  we show all prerelease versions as being versions
        of the release before.
        """
    def to_dev(self, dev_count):
        """Return a development version of this semver.

        :param dev_count: The number of commits since the last release.
        """
    def version_tuple(self):
        """Present the version as a version_info tuple.

        For documentation on version_info tuples see the Python
        documentation for sys.version_info.

        Since semver and PEP-440 represent overlapping but not subsets of
        versions, we have to have some heuristic / mapping rules, and have
        extended the releaselevel field to have alphadev, betadev and
        candidatedev values. When they are present the dev count is used
        to provide the serial.
        - a/b/rc take precedence.
        - if there is no pre-release version the dev version is used.
        - serial is taken from the dev/a/b/c component.
        - final non-dev versions never get serials.
        """

class VersionInfo:
    package: Incomplete
    version: Incomplete
    def __init__(self, package) -> None:
        """Object that understands versioning for a package

        :param package: name of the python package, such as glance, or
                        python-glanceclient
        """
    def release_string(self):
        """Return the full version of the package.

        This including suffixes indicating VCS status.
        """
    def semantic_version(self):
        """Return the SemanticVersion object for this version."""
    def version_string(self):
        """Return the short version minus any alpha/beta tags."""
    canonical_version_string = version_string
    version_string_with_vcs = release_string
    def cached_version_string(self, prefix: str = ''):
        """Return a cached version string.

        This will return a cached version string if one is already cached,
        irrespective of prefix. If none is cached, one will be created with
        prefix and then cached and returned.
        """
