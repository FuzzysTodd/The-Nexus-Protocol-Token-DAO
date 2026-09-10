from _typeshed import Incomplete

__all__ = ['FontBuilder']

class FontBuilder:
    font: Incomplete
    isTTF: Incomplete
    def __init__(self, unitsPerEm: Incomplete | None = None, font: Incomplete | None = None, isTTF: bool = True, glyphDataFormat: int = 0) -> None:
        """Initialize a FontBuilder instance.

        If the `font` argument is not given, a new `TTFont` will be
        constructed, and `unitsPerEm` must be given. If `isTTF` is True,
        the font will be a glyf-based TTF; if `isTTF` is False it will be
        a CFF-based OTF.

        The `glyphDataFormat` argument corresponds to the `head` table field
        that defines the format of the TrueType `glyf` table (default=0).
        TrueType glyphs historically can only contain quadratic splines and static
        components, but there's a proposal to add support for cubic Bezier curves as well
        as variable composites/components at
        https://github.com/harfbuzz/boring-expansion-spec/blob/main/glyf1.md
        You can experiment with the new features by setting `glyphDataFormat` to 1.
        A ValueError is raised if `glyphDataFormat` is left at 0 but glyphs are added
        that contain cubic splines or varcomposites. This is to prevent accidentally
        creating fonts that are incompatible with existing TrueType implementations.

        If `font` is given, it must be a `TTFont` instance and `unitsPerEm`
        must _not_ be given. The `isTTF` and `glyphDataFormat` arguments will be ignored.
        """
    def save(self, file) -> None:
        """Save the font. The 'file' argument can be either a pathname or a
        writable file object.
        """
    def setupHead(self, **values) -> None:
        """Create a new `head` table and initialize it with default values,
        which can be overridden by keyword arguments.
        """
    def updateHead(self, **values) -> None:
        """Update the head table with the fields and values passed as
        keyword arguments.
        """
    def setupGlyphOrder(self, glyphOrder) -> None:
        """Set the glyph order for the font."""
    def setupCharacterMap(self, cmapping, uvs: Incomplete | None = None, allowFallback: bool = False) -> None:
        """Build the `cmap` table for the font. The `cmapping` argument should
        be a dict mapping unicode code points as integers to glyph names.

        The `uvs` argument, when passed, must be a list of tuples, describing
        Unicode Variation Sequences. These tuples have three elements:
            (unicodeValue, variationSelector, glyphName)
        `unicodeValue` and `variationSelector` are integer code points.
        `glyphName` may be None, to indicate this is the default variation.
        Text processors will then use the cmap to find the glyph name.
        Each Unicode Variation Sequence should be an officially supported
        sequence, but this is not policed.
        """
    def setupNameTable(self, nameStrings, windows: bool = True, mac: bool = True) -> None:
        """Create the `name` table for the font. The `nameStrings` argument must
        be a dict, mapping nameIDs or descriptive names for the nameIDs to name
        record values. A value is either a string, or a dict, mapping language codes
        to strings, to allow localized name table entries.

        By default, both Windows (platformID=3) and Macintosh (platformID=1) name
        records are added, unless any of `windows` or `mac` arguments is False.

        The following descriptive names are available for nameIDs:

            copyright (nameID 0)
            familyName (nameID 1)
            styleName (nameID 2)
            uniqueFontIdentifier (nameID 3)
            fullName (nameID 4)
            version (nameID 5)
            psName (nameID 6)
            trademark (nameID 7)
            manufacturer (nameID 8)
            designer (nameID 9)
            description (nameID 10)
            vendorURL (nameID 11)
            designerURL (nameID 12)
            licenseDescription (nameID 13)
            licenseInfoURL (nameID 14)
            typographicFamily (nameID 16)
            typographicSubfamily (nameID 17)
            compatibleFullName (nameID 18)
            sampleText (nameID 19)
            postScriptCIDFindfontName (nameID 20)
            wwsFamilyName (nameID 21)
            wwsSubfamilyName (nameID 22)
            lightBackgroundPalette (nameID 23)
            darkBackgroundPalette (nameID 24)
            variationsPostScriptNamePrefix (nameID 25)
        """
    def setupOS2(self, **values) -> None:
        """Create a new `OS/2` table and initialize it with default values,
        which can be overridden by keyword arguments.
        """
    def setupCFF(self, psName, fontInfo, charStringsDict, privateDict) -> None: ...
    def setupCFF2(self, charStringsDict, fdArrayList: Incomplete | None = None, regions: Incomplete | None = None) -> None: ...
    def setupCFF2Regions(self, regions) -> None: ...
    def setupGlyf(self, glyphs, calcGlyphBounds: bool = True, validateGlyphFormat: bool = True) -> None:
        """Create the `glyf` table from a dict, that maps glyph names
        to `fontTools.ttLib.tables._g_l_y_f.Glyph` objects, for example
        as made by `fontTools.pens.ttGlyphPen.TTGlyphPen`.

        If `calcGlyphBounds` is True, the bounds of all glyphs will be
        calculated. Only pass False if your glyph objects already have
        their bounding box values set.

        If `validateGlyphFormat` is True, raise ValueError if any of the glyphs contains
        cubic curves or is a variable composite but head.glyphDataFormat=0.
        Set it to False to skip the check if you know in advance all the glyphs are
        compatible with the specified glyphDataFormat.
        """
    def setupFvar(self, axes, instances) -> None:
        """Adds an font variations table to the font.

        Args:
            axes (list): See below.
            instances (list): See below.

        ``axes`` should be a list of axes, with each axis either supplied as
        a py:class:`.designspaceLib.AxisDescriptor` object, or a tuple in the
        format ```tupletag, minValue, defaultValue, maxValue, name``.
        The ``name`` is either a string, or a dict, mapping language codes
        to strings, to allow localized name table entries.

        ```instances`` should be a list of instances, with each instance either
        supplied as a py:class:`.designspaceLib.InstanceDescriptor` object, or a
        dict with keys ``location`` (mapping of axis tags to float values),
        ``stylename`` and (optionally) ``postscriptfontname``.
        The ``stylename`` is either a string, or a dict, mapping language codes
        to strings, to allow localized name table entries.
        """
    def setupAvar(self, axes, mappings: Incomplete | None = None) -> None:
        """Adds an axis variations table to the font.

        Args:
            axes (list): A list of py:class:`.designspaceLib.AxisDescriptor` objects.
        """
    def setupGvar(self, variations) -> None: ...
    def calcGlyphBounds(self) -> None:
        """Calculate the bounding boxes of all glyphs in the `glyf` table.
        This is usually not called explicitly by client code.
        """
    def setupHorizontalMetrics(self, metrics) -> None:
        """Create a new `hmtx` table, for horizontal metrics.

        The `metrics` argument must be a dict, mapping glyph names to
        `(width, leftSidebearing)` tuples.
        """
    def setupVerticalMetrics(self, metrics) -> None:
        """Create a new `vmtx` table, for horizontal metrics.

        The `metrics` argument must be a dict, mapping glyph names to
        `(height, topSidebearing)` tuples.
        """
    def setupMetrics(self, tableTag, metrics) -> None:
        """See `setupHorizontalMetrics()` and `setupVerticalMetrics()`."""
    def setupHorizontalHeader(self, **values) -> None:
        """Create a new `hhea` table initialize it with default values,
        which can be overridden by keyword arguments.
        """
    def setupVerticalHeader(self, **values) -> None:
        """Create a new `vhea` table initialize it with default values,
        which can be overridden by keyword arguments.
        """
    def setupVerticalOrigins(self, verticalOrigins, defaultVerticalOrigin: Incomplete | None = None):
        """Create a new `VORG` table. The `verticalOrigins` argument must be
        a dict, mapping glyph names to vertical origin values.

        The `defaultVerticalOrigin` argument should be the most common vertical
        origin value. If omitted, this value will be derived from the actual
        values in the `verticalOrigins` argument.
        """
    def setupPost(self, keepGlyphNames: bool = True, **values) -> None:
        """Create a new `post` table and initialize it with default values,
        which can be overridden by keyword arguments.
        """
    def setupMaxp(self) -> None:
        """Create a new `maxp` table. This is called implicitly by FontBuilder
        itself and is usually not called by client code.
        """
    def setupDummyDSIG(self) -> None:
        """This adds an empty DSIG table to the font to make some MS applications
        happy. This does not properly sign the font.
        """
    def addOpenTypeFeatures(self, features, filename: Incomplete | None = None, tables: Incomplete | None = None, debug: bool = False) -> None:
        '''Add OpenType features to the font from a string containing
        Feature File syntax.

        The `filename` argument is used in error messages and to determine
        where to look for "include" files.

        The optional `tables` argument can be a list of OTL tables tags to
        build, allowing the caller to only build selected OTL tables. See
        `fontTools.feaLib` for details.

        The optional `debug` argument controls whether to add source debugging
        information to the font in the `Debg` table.
        '''
    def addFeatureVariations(self, conditionalSubstitutions, featureTag: str = 'rvrn') -> None:
        """Add conditional substitutions to a Variable Font.

        See `fontTools.varLib.featureVars.addFeatureVariations`.
        """
    def setupCOLR(self, colorLayers, version: Incomplete | None = None, varStore: Incomplete | None = None, varIndexMap: Incomplete | None = None, clipBoxes: Incomplete | None = None, allowLayerReuse: bool = True) -> None:
        """Build new COLR table using color layers dictionary.

        Cf. `fontTools.colorLib.builder.buildCOLR`.
        """
    def setupCPAL(self, palettes, paletteTypes: Incomplete | None = None, paletteLabels: Incomplete | None = None, paletteEntryLabels: Incomplete | None = None) -> None:
        """Build new CPAL table using list of palettes.

        Optionally build CPAL v1 table using paletteTypes, paletteLabels and
        paletteEntryLabels.

        Cf. `fontTools.colorLib.builder.buildCPAL`.
        """
    def setupStat(self, axes, locations: Incomplete | None = None, elidedFallbackName: int = 2) -> None:
        """Build a new 'STAT' table.

        See `fontTools.otlLib.builder.buildStatTable` for details about
        the arguments.
        """
