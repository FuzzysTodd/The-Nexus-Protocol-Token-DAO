from _typeshed import Incomplete
from fontTools.ttLib import TTFont as TTFont
from fontTools.varLib import VarLibError as VarLibError, load_designspace as load_designspace, load_masters as load_masters, models as models
from fontTools.varLib.merger import InstancerMerger as InstancerMerger

log: Incomplete

def interpolate_layout(designspace, loc, master_finder=..., mapped: bool = False):
    """
    Interpolate GPOS from a designspace file and location.

    If master_finder is set, it should be a callable that takes master
    filename as found in designspace file and map it to master font
    binary as to be opened (eg. .ttf or .otf).

    If mapped is False (default), then location is mapped using the
    map element of the axes in designspace file.  If mapped is True,
    it is assumed that location is in designspace's internal space and
    no mapping is performed.
    """
def main(args: Incomplete | None = None):
    """Interpolate GDEF/GPOS/GSUB tables for a point on a designspace"""
