from .compat import ZipFile as ZipFile, detect_encoding as detect_encoding, sysconfig as sysconfig
from .resources import finder as finder
from .util import FileOperator as FileOperator, convert_path as convert_path, get_executable as get_executable, get_export_entry as get_export_entry, get_platform as get_platform, in_venv as in_venv
from _typeshed import Incomplete

logger: Incomplete
FIRST_LINE_RE: Incomplete
SCRIPT_TEMPLATE: str

def enquote_executable(executable): ...

class ScriptMaker:
    """
    A class to copy or create scripts from source scripts or callable
    specifications.
    """
    script_template = SCRIPT_TEMPLATE
    executable: Incomplete
    source_dir: Incomplete
    target_dir: Incomplete
    add_launchers: Incomplete
    force: bool
    clobber: bool
    set_mode: Incomplete
    variants: Incomplete
    version_info: Incomplete
    def __init__(self, source_dir, target_dir, add_launchers: bool = True, dry_run: bool = False, fileop: Incomplete | None = None) -> None: ...
    manifest: Incomplete
    def get_manifest(self, exename): ...
    variant_separator: str
    def get_script_filenames(self, name): ...
    @property
    def dry_run(self): ...
    @dry_run.setter
    def dry_run(self, value) -> None: ...
    def make(self, specification, options: Incomplete | None = None):
        """
        Make a script.

        :param specification: The specification, which is either a valid export
                              entry specification (to make a script from a
                              callable) or a filename (to make a script by
                              copying from a source location).
        :param options: A dictionary of options controlling script generation.
        :return: A list of all absolute pathnames written to.
        """
    def make_multiple(self, specifications, options: Incomplete | None = None):
        """
        Take a list of specifications and make scripts from them,
        :param specifications: A list of specifications.
        :return: A list of all absolute pathnames written to,
        """
