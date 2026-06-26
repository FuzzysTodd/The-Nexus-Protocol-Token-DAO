from enum import Enum

class MatchConditions(Enum):
    """An enum to describe match conditions."""
    Unconditionally: int
    IfNotModified: int
    IfModified: int
    IfPresent: int
    IfMissing: int
