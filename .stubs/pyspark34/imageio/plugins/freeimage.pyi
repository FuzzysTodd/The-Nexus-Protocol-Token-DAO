from ..core import Format as Format, image_as_uint as image_as_uint
from ..core.request import RETURN_BYTES as RETURN_BYTES
from ._freeimage import FNAME_PER_PLATFORM as FNAME_PER_PLATFORM, IO_FLAGS as IO_FLAGS, download as download, fi as fi
from _typeshed import Incomplete

class FreeimageFormat(Format):
    """See :mod:`imageio.plugins.freeimage`"""
    def __init__(self, name, description, extensions: Incomplete | None = None, modes: Incomplete | None = None, *, fif: Incomplete | None = None) -> None: ...
    @property
    def fif(self): ...
    class Reader(Format.Reader): ...
    class Writer(Format.Writer): ...

class FreeimageBmpFormat(FreeimageFormat):
    """A BMP format based on the Freeimage library.

    This format supports grayscale, RGB and RGBA images.

    The freeimage plugin requires a `freeimage` binary. If this binary
    not available on the system, it can be downloaded manually from
    <https://github.com/imageio/imageio-binaries> by either

    - the command line script ``imageio_download_bin freeimage``
    - the Python method ``imageio.plugins.freeimage.download()``

    Parameters for saving
    ---------------------
    compression : bool
        Whether to compress the bitmap using RLE when saving. Default False.
        It seems this does not always work, but who cares, you should use
        PNG anyway.

    """
    class Writer(FreeimageFormat.Writer): ...

class FreeimagePngFormat(FreeimageFormat):
    """A PNG format based on the Freeimage library.

    This format supports grayscale, RGB and RGBA images.

    The freeimage plugin requires a `freeimage` binary. If this binary
    not available on the system, it can be downloaded manually from
    <https://github.com/imageio/imageio-binaries> by either

    - the command line script ``imageio_download_bin freeimage``
    - the Python method ``imageio.plugins.freeimage.download()``

    Parameters for reading
    ----------------------
    ignoregamma : bool
        Avoid gamma correction. Default True.

    Parameters for saving
    ---------------------
    compression : {0, 1, 6, 9}
        The compression factor. Higher factors result in more
        compression at the cost of speed. Note that PNG compression is
        always lossless. Default 9.
    quantize : int
        If specified, turn the given RGB or RGBA image in a paletted image
        for more efficient storage. The value should be between 2 and 256.
        If the value of 0 the image is not quantized.
    interlaced : bool
        Save using Adam7 interlacing. Default False.
    """
    class Reader(FreeimageFormat.Reader): ...
    class Writer(FreeimageFormat.Writer): ...

class FreeimageJpegFormat(FreeimageFormat):
    """A JPEG format based on the Freeimage library.

    This format supports grayscale and RGB images.

    The freeimage plugin requires a `freeimage` binary. If this binary
    not available on the system, it can be downloaded manually from
    <https://github.com/imageio/imageio-binaries> by either

    - the command line script ``imageio_download_bin freeimage``
    - the Python method ``imageio.plugins.freeimage.download()``

    Parameters for reading
    ----------------------
    exifrotate : bool
        Automatically rotate the image according to the exif flag.
        Default True. If 2 is given, do the rotation in Python instead
        of freeimage.
    quickread : bool
        Read the image more quickly, at the expense of quality.
        Default False.

    Parameters for saving
    ---------------------
    quality : scalar
        The compression factor of the saved image (1..100), higher
        numbers result in higher quality but larger file size. Default 75.
    progressive : bool
        Save as a progressive JPEG file (e.g. for images on the web).
        Default False.
    optimize : bool
        On saving, compute optimal Huffman coding tables (can reduce a
        few percent of file size). Default False.
    baseline : bool
        Save basic JPEG, without metadata or any markers. Default False.

    """
    class Reader(FreeimageFormat.Reader): ...
    class Writer(FreeimageFormat.Writer): ...

class FreeimagePnmFormat(FreeimageFormat):
    """A PNM format based on the Freeimage library.

    This format supports single bit (PBM), grayscale (PGM) and RGB (PPM)
    images, even with ASCII or binary coding.

    The freeimage plugin requires a `freeimage` binary. If this binary
    not available on the system, it can be downloaded manually from
    <https://github.com/imageio/imageio-binaries> by either

    - the command line script ``imageio_download_bin freeimage``
    - the Python method ``imageio.plugins.freeimage.download()``

    Parameters for saving
    ---------------------
    use_ascii : bool
        Save with ASCII coding. Default True.
    """
    class Writer(FreeimageFormat.Writer): ...
