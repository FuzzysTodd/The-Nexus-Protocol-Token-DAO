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

class CheckPointInPolygon(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        errorCol (str): column to hold http errors
        handler (object): Which strategy to use when handling requests
        latitude (object): the latitude of location
        longitude (object): the longitude of location
        outputCol (str): The name of the output column
        subscriptionKey (object): the API key to use
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
        userDataIdentifier (object): the identifier for the user uploaded data
    """
    AADToken: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    errorCol: Incomplete
    handler: Incomplete
    latitude: Incomplete
    longitude: Incomplete
    outputCol: Incomplete
    subscriptionKey: Incomplete
    timeout: Incomplete
    url: Incomplete
    userDataIdentifier: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'CheckPointInPolygon_c534a55de823_error', handler: Incomplete | None = None, latitude: Incomplete | None = None, latitudeCol: Incomplete | None = None, longitude: Incomplete | None = None, longitudeCol: Incomplete | None = None, outputCol: str = 'CheckPointInPolygon_c534a55de823_output', subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: str = 'https://atlas.microsoft.com/', userDataIdentifier: Incomplete | None = None, userDataIdentifierCol: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'CheckPointInPolygon_c534a55de823_error', handler: Incomplete | None = None, latitude: Incomplete | None = None, latitudeCol: Incomplete | None = None, longitude: Incomplete | None = None, longitudeCol: Incomplete | None = None, outputCol: str = 'CheckPointInPolygon_c534a55de823_output', subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: str = 'https://atlas.microsoft.com/', userDataIdentifier: Incomplete | None = None, userDataIdentifierCol: Incomplete | None = None):
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
    def setUrl(self, value):
        """
        Args:
            url: Url of the service
        """
    def setUserDataIdentifier(self, value):
        """
        Args:
            userDataIdentifier: the identifier for the user uploaded data
        """
    def setUserDataIdentifierCol(self, value):
        """
        Args:
            userDataIdentifier: the identifier for the user uploaded data
        """
    def getAADToken(self):
        """
        Returns:
            AADToken: AAD Token used for authentication
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
    def getUrl(self):
        """
        Returns:
            url: Url of the service
        """
    def getUserDataIdentifier(self):
        """
        Returns:
            userDataIdentifier: the identifier for the user uploaded data
        """
    def setCustomServiceName(self, value): ...
    def setEndpoint(self, value): ...
    def setDefaultInternalEndpoint(self, value): ...
    def setGeography(self, value): ...
