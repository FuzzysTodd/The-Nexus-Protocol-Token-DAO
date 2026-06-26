from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator, JavaModel as JavaModel, JavaTransformer as JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class SimpleFitMultivariateAnomaly(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        alignMode (str): An optional field, indicates how we align different variables into the same time-range which is required by the model.{Inner, Outer}
        backoffs (list): array of backoffs to use in the handler
        displayName (str): optional field, name of the model
        endTime (str): A required field, end time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.
        errorCol (str): column to hold http errors
        fillNAMethod (str): An optional field, indicates how missed values will be filled with. Can not be set to NotFill, when alignMode is Outer.{Previous, Subsequent, Linear, Zero, Fixed}
        initialPollingDelay (int): number of milliseconds to wait before first poll for result
        inputCols (list): The names of the input columns
        intermediateSaveDir (str): Blob storage location in HDFS where intermediate data is saved while training.
        maxPollingRetries (int): number of times to poll
        outputCol (str): The name of the output column
        paddingValue (int): optional field, is only useful if FillNAMethod is set to Fixed.
        pollingDelay (int): number of milliseconds to wait between polling
        slidingWindow (int): An optional field, indicates how many history points will be used to determine the anomaly score of one subsequent point.
        startTime (str): A required field, start time of data to be used for detection/generating multivariate anomaly detection model, should be date-time.
        subscriptionKey (object): the API key to use
        suppressMaxRetriesException (bool): set true to suppress the maxumimum retries exception and report in the error column
        timestampCol (str): Timestamp column name
        url (str): Url of the service
    """
    alignMode: Incomplete
    backoffs: Incomplete
    displayName: Incomplete
    endTime: Incomplete
    errorCol: Incomplete
    fillNAMethod: Incomplete
    initialPollingDelay: Incomplete
    inputCols: Incomplete
    intermediateSaveDir: Incomplete
    maxPollingRetries: Incomplete
    outputCol: Incomplete
    paddingValue: Incomplete
    pollingDelay: Incomplete
    slidingWindow: Incomplete
    startTime: Incomplete
    subscriptionKey: Incomplete
    suppressMaxRetriesException: Incomplete
    timestampCol: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, alignMode: str = 'Outer', backoffs=[100, 500, 1000], displayName: Incomplete | None = None, endTime: Incomplete | None = None, errorCol: str = 'SimpleFitMultivariateAnomaly_f60762ae77d5_error', fillNAMethod: str = 'Linear', initialPollingDelay: int = 300, inputCols: Incomplete | None = None, intermediateSaveDir: Incomplete | None = None, maxPollingRetries: int = 1000, outputCol: str = 'SimpleFitMultivariateAnomaly_f60762ae77d5_output', paddingValue: Incomplete | None = None, pollingDelay: int = 300, slidingWindow: int = 300, startTime: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, suppressMaxRetriesException: bool = False, timestampCol: str = 'timestamp', url: Incomplete | None = None) -> None: ...
    def setParams(self, alignMode: str = 'Outer', backoffs=[100, 500, 1000], displayName: Incomplete | None = None, endTime: Incomplete | None = None, errorCol: str = 'SimpleFitMultivariateAnomaly_f60762ae77d5_error', fillNAMethod: str = 'Linear', initialPollingDelay: int = 300, inputCols: Incomplete | None = None, intermediateSaveDir: Incomplete | None = None, maxPollingRetries: int = 1000, outputCol: str = 'SimpleFitMultivariateAnomaly_f60762ae77d5_output', paddingValue: Incomplete | None = None, pollingDelay: int = 300, slidingWindow: int = 300, startTime: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, suppressMaxRetriesException: bool = False, timestampCol: str = 'timestamp', url: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setAlignMode(self, value):
        """
        Args:
            alignMode: An optional field, indicates how we align different variables into the same time-range which is required by the model.{Inner, Outer}
        """
    def setBackoffs(self, value):
        """
        Args:
            backoffs: array of backoffs to use in the handler
        """
    def setDisplayName(self, value):
        """
        Args:
            displayName: optional field, name of the model
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
    def setFillNAMethod(self, value):
        """
        Args:
            fillNAMethod: An optional field, indicates how missed values will be filled with. Can not be set to NotFill, when alignMode is Outer.{Previous, Subsequent, Linear, Zero, Fixed}
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
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setPaddingValue(self, value):
        """
        Args:
            paddingValue: optional field, is only useful if FillNAMethod is set to Fixed.
        """
    def setPollingDelay(self, value):
        """
        Args:
            pollingDelay: number of milliseconds to wait between polling
        """
    def setSlidingWindow(self, value):
        """
        Args:
            slidingWindow: An optional field, indicates how many history points will be used to determine the anomaly score of one subsequent point.
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
    def setUrl(self, value):
        """
        Args:
            url: Url of the service
        """
    def getAlignMode(self):
        """
        Returns:
            alignMode: An optional field, indicates how we align different variables into the same time-range which is required by the model.{Inner, Outer}
        """
    def getBackoffs(self):
        """
        Returns:
            backoffs: array of backoffs to use in the handler
        """
    def getDisplayName(self):
        """
        Returns:
            displayName: optional field, name of the model
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
    def getFillNAMethod(self):
        """
        Returns:
            fillNAMethod: An optional field, indicates how missed values will be filled with. Can not be set to NotFill, when alignMode is Outer.{Previous, Subsequent, Linear, Zero, Fixed}
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
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getPaddingValue(self):
        """
        Returns:
            paddingValue: optional field, is only useful if FillNAMethod is set to Fixed.
        """
    def getPollingDelay(self):
        """
        Returns:
            pollingDelay: number of milliseconds to wait between polling
        """
    def getSlidingWindow(self):
        """
        Returns:
            slidingWindow: An optional field, indicates how many history points will be used to determine the anomaly score of one subsequent point.
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
    def getUrl(self):
        """
        Returns:
            url: Url of the service
        """
    def setLocation(self, value): ...
    def cleanUpIntermediateData(self) -> None: ...
