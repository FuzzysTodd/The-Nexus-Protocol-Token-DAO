from _typeshed import Incomplete
from pip._internal.exceptions import InvalidWheelFilename as InvalidWheelFilename
from pip._vendor.packaging.tags import Tag as Tag
from typing import Dict, Iterable, List

class Wheel:
    """A wheel file"""
    wheel_file_re: Incomplete
    filename: Incomplete
    name: Incomplete
    version: Incomplete
    build_tag: Incomplete
    pyversions: Incomplete
    abis: Incomplete
    plats: Incomplete
    file_tags: Incomplete
    def __init__(self, filename: str) -> None:
        """
        :raises InvalidWheelFilename: when the filename is invalid for a wheel
        """
    def get_formatted_file_tags(self) -> List[str]:
        """Return the wheel's tags as a sorted list of strings."""
    def support_index_min(self, tags: List[Tag]) -> int:
        """Return the lowest index that one of the wheel's file_tag combinations
        achieves in the given list of supported tags.

        For example, if there are 8 supported tags and one of the file tags
        is first in the list, then return 0.

        :param tags: the PEP 425 tags to check the wheel against, in order
            with most preferred first.

        :raises ValueError: If none of the wheel's file tags match one of
            the supported tags.
        """
    def find_most_preferred_tag(self, tags: List[Tag], tag_to_priority: Dict[Tag, int]) -> int:
        """Return the priority of the most preferred tag that one of the wheel's file
        tag combinations achieves in the given list of supported tags using the given
        tag_to_priority mapping, where lower priorities are more-preferred.

        This is used in place of support_index_min in some cases in order to avoid
        an expensive linear scan of a large list of tags.

        :param tags: the PEP 425 tags to check the wheel against.
        :param tag_to_priority: a mapping from tag to priority of that tag, where
            lower is more preferred.

        :raises ValueError: If none of the wheel's file tags match one of
            the supported tags.
        """
    def supported(self, tags: Iterable[Tag]) -> bool:
        """Return whether the wheel is compatible with one of the given tags.

        :param tags: the PEP 425 tags to check the wheel against.
        """
