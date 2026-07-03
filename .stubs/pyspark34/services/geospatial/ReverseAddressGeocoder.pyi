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

class ReverseAddressGeocoder(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        backoffs (list): array of backoffs to use in the handler
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        errorCol (str): column to hold http errors
        initialPollingDelay (int): number of milliseconds to wait before first poll for result
        latitude (object): the latitude of location
        longitude (object): the longitude of location
        maxPollingRetries (int): number of times to poll
        outputCol (str): The name of the output column
        pollingDelay (int): number of milliseconds to wait between polling
        subscriptionKey (object): the API key to use
        suppressMaxRetriesException (bool): set true to suppress the maxumimum retries exception and report in the error column
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
    """
    AADToken: Incomplete
    backoffs: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    errorCol: Incomplete
    initialPollingDelay: Incomplete
    latitude: Incomplete
    longitude: Incomplete
    maxPollingRetries: Incomplete
    outputCol: Incomplete
    pollingDelay: Incomplete
    subscriptionKey: Incomplete
    suppressMaxRetriesException: Incomplete
    timeout: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, backoffs=[100, 500, 1000], concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'ReverseAddressGeocoder_be54c353a50b_error', initialPollingDelay: int = 300, latitude: Incomplete | None = None, latitudeCol: Incomplete | None = None, longitude: Incomplete | None = None, longitudeCol: Incomplete | None = None, maxPollingRetries: int = 1000, outputCol: str = 'ReverseAddressGeocoder_be54c353a50b_output', pollingDelay: int = 300, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, suppressMaxRetriesException: bool = False, timeout: float = 60.0, url: str = 'https://atlas.microsoft.com/search/address/reverse/batch/json') -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, backoffs=[100, 500, 1000], concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'ReverseAddressGeocoder_be54c353a50b_error', initialPollingDelay: int = 300, latitude: Incomplete | None = None, latitudeCol: Incomplete | None = None, longitude: Incomplete | None = None, longitudeCol: Incomplete | None = None, maxPollingRetries: int = 1000, outputCol: str = 'ReverseAddressGeocoder_be54c353a50b_output', pollingDelay: int = 300, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, suppressMaxRetriesException: bool = False, timeout: float = 60.0, url: str = 'https://atlas.microsoft.com/search/address/reverse/batch/json'):
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
    def setInitialPollingDelay(self, value):
        """
        Args:
            initialPollingDelay: number of milliseconds to wait before first poll for result
        """
    def setLatitude(self, value):
        """
        Args:
            latitude: the latitude of location
        """
    def setLatitudeCol(self, value):
        """
        Args:
            latitude: the latitude of location
        """
    def setLongitude(self, value):
        """
        Args:
            longitude: the longitude of location
        """
    def setLongitudeCol(self, value):
        """
        Args:
            longitude: the longitude of location
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
    def getInitialPollingDelay(self):
        """
        Returns:
            initialPollingDelay: number of milliseconds to wait before first poll for result
        """
    def getLatitude(self):
        """
        Returns:
            latitude: the latitude of location
        """
    def getLongitude(self):
        """
        Returns:
            longitude: the longitude of location
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
