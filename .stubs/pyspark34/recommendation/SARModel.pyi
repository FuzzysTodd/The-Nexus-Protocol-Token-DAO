from synapse.ml.core.schema.Utils import *
from synapse.ml.recommendation._SARModel import _SARModel

basestring = str

class SARModel(_SARModel):
    def recommendForAllUsers(self, numItems): ...
