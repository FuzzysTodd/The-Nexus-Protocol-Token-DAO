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

class Translate(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        allowFallback (object): Specifies that the service is allowed to fall back to a general system when a custom system does not exist. 
        category (object): A string specifying the category (domain) of the translation. This parameter is used to get translations from a customized system built with Custom Translator. Add the Category ID from your Custom Translator project details to this parameter to use your deployed customized system. Default value is: general.
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        errorCol (str): column to hold http errors
        fromLanguage (object): Specifies the language of the input text. Find which languages are available to translate from by looking up supported languages using the translation scope. If the from parameter is not specified, automatic language detection is applied to determine the source language. You must use the from parameter rather than autodetection when using the dynamic dictionary feature.
        fromScript (object): Specifies the script of the input text.
        handler (object): Which strategy to use when handling requests
        includeAlignment (object): Specifies whether to include alignment projection from source text to translated text.
        includeSentenceLength (object): Specifies whether to include sentence boundaries for the input text and the translated text. 
        outputCol (str): The name of the output column
        profanityAction (object): Specifies how profanities should be treated in translations. Possible values are: NoAction (default), Marked or Deleted. 
        profanityMarker (object): Specifies how profanities should be marked in translations. Possible values are: Asterisk (default) or Tag.
        subscriptionKey (object): the API key to use
        subscriptionRegion (object): the API region to use
        suggestedFrom (object): Specifies a fallback language if the language of the input text can't be identified. Language autodetection is applied when the from parameter is omitted. If detection fails, the suggestedFrom language will be assumed.
        text (object): the string to translate
        textType (object): Defines whether the text being translated is plain text or HTML text. Any HTML needs to be a well-formed, complete element. Possible values are: plain (default) or html.
        timeout (float): number of seconds to wait before closing the connection
        toLanguage (object): Specifies the language of the output text. The target language must be one of the supported languages included in the translation scope. For example, use to=de to translate to German. It's possible to translate to multiple languages simultaneously by repeating the parameter in the query string. For example, use to=de and to=it to translate to German and Italian.
        toScript (object): Specifies the script of the translated text.
        url (str): Url of the service
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    allowFallback: Incomplete
    category: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    errorCol: Incomplete
    fromLanguage: Incomplete
    fromScript: Incomplete
    handler: Incomplete
    includeAlignment: Incomplete
    includeSentenceLength: Incomplete
    outputCol: Incomplete
    profanityAction: Incomplete
    profanityMarker: Incomplete
    subscriptionKey: Incomplete
    subscriptionRegion: Incomplete
    suggestedFrom: Incomplete
    text: Incomplete
    textType: Incomplete
    timeout: Incomplete
    toLanguage: Incomplete
    toScript: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, allowFallback: Incomplete | None = None, allowFallbackCol: Incomplete | None = None, category: Incomplete | None = None, categoryCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'Translate_8832f7e7fc9b_error', fromLanguage: Incomplete | None = None, fromLanguageCol: Incomplete | None = None, fromScript: Incomplete | None = None, fromScriptCol: Incomplete | None = None, handler: Incomplete | None = None, includeAlignment: Incomplete | None = None, includeAlignmentCol: Incomplete | None = None, includeSentenceLength: Incomplete | None = None, includeSentenceLengthCol: Incomplete | None = None, outputCol: str = 'Translate_8832f7e7fc9b_output', profanityAction: Incomplete | None = None, profanityActionCol: Incomplete | None = None, profanityMarker: Incomplete | None = None, profanityMarkerCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, subscriptionRegion: Incomplete | None = None, subscriptionRegionCol: Incomplete | None = None, suggestedFrom: Incomplete | None = None, suggestedFromCol: Incomplete | None = None, text: Incomplete | None = None, textCol: Incomplete | None = None, textType: Incomplete | None = None, textTypeCol: Incomplete | None = None, timeout: float = 60.0, toLanguage: Incomplete | None = None, toLanguageCol: Incomplete | None = None, toScript: Incomplete | None = None, toScriptCol: Incomplete | None = None, url: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, allowFallback: Incomplete | None = None, allowFallbackCol: Incomplete | None = None, category: Incomplete | None = None, categoryCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, errorCol: str = 'Translate_8832f7e7fc9b_error', fromLanguage: Incomplete | None = None, fromLanguageCol: Incomplete | None = None, fromScript: Incomplete | None = None, fromScriptCol: Incomplete | None = None, handler: Incomplete | None = None, includeAlignment: Incomplete | None = None, includeAlignmentCol: Incomplete | None = None, includeSentenceLength: Incomplete | None = None, includeSentenceLengthCol: Incomplete | None = None, outputCol: str = 'Translate_8832f7e7fc9b_output', profanityAction: Incomplete | None = None, profanityActionCol: Incomplete | None = None, profanityMarker: Incomplete | None = None, profanityMarkerCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, subscriptionRegion: Incomplete | None = None, subscriptionRegionCol: Incomplete | None = None, suggestedFrom: Incomplete | None = None, suggestedFromCol: Incomplete | None = None, text: Incomplete | None = None, textCol: Incomplete | None = None, textType: Incomplete | None = None, textTypeCol: Incomplete | None = None, timeout: float = 60.0, toLanguage: Incomplete | None = None, toLanguageCol: Incomplete | None = None, toScript: Incomplete | None = None, toScriptCol: Incomplete | None = None, url: Incomplete | None = None):
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
    def setAllowFallback(self, value):
        """
        Args:
            allowFallback: Specifies that the service is allowed to fall back to a general system when a custom system does not exist. 
        """
    def setAllowFallbackCol(self, value):
        """
        Args:
            allowFallback: Specifies that the service is allowed to fall back to a general system when a custom system does not exist. 
        """
    def setCategory(self, value):
        """
        Args:
            category: A string specifying the category (domain) of the translation. This parameter is used to get translations from a customized system built with Custom Translator. Add the Category ID from your Custom Translator project details to this parameter to use your deployed customized system. Default value is: general.
        """
    def setCategoryCol(self, value):
        """
        Args:
            category: A string specifying the category (domain) of the translation. This parameter is used to get translations from a customized system built with Custom Translator. Add the Category ID from your Custom Translator project details to this parameter to use your deployed customized system. Default value is: general.
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
    def setFromLanguage(self, value):
        """
        Args:
            fromLanguage: Specifies the language of the input text. Find which languages are available to translate from by looking up supported languages using the translation scope. If the from parameter is not specified, automatic language detection is applied to determine the source language. You must use the from parameter rather than autodetection when using the dynamic dictionary feature.
        """
    def setFromLanguageCol(self, value):
        """
        Args:
            fromLanguage: Specifies the language of the input text. Find which languages are available to translate from by looking up supported languages using the translation scope. If the from parameter is not specified, automatic language detection is applied to determine the source language. You must use the from parameter rather than autodetection when using the dynamic dictionary feature.
        """
    def setFromScript(self, value):
        """
        Args:
            fromScript: Specifies the script of the input text.
        """
    def setFromScriptCol(self, value):
        """
        Args:
            fromScript: Specifies the script of the input text.
        """
    def setHandler(self, value):
        """
        Args:
            handler: Which strategy to use when handling requests
        """
    def setIncludeAlignment(self, value):
        """
        Args:
            includeAlignment: Specifies whether to include alignment projection from source text to translated text.
        """
    def setIncludeAlignmentCol(self, value):
        """
        Args:
            includeAlignment: Specifies whether to include alignment projection from source text to translated text.
        """
    def setIncludeSentenceLength(self, value):
        """
        Args:
            includeSentenceLength: Specifies whether to include sentence boundaries for the input text and the translated text. 
        """
    def setIncludeSentenceLengthCol(self, value):
        """
        Args:
            includeSentenceLength: Specifies whether to include sentence boundaries for the input text and the translated text. 
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setProfanityAction(self, value):
        """
        Args:
            profanityAction: Specifies how profanities should be treated in translations. Possible values are: NoAction (default), Marked or Deleted. 
        """
    def setProfanityActionCol(self, value):
        """
        Args:
            profanityAction: Specifies how profanities should be treated in translations. Possible values are: NoAction (default), Marked or Deleted. 
        """
    def setProfanityMarker(self, value):
        """
        Args:
            profanityMarker: Specifies how profanities should be marked in translations. Possible values are: Asterisk (default) or Tag.
        """
    def setProfanityMarkerCol(self, value):
        """
        Args:
            profanityMarker: Specifies how profanities should be marked in translations. Possible values are: Asterisk (default) or Tag.
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
    def setSubscriptionRegion(self, value):
        """
        Args:
            subscriptionRegion: the API region to use
        """
    def setSubscriptionRegionCol(self, value):
        """
        Args:
            subscriptionRegion: the API region to use
        """
    def setSuggestedFrom(self, value):
        """
        Args:
            suggestedFrom: Specifies a fallback language if the language of the input text can't be identified. Language autodetection is applied when the from parameter is omitted. If detection fails, the suggestedFrom language will be assumed.
        """
    def setSuggestedFromCol(self, value):
        """
        Args:
            suggestedFrom: Specifies a fallback language if the language of the input text can't be identified. Language autodetection is applied when the from parameter is omitted. If detection fails, the suggestedFrom language will be assumed.
        """
    def setText(self, value):
        """
        Args:
            text: the string to translate
        """
    def setTextCol(self, value):
        """
        Args:
            text: the string to translate
        """
    def setTextType(self, value):
        """
        Args:
            textType: Defines whether the text being translated is plain text or HTML text. Any HTML needs to be a well-formed, complete element. Possible values are: plain (default) or html.
        """
    def setTextTypeCol(self, value):
        """
        Args:
            textType: Defines whether the text being translated is plain text or HTML text. Any HTML needs to be a well-formed, complete element. Possible values are: plain (default) or html.
        """
    def setTimeout(self, value):
        """
        Args:
            timeout: number of seconds to wait before closing the connection
        """
    def setToLanguage(self, value):
        """
        Args:
            toLanguage: Specifies the language of the output text. The target language must be one of the supported languages included in the translation scope. For example, use to=de to translate to German. It's possible to translate to multiple languages simultaneously by repeating the parameter in the query string. For example, use to=de and to=it to translate to German and Italian.
        """
    def setToLanguageCol(self, value):
        """
        Args:
            toLanguage: Specifies the language of the output text. The target language must be one of the supported languages included in the translation scope. For example, use to=de to translate to German. It's possible to translate to multiple languages simultaneously by repeating the parameter in the query string. For example, use to=de and to=it to translate to German and Italian.
        """
    def setToScript(self, value):
        """
        Args:
            toScript: Specifies the script of the translated text.
        """
    def setToScriptCol(self, value):
        """
        Args:
            toScript: Specifies the script of the translated text.
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
    def getAllowFallback(self):
        """
        Returns:
            allowFallback: Specifies that the service is allowed to fall back to a general system when a custom system does not exist. 
        """
    def getCategory(self):
        """
        Returns:
            category: A string specifying the category (domain) of the translation. This parameter is used to get translations from a customized system built with Custom Translator. Add the Category ID from your Custom Translator project details to this parameter to use your deployed customized system. Default value is: general.
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
    def getFromLanguage(self):
        """
        Returns:
            fromLanguage: Specifies the language of the input text. Find which languages are available to translate from by looking up supported languages using the translation scope. If the from parameter is not specified, automatic language detection is applied to determine the source language. You must use the from parameter rather than autodetection when using the dynamic dictionary feature.
        """
    def getFromScript(self):
        """
        Returns:
            fromScript: Specifies the script of the input text.
        """
    def getHandler(self):
        """
        Returns:
            handler: Which strategy to use when handling requests
        """
    def getIncludeAlignment(self):
        """
        Returns:
            includeAlignment: Specifies whether to include alignment projection from source text to translated text.
        """
    def getIncludeSentenceLength(self):
        """
        Returns:
            includeSentenceLength: Specifies whether to include sentence boundaries for the input text and the translated text. 
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getProfanityAction(self):
        """
        Returns:
            profanityAction: Specifies how profanities should be treated in translations. Possible values are: NoAction (default), Marked or Deleted. 
        """
    def getProfanityMarker(self):
        """
        Returns:
            profanityMarker: Specifies how profanities should be marked in translations. Possible values are: Asterisk (default) or Tag.
        """
    def getSubscriptionKey(self):
        """
        Returns:
            subscriptionKey: the API key to use
        """
    def getSubscriptionRegion(self):
        """
        Returns:
            subscriptionRegion: the API region to use
        """
    def getSuggestedFrom(self):
        """
        Returns:
            suggestedFrom: Specifies a fallback language if the language of the input text can't be identified. Language autodetection is applied when the from parameter is omitted. If detection fails, the suggestedFrom language will be assumed.
        """
    def getText(self):
        """
        Returns:
            text: the string to translate
        """
    def getTextType(self):
        """
        Returns:
            textType: Defines whether the text being translated is plain text or HTML text. Any HTML needs to be a well-formed, complete element. Possible values are: plain (default) or html.
        """
    def getTimeout(self):
        """
        Returns:
            timeout: number of seconds to wait before closing the connection
        """
    def getToLanguage(self):
        """
        Returns:
            toLanguage: Specifies the language of the output text. The target language must be one of the supported languages included in the translation scope. For example, use to=de to translate to German. It's possible to translate to multiple languages simultaneously by repeating the parameter in the query string. For example, use to=de and to=it to translate to German and Italian.
        """
    def getToScript(self):
        """
        Returns:
            toScript: Specifies the script of the translated text.
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
