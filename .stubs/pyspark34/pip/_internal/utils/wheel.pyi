from _typeshed import Incomplete
from email.message import Message
from pip._internal.exceptions import UnsupportedWheel as UnsupportedWheel
from pip._vendor.packaging.utils import canonicalize_name as canonicalize_name
from typing import Tuple
from zipfile import ZipFile

VERSION_COMPATIBLE: Incomplete
logger: Incomplete

def parse_wheel(wheel_zip: ZipFile, name: str) -> Tuple[str, Message]:
    """Extract information from the provided wheel, ensuring it meets basic
    standards.

    Returns the name of the .dist-info directory and the parsed WHEEL metadata.
    """
def wheel_dist_info_dir(source: ZipFile, name: str) -> str:
    """Returns the name of the contained .dist-info directory.

    Raises AssertionError or UnsupportedWheel if not found, >1 found, or
    it doesn't match the provided name.
    """
def read_wheel_metadata_file(source: ZipFile, path: str) -> bytes: ...
def wheel_metadata(source: ZipFile, dist_info_dir: str) -> Message:
    """Return the WHEEL metadata of an extracted wheel, if possible.
    Otherwise, raise UnsupportedWheel.
    """
def wheel_version(wheel_data: Message) -> Tuple[int, ...]:
    """Given WHEEL metadata, return the parsed Wheel-Version.
    Otherwise, raise UnsupportedWheel.
    """
def check_compatibility(version: Tuple[int, ...], name: str) -> None:
    """Raises errors or warns if called with an incompatible Wheel-Version.

    pip should refuse to install a Wheel-Version that's a major series
    ahead of what it's compatible with (e.g 2.0 > 1.1); and warn when
    installing a version only minor version ahead (e.g 1.2 > 1.1).

    version: a 2-tuple representing a Wheel-Version (Major, Minor)
    name: name of wheel or package to raise exception about

    :raises UnsupportedWheel: when an incompatible Wheel-Version is given
    """
