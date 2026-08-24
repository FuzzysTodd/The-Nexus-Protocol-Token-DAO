from _typeshed import Incomplete

__all__ = ['normalizeValue', 'normalizeLocation', 'supportScalar', 'piecewiseLinearMap', 'VariationModel']

def normalizeValue(v, triple, extrapolate: bool = False):
    """Normalizes value based on a min/default/max triple.

    >>> normalizeValue(400, (100, 400, 900))
    0.0
    >>> normalizeValue(100, (100, 400, 900))
    -1.0
    >>> normalizeValue(650, (100, 400, 900))
    0.5
    """
def normalizeLocation(location, axes, extrapolate: bool = False, *, validate: bool = False):
    '''Normalizes location based on axis min/default/max values from axes.

    >>> axes = {"wght": (100, 400, 900)}
    >>> normalizeLocation({"wght": 400}, axes)
    {\'wght\': 0.0}
    >>> normalizeLocation({"wght": 100}, axes)
    {\'wght\': -1.0}
    >>> normalizeLocation({"wght": 900}, axes)
    {\'wght\': 1.0}
    >>> normalizeLocation({"wght": 650}, axes)
    {\'wght\': 0.5}
    >>> normalizeLocation({"wght": 1000}, axes)
    {\'wght\': 1.0}
    >>> normalizeLocation({"wght": 0}, axes)
    {\'wght\': -1.0}
    >>> axes = {"wght": (0, 0, 1000)}
    >>> normalizeLocation({"wght": 0}, axes)
    {\'wght\': 0.0}
    >>> normalizeLocation({"wght": -1}, axes)
    {\'wght\': 0.0}
    >>> normalizeLocation({"wght": 1000}, axes)
    {\'wght\': 1.0}
    >>> normalizeLocation({"wght": 500}, axes)
    {\'wght\': 0.5}
    >>> normalizeLocation({"wght": 1001}, axes)
    {\'wght\': 1.0}
    >>> axes = {"wght": (0, 1000, 1000)}
    >>> normalizeLocation({"wght": 0}, axes)
    {\'wght\': -1.0}
    >>> normalizeLocation({"wght": -1}, axes)
    {\'wght\': -1.0}
    >>> normalizeLocation({"wght": 500}, axes)
    {\'wght\': -0.5}
    >>> normalizeLocation({"wght": 1000}, axes)
    {\'wght\': 0.0}
    >>> normalizeLocation({"wght": 1001}, axes)
    {\'wght\': 0.0}
    '''
def supportScalar(location, support, ot: bool = True, extrapolate: bool = False, axisRanges: Incomplete | None = None):
    '''Returns the scalar multiplier at location, for a master
    with support.  If ot is True, then a peak value of zero
    for support of an axis means "axis does not participate".  That
    is how OpenType Variation Font technology works.

    If extrapolate is True, axisRanges must be a dict that maps axis
    names to (axisMin, axisMax) tuples.

      >>> supportScalar({}, {})
      1.0
      >>> supportScalar({\'wght\':.2}, {})
      1.0
      >>> supportScalar({\'wght\':.2}, {\'wght\':(0,2,3)})
      0.1
      >>> supportScalar({\'wght\':2.5}, {\'wght\':(0,2,4)})
      0.75
      >>> supportScalar({\'wght\':2.5, \'wdth\':0}, {\'wght\':(0,2,4), \'wdth\':(-1,0,+1)})
      0.75
      >>> supportScalar({\'wght\':2.5, \'wdth\':.5}, {\'wght\':(0,2,4), \'wdth\':(-1,0,+1)}, ot=False)
      0.375
      >>> supportScalar({\'wght\':2.5, \'wdth\':0}, {\'wght\':(0,2,4), \'wdth\':(-1,0,+1)})
      0.75
      >>> supportScalar({\'wght\':2.5, \'wdth\':.5}, {\'wght\':(0,2,4), \'wdth\':(-1,0,+1)})
      0.75
      >>> supportScalar({\'wght\':3}, {\'wght\':(0,1,2)}, extrapolate=True, axisRanges={\'wght\':(0, 2)})
      -1.0
      >>> supportScalar({\'wght\':-1}, {\'wght\':(0,1,2)}, extrapolate=True, axisRanges={\'wght\':(0, 2)})
      -1.0
      >>> supportScalar({\'wght\':3}, {\'wght\':(0,2,2)}, extrapolate=True, axisRanges={\'wght\':(0, 2)})
      1.5
      >>> supportScalar({\'wght\':-1}, {\'wght\':(0,2,2)}, extrapolate=True, axisRanges={\'wght\':(0, 2)})
      -0.5
    '''

