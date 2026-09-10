import abc
from _typeshed import Incomplete

Protocol = abc.ABC

class TraversableResourcesLoader:
    """
    Adapt loaders to provide TraversableResources and other
    compatibility.

    Used primarily for Python 3.9 and earlier where the native
    loaders do not yet implement TraversableResources.
    """
    spec: Incomplete
    def __init__(self, spec) -> None: ...
    @property
    def path(self): ...
    def get_resource_reader(self, name): ...

def wrap_spec(package):
    """
    Construct a package spec with traversable compatibility
    on the spec/loader/reader.

    Supersedes _adapters.wrap_spec to use TraversableResourcesLoader
    from above for older Python compatibility (<3.10).
    """

StrPath: Incomplete

def ensure_traversable(path):
    """
    Convert deprecated string arguments to traversables (pathlib.Path).
    """
