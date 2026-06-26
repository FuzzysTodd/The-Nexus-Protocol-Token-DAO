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

class AnalyzeImage(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        descriptionExclude (object): Whether to exclude certain parts of the model in the description
        details (object): what visual feature types to return
        errorCol (str): column to hold http errors
        handler (object): Which strategy to use when handling requests
        imageBytes (object): bytestream of the image to use
        imageUrl (object): the url of the image to use
        language (object): the language of the response (en if none given)
        outputCol (str): The name of the output column
        subscriptionKey (object): the API key to use
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
        visualFeatures (object): what visual feature types to return
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    descriptionExclude: Incomplete
    details: Incomplete
    errorCol: Incomplete
    handler: Incomplete
    imageBytes: Incomplete
    imageUrl: Incomplete
    language: Incomplete
    outputCol: Incomplete
    subscriptionKey: Incomplete
    timeout: Incomplete
    url: Incomplete
    visualFeatures: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, descriptionExclude: Incomplete | None = None, descriptionExcludeCol: Incomplete | None = None, details: Incomplete | None = None, detailsCol: Incomplete | None = None, errorCol: str = 'AnalyzeImage_7429a3cc0cca_error', handler: Incomplete | None = None, imageBytes: Incomplete | None = None, imageBytesCol: Incomplete | None = None, imageUrl: Incomplete | None = None, imageUrlCol: Incomplete | None = None, language: Incomplete | None = None, languageCol: Incomplete | None = None, outputCol: str = 'AnalyzeImage_7429a3cc0cca_output', subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None, visualFeatures: Incomplete | None = None, visualFeaturesCol: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, descriptionExclude: Incomplete | None = None, descriptionExcludeCol: Incomplete | None = None, details: Incomplete | None = None, detailsCol: Incomplete | None = None, errorCol: str = 'AnalyzeImage_7429a3cc0cca_error', handler: Incomplete | None = None, imageBytes: Incomplete | None = None, imageBytesCol: Incomplete | None = None, imageUrl: Incomplete | None = None, imageUrlCol: Incomplete | None = None, language: Incomplete | None = None, languageCol: Incomplete | None = None, outputCol: str = 'AnalyzeImage_7429a3cc0cca_output', subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None, visualFeatures: Incomplete | None = None, visualFeaturesCol: Incomplete | None = None):
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
    def setDescriptionExclude(self, value):
        """
        Args:
            descriptionExclude: Whether to exclude certain parts of the model in the description
        """
    def setDescriptionExcludeCol(self, value):
        """
        Args:
            descriptionExclude: Whether to exclude certain parts of the model in the description
        """
    def setDetails(self, value):
        """
        Args:
            details: what visual feature types to return
        """
    def setDetailsCol(self, value):
        """
        Args:
            details: what visual feature types to return
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
    def setLanguage(self, value):
        """
        Args:
            language: the language of the response (en if none given)
        """
    def setLanguageCol(self, value):
        """
        Args:
            language: the language of the response (en if none given)
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
    def setVisualFeatures(self, value):
        """
        Args:
            visualFeatures: what visual feature types to return
        """
    def setVisualFeaturesCol(self, value):
        """
        Args:
            visualFeatures: what visual feature types to return
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
    def getDescriptionExclude(self):
        """
        Returns:
            descriptionExclude: Whether to exclude certain parts of the model in the description
        """
    def getDetails(self):
        """
        Returns:
            details: what visual feature types to return
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
    def getLanguage(self):
        """
        Returns:
            language: the language of the response (en if none given)
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
    def getVisualFeatures(self):
        """
        Returns:
            visualFeatures: what visual feature types to return
        """
    def setCustomServiceName(self, value): ...
    def setEndpoint(self, value): ...
    def setDefaultInternalEndpoint(self, value): ...
    def setLocation(self, value): ...
    def setLinkedService(self, value): ...
