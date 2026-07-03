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

class AnalyzeHealthText(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        backoffs (list): array of backoffs to use in the handler
        batchSize (int): The max size of the buffer
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        disableServiceLogs (object): disableServiceLogs option
        errorCol (str): column to hold http errors
        initialPollingDelay (int): number of milliseconds to wait before first poll for result
        language (object): the language code of the text (optional for some services)
        maxPollingRetries (int): number of times to poll
        modelVersion (object): Version of the model
        outputCol (str): The name of the output column
        pollingDelay (int): number of milliseconds to wait between polling
        showStats (object): Whether to include detailed statistics in the response
        stringIndexType (object): Specifies the method used to interpret string offsets. Defaults to Text Elements (Graphemes) according to Unicode v8.0.0. For additional information see https://aka.ms/text-analytics-offsets
        subscriptionKey (object): the API key to use
        suppressMaxRetriesException (bool): set true to suppress the maxumimum retries exception and report in the error column
        text (object): the text in the request body
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    backoffs: Incomplete
    batchSize: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    disableServiceLogs: Incomplete
    errorCol: Incomplete
    initialPollingDelay: Incomplete
    language: Incomplete
    maxPollingRetries: Incomplete
    modelVersion: Incomplete
    outputCol: Incomplete
    pollingDelay: Incomplete
    showStats: Incomplete
    stringIndexType: Incomplete
    subscriptionKey: Incomplete
    suppressMaxRetriesException: Incomplete
    text: Incomplete
    timeout: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, backoffs=[100, 500, 1000], batchSize: int = 10, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, disableServiceLogs: Incomplete | None = None, disableServiceLogsCol: Incomplete | None = None, errorCol: str = 'AnalyzeHealthText_72ffb094a8c1_error', initialPollingDelay: int = 300, language: Incomplete | None = None, languageCol: Incomplete | None = None, maxPollingRetries: int = 1000, modelVersion: Incomplete | None = None, modelVersionCol: Incomplete | None = None, outputCol: str = 'AnalyzeHealthText_72ffb094a8c1_output', pollingDelay: int = 300, showStats: Incomplete | None = None, showStatsCol: Incomplete | None = None, stringIndexType: Incomplete | None = None, stringIndexTypeCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, suppressMaxRetriesException: bool = False, text: Incomplete | None = None, textCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, backoffs=[100, 500, 1000], batchSize: int = 10, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, disableServiceLogs: Incomplete | None = None, disableServiceLogsCol: Incomplete | None = None, errorCol: str = 'AnalyzeHealthText_72ffb094a8c1_error', initialPollingDelay: int = 300, language: Incomplete | None = None, languageCol: Incomplete | None = None, maxPollingRetries: int = 1000, modelVersion: Incomplete | None = None, modelVersionCol: Incomplete | None = None, outputCol: str = 'AnalyzeHealthText_72ffb094a8c1_output', pollingDelay: int = 300, showStats: Incomplete | None = None, showStatsCol: Incomplete | None = None, stringIndexType: Incomplete | None = None, stringIndexTypeCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, suppressMaxRetriesException: bool = False, text: Incomplete | None = None, textCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None):
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
    def setBackoffs(self, value):
        """
        Args:
            backoffs: array of backoffs to use in the handler
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
    def setDisableServiceLogs(self, value):
        """
        Args:
            disableServiceLogs: disableServiceLogs option
        """
    def setDisableServiceLogsCol(self, value):
        """
        Args:
            disableServiceLogs: disableServiceLogs option
        """
    def setErrorCol(self, value):
        """
        Args:
            errorCol: column to hold http errors
        """
    def setInitialPollingDelay(self, value):
        """
        Args:
            initialPollingDelay: number of milliseconds to wait before first poll for result
        """
    def setLanguage(self, value):
        """
        Args:
            language: the language code of the text (optional for some services)
        """
    def setLanguageCol(self, value):
        """
        Args:
            language: the language code of the text (optional for some services)
        """
    def setMaxPollingRetries(self, value):
        """
        Args:
            maxPollingRetries: number of times to poll
        """
    def setModelVersion(self, value):
        """
        Args:
            modelVersion: Version of the model
        """
    def setModelVersionCol(self, value):
        """
        Args:
            modelVersion: Version of the model
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
    def setShowStats(self, value):
        """
        Args:
            showStats: Whether to include detailed statistics in the response
        """
    def setShowStatsCol(self, value):
        """
        Args:
            showStats: Whether to include detailed statistics in the response
        """
    def setStringIndexType(self, value):
        """
        Args:
            stringIndexType: Specifies the method used to interpret string offsets. Defaults to Text Elements (Graphemes) according to Unicode v8.0.0. For additional information see https://aka.ms/text-analytics-offsets
        """
    def setStringIndexTypeCol(self, value):
        """
        Args:
            stringIndexType: Specifies the method used to interpret string offsets. Defaults to Text Elements (Graphemes) according to Unicode v8.0.0. For additional information see https://aka.ms/text-analytics-offsets
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
    def setText(self, value):
        """
        Args:
            text: the text in the request body
        """
    def setTextCol(self, value):
        """
        Args:
            text: the text in the request body
        """
    def setTimeout(self, value):
        """
        Args:
            timeout: number of seconds to wait before closing the connection
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
    def getBackoffs(self):
        """
        Returns:
            backoffs: array of backoffs to use in the handler
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
    def getDisableServiceLogs(self):
        """
        Returns:
            disableServiceLogs: disableServiceLogs option
        """
    def getErrorCol(self):
        """
        Returns:
            errorCol: column to hold http errors
        """
    def getInitialPollingDelay(self):
        """
        Returns:
            initialPollingDelay: number of milliseconds to wait before first poll for result
        """
    def getLanguage(self):
        """
        Returns:
            language: the language code of the text (optional for some services)
        """
    def getMaxPollingRetries(self):
        """
        Returns:
            maxPollingRetries: number of times to poll
        """
    def getModelVersion(self):
        """
        Returns:
            modelVersion: Version of the model
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
    def getShowStats(self):
        """
        Returns:
            showStats: Whether to include detailed statistics in the response
        """
    def getStringIndexType(self):
        """
        Returns:
            stringIndexType: Specifies the method used to interpret string offsets. Defaults to Text Elements (Graphemes) according to Unicode v8.0.0. For additional information see https://aka.ms/text-analytics-offsets
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
    def getText(self):
        """
        Returns:
            text: the text in the request body
        """
    def getTimeout(self):
        """
        Returns:
            timeout: number of seconds to wait before closing the connection
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
    def setLinkedService(self, value): ...
