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

class TextToSpeech(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        errorCol (str): column to hold http errors
        language (object): The name of the language used for synthesis
        locale (object): The locale of the input text
        outputFileCol (str): The location of the saved file as an HDFS compliant URI
        outputFormat (object): The format for the output audio can be one of ArraySeq(Raw8Khz8BitMonoMULaw, Riff16Khz16KbpsMonoSiren, Audio16Khz16KbpsMonoSiren, Audio16Khz32KBitRateMonoMp3, Audio16Khz128KBitRateMonoMp3, Audio16Khz64KBitRateMonoMp3, Audio24Khz48KBitRateMonoMp3, Audio24Khz96KBitRateMonoMp3, Audio24Khz160KBitRateMonoMp3, Raw16Khz16BitMonoTrueSilk, Riff16Khz16BitMonoPcm, Riff8Khz16BitMonoPcm, Riff24Khz16BitMonoPcm, Riff8Khz8BitMonoMULaw, Raw16Khz16BitMonoPcm, Raw24Khz16BitMonoPcm, Raw8Khz16BitMonoPcm, Ogg16Khz16BitMonoOpus, Ogg24Khz16BitMonoOpus, Raw48Khz16BitMonoPcm, Riff48Khz16BitMonoPcm, Audio48Khz96KBitRateMonoMp3, Audio48Khz192KBitRateMonoMp3, Ogg48Khz16BitMonoOpus, Webm16Khz16BitMonoOpus, Webm24Khz16BitMonoOpus, Raw24Khz16BitMonoTrueSilk, Raw8Khz8BitMonoALaw, Riff8Khz8BitMonoALaw, Webm24Khz16Bit24KbpsMonoOpus, Audio16Khz16Bit32KbpsMonoOpus, Audio24Khz16Bit48KbpsMonoOpus, Audio24Khz16Bit24KbpsMonoOpus, Raw22050Hz16BitMonoPcm, Riff22050Hz16BitMonoPcm, Raw44100Hz16BitMonoPcm, Riff44100Hz16BitMonoPcm, AmrWb16000Hz)
        subscriptionKey (object): the API key to use
        text (object): The text to synthesize
        url (str): Url of the service
        useSSML (object): whether to interpret the provided text input as SSML (Speech Synthesis Markup Language). The default value is false.
        voiceName (object): The name of the voice used for synthesis
    """
    errorCol: Incomplete
    language: Incomplete
    locale: Incomplete
    outputFileCol: Incomplete
    outputFormat: Incomplete
    subscriptionKey: Incomplete
    text: Incomplete
    url: Incomplete
    useSSML: Incomplete
    voiceName: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, errorCol: str = 'TextToSpeech_52a79bc87289_errors', language: Incomplete | None = None, languageCol: Incomplete | None = None, locale: Incomplete | None = None, localeCol: Incomplete | None = None, outputFileCol: Incomplete | None = None, outputFormat: Incomplete | None = None, outputFormatCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, text: Incomplete | None = None, textCol: Incomplete | None = None, url: Incomplete | None = None, useSSML: Incomplete | None = None, useSSMLCol: Incomplete | None = None, voiceName: Incomplete | None = None, voiceNameCol: Incomplete | None = None) -> None: ...
    def setParams(self, errorCol: str = 'TextToSpeech_52a79bc87289_errors', language: Incomplete | None = None, languageCol: Incomplete | None = None, locale: Incomplete | None = None, localeCol: Incomplete | None = None, outputFileCol: Incomplete | None = None, outputFormat: Incomplete | None = None, outputFormatCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, text: Incomplete | None = None, textCol: Incomplete | None = None, url: Incomplete | None = None, useSSML: Incomplete | None = None, useSSMLCol: Incomplete | None = None, voiceName: Incomplete | None = None, voiceNameCol: Incomplete | None = None):
        """
        Set the (keyword only) parameters
        """
    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
    def setErrorCol(self, value):
        """
        Args:
            errorCol: column to hold http errors
        """
    def setLanguage(self, value):
        """
        Args:
            language: The name of the language used for synthesis
        """
    def setLanguageCol(self, value):
        """
        Args:
            language: The name of the language used for synthesis
        """
    def setLocale(self, value):
        """
        Args:
            locale: The locale of the input text
        """
    def setLocaleCol(self, value):
        """
        Args:
            locale: The locale of the input text
        """
    def setOutputFileCol(self, value):
        """
        Args:
            outputFileCol: The location of the saved file as an HDFS compliant URI
        """
    def setOutputFormat(self, value):
        """
        Args:
            outputFormat: The format for the output audio can be one of ArraySeq(Raw8Khz8BitMonoMULaw, Riff16Khz16KbpsMonoSiren, Audio16Khz16KbpsMonoSiren, Audio16Khz32KBitRateMonoMp3, Audio16Khz128KBitRateMonoMp3, Audio16Khz64KBitRateMonoMp3, Audio24Khz48KBitRateMonoMp3, Audio24Khz96KBitRateMonoMp3, Audio24Khz160KBitRateMonoMp3, Raw16Khz16BitMonoTrueSilk, Riff16Khz16BitMonoPcm, Riff8Khz16BitMonoPcm, Riff24Khz16BitMonoPcm, Riff8Khz8BitMonoMULaw, Raw16Khz16BitMonoPcm, Raw24Khz16BitMonoPcm, Raw8Khz16BitMonoPcm, Ogg16Khz16BitMonoOpus, Ogg24Khz16BitMonoOpus, Raw48Khz16BitMonoPcm, Riff48Khz16BitMonoPcm, Audio48Khz96KBitRateMonoMp3, Audio48Khz192KBitRateMonoMp3, Ogg48Khz16BitMonoOpus, Webm16Khz16BitMonoOpus, Webm24Khz16BitMonoOpus, Raw24Khz16BitMonoTrueSilk, Raw8Khz8BitMonoALaw, Riff8Khz8BitMonoALaw, Webm24Khz16Bit24KbpsMonoOpus, Audio16Khz16Bit32KbpsMonoOpus, Audio24Khz16Bit48KbpsMonoOpus, Audio24Khz16Bit24KbpsMonoOpus, Raw22050Hz16BitMonoPcm, Riff22050Hz16BitMonoPcm, Raw44100Hz16BitMonoPcm, Riff44100Hz16BitMonoPcm, AmrWb16000Hz)
        """
    def setOutputFormatCol(self, value):
        """
        Args:
            outputFormat: The format for the output audio can be one of ArraySeq(Raw8Khz8BitMonoMULaw, Riff16Khz16KbpsMonoSiren, Audio16Khz16KbpsMonoSiren, Audio16Khz32KBitRateMonoMp3, Audio16Khz128KBitRateMonoMp3, Audio16Khz64KBitRateMonoMp3, Audio24Khz48KBitRateMonoMp3, Audio24Khz96KBitRateMonoMp3, Audio24Khz160KBitRateMonoMp3, Raw16Khz16BitMonoTrueSilk, Riff16Khz16BitMonoPcm, Riff8Khz16BitMonoPcm, Riff24Khz16BitMonoPcm, Riff8Khz8BitMonoMULaw, Raw16Khz16BitMonoPcm, Raw24Khz16BitMonoPcm, Raw8Khz16BitMonoPcm, Ogg16Khz16BitMonoOpus, Ogg24Khz16BitMonoOpus, Raw48Khz16BitMonoPcm, Riff48Khz16BitMonoPcm, Audio48Khz96KBitRateMonoMp3, Audio48Khz192KBitRateMonoMp3, Ogg48Khz16BitMonoOpus, Webm16Khz16BitMonoOpus, Webm24Khz16BitMonoOpus, Raw24Khz16BitMonoTrueSilk, Raw8Khz8BitMonoALaw, Riff8Khz8BitMonoALaw, Webm24Khz16Bit24KbpsMonoOpus, Audio16Khz16Bit32KbpsMonoOpus, Audio24Khz16Bit48KbpsMonoOpus, Audio24Khz16Bit24KbpsMonoOpus, Raw22050Hz16BitMonoPcm, Riff22050Hz16BitMonoPcm, Raw44100Hz16BitMonoPcm, Riff44100Hz16BitMonoPcm, AmrWb16000Hz)
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
            text: The text to synthesize
        """
    def setTextCol(self, value):
        """
        Args:
            text: The text to synthesize
        """
    def setUrl(self, value):
        """
        Args:
            url: Url of the service
        """
    def setUseSSML(self, value):
        """
        Args:
            useSSML: whether to interpret the provided text input as SSML (Speech Synthesis Markup Language). The default value is false.
        """
    def setUseSSMLCol(self, value):
        """
        Args:
            useSSML: whether to interpret the provided text input as SSML (Speech Synthesis Markup Language). The default value is false.
        """
    def setVoiceName(self, value):
        """
        Args:
            voiceName: The name of the voice used for synthesis
        """
    def setVoiceNameCol(self, value):
        """
        Args:
            voiceName: The name of the voice used for synthesis
        """
    def getErrorCol(self):
        """
        Returns:
            errorCol: column to hold http errors
        """
    def getLanguage(self):
        """
        Returns:
            language: The name of the language used for synthesis
        """
    def getLocale(self):
        """
        Returns:
            locale: The locale of the input text
        """
    def getOutputFileCol(self):
        """
        Returns:
            outputFileCol: The location of the saved file as an HDFS compliant URI
        """
    def getOutputFormat(self):
        """
        Returns:
            outputFormat: The format for the output audio can be one of ArraySeq(Raw8Khz8BitMonoMULaw, Riff16Khz16KbpsMonoSiren, Audio16Khz16KbpsMonoSiren, Audio16Khz32KBitRateMonoMp3, Audio16Khz128KBitRateMonoMp3, Audio16Khz64KBitRateMonoMp3, Audio24Khz48KBitRateMonoMp3, Audio24Khz96KBitRateMonoMp3, Audio24Khz160KBitRateMonoMp3, Raw16Khz16BitMonoTrueSilk, Riff16Khz16BitMonoPcm, Riff8Khz16BitMonoPcm, Riff24Khz16BitMonoPcm, Riff8Khz8BitMonoMULaw, Raw16Khz16BitMonoPcm, Raw24Khz16BitMonoPcm, Raw8Khz16BitMonoPcm, Ogg16Khz16BitMonoOpus, Ogg24Khz16BitMonoOpus, Raw48Khz16BitMonoPcm, Riff48Khz16BitMonoPcm, Audio48Khz96KBitRateMonoMp3, Audio48Khz192KBitRateMonoMp3, Ogg48Khz16BitMonoOpus, Webm16Khz16BitMonoOpus, Webm24Khz16BitMonoOpus, Raw24Khz16BitMonoTrueSilk, Raw8Khz8BitMonoALaw, Riff8Khz8BitMonoALaw, Webm24Khz16Bit24KbpsMonoOpus, Audio16Khz16Bit32KbpsMonoOpus, Audio24Khz16Bit48KbpsMonoOpus, Audio24Khz16Bit24KbpsMonoOpus, Raw22050Hz16BitMonoPcm, Riff22050Hz16BitMonoPcm, Raw44100Hz16BitMonoPcm, Riff44100Hz16BitMonoPcm, AmrWb16000Hz)
        """
    def getSubscriptionKey(self):
        """
        Returns:
            subscriptionKey: the API key to use
        """
    def getText(self):
        """
        Returns:
            text: The text to synthesize
        """
    def getUrl(self):
        """
        Returns:
            url: Url of the service
        """
    def getUseSSML(self):
        """
        Returns:
            useSSML: whether to interpret the provided text input as SSML (Speech Synthesis Markup Language). The default value is false.
        """
    def getVoiceName(self):
        """
        Returns:
            voiceName: The name of the voice used for synthesis
        """
    def setLocation(self, value): ...
    def setLinkedService(self, value): ...
