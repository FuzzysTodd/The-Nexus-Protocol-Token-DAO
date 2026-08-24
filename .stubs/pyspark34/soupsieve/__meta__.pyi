from _typeshed import Incomplete
from typing import NamedTuple

RE_VER: Incomplete
REL_MAP: Incomplete
DEV_STATUS: Incomplete
PRE_REL_MAP: Incomplete

class Version(NamedTuple('Version', [('major', Incomplete), ('minor', Incomplete), ('micro', Incomplete), ('release', Incomplete), ('pre', Incomplete), ('post', Incomplete), ('dev', Incomplete)])):
    '''
    Get the version (PEP 440).

    A biased approach to the PEP 440 semantic version.

    Provides a tuple structure which is sorted for comparisons `v1 > v2` etc.
      (major, minor, micro, release type, pre-release build, post-release build, development release build)
    Release types are named in is such a way they are comparable with ease.
    Accessors to check if a development, pre-release, or post-release build. Also provides accessor to get
    development status for setup files.

    How it works (currently):

    - You must specify a release type as either `final`, `alpha`, `beta`, or `candidate`.
    - To define a development release, you can use either `.dev`, `.dev-alpha`, `.dev-beta`, or `.dev-candidate`.
      The dot is used to ensure all development specifiers are sorted before `alpha`.
      You can specify a `dev` number for development builds, but do not have to as implicit development releases
      are allowed.
    - You must specify a `pre` value greater than zero if using a prerelease as this project (not PEP 440) does not
      allow implicit prereleases.
    - You can optionally set `post` to a value greater than zero to make the build a post release. While post releases
      are technically allowed in prereleases, it is strongly discouraged, so we are rejecting them. It should be
      noted that we do not allow `post0` even though PEP 440 does not restrict this. This project specifically
      does not allow implicit post releases.
    - It should be noted that we do not support epochs `1!` or local versions `+some-custom.version-1`.

    Acceptable version releases:

    ```
    Version(1, 0, 0, "final")                    1.0
    Version(1, 2, 0, "final")                    1.2
    Version(1, 2, 3, "final")                    1.2.3
    Version(1, 2, 0, ".dev-alpha", pre=4)        1.2a4
    Version(1, 2, 0, ".dev-beta", pre=4)         1.2b4
    Version(1, 2, 0, ".dev-candidate", pre=4)    1.2rc4
    Version(1, 2, 0, "final", post=1)            1.2.post1
    Version(1, 2, 3, ".dev")                     1.2.3.dev0
    Version(1, 2, 3, ".dev", dev=1)              1.2.3.dev1
    ```

    '''
    def __new__(cls, major: int, minor: int, micro: int, release: str = 'final', pre: int = 0, post: int = 0, dev: int = 0) -> Version:
        """Validate version info."""

def parse_version(ver: str) -> Version:
    """Parse version into a comparable Version tuple."""

__version_info__: Incomplete
__version__: Incomplete
