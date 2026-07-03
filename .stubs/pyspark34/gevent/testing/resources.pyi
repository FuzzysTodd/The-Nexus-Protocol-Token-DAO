from _typeshed import Incomplete

def get_ALL_RESOURCES():
    """Return a fresh list of resource names."""
def parse_resources(resource_str: Incomplete | None = None): ...
def unparse_resources(resources):
    """
    Given a list of enabled resources, produce the correct environment variable
    setting to enable (only) that list.
    """
def setup_resources(resources: Incomplete | None = None):
    """
    Call either with a list of resources or a resource string.

    If ``None`` is given, get the resource string from the environment.
    """
def ensure_setup_resources(): ...
def exit_without_resource(resource) -> None:
    """
    Call this in standalone test modules that can't use unittest.SkipTest.

    Exits with a status of 0 if the resource isn't enabled.
    """
def skip_without_resource(resource, reason: str = '') -> None: ...
