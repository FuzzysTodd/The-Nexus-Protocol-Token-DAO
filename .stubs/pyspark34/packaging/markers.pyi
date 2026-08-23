from typing import Any, Callable, Dict

__all__ = ['InvalidMarker', 'UndefinedComparison', 'UndefinedEnvironmentName', 'Marker', 'default_environment']

Operator = Callable[[str, str], bool]

class InvalidMarker(ValueError):
    """
    An invalid marker was found, users should refer to PEP 508.
    """
class UndefinedComparison(ValueError):
    """
    An invalid operation was attempted on a value that doesn't support it.
    """
class UndefinedEnvironmentName(ValueError):
    """
    A name was attempted to be used that does not exist inside of the
    environment.
    """

def default_environment() -> Dict[str, str]: ...

class Marker:
    def __init__(self, marker: str) -> None: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def evaluate(self, environment: Dict[str, str] | None = None) -> bool:
        """Evaluate a marker.

        Return the boolean from evaluating the given marker against the
        environment. environment is an optional argument to override all or
        part of the determined environment.

        The environment is determined from the current Python process.
        """
