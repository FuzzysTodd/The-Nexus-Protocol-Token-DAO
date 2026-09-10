from pathlib import Path

__all__ = ['PathLike', 'is_missing', 'canonical_gpu_indices', 'validate_gpu_indices', 'parse_time', 'parse_memory_size']

PathLike = Path | str

def is_missing(value):
    """
    Used to check whether a dataclass field has ever been assigned.

    If a field without default value has never been assigned, it will have a special value ``MISSING``.
    This function checks if the parameter is ``MISSING``.
    """
def canonical_gpu_indices(indices):
    """
    If ``indices`` is not None, cast it to list of int.
    """
def validate_gpu_indices(indices) -> None: ...
def parse_time(value):
    """
    If ``value`` is a string, convert it to integral number of seconds.
    """
def parse_memory_size(value):
    """
    If ``value`` is a string, convert it to integral number of mega bytes.
    """
