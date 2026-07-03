from fontTools.merge.util import *
from _typeshed import Incomplete
from fontTools import cffLib as cffLib, ttLib as ttLib
from fontTools.merge.base import add_method as add_method, mergeObjects as mergeObjects
from fontTools.merge.cmap import computeMegaCmap as computeMegaCmap
from fontTools.misc.psCharStrings import T2WidthExtractor as T2WidthExtractor
from fontTools.ttLib.tables.DefaultTable import DefaultTable as DefaultTable

log: Incomplete
headFlagsMergeBitMap: Incomplete
os2FsTypeMergeBitMap: Incomplete

def mergeOs2FsType(lst): ...
def merge(self, m, tables): ...
