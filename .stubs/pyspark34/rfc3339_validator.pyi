from _typeshed import Incomplete

__version__: str
RFC3339_REGEX_FLAGS: int
RFC3339_REGEX: Incomplete

def validate_rfc3339(date_string):
    """
    Validates dates against RFC3339 datetime format
    Leap seconds are no supported.
    """
