from _typeshed import Incomplete
from fontTools.misc import etree as ET
from fontTools.misc.loggingTools import LogMixin
from typing import Dict, List, Tuple

__all__ = ['AxisDescriptor', 'AxisLabelDescriptor', 'AxisMappingDescriptor', 'BaseDocReader', 'BaseDocWriter', 'DesignSpaceDocument', 'DesignSpaceDocumentError', 'DiscreteAxisDescriptor', 'InstanceDescriptor', 'LocationLabelDescriptor', 'RangeAxisSubsetDescriptor', 'RuleDescriptor', 'SourceDescriptor', 'ValueAxisSubsetDescriptor', 'VariableFontDescriptor']

class DesignSpaceDocumentError(Exception):
    msg: Incomplete
    obj: Incomplete
    def __init__(self, msg, obj: Incomplete | None = None) -> None: ...

class AsDictMixin:
    def asdict(self): ...

class SimpleDescriptor(AsDictMixin):
    """Containers for a bunch of attributes"""
    def compare(self, other) -> None: ...

class SourceDescriptor(SimpleDescriptor):
    '''Simple container for data related to the source

    .. code:: python

        doc = DesignSpaceDocument()
        s1 = SourceDescriptor()
        s1.path = masterPath1
        s1.name = "master.ufo1"
        s1.font = defcon.Font("master.ufo1")
        s1.location = dict(weight=0)
        s1.familyName = "MasterFamilyName"
        s1.styleName = "MasterStyleNameOne"
        s1.localisedFamilyName = dict(fr="Caractère")
        s1.mutedGlyphNames.append("A")
        s1.mutedGlyphNames.append("Z")
        doc.addSource(s1)

    '''
    flavor: str
    filename: Incomplete
    path: Incomplete
    font: Incomplete
    name: Incomplete
    designLocation: Incomplete
    layerName: Incomplete
    familyName: Incomplete
    styleName: Incomplete
    localisedFamilyName: Incomplete
    copyLib: Incomplete
    copyInfo: Incomplete
    copyGroups: Incomplete
    copyFeatures: Incomplete
    muteKerning: Incomplete
    muteInfo: Incomplete
    mutedGlyphNames: Incomplete
    def __init__(self, *, filename: Incomplete | None = None, path: Incomplete | None = None, font: Incomplete | None = None, name: Incomplete | None = None, location: Incomplete | None = None, designLocation: Incomplete | None = None, layerName: Incomplete | None = None, familyName: Incomplete | None = None, styleName: Incomplete | None = None, localisedFamilyName: Incomplete | None = None, copyLib: bool = False, copyInfo: bool = False, copyGroups: bool = False, copyFeatures: bool = False, muteKerning: bool = False, muteInfo: bool = False, mutedGlyphNames: Incomplete | None = None) -> None: ...
    @property
    def location(self):
        """dict. Axis values for this source, in design space coordinates.

        MutatorMath + varLib.

        .. deprecated:: 5.0
           Use the more explicit alias for this property :attr:`designLocation`.
        """
    @location.setter
    def location(self, location: SimpleLocationDict | None): ...
    def setFamilyName(self, familyName, languageCode: str = 'en') -> None:
        """Setter for :attr:`localisedFamilyName`

        .. versionadded:: 5.0
        """
    def getFamilyName(self, languageCode: str = 'en'):
        """Getter for :attr:`localisedFamilyName`

        .. versionadded:: 5.0
        """
    def getFullDesignLocation(self, doc: DesignSpaceDocument) -> SimpleLocationDict:
        """Get the complete design location of this source, from its
        :attr:`designLocation` and the document's axis defaults.

        .. versionadded:: 5.0
        """

class RuleDescriptor(SimpleDescriptor):
    '''Represents the rule descriptor element: a set of glyph substitutions to
    trigger conditionally in some parts of the designspace.

    .. code:: python

        r1 = RuleDescriptor()
        r1.name = "unique.rule.name"
        r1.conditionSets.append([dict(name="weight", minimum=-10, maximum=10), dict(...)])
        r1.conditionSets.append([dict(...), dict(...)])
        r1.subs.append(("a", "a.alt"))

    .. code:: xml

        <!-- optional: list of substitution rules -->
        <rules>
            <rule name="vertical.bars">
                <conditionset>
                    <condition minimum="250.000000" maximum="750.000000" name="weight"/>
                    <condition minimum="100" name="width"/>
                    <condition minimum="10" maximum="40" name="optical"/>
                </conditionset>
                <sub name="cent" with="cent.alt"/>
                <sub name="dollar" with="dollar.alt"/>
            </rule>
        </rules>
    '''
    name: Incomplete
    conditionSets: Incomplete
    subs: Incomplete
    def __init__(self, *, name: Incomplete | None = None, conditionSets: Incomplete | None = None, subs: Incomplete | None = None) -> None: ...
