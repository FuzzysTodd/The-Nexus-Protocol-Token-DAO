from . import ExifTags as ExifTags, Image as Image, ImageFile as ImageFile, ImageOps as ImageOps, ImagePalette as ImagePalette, TiffTags as TiffTags
from .TiffTags import TYPES as TYPES
from ._binary import o8 as o8
from _typeshed import Incomplete
from collections.abc import MutableMapping
from numbers import Rational

logger: Incomplete
READ_LIBTIFF: bool
WRITE_LIBTIFF: bool
IFD_LEGACY_API: bool
STRIP_SIZE: int
II: bytes
MM: bytes
IMAGEWIDTH: int
IMAGELENGTH: int
BITSPERSAMPLE: int
COMPRESSION: int
PHOTOMETRIC_INTERPRETATION: int
FILLORDER: int
IMAGEDESCRIPTION: int
STRIPOFFSETS: int
SAMPLESPERPIXEL: int
ROWSPERSTRIP: int
STRIPBYTECOUNTS: int
X_RESOLUTION: int
Y_RESOLUTION: int
PLANAR_CONFIGURATION: int
RESOLUTION_UNIT: int
TRANSFERFUNCTION: int
SOFTWARE: int
DATE_TIME: int
ARTIST: int
PREDICTOR: int
COLORMAP: int
TILEWIDTH: int
TILELENGTH: int
TILEOFFSETS: int
TILEBYTECOUNTS: int
SUBIFD: int
EXTRASAMPLES: int
SAMPLEFORMAT: int
JPEGTABLES: int
YCBCRSUBSAMPLING: int
REFERENCEBLACKWHITE: int
COPYRIGHT: int
IPTC_NAA_CHUNK: int
PHOTOSHOP_CHUNK: int
ICCPROFILE: int
EXIFIFD: int
XMP: int
JPEGQUALITY: int
IMAGEJ_META_DATA_BYTE_COUNTS: int
IMAGEJ_META_DATA: int
COMPRESSION_INFO: Incomplete
COMPRESSION_INFO_REV: Incomplete
OPEN_INFO: Incomplete
MAX_SAMPLESPERPIXEL: Incomplete
PREFIXES: Incomplete

class IFDRational(Rational):
    """Implements a rational class where 0/0 is a legal value to match
    the in the wild use of exif rationals.

    e.g., DigitalZoomRatio - 0.00/0.00  indicates that no digital zoom was used
    """
    def __init__(self, value, denominator: int = 1) -> None:
        """
        :param value: either an integer numerator, a
        float/rational/other number, or an IFDRational
        :param denominator: Optional integer denominator
        """
    @property
    def numerator(self): ...
    @property
    def denominator(self): ...
    def limit_rational(self, max_denominator):
        """

        :param max_denominator: Integer, the maximum denominator value
        :returns: Tuple of (numerator, denominator)
        """
    def __hash__(self): ...
    def __eq__(self, other): ...
    __add__: Incomplete
    __radd__: Incomplete
    __sub__: Incomplete
    __rsub__: Incomplete
    __mul__: Incomplete
    __rmul__: Incomplete
    __truediv__: Incomplete
    __rtruediv__: Incomplete
    __floordiv__: Incomplete
    __rfloordiv__: Incomplete
    __mod__: Incomplete
    __rmod__: Incomplete
    __pow__: Incomplete
    __rpow__: Incomplete
    __pos__: Incomplete
    __neg__: Incomplete
    __abs__: Incomplete
    __trunc__: Incomplete
    __lt__: Incomplete
    __gt__: Incomplete
    __le__: Incomplete
    __ge__: Incomplete
    __bool__: Incomplete
    __ceil__: Incomplete
    __floor__: Incomplete
    __round__: Incomplete
    __int__: Incomplete

