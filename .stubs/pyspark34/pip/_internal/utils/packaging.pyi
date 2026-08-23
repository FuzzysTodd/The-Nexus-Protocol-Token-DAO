from _typeshed import Incomplete
from pip._vendor.packaging import specifiers as specifiers, version as version
from pip._vendor.packaging.requirements import Requirement as Requirement
from typing import Tuple

NormalizedExtra: Incomplete
logger: Incomplete

def check_requires_python(requires_python: str | None, version_info: Tuple[int, ...]) -> bool:
    '''
    Check if the given Python version matches a "Requires-Python" specifier.

    :param version_info: A 3-tuple of ints representing a Python
        major-minor-micro version to check (e.g. `sys.version_info[:3]`).

    :return: `True` if the given Python version satisfies the requirement.
        Otherwise, return `False`.

    :raises InvalidSpecifier: If `requires_python` has an invalid format.
    '''
def get_requirement(req_string: str) -> Requirement:
    """Construct a packaging.Requirement object with caching"""
def safe_extra(extra: str) -> NormalizedExtra:
    """Convert an arbitrary string to a standard 'extra' name

    Any runs of non-alphanumeric characters are replaced with a single '_',
    and the result is always lowercased.

    This function is duplicated from ``pkg_resources``. Note that this is not
    the same to either ``canonicalize_name`` or ``_egg_link_name``.
    """
