from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel, JavaTransformer as JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class SimpleDetectMultivariateAnomaly(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaModel):
    """
    Args:
        backoffs (list): array of backoffs to use in the handler
        diagnosticsInfo (object): diagnosticsInfo for training a multivariate anomaly detection model
        endTime (str): A required field, end time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.
        errorCol (str): column to hold http errors
        handler (object): Which strategy to use when handling requests
        initialPollingDelay (int): number of milliseconds to wait before first poll for result
        inputCols (list): The names of the input columns
        intermediateSaveDir (str): Blob storage location in HDFS where intermediate data is saved while training.
        maxPollingRetries (int): number of times to poll
        modelId (str): Format - uuid. Model identifier.
        outputCol (str): The name of the output column
        pollingDelay (int): number of milliseconds to wait between polling
        startTime (str): A required field, start time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.
        subscriptionKey (object): the API key to use
        suppressMaxRetriesException (bool): set true to suppress the maxumimum retries exception and report in the error column
        timestampCol (str): Timestamp column name
        topContributorCount (int): This is a number that you could specify N from 1 to 30, which will give you the details of top N contributed variables in the anomaly results. For example, if you have 100 variables in the model, but you only care the top five contributed variables in detection results, then you should fill this field with 5. The default number is 10.
        url (str): Url of the service
    """
    backoffs: Incomplete
    diagnosticsInfo: Incomplete
    endTime: Incomplete
    errorCol: Incomplete
    handler: Incomplete
    initialPollingDelay: Incomplete
    inputCols: Incomplete
    intermediateSaveDir: Incomplete
    maxPollingRetries: Incomplete
    modelId: Incomplete
    outputCol: Incomplete
    pollingDelay: Incomplete
    startTime: Incomplete
    subscriptionKey: Incomplete
    suppressMaxRetriesException: Incomplete
    timestampCol: Incomplete
    topContributorCount: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, backoffs=[100, 500, 1000], diagnosticsInfo: Incomplete | None = None, endTime: Incomplete | None = None, errorCol: str = 'SimpleDetectMultivariateAnomaly_5da78e72489a_error', handler: Incomplete | None = None, initialPollingDelay: int = 300, inputCols: Incomplete | None = None, intermediateSaveDir: Incomplete | None = None, maxPollingRetries: int = 1000, modelId: Incomplete | None = None, outputCol: str = 'SimpleDetectMultivariateAnomaly_5da78e72489a_output', pollingDelay: int = 300, startTime: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, suppressMaxRetriesException: bool = False, timestampCol: str = 'timestamp', topContributorCount: int = 10, url: Incomplete | None = None) -> None: ...
    def setParams(self, backoffs=[100, 500, 1000], diagnosticsInfo: Incomplete | None = None, endTime: Incomplete | None = None, errorCol: str = 'SimpleDetectMultivariateAnomaly_5da78e72489a_error', handler: Incomplete | None = None, initialPollingDelay: int = 300, inputCols: Incomplete | None = None, intermediateSaveDir: Incomplete | None = None, maxPollingRetries: int = 1000, modelId: Incomplete | None = None, outputCol: str = 'SimpleDetectMultivariateAnomaly_5da78e72489a_output', pollingDelay: int = 300, startTime: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, suppressMaxRetriesException: bool = False, timestampCol: str = 'timestamp', topContributorCount: int = 10, url: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setBackoffs(self, value):
        """
        Args:
            backoffs: array of backoffs to use in the handler
        """
    def setDiagnosticsInfo(self, value):
        """
        Args:
            diagnosticsInfo: diagnosticsInfo for training a multivariate anomaly detection model
        """
    def setEndTime(self, value):
        """
        Args:
            endTime: A required field, end time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.
        """
    def setErrorCol(self, value):
        """
        Args:
            errorCol: column to hold http errors
        """
    def setHandler(self, value):
        """
        Args:
            handler: Which strategy to use when handling requests
        """
    def setInitialPollingDelay(self, value):
        """
        Args:
            initialPollingDelay: number of milliseconds to wait before first poll for result
        """
    def setInputCols(self, value):
        """
        Args:
            inputCols: The names of the input columns
        """
    def setIntermediateSaveDir(self, value):
        """
        Args:
            intermediateSaveDir: Blob storage location in HDFS where intermediate data is saved while training.
        """
    def setMaxPollingRetries(self, value):
        """
        Args:
            maxPollingRetries: number of times to poll
        """
    def setModelId(self, value):
        """
        Args:
            modelId: Format - uuid. Model identifier.
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setPollingDelay(self, value):
        """
        Args:
            pollingDelay: number of milliseconds to wait between polling
        """
    def setStartTime(self, value):
        """
        Args:
            startTime: A required field, start time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.
        """
    def setSubscriptionKey(self, value):
        """
        Args:
            subscriptionKey: the API key to use
        """
    def setSubscriptionKeyCol(self, value):
        """
        Args:
            subscriptionKey: the API key to use
        """
    def setSuppressMaxRetriesException(self, value):
        """
        Args:
            suppressMaxRetriesException: set true to suppress the maxumimum retries exception and report in the error column
        """
    def setTimestampCol(self, value):
        """
        Args:
            timestampCol: Timestamp column name
        """
    def setTopContributorCount(self, value):
        """
        Args:
            topContributorCount: This is a number that you could specify N from 1 to 30, which will give you the details of top N contributed variables in the anomaly results. For example, if you have 100 variables in the model, but you only care the top five contributed variables in detection results, then you should fill this field with 5. The default number is 10.
        """
    def setUrl(self, value):
        """
        Args:
            url: Url of the service
        """
    def getBackoffs(self):
        """
        Returns:
            backoffs: array of backoffs to use in the handler
        """
    def getDiagnosticsInfo(self):
        """
        Returns:
            diagnosticsInfo: diagnosticsInfo for training a multivariate anomaly detection model
        """
    def getEndTime(self):
        """
        Returns:
            endTime: A required field, end time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.
        """
    def getErrorCol(self):
        """
        Returns:
            errorCol: column to hold http errors
        """
    def getHandler(self):
        """
        Returns:
            handler: Which strategy to use when handling requests
        """
    def getInitialPollingDelay(self):
        """
        Returns:
            initialPollingDelay: number of milliseconds to wait before first poll for result
        """
    def getInputCols(self):
        """
        Returns:
            inputCols: The names of the input columns
        """
    def getIntermediateSaveDir(self):
        """
        Returns:
            intermediateSaveDir: Blob storage location in HDFS where intermediate data is saved while training.
        """
    def getMaxPollingRetries(self):
        """
        Returns:
            maxPollingRetries: number of times to poll
        """
    def getModelId(self):
        """
        Returns:
            modelId: Format - uuid. Model identifier.
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getPollingDelay(self):
        """
        Returns:
            pollingDelay: number of milliseconds to wait between polling
        """
    def getStartTime(self):
        """
        Returns:
            startTime: A required field, start time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.
        """
    def getSubscriptionKey(self):
        """
        Returns:
            subscriptionKey: the API key to use
        """
    def getSuppressMaxRetriesException(self):
        """
        Returns:
            suppressMaxRetriesException: set true to suppress the maxumimum retries exception and report in the error column
        """
    def getTimestampCol(self):
        """
        Returns:
            timestampCol: Timestamp column name
        """
    def getTopContributorCount(self):
        """
        Returns:
            topContributorCount: This is a number that you could specify N from 1 to 30, which will give you the details of top N contributed variables in the anomaly results. For example, if you have 100 variables in the model, but you only care the top five contributed variables in detection results, then you should fill this field with 5. The default number is 10.
        """
    def getUrl(self):
        """
        Returns:
            url: Url of the service
        """
    def setLocation(self, value): ...
    def cleanUpIntermediateData(self) -> None: ...
