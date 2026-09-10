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

class AnalyzeText(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        apiVersion (object): version of the api
        batchSize (int): The max size of the buffer
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        countryHint (object): the countryHint for language detection
        domain (object): if specified, will set the PII domain to include only a subset of the entity categories. Possible values include: 'PHI', 'none'.
        errorCol (str): column to hold http errors
        handler (object): Which strategy to use when handling requests
        kind (str): Enumeration of supported Text Analysis tasks
        language (object): the language code of the text (optional for some services)
        loggingOptOut (object): loggingOptOut for task
        modelVersion (object): Version of the model
        opinionMining (object): opinionMining option for SentimentAnalysisTask
        outputCol (str): The name of the output column
        piiCategories (object): describes the PII categories to return
        showStats (object): Whether to include detailed statistics in the response
        stringIndexType (object): Specifies the method used to interpret string offsets. Defaults to Text Elements (Graphemes) according to Unicode v8.0.0. For additional information see https://aka.ms/text-analytics-offsets
        subscriptionKey (object): the API key to use
        text (object): the text in the request body
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    apiVersion: Incomplete
    batchSize: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    countryHint: Incomplete
    domain: Incomplete
    errorCol: Incomplete
    handler: Incomplete
    kind: Incomplete
    language: Incomplete
    loggingOptOut: Incomplete
    modelVersion: Incomplete
    opinionMining: Incomplete
    outputCol: Incomplete
    piiCategories: Incomplete
    showStats: Incomplete
    stringIndexType: Incomplete
    subscriptionKey: Incomplete
    text: Incomplete
    timeout: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, apiVersion: Incomplete | None = None, apiVersionCol: Incomplete | None = None, batchSize: int = 10, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, countryHint: Incomplete | None = None, countryHintCol: Incomplete | None = None, domain: Incomplete | None = None, domainCol: Incomplete | None = None, errorCol: str = 'AnalyzeText_592c7b20d0cb_error', handler: Incomplete | None = None, kind: Incomplete | None = None, language: Incomplete | None = None, languageCol: Incomplete | None = None, loggingOptOut: Incomplete | None = None, loggingOptOutCol: Incomplete | None = None, modelVersion: Incomplete | None = None, modelVersionCol: Incomplete | None = None, opinionMining: Incomplete | None = None, opinionMiningCol: Incomplete | None = None, outputCol: str = 'AnalyzeText_592c7b20d0cb_output', piiCategories: Incomplete | None = None, piiCategoriesCol: Incomplete | None = None, showStats: Incomplete | None = None, showStatsCol: Incomplete | None = None, stringIndexType: Incomplete | None = None, stringIndexTypeCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, text: Incomplete | None = None, textCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, apiVersion: Incomplete | None = None, apiVersionCol: Incomplete | None = None, batchSize: int = 10, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, countryHint: Incomplete | None = None, countryHintCol: Incomplete | None = None, domain: Incomplete | None = None, domainCol: Incomplete | None = None, errorCol: str = 'AnalyzeText_592c7b20d0cb_error', handler: Incomplete | None = None, kind: Incomplete | None = None, language: Incomplete | None = None, languageCol: Incomplete | None = None, loggingOptOut: Incomplete | None = None, loggingOptOutCol: Incomplete | None = None, modelVersion: Incomplete | None = None, modelVersionCol: Incomplete | None = None, opinionMining: Incomplete | None = None, opinionMiningCol: Incomplete | None = None, outputCol: str = 'AnalyzeText_592c7b20d0cb_output', piiCategories: Incomplete | None = None, piiCategoriesCol: Incomplete | None = None, showStats: Incomplete | None = None, showStatsCol: Incomplete | None = None, stringIndexType: Incomplete | None = None, stringIndexTypeCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, text: Incomplete | None = None, textCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None):
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
    def setApiVersion(self, value):
        """
        Args:
            apiVersion: version of the api
        """
    def setApiVersionCol(self, value):
        """
        Args:
            apiVersion: version of the api
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
    def setCountryHint(self, value):
        """
        Args:
            countryHint: the countryHint for language detection
        """
    def setCountryHintCol(self, value):
        """
        Args:
            countryHint: the countryHint for language detection
        """
    def setDomain(self, value):
        """
        Args:
            domain: if specified, will set the PII domain to include only a subset of the entity categories. Possible values include: 'PHI', 'none'.
        """
    def setDomainCol(self, value):
        """
        Args:
            domain: if specified, will set the PII domain to include only a subset of the entity categories. Possible values include: 'PHI', 'none'.
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
    def setKind(self, value):
        """
        Args:
            kind: Enumeration of supported Text Analysis tasks
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
    def setLoggingOptOut(self, value):
        """
        Args:
            loggingOptOut: loggingOptOut for task
        """
    def setLoggingOptOutCol(self, value):
        """
        Args:
            loggingOptOut: loggingOptOut for task
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
    def setOpinionMining(self, value):
        """
        Args:
            opinionMining: opinionMining option for SentimentAnalysisTask
        """
    def setOpinionMiningCol(self, value):
        """
        Args:
            opinionMining: opinionMining option for SentimentAnalysisTask
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setPiiCategories(self, value):
        """
        Args:
            piiCategories: describes the PII categories to return
        """
    def setPiiCategoriesCol(self, value):
        """
        Args:
            piiCategories: describes the PII categories to return
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
    def getApiVersion(self):
        """
        Returns:
            apiVersion: version of the api
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
    def getCountryHint(self):
        """
        Returns:
            countryHint: the countryHint for language detection
        """
    def getDomain(self):
        """
        Returns:
            domain: if specified, will set the PII domain to include only a subset of the entity categories. Possible values include: 'PHI', 'none'.
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
    def getKind(self):
        """
        Returns:
            kind: Enumeration of supported Text Analysis tasks
        """
    def getLanguage(self):
        """
        Returns:
            language: the language code of the text (optional for some services)
        """
    def getLoggingOptOut(self):
        """
        Returns:
            loggingOptOut: loggingOptOut for task
        """
    def getModelVersion(self):
        """
        Returns:
            modelVersion: Version of the model
        """
    def getOpinionMining(self):
        """
        Returns:
            opinionMining: opinionMining option for SentimentAnalysisTask
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getPiiCategories(self):
        """
        Returns:
            piiCategories: describes the PII categories to return
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
