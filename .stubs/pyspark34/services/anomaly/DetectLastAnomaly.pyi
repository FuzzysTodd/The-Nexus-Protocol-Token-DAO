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

class DetectLastAnomaly(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    '''
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        customInterval (object):  Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.     
        errorCol (str): column to hold http errors
        granularity (object):  Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.     
        handler (object): Which strategy to use when handling requests
        imputeFixedValue (object):  Optional argument, fixed value to use when imputeMode is set to "fixed"     
        imputeMode (object):  Optional argument, impute mode of a time series. Possible values: auto, previous, linear, fixed, zero, notFill     
        maxAnomalyRatio (object):  Optional argument, advanced model parameter, max anomaly ratio in a time series.     
        outputCol (str): The name of the output column
        period (object):  Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.     
        sensitivity (object):  Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted     
        series (object):  Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.     
        subscriptionKey (object): the API key to use
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
    '''
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    customInterval: Incomplete
    errorCol: Incomplete
    granularity: Incomplete
    handler: Incomplete
    imputeFixedValue: Incomplete
    imputeMode: Incomplete
    maxAnomalyRatio: Incomplete
    outputCol: Incomplete
    period: Incomplete
    sensitivity: Incomplete
    series: Incomplete
    subscriptionKey: Incomplete
    timeout: Incomplete
    url: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, customInterval: Incomplete | None = None, customIntervalCol: Incomplete | None = None, errorCol: str = 'DetectLastAnomaly_f58d45bf5cd9_error', granularity: Incomplete | None = None, granularityCol: Incomplete | None = None, handler: Incomplete | None = None, imputeFixedValue: Incomplete | None = None, imputeFixedValueCol: Incomplete | None = None, imputeMode: Incomplete | None = None, imputeModeCol: Incomplete | None = None, maxAnomalyRatio: Incomplete | None = None, maxAnomalyRatioCol: Incomplete | None = None, outputCol: str = 'DetectLastAnomaly_f58d45bf5cd9_output', period: Incomplete | None = None, periodCol: Incomplete | None = None, sensitivity: Incomplete | None = None, sensitivityCol: Incomplete | None = None, series: Incomplete | None = None, seriesCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, customInterval: Incomplete | None = None, customIntervalCol: Incomplete | None = None, errorCol: str = 'DetectLastAnomaly_f58d45bf5cd9_error', granularity: Incomplete | None = None, granularityCol: Incomplete | None = None, handler: Incomplete | None = None, imputeFixedValue: Incomplete | None = None, imputeFixedValueCol: Incomplete | None = None, imputeMode: Incomplete | None = None, imputeModeCol: Incomplete | None = None, maxAnomalyRatio: Incomplete | None = None, maxAnomalyRatioCol: Incomplete | None = None, outputCol: str = 'DetectLastAnomaly_f58d45bf5cd9_output', period: Incomplete | None = None, periodCol: Incomplete | None = None, sensitivity: Incomplete | None = None, sensitivityCol: Incomplete | None = None, series: Incomplete | None = None, seriesCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: Incomplete | None = None):
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
    def setCustomInterval(self, value):
        """
        Args:
            customInterval:  Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.     
        """
    def setCustomIntervalCol(self, value):
        """
        Args:
            customInterval:  Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.     
        """
    def setErrorCol(self, value):
        """
        Args:
            errorCol: column to hold http errors
        """
    def setGranularity(self, value):
        """
        Args:
            granularity:  Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.     
        """
    def setGranularityCol(self, value):
        """
        Args:
            granularity:  Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.     
        """
    def setHandler(self, value):
        """
        Args:
            handler: Which strategy to use when handling requests
        """
    def setImputeFixedValue(self, value):
        '''
        Args:
            imputeFixedValue:  Optional argument, fixed value to use when imputeMode is set to "fixed"     
        '''
    def setImputeFixedValueCol(self, value):
        '''
        Args:
            imputeFixedValue:  Optional argument, fixed value to use when imputeMode is set to "fixed"     
        '''
    def setImputeMode(self, value):
        """
        Args:
            imputeMode:  Optional argument, impute mode of a time series. Possible values: auto, previous, linear, fixed, zero, notFill     
        """
    def setImputeModeCol(self, value):
        """
        Args:
            imputeMode:  Optional argument, impute mode of a time series. Possible values: auto, previous, linear, fixed, zero, notFill     
        """
    def setMaxAnomalyRatio(self, value):
        """
        Args:
            maxAnomalyRatio:  Optional argument, advanced model parameter, max anomaly ratio in a time series.     
        """
    def setMaxAnomalyRatioCol(self, value):
        """
        Args:
            maxAnomalyRatio:  Optional argument, advanced model parameter, max anomaly ratio in a time series.     
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setPeriod(self, value):
        """
        Args:
            period:  Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.     
        """
    def setPeriodCol(self, value):
        """
        Args:
            period:  Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.     
        """
    def setSensitivity(self, value):
        """
        Args:
            sensitivity:  Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted     
        """
    def setSensitivityCol(self, value):
        """
        Args:
            sensitivity:  Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted     
        """
    def setSeries(self, value):
        """
        Args:
            series:  Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.     
        """
    def setSeriesCol(self, value):
        """
        Args:
            series:  Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.     
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
    def getCustomInterval(self):
        """
        Returns:
            customInterval:  Custom Interval is used to set non-standard time interval, for example, if the series is 5 minutes,  request can be set as granularity=minutely, customInterval=5.     
        """
    def getErrorCol(self):
        """
        Returns:
            errorCol: column to hold http errors
        """
    def getGranularity(self):
        """
        Returns:
            granularity:  Can only be one of yearly, monthly, weekly, daily, hourly or minutely. Granularity is used for verify whether input series is valid.     
        """
    def getHandler(self):
        """
        Returns:
            handler: Which strategy to use when handling requests
        """
    def getImputeFixedValue(self):
        '''
        Returns:
            imputeFixedValue:  Optional argument, fixed value to use when imputeMode is set to "fixed"     
        '''
    def getImputeMode(self):
        """
        Returns:
            imputeMode:  Optional argument, impute mode of a time series. Possible values: auto, previous, linear, fixed, zero, notFill     
        """
    def getMaxAnomalyRatio(self):
        """
        Returns:
            maxAnomalyRatio:  Optional argument, advanced model parameter, max anomaly ratio in a time series.     
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getPeriod(self):
        """
        Returns:
            period:  Optional argument, periodic value of a time series. If the value is null or does not present, the API will determine the period automatically.     
        """
    def getSensitivity(self):
        """
        Returns:
            sensitivity:  Optional argument, advanced model parameter, between 0-99, the lower the value is, the larger the margin value will be which means less anomalies will be accepted     
        """
    def getSeries(self):
        """
        Returns:
            series:  Time series data points. Points should be sorted by timestamp in ascending order to match the anomaly detection result. If the data is not sorted correctly or there is duplicated timestamp, the API will not work. In such case, an error message will be returned.     
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
