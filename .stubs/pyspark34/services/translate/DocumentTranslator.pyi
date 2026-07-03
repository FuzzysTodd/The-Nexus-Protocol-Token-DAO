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

class DocumentTranslator(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        backoffs (list): array of backoffs to use in the handler
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        errorCol (str): column to hold http errors
        filterPrefix (object): A case-sensitive prefix string to filter documents in the source path for translation. For example, when using an Azure storage blob Uri, use the prefix to restrict sub folders for translation.
        filterSuffix (object): A case-sensitive suffix string to filter documents in the source path for translation. This is most often use for file extensions.
        initialPollingDelay (int): number of milliseconds to wait before first poll for result
        maxPollingRetries (int): number of times to poll
        outputCol (str): The name of the output column
        pollingDelay (int): number of milliseconds to wait between polling
        serviceName (str): 
        sourceLanguage (object): Language code. If none is specified, we will perform auto detect on the document.
        sourceStorageSource (object): Storage source of source input.
        sourceUrl (object): Location of the folder / container or single file with your documents.
        storageType (object): Storage type of the input documents source string. Required for single document translation only.
        subscriptionKey (object): the API key to use
        suppressMaxRetriesException (bool): set true to suppress the maxumimum retries exception and report in the error column
        targets (object): Destination for the finished translated documents.
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    backoffs: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    errorCol: Incomplete
    filterPrefix: Incomplete
    filterSuffix: Incomplete
    initialPollingDelay: Incomplete
    maxPollingRetries: Incomplete
    outputCol: Incomplete
    pollingDelay: Incomplete
    serviceName: Incomplete
    sourceLanguage: Incomplete
    sourceStorageSource: Incomplete
    sourceUrl: Incomplete
    storageType: Incomplete
    subscriptionKey: Incomplete
    suppressMaxRetriesException: Incomplete
    targets: Incomplete
    timeout: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, backoffs=[100, 500, 1000], concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'DocumentTranslator_ce5abc3a49c6_error', filterPrefix: Incomplete | None = None, filterPrefixCol: Incomplete | None = None, filterSuffix: Incomplete | None = None, filterSuffixCol: Incomplete | None = None, initialPollingDelay: int = 300, maxPollingRetries: int = 1000, outputCol: str = 'DocumentTranslator_ce5abc3a49c6_output', pollingDelay: int = 300, serviceName: Incomplete | None = None, sourceLanguage: Incomplete | None = None, sourceLanguageCol: Incomplete | None = None, sourceStorageSource: Incomplete | None = None, sourceStorageSourceCol: Incomplete | None = None, sourceUrl: Incomplete | None = None, sourceUrlCol: Incomplete | None = None, storageType: Incomplete | None = None, storageTypeCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, suppressMaxRetriesException: bool = False, targets: Incomplete | None = None, targetsCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, backoffs=[100, 500, 1000], concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'DocumentTranslator_ce5abc3a49c6_error', filterPrefix: Incomplete | None = None, filterPrefixCol: Incomplete | None = None, filterSuffix: Incomplete | None = None, filterSuffixCol: Incomplete | None = None, initialPollingDelay: int = 300, maxPollingRetries: int = 1000, outputCol: str = 'DocumentTranslator_ce5abc3a49c6_output', pollingDelay: int = 300, serviceName: Incomplete | None = None, sourceLanguage: Incomplete | None = None, sourceLanguageCol: Incomplete | None = None, sourceStorageSource: Incomplete | None = None, sourceStorageSourceCol: Incomplete | None = None, sourceUrl: Incomplete | None = None, sourceUrlCol: Incomplete | None = None, storageType: Incomplete | None = None, storageTypeCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, suppressMaxRetriesException: bool = False, targets: Incomplete | None = None, targetsCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None):
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
    def setFilterPrefix(self, value):
        """
        Args:
            filterPrefix: A case-sensitive prefix string to filter documents in the source path for translation. For example, when using an Azure storage blob Uri, use the prefix to restrict sub folders for translation.
        """
    def setFilterPrefixCol(self, value):
        """
        Args:
            filterPrefix: A case-sensitive prefix string to filter documents in the source path for translation. For example, when using an Azure storage blob Uri, use the prefix to restrict sub folders for translation.
        """
    def setFilterSuffix(self, value):
        """
        Args:
            filterSuffix: A case-sensitive suffix string to filter documents in the source path for translation. This is most often use for file extensions.
        """
    def setFilterSuffixCol(self, value):
        """
        Args:
            filterSuffix: A case-sensitive suffix string to filter documents in the source path for translation. This is most often use for file extensions.
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
    def setServiceName(self, value):
        """
        Args:
            serviceName: 
        """
    def setSourceLanguage(self, value):
        """
        Args:
            sourceLanguage: Language code. If none is specified, we will perform auto detect on the document.
        """
    def setSourceLanguageCol(self, value):
        """
        Args:
            sourceLanguage: Language code. If none is specified, we will perform auto detect on the document.
        """
    def setSourceStorageSource(self, value):
        """
        Args:
            sourceStorageSource: Storage source of source input.
        """
    def setSourceStorageSourceCol(self, value):
        """
        Args:
            sourceStorageSource: Storage source of source input.
        """
    def setSourceUrl(self, value):
        """
        Args:
            sourceUrl: Location of the folder / container or single file with your documents.
        """
    def setSourceUrlCol(self, value):
        """
        Args:
            sourceUrl: Location of the folder / container or single file with your documents.
        """
    def setStorageType(self, value):
        """
        Args:
            storageType: Storage type of the input documents source string. Required for single document translation only.
        """
    def setStorageTypeCol(self, value):
        """
        Args:
            storageType: Storage type of the input documents source string. Required for single document translation only.
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
    def setTargets(self, value):
        """
        Args:
            targets: Destination for the finished translated documents.
        """
    def setTargetsCol(self, value):
        """
        Args:
            targets: Destination for the finished translated documents.
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
    def getFilterPrefix(self):
        """
        Returns:
            filterPrefix: A case-sensitive prefix string to filter documents in the source path for translation. For example, when using an Azure storage blob Uri, use the prefix to restrict sub folders for translation.
        """
    def getFilterSuffix(self):
        """
        Returns:
            filterSuffix: A case-sensitive suffix string to filter documents in the source path for translation. This is most often use for file extensions.
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
    def getServiceName(self):
        """
        Returns:
            serviceName: 
        """
    def getSourceLanguage(self):
        """
        Returns:
            sourceLanguage: Language code. If none is specified, we will perform auto detect on the document.
        """
    def getSourceStorageSource(self):
        """
        Returns:
            sourceStorageSource: Storage source of source input.
        """
    def getSourceUrl(self):
        """
        Returns:
            sourceUrl: Location of the folder / container or single file with your documents.
        """
    def getStorageType(self):
        """
        Returns:
            storageType: Storage type of the input documents source string. Required for single document translation only.
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
    def getTargets(self):
        """
        Returns:
            targets: Destination for the finished translated documents.
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
    def setLinkedService(self, value): ...
