from fontTools.designspaceLib import AxisLabelDescriptor as AxisLabelDescriptor, DesignSpaceDocument as DesignSpaceDocument, DesignSpaceDocumentError as DesignSpaceDocumentError, LocationLabelDescriptor as LocationLabelDescriptor
from fontTools.designspaceLib.types import Region as Region, getVFUserRegion as getVFUserRegion, locationInRegion as locationInRegion
from fontTools.ttLib import TTFont as TTFont
from typing import Dict, List

def buildVFStatTable(ttFont: TTFont, doc: DesignSpaceDocument, vfName: str) -> None:
    """Build the STAT table for the variable font identified by its name in
    the given document.

    Knowing which variable we're building STAT data for is needed to subset
    the STAT locations to only include what the variable font actually ships.

    .. versionadded:: 5.0

    .. seealso::
        - :func:`getStatAxes()`
        - :func:`getStatLocations()`
        - :func:`fontTools.otlLib.builder.buildStatTable()`
    """
def getStatAxes(doc: DesignSpaceDocument, userRegion: Region) -> List[Dict]:
    """Return a list of axis dicts suitable for use as the ``axes``
    argument to :func:`fontTools.otlLib.builder.buildStatTable()`.

    .. versionadded:: 5.0
    """
def getStatLocations(doc: DesignSpaceDocument, userRegion: Region) -> List[Dict]:
    """Return a list of location dicts suitable for use as the ``locations``
    argument to :func:`fontTools.otlLib.builder.buildStatTable()`.

    .. versionadded:: 5.0
    """
