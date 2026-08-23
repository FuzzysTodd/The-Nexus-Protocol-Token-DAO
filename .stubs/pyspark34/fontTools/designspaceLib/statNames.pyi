from _typeshed import Incomplete
from dataclasses import dataclass
from fontTools.designspaceLib import AxisDescriptor as AxisDescriptor, AxisLabelDescriptor as AxisLabelDescriptor, DesignSpaceDocument as DesignSpaceDocument, DesignSpaceDocumentError as DesignSpaceDocumentError, DiscreteAxisDescriptor as DiscreteAxisDescriptor, SimpleLocationDict as SimpleLocationDict, SourceDescriptor as SourceDescriptor
from typing import Dict

LOGGER: Incomplete
RibbiStyle = str
BOLD_ITALIC_TO_RIBBI_STYLE: Incomplete

@dataclass
class StatNames:
    """Name data generated from the STAT table information."""
    familyNames: Dict[str, str]
    styleNames: Dict[str, str]
    postScriptFontName: str | None
    styleMapFamilyNames: Dict[str, str]
    styleMapStyleName: RibbiStyle | None
    def __init__(self, familyNames, styleNames, postScriptFontName, styleMapFamilyNames, styleMapStyleName) -> None: ...

def getStatNames(doc: DesignSpaceDocument, userLocation: SimpleLocationDict) -> StatNames:
    """Compute the family, style, PostScript names of the given ``userLocation``
    using the document's STAT information.

    Also computes localizations.

    If not enough STAT data is available for a given name, either its dict of
    localized names will be empty (family and style names), or the name will be
    None (PostScript name).

    .. versionadded:: 5.0
    """