AnisotropicLocationDict = Dict[str, float | Tuple[float, float]]
SimpleLocationDict = Dict[str, float]

class AxisMappingDescriptor(SimpleDescriptor):
    '''Represents the axis mapping element: mapping an input location
    to an output location in the designspace.

    .. code:: python

        m1 = AxisMappingDescriptor()
        m1.inputLocation = {"weight": 900, "width": 150}
        m1.outputLocation = {"weight": 870}

    .. code:: xml

        <mappings>
            <mapping>
                <input>
                    <dimension name="weight" xvalue="900"/>
                    <dimension name="width" xvalue="150"/>
                </input>
                <output>
                    <dimension name="weight" xvalue="870"/>
                </output>
            </mapping>
        </mappings>
    '''
    inputLocation: Incomplete
    outputLocation: Incomplete
    description: Incomplete
    groupDescription: Incomplete
    def __init__(self, *, inputLocation: Incomplete | None = None, outputLocation: Incomplete | None = None, description: Incomplete | None = None, groupDescription: Incomplete | None = None) -> None: ...

class InstanceDescriptor(SimpleDescriptor):
    '''Simple container for data related to the instance


    .. code:: python

        i2 = InstanceDescriptor()
        i2.path = instancePath2
        i2.familyName = "InstanceFamilyName"
        i2.styleName = "InstanceStyleName"
        i2.name = "instance.ufo2"
        # anisotropic location
        i2.designLocation = dict(weight=500, width=(400,300))
        i2.postScriptFontName = "InstancePostscriptName"
        i2.styleMapFamilyName = "InstanceStyleMapFamilyName"
        i2.styleMapStyleName = "InstanceStyleMapStyleName"
        i2.lib[\'com.coolDesignspaceApp.specimenText\'] = \'Hamburgerwhatever\'
        doc.addInstance(i2)
    '''
    flavor: str
    filename: Incomplete
    path: Incomplete
    font: Incomplete
    name: Incomplete
    locationLabel: Incomplete
    designLocation: Incomplete
    userLocation: Incomplete
    familyName: Incomplete
    styleName: Incomplete
    postScriptFontName: Incomplete
    styleMapFamilyName: Incomplete
    styleMapStyleName: Incomplete
    localisedFamilyName: Incomplete
    localisedStyleName: Incomplete
    localisedStyleMapFamilyName: Incomplete
    localisedStyleMapStyleName: Incomplete
    glyphs: Incomplete
    kerning: Incomplete
    info: Incomplete
    lib: Incomplete
    def __init__(self, *, filename: Incomplete | None = None, path: Incomplete | None = None, font: Incomplete | None = None, name: Incomplete | None = None, location: Incomplete | None = None, locationLabel: Incomplete | None = None, designLocation: Incomplete | None = None, userLocation: Incomplete | None = None, familyName: Incomplete | None = None, styleName: Incomplete | None = None, postScriptFontName: Incomplete | None = None, styleMapFamilyName: Incomplete | None = None, styleMapStyleName: Incomplete | None = None, localisedFamilyName: Incomplete | None = None, localisedStyleName: Incomplete | None = None, localisedStyleMapFamilyName: Incomplete | None = None, localisedStyleMapStyleName: Incomplete | None = None, glyphs: Incomplete | None = None, kerning: bool = True, info: bool = True, lib: Incomplete | None = None) -> None: ...
    @property
    def location(self):
        """dict. Axis values for this instance.

        MutatorMath + varLib.

        .. deprecated:: 5.0
           Use the more explicit alias for this property :attr:`designLocation`.
        """
    @location.setter
    def location(self, location: AnisotropicLocationDict | None): ...
    def setStyleName(self, styleName, languageCode: str = 'en') -> None:
        """These methods give easier access to the localised names."""
    def getStyleName(self, languageCode: str = 'en'): ...
    def setFamilyName(self, familyName, languageCode: str = 'en') -> None: ...
    def getFamilyName(self, languageCode: str = 'en'): ...
    def setStyleMapStyleName(self, styleMapStyleName, languageCode: str = 'en') -> None: ...
    def getStyleMapStyleName(self, languageCode: str = 'en'): ...
    def setStyleMapFamilyName(self, styleMapFamilyName, languageCode: str = 'en') -> None: ...
    def getStyleMapFamilyName(self, languageCode: str = 'en'): ...
    def clearLocation(self, axisName: str | None = None):
        """Clear all location-related fields. Ensures that
        :attr:``designLocation`` and :attr:``userLocation`` are dictionaries
        (possibly empty if clearing everything).

        In order to update the location of this instance wholesale, a user
        should first clear all the fields, then change the field(s) for which
        they have data.

        .. code:: python

            instance.clearLocation()
            instance.designLocation = {'Weight': (34, 36.5), 'Width': 100}
            instance.userLocation = {'Opsz': 16}

        In order to update a single axis location, the user should only clear
        that axis, then edit the values:

        .. code:: python

            instance.clearLocation('Weight')
            instance.designLocation['Weight'] = (34, 36.5)

        Args:
          axisName: if provided, only clear the location for that axis.

        .. versionadded:: 5.0
        """
    def getLocationLabelDescriptor(self, doc: DesignSpaceDocument) -> LocationLabelDescriptor | None:
        """Get the :class:`LocationLabelDescriptor` instance that matches
        this instances's :attr:`locationLabel`.

        Raises if the named label can't be found.

        .. versionadded:: 5.0
        """
    def getFullDesignLocation(self, doc: DesignSpaceDocument) -> AnisotropicLocationDict:
        """Get the complete design location of this instance, by combining data
        from the various location fields, default axis values and mappings, and
        top-level location labels.

        The source of truth for this instance's location is determined for each
        axis independently by taking the first not-None field in this list:

        - ``locationLabel``: the location along this axis is the same as the
          matching STAT format 4 label. No anisotropy.
        - ``designLocation[axisName]``: the explicit design location along this
          axis, possibly anisotropic.
        - ``userLocation[axisName]``: the explicit user location along this
          axis. No anisotropy.
        - ``axis.default``: default axis value. No anisotropy.

        .. versionadded:: 5.0
        """
    def getFullUserLocation(self, doc: DesignSpaceDocument) -> SimpleLocationDict:
        """Get the complete user location for this instance.

        .. seealso:: :meth:`getFullDesignLocation`

        .. versionadded:: 5.0
        """

