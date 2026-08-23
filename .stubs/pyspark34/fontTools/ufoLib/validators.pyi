from _typeshed import Incomplete
from fontTools.ufoLib.utils import numberTypes as numberTypes

def isDictEnough(value):
    """
    Some objects will likely come in that aren't
    dicts but are dict-ish enough.
    """
def genericTypeValidator(value, typ):
    """
    Generic. (Added at version 2.)
    """
def genericIntListValidator(values, validValues):
    """
    Generic. (Added at version 2.)
    """
def genericNonNegativeIntValidator(value):
    """
    Generic. (Added at version 3.)
    """
def genericNonNegativeNumberValidator(value):
    """
    Generic. (Added at version 3.)
    """
def genericDictValidator(value, prototype):
    """
    Generic. (Added at version 3.)
    """
def fontInfoStyleMapStyleNameValidator(value):
    """
    Version 2+.
    """
def fontInfoOpenTypeGaspRangeRecordsValidator(value):
    """
    Version 3+.
    """
def fontInfoOpenTypeHeadCreatedValidator(value):
    """
    Version 2+.
    """
def fontInfoOpenTypeNameRecordsValidator(value):
    """
    Version 3+.
    """
def fontInfoOpenTypeOS2WeightClassValidator(value):
    """
    Version 2+.
    """
def fontInfoOpenTypeOS2WidthClassValidator(value):
    """
    Version 2+.
    """
def fontInfoVersion2OpenTypeOS2PanoseValidator(values):
    """
    Version 2.
    """
def fontInfoVersion3OpenTypeOS2PanoseValidator(values):
    """
    Version 3+.
    """
def fontInfoOpenTypeOS2FamilyClassValidator(values):
    """
    Version 2+.
    """
def fontInfoPostscriptBluesValidator(values):
    """
    Version 2+.
    """
def fontInfoPostscriptOtherBluesValidator(values):
    """
    Version 2+.
    """
def fontInfoPostscriptStemsValidator(values):
    """
    Version 2+.
    """
def fontInfoPostscriptWindowsCharacterSetValidator(value):
    """
    Version 2+.
    """
def fontInfoWOFFMetadataUniqueIDValidator(value):
    """
    Version 3+.
    """
def fontInfoWOFFMetadataVendorValidator(value):
    """
    Version 3+.
    """
def fontInfoWOFFMetadataCreditsValidator(value):
    """
    Version 3+.
    """
def fontInfoWOFFMetadataDescriptionValidator(value):
    """
    Version 3+.
    """
def fontInfoWOFFMetadataLicenseValidator(value):
    """
    Version 3+.
    """
def fontInfoWOFFMetadataTrademarkValidator(value):
    """
    Version 3+.
    """
def fontInfoWOFFMetadataCopyrightValidator(value):
    """
    Version 3+.
    """
def fontInfoWOFFMetadataLicenseeValidator(value):
    """
    Version 3+.
    """
def fontInfoWOFFMetadataTextValue(value):
    """
    Version 3+.
    """
def fontInfoWOFFMetadataExtensionsValidator(value):
    """
    Version 3+.
    """
def fontInfoWOFFMetadataExtensionValidator(value):
    """
    Version 3+.
    """
def fontInfoWOFFMetadataExtensionItemValidator(value):
    """
    Version 3+.
    """
def fontInfoWOFFMetadataExtensionNameValidator(value):
    """
    Version 3+.
    """
def fontInfoWOFFMetadataExtensionValueValidator(value):
    """
    Version 3+.
    """
def guidelinesValidator(value, identifiers: Incomplete | None = None):
    """
    Version 3+.
    """
def guidelineValidator(value):
    """
    Version 3+.
    """
def anchorsValidator(value, identifiers: Incomplete | None = None):
    """
    Version 3+.
    """
def anchorValidator(value):
    """
    Version 3+.
    """
def identifierValidator(value):
    '''
    Version 3+.

    >>> identifierValidator("a")
    True
    >>> identifierValidator("")
    False
    >>> identifierValidator("a" * 101)
    False
    '''
def colorValidator(value):
    '''
    Version 3+.

    >>> colorValidator("0,0,0,0")
    True
    >>> colorValidator(".5,.5,.5,.5")
    True
    >>> colorValidator("0.5,0.5,0.5,0.5")
    True
    >>> colorValidator("1,1,1,1")
    True

    >>> colorValidator("2,0,0,0")
    False
    >>> colorValidator("0,2,0,0")
    False
    >>> colorValidator("0,0,2,0")
    False
    >>> colorValidator("0,0,0,2")
    False

    >>> colorValidator("1r,1,1,1")
    False
    >>> colorValidator("1,1g,1,1")
    False
    >>> colorValidator("1,1,1b,1")
    False
    >>> colorValidator("1,1,1,1a")
    False

    >>> colorValidator("1 1 1 1")
    False
    >>> colorValidator("1 1,1,1")
    False
    >>> colorValidator("1,1 1,1")
    False
    >>> colorValidator("1,1,1 1")
    False

    >>> colorValidator("1, 1, 1, 1")
    True
    '''

