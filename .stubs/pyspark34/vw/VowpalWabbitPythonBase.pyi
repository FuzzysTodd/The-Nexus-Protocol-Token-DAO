from pyspark.ml.common import inherit_doc as inherit_doc

def to_java_params(sc, model, pyParamMap): ...

class VowpalWabbitPythonBase:
    def setInitialModel(self, model) -> None:
        """
        Initialize the estimator with a previously trained model.
        """
    def parallelFit(self, dataset, param_maps): ...

class VowpalWabbitPythonBaseModel:
    def saveNativeModel(self, filename) -> None:
        """
        Save the native model to a local or WASB remote location.
        """
    def getNativeModel(self):
        """
        Get the binary native VW model.
        """
    def getReadableModel(self): ...
    def getPerformanceStatistics(self): ...
