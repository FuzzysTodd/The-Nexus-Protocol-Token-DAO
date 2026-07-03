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

class OpenAIPrompt(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        apiVersion (object): version of the api
        bestOf (object): How many generations to create server side, and display only the best. Will not stream intermediate progress if best_of > 1. Has maximum value of 128.
        cacheLevel (object): can be used to disable any server-side caching, 0=no cache, 1=prompt prefix enabled, 2=full cache
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        deploymentName (object): The name of the deployment
        dropPrompt (bool): whether to drop the column of prompts after templating
        echo (object): Echo back the prompt in addition to the completion
        errorCol (str): column to hold http errors
        frequencyPenalty (object): How much to penalize new tokens based on whether they appear in the text so far. Increases the likelihood of the model to talk about new topics.
        logProbs (object): Include the log probabilities on the `logprobs` most likely tokens, as well the chosen tokens. So for example, if `logprobs` is 10, the API will return a list of the 10 most likely tokens. If `logprobs` is 0, only the chosen tokens will have logprobs returned. Minimum of 0 and maximum of 100 allowed.
        maxTokens (object): The maximum number of tokens to generate. Has minimum of 0.
        n (object): How many snippets to generate for each prompt. Minimum of 1 and maximum of 128 allowed.
        outputCol (str): The name of the output column
        postProcessing (str): Post processing options: csv, json, regex
        postProcessingOptions (dict): Options (default): delimiter=',', jsonSchema, regex, regexGroup=0
        presencePenalty (object): How much to penalize new tokens based on their existing frequency in the text so far. Decreases the likelihood of the model to repeat the same line verbatim. Has minimum of -2 and maximum of 2.
        promptTemplate (str): The prompt. supports string interpolation {col1}: {col2}.
        stop (object): A sequence which indicates the end of the current document.
        subscriptionKey (object): the API key to use
        temperature (object): What sampling temperature to use. Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer. We generally recommend using this or `top_p` but not both. Minimum of 0 and maximum of 2 allowed.
        timeout (float): number of seconds to wait before closing the connection
        topP (object): An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10 percent probability mass are considered. We generally recommend using this or `temperature` but not both. Minimum of 0 and maximum of 1 allowed.
        url (str): Url of the service
        user (object): The ID of the end-user, for use in tracking and rate-limiting.
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    apiVersion: Incomplete
    bestOf: Incomplete
    cacheLevel: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    deploymentName: Incomplete
    dropPrompt: Incomplete
    echo: Incomplete
    errorCol: Incomplete
    frequencyPenalty: Incomplete
    logProbs: Incomplete
    maxTokens: Incomplete
    n: Incomplete
    outputCol: Incomplete
    postProcessing: Incomplete
    postProcessingOptions: Incomplete
    presencePenalty: Incomplete
    promptTemplate: Incomplete
    stop: Incomplete
    subscriptionKey: Incomplete
    temperature: Incomplete
    timeout: Incomplete
    topP: Incomplete
    url: Incomplete
    user: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, apiVersion: Incomplete | None = None, apiVersionCol: Incomplete | None = None, bestOf: Incomplete | None = None, bestOfCol: Incomplete | None = None, cacheLevel: Incomplete | None = None, cacheLevelCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, deploymentName: Incomplete | None = None, deploymentNameCol: Incomplete | None = None, dropPrompt: bool = True, echo: Incomplete | None = None, echoCol: Incomplete | None = None, errorCol: str = 'OpenAIPrompt_bf546f3ae031_error', frequencyPenalty: Incomplete | None = None, frequencyPenaltyCol: Incomplete | None = None, logProbs: Incomplete | None = None, logProbsCol: Incomplete | None = None, maxTokens: Incomplete | None = None, maxTokensCol: Incomplete | None = None, n: Incomplete | None = None, nCol: Incomplete | None = None, outputCol: str = 'OpenAIPrompt_bf546f3ae031_output', postProcessing: str = '', postProcessingOptions={}, presencePenalty: Incomplete | None = None, presencePenaltyCol: Incomplete | None = None, promptTemplate: Incomplete | None = None, stop: Incomplete | None = None, stopCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, temperature: Incomplete | None = None, temperatureCol: Incomplete | None = None, timeout: float = 60.0, topP: Incomplete | None = None, topPCol: Incomplete | None = None, url: Incomplete | None = None, user: Incomplete | None = None, userCol: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, apiVersion: Incomplete | None = None, apiVersionCol: Incomplete | None = None, bestOf: Incomplete | None = None, bestOfCol: Incomplete | None = None, cacheLevel: Incomplete | None = None, cacheLevelCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, deploymentName: Incomplete | None = None, deploymentNameCol: Incomplete | None = None, dropPrompt: bool = True, echo: Incomplete | None = None, echoCol: Incomplete | None = None, errorCol: str = 'OpenAIPrompt_bf546f3ae031_error', frequencyPenalty: Incomplete | None = None, frequencyPenaltyCol: Incomplete | None = None, logProbs: Incomplete | None = None, logProbsCol: Incomplete | None = None, maxTokens: Incomplete | None = None, maxTokensCol: Incomplete | None = None, n: Incomplete | None = None, nCol: Incomplete | None = None, outputCol: str = 'OpenAIPrompt_bf546f3ae031_output', postProcessing: str = '', postProcessingOptions={}, presencePenalty: Incomplete | None = None, presencePenaltyCol: Incomplete | None = None, promptTemplate: Incomplete | None = None, stop: Incomplete | None = None, stopCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, temperature: Incomplete | None = None, temperatureCol: Incomplete | None = None, timeout: float = 60.0, topP: Incomplete | None = None, topPCol: Incomplete | None = None, url: Incomplete | None = None, user: Incomplete | None = None, userCol: Incomplete | None = None):
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
    def setApiVersion(self, value):
        """
        Args:
            apiVersion: version of the api
        """
    def setApiVersionCol(self, value):
        """
        Args:
            apiVersion: version of the api
        """
    def setBestOf(self, value):
        """
        Args:
            bestOf: How many generations to create server side, and display only the best. Will not stream intermediate progress if best_of > 1. Has maximum value of 128.
        """
    def setBestOfCol(self, value):
        """
        Args:
            bestOf: How many generations to create server side, and display only the best. Will not stream intermediate progress if best_of > 1. Has maximum value of 128.
        """
    def setCacheLevel(self, value):
        """
        Args:
            cacheLevel: can be used to disable any server-side caching, 0=no cache, 1=prompt prefix enabled, 2=full cache
        """
    def setCacheLevelCol(self, value):
        """
        Args:
            cacheLevel: can be used to disable any server-side caching, 0=no cache, 1=prompt prefix enabled, 2=full cache
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
    def setDeploymentName(self, value):
        """
        Args:
            deploymentName: The name of the deployment
        """
    def setDeploymentNameCol(self, value):
        """
        Args:
            deploymentName: The name of the deployment
        """
    def setDropPrompt(self, value):
        """
        Args:
            dropPrompt: whether to drop the column of prompts after templating
        """
    def setEcho(self, value):
        """
        Args:
            echo: Echo back the prompt in addition to the completion
        """
    def setEchoCol(self, value):
        """
        Args:
            echo: Echo back the prompt in addition to the completion
        """
    def setErrorCol(self, value):
        """
        Args:
            errorCol: column to hold http errors
        """
    def setFrequencyPenalty(self, value):
        """
        Args:
            frequencyPenalty: How much to penalize new tokens based on whether they appear in the text so far. Increases the likelihood of the model to talk about new topics.
        """
    def setFrequencyPenaltyCol(self, value):
        """
        Args:
            frequencyPenalty: How much to penalize new tokens based on whether they appear in the text so far. Increases the likelihood of the model to talk about new topics.
        """
    def setLogProbs(self, value):
        """
        Args:
            logProbs: Include the log probabilities on the `logprobs` most likely tokens, as well the chosen tokens. So for example, if `logprobs` is 10, the API will return a list of the 10 most likely tokens. If `logprobs` is 0, only the chosen tokens will have logprobs returned. Minimum of 0 and maximum of 100 allowed.
        """
    def setLogProbsCol(self, value):
        """
        Args:
            logProbs: Include the log probabilities on the `logprobs` most likely tokens, as well the chosen tokens. So for example, if `logprobs` is 10, the API will return a list of the 10 most likely tokens. If `logprobs` is 0, only the chosen tokens will have logprobs returned. Minimum of 0 and maximum of 100 allowed.
        """
    def setMaxTokens(self, value):
        """
        Args:
            maxTokens: The maximum number of tokens to generate. Has minimum of 0.
        """
    def setMaxTokensCol(self, value):
        """
        Args:
            maxTokens: The maximum number of tokens to generate. Has minimum of 0.
        """
    def setN(self, value):
        """
        Args:
            n: How many snippets to generate for each prompt. Minimum of 1 and maximum of 128 allowed.
        """
    def setNCol(self, value):
        """
        Args:
            n: How many snippets to generate for each prompt. Minimum of 1 and maximum of 128 allowed.
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setPostProcessing(self, value):
        """
        Args:
            postProcessing: Post processing options: csv, json, regex
        """
    def setPostProcessingOptions(self, value):
        """
        Args:
            postProcessingOptions: Options (default): delimiter=',', jsonSchema, regex, regexGroup=0
        """
    def setPresencePenalty(self, value):
        """
        Args:
            presencePenalty: How much to penalize new tokens based on their existing frequency in the text so far. Decreases the likelihood of the model to repeat the same line verbatim. Has minimum of -2 and maximum of 2.
        """
    def setPresencePenaltyCol(self, value):
        """
        Args:
            presencePenalty: How much to penalize new tokens based on their existing frequency in the text so far. Decreases the likelihood of the model to repeat the same line verbatim. Has minimum of -2 and maximum of 2.
        """
    def setPromptTemplate(self, value):
        """
        Args:
            promptTemplate: The prompt. supports string interpolation {col1}: {col2}.
        """
    def setStop(self, value):
        """
        Args:
            stop: A sequence which indicates the end of the current document.
        """
    def setStopCol(self, value):
        """
        Args:
            stop: A sequence which indicates the end of the current document.
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
    def setTemperature(self, value):
        """
        Args:
            temperature: What sampling temperature to use. Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer. We generally recommend using this or `top_p` but not both. Minimum of 0 and maximum of 2 allowed.
        """
    def setTemperatureCol(self, value):
        """
        Args:
            temperature: What sampling temperature to use. Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer. We generally recommend using this or `top_p` but not both. Minimum of 0 and maximum of 2 allowed.
        """
    def setTimeout(self, value):
        """
        Args:
            timeout: number of seconds to wait before closing the connection
        """
    def setTopP(self, value):
        """
        Args:
            topP: An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10 percent probability mass are considered. We generally recommend using this or `temperature` but not both. Minimum of 0 and maximum of 1 allowed.
        """
    def setTopPCol(self, value):
        """
        Args:
            topP: An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10 percent probability mass are considered. We generally recommend using this or `temperature` but not both. Minimum of 0 and maximum of 1 allowed.
        """
    def setUrl(self, value):
        """
        Args:
            url: Url of the service
        """
    def setUser(self, value):
        """
        Args:
            user: The ID of the end-user, for use in tracking and rate-limiting.
        """
    def setUserCol(self, value):
        """
        Args:
            user: The ID of the end-user, for use in tracking and rate-limiting.
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
    def getApiVersion(self):
        """
        Returns:
            apiVersion: version of the api
        """
    def getBestOf(self):
        """
        Returns:
            bestOf: How many generations to create server side, and display only the best. Will not stream intermediate progress if best_of > 1. Has maximum value of 128.
        """
    def getCacheLevel(self):
        """
        Returns:
            cacheLevel: can be used to disable any server-side caching, 0=no cache, 1=prompt prefix enabled, 2=full cache
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
    def getDeploymentName(self):
        """
        Returns:
            deploymentName: The name of the deployment
        """
    def getDropPrompt(self):
        """
        Returns:
            dropPrompt: whether to drop the column of prompts after templating
        """
    def getEcho(self):
        """
        Returns:
            echo: Echo back the prompt in addition to the completion
        """
    def getErrorCol(self):
        """
        Returns:
            errorCol: column to hold http errors
        """
    def getFrequencyPenalty(self):
        """
        Returns:
            frequencyPenalty: How much to penalize new tokens based on whether they appear in the text so far. Increases the likelihood of the model to talk about new topics.
        """
    def getLogProbs(self):
        """
        Returns:
            logProbs: Include the log probabilities on the `logprobs` most likely tokens, as well the chosen tokens. So for example, if `logprobs` is 10, the API will return a list of the 10 most likely tokens. If `logprobs` is 0, only the chosen tokens will have logprobs returned. Minimum of 0 and maximum of 100 allowed.
        """
    def getMaxTokens(self):
        """
        Returns:
            maxTokens: The maximum number of tokens to generate. Has minimum of 0.
        """
    def getN(self):
        """
        Returns:
            n: How many snippets to generate for each prompt. Minimum of 1 and maximum of 128 allowed.
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getPostProcessing(self):
        """
        Returns:
            postProcessing: Post processing options: csv, json, regex
        """
    def getPostProcessingOptions(self):
        """
        Returns:
            postProcessingOptions: Options (default): delimiter=',', jsonSchema, regex, regexGroup=0
        """
    def getPresencePenalty(self):
        """
        Returns:
            presencePenalty: How much to penalize new tokens based on their existing frequency in the text so far. Decreases the likelihood of the model to repeat the same line verbatim. Has minimum of -2 and maximum of 2.
        """
    def getPromptTemplate(self):
        """
        Returns:
            promptTemplate: The prompt. supports string interpolation {col1}: {col2}.
        """
    def getStop(self):
        """
        Returns:
            stop: A sequence which indicates the end of the current document.
        """
    def getSubscriptionKey(self):
        """
        Returns:
            subscriptionKey: the API key to use
        """
    def getTemperature(self):
        """
        Returns:
            temperature: What sampling temperature to use. Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer. We generally recommend using this or `top_p` but not both. Minimum of 0 and maximum of 2 allowed.
        """
    def getTimeout(self):
        """
        Returns:
            timeout: number of seconds to wait before closing the connection
        """
    def getTopP(self):
        """
        Returns:
            topP: An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10 percent probability mass are considered. We generally recommend using this or `temperature` but not both. Minimum of 0 and maximum of 1 allowed.
        """
    def getUrl(self):
        """
        Returns:
            url: Url of the service
        """
    def getUser(self):
        """
        Returns:
            user: The ID of the end-user, for use in tracking and rate-limiting.
        """
    def setCustomServiceName(self, value): ...
    def setEndpoint(self, value): ...
    def setDefaultInternalEndpoint(self, value): ...