class ImageFileDirectory_v2(MutableMapping):
    """This class represents a TIFF tag directory.  To speed things up, we
    don't decode tags unless they're asked for.

    Exposes a dictionary interface of the tags in the directory::

        ifd = ImageFileDirectory_v2()
        ifd[key] = 'Some Data'
        ifd.tagtype[key] = TiffTags.ASCII
        print(ifd[key])
        'Some Data'

    Individual values are returned as the strings or numbers, sequences are
    returned as tuples of the values.

    The tiff metadata type of each item is stored in a dictionary of
    tag types in
    :attr:`~PIL.TiffImagePlugin.ImageFileDirectory_v2.tagtype`. The types
    are read from a tiff file, guessed from the type added, or added
    manually.

    Data Structures:

        * ``self.tagtype = {}``

          * Key: numerical TIFF tag number
          * Value: integer corresponding to the data type from
            :py:data:`.TiffTags.TYPES`

          .. versionadded:: 3.0.0

    'Internal' data structures:

        * ``self._tags_v2 = {}``

          * Key: numerical TIFF tag number
          * Value: decoded data, as tuple for multiple values

        * ``self._tagdata = {}``

          * Key: numerical TIFF tag number
          * Value: undecoded byte string from file

        * ``self._tags_v1 = {}``

          * Key: numerical TIFF tag number
          * Value: decoded data in the v1 format

    Tags will be found in the private attributes ``self._tagdata``, and in
    ``self._tags_v2`` once decoded.

    ``self.legacy_api`` is a value for internal use, and shouldn't be changed
    from outside code. In cooperation with
    :py:class:`~PIL.TiffImagePlugin.ImageFileDirectory_v1`, if ``legacy_api``
    is true, then decoded tags will be populated into both ``_tags_v1`` and
    ``_tags_v2``. ``_tags_v2`` will be used if this IFD is used in the TIFF
    save routine. Tags should be read from ``_tags_v1`` if
    ``legacy_api == true``.

    """
    group: Incomplete
    tagtype: Incomplete
    def __init__(self, ifh: bytes = b'II*\x00\x00\x00\x00\x00', prefix: Incomplete | None = None, group: Incomplete | None = None) -> None:
        """Initialize an ImageFileDirectory.

        To construct an ImageFileDirectory from a real file, pass the 8-byte
        magic header to the constructor.  To only set the endianness, pass it
        as the 'prefix' keyword argument.

        :param ifh: One of the accepted magic headers (cf. PREFIXES); also sets
              endianness.
        :param prefix: Override the endianness of the file.
        """
    prefix: Incomplete
    offset: Incomplete
    legacy_api: Incomplete
    @legacy_api.setter
    def legacy_api(self, value) -> None: ...
    def reset(self) -> None: ...
    def named(self):
        """
        :returns: dict of name|key: value

        Returns the complete tag dictionary, with named tags where possible.
        """
    def __len__(self) -> int: ...
    def __getitem__(self, tag): ...
    def __contains__(self, tag) -> bool: ...
    def __setitem__(self, tag, value) -> None: ...
    def __delitem__(self, tag) -> None: ...
    def __iter__(self): ...
    def load_byte(self, data, legacy_api: bool = True): ...
    def write_byte(self, data): ...
    def load_string(self, data, legacy_api: bool = True): ...
    def write_string(self, value): ...
    def load_rational(self, data, legacy_api: bool = True): ...
    def write_rational(self, *values): ...
    def load_undefined(self, data, legacy_api: bool = True): ...
    def write_undefined(self, value): ...
    def load_signed_rational(self, data, legacy_api: bool = True): ...
    def write_signed_rational(self, *values): ...
    def load(self, fp) -> None: ...
    def tobytes(self, offset: int = 0): ...
    def save(self, fp): ...

name: Incomplete

