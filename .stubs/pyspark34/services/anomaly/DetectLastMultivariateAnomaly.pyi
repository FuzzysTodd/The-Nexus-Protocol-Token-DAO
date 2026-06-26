from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel as JavaModel, JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class DetectLastMultivariateAnomaly(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        batchSize (int): The max size of the buffer
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        diagnosticsInfo (object): diagnosticsInfo for training a multivariate anomaly detection model
        errorCol (str): column to hold http errors
        handler (object): Which strategy to use when handling requests
        inputVariablesCols (list): The names of the input variables columns
        modelId (str): Format - uuid. Model identifier.
        outputCol (str): The name of the output column
        subscriptionKey (object): the API key to use
        timeout (float): number of seconds to wait before closing the connection
        timestampCol (str): Timestamp column name
        topContributorCount (int): This is a number that you could specify N from 1 to 30, which will give you the details of top N contributed variables in the anomaly results. For example, if you have 100 variables in the model, but you only care the top five contributed variables in detection results, then you should fill this field with 5. The default number is 10.
        url (str): Url of the service
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    batchSize: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    diagnosticsInfo: Incomplete
    errorCol: Incomplete
    handler: Incomplete
    inputVariablesCols: Incomplete
    modelId: Incomplete
    outputCol: Incomplete
    subscriptionKey: Incomplete
    timeout: Incomplete
    timestampCol: Incomplete
    topContributorCount: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, batchSize: int = 300, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, diagnosticsInfo: Incomplete | None = None, errorCol: str = 'DetectLastMultivariateAnomaly_656155236608_error', handler: Incomplete | None = None, inputVariablesCols: Incomplete | None = None, modelId: Incomplete | None = None, outputCol: str = 'DetectLastMultivariateAnomaly_656155236608_output', subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, timestampCol: str = 'timestamp', topContributorCount: int = 10, url: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, batchSize: int = 300, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, diagnosticsInfo: Incomplete | None = None, errorCol: str = 'DetectLastMultivariateAnomaly_656155236608_error', handler: Incomplete | None = None, inputVariablesCols: Incomplete | None = None, modelId: Incomplete | None = None, outputCol: str = 'DetectLastMultivariateAnomaly_656155236608_output', subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, timestampCol: str = 'timestamp', topContributorCount: int = 10, url: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setAADToken(self, value):
        """
        Args:
            AADToken: AAD Token used for authentication
        """
    def setAADTokenCol(self, value):
        """
        Args:
            AADToken: AAD Token used for authentication
        """
    def setCustomAuthHeader(self, value):
        """
        Args:
            CustomAuthHeader: A Custom Value for Authorization Header
        """
    def setCustomAuthHeaderCol(self, value):
        """
        Args:
            CustomAuthHeader: A Custom Value for Authorization Header
        """
    def setBatchSize(self, value):
        """
        Args:
            batchSize: The max size of the buffer
        """
    def setConcurrency(self, value):
        """
        Args:
            concurrency: max number of concurrent calls
        """
    def setConcurrentTimeout(self, value):
        """
        Args:
            concurrentTimeout: max number seconds to wait on futures if concurrency >= 1
        """
    def setDiagnosticsInfo(self, value):
        """
        Args:
            diagnosticsInfo: diagnosticsInfo for training a multivariate anomaly detection model
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
    def setInputVariablesCols(self, value):
        """
        Args:
            inputVariablesCols: The names of the input variables columns
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
    def setTimeout(self, value):
        """
        Args:
            timeout: number of seconds to wait before closing the connection
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
    def getAADToken(self):
        """
        Returns:
            AADToken: AAD Token used for authentication
        """
    def getCustomAuthHeader(self):
        """
        Returns:
            CustomAuthHeader: A Custom Value for Authorization Header
        """
    def getBatchSize(self):
        """
        Returns:
            batchSize: The max size of the buffer
        """
    def getConcurrency(self):
        """
        Returns:
            concurrency: max number of concurrent calls
        """
    def getConcurrentTimeout(self):
        """
        Returns:
            concurrentTimeout: max number seconds to wait on futures if concurrency >= 1
        """
    def getDiagnosticsInfo(self):
        """
        Returns:
            diagnosticsInfo: diagnosticsInfo for training a multivariate anomaly detection model
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
    def getInputVariablesCols(self):
        """
        Returns:
            inputVariablesCols: The names of the input variables columns
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
    def getSubscriptionKey(self):
        """
        Returns:
            subscriptionKey: the API key to use
        """
    def getTimeout(self):
        """
        Returns:
            timeout: number of seconds to wait before closing the connection
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
    def setCustomServiceName(self, value): ...
    def setEndpoint(self, value): ...
    def setDefaultInternalEndpoint(self, value): ...
    def setLocation(self, value): ...
