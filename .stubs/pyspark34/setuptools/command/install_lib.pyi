import distutils.command.install_lib as orig

class install_lib(orig.install_lib):
    """Don't add compiled flags to filenames of non-Python files"""
    def run(self) -> None: ...
    def get_exclusions(self):
        """
        Return a collections.Sized collections.Container of paths to be
        excluded for single_version_externally_managed installations.
        """
    def copy_tree(self, infile, outfile, preserve_mode: int = 1, preserve_times: int = 1, preserve_symlinks: int = 0, level: int = 1): ...
    def get_outputs(self): ...
