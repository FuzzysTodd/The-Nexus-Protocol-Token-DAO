from .base import WriterBase as WriterBase
from nbconvert.utils import io as io

class StdoutWriter(WriterBase):
    """Consumes output from nbconvert export...() methods and writes to the
    stdout stream."""
    def write(self, output, resources, **kw) -> None:
        """
        Consume and write Jinja output.

        See base for more...
        """
