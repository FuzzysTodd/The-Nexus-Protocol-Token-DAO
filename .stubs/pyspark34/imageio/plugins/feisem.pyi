from .tifffile import TiffFormat as TiffFormat

class FEISEMFormat(TiffFormat):
    """See :mod:`imageio.plugins.feisem`"""
    class Reader(TiffFormat.Reader): ...
