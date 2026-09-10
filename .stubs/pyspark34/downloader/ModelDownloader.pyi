from pyspark.ml.param.shared import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete

basestring = str
DEFAULT_URL: str

class ModelSchema:
    """
    An object that represents a model.

    Args:
        name (str): Name of the model
        dataset (DataFrame): Dataset it was trained on
        modelType (str): Domain that the model operates on
        uri (str): The location of the model's bytes
        hash (str): The sha256 hash of the models bytes
        size (int): the size of the model in bytes
        inputNode (int): the node which represents the input
        numLayers (int): the number of layers of the model
        layerNames (array): the names of nodes that represent layers in the network
    """
    name: Incomplete
    dataset: Incomplete
    modelType: Incomplete
    uri: Incomplete
    hash: Incomplete
    size: Incomplete
    inputNode: Incomplete
    numLayers: Incomplete
    layerNames: Incomplete
    def __init__(self, name, dataset, modelType, uri, hash, size, inputNode, numLayers, layerNames) -> None: ...
    def toJava(self, sparkSession): ...
    @staticmethod
    def fromJava(jobj): ...

class ModelDownloader:
    """
    A class for downloading CNTK pretrained models in python. To download all models use the downloadModels
    function. To browse models from the microsoft server please use remoteModels.

    Args:
        sparkSession (SparkSession): A spark session for interfacing between python and java
        localPath (str): The folder to save models to
        serverURL (str): The location of the model Server, beware this default can change!
    """
    localPath: Incomplete
    serverURL: Incomplete
    def __init__(self, sparkSession, localPath, serverURL=...) -> None: ...
    def localModels(self):
        """
        Downloads models stored locally on the filesystem
        """
    def remoteModels(self):
        """
        Downloads models stored remotely.
        """
    def downloadModel(self, model):
        """
        Download a model

        Args:
            model (object): The model to be downloaded

        Returns:
            object: model schema
        """
    def downloadByName(self, name):
        """
        Downloads a named model

        Args:
            name (str): The name of the model
        """
    def downloadModels(self, models: Incomplete | None = None):
        """
        Download models

        Args:
            models: The models to be downloaded

        Returns:
            list: list of models downloaded
        """
