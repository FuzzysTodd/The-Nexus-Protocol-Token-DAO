from fontTools.ufoLib.validators import *
import enum
from _typeshed import Incomplete
from fontTools.ufoLib.errors import UFOLibError as UFOLibError
from fontTools.ufoLib.utils import _VersionTupleEnumMixin

__all__ = ['makeUFOPath', 'UFOLibError', 'UFOReader', 'UFOWriter', 'UFOReaderWriter', 'UFOFileStructure', 'fontInfoAttributesVersion1', 'fontInfoAttributesVersion2', 'fontInfoAttributesVersion3', 'deprecatedFontInfoAttributesVersion2', 'validateFontInfoVersion2ValueForAttribute', 'validateFontInfoVersion3ValueForAttribute', 'convertFontInfoValueForAttributeFromVersion1ToVersion2', 'convertFontInfoValueForAttributeFromVersion2ToVersion1']

class UFOFormatVersion(tuple, _VersionTupleEnumMixin, enum.Enum):
    FORMAT_1_0: Incomplete
    FORMAT_2_0: Incomplete
    FORMAT_3_0: Incomplete

class UFOFileStructure(enum.Enum):
    ZIP: str
    PACKAGE: str

class _UFOBaseIO:
    def getFileModificationTime(self, path):
        """
        Returns the modification time for the file at the given path, as a
        floating point number giving the number of seconds since the epoch.
        The path must be relative to the UFO path.
        Returns None if the file does not exist.
        """

class UFOReader(_UFOBaseIO):
    """
    Read the various components of the .ufo.

    By default read data is validated. Set ``validate`` to
    ``False`` to not validate the data.
    """
    fs: Incomplete
    def __init__(self, path, validate: bool = True) -> None: ...
    path: Incomplete
    formatVersion: Incomplete
    @property
    def formatVersionTuple(self):
        """The (major, minor) format version of the UFO.
        This is determined by reading metainfo.plist during __init__.
        """
    fileStructure: Incomplete
    def readBytesFromPath(self, path):
        """
        Returns the bytes in the file at the given path.
        The path must be relative to the UFO's filesystem root.
        Returns None if the file does not exist.
        """
    def getReadFileForPath(self, path, encoding: Incomplete | None = None):
        """
        Returns a file (or file-like) object for the file at the given path.
        The path must be relative to the UFO path.
        Returns None if the file does not exist.
        By default the file is opened in binary mode (reads bytes).
        If encoding is passed, the file is opened in text mode (reads str).

        Note: The caller is responsible for closing the open file.
        """
    def readMetaInfo(self, validate: Incomplete | None = None) -> None:
        """
        Read metainfo.plist and set formatVersion. Only used for internal operations.

        ``validate`` will validate the read data, by default it is set
        to the class's validate value, can be overridden.
        """
    def readGroups(self, validate: Incomplete | None = None):
        """
        Read groups.plist. Returns a dict.
        ``validate`` will validate the read data, by default it is set to the
        class's validate value, can be overridden.
        """
    def getKerningGroupConversionRenameMaps(self, validate: Incomplete | None = None):
        '''
        Get maps defining the renaming that was done during any
        needed kerning group conversion. This method returns a
        dictionary of this form::

                {
                        "side1" : {"old group name" : "new group name"},
                        "side2" : {"old group name" : "new group name"}
                }

        When no conversion has been performed, the side1 and side2
        dictionaries will be empty.

        ``validate`` will validate the groups, by default it is set to the
        class\'s validate value, can be overridden.
        '''
    def readInfo(self, info, validate: Incomplete | None = None) -> None:
        """
        Read fontinfo.plist. It requires an object that allows
        setting attributes with names that follow the fontinfo.plist
        version 3 specification. This will write the attributes
        defined in the file into the object.

        ``validate`` will validate the read data, by default it is set to the
        class's validate value, can be overridden.
        """
    def readKerning(self, validate: Incomplete | None = None):
        """
        Read kerning.plist. Returns a dict.

        ``validate`` will validate the kerning data, by default it is set to the
        class's validate value, can be overridden.
        """
    def readLib(self, validate: Incomplete | None = None):
        """
        Read lib.plist. Returns a dict.

        ``validate`` will validate the data, by default it is set to the
        class's validate value, can be overridden.
        """
    def readFeatures(self):
        """
        Read features.fea. Return a string.
        The returned string is empty if the file is missing.
        """
    def getLayerNames(self, validate: Incomplete | None = None):
        """
        Get the ordered layer names from layercontents.plist.

        ``validate`` will validate the data, by default it is set to the
        class's validate value, can be overridden.
        """
    def getDefaultLayerName(self, validate: Incomplete | None = None):
        """
        Get the default layer name from layercontents.plist.

        ``validate`` will validate the data, by default it is set to the
        class's validate value, can be overridden.
        """
    def getGlyphSet(self, layerName: Incomplete | None = None, validateRead: Incomplete | None = None, validateWrite: Incomplete | None = None):
        """
        Return the GlyphSet associated with the
        glyphs directory mapped to layerName
        in the UFO. If layerName is not provided,
        the name retrieved with getDefaultLayerName
        will be used.

        ``validateRead`` will validate the read data, by default it is set to the
        class's validate value, can be overridden.
        ``validateWrite`` will validate the written data, by default it is set to the
        class's validate value, can be overridden.
        """
    def getCharacterMapping(self, layerName: Incomplete | None = None, validate: Incomplete | None = None):
        """
        Return a dictionary that maps unicode values (ints) to
        lists of glyph names.
        """
    def getDataDirectoryListing(self):
        """
        Returns a list of all files in the data directory.
        The returned paths will be relative to the UFO.
        This will not list directory names, only file names.
        Thus, empty directories will be skipped.
        """
    def getImageDirectoryListing(self, validate: Incomplete | None = None):
        """
        Returns a list of all image file names in
        the images directory. Each of the images will
        have been verified to have the PNG signature.

        ``validate`` will validate the data, by default it is set to the
        class's validate value, can be overridden.
        """
    def readData(self, fileName):
        """
        Return bytes for the file named 'fileName' inside the 'data/' directory.
        """
    def readImage(self, fileName, validate: Incomplete | None = None):
        """
        Return image data for the file named fileName.

        ``validate`` will validate the data, by default it is set to the
        class's validate value, can be overridden.
        """
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

