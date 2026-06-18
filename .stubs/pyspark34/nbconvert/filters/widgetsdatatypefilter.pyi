from _typeshed import Incomplete
from nbconvert.utils.base import NbConvertBase

__all__ = ['WidgetsDataTypeFilter']

class WidgetsDataTypeFilter(NbConvertBase):
    """Returns the preferred display format, excluding the widget output if
    there is no widget state available"""
    metadata: Incomplete
    notebook_path: str
    def __init__(self, notebook_metadata: Incomplete | None = None, resources: Incomplete | None = None, **kwargs) -> None:
        """Initialize the filter."""
    def __call__(self, output):
        """Return the first available format in the priority.

        Produces a UserWarning if no compatible mimetype is found.

        `output` is dict with structure {mimetype-of-element: value-of-element}

        """
