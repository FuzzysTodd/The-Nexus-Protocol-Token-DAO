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

class SpeakerEmotionInference(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        errorCol (str): column to hold http errors
        handler (object): Which strategy to use when handling requests
        locale (object): The locale of the input text
        outputCol (str): The name of the output column
        subscriptionKey (object): the API key to use
        text (object): The text to annotate with inferred emotion
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
        voiceName (object): The name of the voice used for synthesis
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    errorCol: Incomplete
    handler: Incomplete
    locale: Incomplete
    outputCol: Incomplete
    subscriptionKey: Incomplete
    text: Incomplete
    timeout: Incomplete
    url: Incomplete
    voiceName: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'SpeakerEmotionInference_fa0f59faca93_error', handler: Incomplete | None = None, locale: Incomplete | None = None, localeCol: Incomplete | None = None, outputCol: str = 'SpeakerEmotionInference_fa0f59faca93_output', subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, text: Incomplete | None = None, textCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None, voiceName: Incomplete | None = None, voiceNameCol: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'SpeakerEmotionInference_fa0f59faca93_error', handler: Incomplete | None = None, locale: Incomplete | None = None, localeCol: Incomplete | None = None, outputCol: str = 'SpeakerEmotionInference_fa0f59faca93_output', subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, text: Incomplete | None = None, textCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None, voiceName: Incomplete | None = None, voiceNameCol: Incomplete | None = None):
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
    def setHandler(self, value):
        """
        Args:
            handler: Which strategy to use when handling requests
        """
    def setLocale(self, value):
        """
        Args:
            locale: The locale of the input text
        """
    def setLocaleCol(self, value):
        """
        Args:
            locale: The locale of the input text
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
    def setText(self, value):
        """
        Args:
            text: The text to annotate with inferred emotion
        """
    def setTextCol(self, value):
        """
        Args:
            text: The text to annotate with inferred emotion
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
    def setVoiceName(self, value):
        """
        Args:
            voiceName: The name of the voice used for synthesis
        """
    def setVoiceNameCol(self, value):
        """
        Args:
            voiceName: The name of the voice used for synthesis
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
    def getHandler(self):
        """
        Returns:
            handler: Which strategy to use when handling requests
        """
    def getLocale(self):
        """
        Returns:
            locale: The locale of the input text
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
    def getText(self):
        """
        Returns:
            text: The text to annotate with inferred emotion
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
    def getVoiceName(self):
        """
        Returns:
            voiceName: The name of the voice used for synthesis
        """
    def setCustomServiceName(self, value): ...
    def setEndpoint(self, value): ...
    def setDefaultInternalEndpoint(self, value): ...
    def setLocation(self, value): ...
