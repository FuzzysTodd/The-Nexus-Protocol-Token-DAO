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

class DictionaryLookup(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        errorCol (str): column to hold http errors
        fromLanguage (object): Specifies the language of the input text. The source language must be one of the supported languages included in the dictionary scope.
        handler (object): Which strategy to use when handling requests
        outputCol (str): The name of the output column
        subscriptionKey (object): the API key to use
        subscriptionRegion (object): the API region to use
        text (object): the string to translate
        timeout (float): number of seconds to wait before closing the connection
        toLanguage (object): Specifies the language of the output text. The target language must be one of the supported languages included in the dictionary scope.
        url (str): Url of the service
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    errorCol: Incomplete
    fromLanguage: Incomplete
    handler: Incomplete
    outputCol: Incomplete
    subscriptionKey: Incomplete
    subscriptionRegion: Incomplete
    text: Incomplete
    timeout: Incomplete
    toLanguage: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'DictionaryLookup_943e18de1a5a_error', fromLanguage: Incomplete | None = None, fromLanguageCol: Incomplete | None = None, handler: Incomplete | None = None, outputCol: str = 'DictionaryLookup_943e18de1a5a_output', subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, subscriptionRegion: Incomplete | None = None, subscriptionRegionCol: Incomplete | None = None, text: Incomplete | None = None, textCol: Incomplete | None = None, timeout: float = 60.0, toLanguage: Incomplete | None = None, toLanguageCol: Incomplete | None = None, url: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'DictionaryLookup_943e18de1a5a_error', fromLanguage: Incomplete | None = None, fromLanguageCol: Incomplete | None = None, handler: Incomplete | None = None, outputCol: str = 'DictionaryLookup_943e18de1a5a_output', subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, subscriptionRegion: Incomplete | None = None, subscriptionRegionCol: Incomplete | None = None, text: Incomplete | None = None, textCol: Incomplete | None = None, timeout: float = 60.0, toLanguage: Incomplete | None = None, toLanguageCol: Incomplete | None = None, url: Incomplete | None = None):
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
    def setErrorCol(self, value):
        """
        Args:
            errorCol: column to hold http errors
        """
    def setFromLanguage(self, value):
        """
        Args:
            fromLanguage: Specifies the language of the input text. The source language must be one of the supported languages included in the dictionary scope.
        """
    def setFromLanguageCol(self, value):
        """
        Args:
            fromLanguage: Specifies the language of the input text. The source language must be one of the supported languages included in the dictionary scope.
        """
    def setHandler(self, value):
        """
        Args:
            handler: Which strategy to use when handling requests
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
    def setSubscriptionRegion(self, value):
        """
        Args:
            subscriptionRegion: the API region to use
        """
    def setSubscriptionRegionCol(self, value):
        """
        Args:
            subscriptionRegion: the API region to use
        """
    def setText(self, value):
        """
        Args:
            text: the string to translate
        """
    def setTextCol(self, value):
        """
        Args:
            text: the string to translate
        """
    def setTimeout(self, value):
        """
        Args:
            timeout: number of seconds to wait before closing the connection
        """
    def setToLanguage(self, value):
        """
        Args:
            toLanguage: Specifies the language of the output text. The target language must be one of the supported languages included in the dictionary scope.
        """
    def setToLanguageCol(self, value):
        """
        Args:
            toLanguage: Specifies the language of the output text. The target language must be one of the supported languages included in the dictionary scope.
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
    def getErrorCol(self):
        """
        Returns:
            errorCol: column to hold http errors
        """
    def getFromLanguage(self):
        """
        Returns:
            fromLanguage: Specifies the language of the input text. The source language must be one of the supported languages included in the dictionary scope.
        """
    def getHandler(self):
        """
        Returns:
            handler: Which strategy to use when handling requests
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
    def getSubscriptionRegion(self):
        """
        Returns:
            subscriptionRegion: the API region to use
        """
    def getText(self):
        """
        Returns:
            text: the string to translate
        """
    def getTimeout(self):
        """
        Returns:
            timeout: number of seconds to wait before closing the connection
        """
    def getToLanguage(self):
        """
        Returns:
            toLanguage: Specifies the language of the output text. The target language must be one of the supported languages included in the dictionary scope.
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