class ImageFileDirectory_v1(ImageFileDirectory_v2):
    """This class represents the **legacy** interface to a TIFF tag directory.

    Exposes a dictionary interface of the tags in the directory::

        ifd = ImageFileDirectory_v1()
        ifd[key] = 'Some Data'
        ifd.tagtype[key] = TiffTags.ASCII
        print(ifd[key])
        ('Some Data',)

    Also contains a dictionary of tag types as read from the tiff image file,
    :attr:`~PIL.TiffImagePlugin.ImageFileDirectory_v1.tagtype`.

    Values are returned as a tuple.

    ..  deprecated:: 3.0.0
    """
    def __init__(self, *args, **kwargs) -> None: ...
    tags: Incomplete
    tagdata: Incomplete
    tagtype: dict
    @classmethod
    def from_v2(cls, original):
        """Returns an
        :py:class:`~PIL.TiffImagePlugin.ImageFileDirectory_v1`
        instance with the same data as is contained in the original
        :py:class:`~PIL.TiffImagePlugin.ImageFileDirectory_v2`
        instance.

        :returns: :py:class:`~PIL.TiffImagePlugin.ImageFileDirectory_v1`

        """
    def to_v2(self):
        """Returns an
        :py:class:`~PIL.TiffImagePlugin.ImageFileDirectory_v2`
        instance with the same data as is contained in the original
        :py:class:`~PIL.TiffImagePlugin.ImageFileDirectory_v1`
        instance.

        :returns: :py:class:`~PIL.TiffImagePlugin.ImageFileDirectory_v2`

        """
    def __contains__(self, tag) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __setitem__(self, tag, value) -> None: ...
    def __getitem__(self, tag): ...
ImageFileDirectory = ImageFileDirectory_v1

class TiffImageFile(ImageFile.ImageFile):
    format: str
    format_description: str
    tag_v2: Incomplete
    tag: Incomplete
    def __init__(self, fp: Incomplete | None = None, filename: Incomplete | None = None) -> None: ...
    @property
    def n_frames(self): ...
    im: Incomplete
    def seek(self, frame) -> None:
        """Select a given frame as current image"""
    def tell(self):
        """Return the current frame number"""
    def getxmp(self):
        """
        Returns a dictionary containing the XMP tags.
        Requires defusedxml to be installed.

        :returns: XMP tags in a dictionary.
        """
    def get_photoshop_blocks(self):
        '''
        Returns a dictionary of Photoshop "Image Resource Blocks".
        The keys are the image resource ID. For more information, see
        https://www.adobe.com/devnet-apps/photoshop/fileformatashtml/#50577409_pgfId-1037727

        :returns: Photoshop "Image Resource Blocks" in a dictionary.
        '''
    def load(self): ...
    def load_end(self) -> None: ...

SAVE_INFO: Incomplete

class AppendingTiffWriter:
    fieldSizes: Incomplete
    Tags: Incomplete
    f: Incomplete
    close_fp: bool
    name: Incomplete
    beginning: Incomplete
    def __init__(self, fn, new: bool = False) -> None: ...
    whereToWriteNewIFDOffset: Incomplete
    offsetOfNewPage: int
    IIMM: Incomplete
    isFirst: bool
    def setup(self) -> None: ...
    def finalize(self) -> None: ...
    def newFrame(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None): ...
    def tell(self): ...
    def seek(self, offset, whence=...): ...
    def goToEnd(self) -> None: ...
    endian: Incomplete
    longFmt: Incomplete
    shortFmt: Incomplete
    tagFormat: Incomplete
    def setEndian(self, endian) -> None: ...
    def skipIFDs(self) -> None: ...
    def write(self, data): ...
    def readShort(self): ...
    def readLong(self): ...
    def rewriteLastShortToLong(self, value) -> None: ...
    def rewriteLastShort(self, value) -> None: ...
    def rewriteLastLong(self, value) -> None: ...
    def writeShort(self, value) -> None: ...
    def writeLong(self, value) -> None: ...
    def close(self) -> None: ...
    def fixIFD(self) -> None: ...
    def fixOffsets(self, count, isShort: bool = False, isLong: bool = False) -> None: ...
