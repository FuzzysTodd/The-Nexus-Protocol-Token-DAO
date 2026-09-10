from .geo import AitoffAxes as AitoffAxes, HammerAxes as HammerAxes, LambertAxes as LambertAxes, MollweideAxes as MollweideAxes
from .polar import PolarAxes as PolarAxes
from _typeshed import Incomplete

class ProjectionRegistry:
    """A mapping of registered projection names to projection classes."""
    def __init__(self) -> None: ...
    def register(self, *projections) -> None:
        """Register a new set of projections."""
    def get_projection_class(self, name):
        """Get a projection class from its *name*."""
    def get_projection_names(self):
        """Return the names of all projections currently registered."""

projection_registry: Incomplete

def register_projection(cls) -> None: ...
def get_projection_class(projection: Incomplete | None = None):
    """
    Get a projection class from its name.

    If *projection* is None, a standard rectilinear projection is returned.
    """

get_projection_names: Incomplete
