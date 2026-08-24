import unittest
from . import sysinfo as sysinfo
from _typeshed import Incomplete

skipOnMac: Incomplete
skipOnMacOnCI: Incomplete
skipOnWindows: Incomplete
skipOnAppVeyor: Incomplete
skipOnCI: Incomplete
skipOnManylinux: Incomplete
skipOnPyPy: Incomplete
skipOnPyPyOnCI: Incomplete
skipOnPyPy3OnCI: Incomplete
skipOnPyPy3: Incomplete
skipOnPyPyOnWindows: Incomplete
skipOnPy3: Incomplete
skipOnPy37: Incomplete
skipOnPy310: Incomplete
skipOnPy312: Incomplete
skipOnPurePython: Incomplete
skipWithCExtensions: Incomplete
skipOnLibuv: Incomplete
skipOnLibuvOnWin: Incomplete
skipOnLibuvOnCI: Incomplete
skipOnLibuvOnCIOnPyPy: Incomplete
skipOnLibuvOnPyPyOnWin: Incomplete
skipOnLibuvOnTravisOnCPython27: Incomplete
skipOnLibev: Incomplete
skipOnWindows = unittest.skip
skipOnMac = unittest.skip
skipOnAppVeyor = unittest.skip
skipOnCI = unittest.skip
skipOnMacOnCI = unittest.skip
skipOnManylinux = unittest.skip
skipOnPyPy = unittest.skip
skipOnPyPyOnCI = unittest.skip
skipOnPyPyOnWindows = unittest.skip
skipOnPyPy3 = unittest.skip
skipOnPyPy3OnCI = unittest.skip
skipUnderCoverage: Incomplete
skipIf = unittest.skipIf
skipUnless = unittest.skipUnless

def skipWithoutPSUtil(reason): ...
skipOnLibuv = unittest.skip
skipOnLibuvOnCI = unittest.skip
skipOnLibuvOnCIOnPyPy = unittest.skip
skipOnLibuvOnTravisOnCPython27 = unittest.skip
skipOnLibuvOnWin = unittest.skip
skipOnLibuvOnPyPyOnWin = unittest.skip
skipOnLibev = unittest.skip

def skipWithoutResource(resource, reason: str = ''): ...
def skipWithoutExternalNetwork(reason: str = ''): ...
