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

class OpenAIEmbedding(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        apiVersion (object): version of the api
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        deploymentName (object): The name of the deployment
        errorCol (str): column to hold http errors
        handler (object): Which strategy to use when handling requests
        outputCol (str): The name of the output column
        subscriptionKey (object): the API key to use
        text (object): Input text to get embeddings for.
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
        user (object): The ID of the end-user, for use in tracking and rate-limiting.
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    apiVersion: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    deploymentName: Incomplete
    errorCol: Incomplete
    handler: Incomplete
    outputCol: Incomplete
    subscriptionKey: Incomplete
    text: Incomplete
    timeout: Incomplete
    url: Incomplete
    user: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, apiVersion: Incomplete | None = None, apiVersionCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, deploymentName: Incomplete | None = None, deploymentNameCol: Incomplete | None = None, errorCol: str = 'OpenAIEmbedding_75c857ec95e6_error', handler: Incomplete | None = None, outputCol: str = 'OpenAIEmbedding_75c857ec95e6_output', subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, text: Incomplete | None = None, textCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None, user: Incomplete | None = None, userCol: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, apiVersion: Incomplete | None = None, apiVersionCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, deploymentName: Incomplete | None = None, deploymentNameCol: Incomplete | None = None, errorCol: str = 'OpenAIEmbedding_75c857ec95e6_error', handler: Incomplete | None = None, outputCol: str = 'OpenAIEmbedding_75c857ec95e6_output', subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, text: Incomplete | None = None, textCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None, user: Incomplete | None = None, userCol: Incomplete | None = None):
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
    def setDeploymentName(self, value):
        """
        Args:
            deploymentName: The name of the deployment
        """
    def setDeploymentNameCol(self, value):
        """
        Args:
            deploymentName: The name of the deployment
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
            text: Input text to get embeddings for.
        """
    def setTextCol(self, value):
        """
        Args:
            text: Input text to get embeddings for.
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
    def setUser(self, value):
        """
        Args:
            user: The ID of the end-user, for use in tracking and rate-limiting.
        """
    def setUserCol(self, value):
        """
        Args:
            user: The ID of the end-user, for use in tracking and rate-limiting.
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
    def getDeploymentName(self):
        """
        Returns:
            deploymentName: The name of the deployment
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
            text: Input text to get embeddings for.
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
    def getUser(self):
        """
        Returns:
            user: The ID of the end-user, for use in tracking and rate-limiting.
        """
    def setCustomServiceName(self, value): ...
    def setEndpoint(self, value): ...
    def setDefaultInternalEndpoint(self, value): ...
