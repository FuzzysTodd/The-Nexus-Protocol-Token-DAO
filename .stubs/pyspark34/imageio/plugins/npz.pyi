from ..core import Format as Format

class NpzFormat(Format):
    """See :mod:`imageio.plugins.npz`"""
    class Reader(Format.Reader): ...
    class Writer(Format.Writer):
        def set_meta_data(self, meta) -> None: ...
