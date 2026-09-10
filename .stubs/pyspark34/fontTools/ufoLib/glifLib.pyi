import enum
from _typeshed import Incomplete
from fontTools.pens.pointPen import AbstractPointPen
from fontTools.ufoLib import _UFOBaseIO
from fontTools.ufoLib.errors import GlifLibError as GlifLibError
from fontTools.ufoLib.utils import _VersionTupleEnumMixin

__all__ = ['GlyphSet', 'GlifLibError', 'readGlyphFromString', 'writeGlyphToString', 'glyphNameToFileName']

class GLIFFormatVersion(tuple, _VersionTupleEnumMixin, enum.Enum):
    FORMAT_1_0: Incomplete
    FORMAT_2_0: Incomplete
    @classmethod
    def default(cls, ufoFormatVersion: Incomplete | None = None): ...
    @classmethod
    def supported_versions(cls, ufoFormatVersion: Incomplete | None = None): ...

class Glyph:
    """
    Minimal glyph object. It has no glyph attributes until either
    the draw() or the drawPoints() method has been called.
    """
    glyphName: Incomplete
    glyphSet: Incomplete
    def __init__(self, glyphName, glyphSet) -> None: ...
    def draw(self, pen, outputImpliedClosingLine: bool = False) -> None:
        """
        Draw this glyph onto a *FontTools* Pen.
        """
    def drawPoints(self, pointPen) -> None:
        """
        Draw this glyph onto a PointPen.
        """

