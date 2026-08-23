from IPython.core.error import UsageError as UsageError
from IPython.core.magic import Magics as Magics, line_magic as line_magic, magics_class as magics_class

class ExtensionMagics(Magics):
    """Magics to manage the IPython extensions system."""
    def load_ext(self, module_str) -> None:
        """Load an IPython extension by its module name."""
    def unload_ext(self, module_str) -> None:
        """Unload an IPython extension by its module name.

        Not all extensions can be unloaded, only those which define an
        ``unload_ipython_extension`` function.
        """
    def reload_ext(self, module_str) -> None:
        """Reload an IPython extension by its module name."""
