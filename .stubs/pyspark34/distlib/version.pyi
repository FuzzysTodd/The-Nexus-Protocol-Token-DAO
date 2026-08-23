from _typeshed import Incomplete

__all__ = ['NormalizedVersion', 'NormalizedMatcher', 'LegacyVersion', 'LegacyMatcher', 'SemanticVersion', 'SemanticMatcher', 'UnsupportedVersionError', 'get_scheme']

class UnsupportedVersionError(ValueError):
    """This is an unsupported version."""

class Version:
    def __init__(self, s) -> None: ...
    def parse(self, s) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __gt__(self, other): ...
    def __le__(self, other): ...
    def __ge__(self, other): ...
    def __hash__(self): ...
    @property
    def is_prerelease(self) -> None: ...

class Matcher:
    version_class: Incomplete
    def parse_requirement(self, s): ...
    name: Incomplete
    key: Incomplete
    def __init__(self, s) -> None: ...
    def match(self, version):
        """
        Check if the provided version matches the constraints.

        :param version: The version to match against this instance.
        :type version: String or :class:`Version` instance.
        """
    @property
    def exact_version(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...

class NormalizedVersion(Version):
    '''A rational version.

    Good:
        1.2         # equivalent to "1.2.0"
        1.2.0
        1.2a1
        1.2.3a2
        1.2.3b1
        1.2.3c1
        1.2.3.4
        TODO: fill this out

    Bad:
        1           # minimum two numbers
        1.2a        # release level must have a release serial
        1.2.3b
    '''
    def parse(self, s): ...
    PREREL_TAGS: Incomplete
    @property
    def is_prerelease(self): ...

class NormalizedMatcher(Matcher):
    version_class = NormalizedVersion

class LegacyVersion(Version):
    def parse(self, s): ...
    @property
    def is_prerelease(self): ...

class LegacyMatcher(Matcher):
    version_class = LegacyVersion
    numeric_re: Incomplete

class SemanticVersion(Version):
    def parse(self, s): ...
    @property
    def is_prerelease(self): ...

class SemanticMatcher(Matcher):
    version_class = SemanticVersion

class VersionScheme:
    key: Incomplete
    matcher: Incomplete
    suggester: Incomplete
    def __init__(self, key, matcher, suggester: Incomplete | None = None) -> None: ...
    def is_valid_version(self, s): ...
    def is_valid_matcher(self, s): ...
    def is_valid_constraint_list(self, s):
        """
        Used for processing some metadata fields
        """
    def suggest(self, s): ...

def get_scheme(name): ...
