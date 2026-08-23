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

class AddDocuments(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        actionCol (str):  You can combine actions, such as an upload and a delete, in the same batch.  upload: An upload action is similar to an 'upsert' where the document will be inserted if it is new and updated/replaced if it exists. Note that all fields are replaced in the update case.  merge: Merge updates an existing document with the specified fields. If the document doesn't exist, the merge will fail. Any field you specify in a merge will replace the existing field in the document. This includes fields of type Collection(Edm.String). For example, if the document contains a field 'tags' with value ['budget'] and you execute a merge with value ['economy', 'pool'] for 'tags', the final value of the 'tags' field will be ['economy', 'pool'].  It will not be ['budget', 'economy', 'pool'].  mergeOrUpload: This action behaves like merge if a document  with the given key already exists in the index.  If the document does not exist, it behaves like upload with a new document.  delete: Delete removes the specified document from the index.  Note that any field you specify in a delete operation,  other than the key field, will be ignored. If you want to   remove an individual field from a document, use merge   instead and simply set the field explicitly to null.     
        batchSize (int): The max size of the buffer
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        errorCol (str): column to hold http errors
        handler (object): Which strategy to use when handling requests
        indexName (str): 
        outputCol (str): The name of the output column
        serviceName (str): 
        subscriptionKey (object): the API key to use
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    actionCol: Incomplete
    batchSize: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    errorCol: Incomplete
    handler: Incomplete
    indexName: Incomplete
    outputCol: Incomplete
    serviceName: Incomplete
    subscriptionKey: Incomplete
    timeout: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, actionCol: str = '@search.action', batchSize: int = 100, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'AddDocuments_9d4744a278aa_error', handler: Incomplete | None = None, indexName: Incomplete | None = None, outputCol: str = 'AddDocuments_9d4744a278aa_output', serviceName: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, actionCol: str = '@search.action', batchSize: int = 100, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'AddDocuments_9d4744a278aa_error', handler: Incomplete | None = None, indexName: Incomplete | None = None, outputCol: str = 'AddDocuments_9d4744a278aa_output', serviceName: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None):
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
    def setActionCol(self, value):
        """
        Args:
            actionCol:  You can combine actions, such as an upload and a delete, in the same batch.  upload: An upload action is similar to an 'upsert' where the document will be inserted if it is new and updated/replaced if it exists. Note that all fields are replaced in the update case.  merge: Merge updates an existing document with the specified fields. If the document doesn't exist, the merge will fail. Any field you specify in a merge will replace the existing field in the document. This includes fields of type Collection(Edm.String). For example, if the document contains a field 'tags' with value ['budget'] and you execute a merge with value ['economy', 'pool'] for 'tags', the final value of the 'tags' field will be ['economy', 'pool'].  It will not be ['budget', 'economy', 'pool'].  mergeOrUpload: This action behaves like merge if a document  with the given key already exists in the index.  If the document does not exist, it behaves like upload with a new document.  delete: Delete removes the specified document from the index.  Note that any field you specify in a delete operation,  other than the key field, will be ignored. If you want to   remove an individual field from a document, use merge   instead and simply set the field explicitly to null.     
        """
    def setBatchSize(self, value):
        """
        Args:
            batchSize: The max size of the buffer
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
    def setIndexName(self, value):
        """
        Args:
            indexName: 
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setServiceName(self, value):
        """
        Args:
            serviceName: 
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
    def getActionCol(self):
        """
        Returns:
            actionCol:  You can combine actions, such as an upload and a delete, in the same batch.  upload: An upload action is similar to an 'upsert' where the document will be inserted if it is new and updated/replaced if it exists. Note that all fields are replaced in the update case.  merge: Merge updates an existing document with the specified fields. If the document doesn't exist, the merge will fail. Any field you specify in a merge will replace the existing field in the document. This includes fields of type Collection(Edm.String). For example, if the document contains a field 'tags' with value ['budget'] and you execute a merge with value ['economy', 'pool'] for 'tags', the final value of the 'tags' field will be ['economy', 'pool'].  It will not be ['budget', 'economy', 'pool'].  mergeOrUpload: This action behaves like merge if a document  with the given key already exists in the index.  If the document does not exist, it behaves like upload with a new document.  delete: Delete removes the specified document from the index.  Note that any field you specify in a delete operation,  other than the key field, will be ignored. If you want to   remove an individual field from a document, use merge   instead and simply set the field explicitly to null.     
        """
    def getBatchSize(self):
        """
        Returns:
            batchSize: The max size of the buffer
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
    def getIndexName(self):
        """
        Returns:
            indexName: 
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getServiceName(self):
        """
        Returns:
            serviceName: 
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