class VariationModel:
    """Locations must have the base master at the origin (ie. 0).

    If the extrapolate argument is set to True, then values are extrapolated
    outside the axis range.

      >>> from pprint import pprint
      >>> locations = [       {'wght':100},       {'wght':-100},       {'wght':-180},       {'wdth':+.3},       {'wght':+120,'wdth':.3},       {'wght':+120,'wdth':.2},       {},       {'wght':+180,'wdth':.3},       {'wght':+180},       ]
      >>> model = VariationModel(locations, axisOrder=['wght'])
      >>> pprint(model.locations)
      [{},
       {'wght': -100},
       {'wght': -180},
       {'wght': 100},
       {'wght': 180},
       {'wdth': 0.3},
       {'wdth': 0.3, 'wght': 180},
       {'wdth': 0.3, 'wght': 120},
       {'wdth': 0.2, 'wght': 120}]
      >>> pprint(model.deltaWeights)
      [{},
       {0: 1.0},
       {0: 1.0},
       {0: 1.0},
       {0: 1.0},
       {0: 1.0},
       {0: 1.0, 4: 1.0, 5: 1.0},
       {0: 1.0, 3: 0.75, 4: 0.25, 5: 1.0, 6: 0.6666666666666666},
       {0: 1.0,
        3: 0.75,
        4: 0.25,
        5: 0.6666666666666667,
        6: 0.4444444444444445,
        7: 0.6666666666666667}]
    """
    origLocations: Incomplete
    axisOrder: Incomplete
    extrapolate: Incomplete
    axisRanges: Incomplete
    locations: Incomplete
    mapping: Incomplete
    reverseMapping: Incomplete
    def __init__(self, locations, axisOrder: Incomplete | None = None, extrapolate: bool = False) -> None: ...
    def getSubModel(self, items):
        """Return a sub-model and the items that are not None.

        The sub-model is necessary for working with the subset
        of items when some are None.

        The sub-model is cached."""
    @staticmethod
    def computeAxisRanges(locations): ...
    @staticmethod
    def getMasterLocationsSortKeyFunc(locations, axisOrder=[]): ...
    def reorderMasters(self, master_list, mapping): ...
    def getDeltas(self, masterValues, *, round=...): ...
    def getDeltasAndSupports(self, items, *, round=...): ...
    def getScalars(self, loc):
        """Return scalars for each delta, for the given location.
        If interpolating many master-values at the same location,
        this function allows speed up by fetching the scalars once
        and using them with interpolateFromMastersAndScalars()."""
    def getMasterScalars(self, targetLocation):
        """Return multipliers for each master, for the given location.
        If interpolating many master-values at the same location,
        this function allows speed up by fetching the scalars once
        and using them with interpolateFromValuesAndScalars().

        Note that the scalars used in interpolateFromMastersAndScalars(),
        are *not* the same as the ones returned here. They are the result
        of getScalars()."""
    @staticmethod
    def interpolateFromValuesAndScalars(values, scalars):
        """Interpolate from values and scalars coefficients.

        If the values are master-values, then the scalars should be
        fetched from getMasterScalars().

        If the values are deltas, then the scalars should be fetched
        from getScalars(); in which case this is the same as
        interpolateFromDeltasAndScalars().
        """
    @staticmethod
    def interpolateFromDeltasAndScalars(deltas, scalars):
        """Interpolate from deltas and scalars fetched from getScalars()."""
    def interpolateFromDeltas(self, loc, deltas):
        """Interpolate from deltas, at location loc."""
    def interpolateFromMasters(self, loc, masterValues, *, round=...):
        """Interpolate from master-values, at location loc."""
    def interpolateFromMastersAndScalars(self, masterValues, scalars, *, round=...):
        """Interpolate from master-values, and scalars fetched from
        getScalars(), which is useful when you want to interpolate
        multiple master-values with the same location."""

def piecewiseLinearMap(v, mapping): ...
