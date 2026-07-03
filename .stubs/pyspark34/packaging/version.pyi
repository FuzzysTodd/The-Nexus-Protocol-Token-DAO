from ._structures import InfinityType, NegativeInfinityType
from _typeshed import Incomplete
from typing import Callable, NamedTuple, Tuple

__all__ = ['VERSION_PATTERN', 'parse', 'Version', 'InvalidVersion']

LocalType = Tuple[int | str, ...]
CmpPrePostDevType = InfinityType | NegativeInfinityType | Tuple[str, int]
CmpLocalType = NegativeInfinityType | Tuple[Tuple[int, str] | Tuple[NegativeInfinityType, int | str], ...]
CmpKey = Tuple[int, Tuple[int, ...], CmpPrePostDevType, CmpPrePostDevType, CmpPrePostDevType, CmpLocalType]
VersionComparisonMethod = Callable[[CmpKey, CmpKey], bool]

class _Version(NamedTuple):
    epoch: int
    release: Tuple[int, ...]
    dev: Tuple[str, int] | None
    pre: Tuple[str, int] | None
    post: Tuple[str, int] | None
    local: LocalType | None

def parse(version: str) -> Version:
    """Parse the given version string.

    >>> parse('1.0.dev1')
    <Version('1.0.dev1')>

    :param version: The version string to parse.
    :raises InvalidVersion: When the version string is not a valid version.
    """

class InvalidVersion(ValueError):
    '''Raised when a version string is not a valid version.

    >>> Version("invalid")
    Traceback (most recent call last):
        ...
    packaging.version.InvalidVersion: Invalid version: \'invalid\'
    '''

class _BaseVersion:
    def __hash__(self) -> int: ...
    def __lt__(self, other: _BaseVersion) -> bool: ...
    def __le__(self, other: _BaseVersion) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: _BaseVersion) -> bool: ...
    def __gt__(self, other: _BaseVersion) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

VERSION_PATTERN: Incomplete

class Version(_BaseVersion):
    '''This class abstracts handling of a project\'s versions.

    A :class:`Version` instance is comparison aware and can be compared and
    sorted using the standard Python interfaces.

    >>> v1 = Version("1.0a5")
    >>> v2 = Version("1.0")
    >>> v1
    <Version(\'1.0a5\')>
    >>> v2
    <Version(\'1.0\')>
    >>> v1 < v2
    True
    >>> v1 == v2
    False
    >>> v1 > v2
    False
    >>> v1 >= v2
    False
    >>> v1 <= v2
    True
    '''
    def __init__(self, version: str) -> None:
        """Initialize a Version object.

        :param version:
            The string representation of a version which will be parsed and normalized
            before use.
        :raises InvalidVersion:
            If the ``version`` does not conform to PEP 440 in any way then this
            exception will be raised.
        """
    @property
    def epoch(self) -> int:
        '''The epoch of the version.

        >>> Version("2.0.0").epoch
        0
        >>> Version("1!2.0.0").epoch
        1
        '''
    @property
    def release(self) -> Tuple[int, ...]:
        '''The components of the "release" segment of the version.

        >>> Version("1.2.3").release
        (1, 2, 3)
        >>> Version("2.0.0").release
        (2, 0, 0)
        >>> Version("1!2.0.0.post0").release
        (2, 0, 0)

        Includes trailing zeroes but not the epoch or any pre-release / development /
        post-release suffixes.
        '''
    @property
    def pre(self) -> Tuple[str, int] | None:
        '''The pre-release segment of the version.

        >>> print(Version("1.2.3").pre)
        None
        >>> Version("1.2.3a1").pre
        (\'a\', 1)
        >>> Version("1.2.3b1").pre
        (\'b\', 1)
        >>> Version("1.2.3rc1").pre
        (\'rc\', 1)
        '''
    @property
    def post(self) -> int | None:
        '''The post-release number of the version.

        >>> print(Version("1.2.3").post)
        None
        >>> Version("1.2.3.post1").post
        1
        '''
    @property
    def dev(self) -> int | None:
        '''The development number of the version.

        >>> print(Version("1.2.3").dev)
        None
        >>> Version("1.2.3.dev1").dev
        1
        '''
    @property
    def local(self) -> str | None:
        '''The local version segment of the version.

        >>> print(Version("1.2.3").local)
        None
        >>> Version("1.2.3+abc").local
        \'abc\'
        '''
    @property
    def public(self) -> str:
        '''The public portion of the version.

        >>> Version("1.2.3").public
        \'1.2.3\'
        >>> Version("1.2.3+abc").public
        \'1.2.3\'
        >>> Version("1.2.3+abc.dev1").public
        \'1.2.3\'
        '''
    @property
    def base_version(self) -> str:
        '''The "base version" of the version.

        >>> Version("1.2.3").base_version
        \'1.2.3\'
        >>> Version("1.2.3+abc").base_version
        \'1.2.3\'
        >>> Version("1!1.2.3+abc.dev1").base_version
        \'1!1.2.3\'

        The "base version" is the public version of the project without any pre or post
        release markers.
        '''
    @property
    def is_prerelease(self) -> bool:
        '''Whether this version is a pre-release.

        >>> Version("1.2.3").is_prerelease
        False
        >>> Version("1.2.3a1").is_prerelease
        True
        >>> Version("1.2.3b1").is_prerelease
        True
        >>> Version("1.2.3rc1").is_prerelease
        True
        >>> Version("1.2.3dev1").is_prerelease
        True
        '''
    @property
    def is_postrelease(self) -> bool:
        '''Whether this version is a post-release.

        >>> Version("1.2.3").is_postrelease
        False
        >>> Version("1.2.3.post1").is_postrelease
        True
        '''
    @property
    def is_devrelease(self) -> bool:
        '''Whether this version is a development release.

        >>> Version("1.2.3").is_devrelease
        False
        >>> Version("1.2.3.dev1").is_devrelease
        True
        '''
    @property
    def major(self) -> int:
        '''The first item of :attr:`release` or ``0`` if unavailable.

        >>> Version("1.2.3").major
        1
        '''
    @property
    def minor(self) -> int:
        '''The second item of :attr:`release` or ``0`` if unavailable.

        >>> Version("1.2.3").minor
        2
        >>> Version("1").minor
        0
        '''
    @property
    def micro(self) -> int:
        '''The third item of :attr:`release` or ``0`` if unavailable.

        >>> Version("1.2.3").micro
        3
        >>> Version("1").micro
        0
        '''
