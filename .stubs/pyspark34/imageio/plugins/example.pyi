from .. import formats as formats
from ..core import Format as Format
from _typeshed import Incomplete

class DummyFormat(Format):
    """The dummy format is an example format that does nothing.
    It will never indicate that it can read or write a file. When
    explicitly asked to read, it will simply read the bytes. When
    explicitly asked to write, it will raise an error.

    This documentation is shown when the user does ``help('thisformat')``.

    Parameters for reading
    ----------------------
    Specify arguments in numpy doc style here.

    Parameters for saving
    ---------------------
    Specify arguments in numpy doc style here.

    """
    class Reader(Format.Reader): ...
    class Writer(Format.Writer):
        def set_meta_data(self, meta) -> None: ...

format: Incomplete
