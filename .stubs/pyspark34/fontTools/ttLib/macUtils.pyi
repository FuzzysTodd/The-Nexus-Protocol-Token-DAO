from _typeshed import Incomplete
from fontTools.misc.macRes import ResourceError as ResourceError, ResourceReader as ResourceReader
from io import BytesIO

def getSFNTResIndices(path):
    """Determine whether a file has a 'sfnt' resource fork or not."""
def openTTFonts(path):
    """Given a pathname, return a list of TTFont objects. In the case
    of a flat TTF/OTF file, the list will contain just one font object;
    but in the case of a Mac font suitcase it will contain as many
    font objects as there are sfnt resources in the file.
    """

class SFNTResourceReader(BytesIO):
    """Simple read-only file wrapper for 'sfnt' resources."""
    rsrc: Incomplete
    name: Incomplete
    def __init__(self, path, res_name_or_index) -> None: ...
