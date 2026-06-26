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

class IdentifyFaces(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        confidenceThreshold (object): Optional parameter.Customized identification confidence threshold, in the range of [0, 1].Advanced user can tweak this value to override defaultinternal threshold for better precision on their scenario data.Note there is no guarantee of this threshold value workingon other data and after algorithm updates.
        errorCol (str): column to hold http errors
        faceIds (object): Array of query faces faceIds, created by the Face - Detect. Each of the faces are identified independently. The valid number of faceIds is between [1, 10]. 
        handler (object): Which strategy to use when handling requests
        largePersonGroupId (object): largePersonGroupId of the target large person group, created by LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        maxNumOfCandidatesReturned (object): The range of maxNumOfCandidatesReturned is between 1 and 100 (default is 10).
        outputCol (str): The name of the output column
        personGroupId (object): personGroupId of the target person group, created by PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        subscriptionKey (object): the API key to use
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    confidenceThreshold: Incomplete
    errorCol: Incomplete
    faceIds: Incomplete
    handler: Incomplete
    largePersonGroupId: Incomplete
    maxNumOfCandidatesReturned: Incomplete
    outputCol: Incomplete
    personGroupId: Incomplete
    subscriptionKey: Incomplete
    timeout: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, confidenceThreshold: Incomplete | None = None, confidenceThresholdCol: Incomplete | None = None, errorCol: str = 'IdentifyFaces_c7779ade3f92_error', faceIds: Incomplete | None = None, faceIdsCol: Incomplete | None = None, handler: Incomplete | None = None, largePersonGroupId: Incomplete | None = None, largePersonGroupIdCol: Incomplete | None = None, maxNumOfCandidatesReturned: Incomplete | None = None, maxNumOfCandidatesReturnedCol: Incomplete | None = None, outputCol: str = 'IdentifyFaces_c7779ade3f92_output', personGroupId: Incomplete | None = None, personGroupIdCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, confidenceThreshold: Incomplete | None = None, confidenceThresholdCol: Incomplete | None = None, errorCol: str = 'IdentifyFaces_c7779ade3f92_error', faceIds: Incomplete | None = None, faceIdsCol: Incomplete | None = None, handler: Incomplete | None = None, largePersonGroupId: Incomplete | None = None, largePersonGroupIdCol: Incomplete | None = None, maxNumOfCandidatesReturned: Incomplete | None = None, maxNumOfCandidatesReturnedCol: Incomplete | None = None, outputCol: str = 'IdentifyFaces_c7779ade3f92_output', personGroupId: Incomplete | None = None, personGroupIdCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None):
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
    def setConfidenceThreshold(self, value):
        """
        Args:
            confidenceThreshold: Optional parameter.Customized identification confidence threshold, in the range of [0, 1].Advanced user can tweak this value to override defaultinternal threshold for better precision on their scenario data.Note there is no guarantee of this threshold value workingon other data and after algorithm updates.
        """
    def setConfidenceThresholdCol(self, value):
        """
        Args:
            confidenceThreshold: Optional parameter.Customized identification confidence threshold, in the range of [0, 1].Advanced user can tweak this value to override defaultinternal threshold for better precision on their scenario data.Note there is no guarantee of this threshold value workingon other data and after algorithm updates.
        """
    def setErrorCol(self, value):
        """
        Args:
            errorCol: column to hold http errors
        """
    def setFaceIds(self, value):
        """
        Args:
            faceIds: Array of query faces faceIds, created by the Face - Detect. Each of the faces are identified independently. The valid number of faceIds is between [1, 10]. 
        """
    def setFaceIdsCol(self, value):
        """
        Args:
            faceIds: Array of query faces faceIds, created by the Face - Detect. Each of the faces are identified independently. The valid number of faceIds is between [1, 10]. 
        """
    def setHandler(self, value):
        """
        Args:
            handler: Which strategy to use when handling requests
        """
    def setLargePersonGroupId(self, value):
        """
        Args:
            largePersonGroupId: largePersonGroupId of the target large person group, created by LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
    def setLargePersonGroupIdCol(self, value):
        """
        Args:
            largePersonGroupId: largePersonGroupId of the target large person group, created by LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
    def setMaxNumOfCandidatesReturned(self, value):
        """
        Args:
            maxNumOfCandidatesReturned: The range of maxNumOfCandidatesReturned is between 1 and 100 (default is 10).
        """
    def setMaxNumOfCandidatesReturnedCol(self, value):
        """
        Args:
            maxNumOfCandidatesReturned: The range of maxNumOfCandidatesReturned is between 1 and 100 (default is 10).
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setPersonGroupId(self, value):
        """
        Args:
            personGroupId: personGroupId of the target person group, created by PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
    def setPersonGroupIdCol(self, value):
        """
        Args:
            personGroupId: personGroupId of the target person group, created by PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
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
    def getConfidenceThreshold(self):
        """
        Returns:
            confidenceThreshold: Optional parameter.Customized identification confidence threshold, in the range of [0, 1].Advanced user can tweak this value to override defaultinternal threshold for better precision on their scenario data.Note there is no guarantee of this threshold value workingon other data and after algorithm updates.
        """
    def getErrorCol(self):
        """
        Returns:
            errorCol: column to hold http errors
        """
    def getFaceIds(self):
        """
        Returns:
            faceIds: Array of query faces faceIds, created by the Face - Detect. Each of the faces are identified independently. The valid number of faceIds is between [1, 10]. 
        """
    def getHandler(self):
        """
        Returns:
            handler: Which strategy to use when handling requests
        """
    def getLargePersonGroupId(self):
        """
        Returns:
            largePersonGroupId: largePersonGroupId of the target large person group, created by LargePersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
        """
    def getMaxNumOfCandidatesReturned(self):
        """
        Returns:
            maxNumOfCandidatesReturned: The range of maxNumOfCandidatesReturned is between 1 and 100 (default is 10).
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getPersonGroupId(self):
        """
        Returns:
            personGroupId: personGroupId of the target person group, created by PersonGroup - Create. Parameter personGroupId and largePersonGroupId should not be provided at the same time.
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
