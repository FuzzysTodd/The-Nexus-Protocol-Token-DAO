from _typeshed import Incomplete

__all__ = ['planWeightAxis', 'planWidthAxis', 'planSlantAxis', 'planOpticalSizeAxis', 'planAxis', 'sanitizeWeight', 'sanitizeWidth', 'sanitizeSlant', 'measureWeight', 'measureWidth', 'measureSlant', 'normalizeLinear', 'normalizeLog', 'normalizeDegrees', 'interpolateLinear', 'interpolateLog', 'processAxis', 'makeDesignspaceSnippet', 'addEmptyAvar', 'main']

def normalizeLinear(value, rangeMin, rangeMax):
    """Linearly normalize value in [rangeMin, rangeMax] to [0, 1], with extrapolation."""
def interpolateLinear(t, a, b):
    """Linear interpolation between a and b, with t typically in [0, 1]."""
def normalizeLog(value, rangeMin, rangeMax):
    """Logarithmically normalize value in [rangeMin, rangeMax] to [0, 1], with extrapolation."""
def interpolateLog(t, a, b):
    """Logarithmic interpolation between a and b, with t typically in [0, 1]."""
def normalizeDegrees(value, rangeMin, rangeMax):
    """Angularly normalize value in [rangeMin, rangeMax] to [0, 1], with extrapolation."""
def measureWeight(glyphset, glyphs: Incomplete | None = None):
    """Measure the perceptual average weight of the given glyphs."""
def measureWidth(glyphset, glyphs: Incomplete | None = None):
    """Measure the average width of the given glyphs."""
def measureSlant(glyphset, glyphs: Incomplete | None = None):
    """Measure the perceptual average slant angle of the given glyphs."""
def sanitizeWidth(userTriple, designTriple, pins, measurements):
    """Sanitize the width axis limits."""
def sanitizeWeight(userTriple, designTriple, pins, measurements):
    """Sanitize the weight axis limits."""
def sanitizeSlant(userTriple, designTriple, pins, measurements):
    """Sanitize the slant axis limits."""
def planAxis(measureFunc, normalizeFunc, interpolateFunc, glyphSetFunc, axisTag, axisLimits, values, samples: Incomplete | None = None, glyphs: Incomplete | None = None, designLimits: Incomplete | None = None, pins: Incomplete | None = None, sanitizeFunc: Incomplete | None = None):
    '''Plan an axis.

    measureFunc: callable that takes a glyphset and an optional
    list of glyphnames, and returns the glyphset-wide measurement
    to be used for the axis.

    normalizeFunc: callable that takes a measurement and a minimum
    and maximum, and normalizes the measurement into the range 0..1,
    possibly extrapolating too.

    interpolateFunc: callable that takes a normalized t value, and a
    minimum and maximum, and returns the interpolated value,
    possibly extrapolating too.

    glyphSetFunc: callable that takes a variations "location" dictionary,
    and returns a glyphset.

    axisTag: the axis tag string.

    axisLimits: a triple of minimum, default, and maximum values for
    the axis. Or an `fvar` Axis object.

    values: a list of output values to map for this axis.

    samples: the number of samples to use when sampling. Default 8.

    glyphs: a list of glyph names to use when sampling. Defaults to None,
    which will process all glyphs.

    designLimits: an optional triple of minimum, default, and maximum values
    represenging the "design" limits for the axis. If not provided, the
    axisLimits will be used.

    pins: an optional dictionary of before/after mapping entries to pin in
    the output.

    sanitizeFunc: an optional callable to call to sanitize the axis limits.
    '''
def planWeightAxis(glyphSetFunc, axisLimits, weights: Incomplete | None = None, samples: Incomplete | None = None, glyphs: Incomplete | None = None, designLimits: Incomplete | None = None, pins: Incomplete | None = None, sanitize: bool = False):
    """Plan a weight (`wght`) axis.

    weights: A list of weight values to plan for. If None, the default
    values are used.

    This function simply calls planAxis with values=weights, and the appropriate
    arguments. See documenation for planAxis for more information.
    """
def planWidthAxis(glyphSetFunc, axisLimits, widths: Incomplete | None = None, samples: Incomplete | None = None, glyphs: Incomplete | None = None, designLimits: Incomplete | None = None, pins: Incomplete | None = None, sanitize: bool = False):
    """Plan a width (`wdth`) axis.

    widths: A list of width values (percentages) to plan for. If None, the default
    values are used.

    This function simply calls planAxis with values=widths, and the appropriate
    arguments. See documenation for planAxis for more information.
    """
def planSlantAxis(glyphSetFunc, axisLimits, slants: Incomplete | None = None, samples: Incomplete | None = None, glyphs: Incomplete | None = None, designLimits: Incomplete | None = None, pins: Incomplete | None = None, sanitize: bool = False):
    """Plan a slant (`slnt`) axis.

    slants: A list slant angles to plan for. If None, the default
    values are used.

    This function simply calls planAxis with values=slants, and the appropriate
    arguments. See documenation for planAxis for more information.
    """
def planOpticalSizeAxis(glyphSetFunc, axisLimits, sizes: Incomplete | None = None, samples: Incomplete | None = None, glyphs: Incomplete | None = None, designLimits: Incomplete | None = None, pins: Incomplete | None = None, sanitize: bool = False):
    """Plan a optical-size (`opsz`) axis.

    sizes: A list of optical size values to plan for. If None, the default
    values are used.

    This function simply calls planAxis with values=sizes, and the appropriate
    arguments. See documenation for planAxis for more information.
    """
def makeDesignspaceSnippet(axisTag, axisName, axisLimit, mapping):
    """Make a designspace snippet for a single axis."""
def addEmptyAvar(font) -> None:
    """Add an empty `avar` table to the font."""
def processAxis(font, planFunc, axisTag, axisName, values, samples: Incomplete | None = None, glyphs: Incomplete | None = None, designLimits: Incomplete | None = None, pins: Incomplete | None = None, sanitize: bool = False, plot: bool = False):
    """Process a single axis."""
def main(args: Incomplete | None = None):
    """Plan the standard axis mappings for a variable font"""
