from collections.abc import Generator
from copy import deepcopy as deepcopy
from enum import IntEnum

class NameID(IntEnum):
    FAMILY_NAME: int
    SUBFAMILY_NAME: int
    UNIQUE_FONT_IDENTIFIER: int
    FULL_FONT_NAME: int
    VERSION_STRING: int
    POSTSCRIPT_NAME: int
    TYPOGRAPHIC_FAMILY_NAME: int
    TYPOGRAPHIC_SUBFAMILY_NAME: int
    VARIATIONS_POSTSCRIPT_NAME_PREFIX: int

ELIDABLE_AXIS_VALUE_NAME: int

def getVariationNameIDs(varfont): ...
def pruningUnusedNames(varfont) -> Generator[None, None, None]: ...
def updateNameTable(varfont, axisLimits) -> None:
    '''Update instatiated variable font\'s name table using STAT AxisValues.

    Raises ValueError if the STAT table is missing or an Axis Value table is
    missing for requested axis locations.

    First, collect all STAT AxisValues that match the new default axis locations
    (excluding "elided" ones); concatenate the strings in design axis order,
    while giving priority to "synthetic" values (Format 4), to form the
    typographic subfamily name associated with the new default instance.
    Finally, update all related records in the name table, making sure that
    legacy family/sub-family names conform to the the R/I/B/BI (Regular, Italic,
    Bold, Bold Italic) naming model.

    Example: Updating a partial variable font:
    | >>> ttFont = TTFont("OpenSans[wdth,wght].ttf")
    | >>> updateNameTable(ttFont, {"wght": (400, 900), "wdth": 75})

    The name table records will be updated in the following manner:
    NameID 1 familyName: "Open Sans" --> "Open Sans Condensed"
    NameID 2 subFamilyName: "Regular" --> "Regular"
    NameID 3 Unique font identifier: "3.000;GOOG;OpenSans-Regular" -->         "3.000;GOOG;OpenSans-Condensed"
    NameID 4 Full font name: "Open Sans Regular" --> "Open Sans Condensed"
    NameID 6 PostScript name: "OpenSans-Regular" --> "OpenSans-Condensed"
    NameID 16 Typographic Family name: None --> "Open Sans"
    NameID 17 Typographic Subfamily name: None --> "Condensed"

    References:
    https://docs.microsoft.com/en-us/typography/opentype/spec/stat
    https://docs.microsoft.com/en-us/typography/opentype/spec/name#name-ids
    '''
def checkAxisValuesExist(stat, axisValues, axisCoords) -> None: ...