class UFOWriter(UFOReader):
    """
    Write the various components of the .ufo.

    By default, the written data will be validated before writing. Set ``validate`` to
    ``False`` if you do not want to validate the data. Validation can also be overriden
    on a per method level if desired.

    The ``formatVersion`` argument allows to specify the UFO format version as a tuple
    of integers (major, minor), or as a single integer for the major digit only (minor
    is implied as 0). By default the latest formatVersion will be used; currently it's
    3.0, which is equivalent to formatVersion=(3, 0).

    An UnsupportedUFOFormat exception is raised if the requested UFO formatVersion is
    not supported.
    """
    fs: Incomplete
    layerContents: Incomplete
    def __init__(self, path, formatVersion: Incomplete | None = None, fileCreator: str = 'com.github.fonttools.ufoLib', structure: Incomplete | None = None, validate: bool = True) -> None: ...
    fileCreator: Incomplete
    def copyFromReader(self, reader, sourcePath, destPath) -> None:
        """
        Copy the sourcePath in the provided UFOReader to destPath
        in this writer. The paths must be relative. This works with
        both individual files and directories.
        """
    def writeBytesToPath(self, path, data) -> None:
        """
        Write bytes to a path relative to the UFO filesystem's root.
        If writing to an existing UFO, check to see if data matches the data
        that is already in the file at path; if so, the file is not rewritten
        so that the modification date is preserved.
        If needed, the directory tree for the given path will be built.
        """
    def getFileObjectForPath(self, path, mode: str = 'w', encoding: Incomplete | None = None):
        '''
        Returns a file (or file-like) object for the
        file at the given path. The path must be relative
        to the UFO path. Returns None if the file does
        not exist and the mode is "r" or "rb.
        An encoding may be passed if the file is opened in text mode.

        Note: The caller is responsible for closing the open file.
        '''
    def removePath(self, path, force: bool = False, removeEmptyParents: bool = True) -> None:
        """
        Remove the file (or directory) at path. The path
        must be relative to the UFO.
        Raises UFOLibError if the path doesn't exist.
        If force=True, ignore non-existent paths.
        If the directory where 'path' is located becomes empty, it will
        be automatically removed, unless 'removeEmptyParents' is False.
        """
    removeFileForPath = removePath
    def setModificationTime(self) -> None:
        """
        Set the UFO modification time to the current time.
        This is never called automatically. It is up to the
        caller to call this when finished working on the UFO.
        """
    def setKerningGroupConversionRenameMaps(self, maps) -> None:
        '''
        Set maps defining the renaming that should be done
        when writing groups and kerning in UFO 1 and UFO 2.
        This will effectively undo the conversion done when
        UFOReader reads this data. The dictionary should have
        this form::

                {
                        "side1" : {"group name to use when writing" : "group name in data"},
                        "side2" : {"group name to use when writing" : "group name in data"}
                }

        This is the same form returned by UFOReader\'s
        getKerningGroupConversionRenameMaps method.
        '''
    def writeGroups(self, groups, validate: Incomplete | None = None) -> None:
        """
        Write groups.plist. This method requires a
        dict of glyph groups as an argument.

        ``validate`` will validate the data, by default it is set to the
        class's validate value, can be overridden.
        """
    def writeInfo(self, info, validate: Incomplete | None = None) -> None:
        """
        Write info.plist. This method requires an object
        that supports getting attributes that follow the
        fontinfo.plist version 2 specification. Attributes
        will be taken from the given object and written
        into the file.

        ``validate`` will validate the data, by default it is set to the
        class's validate value, can be overridden.
        """
    def writeKerning(self, kerning, validate: Incomplete | None = None) -> None:
        """
        Write kerning.plist. This method requires a
        dict of kerning pairs as an argument.

        This performs basic structural validation of the kerning,
        but it does not check for compliance with the spec in
        regards to conflicting pairs. The assumption is that the
        kerning data being passed is standards compliant.

        ``validate`` will validate the data, by default it is set to the
        class's validate value, can be overridden.
        """
    def writeLib(self, libDict, validate: Incomplete | None = None) -> None:
        """
        Write lib.plist. This method requires a
        lib dict as an argument.

        ``validate`` will validate the data, by default it is set to the
        class's validate value, can be overridden.
        """
    def writeFeatures(self, features, validate: Incomplete | None = None) -> None:
        """
        Write features.fea. This method requires a
        features string as an argument.
        """
    def writeLayerContents(self, layerOrder: Incomplete | None = None, validate: Incomplete | None = None) -> None:
        """
        Write the layercontents.plist file. This method  *must* be called
        after all glyph sets have been written.
        """
    def getGlyphSet(self, layerName: Incomplete | None = None, defaultLayer: bool = True, glyphNameToFileNameFunc: Incomplete | None = None, validateRead: Incomplete | None = None, validateWrite: Incomplete | None = None, expectContentsFile: bool = False):
        """
        Return the GlyphSet object associated with the
        appropriate glyph directory in the .ufo.
        If layerName is None, the default glyph set
        will be used. The defaultLayer flag indictes
        that the layer should be saved into the default
        glyphs directory.

        ``validateRead`` will validate the read data, by default it is set to the
        class's validate value, can be overridden.
        ``validateWrte`` will validate the written data, by default it is set to the
        class's validate value, can be overridden.
        ``expectContentsFile`` will raise a GlifLibError if a contents.plist file is
        not found on the glyph set file system. This should be set to ``True`` if you
        are reading an existing UFO and ``False`` if you use ``getGlyphSet`` to create
        a fresh\tglyph set.
        """
    def renameGlyphSet(self, layerName, newLayerName, defaultLayer: bool = False) -> None:
        """
        Rename a glyph set.

        Note: if a GlyphSet object has already been retrieved for
        layerName, it is up to the caller to inform that object that
        the directory it represents has changed.
        """
    def deleteGlyphSet(self, layerName) -> None:
        """
        Remove the glyph set matching layerName.
        """
    def writeData(self, fileName, data) -> None:
        """
        Write data to fileName in the 'data' directory.
        The data must be a bytes string.
        """
    def removeData(self, fileName) -> None:
        """
        Remove the file named fileName from the data directory.
        """
    def writeImage(self, fileName, data, validate: Incomplete | None = None) -> None:
        """
        Write data to fileName in the images directory.
        The data must be a valid PNG.
        """
    def removeImage(self, fileName, validate: Incomplete | None = None) -> None:
        """
        Remove the file named fileName from the
        images directory.
        """
    def copyImageFromReader(self, reader, sourceFileName, destFileName, validate: Incomplete | None = None) -> None:
        """
        Copy the sourceFileName in the provided UFOReader to destFileName
        in this writer. This uses the most memory efficient method possible
        for copying the data possible.
        """
    def close(self) -> None: ...
