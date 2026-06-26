from synapse.ml.explainers._ICETransformer import _ICETransformer
from typing import Dict, List

class ICETransformer(_ICETransformer):
    def setCategoricalFeatures(self, values: List[str | Dict]):
        """
        Args:
        values: The list of values that represent categorical features to explain.
        Values are list of dicts with parameters or just a list of names of categorical features
        """
    def setNumericFeatures(self, values: List[str | Dict]):
        """
        Args:
        values: The list of values that represent numeric features to explain.
        Values are list of dicts with parameters or just a list of names of numeric features
        """
