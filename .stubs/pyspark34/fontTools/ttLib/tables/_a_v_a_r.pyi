from . import DefaultTable as DefaultTable, otTables as otTables
from .otBase import BaseTTXConverter as BaseTTXConverter
from _typeshed import Incomplete
from fontTools.misc import sstruct as sstruct
from fontTools.misc.roundTools import otRound as otRound
from fontTools.misc.textTools import bytesjoin as bytesjoin, safeEval as safeEval
from fontTools.ttLib import TTLibError as TTLibError
from fontTools.varLib.models import piecewiseLinearMap as piecewiseLinearMap
from fontTools.varLib.varStore import NO_VARIATION_INDEX as NO_VARIATION_INDEX, VarStoreInstancer as VarStoreInstancer

log: Incomplete

class table__a_v_a_r(BaseTTXConverter):
    '''Axis Variations Table

    This class represents the ``avar`` table of a variable font. The object has one
    substantive attribute, ``segments``, which maps axis tags to a segments dictionary::

        >>> font["avar"].segments   # doctest: +SKIP
        {\'wght\': {-1.0: -1.0,
          0.0: 0.0,
          0.125: 0.11444091796875,
          0.25: 0.23492431640625,
          0.5: 0.35540771484375,
          0.625: 0.5,
          0.75: 0.6566162109375,
          0.875: 0.81927490234375,
          1.0: 1.0},
         \'ital\': {-1.0: -1.0, 0.0: 0.0, 1.0: 1.0}}

    Notice that the segments dictionary is made up of normalized values. A valid
    ``avar`` segment mapping must contain the entries ``-1.0: -1.0, 0.0: 0.0, 1.0: 1.0``.
    fontTools does not enforce this, so it is your responsibility to ensure that
    mappings are valid.
    '''
    dependencies: Incomplete
    segments: Incomplete
    def __init__(self, tag: Incomplete | None = None) -> None: ...
    table: Incomplete
    def compile(self, ttFont): ...
    majorVersion: Incomplete
    minorVersion: Incomplete
    def decompile(self, data, ttFont) -> None: ...
    def toXML(self, writer, ttFont) -> None: ...
    def fromXML(self, name, attrs, content, ttFont) -> None: ...
    def renormalizeLocation(self, location, font): ...