pngSignature: bytes

def imageValidator(value):
    """
    Version 3+.
    """
def pngValidator(path: Incomplete | None = None, data: Incomplete | None = None, fileObj: Incomplete | None = None):
    """
    Version 3+.

    This checks the signature of the image data.
    """
def layerContentsValidator(value, ufoPathOrFileSystem):
    """
    Check the validity of layercontents.plist.
    Version 3+.
    """
def groupsValidator(value):
    '''
    Check the validity of the groups.
    Version 3+ (though it\'s backwards compatible with UFO 1 and UFO 2).

    >>> groups = {"A" : ["A", "A"], "A2" : ["A"]}
    >>> groupsValidator(groups)
    (True, None)

    >>> groups = {"" : ["A"]}
    >>> valid, msg = groupsValidator(groups)
    >>> valid
    False
    >>> print(msg)
    A group has an empty name.

    >>> groups = {"public.awesome" : ["A"]}
    >>> groupsValidator(groups)
    (True, None)

    >>> groups = {"public.kern1." : ["A"]}
    >>> valid, msg = groupsValidator(groups)
    >>> valid
    False
    >>> print(msg)
    The group data contains a kerning group with an incomplete name.
    >>> groups = {"public.kern2." : ["A"]}
    >>> valid, msg = groupsValidator(groups)
    >>> valid
    False
    >>> print(msg)
    The group data contains a kerning group with an incomplete name.

    >>> groups = {"public.kern1.A" : ["A"], "public.kern2.A" : ["A"]}
    >>> groupsValidator(groups)
    (True, None)

    >>> groups = {"public.kern1.A1" : ["A"], "public.kern1.A2" : ["A"]}
    >>> valid, msg = groupsValidator(groups)
    >>> valid
    False
    >>> print(msg)
    The glyph "A" occurs in too many kerning groups.
    '''
def kerningValidator(data):
    '''
    Check the validity of the kerning data structure.
    Version 3+ (though it\'s backwards compatible with UFO 1 and UFO 2).

    >>> kerning = {"A" : {"B" : 100}}
    >>> kerningValidator(kerning)
    (True, None)

    >>> kerning = {"A" : ["B"]}
    >>> valid, msg = kerningValidator(kerning)
    >>> valid
    False
    >>> print(msg)
    The kerning data is not in the correct format.

    >>> kerning = {"A" : {"B" : "100"}}
    >>> valid, msg = kerningValidator(kerning)
    >>> valid
    False
    >>> print(msg)
    The kerning data is not in the correct format.
    '''
def fontLibValidator(value):
    '''
    Check the validity of the lib.
    Version 3+ (though it\'s backwards compatible with UFO 1 and UFO 2).

    >>> lib = {"foo" : "bar"}
    >>> fontLibValidator(lib)
    (True, None)

    >>> lib = {"public.awesome" : "hello"}
    >>> fontLibValidator(lib)
    (True, None)

    >>> lib = {"public.glyphOrder" : ["A", "C", "B"]}
    >>> fontLibValidator(lib)
    (True, None)

    >>> lib = "hello"
    >>> valid, msg = fontLibValidator(lib)
    >>> valid
    False
    >>> print(msg)  # doctest: +ELLIPSIS
    The lib data is not in the correct format: expected a dictionary, ...

    >>> lib = {1: "hello"}
    >>> valid, msg = fontLibValidator(lib)
    >>> valid
    False
    >>> print(msg)
    The lib key is not properly formatted: expected str, found int: 1

    >>> lib = {"public.glyphOrder" : "hello"}
    >>> valid, msg = fontLibValidator(lib)
    >>> valid
    False
    >>> print(msg)  # doctest: +ELLIPSIS
    public.glyphOrder is not properly formatted: expected list or tuple,...

    >>> lib = {"public.glyphOrder" : ["A", 1, "B"]}
    >>> valid, msg = fontLibValidator(lib)
    >>> valid
    False
    >>> print(msg)  # doctest: +ELLIPSIS
    public.glyphOrder is not properly formatted: expected str,...
    '''
def glyphLibValidator(value):
    '''
    Check the validity of the lib.
    Version 3+ (though it\'s backwards compatible with UFO 1 and UFO 2).

    >>> lib = {"foo" : "bar"}
    >>> glyphLibValidator(lib)
    (True, None)

    >>> lib = {"public.awesome" : "hello"}
    >>> glyphLibValidator(lib)
    (True, None)

    >>> lib = {"public.markColor" : "1,0,0,0.5"}
    >>> glyphLibValidator(lib)
    (True, None)

    >>> lib = {"public.markColor" : 1}
    >>> valid, msg = glyphLibValidator(lib)
    >>> valid
    False
    >>> print(msg)
    public.markColor is not properly formatted.
    '''
