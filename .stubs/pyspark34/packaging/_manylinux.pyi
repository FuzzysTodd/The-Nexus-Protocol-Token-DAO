from ._elffile import EIClass as EIClass, EIData as EIData, ELFFile as ELFFile, EMachine as EMachine
from typing import Iterator, NamedTuple, Sequence

EF_ARM_ABIMASK: int
EF_ARM_ABI_VER5: int
EF_ARM_ABI_FLOAT_HARD: int

class _GLibCVersion(NamedTuple):
    major: int
    minor: int

def platform_tags(archs: Sequence[str]) -> Iterator[str]:
    """Generate manylinux tags compatible to the current platform.

    :param archs: Sequence of compatible architectures.
        The first one shall be the closest to the actual architecture and be the part of
        platform tag after the ``linux_`` prefix, e.g. ``x86_64``.
        The ``linux_`` prefix is assumed as a prerequisite for the current platform to
        be manylinux-compatible.

    :returns: An iterator of compatible manylinux tags.
    """
