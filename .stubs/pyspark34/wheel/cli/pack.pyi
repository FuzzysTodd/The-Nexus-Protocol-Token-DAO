from _typeshed import Incomplete
from wheel.cli import WheelError as WheelError
from wheel.wheelfile import WheelFile as WheelFile

DIST_INFO_RE: Incomplete
BUILD_NUM_RE: Incomplete

def pack(directory: str, dest_dir: str, build_number: str | None):
    """Repack a previously unpacked wheel directory into a new wheel file.

    The .dist-info/WHEEL file must contain one or more tags so that the target
    wheel file name can be determined.

    :param directory: The unpacked wheel directory
    :param dest_dir: Destination directory (defaults to the current directory)
    """
def read_tags(input_str: bytes) -> tuple[list[str], str | None]:
    """Read tags from a string.

    :param input_str: A string containing one or more tags, separated by spaces
    :return: A list of tags and a list of build tags
    """
def set_build_number(wheel_file_content: bytes, build_number: str | None) -> bytes:
    """Compute a build tag and add/replace/remove as necessary.

    :param wheel_file_content: The contents of .dist-info/WHEEL
    :param build_number: The build tags present in .dist-info/WHEEL
    :return: The (modified) contents of .dist-info/WHEEL
    """
def compute_tagline(tags: list[str]) -> str:
    """Compute a tagline from a list of tags.

    :param tags: A list of tags
    :return: A tagline
    """
