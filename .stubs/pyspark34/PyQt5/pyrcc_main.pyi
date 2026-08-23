from .pyrcc import *
from PyQt5.QtCore import PYQT_VERSION_STR as PYQT_VERSION_STR, QDir as QDir, QFile as QFile

verbose: bool
compressLevel = CONSTANT_COMPRESSLEVEL_DEFAULT
compressThreshold = CONSTANT_COMPRESSTHRESHOLD_DEFAULT
resourceRoot: str

def processResourceFile(filenamesIn, filenameOut, listFiles): ...
def showHelp(error) -> None: ...
def main() -> None: ...
