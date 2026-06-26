from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.lightgbm._LightGBMRankerModel import _LightGBMRankerModel
from synapse.ml.lightgbm.mixin import LightGBMModelMixin

class LightGBMRankerModel(LightGBMModelMixin, _LightGBMRankerModel):
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
    def getBoosterNumClasses(self):
        """Get the number of classes from the booster.

        Returns:
            The number of classes.
        """
