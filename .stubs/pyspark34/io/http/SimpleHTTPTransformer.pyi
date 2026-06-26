from synapse.ml.io.http._SimpleHTTPTransformer import _SimpleHTTPTransformer

basestring = str

class SimpleHTTPTransformer(_SimpleHTTPTransformer):
    def setUrl(self, value): ...
