from _typeshed import Incomplete

logger: Incomplete

class BitArray:
    """Dynamic array of bits that automatically resizes
    with factors of two.
    Append bits using .append() or +=
    You can reverse bits using .reverse()
    """
    data: Incomplete
    def __init__(self, initvalue: Incomplete | None = None) -> None: ...
    def __len__(self) -> int: ...
    def __add__(self, value): ...
    def append(self, bits) -> None: ...
    def reverse(self) -> None:
        """In-place reverse."""
    def tobytes(self):
        """Convert to bytes. If necessary,
        zeros are padded to the end (right side).
        """

def int2uint32(i): ...
def int2uint16(i): ...
def int2uint8(i): ...
def int2bits(i, n: Incomplete | None = None):
    """convert int to a string of bits (0's and 1's in a string),
    pad to n elements. Convert back using int(ss,2)."""
def bits2int(bb, n: int = 8): ...
def get_type_and_len(bb):
    """bb should be 6 bytes at least
    Return (type, length, length_of_full_tag)
    """
def signedint2bits(i, n: Incomplete | None = None):
    """convert signed int to a string of bits (0's and 1's in a string),
    pad to n elements. Negative numbers are stored in 2's complement bit
    patterns, thus positive numbers always start with a 0.
    """
def twits2bits(arr):
    """Given a few (signed) numbers, store them
    as compactly as possible in the wat specifief by the swf format.
    The numbers are multiplied by 20, assuming they
    are twits.
    Can be used to make the RECT record.
    """
def floats2bits(arr):
    """Given a few (signed) numbers, convert them to bits,
    stored as FB (float bit values). We always use 16.16.
    Negative numbers are not (yet) possible, because I don't
    know how the're implemented (ambiguity).
    """

class Tag:
    bytes: Incomplete
    tagtype: int
    def __init__(self) -> None: ...
    def process_tag(self) -> None:
        """Implement this to create the tag."""
    def get_tag(self):
        """Calls processTag and attaches the header."""
    def make_rect_record(self, xmin, xmax, ymin, ymax):
        """Simply uses makeCompactArray to produce
        a RECT Record."""
    def make_matrix_record(self, scale_xy: Incomplete | None = None, rot_xy: Incomplete | None = None, trans_xy: Incomplete | None = None): ...

class ControlTag(Tag):
    def __init__(self) -> None: ...

class FileAttributesTag(ControlTag):
    tagtype: int
    def __init__(self) -> None: ...
    bytes: Incomplete
    def process_tag(self) -> None: ...

class ShowFrameTag(ControlTag):
    tagtype: int
    def __init__(self) -> None: ...
    bytes: Incomplete
    def process_tag(self) -> None: ...

class SetBackgroundTag(ControlTag):
    """Set the color in 0-255, or 0-1 (if floats given)."""
    tagtype: int
    rgb: Incomplete
    def __init__(self, *rgb) -> None: ...
    bytes: Incomplete
    def process_tag(self) -> None: ...

class DoActionTag(Tag):
    tagtype: int
    actions: Incomplete
    def __init__(self, action: str = 'stop') -> None: ...
    def append(self, action) -> None: ...
    bytes: Incomplete
    def process_tag(self) -> None: ...

class DefinitionTag(Tag):
    counter: int
    id: Incomplete
    def __init__(self) -> None: ...

class BitmapTag(DefinitionTag):
    tagtype: int
    imshape: Incomplete
    def __init__(self, im) -> None: ...
    bytes: Incomplete
    def process_tag(self) -> None: ...

class PlaceObjectTag(ControlTag):
    tagtype: int
    depth: Incomplete
    idToPlace: Incomplete
    xy: Incomplete
    move: Incomplete
    def __init__(self, depth, idToPlace: Incomplete | None = None, xy=(0, 0), move: bool = False) -> None: ...
    bytes: Incomplete
    def process_tag(self) -> None: ...

class ShapeTag(DefinitionTag):
    tagtype: int
    bitmapId: Incomplete
    xy: Incomplete
    wh: Incomplete
    def __init__(self, bitmapId, xy, wh) -> None: ...
    bytes: Incomplete
    def process_tag(self) -> None:
        """Returns a defineshape tag. with a bitmap fill"""
    def make_style_change_record(self, lineStyle: Incomplete | None = None, fillStyle: Incomplete | None = None, moveTo: Incomplete | None = None): ...
    def make_straight_edge_record(self, *dxdy): ...
    def make_end_shape_record(self): ...

def read_pixels(bb, i, tagType, L1):
    """With pf's seed after the recordheader, reads the pixeldata."""
def checkImages(images):
    """checkImages(images)
    Check numpy images and correct intensity range etc.
    The same for all movie formats.
    """
def build_file(fp, taglist, nframes: int = 1, framesize=(500, 500), fps: int = 10, version: int = 8) -> None:
    """Give the given file (as bytes) a header."""
def write_swf(filename, images, duration: float = 0.1, repeat: bool = True) -> None:
    """Write an swf-file from the specified images. If repeat is False,
    the movie is finished with a stop action. Duration may also
    be a list with durations for each frame (note that the duration
    for each frame is always an integer amount of the minimum duration.)

    Images should be a list consisting numpy arrays with values between
    0 and 255 for integer types, and between 0 and 1 for float types.

    """
def read_swf(filename):
    """Read all images from an SWF (shockwave flash) file. Returns a list
    of numpy arrays.

    Limitation: only read the PNG encoded images (not the JPG encoded ones).
    """
writeSwf = write_swf
readSwf = read_swf
