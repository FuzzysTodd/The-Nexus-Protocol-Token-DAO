import importlib.metadata
from _typeshed import Incomplete
from typing import Protocol

class BadMetadata(ValueError):
    dist: Incomplete
    reason: Incomplete
    def __init__(self, dist: importlib.metadata.Distribution, *, reason: str) -> None: ...

class BasePath(Protocol):
    """A protocol that various path objects conform.

    This exists because importlib.metadata uses both ``pathlib.Path`` and
    ``zipfile.Path``, and we need a common base for type hints (Union does not
    work well since ``zipfile.Path`` is too new for our linter setup).

    This does not mean to be exhaustive, but only contains things that present
    in both classes *that we need*.
    """
    @property
    def name(self) -> str: ...
    @property
    def parent(self) -> BasePath: ...

def get_info_location(d: importlib.metadata.Distribution) -> BasePath | None:
    """Find the path to the distribution's metadata directory.

    HACK: This relies on importlib.metadata's private ``_path`` attribute. Not
    all distributions exist on disk, so importlib.metadata is correct to not
    expose the attribute as public. But pip's code base is old and not as clean,
    so we do this to avoid having to rewrite too many things. Hopefully we can
    eliminate this some day.
    """
def get_dist_name(dist: importlib.metadata.Distribution) -> str:
    """Get the distribution's project name.

    The ``name`` attribute is only available in Python 3.10 or later. We are
    targeting exactly that, but Mypy does not know this.
    """