class AbstractAxisDescriptor(SimpleDescriptor):
    flavor: str
    tag: Incomplete
    name: Incomplete
    labelNames: Incomplete
    hidden: Incomplete
    map: Incomplete
    axisOrdering: Incomplete
    axisLabels: Incomplete
    def __init__(self, *, tag: Incomplete | None = None, name: Incomplete | None = None, labelNames: Incomplete | None = None, hidden: bool = False, map: Incomplete | None = None, axisOrdering: Incomplete | None = None, axisLabels: Incomplete | None = None) -> None: ...

class AxisDescriptor(AbstractAxisDescriptor):
    '''Simple container for the axis data.

    Add more localisations?

    .. code:: python

        a1 = AxisDescriptor()
        a1.minimum = 1
        a1.maximum = 1000
        a1.default = 400
        a1.name = "weight"
        a1.tag = "wght"
        a1.labelNames[\'fa-IR\'] = "قطر"
        a1.labelNames[\'en\'] = "Wéíght"
        a1.map = [(1.0, 10.0), (400.0, 66.0), (1000.0, 990.0)]
        a1.axisOrdering = 1
        a1.axisLabels = [
            AxisLabelDescriptor(name="Regular", userValue=400, elidable=True)
        ]
        doc.addAxis(a1)
    '''
    minimum: Incomplete
    maximum: Incomplete
    default: Incomplete
    def __init__(self, *, tag: Incomplete | None = None, name: Incomplete | None = None, labelNames: Incomplete | None = None, minimum: Incomplete | None = None, default: Incomplete | None = None, maximum: Incomplete | None = None, hidden: bool = False, map: Incomplete | None = None, axisOrdering: Incomplete | None = None, axisLabels: Incomplete | None = None) -> None: ...
    def serialize(self): ...
    def map_forward(self, v):
        """Maps value from axis mapping's input (user) to output (design)."""
    def map_backward(self, v):
        """Maps value from axis mapping's output (design) to input (user)."""

