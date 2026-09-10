from _typeshed import Incomplete

class Installable:
    """ Encapsulate a list of files and directories that will be installed into
    a target directory.
    """
    name: Incomplete
    target_subdir: Incomplete
    files: Incomplete
    def __init__(self, name, *, target_subdir: Incomplete | None = None) -> None:
        """ Initialise the installable.  The optional target_subdir is the
        path of a sub-directory of the eventual target where the files will be
        installed.  If target_subdir is an absolute pathname then it is used as
        the eventual target name.
        """
    def get_full_target_dir(self, target_dir):
        """ Return the full target directory name. """
    def install(self, target_dir, installed, *, do_install: bool = True) -> None:
        """ Optionally install the files in a target directory and update the
        given list of installed files.
        """
