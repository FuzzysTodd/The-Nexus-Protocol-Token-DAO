from nbconvert.utils.base import NbConvertBase

__all__ = ['DataTypeFilter']

class DataTypeFilter(NbConvertBase):
    """Returns the preferred display format"""
    def __call__(self, output):
        """Return the first available format in the priority.

        Produces a UserWarning if no compatible mimetype is found.

        `output` is dict with structure {mimetype-of-element: value-of-element}

        """
