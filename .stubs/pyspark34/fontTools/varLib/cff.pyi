from .errors import VarLibCFFDictMergeError as VarLibCFFDictMergeError, VarLibCFFHintTypeMergeError as VarLibCFFHintTypeMergeError, VarLibCFFPointTypeMergeError as VarLibCFFPointTypeMergeError, VarLibMergeError as VarLibMergeError
from _typeshed import Incomplete
from fontTools import varLib as varLib
from fontTools.cffLib import FDArrayIndex as FDArrayIndex, FontDict as FontDict, TopDictIndex as TopDictIndex, VarStoreData as VarStoreData, buildOrder as buildOrder, maxStackLimit as maxStackLimit, privateDictOperators as privateDictOperators, privateDictOperators2 as privateDictOperators2, topDictOperators as topDictOperators, topDictOperators2 as topDictOperators2
from fontTools.cffLib.specializer import commandsToProgram as commandsToProgram, specializeCommands as specializeCommands
from fontTools.misc.loggingTools import deprecateFunction as deprecateFunction
from fontTools.misc.psCharStrings import T2CharString as T2CharString, T2OutlineExtractor as T2OutlineExtractor
from fontTools.misc.roundTools import roundFunc as roundFunc
from fontTools.pens.t2CharStringPen import T2CharStringPen as T2CharStringPen
from fontTools.ttLib import newTable as newTable
from fontTools.varLib.models import allEqual as allEqual
from io import BytesIO as BytesIO
from typing import NamedTuple

MergeDictError = VarLibCFFDictMergeError
MergeTypeError = VarLibCFFPointTypeMergeError

def addCFFVarStore(varFont, varModel, varDataList, masterSupports) -> None: ...
def convertCFFtoCFF2(varFont): ...
def conv_to_int(num): ...

pd_blend_fields: Incomplete

def get_private(regionFDArrays, fd_index, ri, fd_map): ...
def merge_PrivateDicts(top_dicts, vsindex_dict, var_model, fd_map) -> None:
    """
    I step through the FontDicts in the FDArray of the varfont TopDict.
    For each varfont FontDict:

    * step through each key in FontDict.Private.
    * For each key, step through each relevant source font Private dict, and
            build a list of values to blend.

    The 'relevant' source fonts are selected by first getting the right
    submodel using ``vsindex_dict[vsindex]``. The indices of the
    ``subModel.locations`` are mapped to source font list indices by
    assuming the latter order is the same as the order of the
    ``var_model.locations``. I can then get the index of each subModel
    location in the list of ``var_model.locations``.
    """
def getfd_map(varFont, fonts_list):
    """Since a subset source font may have fewer FontDicts in their
    FDArray than the default font, we have to match up the FontDicts in
    the different fonts . We do this with the FDSelect array, and by
    assuming that the same glyph will reference  matching FontDicts in
    each source font. We return a mapping from fdIndex in the default
    font to a dictionary which maps each master list index of each
    region font to the equivalent fdIndex in the region font."""

class CVarData(NamedTuple):
    varDataList: Incomplete
    masterSupports: Incomplete
    vsindex_dict: Incomplete

def merge_region_fonts(varFont, model, ordered_fonts_list, glyphOrder) -> None: ...
def merge_charstrings(glyphOrder, num_masters, top_dicts, masterModel): ...

class CFFToCFF2OutlineExtractor(T2OutlineExtractor):
    """This class is used to remove the initial width from the CFF
    charstring without trying to add the width to self.nominalWidthX,
    which is None."""
    width: Incomplete
    gotWidth: int
    def popallWidth(self, evenOdd: int = 0): ...

class MergeOutlineExtractor(CFFToCFF2OutlineExtractor):
    """Used to extract the charstring commands - including hints - from a
    CFF charstring in order to merge it as another set of region data
    into a CFF2 variable font charstring."""
    def __init__(self, pen, localSubrs, globalSubrs, nominalWidthX, defaultWidthX, private: Incomplete | None = None, blender: Incomplete | None = None) -> None: ...
    hintCount: Incomplete
    def countHints(self): ...
    def op_hstem(self, index) -> None: ...
    def op_vstem(self, index) -> None: ...
    def op_hstemhm(self, index) -> None: ...
    def op_vstemhm(self, index) -> None: ...
    def op_hintmask(self, index): ...
    def op_cntrmask(self, index): ...

class CFF2CharStringMergePen(T2CharStringPen):
    """Pen to merge Type 2 CharStrings."""
    pt_index: int
    m_index: Incomplete
    num_masters: Incomplete
    prev_move_idx: int
    seen_moveto: bool
    glyphName: Incomplete
    round: Incomplete
    def __init__(self, default_commands, glyphName, num_masters, master_idx, roundTolerance: float = 0.01) -> None: ...
    def add_point(self, point_type, pt_coords) -> None: ...
    def add_hint(self, hint_type, args) -> None: ...
    def add_hintmask(self, hint_type, abs_args) -> None: ...
    def restart(self, region_idx) -> None: ...
    def getCommands(self): ...
    def reorder_blend_args(self, commands, get_delta_func):
        """
        We first re-order the master coordinate values.
        For a moveto to lineto, the args are now arranged as::

                [ [master_0 x,y], [master_1 x,y], [master_2 x,y] ]

        We re-arrange this to::

                [\t[master_0 x, master_1 x, master_2 x],
                        [master_0 y, master_1 y, master_2 y]
                ]

        If the master values are all the same, we collapse the list to
        as single value instead of a list.

        We then convert this to::

                [ [master_0 x] + [x delta tuple] + [numBlends=1]
                  [master_0 y] + [y delta tuple] + [numBlends=1]
                ]
        """
    def getCharString(self, private: Incomplete | None = None, globalSubrs: Incomplete | None = None, var_model: Incomplete | None = None, optimize: bool = True): ...
