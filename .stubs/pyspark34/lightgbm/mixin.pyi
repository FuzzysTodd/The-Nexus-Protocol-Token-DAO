from synapse.ml.core.serialize.java_params_patch import *
from _typeshed import Incomplete

class LightGBMModelMixin:
    def saveNativeModel(self, filename, overwrite: bool = True) -> None:
        """
        Save the booster as string format to a local or WASB remote location.
        """
    def getNativeModel(self):
        """
        Get the native model serialized representation as a string.
        """
    def getFeatureImportances(self, importance_type: str = 'split'):
        '''
        Get the feature importances as a list.  The importance_type can be "split" or "gain".
        '''
    def getFeatureShaps(self, vector):
        """
        Get the local shap feature importances.
        """
    def getBoosterBestIteration(self):
        """Get the best iteration from the booster.

        Returns:
            The best iteration, if early stopping was triggered.
        """
    def getBoosterNumTotalIterations(self):
        """Get the total number of iterations trained.

        Returns:
            The total number of iterations trained.
        """
    def getBoosterNumTotalModel(self):
        """Get the total number of models trained.

        Returns:
            The total number of models.
        """
    def getBoosterNumFeatures(self):
        """Get the number of features from the booster.

        Returns:
            The number of features.
        """
    def setPredictDisableShapeCheck(self, value: Incomplete | None = None) -> None:
        """
        Set shape check or not when predict.
        """
