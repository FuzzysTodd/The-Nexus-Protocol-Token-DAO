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

class RecognizeText(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        backoffs (list): array of backoffs to use in the handler
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        errorCol (str): column to hold http errors
        imageBytes (object): bytestream of the image to use
        imageUrl (object): the url of the image to use
        initialPollingDelay (int): number of milliseconds to wait before first poll for result
        maxPollingRetries (int): number of times to poll
        mode (object): If this parameter is set to 'Printed', printed text recognition is performed. If 'Handwritten' is specified, handwriting recognition is performed
        outputCol (str): The name of the output column
        pollingDelay (int): number of milliseconds to wait between polling
        subscriptionKey (object): the API key to use
        suppressMaxRetriesException (bool): set true to suppress the maxumimum retries exception and report in the error column
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    backoffs: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    errorCol: Incomplete
    imageBytes: Incomplete
    imageUrl: Incomplete
    initialPollingDelay: Incomplete
    maxPollingRetries: Incomplete
    mode: Incomplete
    outputCol: Incomplete
    pollingDelay: Incomplete
    subscriptionKey: Incomplete
    suppressMaxRetriesException: Incomplete
    timeout: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, backoffs=[100, 500, 1000], concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'RecognizeText_831c7e28d389_error', imageBytes: Incomplete | None = None, imageBytesCol: Incomplete | None = None, imageUrl: Incomplete | None = None, imageUrlCol: Incomplete | None = None, initialPollingDelay: int = 300, maxPollingRetries: int = 1000, mode: Incomplete | None = None, modeCol: Incomplete | None = None, outputCol: str = 'RecognizeText_831c7e28d389_output', pollingDelay: int = 300, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, suppressMaxRetriesException: bool = False, timeout: float = 60.0, url: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, backoffs=[100, 500, 1000], concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'RecognizeText_831c7e28d389_error', imageBytes: Incomplete | None = None, imageBytesCol: Incomplete | None = None, imageUrl: Incomplete | None = None, imageUrlCol: Incomplete | None = None, initialPollingDelay: int = 300, maxPollingRetries: int = 1000, mode: Incomplete | None = None, modeCol: Incomplete | None = None, outputCol: str = 'RecognizeText_831c7e28d389_output', pollingDelay: int = 300, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, suppressMaxRetriesException: bool = False, timeout: float = 60.0, url: Incomplete | None = None):
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
    def setImageBytes(self, value):
        """
        Args:
            imageBytes: bytestream of the image to use
        """
    def setImageBytesCol(self, value):
        """
        Args:
            imageBytes: bytestream of the image to use
        """
    def setImageUrl(self, value):
        """
        Args:
            imageUrl: the url of the image to use
        """
    def setImageUrlCol(self, value):
        """
        Args:
            imageUrl: the url of the image to use
        """
    def setInitialPollingDelay(self, value):
        """
        Args:
            initialPollingDelay: number of milliseconds to wait before first poll for result
        """
    def setMaxPollingRetries(self, value):
        """
        Args:
            maxPollingRetries: number of times to poll
        """
    def setMode(self, value):
        """
        Args:
            mode: If this parameter is set to 'Printed', printed text recognition is performed. If 'Handwritten' is specified, handwriting recognition is performed
        """
    def setModeCol(self, value):
        """
        Args:
            mode: If this parameter is set to 'Printed', printed text recognition is performed. If 'Handwritten' is specified, handwriting recognition is performed
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
    def getImageBytes(self):
        """
        Returns:
            imageBytes: bytestream of the image to use
        """
    def getImageUrl(self):
        """
        Returns:
            imageUrl: the url of the image to use
        """
    def getInitialPollingDelay(self):
        """
        Returns:
            initialPollingDelay: number of milliseconds to wait before first poll for result
        """
    def getMaxPollingRetries(self):
        """
        Returns:
            maxPollingRetries: number of times to poll
        """
    def getMode(self):
        """
        Returns:
            mode: If this parameter is set to 'Printed', printed text recognition is performed. If 'Handwritten' is specified, handwriting recognition is performed
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
