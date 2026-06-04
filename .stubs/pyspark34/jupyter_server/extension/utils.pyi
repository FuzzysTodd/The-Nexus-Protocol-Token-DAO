from _typeshed import Incomplete

class ExtensionLoadingError(Exception):
    """An extension loading error."""
class ExtensionMetadataError(Exception):
    """An extension metadata error."""
class ExtensionModuleNotFound(Exception):
    """An extension module not found error."""
class NotAnExtensionApp(Exception):
    """An error raised when a module is not an extension."""

def get_loader(obj, logger: Incomplete | None = None):
    """Looks for _load_jupyter_server_extension as an attribute
    of the object or module.

    Adds backwards compatibility for old function name missing the
    underscore prefix.
    """
def get_metadata(package_name, logger: Incomplete | None = None):
    """Find the extension metadata from an extension package.

    This looks for a `_jupyter_server_extension_points` function
    that returns metadata about all extension points within a Jupyter
    Server Extension pacakge.

    If it doesn't exist, return a basic metadata packet given
    the module name.
    """
def validate_extension(name):
    """Raises an exception is the extension is missing a needed
    hook or metadata field.
    An extension is valid if:
    1) name is an importable Python package.
    1) the package has a _jupyter_server_extension_paths function
    2) each extension path has a _load_jupyter_server_extension function

    If this works, nothing should happen.
    """
