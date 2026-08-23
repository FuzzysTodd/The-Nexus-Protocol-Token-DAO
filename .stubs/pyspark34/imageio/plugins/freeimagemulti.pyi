from ..core import Format as Format, image_as_uint as image_as_uint
from ._freeimage import IO_FLAGS as IO_FLAGS, fi as fi
from .freeimage import FreeimageFormat as FreeimageFormat
from _typeshed import Incomplete

logger: Incomplete

class FreeimageMulti(FreeimageFormat):
    """Base class for freeimage formats that support multiple images."""
    class Reader(Format.Reader): ...
    class Writer(FreeimageFormat.Writer): ...

class MngFormat(FreeimageMulti):
    """An Mng format based on the Freeimage library.

    Read only. Seems broken.
    """

class IcoFormat(FreeimageMulti):
    """An ICO format based on the Freeimage library.

    This format supports grayscale, RGB and RGBA images.

    The freeimage plugin requires a `freeimage` binary. If this binary
    is not available on the system, it can be downloaded by either

    - the command line script ``imageio_download_bin freeimage``
    - the Python method ``imageio.plugins.freeimage.download()``

    Parameters for reading
    ----------------------
    makealpha : bool
        Convert to 32-bit and create an alpha channel from the AND-
        mask when loading. Default False. Note that this returns wrong
        results if the image was already RGBA.

    """
    class Reader(FreeimageMulti.Reader): ...

class GifFormat(FreeimageMulti):
    """A format for reading and writing static and animated GIF, based
    on the Freeimage library.

    Images read with this format are always RGBA. Currently,
    the alpha channel is ignored when saving RGB images with this
    format.

    The freeimage plugin requires a `freeimage` binary. If this binary
    is not available on the system, it can be downloaded by either

    - the command line script ``imageio_download_bin freeimage``
    - the Python method ``imageio.plugins.freeimage.download()``

    Parameters for reading
    ----------------------
    playback : bool
        'Play' the GIF to generate each frame (as 32bpp) instead of
        returning raw frame data when loading. Default True.

    Parameters for saving
    ---------------------
    loop : int
        The number of iterations. Default 0 (meaning loop indefinitely)
    duration : {float, list}
        The duration (in seconds) of each frame. Either specify one value
        that is used for all frames, or one value for each frame.
        Note that in the GIF format the duration/delay is expressed in
        hundredths of a second, which limits the precision of the duration.
    fps : float
        The number of frames per second. If duration is not given, the
        duration for each frame is set to 1/fps. Default 10.
    palettesize : int
        The number of colors to quantize the image to. Is rounded to
        the nearest power of two. Default 256.
    quantizer : {'wu', 'nq'}
        The quantization algorithm:
            * wu - Wu, Xiaolin, Efficient Statistical Computations for
              Optimal Color Quantization
            * nq (neuqant) - Dekker A. H., Kohonen neural networks for
              optimal color quantization
    subrectangles : bool
        If True, will try and optimize the GIF by storing only the
        rectangular parts of each frame that change with respect to the
        previous. Unfortunately, this option seems currently broken
        because FreeImage does not handle DisposalMethod correctly.
        Default False.
    """
    class Reader(FreeimageMulti.Reader): ...
    class Writer(FreeimageMulti.Writer): ...
