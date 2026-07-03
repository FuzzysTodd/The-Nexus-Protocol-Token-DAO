from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext, SparkContext as SparkContext
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator, JavaModel as JavaModel, JavaTransformer as JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class TextFeaturizer(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """
    Args:
        binary (bool): If true, all nonegative word counts are set to 1
        caseSensitiveStopWords (bool):  Whether to do a case sensitive comparison over the stop words
        defaultStopWordLanguage (str): Which language to use for the stop word remover, set this to custom to use the stopWords input
        inputCol (str): The name of the input column
        minDocFreq (int): The minimum number of documents in which a term should appear.
        minTokenLength (int): Minimum token length, >= 0.
        nGramLength (int): The size of the Ngrams
        numFeatures (int): Set the number of features to hash each document to
        outputCol (str): The name of the output column
        stopWords (str): The words to be filtered out.
        toLowercase (bool): Indicates whether to convert all characters to lowercase before tokenizing.
        tokenizerGaps (bool): Indicates whether regex splits on gaps (true) or matches tokens (false).
        tokenizerPattern (str): Regex pattern used to match delimiters if gaps is true or tokens if gaps is false.
        useIDF (bool): Whether to scale the Term Frequencies by IDF
        useNGram (bool): Whether to enumerate N grams
        useStopWordsRemover (bool): Whether to remove stop words from tokenized data
        useTokenizer (bool): Whether to tokenize the input
    """
    binary: Incomplete
    caseSensitiveStopWords: Incomplete
    defaultStopWordLanguage: Incomplete
    inputCol: Incomplete
    minDocFreq: Incomplete
    minTokenLength: Incomplete
    nGramLength: Incomplete
    numFeatures: Incomplete
    outputCol: Incomplete
    stopWords: Incomplete
    toLowercase: Incomplete
    tokenizerGaps: Incomplete
    tokenizerPattern: Incomplete
    useIDF: Incomplete
    useNGram: Incomplete
    useStopWordsRemover: Incomplete
    useTokenizer: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, binary: bool = False, caseSensitiveStopWords: bool = False, defaultStopWordLanguage: str = 'english', inputCol: Incomplete | None = None, minDocFreq: int = 1, minTokenLength: int = 0, nGramLength: int = 2, numFeatures: int = 262144, outputCol: str = 'TextFeaturizer_d9ab0c74f693_output', stopWords: Incomplete | None = None, toLowercase: bool = True, tokenizerGaps: bool = True, tokenizerPattern: str = '\\s+', useIDF: bool = True, useNGram: bool = False, useStopWordsRemover: bool = False, useTokenizer: bool = True) -> None: ...
    def setParams(self, binary: bool = False, caseSensitiveStopWords: bool = False, defaultStopWordLanguage: str = 'english', inputCol: Incomplete | None = None, minDocFreq: int = 1, minTokenLength: int = 0, nGramLength: int = 2, numFeatures: int = 262144, outputCol: str = 'TextFeaturizer_d9ab0c74f693_output', stopWords: Incomplete | None = None, toLowercase: bool = True, tokenizerGaps: bool = True, tokenizerPattern: str = '\\s+', useIDF: bool = True, useNGram: bool = False, useStopWordsRemover: bool = False, useTokenizer: bool = True):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setBinary(self, value):
        """
        Args:
            binary: If true, all nonegative word counts are set to 1
        """
    def setCaseSensitiveStopWords(self, value):
        """
        Args:
            caseSensitiveStopWords:  Whether to do a case sensitive comparison over the stop words
        """
    def setDefaultStopWordLanguage(self, value):
        """
        Args:
            defaultStopWordLanguage: Which language to use for the stop word remover, set this to custom to use the stopWords input
        """
    def setInputCol(self, value):
        """
        Args:
            inputCol: The name of the input column
        """
    def setMinDocFreq(self, value):
        """
        Args:
            minDocFreq: The minimum number of documents in which a term should appear.
        """
    def setMinTokenLength(self, value):
        """
        Args:
            minTokenLength: Minimum token length, >= 0.
        """
    def setNGramLength(self, value):
        """
        Args:
            nGramLength: The size of the Ngrams
        """
    def setNumFeatures(self, value):
        """
        Args:
            numFeatures: Set the number of features to hash each document to
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setStopWords(self, value):
        """
        Args:
            stopWords: The words to be filtered out.
        """
    def setToLowercase(self, value):
        """
        Args:
            toLowercase: Indicates whether to convert all characters to lowercase before tokenizing.
        """
    def setTokenizerGaps(self, value):
        """
        Args:
            tokenizerGaps: Indicates whether regex splits on gaps (true) or matches tokens (false).
        """
    def setTokenizerPattern(self, value):
        """
        Args:
            tokenizerPattern: Regex pattern used to match delimiters if gaps is true or tokens if gaps is false.
        """
    def setUseIDF(self, value):
        """
        Args:
            useIDF: Whether to scale the Term Frequencies by IDF
        """
    def setUseNGram(self, value):
        """
        Args:
            useNGram: Whether to enumerate N grams
        """
    def setUseStopWordsRemover(self, value):
        """
        Args:
            useStopWordsRemover: Whether to remove stop words from tokenized data
        """
    def setUseTokenizer(self, value):
        """
        Args:
            useTokenizer: Whether to tokenize the input
        """
    def getBinary(self):
        """
        Returns:
            binary: If true, all nonegative word counts are set to 1
        """
    def getCaseSensitiveStopWords(self):
        """
        Returns:
            caseSensitiveStopWords:  Whether to do a case sensitive comparison over the stop words
        """
    def getDefaultStopWordLanguage(self):
        """
        Returns:
            defaultStopWordLanguage: Which language to use for the stop word remover, set this to custom to use the stopWords input
        """
    def getInputCol(self):
        """
        Returns:
            inputCol: The name of the input column
        """
    def getMinDocFreq(self):
        """
        Returns:
            minDocFreq: The minimum number of documents in which a term should appear.
        """
    def getMinTokenLength(self):
        """
        Returns:
            minTokenLength: Minimum token length, >= 0.
        """
    def getNGramLength(self):
        """
        Returns:
            nGramLength: The size of the Ngrams
        """
    def getNumFeatures(self):
        """
        Returns:
            numFeatures: Set the number of features to hash each document to
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getStopWords(self):
        """
        Returns:
            stopWords: The words to be filtered out.
        """
    def getToLowercase(self):
        """
        Returns:
            toLowercase: Indicates whether to convert all characters to lowercase before tokenizing.
        """
    def getTokenizerGaps(self):
        """
        Returns:
            tokenizerGaps: Indicates whether regex splits on gaps (true) or matches tokens (false).
        """
    def getTokenizerPattern(self):
        """
        Returns:
            tokenizerPattern: Regex pattern used to match delimiters if gaps is true or tokens if gaps is false.
        """
    def getUseIDF(self):
        """
        Returns:
            useIDF: Whether to scale the Term Frequencies by IDF
        """
    def getUseNGram(self):
        """
        Returns:
            useNGram: Whether to enumerate N grams
        """
    def getUseStopWordsRemover(self):
        """
        Returns:
            useStopWordsRemover: Whether to remove stop words from tokenized data
        """
    def getUseTokenizer(self):
        """
        Returns:
            useTokenizer: Whether to tokenize the input
        """
