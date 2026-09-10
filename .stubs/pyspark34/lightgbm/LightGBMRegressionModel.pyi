from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.lightgbm._LightGBMRegressionModel import _LightGBMRegressionModel
from synapse.ml.lightgbm.mixin import LightGBMModelMixin

class LightGBMRegressionModel(LightGBMModelMixin, _LightGBMRegressionModel):
    @staticmethod
    def loadNativeModelFromFile(filename):
        """
        Load the model from a native LightGBM text file.
        """
    @staticmethod
    def loadNativeModelFromString(model):
        """
        Load the model from a native LightGBM model string.
        """
