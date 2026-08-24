from ..wheelfile import WheelFile as WheelFile
from .pack import read_tags as read_tags, set_build_number as set_build_number
from collections.abc import Iterable

def tags(wheel: str, python_tags: str | None = None, abi_tags: str | None = None, platform_tags: str | None = None, build_tag: str | None = None, remove: bool = False) -> str:
    '''Change the tags on a wheel file.

    The tags are left unchanged if they are not specified. To specify "none",
    use ["none"]. To append to the previous tags, a tag should start with a
    "+".  If a tag starts with "-", it will be removed from existing tags.
    Processing is done left to right.

    :param wheel: The paths to the wheels
    :param python_tags: The Python tags to set
    :param abi_tags: The ABI tags to set
    :param platform_tags: The platform tags to set
    :param build_tag: The build tag to set
    :param remove: Remove the original wheel
    '''
def set_tags(in_string: bytes, tags: Iterable[str]) -> bytes:
    """Set the tags in the .dist-info/WHEEL file contents.

    :param in_string: The string to modify.
    :param tags: The tags to set.
    """
