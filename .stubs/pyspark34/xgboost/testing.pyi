from typing import Any
from typing_extensions import TypedDict

class PytestSkip(TypedDict):
    condition: bool
    reason: str

def has_ipv6() -> bool:
    """Check whether IPv6 is enabled on this host."""
def skip_ipv6() -> PytestSkip:
    """PyTest skip mark for IPv6."""
def timeout(sec: int, *args: Any, enable: bool = True, **kwargs: Any) -> Any:
    """Make a pytest mark for the `pytest-timeout` package.

    Parameters
    ----------
    sec :
        Timeout seconds.
    enable :
        Control whether timeout should be applied, used for debugging.

    Returns
    -------
    pytest.mark.timeout
    """
