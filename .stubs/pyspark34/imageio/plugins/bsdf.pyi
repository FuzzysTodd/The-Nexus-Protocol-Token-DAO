from ..core import Format as Format
from _typeshed import Incomplete

def get_bsdf_serializer(options): ...

class Image:
    """Class in which we wrap the array and meta data. By using an extension
    we can make BSDF trigger on these classes and thus encode the images.
    as actual images.
    """
    array: Incomplete
    meta: Incomplete
    def __init__(self, array, meta) -> None: ...
    def get_array(self): ...
    def get_meta(self): ...

class Image2D(Image): ...
class Image3D(Image): ...

class BsdfFormat(Format):
    '''The BSDF format enables reading and writing of image data in the
    BSDF serialization format. This format allows storage of images, volumes,
    and series thereof. Data can be of any numeric data type, and can
    optionally be compressed. Each image/volume can have associated
    meta data, which can consist of any data type supported by BSDF.

    By default, image data is lazily loaded; the actual image data is
    not read until it is requested. This allows storing multiple images
    in a single file and still have fast access to individual images.
    Alternatively, a series of images can be read in streaming mode, reading
    images as they are read (e.g. from http).

    BSDF is a simple generic binary format. It is easy to extend and there
    are standard extension definitions for 2D and 3D image data.
    Read more at http://bsdf.io.

    Parameters for reading
    ----------------------
    random_access : bool
        Whether individual images in the file can be read in random order.
        Defaults to True for normal files, and to False when reading from HTTP.
        If False, the file is read in "streaming mode", allowing reading
        files as they are read, but without support for "rewinding".
        Note that setting this to True when reading from HTTP, the whole file
        is read upon opening it (since lazy loading is not possible over HTTP).

    Parameters for saving
    ---------------------
    compression : {0, 1, 2}
        Use ``0`` or "no" for no compression, ``1`` or "zlib" for Zlib
        compression (same as zip files and PNG), and ``2`` or "bz2" for Bz2
        compression (more compact but slower). Default 1 (zlib).
        Note that some BSDF implementations may not support compression
        (e.g. JavaScript).

    '''
    class Reader(Format.Reader): ...
    class Writer(Format.Writer):
        def set_meta_data(self, meta) -> None: ...
