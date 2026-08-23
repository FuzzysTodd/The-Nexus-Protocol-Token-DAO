from pyspark.sql.types import *
from _typeshed import Incomplete
from pyspark import SparkContext as SparkContext
from pyspark.sql.types import Row as Row
from synapse.ml.opencv._ImageTransformer import _ImageTransformer

basestring = str
ImageFields: Incomplete
ImageSchema: Incomplete

def toNDArray(image):
    """
    Converts an image to a 1-dimensional array

    Args:
        image (object): The image to be converted

    Returns:
        array: The image as a 1-dimensional array
    """
def toImage(array, path: str = '', mode: int = 16):
    """

    Converts a one-dimensional array to a 2 dimensional image

    Args:
        array (array):
        path (str):
        ocvType (int):

    Returns:
        object: 2 dimensional image
    """

class ImageTransformer(_ImageTransformer):
    """
    Transformer for common image processing stages.
    """
    def resize(self, size, keep_aspect_ratio: bool = True):
        """
        Resizes the image to the given size.

        Args:
            size (int or tuple(width, height)): The size to resize to (>=0).
            keep_aspect_ratio (bool): Whether to keep aspect ratio.
            If true, the shorter side of the image will be resized to the specified size.
        """
    def crop(self, x, y, height, width):
        """
        Crops the image given the starting x,y coordinates
        and the width and height

        Args:
            x (int): The initial x coordinate (>=0)
            y (int): The initial y coordinate (>=0)
            height (int): The height to crop to (>=0)
            width (int): The width to crop to (>=0)

        """
    def centerCrop(self, height, width):
        """
        Center crops the image given the width and height.

        Args:
            height (int): The height to crop to (>= 0)
            width (int): The width to crop to (>= 0)

        """
    def colorFormat(self, format):
        """
        Formats the image to the given image format

        Args:
            format (int): The format to convert to, please see OpenCV cvtColor function documentation for all formats

        """
    def blur(self, height, width):
        """
        Blurs the image using a normalized box filter

        Args:
            height (double): The height of the box filter (>= 0)
            width (double): The width of the box filter (>= 0)

        """
    def threshold(self, threshold, max_val, threshold_type):
        """
        Thresholds the image, please see OpenCV threshold function documentation for more information

        Args:
            threshold: (double) The threshold value
            max_val (double): The maximum value to use
            threshold_type (double): The type of threshold, can be binary, binary_inv, trunc, zero, zero_inv

        """
    def gaussianKernel(self, aperture_size, sigma):
        """
        Blurs the image by applying a gaussian kernel

        Args:
            aperture_size (double): The aperture size, which should be odd and positive
            sigma (double): The standard deviation of the gaussian

        """
    def flip(self, flip_code: int = 1):
        """
        Flips the image
        :param int flip_code: a flag to specify how to flip the image
        - 0 means flipping around the x-axis (up-down)
        - positive value (for example, 1) means flipping around y-axis (left-right, default)
        - negative value (for example, -1) means flipping around both axes (diagonally)
        See OpenCV documentation for details.
        """
    def normalize(self, mean, std, color_scale_factor):
        """
        Normalizes the image by multiplying the color_scale_factor, substracting mean and dividing by std
        """
