from _typeshed import Incomplete
from fontTools import configLogger as configLogger
from fontTools.feaLib.builder import Builder as Builder, addOpenTypeFeatures as addOpenTypeFeatures
from fontTools.feaLib.error import FeatureLibError as FeatureLibError
from fontTools.misc.cliTools import makeOutputFileName as makeOutputFileName
from fontTools.ttLib import TTFont as TTFont

log: Incomplete

def main(args: Incomplete | None = None) -> None:
    """Add features from a feature file (.fea) into an OTF font"""