class GlyphSet(_UFOBaseIO):
    """
    GlyphSet manages a set of .glif files inside one directory.

    GlyphSet's constructor takes a path to an existing directory as it's
    first argument. Reading glyph data can either be done through the
    readGlyph() method, or by using GlyphSet's dictionary interface, where
    the keys are glyph names and the values are (very) simple glyph objects.

    To write a glyph to the glyph set, you use the writeGlyph() method.
    The simple glyph objects returned through the dict interface do not
    support writing, they are just a convenient way to get at the glyph data.
    """
    glyphClass = Glyph
    dirName: Incomplete
    fs: Incomplete
    ufoFormatVersion: Incomplete
    ufoFormatVersionTuple: Incomplete
    glyphNameToFileName: Incomplete
    def __init__(self, path, glyphNameToFileNameFunc: Incomplete | None = None, ufoFormatVersion: Incomplete | None = None, validateRead: bool = True, validateWrite: bool = True, expectContentsFile: bool = False) -> None:
        """
        'path' should be a path (string) to an existing local directory, or
        an instance of fs.base.FS class.

        The optional 'glyphNameToFileNameFunc' argument must be a callback
        function that takes two arguments: a glyph name and a list of all
        existing filenames (if any exist). It should return a file name
        (including the .glif extension). The glyphNameToFileName function
        is called whenever a file name is created for a given glyph name.

        ``validateRead`` will validate read operations. Its default is ``True``.
        ``validateWrite`` will validate write operations. Its default is ``True``.
        ``expectContentsFile`` will raise a GlifLibError if a contents.plist file is
        not found on the glyph set file system. This should be set to ``True`` if you
        are reading an existing UFO and ``False`` if you create a fresh\tglyph set.
        """
    contents: Incomplete
    def rebuildContents(self, validateRead: Incomplete | None = None) -> None:
        """
        Rebuild the contents dict by loading contents.plist.

        ``validateRead`` will validate the data, by default it is set to the
        class's ``validateRead`` value, can be overridden.
        """
    def getReverseContents(self):
        """
        Return a reversed dict of self.contents, mapping file names to
        glyph names. This is primarily an aid for custom glyph name to file
        name schemes that want to make sure they don't generate duplicate
        file names. The file names are converted to lowercase so we can
        reliably check for duplicates that only differ in case, which is
        important for case-insensitive file systems.
        """
    def writeContents(self) -> None:
        """
        Write the contents.plist file out to disk. Call this method when
        you're done writing glyphs.
        """
    def readLayerInfo(self, info, validateRead: Incomplete | None = None) -> None:
        """
        ``validateRead`` will validate the data, by default it is set to the
        class's ``validateRead`` value, can be overridden.
        """
    def writeLayerInfo(self, info, validateWrite: Incomplete | None = None) -> None:
        """
        ``validateWrite`` will validate the data, by default it is set to the
        class's ``validateWrite`` value, can be overridden.
        """
    def getGLIF(self, glyphName):
        """
        Get the raw GLIF text for a given glyph name. This only works
        for GLIF files that are already on disk.

        This method is useful in situations when the raw XML needs to be
        read from a glyph set for a particular glyph before fully parsing
        it into an object structure via the readGlyph method.

        Raises KeyError if 'glyphName' is not in contents.plist, or
        GlifLibError if the file associated with can't be found.
        """
    def getGLIFModificationTime(self, glyphName):
        """
        Returns the modification time for the GLIF file with 'glyphName', as
        a floating point number giving the number of seconds since the epoch.
        Return None if the associated file does not exist or the underlying
        filesystem does not support getting modified times.
        Raises KeyError if the glyphName is not in contents.plist.
        """
    def readGlyph(self, glyphName, glyphObject: Incomplete | None = None, pointPen: Incomplete | None = None, validate: Incomplete | None = None) -> None:
        """
        Read a .glif file for 'glyphName' from the glyph set. The
        'glyphObject' argument can be any kind of object (even None);
        the readGlyph() method will attempt to set the following
        attributes on it:

        width
                the advance width of the glyph
        height
                the advance height of the glyph
        unicodes
                a list of unicode values for this glyph
        note
                a string
        lib
                a dictionary containing custom data
        image
                a dictionary containing image data
        guidelines
                a list of guideline data dictionaries
        anchors
                a list of anchor data dictionaries

        All attributes are optional, in two ways:

        1) An attribute *won't* be set if the .glif file doesn't
           contain data for it. 'glyphObject' will have to deal
           with default values itself.
        2) If setting the attribute fails with an AttributeError
           (for example if the 'glyphObject' attribute is read-
           only), readGlyph() will not propagate that exception,
           but ignore that attribute.

        To retrieve outline information, you need to pass an object
        conforming to the PointPen protocol as the 'pointPen' argument.
        This argument may be None if you don't need the outline data.

        readGlyph() will raise KeyError if the glyph is not present in
        the glyph set.

        ``validate`` will validate the data, by default it is set to the
        class's ``validateRead`` value, can be overridden.
        """
    def writeGlyph(self, glyphName, glyphObject: Incomplete | None = None, drawPointsFunc: Incomplete | None = None, formatVersion: Incomplete | None = None, validate: Incomplete | None = None) -> None:
        """
        Write a .glif file for 'glyphName' to the glyph set. The
        'glyphObject' argument can be any kind of object (even None);
        the writeGlyph() method will attempt to get the following
        attributes from it:

        width
                the advance width of the glyph
        height
                the advance height of the glyph
        unicodes
                a list of unicode values for this glyph
        note
                a string
        lib
                a dictionary containing custom data
        image
                a dictionary containing image data
        guidelines
                a list of guideline data dictionaries
        anchors
                a list of anchor data dictionaries

        All attributes are optional: if 'glyphObject' doesn't
        have the attribute, it will simply be skipped.

        To write outline data to the .glif file, writeGlyph() needs
        a function (any callable object actually) that will take one
        argument: an object that conforms to the PointPen protocol.
        The function will be called by writeGlyph(); it has to call the
        proper PointPen methods to transfer the outline to the .glif file.

        The GLIF format version will be chosen based on the ufoFormatVersion
        passed during the creation of this object. If a particular format
        version is desired, it can be passed with the formatVersion argument.
        The formatVersion argument accepts either a tuple of integers for
        (major, minor), or a single integer for the major digit only (with
        minor digit implied as 0).

        An UnsupportedGLIFFormat exception is raised if the requested GLIF
        formatVersion is not supported.

        ``validate`` will validate the data, by default it is set to the
        class's ``validateWrite`` value, can be overridden.
        """
    def deleteGlyph(self, glyphName) -> None:
        """Permanently delete the glyph from the glyph set on disk. Will
        raise KeyError if the glyph is not present in the glyph set.
        """
    def keys(self): ...
    def has_key(self, glyphName): ...
    __contains__ = has_key
    def __len__(self) -> int: ...
    def __getitem__(self, glyphName): ...
    def getUnicodes(self, glyphNames: Incomplete | None = None):
        """
        Return a dictionary that maps glyph names to lists containing
        the unicode value[s] for that glyph, if any. This parses the .glif
        files partially, so it is a lot faster than parsing all files completely.
        By default this checks all glyphs, but a subset can be passed with glyphNames.
        """
    def getComponentReferences(self, glyphNames: Incomplete | None = None):
        """
        Return a dictionary that maps glyph names to lists containing the
        base glyph name of components in the glyph. This parses the .glif
        files partially, so it is a lot faster than parsing all files completely.
        By default this checks all glyphs, but a subset can be passed with glyphNames.
        """
    def getImageReferences(self, glyphNames: Incomplete | None = None):
        """
        Return a dictionary that maps glyph names to the file name of the image
        referenced by the glyph. This parses the .glif files partially, so it is a
        lot faster than parsing all files completely.
        By default this checks all glyphs, but a subset can be passed with glyphNames.
        """
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

def glyphNameToFileName(glyphName, existingFileNames):
    """
    Wrapper around the userNameToFileName function in filenames.py

    Note that existingFileNames should be a set for large glyphsets
    or performance will suffer.
    """
