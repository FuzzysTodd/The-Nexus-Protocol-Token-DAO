from synapse.ml.automl._BestModel import _BestModel

basestring = str

class BestModel(_BestModel):
    def getBestModel(self):
        """
        Returns the best model.
        """
    def getScoredDataset(self):
        """
        Returns scored dataset for the best model.
        """
    def getEvaluationResults(self):
        """
        Returns the ROC curve with TPR, FPR.
        """
    def getBestModelMetrics(self):
        """
        Returns all of the best model metrics results from the evaluator.
        """
    def getAllModelMetrics(self):
        """
        Returns a table of metrics from all models compared from the evaluation comparison.
        """
