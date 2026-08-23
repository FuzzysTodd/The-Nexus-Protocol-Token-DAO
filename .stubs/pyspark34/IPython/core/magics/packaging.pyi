from IPython.core.magic import Magics as Magics, line_magic as line_magic, magics_class as magics_class
from _typeshed import Incomplete

CONDA_COMMANDS_REQUIRING_PREFIX: Incomplete
CONDA_COMMANDS_REQUIRING_YES: Incomplete
CONDA_ENV_FLAGS: Incomplete
CONDA_YES_FLAGS: Incomplete

class PackagingMagics(Magics):
    """Magics related to packaging & installation"""
    def pip(self, line) -> None:
        """Run the pip package manager within the current kernel.

        Usage:
          %pip install [pkgs]
        """
    def conda(self, line) -> None:
        """Run the conda package manager within the current kernel.

        Usage:
          %conda install [pkgs]
        """
