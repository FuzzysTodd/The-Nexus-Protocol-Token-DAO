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

class VerifyFaces(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        errorCol (str): column to hold http errors
        faceId (object): faceId of the face, comes from Face - Detect.
        faceId1 (object): faceId of one face, comes from Face - Detect.
        faceId2 (object): faceId of another face, comes from Face - Detect.
        handler (object): Which strategy to use when handling requests
        largePersonGroupId (object): Using existing largePersonGroupId and personId for fast adding a specified person. largePersonGroupId is created in LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        outputCol (str): The name of the output column
        personGroupId (object): Using existing personGroupId and personId for fast loading a specified person. personGroupId is created in PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        personId (object): Specify a certain person in a person group or a large person group. personId is created in PersonGroup Person - Create or LargePersonGroup Person - Create.
        subscriptionKey (object): the API key to use
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    errorCol: Incomplete
    faceId: Incomplete
    faceId1: Incomplete
    faceId2: Incomplete
    handler: Incomplete
    largePersonGroupId: Incomplete
    outputCol: Incomplete
    personGroupId: Incomplete
    personId: Incomplete
    subscriptionKey: Incomplete
    timeout: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'VerifyFaces_8265032beab3_error', faceId: Incomplete | None = None, faceIdCol: Incomplete | None = None, faceId1: Incomplete | None = None, faceId1Col: Incomplete | None = None, faceId2: Incomplete | None = None, faceId2Col: Incomplete | None = None, handler: Incomplete | None = None, largePersonGroupId: Incomplete | None = None, largePersonGroupIdCol: Incomplete | None = None, outputCol: str = 'VerifyFaces_8265032beab3_output', personGroupId: Incomplete | None = None, personGroupIdCol: Incomplete | None = None, personId: Incomplete | None = None, personIdCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'VerifyFaces_8265032beab3_error', faceId: Incomplete | None = None, faceIdCol: Incomplete | None = None, faceId1: Incomplete | None = None, faceId1Col: Incomplete | None = None, faceId2: Incomplete | None = None, faceId2Col: Incomplete | None = None, handler: Incomplete | None = None, largePersonGroupId: Incomplete | None = None, largePersonGroupIdCol: Incomplete | None = None, outputCol: str = 'VerifyFaces_8265032beab3_output', personGroupId: Incomplete | None = None, personGroupIdCol: Incomplete | None = None, personId: Incomplete | None = None, personIdCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None):
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
    def setFaceId(self, value):
        """
        Args:
            faceId: faceId of the face, comes from Face - Detect.
        """
    def setFaceIdCol(self, value):
        """
        Args:
            faceId: faceId of the face, comes from Face - Detect.
        """
    def setFaceId1(self, value):
        """
        Args:
            faceId1: faceId of one face, comes from Face - Detect.
        """
    def setFaceId1Col(self, value):
        """
        Args:
            faceId1: faceId of one face, comes from Face - Detect.
        """
    def setFaceId2(self, value):
        """
        Args:
            faceId2: faceId of another face, comes from Face - Detect.
        """
    def setFaceId2Col(self, value):
        """
        Args:
            faceId2: faceId of another face, comes from Face - Detect.
        """
    def setHandler(self, value):
        """
        Args:
            handler: Which strategy to use when handling requests
        """
    def setLargePersonGroupId(self, value):
        """
        Args:
            largePersonGroupId: Using existing largePersonGroupId and personId for fast adding a specified person. largePersonGroupId is created in LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
    def setLargePersonGroupIdCol(self, value):
        """
        Args:
            largePersonGroupId: Using existing largePersonGroupId and personId for fast adding a specified person. largePersonGroupId is created in LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setPersonGroupId(self, value):
        """
        Args:
            personGroupId: Using existing personGroupId and personId for fast loading a specified person. personGroupId is created in PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
    def setPersonGroupIdCol(self, value):
        """
        Args:
            personGroupId: Using existing personGroupId and personId for fast loading a specified person. personGroupId is created in PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
    def setPersonId(self, value):
        """
        Args:
            personId: Specify a certain person in a person group or a large person group. personId is created in PersonGroup Person - Create or LargePersonGroup Person - Create.
        """
    def setPersonIdCol(self, value):
        """
        Args:
            personId: Specify a certain person in a person group or a large person group. personId is created in PersonGroup Person - Create or LargePersonGroup Person - Create.
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
    def getFaceId(self):
        """
        Returns:
            faceId: faceId of the face, comes from Face - Detect.
        """
    def getFaceId1(self):
        """
        Returns:
            faceId1: faceId of one face, comes from Face - Detect.
        """
    def getFaceId2(self):
        """
        Returns:
            faceId2: faceId of another face, comes from Face - Detect.
        """
    def getHandler(self):
        """
        Returns:
            handler: Which strategy to use when handling requests
        """
    def getLargePersonGroupId(self):
        """
        Returns:
            largePersonGroupId: Using existing largePersonGroupId and personId for fast adding a specified person. largePersonGroupId is created in LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getPersonGroupId(self):
        """
        Returns:
            personGroupId: Using existing personGroupId and personId for fast loading a specified person. personGroupId is created in PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
    def getPersonId(self):
        """
        Returns:
            personId: Specify a certain person in a person group or a large person group. personId is created in PersonGroup Person - Create or LargePersonGroup Person - Create.
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
