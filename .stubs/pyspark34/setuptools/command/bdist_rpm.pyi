import distutils.command.bdist_rpm as orig
from ..warnings import SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning

class bdist_rpm(orig.bdist_rpm):
    """
    Override the default bdist_rpm behavior to do the following:

    1. Run egg_info to ensure the name and version are properly calculated.
    2. Always run 'install' using --single-version-externally-managed to
       disable eggs in RPM distributions.
    """
    def run(self) -> None: ...