UFOReaderWriter = UFOWriter

def makeUFOPath(path):
    '''
    Return a .ufo pathname.

    >>> makeUFOPath("directory/something.ext") == (
    ... \tos.path.join(\'directory\', \'something.ufo\'))
    True
    >>> makeUFOPath("directory/something.another.thing.ext") == (
    ... \tos.path.join(\'directory\', \'something.another.thing.ufo\'))
    True
    '''
def validateFontInfoVersion2ValueForAttribute(attr, value):
    """
    This performs very basic validation of the value for attribute
    following the UFO 2 fontinfo.plist specification. The results
    of this should not be interpretted as *correct* for the font
    that they are part of. This merely indicates that the value
    is of the proper type and, where the specification defines
    a set range of possible values for an attribute, that the
    value is in the accepted range.
    """
def validateFontInfoVersion3ValueForAttribute(attr, value):
    """
    This performs very basic validation of the value for attribute
    following the UFO 3 fontinfo.plist specification. The results
    of this should not be interpretted as *correct* for the font
    that they are part of. This merely indicates that the value
    is of the proper type and, where the specification defines
    a set range of possible values for an attribute, that the
    value is in the accepted range.
    """

fontInfoAttributesVersion1: Incomplete
fontInfoAttributesVersion2: Incomplete
fontInfoAttributesVersion3: Incomplete
deprecatedFontInfoAttributesVersion2: Incomplete

def convertFontInfoValueForAttributeFromVersion1ToVersion2(attr, value):
    """
    Convert value from version 1 to version 2 format.
    Returns the new attribute name and the converted value.
    If the value is None, None will be returned for the new value.
    """
def convertFontInfoValueForAttributeFromVersion2ToVersion1(attr, value):
    """
    Convert value from version 2 to version 1 format.
    Returns the new attribute name and the converted value.
    If the value is None, None will be returned for the new value.
    """
