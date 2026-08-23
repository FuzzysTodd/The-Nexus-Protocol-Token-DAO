import PIL.Image
import numpy as np
from .utils import ExplicitEnum as ExplicitEnum, is_jax_tensor as is_jax_tensor, is_tf_tensor as is_tf_tensor, is_torch_available as is_torch_available, is_torch_tensor as is_torch_tensor, is_vision_available as is_vision_available, requires_backends as requires_backends, to_numpy as to_numpy
from .utils.constants import IMAGENET_DEFAULT_MEAN as IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD as IMAGENET_DEFAULT_STD, IMAGENET_STANDARD_MEAN as IMAGENET_STANDARD_MEAN, IMAGENET_STANDARD_STD as IMAGENET_STANDARD_STD
from _typeshed import Incomplete
from typing import Dict, Iterable, List, Tuple, Union

PILImageResampling: Incomplete
ImageInput: Incomplete

class ChannelDimension(ExplicitEnum):
    FIRST: str
    LAST: str

def is_valid_image(img): ...
def valid_images(imgs): ...
def is_batched(img): ...
def to_numpy_array(img) -> np.ndarray: ...
def infer_channel_dimension_format(image: np.ndarray) -> ChannelDimension:
    """
    Infers the channel dimension format of `image`.

    Args:
        image (`np.ndarray`):
            The image to infer the channel dimension of.

    Returns:
        The channel dimension of the image.
    """
def get_channel_dimension_axis(image: np.ndarray) -> int:
    """
    Returns the channel dimension axis of the image.

    Args:
        image (`np.ndarray`):
            The image to get the channel dimension axis of.

    Returns:
        The channel dimension axis of the image.
    """
def get_image_size(image: np.ndarray, channel_dim: ChannelDimension = None) -> Tuple[int, int]:
    """
    Returns the (height, width) dimensions of the image.

    Args:
        image (`np.ndarray`):
            The image to get the dimensions of.
        channel_dim (`ChannelDimension`, *optional*):
            Which dimension the channel dimension is in. If `None`, will infer the channel dimension from the image.

    Returns:
        A tuple of the image's height and width.
    """
def is_valid_annotation_coco_detection(annotation: Dict[str, Union[List, Tuple]]) -> bool: ...
def is_valid_annotation_coco_panoptic(annotation: Dict[str, Union[List, Tuple]]) -> bool: ...
def valid_coco_detection_annotations(annotations: Iterable[Dict[str, Union[List, Tuple]]]) -> bool: ...
def valid_coco_panoptic_annotations(annotations: Iterable[Dict[str, Union[List, Tuple]]]) -> bool: ...
def load_image(image: Union[str, 'PIL.Image.Image']) -> PIL.Image.Image:
    """
    Loads `image` to a PIL Image.

    Args:
        image (`str` or `PIL.Image.Image`):
            The image to convert to the PIL Image format.

    Returns:
        `PIL.Image.Image`: A PIL Image.
    """