class DiscreteAxisDescriptor(AbstractAxisDescriptor):
    '''Container for discrete axis data.

    Use this for axes that do not interpolate. The main difference from a
    continuous axis is that a continuous axis has a ``minimum`` and ``maximum``,
    while a discrete axis has a list of ``values``.

    Example: an Italic axis with 2 stops, Roman and Italic, that are not
    compatible. The axis still allows to bind together the full font family,
    which is useful for the STAT table, however it can\'t become a variation
    axis in a VF.

    .. code:: python

        a2 = DiscreteAxisDescriptor()
        a2.values = [0, 1]
        a2.default = 0
        a2.name = "Italic"
        a2.tag = "ITAL"
        a2.labelNames[\'fr\'] = "Italique"
        a2.map = [(0, 0), (1, -11)]
        a2.axisOrdering = 2
        a2.axisLabels = [
            AxisLabelDescriptor(name="Roman", userValue=0, elidable=True)
        ]
        doc.addAxis(a2)

    .. versionadded:: 5.0
    '''
    flavor: str
    default: Incomplete
    values: Incomplete
    def __init__(self, *, tag: Incomplete | None = None, name: Incomplete | None = None, labelNames: Incomplete | None = None, values: Incomplete | None = None, default: Incomplete | None = None, hidden: bool = False, map: Incomplete | None = None, axisOrdering: Incomplete | None = None, axisLabels: Incomplete | None = None) -> None: ...
    def map_forward(self, value):
        """Maps value from axis mapping's input to output.

        Returns value unchanged if no mapping entry is found.

        Note: for discrete axes, each value must have its mapping entry, if
        you intend that value to be mapped.
        """
    def map_backward(self, value):
        """Maps value from axis mapping's output to input.

        Returns value unchanged if no mapping entry is found.

        Note: for discrete axes, each value must have its mapping entry, if
        you intend that value to be mapped.
        """

class AxisLabelDescriptor(SimpleDescriptor):
    """Container for axis label data.

    Analogue of OpenType's STAT data for a single axis (formats 1, 2 and 3).
    All values are user values.
    See: `OTSpec STAT Axis value table, format 1, 2, 3 <https://docs.microsoft.com/en-us/typography/opentype/spec/stat#axis-value-table-format-1>`_

    The STAT format of the Axis value depends on which field are filled-in,
    see :meth:`getFormat`

    .. versionadded:: 5.0
    """
    flavor: str
    userMinimum: Incomplete
    userValue: Incomplete
    userMaximum: Incomplete
    name: Incomplete
    elidable: Incomplete
    olderSibling: Incomplete
    linkedUserValue: Incomplete
    labelNames: Incomplete
    def __init__(self, *, name, userValue, userMinimum: Incomplete | None = None, userMaximum: Incomplete | None = None, elidable: bool = False, olderSibling: bool = False, linkedUserValue: Incomplete | None = None, labelNames: Incomplete | None = None) -> None: ...
    def getFormat(self) -> int:
        """Determine which format of STAT Axis value to use to encode this label.

        ===========  =========  ===========  ===========  ===============
        STAT Format  userValue  userMinimum  userMaximum  linkedUserValue
        ===========  =========  ===========  ===========  ===============
        1            ✅          ❌            ❌            ❌
        2            ✅          ✅            ✅            ❌
        3            ✅          ❌            ❌            ✅
        ===========  =========  ===========  ===========  ===============
        """
    @property
    def defaultName(self) -> str:
        """Return the English name from :attr:`labelNames` or the :attr:`name`."""

