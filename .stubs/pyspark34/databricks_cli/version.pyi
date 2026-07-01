from _typeshed import Incomplete

version: str

def print_version_callback(ctx, param, value) -> None: ...
def is_release_version(value: Incomplete | None = None):
    """
    Returns whether the current version of databricks-cli is a release version or not.
    """
def next_development_version(value: Incomplete | None = None):
    """
    Returns the hypothetical next development version of databricks-cli.
    """
