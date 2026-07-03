from _typeshed import Incomplete
from nbconvert.utils.base import NbConvertBase as NbConvertBase

class WriterBase(NbConvertBase):
    """Consumes output from nbconvert export...() methods and writes to a
    useful location."""
    files: Incomplete
    def __init__(self, config: Incomplete | None = None, **kw) -> None:
        """
        Constructor
        """
    def write(self, output, resources, **kw) -> None:
        """
        Consume and write Jinja output.

        Parameters
        ----------
        output : string
            Conversion results.  This string contains the file contents of the
            converted file.
        resources : dict
            Resources created and filled by the nbconvert conversion process.
            Includes output from preprocessors, such as the extract figure
            preprocessor.
        """
