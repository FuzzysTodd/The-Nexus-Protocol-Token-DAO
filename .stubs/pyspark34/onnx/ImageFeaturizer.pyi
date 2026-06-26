from synapse.ml.onnx._ImageFeaturizer import _ImageFeaturizer

basestring = str

class ImageFeaturizer(_ImageFeaturizer):
    """

    Args:
        name (str): The name of the model in the OnnxHub
        location (str): The location of the model, either on local or HDFS
    """
    def setModelLocation(self, location): ...
    def setModel(self, name): ...
    def setMiniBatchSize(self, size): ...