def readGlyphFromString(aString, glyphObject: Incomplete | None = None, pointPen: Incomplete | None = None, formatVersions: Incomplete | None = None, validate: bool = True) -> None:
    """
    Read .glif data from a string into a glyph object.

    The 'glyphObject' argument can be any kind of object (even None);
    the readGlyphFromString() method will attempt to set the following
    attributes on it:

    width
            the advance width of the glyph
    height
            the advance height of the glyph
    unicodes
            a list of unicode values for this glyph
    note
            a string
    lib
            a dictionary containing custom data
    image
            a dictionary containing image data
    guidelines
            a list of guideline data dictionaries
    anchors
            a list of anchor data dictionaries

    All attributes are optional, in two ways:

    1) An attribute *won't* be set if the .glif file doesn't
       contain data for it. 'glyphObject' will have to deal
       with default values itself.
    2) If setting the attribute fails with an AttributeError
       (for example if the 'glyphObject' attribute is read-
       only), readGlyphFromString() will not propagate that
       exception, but ignore that attribute.

    To retrieve outline information, you need to pass an object
    conforming to the PointPen protocol as the 'pointPen' argument.
    This argument may be None if you don't need the outline data.

    The formatVersions optional argument define the GLIF format versions
    that are allowed to be read.
    The type is Optional[Iterable[Tuple[int, int], int]]. It can contain
    either integers (for the major versions to be allowed, with minor
    digits defaulting to 0), or tuples of integers to specify both
    (major, minor) versions.
    By default when formatVersions is None all the GLIF format versions
    currently defined are allowed to be read.

    ``validate`` will validate the read data. It is set to ``True`` by default.
    """
def writeGlyphToString(glyphName, glyphObject: Incomplete | None = None, drawPointsFunc: Incomplete | None = None, formatVersion: Incomplete | None = None, validate: bool = True):
    '''
    Return .glif data for a glyph as a string. The XML declaration\'s
    encoding is always set to "UTF-8".
    The \'glyphObject\' argument can be any kind of object (even None);
    the writeGlyphToString() method will attempt to get the following
    attributes from it:

    width
            the advance width of the glyph
    height
            the advance height of the glyph
    unicodes
            a list of unicode values for this glyph
    note
            a string
    lib
            a dictionary containing custom data
    image
            a dictionary containing image data
    guidelines
            a list of guideline data dictionaries
    anchors
            a list of anchor data dictionaries

    All attributes are optional: if \'glyphObject\' doesn\'t
    have the attribute, it will simply be skipped.

    To write outline data to the .glif file, writeGlyphToString() needs
    a function (any callable object actually) that will take one
    argument: an object that conforms to the PointPen protocol.
    The function will be called by writeGlyphToString(); it has to call the
    proper PointPen methods to transfer the outline to the .glif file.

    The GLIF format version can be specified with the formatVersion argument.
    This accepts either a tuple of integers for (major, minor), or a single
    integer for the major digit only (with minor digit implied as 0).
    By default when formatVesion is None the latest GLIF format version will
    be used; currently it\'s 2.0, which is equivalent to formatVersion=(2, 0).

    An UnsupportedGLIFFormat exception is raised if the requested UFO
    formatVersion is not supported.

    ``validate`` will validate the written data. It is set to ``True`` by default.
    '''

class _DoneParsing(Exception): ...

class _BaseParser:
    def __init__(self) -> None: ...
    def parse(self, text) -> None: ...
    def startElementHandler(self, name, attrs) -> None: ...
    def endElementHandler(self, name) -> None: ...

class _FetchUnicodesParser(_BaseParser):
    unicodes: Incomplete
    def __init__(self) -> None: ...
    def startElementHandler(self, name, attrs) -> None: ...

class _FetchImageFileNameParser(_BaseParser):
    fileName: Incomplete
    def __init__(self) -> None: ...
    def startElementHandler(self, name, attrs) -> None: ...

class _FetchComponentBasesParser(_BaseParser):
    bases: Incomplete
    def __init__(self) -> None: ...
    def startElementHandler(self, name, attrs) -> None: ...
    def endElementHandler(self, name) -> None: ...

class GLIFPointPen(AbstractPointPen):
    """
    Helper class using the PointPen protocol to write the <outline>
    part of .glif files.
    """
    formatVersion: Incomplete
    identifiers: Incomplete
    outline: Incomplete
    contour: Incomplete
    prevOffCurveCount: int
    prevPointTypes: Incomplete
    validate: Incomplete
    def __init__(self, element, formatVersion: Incomplete | None = None, identifiers: Incomplete | None = None, validate: bool = True) -> None: ...
    def beginPath(self, identifier: Incomplete | None = None, **kwargs) -> None: ...
    prevPointType: Incomplete
    def endPath(self) -> None: ...
    def addPoint(self, pt, segmentType: Incomplete | None = None, smooth: Incomplete | None = None, name: Incomplete | None = None, identifier: Incomplete | None = None, **kwargs) -> None: ...
    def addComponent(self, glyphName, transformation, identifier: Incomplete | None = None, **kwargs) -> None: ...
