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

class TextAnalyze(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        backoffs (list): array of backoffs to use in the handler
        batchSize (int): The max size of the buffer
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        disableServiceLogs (object): disableServiceLogs option
        entityLinkingParams (dict): the parameters to pass to the entityLinking model
        entityRecognitionParams (dict): the parameters to pass to the entity recognition model
        errorCol (str): column to hold http errors
        includeEntityLinking (bool): Whether to perform EntityLinking
        includeEntityRecognition (bool): Whether to perform entity recognition
        includeKeyPhraseExtraction (bool): Whether to perform EntityLinking
        includePii (bool): Whether to perform PII Detection
        includeSentimentAnalysis (bool): Whether to perform SentimentAnalysis
        initialPollingDelay (int): number of milliseconds to wait before first poll for result
        keyPhraseExtractionParams (dict): the parameters to pass to the keyPhraseExtraction model
        language (object): the language code of the text (optional for some services)
        maxPollingRetries (int): number of times to poll
        modelVersion (object): Version of the model
        outputCol (str): The name of the output column
        piiParams (dict): the parameters to pass to the PII model
        pollingDelay (int): number of milliseconds to wait between polling
        sentimentAnalysisParams (dict): the parameters to pass to the sentimentAnalysis model
        showStats (object): Whether to include detailed statistics in the response
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
    entityLinkingParams: Incomplete
    entityRecognitionParams: Incomplete
    errorCol: Incomplete
    includeEntityLinking: Incomplete
    includeEntityRecognition: Incomplete
    includeKeyPhraseExtraction: Incomplete
    includePii: Incomplete
    includeSentimentAnalysis: Incomplete
    initialPollingDelay: Incomplete
    keyPhraseExtractionParams: Incomplete
    language: Incomplete
    maxPollingRetries: Incomplete
    modelVersion: Incomplete
    outputCol: Incomplete
    piiParams: Incomplete
    pollingDelay: Incomplete
    sentimentAnalysisParams: Incomplete
    showStats: Incomplete
    subscriptionKey: Incomplete
    suppressMaxRetriesException: Incomplete
    text: Incomplete
    timeout: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, backoffs=[100, 500, 1000], batchSize: int = 10, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, disableServiceLogs: Incomplete | None = None, disableServiceLogsCol: Incomplete | None = None, entityLinkingParams={'model-version': 'latest'}, entityRecognitionParams={'model-version': 'latest'}, errorCol: str = 'TextAnalyze_79f5009f2d92_error', includeEntityLinking: bool = True, includeEntityRecognition: bool = True, includeKeyPhraseExtraction: bool = True, includePii: bool = True, includeSentimentAnalysis: bool = True, initialPollingDelay: int = 300, keyPhraseExtractionParams={'model-version': 'latest'}, language: Incomplete | None = None, languageCol: Incomplete | None = None, maxPollingRetries: int = 1000, modelVersion: Incomplete | None = None, modelVersionCol: Incomplete | None = None, outputCol: str = 'TextAnalyze_79f5009f2d92_output', piiParams={'model-version': 'latest'}, pollingDelay: int = 300, sentimentAnalysisParams={'model-version': 'latest'}, showStats: Incomplete | None = None, showStatsCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, suppressMaxRetriesException: bool = False, text: Incomplete | None = None, textCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, backoffs=[100, 500, 1000], batchSize: int = 10, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, disableServiceLogs: Incomplete | None = None, disableServiceLogsCol: Incomplete | None = None, entityLinkingParams={'model-version': 'latest'}, entityRecognitionParams={'model-version': 'latest'}, errorCol: str = 'TextAnalyze_79f5009f2d92_error', includeEntityLinking: bool = True, includeEntityRecognition: bool = True, includeKeyPhraseExtraction: bool = True, includePii: bool = True, includeSentimentAnalysis: bool = True, initialPollingDelay: int = 300, keyPhraseExtractionParams={'model-version': 'latest'}, language: Incomplete | None = None, languageCol: Incomplete | None = None, maxPollingRetries: int = 1000, modelVersion: Incomplete | None = None, modelVersionCol: Incomplete | None = None, outputCol: str = 'TextAnalyze_79f5009f2d92_output', piiParams={'model-version': 'latest'}, pollingDelay: int = 300, sentimentAnalysisParams={'model-version': 'latest'}, showStats: Incomplete | None = None, showStatsCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, suppressMaxRetriesException: bool = False, text: Incomplete | None = None, textCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None):
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
    def setEntityLinkingParams(self, value):
        """
        Args:
            entityLinkingParams: the parameters to pass to the entityLinking model
        """
    def setEntityRecognitionParams(self, value):
        """
        Args:
            entityRecognitionParams: the parameters to pass to the entity recognition model
        """
    def setErrorCol(self, value):
        """
        Args:
            errorCol: column to hold http errors
        """
    def setIncludeEntityLinking(self, value):
        """
        Args:
            includeEntityLinking: Whether to perform EntityLinking
        """
    def setIncludeEntityRecognition(self, value):
        """
        Args:
            includeEntityRecognition: Whether to perform entity recognition
        """
    def setIncludeKeyPhraseExtraction(self, value):
        """
        Args:
            includeKeyPhraseExtraction: Whether to perform EntityLinking
        """
    def setIncludePii(self, value):
        """
        Args:
            includePii: Whether to perform PII Detection
        """
    def setIncludeSentimentAnalysis(self, value):
        """
        Args:
            includeSentimentAnalysis: Whether to perform SentimentAnalysis
        """
    def setInitialPollingDelay(self, value):
        """
        Args:
            initialPollingDelay: number of milliseconds to wait before first poll for result
        """
    def setKeyPhraseExtractionParams(self, value):
        """
        Args:
            keyPhraseExtractionParams: the parameters to pass to the keyPhraseExtraction model
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
    def setPiiParams(self, value):
        """
        Args:
            piiParams: the parameters to pass to the PII model
        """
    def setPollingDelay(self, value):
        """
        Args:
            pollingDelay: number of milliseconds to wait between polling
        """
    def setSentimentAnalysisParams(self, value):
        """
        Args:
            sentimentAnalysisParams: the parameters to pass to the sentimentAnalysis model
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
    def getEntityLinkingParams(self):
        """
        Returns:
            entityLinkingParams: the parameters to pass to the entityLinking model
        """
    def getEntityRecognitionParams(self):
        """
        Returns:
            entityRecognitionParams: the parameters to pass to the entity recognition model
        """
    def getErrorCol(self):
        """
        Returns:
            errorCol: column to hold http errors
        """
    def getIncludeEntityLinking(self):
        """
        Returns:
            includeEntityLinking: Whether to perform EntityLinking
        """
    def getIncludeEntityRecognition(self):
        """
        Returns:
            includeEntityRecognition: Whether to perform entity recognition
        """
    def getIncludeKeyPhraseExtraction(self):
        """
        Returns:
            includeKeyPhraseExtraction: Whether to perform EntityLinking
        """
    def getIncludePii(self):
        """
        Returns:
            includePii: Whether to perform PII Detection
        """
    def getIncludeSentimentAnalysis(self):
        """
        Returns:
            includeSentimentAnalysis: Whether to perform SentimentAnalysis
        """
    def getInitialPollingDelay(self):
        """
        Returns:
            initialPollingDelay: number of milliseconds to wait before first poll for result
        """
    def getKeyPhraseExtractionParams(self):
        """
        Returns:
            keyPhraseExtractionParams: the parameters to pass to the keyPhraseExtraction model
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
    def getPiiParams(self):
        """
        Returns:
            piiParams: the parameters to pass to the PII model
        """
    def getPollingDelay(self):
        """
        Returns:
            pollingDelay: number of milliseconds to wait between polling
        """
    def getSentimentAnalysisParams(self):
        """
        Returns:
            sentimentAnalysisParams: the parameters to pass to the sentimentAnalysis model
        """
    def getShowStats(self):
        """
        Returns:
            showStats: Whether to include detailed statistics in the response
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
