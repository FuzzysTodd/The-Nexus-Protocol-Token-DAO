from ..core import Format as Format
from ..v2 import imread as imread
from _typeshed import Incomplete

logger: Incomplete
LYTRO_ILLUM_IMAGE_SIZE: Incomplete
LYTRO_F01_IMAGE_SIZE: Incomplete
HEADER_LENGTH: int
SIZE_LENGTH: int
SHA1_LENGTH: int
PADDING_LENGTH: int
DATA_CHUNKS_ILLUM: int
DATA_CHUNKS_F01: int

class LytroFormat(Format):
    """Base class for Lytro format.
    The subclasses LytroLfrFormat, LytroLfpFormat, LytroIllumRawFormat and
    LytroF01RawFormat implement the Lytro-LFR, Lytro-LFP and Lytro-RAW format
    for the Illum and original F01 camera respectively.
    Writing is not supported.
    """
    class Writer(Format.Writer): ...

class LytroIllumRawFormat(LytroFormat):
    """This is the Lytro Illum RAW format.
    The raw format is a 10bit image format as used by the Lytro Illum
    light field camera. The format will read the specified raw file and will
    try to load a .txt or .json file with the associated meta data.
    This format does not support writing.


    Parameters for reading
    ----------------------
    meta_only : bool
        Whether to only read the metadata.
    """
    @staticmethod
    def rearrange_bits(array): ...
    class Reader(Format.Reader): ...

class LytroLfrFormat(LytroFormat):
    """This is the Lytro Illum LFR format.
    The lfr is a image and meta data container format as used by the
    Lytro Illum light field camera.
    The format will read the specified lfr file.
    This format does not support writing.

    Parameters for reading
    ----------------------
    meta_only : bool
        Whether to only read the metadata.
    include_thumbnail : bool
        Whether to include an image thumbnail in the metadata.
    """
    class Reader(Format.Reader): ...

class LytroF01RawFormat(LytroFormat):
    """This is the Lytro RAW format for the original F01 Lytro camera.
    The raw format is a 12bit image format as used by the Lytro F01
    light field camera. The format will read the specified raw file and will
    try to load a .txt or .json file with the associated meta data.
    This format does not support writing.


    Parameters for reading
    ----------------------
    meta_only : bool
        Whether to only read the metadata.

    """
    @staticmethod
    def rearrange_bits(array): ...
    class Reader(Format.Reader): ...

class LytroLfpFormat(LytroFormat):
    """This is the Lytro Illum LFP format.
    The lfp is a image and meta data container format as used by the
    Lytro F01 light field camera.
    The format will read the specified lfp file.
    This format does not support writing.

    Parameters for reading
    ----------------------
    meta_only : bool
        Whether to only read the metadata.
    include_thumbnail : bool
        Whether to include an image thumbnail in the metadata.
    """
    class Reader(Format.Reader): ...
