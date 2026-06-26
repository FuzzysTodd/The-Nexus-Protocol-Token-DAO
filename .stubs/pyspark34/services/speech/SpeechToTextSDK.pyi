from pyspark.ml.param.shared import *
from synapse.ml.core.serialize.java_params_patch import *
from synapse.ml.core.schema.Utils import *
from _typeshed import Incomplete
from pyspark import SQLContext as SQLContext
from pyspark.ml.evaluation import JavaEvaluator as JavaEvaluator
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from pyspark.ml.wrapper import JavaEstimator as JavaEstimator, JavaModel as JavaModel, JavaTransformer
from pyspark.sql import DataFrame as DataFrame
from synapse.ml.core.platform import running_on_synapse_internal as running_on_synapse_internal
from synapse.ml.core.schema.TypeConversionUtils import complexTypeConverter as complexTypeConverter, generateTypeConverter as generateTypeConverter

basestring = str

class SpeechToTextSDK(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        audioDataCol (str): Column holding audio data, must be either ByteArrays or Strings representing file URIs
        endpointId (str): endpoint for custom speech models
        extraFfmpegArgs (list): extra arguments to for ffmpeg output decoding
        fileType (object): The file type of the sound files, supported types: wav, ogg, mp3
        format (object):  Specifies the result format. Accepted values are simple and detailed. Default is simple.     
        language (object):  Identifies the spoken language that is being recognized.     
        outputCol (str): The name of the output column
        participantsJson (object): a json representation of a list of conversation participants (email, language, user)
        profanity (object):  Specifies how to handle profanity in recognition results. Accepted values are masked, which replaces profanity with asterisks, removed, which remove all profanity from the result, or raw, which includes the profanity in the result. The default setting is masked.     
        recordAudioData (bool): Whether to record audio data to a file location, for use only with m3u8 streams
        recordedFileNameCol (str): Column holding file names to write audio data to if ``recordAudioData'' is set to true
        streamIntermediateResults (bool): Whether or not to immediately return itermediate results, or group in a sequence
        subscriptionKey (object): the API key to use
        url (str): Url of the service
        wordLevelTimestamps (object): Whether to request timestamps foe each indivdual word
    """
    audioDataCol: Incomplete
    endpointId: Incomplete
    extraFfmpegArgs: Incomplete
    fileType: Incomplete
    format: Incomplete
    language: Incomplete
    outputCol: Incomplete
    participantsJson: Incomplete
    profanity: Incomplete
    recordAudioData: Incomplete
    recordedFileNameCol: Incomplete
    streamIntermediateResults: Incomplete
    subscriptionKey: Incomplete
    url: Incomplete
    wordLevelTimestamps: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, audioDataCol: Incomplete | None = None, endpointId: Incomplete | None = None, extraFfmpegArgs=[], fileType: Incomplete | None = None, fileTypeCol: Incomplete | None = None, format: Incomplete | None = None, formatCol: Incomplete | None = None, language: Incomplete | None = None, languageCol: Incomplete | None = None, outputCol: Incomplete | None = None, participantsJson: Incomplete | None = None, participantsJsonCol: Incomplete | None = None, profanity: Incomplete | None = None, profanityCol: Incomplete | None = None, recordAudioData: bool = False, recordedFileNameCol: Incomplete | None = None, streamIntermediateResults: bool = True, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, url: Incomplete | None = None, wordLevelTimestamps: Incomplete | None = None, wordLevelTimestampsCol: Incomplete | None = None) -> None: ...
    def setParams(self, audioDataCol: Incomplete | None = None, endpointId: Incomplete | None = None, extraFfmpegArgs=[], fileType: Incomplete | None = None, fileTypeCol: Incomplete | None = None, format: Incomplete | None = None, formatCol: Incomplete | None = None, language: Incomplete | None = None, languageCol: Incomplete | None = None, outputCol: Incomplete | None = None, participantsJson: Incomplete | None = None, participantsJsonCol: Incomplete | None = None, profanity: Incomplete | None = None, profanityCol: Incomplete | None = None, recordAudioData: bool = False, recordedFileNameCol: Incomplete | None = None, streamIntermediateResults: bool = True, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, url: Incomplete | None = None, wordLevelTimestamps: Incomplete | None = None, wordLevelTimestampsCol: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setAudioDataCol(self, value):
        """
        Args:
            audioDataCol: Column holding audio data, must be either ByteArrays or Strings representing file URIs
        """
    def setEndpointId(self, value):
        """
        Args:
            endpointId: endpoint for custom speech models
        """
    def setExtraFfmpegArgs(self, value):
        """
        Args:
            extraFfmpegArgs: extra arguments to for ffmpeg output decoding
        """
    def setFileType(self, value):
        """
        Args:
            fileType: The file type of the sound files, supported types: wav, ogg, mp3
        """
    def setFileTypeCol(self, value):
        """
        Args:
            fileType: The file type of the sound files, supported types: wav, ogg, mp3
        """
    def setFormat(self, value):
        """
        Args:
            format:  Specifies the result format. Accepted values are simple and detailed. Default is simple.     
        """
    def setFormatCol(self, value):
        """
        Args:
            format:  Specifies the result format. Accepted values are simple and detailed. Default is simple.     
        """
    def setLanguage(self, value):
        """
        Args:
            language:  Identifies the spoken language that is being recognized.     
        """
    def setLanguageCol(self, value):
        """
        Args:
            language:  Identifies the spoken language that is being recognized.     
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setParticipantsJson(self, value):
        """
        Args:
            participantsJson: a json representation of a list of conversation participants (email, language, user)
        """
    def setParticipantsJsonCol(self, value):
        """
        Args:
            participantsJson: a json representation of a list of conversation participants (email, language, user)
        """
    def setProfanity(self, value):
        """
        Args:
            profanity:  Specifies how to handle profanity in recognition results. Accepted values are masked, which replaces profanity with asterisks, removed, which remove all profanity from the result, or raw, which includes the profanity in the result. The default setting is masked.     
        """
    def setProfanityCol(self, value):
        """
        Args:
            profanity:  Specifies how to handle profanity in recognition results. Accepted values are masked, which replaces profanity with asterisks, removed, which remove all profanity from the result, or raw, which includes the profanity in the result. The default setting is masked.     
        """
    def setRecordAudioData(self, value):
        """
        Args:
            recordAudioData: Whether to record audio data to a file location, for use only with m3u8 streams
        """
    def setRecordedFileNameCol(self, value):
        """
        Args:
            recordedFileNameCol: Column holding file names to write audio data to if ``recordAudioData'' is set to true
        """
    def setStreamIntermediateResults(self, value):
        """
        Args:
            streamIntermediateResults: Whether or not to immediately return itermediate results, or group in a sequence
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
    def setUrl(self, value):
        """
        Args:
            url: Url of the service
        """
    def setWordLevelTimestamps(self, value):
        """
        Args:
            wordLevelTimestamps: Whether to request timestamps foe each indivdual word
        """
    def setWordLevelTimestampsCol(self, value):
        """
        Args:
            wordLevelTimestamps: Whether to request timestamps foe each indivdual word
        """
    def getAudioDataCol(self):
        """
        Returns:
            audioDataCol: Column holding audio data, must be either ByteArrays or Strings representing file URIs
        """
    def getEndpointId(self):
        """
        Returns:
            endpointId: endpoint for custom speech models
        """
    def getExtraFfmpegArgs(self):
        """
        Returns:
            extraFfmpegArgs: extra arguments to for ffmpeg output decoding
        """
    def getFileType(self):
        """
        Returns:
            fileType: The file type of the sound files, supported types: wav, ogg, mp3
        """
    def getFormat(self):
        """
        Returns:
            format:  Specifies the result format. Accepted values are simple and detailed. Default is simple.     
        """
    def getLanguage(self):
        """
        Returns:
            language:  Identifies the spoken language that is being recognized.     
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getParticipantsJson(self):
        """
        Returns:
            participantsJson: a json representation of a list of conversation participants (email, language, user)
        """
    def getProfanity(self):
        """
        Returns:
            profanity:  Specifies how to handle profanity in recognition results. Accepted values are masked, which replaces profanity with asterisks, removed, which remove all profanity from the result, or raw, which includes the profanity in the result. The default setting is masked.     
        """
    def getRecordAudioData(self):
        """
        Returns:
            recordAudioData: Whether to record audio data to a file location, for use only with m3u8 streams
        """
    def getRecordedFileNameCol(self):
        """
        Returns:
            recordedFileNameCol: Column holding file names to write audio data to if ``recordAudioData'' is set to true
        """
    def getStreamIntermediateResults(self):
        """
        Returns:
            streamIntermediateResults: Whether or not to immediately return itermediate results, or group in a sequence
        """
    def getSubscriptionKey(self):
        """
        Returns:
            subscriptionKey: the API key to use
        """
    def getUrl(self):
        """
        Returns:
            url: Url of the service
        """
    def getWordLevelTimestamps(self):
        """
        Returns:
            wordLevelTimestamps: Whether to request timestamps foe each indivdual word
        """
    def setLocation(self, value): ...
    def setLinkedService(self, value): ...