class LocationLabelDescriptor(SimpleDescriptor):
    """Container for location label data.

    Analogue of OpenType's STAT data for a free-floating location (format 4).
    All values are user values.

    See: `OTSpec STAT Axis value table, format 4 <https://docs.microsoft.com/en-us/typography/opentype/spec/stat#axis-value-table-format-4>`_

    .. versionadded:: 5.0
    """
    flavor: str
    name: Incomplete
    userLocation: Incomplete
    elidable: Incomplete
    olderSibling: Incomplete
    labelNames: Incomplete
    def __init__(self, *, name, userLocation, elidable: bool = False, olderSibling: bool = False, labelNames: Incomplete | None = None) -> None: ...
    @property
    def defaultName(self) -> str:
        """Return the English name from :attr:`labelNames` or the :attr:`name`."""
    def getFullUserLocation(self, doc: DesignSpaceDocument) -> SimpleLocationDict:
        """Get the complete user location of this label, by combining data
        from the explicit user location and default axis values.

        .. versionadded:: 5.0
        """

class VariableFontDescriptor(SimpleDescriptor):
    """Container for variable fonts, sub-spaces of the Designspace.

    Use-cases:

    - From a single DesignSpace with discrete axes, define 1 variable font
      per value on the discrete axes. Before version 5, you would have needed
      1 DesignSpace per such variable font, and a lot of data duplication.
    - From a big variable font with many axes, define subsets of that variable
      font that only include some axes and freeze other axes at a given location.

    .. versionadded:: 5.0
    """
    flavor: str
    filename: Incomplete
    name: Incomplete
    axisSubsets: Incomplete
    lib: Incomplete
    def __init__(self, *, name, filename: Incomplete | None = None, axisSubsets: Incomplete | None = None, lib: Incomplete | None = None) -> None: ...

class RangeAxisSubsetDescriptor(SimpleDescriptor):
    """Subset of a continuous axis to include in a variable font.

    .. versionadded:: 5.0
    """
    flavor: str
    name: Incomplete
    userMinimum: Incomplete
    userDefault: Incomplete
    userMaximum: Incomplete
    def __init__(self, *, name, userMinimum=..., userDefault: Incomplete | None = None, userMaximum=...) -> None: ...

class ValueAxisSubsetDescriptor(SimpleDescriptor):
    """Single value of a discrete or continuous axis to use in a variable font.

    .. versionadded:: 5.0
    """
    flavor: str
    name: Incomplete
    userValue: Incomplete
    def __init__(self, *, name, userValue) -> None: ...

class BaseDocWriter:
    axisDescriptorClass = AxisDescriptor
    discreteAxisDescriptorClass = DiscreteAxisDescriptor
    axisLabelDescriptorClass = AxisLabelDescriptor
    axisMappingDescriptorClass = AxisMappingDescriptor
    locationLabelDescriptorClass = LocationLabelDescriptor
    ruleDescriptorClass = RuleDescriptor
    sourceDescriptorClass = SourceDescriptor
    variableFontDescriptorClass = VariableFontDescriptor
    valueAxisSubsetDescriptorClass = ValueAxisSubsetDescriptor
    rangeAxisSubsetDescriptorClass = RangeAxisSubsetDescriptor
    instanceDescriptorClass = InstanceDescriptor
    @classmethod
    def getAxisDecriptor(cls): ...
    @classmethod
    def getAxisMappingDescriptor(cls): ...
    @classmethod
    def getSourceDescriptor(cls): ...
    @classmethod
    def getInstanceDescriptor(cls): ...
    @classmethod
    def getRuleDescriptor(cls): ...
    path: Incomplete
    documentObject: Incomplete
    effectiveFormatTuple: Incomplete
    root: Incomplete
    def __init__(self, documentPath, documentObject: DesignSpaceDocument) -> None: ...
    def write(self, pretty: bool = True, encoding: str = 'UTF-8', xml_declaration: bool = True) -> None: ...
    def intOrFloat(self, num): ...

