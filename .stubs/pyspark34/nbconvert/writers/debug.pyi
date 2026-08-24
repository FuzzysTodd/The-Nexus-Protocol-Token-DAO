from .base import WriterBase as WriterBase

class DebugWriter(WriterBase):
    """Consumes output from nbconvert export...() methods and writes useful
    debugging information to the stdout.  The information includes a list of
    resources that were extracted from the notebook(s) during export."""
    def write(self, output, resources, notebook_name: str = 'notebook', **kw) -> None:
        """
        Consume and write Jinja output.

        See base for more...
        """