class ImageFeatureExtractionMixin:
    """
    Mixin that contain utilities for preparing image features.
    """
    def to_pil_image(self, image, rescale: Incomplete | None = None):
        """
        Converts `image` to a PIL Image. Optionally rescales it and puts the channel dimension back as the last axis if
        needed.

        Args:
            image (`PIL.Image.Image` or `numpy.ndarray` or `torch.Tensor`):
                The image to convert to the PIL Image format.
            rescale (`bool`, *optional*):
                Whether or not to apply the scaling factor (to make pixel values integers between 0 and 255). Will
                default to `True` if the image type is a floating type, `False` otherwise.
        """
    def convert_rgb(self, image):
        """
        Converts `PIL.Image.Image` to RGB format.

        Args:
            image (`PIL.Image.Image`):
                The image to convert.
        """
    def rescale(self, image: np.ndarray, scale: Union[float, int]) -> np.ndarray:
        """
        Rescale a numpy image by scale amount
        """
    def to_numpy_array(self, image, rescale: Incomplete | None = None, channel_first: bool = True):
        """
        Converts `image` to a numpy array. Optionally rescales it and puts the channel dimension as the first
        dimension.

        Args:
            image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor`):
                The image to convert to a NumPy array.
            rescale (`bool`, *optional*):
                Whether or not to apply the scaling factor (to make pixel values floats between 0. and 1.). Will
                default to `True` if the image is a PIL Image or an array/tensor of integers, `False` otherwise.
            channel_first (`bool`, *optional*, defaults to `True`):
                Whether or not to permute the dimensions of the image to put the channel dimension first.
        """
    def expand_dims(self, image):
        """
        Expands 2-dimensional `image` to 3 dimensions.

        Args:
            image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor`):
                The image to expand.
        """
    def normalize(self, image, mean, std, rescale: bool = False):
        """
        Normalizes `image` with `mean` and `std`. Note that this will trigger a conversion of `image` to a NumPy array
        if it's a PIL Image.

        Args:
            image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor`):
                The image to normalize.
            mean (`List[float]` or `np.ndarray` or `torch.Tensor`):
                The mean (per channel) to use for normalization.
            std (`List[float]` or `np.ndarray` or `torch.Tensor`):
                The standard deviation (per channel) to use for normalization.
            rescale (`bool`, *optional*, defaults to `False`):
                Whether or not to rescale the image to be between 0 and 1. If a PIL image is provided, scaling will
                happen automatically.
        """
    def resize(self, image, size, resample: Incomplete | None = None, default_to_square: bool = True, max_size: Incomplete | None = None):
        """
        Resizes `image`. Enforces conversion of input to PIL.Image.

        Args:
            image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor`):
                The image to resize.
            size (`int` or `Tuple[int, int]`):
                The size to use for resizing the image. If `size` is a sequence like (h, w), output size will be
                matched to this.

                If `size` is an int and `default_to_square` is `True`, then image will be resized to (size, size). If
                `size` is an int and `default_to_square` is `False`, then smaller edge of the image will be matched to
                this number. i.e, if height > width, then image will be rescaled to (size * height / width, size).
            resample (`int`, *optional*, defaults to `PILImageResampling.BILINEAR`):
                The filter to user for resampling.
            default_to_square (`bool`, *optional*, defaults to `True`):
                How to convert `size` when it is a single int. If set to `True`, the `size` will be converted to a
                square (`size`,`size`). If set to `False`, will replicate
                [`torchvision.transforms.Resize`](https://pytorch.org/vision/stable/transforms.html#torchvision.transforms.Resize)
                with support for resizing only the smallest edge and providing an optional `max_size`.
            max_size (`int`, *optional*, defaults to `None`):
                The maximum allowed for the longer edge of the resized image: if the longer edge of the image is
                greater than `max_size` after being resized according to `size`, then the image is resized again so
                that the longer edge is equal to `max_size`. As a result, `size` might be overruled, i.e the smaller
                edge may be shorter than `size`. Only used if `default_to_square` is `False`.

        Returns:
            image: A resized `PIL.Image.Image`.
        """
    def center_crop(self, image, size):
        """
        Crops `image` to the given size using a center crop. Note that if the image is too small to be cropped to the
        size given, it will be padded (so the returned result has the size asked).

        Args:
            image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor` of shape (n_channels, height, width) or (height, width, n_channels)):
                The image to resize.
            size (`int` or `Tuple[int, int]`):
                The size to which crop the image.

        Returns:
            new_image: A center cropped `PIL.Image.Image` or `np.ndarray` or `torch.Tensor` of shape: (n_channels,
            height, width).
        """
    def flip_channel_order(self, image):
        """
        Flips the channel order of `image` from RGB to BGR, or vice versa. Note that this will trigger a conversion of
        `image` to a NumPy array if it's a PIL Image.

        Args:
            image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor`):
                The image whose color channels to flip. If `np.ndarray` or `torch.Tensor`, the channel dimension should
                be first.
        """
    def rotate(self, image, angle, resample: Incomplete | None = None, expand: int = 0, center: Incomplete | None = None, translate: Incomplete | None = None, fillcolor: Incomplete | None = None):
        """
        Returns a rotated copy of `image`. This method returns a copy of `image`, rotated the given number of degrees
        counter clockwise around its centre.

        Args:
            image (`PIL.Image.Image` or `np.ndarray` or `torch.Tensor`):
                The image to rotate. If `np.ndarray` or `torch.Tensor`, will be converted to `PIL.Image.Image` before
                rotating.

        Returns:
            image: A rotated `PIL.Image.Image`.
        """
