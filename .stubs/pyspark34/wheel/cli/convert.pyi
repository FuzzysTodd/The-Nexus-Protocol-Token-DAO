from . import WheelError as WheelError
from ..bdist_wheel import bdist_wheel as bdist_wheel
from ..wheelfile import WheelFile as WheelFile
from _typeshed import Incomplete

egg_info_re: Incomplete

class _bdist_wheel_tag(bdist_wheel):
    full_tag_supplied: bool
    full_tag: Incomplete
    def get_tag(self): ...

def egg2wheel(egg_path: str, dest_dir: str): ...
def parse_wininst_info(wininfo_name, egginfo_name):
    """Extract metadata from filenames.

    Extracts the 4 metadataitems needed (name, version, pyversion, arch) from
    the installer filename and the name of the egg-info directory embedded in
    the zipfile (if any).

    The egginfo filename has the format::

        name-ver(-pyver)(-arch).egg-info

    The installer filename has the format::

        name-ver.arch(-pyver).exe

    Some things to note:

    1. The installer filename is not definitive. An installer can be renamed
       and work perfectly well as an installer. So more reliable data should
       be used whenever possible.
    2. The egg-info data should be preferred for the name and version, because
       these come straight from the distutils metadata, and are mandatory.
    3. The pyver from the egg-info data should be ignored, as it is
       constructed from the version of Python used to build the installer,
       which is irrelevant - the installer filename is correct here (even to
       the point that when it's not there, any version is implied).
    4. The architecture must be taken from the installer filename, as it is
       not included in the egg-info data.
    5. Architecture-neutral installers still have an architecture because the
       installer format itself (being executable) is architecture-specific. We
       should therefore ignore the architecture if the content is pure-python.
    """
def wininst2wheel(path, dest_dir) -> None: ...
def convert(files, dest_dir, verbose) -> None: ...
