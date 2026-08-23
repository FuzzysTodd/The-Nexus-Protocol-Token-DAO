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

class _BingImageSearch(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """
    Args:
        AADToken (object): AAD Token used for authentication
        CustomAuthHeader (object): A Custom Value for Authorization Header
        aspect (object): Filter images by the following aspect ratios: Square: Return images with standard aspect ratioWide: Return images with wide screen aspect ratioTall: Return images with tall aspect ratioAll: Do not filter by aspect. Specifying this value is the same as not specifying the aspect parameter.
        color (object): Filter images by the following color options:ColorOnly: Return color imagesMonochrome: Return black and white imagesReturn images with one of the following dominant colors:Black,Blue,Brown,Gray,Green,Orange,Pink,Purple,Red,Teal,White,Yellow
        concurrency (int): max number of concurrent calls
        concurrentTimeout (float): max number seconds to wait on futures if concurrency >= 1
        count (object): The number of image results to return in the response. The actual number delivered may be less than requested.
        errorCol (str): column to hold http errors
        freshness (object): Filter images by the following discovery options:Day: Return images discovered by Bing within the last 24 hoursWeek: Return images discovered by Bing within the last 7 daysMonth: Return images discovered by Bing within the last 30 daysYear: Return images discovered within the last year2017-06-15..2018-06-15: Return images discovered within the specified range of dates
        handler (object): Which strategy to use when handling requests
        height (object): Filter images that have the specified height, in pixels.You may use this filter with the size filter to return small images that have a height of 150 pixels.
        imageContent (object): Filter images by the following content types:Face: Return images that show only a person's facePortrait: Return images that show only a person's head and shoulders
        imageType (object): Filter images by the following image types:AnimatedGif: return animated gif imagesAnimatedGifHttps: return animated gif images that are from an https addressClipart: Return only clip art imagesLine: Return only line drawingsPhoto: Return only photographs (excluding line drawings, animated Gifs, and clip art)Shopping: Return only images that contain items where Bing knows of a merchant that is selling the items. This option is valid in the en-US market only. Transparent: Return only images with a transparent background.
        license (object): Filter images by the following license types:Any: Return images that are under any license type. The response doesn't include images that do not specify a license or the license is unknown.Public: Return images where the creator has waived their exclusive rights, to the fullest extent allowed by law.Share: Return images that may be shared with others. Changing or editing the image might not be allowed. Also, modifying, sharing, and using the image for commercial purposes might not be allowed. Typically, this option returns the most images.ShareCommercially: Return images that may be shared with others for personal or commercial purposes. Changing or editing the image might not be allowed.Modify: Return images that may be modified, shared, and used. Changing or editing the image might not be allowed. Modifying, sharing, and using the image for commercial purposes might not be allowed. ModifyCommercially: Return images that may be modified, shared, and used for personal or commercial purposes. Typically, this option returns the fewest images.All: Do not filter by license type. Specifying this value is the same as not specifying the license parameter. For more information about these license types, see Filter Images By License Type.
        maxFileSize (object): Filter images that are less than or equal to the specified file size.The maximum file size that you may specify is 520,192 bytes. If you specify a larger value, the API uses 520,192. It is possible that the response may include images that are slightly larger than the specified maximum.You may specify this filter and minFileSize to filter images within a range of file sizes.
        maxHeight (object): Filter images that have a height that is less than or equal to the specified height. Specify the height in pixels.You may specify this filter and minHeight to filter images within a range of heights. This filter and the height filter are mutually exclusive.
        maxWidth (object): Filter images that have a width that is less than or equal to the specified width. Specify the width in pixels.You may specify this filter and maxWidth to filter images within a range of widths. This filter and the width filter are mutually exclusive.
        minFileSize (object): Filter images that are greater than or equal to the specified file size. The maximum file size that you may specify is 520,192 bytes. If you specify a larger value, the API uses 520,192. It is possible that the response may include images that are slightly smaller than the specified minimum. You may specify this filter and maxFileSize to filter images within a range of file sizes.
        minHeight (object): Filter images that have a height that is greater than or equal to the specified height. Specify the height in pixels.You may specify this filter and maxHeight to filter images within a range of heights. This filter and the height filter are mutually exclusive.
        minWidth (object): Filter images that have a width that is greater than or equal to the specified width. Specify the width in pixels. You may specify this filter and maxWidth to filter images within a range of widths. This filter and the width filter are mutually exclusive.
        mkt (object): The market where the results come from. Typically, this is the country where the user is making the request from; however, it could be a different country if the user is not located in a country where Bing delivers results. The market must be in the form -. For example, en-US. Full list of supported markets: es-AR,en-AU,de-AT,nl-BE,fr-BE,pt-BR,en-CA,fr-CA,es-CL,da-DK,fi-FI,fr-FR,de-DE,zh-HK,en-IN,en-ID,en-IE,it-IT,ja-JP,ko-KR,en-MY,es-MX,nl-NL,en-NZ,no-NO,zh-CN,pl-PL,pt-PT,en-PH,ru-RU,ar-SA,en-ZA,es-ES,sv-SE,fr-CH,de-CH,zh-TW,tr-TR,en-GB,en-US,es-US
        offset (object): The zero-based offset that indicates the number of image results to skip before returning results
        outputCol (str): The name of the output column
        q (object): The user's search query string
        size (object): Filter images by the following sizes:Small: Return images that are less than 200x200 pixelsMedium: Return images that are greater than or equal to 200x200 pixels but less than 500x500 pixelsLarge: Return images that are 500x500 pixels or largerWallpaper: Return wallpaper images.AllDo not filter by size. Specifying this value is the same as not specifying the size parameter.You may use this parameter along with the height or width parameters. For example, you may use height and size to request small images that are 150 pixels tall.
        subscriptionKey (object): the API key to use
        timeout (float): number of seconds to wait before closing the connection
        url (str): Url of the service
        width (object): Filter images that have the specified width, in pixels.You may use this filter with the size filter to return small images that have a width of 150 pixels.
    """
    AADToken: Incomplete
    CustomAuthHeader: Incomplete
    aspect: Incomplete
    color: Incomplete
    concurrency: Incomplete
    concurrentTimeout: Incomplete
    count: Incomplete
    errorCol: Incomplete
    freshness: Incomplete
    handler: Incomplete
    height: Incomplete
    imageContent: Incomplete
    imageType: Incomplete
    license: Incomplete
    maxFileSize: Incomplete
    maxHeight: Incomplete
    maxWidth: Incomplete
    minFileSize: Incomplete
    minHeight: Incomplete
    minWidth: Incomplete
    mkt: Incomplete
    offset: Incomplete
    outputCol: Incomplete
    q: Incomplete
    size: Incomplete
    subscriptionKey: Incomplete
    timeout: Incomplete
    url: Incomplete
    width: Incomplete
    def __init__(self, java_obj: Incomplete | None = None, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, aspect: Incomplete | None = None, aspectCol: Incomplete | None = None, color: Incomplete | None = None, colorCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, count: Incomplete | None = None, countCol: Incomplete | None = None, errorCol: str = 'BingImageSearch_1dc36d6bcd4b_error', freshness: Incomplete | None = None, freshnessCol: Incomplete | None = None, handler: Incomplete | None = None, height: Incomplete | None = None, heightCol: Incomplete | None = None, imageContent: Incomplete | None = None, imageContentCol: Incomplete | None = None, imageType: Incomplete | None = None, imageTypeCol: Incomplete | None = None, license: Incomplete | None = None, licenseCol: Incomplete | None = None, maxFileSize: Incomplete | None = None, maxFileSizeCol: Incomplete | None = None, maxHeight: Incomplete | None = None, maxHeightCol: Incomplete | None = None, maxWidth: Incomplete | None = None, maxWidthCol: Incomplete | None = None, minFileSize: Incomplete | None = None, minFileSizeCol: Incomplete | None = None, minHeight: Incomplete | None = None, minHeightCol: Incomplete | None = None, minWidth: Incomplete | None = None, minWidthCol: Incomplete | None = None, mkt: Incomplete | None = None, mktCol: Incomplete | None = None, offset: Incomplete | None = None, offsetCol: Incomplete | None = None, outputCol: str = 'BingImageSearch_1dc36d6bcd4b_output', q: Incomplete | None = None, qCol: Incomplete | None = None, size: Incomplete | None = None, sizeCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: str = 'https://api.bing.microsoft.com/v7.0/images/search', width: Incomplete | None = None, widthCol: Incomplete | None = None) -> None: ...
    def setParams(self, AADToken: Incomplete | None = None, AADTokenCol: Incomplete | None = None, CustomAuthHeader: Incomplete | None = None, CustomAuthHeaderCol: Incomplete | None = None, aspect: Incomplete | None = None, aspectCol: Incomplete | None = None, color: Incomplete | None = None, colorCol: Incomplete | None = None, concurrency: int = 1, concurrentTimeout: Incomplete | None = None, count: Incomplete | None = None, countCol: Incomplete | None = None, errorCol: str = 'BingImageSearch_1dc36d6bcd4b_error', freshness: Incomplete | None = None, freshnessCol: Incomplete | None = None, handler: Incomplete | None = None, height: Incomplete | None = None, heightCol: Incomplete | None = None, imageContent: Incomplete | None = None, imageContentCol: Incomplete | None = None, imageType: Incomplete | None = None, imageTypeCol: Incomplete | None = None, license: Incomplete | None = None, licenseCol: Incomplete | None = None, maxFileSize: Incomplete | None = None, maxFileSizeCol: Incomplete | None = None, maxHeight: Incomplete | None = None, maxHeightCol: Incomplete | None = None, maxWidth: Incomplete | None = None, maxWidthCol: Incomplete | None = None, minFileSize: Incomplete | None = None, minFileSizeCol: Incomplete | None = None, minHeight: Incomplete | None = None, minHeightCol: Incomplete | None = None, minWidth: Incomplete | None = None, minWidthCol: Incomplete | None = None, mkt: Incomplete | None = None, mktCol: Incomplete | None = None, offset: Incomplete | None = None, offsetCol: Incomplete | None = None, outputCol: str = 'BingImageSearch_1dc36d6bcd4b_output', q: Incomplete | None = None, qCol: Incomplete | None = None, size: Incomplete | None = None, sizeCol: Incomplete | None = None, subscriptionKey: Incomplete | None = None, subscriptionKeyCol: Incomplete | None = None, timeout: float = 60.0, url: str = 'https://api.bing.microsoft.com/v7.0/images/search', width: Incomplete | None = None, widthCol: Incomplete | None = None):
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
    def setAspect(self, value):
        """
        Args:
            aspect: Filter images by the following aspect ratios: Square: Return images with standard aspect ratioWide: Return images with wide screen aspect ratioTall: Return images with tall aspect ratioAll: Do not filter by aspect. Specifying this value is the same as not specifying the aspect parameter.
        """
    def setAspectCol(self, value):
        """
        Args:
            aspect: Filter images by the following aspect ratios: Square: Return images with standard aspect ratioWide: Return images with wide screen aspect ratioTall: Return images with tall aspect ratioAll: Do not filter by aspect. Specifying this value is the same as not specifying the aspect parameter.
        """
    def setColor(self, value):
        """
        Args:
            color: Filter images by the following color options:ColorOnly: Return color imagesMonochrome: Return black and white imagesReturn images with one of the following dominant colors:Black,Blue,Brown,Gray,Green,Orange,Pink,Purple,Red,Teal,White,Yellow
        """
    def setColorCol(self, value):
        """
        Args:
            color: Filter images by the following color options:ColorOnly: Return color imagesMonochrome: Return black and white imagesReturn images with one of the following dominant colors:Black,Blue,Brown,Gray,Green,Orange,Pink,Purple,Red,Teal,White,Yellow
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
    def setCount(self, value):
        """
        Args:
            count: The number of image results to return in the response. The actual number delivered may be less than requested.
        """
    def setCountCol(self, value):
        """
        Args:
            count: The number of image results to return in the response. The actual number delivered may be less than requested.
        """
    def setErrorCol(self, value):
        """
        Args:
            errorCol: column to hold http errors
        """
    def setFreshness(self, value):
        """
        Args:
            freshness: Filter images by the following discovery options:Day: Return images discovered by Bing within the last 24 hoursWeek: Return images discovered by Bing within the last 7 daysMonth: Return images discovered by Bing within the last 30 daysYear: Return images discovered within the last year2017-06-15..2018-06-15: Return images discovered within the specified range of dates
        """
    def setFreshnessCol(self, value):
        """
        Args:
            freshness: Filter images by the following discovery options:Day: Return images discovered by Bing within the last 24 hoursWeek: Return images discovered by Bing within the last 7 daysMonth: Return images discovered by Bing within the last 30 daysYear: Return images discovered within the last year2017-06-15..2018-06-15: Return images discovered within the specified range of dates
        """
    def setHandler(self, value):
        """
        Args:
            handler: Which strategy to use when handling requests
        """
    def setHeight(self, value):
        """
        Args:
            height: Filter images that have the specified height, in pixels.You may use this filter with the size filter to return small images that have a height of 150 pixels.
        """
    def setHeightCol(self, value):
        """
        Args:
            height: Filter images that have the specified height, in pixels.You may use this filter with the size filter to return small images that have a height of 150 pixels.
        """
    def setImageContent(self, value):
        """
        Args:
            imageContent: Filter images by the following content types:Face: Return images that show only a person's facePortrait: Return images that show only a person's head and shoulders
        """
    def setImageContentCol(self, value):
        """
        Args:
            imageContent: Filter images by the following content types:Face: Return images that show only a person's facePortrait: Return images that show only a person's head and shoulders
        """
    def setImageType(self, value):
        """
        Args:
            imageType: Filter images by the following image types:AnimatedGif: return animated gif imagesAnimatedGifHttps: return animated gif images that are from an https addressClipart: Return only clip art imagesLine: Return only line drawingsPhoto: Return only photographs (excluding line drawings, animated Gifs, and clip art)Shopping: Return only images that contain items where Bing knows of a merchant that is selling the items. This option is valid in the en-US market only. Transparent: Return only images with a transparent background.
        """
    def setImageTypeCol(self, value):
        """
        Args:
            imageType: Filter images by the following image types:AnimatedGif: return animated gif imagesAnimatedGifHttps: return animated gif images that are from an https addressClipart: Return only clip art imagesLine: Return only line drawingsPhoto: Return only photographs (excluding line drawings, animated Gifs, and clip art)Shopping: Return only images that contain items where Bing knows of a merchant that is selling the items. This option is valid in the en-US market only. Transparent: Return only images with a transparent background.
        """
    def setLicense(self, value):
        """
        Args:
            license: Filter images by the following license types:Any: Return images that are under any license type. The response doesn't include images that do not specify a license or the license is unknown.Public: Return images where the creator has waived their exclusive rights, to the fullest extent allowed by law.Share: Return images that may be shared with others. Changing or editing the image might not be allowed. Also, modifying, sharing, and using the image for commercial purposes might not be allowed. Typically, this option returns the most images.ShareCommercially: Return images that may be shared with others for personal or commercial purposes. Changing or editing the image might not be allowed.Modify: Return images that may be modified, shared, and used. Changing or editing the image might not be allowed. Modifying, sharing, and using the image for commercial purposes might not be allowed. ModifyCommercially: Return images that may be modified, shared, and used for personal or commercial purposes. Typically, this option returns the fewest images.All: Do not filter by license type. Specifying this value is the same as not specifying the license parameter. For more information about these license types, see Filter Images By License Type.
        """
    def setLicenseCol(self, value):
        """
        Args:
            license: Filter images by the following license types:Any: Return images that are under any license type. The response doesn't include images that do not specify a license or the license is unknown.Public: Return images where the creator has waived their exclusive rights, to the fullest extent allowed by law.Share: Return images that may be shared with others. Changing or editing the image might not be allowed. Also, modifying, sharing, and using the image for commercial purposes might not be allowed. Typically, this option returns the most images.ShareCommercially: Return images that may be shared with others for personal or commercial purposes. Changing or editing the image might not be allowed.Modify: Return images that may be modified, shared, and used. Changing or editing the image might not be allowed. Modifying, sharing, and using the image for commercial purposes might not be allowed. ModifyCommercially: Return images that may be modified, shared, and used for personal or commercial purposes. Typically, this option returns the fewest images.All: Do not filter by license type. Specifying this value is the same as not specifying the license parameter. For more information about these license types, see Filter Images By License Type.
        """
    def setMaxFileSize(self, value):
        """
        Args:
            maxFileSize: Filter images that are less than or equal to the specified file size.The maximum file size that you may specify is 520,192 bytes. If you specify a larger value, the API uses 520,192. It is possible that the response may include images that are slightly larger than the specified maximum.You may specify this filter and minFileSize to filter images within a range of file sizes.
        """
    def setMaxFileSizeCol(self, value):
        """
        Args:
            maxFileSize: Filter images that are less than or equal to the specified file size.The maximum file size that you may specify is 520,192 bytes. If you specify a larger value, the API uses 520,192. It is possible that the response may include images that are slightly larger than the specified maximum.You may specify this filter and minFileSize to filter images within a range of file sizes.
        """
    def setMaxHeight(self, value):
        """
        Args:
            maxHeight: Filter images that have a height that is less than or equal to the specified height. Specify the height in pixels.You may specify this filter and minHeight to filter images within a range of heights. This filter and the height filter are mutually exclusive.
        """
    def setMaxHeightCol(self, value):
        """
        Args:
            maxHeight: Filter images that have a height that is less than or equal to the specified height. Specify the height in pixels.You may specify this filter and minHeight to filter images within a range of heights. This filter and the height filter are mutually exclusive.
        """
    def setMaxWidth(self, value):
        """
        Args:
            maxWidth: Filter images that have a width that is less than or equal to the specified width. Specify the width in pixels.You may specify this filter and maxWidth to filter images within a range of widths. This filter and the width filter are mutually exclusive.
        """
    def setMaxWidthCol(self, value):
        """
        Args:
            maxWidth: Filter images that have a width that is less than or equal to the specified width. Specify the width in pixels.You may specify this filter and maxWidth to filter images within a range of widths. This filter and the width filter are mutually exclusive.
        """
    def setMinFileSize(self, value):
        """
        Args:
            minFileSize: Filter images that are greater than or equal to the specified file size. The maximum file size that you may specify is 520,192 bytes. If you specify a larger value, the API uses 520,192. It is possible that the response may include images that are slightly smaller than the specified minimum. You may specify this filter and maxFileSize to filter images within a range of file sizes.
        """
    def setMinFileSizeCol(self, value):
        """
        Args:
            minFileSize: Filter images that are greater than or equal to the specified file size. The maximum file size that you may specify is 520,192 bytes. If you specify a larger value, the API uses 520,192. It is possible that the response may include images that are slightly smaller than the specified minimum. You may specify this filter and maxFileSize to filter images within a range of file sizes.
        """
    def setMinHeight(self, value):
        """
        Args:
            minHeight: Filter images that have a height that is greater than or equal to the specified height. Specify the height in pixels.You may specify this filter and maxHeight to filter images within a range of heights. This filter and the height filter are mutually exclusive.
        """
    def setMinHeightCol(self, value):
        """
        Args:
            minHeight: Filter images that have a height that is greater than or equal to the specified height. Specify the height in pixels.You may specify this filter and maxHeight to filter images within a range of heights. This filter and the height filter are mutually exclusive.
        """
    def setMinWidth(self, value):
        """
        Args:
            minWidth: Filter images that have a width that is greater than or equal to the specified width. Specify the width in pixels. You may specify this filter and maxWidth to filter images within a range of widths. This filter and the width filter are mutually exclusive.
        """
    def setMinWidthCol(self, value):
        """
        Args:
            minWidth: Filter images that have a width that is greater than or equal to the specified width. Specify the width in pixels. You may specify this filter and maxWidth to filter images within a range of widths. This filter and the width filter are mutually exclusive.
        """
    def setMkt(self, value):
        """
        Args:
            mkt: The market where the results come from. Typically, this is the country where the user is making the request from; however, it could be a different country if the user is not located in a country where Bing delivers results. The market must be in the form -. For example, en-US. Full list of supported markets: es-AR,en-AU,de-AT,nl-BE,fr-BE,pt-BR,en-CA,fr-CA,es-CL,da-DK,fi-FI,fr-FR,de-DE,zh-HK,en-IN,en-ID,en-IE,it-IT,ja-JP,ko-KR,en-MY,es-MX,nl-NL,en-NZ,no-NO,zh-CN,pl-PL,pt-PT,en-PH,ru-RU,ar-SA,en-ZA,es-ES,sv-SE,fr-CH,de-CH,zh-TW,tr-TR,en-GB,en-US,es-US
        """
    def setMktCol(self, value):
        """
        Args:
            mkt: The market where the results come from. Typically, this is the country where the user is making the request from; however, it could be a different country if the user is not located in a country where Bing delivers results. The market must be in the form -. For example, en-US. Full list of supported markets: es-AR,en-AU,de-AT,nl-BE,fr-BE,pt-BR,en-CA,fr-CA,es-CL,da-DK,fi-FI,fr-FR,de-DE,zh-HK,en-IN,en-ID,en-IE,it-IT,ja-JP,ko-KR,en-MY,es-MX,nl-NL,en-NZ,no-NO,zh-CN,pl-PL,pt-PT,en-PH,ru-RU,ar-SA,en-ZA,es-ES,sv-SE,fr-CH,de-CH,zh-TW,tr-TR,en-GB,en-US,es-US
        """
    def setOffset(self, value):
        """
        Args:
            offset: The zero-based offset that indicates the number of image results to skip before returning results
        """
    def setOffsetCol(self, value):
        """
        Args:
            offset: The zero-based offset that indicates the number of image results to skip before returning results
        """
    def setOutputCol(self, value):
        """
        Args:
            outputCol: The name of the output column
        """
    def setQ(self, value):
        """
        Args:
            q: The user's search query string
        """
    def setQCol(self, value):
        """
        Args:
            q: The user's search query string
        """
    def setSize(self, value):
        """
        Args:
            size: Filter images by the following sizes:Small: Return images that are less than 200x200 pixelsMedium: Return images that are greater than or equal to 200x200 pixels but less than 500x500 pixelsLarge: Return images that are 500x500 pixels or largerWallpaper: Return wallpaper images.AllDo not filter by size. Specifying this value is the same as not specifying the size parameter.You may use this parameter along with the height or width parameters. For example, you may use height and size to request small images that are 150 pixels tall.
        """
    def setSizeCol(self, value):
        """
        Args:
            size: Filter images by the following sizes:Small: Return images that are less than 200x200 pixelsMedium: Return images that are greater than or equal to 200x200 pixels but less than 500x500 pixelsLarge: Return images that are 500x500 pixels or largerWallpaper: Return wallpaper images.AllDo not filter by size. Specifying this value is the same as not specifying the size parameter.You may use this parameter along with the height or width parameters. For example, you may use height and size to request small images that are 150 pixels tall.
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
    def setWidth(self, value):
        """
        Args:
            width: Filter images that have the specified width, in pixels.You may use this filter with the size filter to return small images that have a width of 150 pixels.
        """
    def setWidthCol(self, value):
        """
        Args:
            width: Filter images that have the specified width, in pixels.You may use this filter with the size filter to return small images that have a width of 150 pixels.
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
    def getAspect(self):
        """
        Returns:
            aspect: Filter images by the following aspect ratios: Square: Return images with standard aspect ratioWide: Return images with wide screen aspect ratioTall: Return images with tall aspect ratioAll: Do not filter by aspect. Specifying this value is the same as not specifying the aspect parameter.
        """
    def getColor(self):
        """
        Returns:
            color: Filter images by the following color options:ColorOnly: Return color imagesMonochrome: Return black and white imagesReturn images with one of the following dominant colors:Black,Blue,Brown,Gray,Green,Orange,Pink,Purple,Red,Teal,White,Yellow
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
    def getCount(self):
        """
        Returns:
            count: The number of image results to return in the response. The actual number delivered may be less than requested.
        """
    def getErrorCol(self):
        """
        Returns:
            errorCol: column to hold http errors
        """
    def getFreshness(self):
        """
        Returns:
            freshness: Filter images by the following discovery options:Day: Return images discovered by Bing within the last 24 hoursWeek: Return images discovered by Bing within the last 7 daysMonth: Return images discovered by Bing within the last 30 daysYear: Return images discovered within the last year2017-06-15..2018-06-15: Return images discovered within the specified range of dates
        """
    def getHandler(self):
        """
        Returns:
            handler: Which strategy to use when handling requests
        """
    def getHeight(self):
        """
        Returns:
            height: Filter images that have the specified height, in pixels.You may use this filter with the size filter to return small images that have a height of 150 pixels.
        """
    def getImageContent(self):
        """
        Returns:
            imageContent: Filter images by the following content types:Face: Return images that show only a person's facePortrait: Return images that show only a person's head and shoulders
        """
    def getImageType(self):
        """
        Returns:
            imageType: Filter images by the following image types:AnimatedGif: return animated gif imagesAnimatedGifHttps: return animated gif images that are from an https addressClipart: Return only clip art imagesLine: Return only line drawingsPhoto: Return only photographs (excluding line drawings, animated Gifs, and clip art)Shopping: Return only images that contain items where Bing knows of a merchant that is selling the items. This option is valid in the en-US market only. Transparent: Return only images with a transparent background.
        """
    def getLicense(self):
        """
        Returns:
            license: Filter images by the following license types:Any: Return images that are under any license type. The response doesn't include images that do not specify a license or the license is unknown.Public: Return images where the creator has waived their exclusive rights, to the fullest extent allowed by law.Share: Return images that may be shared with others. Changing or editing the image might not be allowed. Also, modifying, sharing, and using the image for commercial purposes might not be allowed. Typically, this option returns the most images.ShareCommercially: Return images that may be shared with others for personal or commercial purposes. Changing or editing the image might not be allowed.Modify: Return images that may be modified, shared, and used. Changing or editing the image might not be allowed. Modifying, sharing, and using the image for commercial purposes might not be allowed. ModifyCommercially: Return images that may be modified, shared, and used for personal or commercial purposes. Typically, this option returns the fewest images.All: Do not filter by license type. Specifying this value is the same as not specifying the license parameter. For more information about these license types, see Filter Images By License Type.
        """
    def getMaxFileSize(self):
        """
        Returns:
            maxFileSize: Filter images that are less than or equal to the specified file size.The maximum file size that you may specify is 520,192 bytes. If you specify a larger value, the API uses 520,192. It is possible that the response may include images that are slightly larger than the specified maximum.You may specify this filter and minFileSize to filter images within a range of file sizes.
        """
    def getMaxHeight(self):
        """
        Returns:
            maxHeight: Filter images that have a height that is less than or equal to the specified height. Specify the height in pixels.You may specify this filter and minHeight to filter images within a range of heights. This filter and the height filter are mutually exclusive.
        """
    def getMaxWidth(self):
        """
        Returns:
            maxWidth: Filter images that have a width that is less than or equal to the specified width. Specify the width in pixels.You may specify this filter and maxWidth to filter images within a range of widths. This filter and the width filter are mutually exclusive.
        """
    def getMinFileSize(self):
        """
        Returns:
            minFileSize: Filter images that are greater than or equal to the specified file size. The maximum file size that you may specify is 520,192 bytes. If you specify a larger value, the API uses 520,192. It is possible that the response may include images that are slightly smaller than the specified minimum. You may specify this filter and maxFileSize to filter images within a range of file sizes.
        """
    def getMinHeight(self):
        """
        Returns:
            minHeight: Filter images that have a height that is greater than or equal to the specified height. Specify the height in pixels.You may specify this filter and maxHeight to filter images within a range of heights. This filter and the height filter are mutually exclusive.
        """
    def getMinWidth(self):
        """
        Returns:
            minWidth: Filter images that have a width that is greater than or equal to the specified width. Specify the width in pixels. You may specify this filter and maxWidth to filter images within a range of widths. This filter and the width filter are mutually exclusive.
        """
    def getMkt(self):
        """
        Returns:
            mkt: The market where the results come from. Typically, this is the country where the user is making the request from; however, it could be a different country if the user is not located in a country where Bing delivers results. The market must be in the form -. For example, en-US. Full list of supported markets: es-AR,en-AU,de-AT,nl-BE,fr-BE,pt-BR,en-CA,fr-CA,es-CL,da-DK,fi-FI,fr-FR,de-DE,zh-HK,en-IN,en-ID,en-IE,it-IT,ja-JP,ko-KR,en-MY,es-MX,nl-NL,en-NZ,no-NO,zh-CN,pl-PL,pt-PT,en-PH,ru-RU,ar-SA,en-ZA,es-ES,sv-SE,fr-CH,de-CH,zh-TW,tr-TR,en-GB,en-US,es-US
        """
    def getOffset(self):
        """
        Returns:
            offset: The zero-based offset that indicates the number of image results to skip before returning results
        """
    def getOutputCol(self):
        """
        Returns:
            outputCol: The name of the output column
        """
    def getQ(self):
        """
        Returns:
            q: The user's search query string
        """
    def getSize(self):
        """
        Returns:
            size: Filter images by the following sizes:Small: Return images that are less than 200x200 pixelsMedium: Return images that are greater than or equal to 200x200 pixels but less than 500x500 pixelsLarge: Return images that are 500x500 pixels or largerWallpaper: Return wallpaper images.AllDo not filter by size. Specifying this value is the same as not specifying the size parameter.You may use this parameter along with the height or width parameters. For example, you may use height and size to request small images that are 150 pixels tall.
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
    def getWidth(self):
        """
        Returns:
            width: Filter images that have the specified width, in pixels.You may use this filter with the size filter to return small images that have a width of 150 pixels.
        """
    def setCustomServiceName(self, value): ...
    def setEndpoint(self, value): ...
    def setDefaultInternalEndpoint(self, value): ...
    def setLinkedService(self, value): ...