class BaseDocReader(LogMixin):
    axisDescriptorClass = AxisDescriptor
    discreteAxisDescriptorClass = DiscreteAxisDescriptor
    axisLabelDescriptorClass = AxisLabelDescriptor
    axisMappingDescriptorClass = AxisMappingDescriptor
    locationLabelDescriptorClass = LocationLabelDescriptor
    ruleDescriptorClass = RuleDescriptor
    sourceDescriptorClass = SourceDescriptor
    variableFontsDescriptorClass = VariableFontDescriptor
    valueAxisSubsetDescriptorClass = ValueAxisSubsetDescriptor
    rangeAxisSubsetDescriptorClass = RangeAxisSubsetDescriptor
    instanceDescriptorClass = InstanceDescriptor
    path: Incomplete
    documentObject: Incomplete
    root: Incomplete
    rules: Incomplete
    sources: Incomplete
    instances: Incomplete
    axisDefaults: Incomplete
    def __init__(self, documentPath, documentObject) -> None: ...
    @classmethod
    def fromstring(cls, string, documentObject): ...
    def read(self) -> None: ...
    def readRules(self) -> None: ...
    def readAxes(self) -> None: ...
    def readAxisLabel(self, element: ET.Element): ...
    def readLabels(self) -> None: ...
    def readVariableFonts(self) -> None: ...
    def readAxisSubset(self, element: ET.Element): ...
    def readSources(self) -> None: ...
    def locationFromElement(self, element):
        """Read a nested ``<location>`` element inside the given ``element``.

        .. versionchanged:: 5.0
           Return a tuple of (designLocation, userLocation)
        """
    def readLocationElement(self, locationElement):
        """Read a ``<location>`` element.

        .. versionchanged:: 5.0
           Return a tuple of (designLocation, userLocation)
        """
    def readInstances(self, makeGlyphs: bool = True, makeKerning: bool = True, makeInfo: bool = True) -> None: ...
    def readLibElement(self, libElement, instanceObject) -> None:
        """Read the lib element for the given instance."""
    def readInfoElement(self, infoElement, instanceObject) -> None:
        """Read the info element."""
    def readGlyphElement(self, glyphElement, instanceObject) -> None:
        '''
        Read the glyph element, which could look like either one of these:

        .. code-block:: xml

            <glyph name="b" unicode="0x62"/>

            <glyph name="b"/>

            <glyph name="b">
                <master location="location-token-bbb" source="master-token-aaa2"/>
                <master glyphname="b.alt1" location="location-token-ccc" source="master-token-aaa3"/>
                <note>
                    This is an instance from an anisotropic interpolation.
                </note>
            </glyph>
        '''
    def readLib(self) -> None:
        """Read the lib element for the whole document."""

