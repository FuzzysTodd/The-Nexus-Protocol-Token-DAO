from synapse.ml.io.http._JSONOutputParser import _JSONOutputParser

basestring = str

class JSONOutputParser(_JSONOutputParser):
    def setDataType(self, value): ...
    def getDataType(self): ...
