from . import Image as Image
from _typeshed import Incomplete

LUT_SIZE: Incomplete
ROTATION_MATRIX: Incomplete
MIRROR_MATRIX: Incomplete

class LutBuilder:
    '''A class for building a MorphLut from a descriptive language

    The input patterns is a list of a strings sequences like these::

        4:(...
           .1.
           111)->1

    (whitespaces including linebreaks are ignored). The option 4
    describes a series of symmetry operations (in this case a
    4-rotation), the pattern is described by:

    - . or X - Ignore
    - 1 - Pixel is on
    - 0 - Pixel is off

    The result of the operation is described after "->" string.

    The default is to return the current pixel value, which is
    returned if no other match is found.

    Operations:

    - 4 - 4 way rotation
    - N - Negate
    - 1 - Dummy op for no other operation (an op must always be given)
    - M - Mirroring

    Example::

        lb = LutBuilder(patterns = ["4:(... .1. 111)->1"])
        lut = lb.build_lut()

    '''
    patterns: Incomplete
    lut: Incomplete
    def __init__(self, patterns: Incomplete | None = None, op_name: Incomplete | None = None) -> None: ...
    def add_patterns(self, patterns) -> None: ...
    def build_default_lut(self) -> None: ...
    def get_lut(self): ...
    def build_lut(self):
        """Compile all patterns into a morphology lut.

        TBD :Build based on (file) morphlut:modify_lut
        """

class MorphOp:
    """A class for binary morphological operators"""
    lut: Incomplete
    def __init__(self, lut: Incomplete | None = None, op_name: Incomplete | None = None, patterns: Incomplete | None = None) -> None:
        """Create a binary morphological operator"""
    def apply(self, image):
        """Run a single morphological operation on an image

        Returns a tuple of the number of changed pixels and the
        morphed image"""
    def match(self, image):
        """Get a list of coordinates matching the morphological operation on
        an image.

        Returns a list of tuples of (x,y) coordinates
        of all matching pixels. See :ref:`coordinate-system`."""
    def get_on_pixels(self, image):
        """Get a list of all turned on pixels in a binary image

        Returns a list of tuples of (x,y) coordinates
        of all matching pixels. See :ref:`coordinate-system`."""
    def load_lut(self, filename) -> None:
        """Load an operator from an mrl file"""
    def save_lut(self, filename) -> None:
        """Save an operator to an mrl file"""
    def set_lut(self, lut) -> None:
        """Set the lut from an external source"""