class DesignSpaceDocument(LogMixin, AsDictMixin):
    '''The DesignSpaceDocument object can read and write ``.designspace`` data.
    It imports the axes, sources, variable fonts and instances to very basic
    **descriptor** objects that store the data in attributes. Data is added to
    the document by creating such descriptor objects, filling them with data
    and then adding them to the document. This makes it easy to integrate this
    object in different contexts.

    The **DesignSpaceDocument** object can be subclassed to work with
    different objects, as long as they have the same attributes. Reader and
    Writer objects can be subclassed as well.

    **Note:** Python attribute names are usually camelCased, the
    corresponding `XML <document-xml-structure>`_ attributes are usually
    all lowercase.

    .. code:: python

        from fontTools.designspaceLib import DesignSpaceDocument
        doc = DesignSpaceDocument.fromfile("some/path/to/my.designspace")
        doc.formatVersion
        doc.elidedFallbackName
        doc.axes
        doc.axisMappings
        doc.locationLabels
        doc.rules
        doc.rulesProcessingLast
        doc.sources
        doc.variableFonts
        doc.instances
        doc.lib

    '''
    path: Incomplete
    filename: Incomplete
    formatVersion: Incomplete
    elidedFallbackName: Incomplete
    axes: Incomplete
    axisMappings: Incomplete
    locationLabels: Incomplete
    rules: Incomplete
    rulesProcessingLast: bool
    sources: Incomplete
    variableFonts: Incomplete
    instances: Incomplete
    lib: Incomplete
    default: Incomplete
    readerClass: Incomplete
    writerClass: Incomplete
    def __init__(self, readerClass: Incomplete | None = None, writerClass: Incomplete | None = None) -> None: ...
    @classmethod
    def fromfile(cls, path, readerClass: Incomplete | None = None, writerClass: Incomplete | None = None):
        """Read a designspace file from ``path`` and return a new instance of
        :class:.
        """
    @classmethod
    def fromstring(cls, string, readerClass: Incomplete | None = None, writerClass: Incomplete | None = None): ...
    def tostring(self, encoding: Incomplete | None = None):
        """Returns the designspace as a string. Default encoding ``utf-8``."""
    def read(self, path) -> None:
        """Read a designspace file from ``path`` and populates the fields of
        ``self`` with the data.
        """
    def write(self, path) -> None:
        """Write this designspace to ``path``."""
    def updatePaths(self) -> None:
        '''
        Right before we save we need to identify and respond to the following situations:
        In each descriptor, we have to do the right thing for the filename attribute.

        ::

            case 1.
            descriptor.filename == None
            descriptor.path == None

            -- action:
            write as is, descriptors will not have a filename attr.
            useless, but no reason to interfere.


            case 2.
            descriptor.filename == "../something"
            descriptor.path == None

            -- action:
            write as is. The filename attr should not be touched.


            case 3.
            descriptor.filename == None
            descriptor.path == "~/absolute/path/there"

            -- action:
            calculate the relative path for filename.
            We\'re not overwriting some other value for filename, it should be fine


            case 4.
            descriptor.filename == \'../somewhere\'
            descriptor.path == "~/absolute/path/there"

            -- action:
            there is a conflict between the given filename, and the path.
            So we know where the file is relative to the document.
            Can\'t guess why they\'re different, we just choose for path to be correct and update filename.
        '''
    def addSource(self, sourceDescriptor: SourceDescriptor):
        """Add the given ``sourceDescriptor`` to ``doc.sources``."""
    def addSourceDescriptor(self, **kwargs):
        """Instantiate a new :class:`SourceDescriptor` using the given
        ``kwargs`` and add it to ``doc.sources``.
        """
    def addInstance(self, instanceDescriptor: InstanceDescriptor):
        """Add the given ``instanceDescriptor`` to :attr:`instances`."""
    def addInstanceDescriptor(self, **kwargs):
        """Instantiate a new :class:`InstanceDescriptor` using the given
        ``kwargs`` and add it to :attr:`instances`.
        """
    def addAxis(self, axisDescriptor: AxisDescriptor | DiscreteAxisDescriptor):
        """Add the given ``axisDescriptor`` to :attr:`axes`."""
    def addAxisDescriptor(self, **kwargs):
        """Instantiate a new :class:`AxisDescriptor` using the given
        ``kwargs`` and add it to :attr:`axes`.

        The axis will be and instance of :class:`DiscreteAxisDescriptor` if
        the ``kwargs`` provide a ``value``, or a :class:`AxisDescriptor` otherwise.
        """
    def addAxisMapping(self, axisMappingDescriptor: AxisMappingDescriptor):
        """Add the given ``axisMappingDescriptor`` to :attr:`axisMappings`."""
    def addAxisMappingDescriptor(self, **kwargs):
        """Instantiate a new :class:`AxisMappingDescriptor` using the given
        ``kwargs`` and add it to :attr:`rules`.
        """
    def addRule(self, ruleDescriptor: RuleDescriptor):
        """Add the given ``ruleDescriptor`` to :attr:`rules`."""
    def addRuleDescriptor(self, **kwargs):
        """Instantiate a new :class:`RuleDescriptor` using the given
        ``kwargs`` and add it to :attr:`rules`.
        """
    def addVariableFont(self, variableFontDescriptor: VariableFontDescriptor):
        """Add the given ``variableFontDescriptor`` to :attr:`variableFonts`.

        .. versionadded:: 5.0
        """
    def addVariableFontDescriptor(self, **kwargs):
        """Instantiate a new :class:`VariableFontDescriptor` using the given
        ``kwargs`` and add it to :attr:`variableFonts`.

        .. versionadded:: 5.0
        """
    def addLocationLabel(self, locationLabelDescriptor: LocationLabelDescriptor):
        """Add the given ``locationLabelDescriptor`` to :attr:`locationLabels`.

        .. versionadded:: 5.0
        """
    def addLocationLabelDescriptor(self, **kwargs):
        """Instantiate a new :class:`LocationLabelDescriptor` using the given
        ``kwargs`` and add it to :attr:`locationLabels`.

        .. versionadded:: 5.0
        """
    def newDefaultLocation(self):
        """Return a dict with the default location in design space coordinates."""
    def labelForUserLocation(self, userLocation: SimpleLocationDict) -> LocationLabelDescriptor | None:
        """Return the :class:`LocationLabel` that matches the given
        ``userLocation``, or ``None`` if no such label exists.

        .. versionadded:: 5.0
        """
    def updateFilenameFromPath(self, masters: bool = True, instances: bool = True, force: bool = False) -> None:
        """Set a descriptor filename attr from the path and this document path.

        If the filename attribute is not None: skip it.
        """
    def newAxisDescriptor(self):
        """Ask the writer class to make us a new axisDescriptor."""
    def newSourceDescriptor(self):
        """Ask the writer class to make us a new sourceDescriptor."""
    def newInstanceDescriptor(self):
        """Ask the writer class to make us a new instanceDescriptor."""
    def getAxisOrder(self):
        """Return a list of axis names, in the same order as defined in the document."""
    def getAxis(self, name: str) -> AxisDescriptor | DiscreteAxisDescriptor | None:
        """Return the axis with the given ``name``, or ``None`` if no such axis exists."""
    def getAxisByTag(self, tag: str) -> AxisDescriptor | DiscreteAxisDescriptor | None:
        """Return the axis with the given ``tag``, or ``None`` if no such axis exists."""
    def getLocationLabel(self, name: str) -> LocationLabelDescriptor | None:
        """Return the top-level location label with the given ``name``, or
        ``None`` if no such label exists.

        .. versionadded:: 5.0
        """
    def map_forward(self, userLocation: SimpleLocationDict) -> SimpleLocationDict:
        """Map a user location to a design location.

        Assume that missing coordinates are at the default location for that axis.

        Note: the output won't be anisotropic, only the xvalue is set.

        .. versionadded:: 5.0
        """
    def map_backward(self, designLocation: AnisotropicLocationDict) -> SimpleLocationDict:
        """Map a design location to a user location.

        Assume that missing coordinates are at the default location for that axis.

        When the input has anisotropic locations, only the xvalue is used.

        .. versionadded:: 5.0
        """
    def findDefault(self):
        """Set and return SourceDescriptor at the default location or None.

        The default location is the set of all `default` values in user space
        of all axes.

        This function updates the document's :attr:`default` value.

        .. versionchanged:: 5.0
           Allow the default source to not specify some of the axis values, and
           they are assumed to be the default.
           See :meth:`SourceDescriptor.getFullDesignLocation()`
        """
    def normalizeLocation(self, location):
        """Return a dict with normalized axis values."""
    def normalize(self) -> None:
        """
        Normalise the geometry of this designspace:

        - scale all the locations of all masters and instances to the -1 - 0 - 1 value.
        - we need the axis data to do the scaling, so we do those last.
        """
    def loadSourceFonts(self, opener, **kwargs):
        '''Ensure SourceDescriptor.font attributes are loaded, and return list of fonts.

        Takes a callable which initializes a new font object (e.g. TTFont, or
        defcon.Font, etc.) from the SourceDescriptor.path, and sets the
        SourceDescriptor.font attribute.
        If the font attribute is already not None, it is not loaded again.
        Fonts with the same path are only loaded once and shared among SourceDescriptors.

        For example, to load UFO sources using defcon:

            designspace = DesignSpaceDocument.fromfile("path/to/my.designspace")
            designspace.loadSourceFonts(defcon.Font)

        Or to load masters as FontTools binary fonts, including extra options:

            designspace.loadSourceFonts(ttLib.TTFont, recalcBBoxes=False)

        Args:
            opener (Callable): takes one required positional argument, the source.path,
                and an optional list of keyword arguments, and returns a new font object
                loaded from the path.
            **kwargs: extra options passed on to the opener function.

        Returns:
            List of font objects in the order they appear in the sources list.
        '''
    @property
    def formatTuple(self):
        """Return the formatVersion as a tuple of (major, minor).

        .. versionadded:: 5.0
        """
    def getVariableFonts(self) -> List[VariableFontDescriptor]:
        """Return all variable fonts defined in this document, or implicit
        variable fonts that can be built from the document's continuous axes.

        In the case of Designspace documents before version 5, the whole
        document was implicitly describing a variable font that covers the
        whole space.

        In version 5 and above documents, there can be as many variable fonts
        as there are locations on discrete axes.

        .. seealso:: :func:`splitInterpolable`

        .. versionadded:: 5.0
        """
    def deepcopyExceptFonts(self):
        """Allow deep-copying a DesignSpace document without deep-copying
        attached UFO fonts or TTFont objects. The :attr:`font` attribute
        is shared by reference between the original and the copy.

        .. versionadded:: 5.0
        """
