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

class DetectFace(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        errorCol (str): column to hold http errors
        handler (object): Which strategy to use when handling requests
        imageUrl (object): the url of the image to use
        outputCol (str): The name of the output column
        returnFaceAttributes (object): Analyze and return the one or more specified face attributes Supported face attributes include: age, gender, headPose, smile, facialHair, glasses, emotion, hair, makeup, occlusion, accessories, blur, exposure and noise. Face attribute analysis has additional computational and time cost.
        returnFaceId (object): Return faceIds of the detected faces or not. The default value is true
        returnFaceLandmarks (object): Return face landmarks of the detected faces or not. The default value is false.
        subscriptionKey (object): the API key to use
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    errorCol: Incomplete
    handler: Incomplete
    imageUrl: Incomplete
    outputCol: Incomplete
    returnFaceAttributes: Incomplete
    returnFaceId: Incomplete
    returnFaceLandmarks: Incomplete
    subscriptionKey: Incomplete
    timeout: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'DetectFace_dbd4908fc3e5_error', handler: Incomplete | None = None, imageUrl: Incomplete | None = None, imageUrlCol: Incomplete | None = None, outputCol: str = 'DetectFace_dbd4908fc3e5_output', returnFaceAttributes: Incomplete | None = None, returnFaceAttributesCol: Incomplete | None = None, returnFaceId: Incomplete | None = None, returnFaceIdCol: Incomplete | None = None, returnFaceLandmarks: Incomplete | None = None, returnFaceLandmarksCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'DetectFace_dbd4908fc3e5_error', handler: Incomplete | None = None, imageUrl: Incomplete | None = None, imageUrlCol: Incomplete | None = None, outputCol: str = 'DetectFace_dbd4908fc3e5_output', returnFaceAttributes: Incomplete | None = None, returnFaceAttributesCol: Incomplete | None = None, returnFaceId: Incomplete | None = None, returnFaceIdCol: Incomplete | None = None, returnFaceLandmarks: Incomplete | None = None, returnFaceLandmarksCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None):
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
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setReturnFaceAttributes(self, value):
        """
        Args:
            returnFaceAttributes: Analyze and return the one or more specified face attributes Supported face attributes include: age, gender, headPose, smile, facialHair, glasses, emotion, hair, makeup, occlusion, accessories, blur, exposure and noise. Face attribute analysis has additional computational and time cost.
        """
    def setReturnFaceAttributesCol(self, value):
        """
        Args:
            returnFaceAttributes: Analyze and return the one or more specified face attributes Supported face attributes include: age, gender, headPose, smile, facialHair, glasses, emotion, hair, makeup, occlusion, accessories, blur, exposure and noise. Face attribute analysis has additional computational and time cost.
        """
    def setReturnFaceId(self, value):
        """
        Args:
            returnFaceId: Return faceIds of the detected faces or not. The default value is true
        """
    def setReturnFaceIdCol(self, value):
        """
        Args:
            returnFaceId: Return faceIds of the detected faces or not. The default value is true
        """
    def setReturnFaceLandmarks(self, value):
        """
        Args:
            returnFaceLandmarks: Return face landmarks of the detected faces or not. The default value is false.
        """
    def setReturnFaceLandmarksCol(self, value):
        """
        Args:
            returnFaceLandmarks: Return face landmarks of the detected faces or not. The default value is false.
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
    def getImageUrl(self):
        """
        Returns:
            imageUrl: the url of the image to use
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getReturnFaceAttributes(self):
        """
        Returns:
            returnFaceAttributes: Analyze and return the one or more specified face attributes Supported face attributes include: age, gender, headPose, smile, facialHair, glasses, emotion, hair, makeup, occlusion, accessories, blur, exposure and noise. Face attribute analysis has additional computational and time cost.
        """
    def getReturnFaceId(self):
        """
        Returns:
            returnFaceId: Return faceIds of the detected faces or not. The default value is true
        """
    def getReturnFaceLandmarks(self):
        """
        Returns:
            returnFaceLandmarks: Return face landmarks of the detected faces or not. The default value is false.
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
    def setCustomServiceName(self, value): ...
    def setEndpoint(self, value): ...
    def setDefaultInternalEndpoint(self, value): ...
    def setLocation(self, value): ...
    def setLinkedService(self, value): ...
