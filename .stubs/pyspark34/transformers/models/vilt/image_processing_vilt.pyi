import PIL
import numpy as np
from ...image_processing_utils import BaseImageProcessor as BaseImageProcessor, BatchFeature as BatchFeature, get_size_dict as get_size_dict
from ...image_transforms import PaddingMode as PaddingMode, normalize as normalize, pad as pad, rescale as rescale, resize as resize, to_channel_dimension_format as to_channel_dimension_format
from ...image_utils import ChannelDimension as ChannelDimension, IMAGENET_STANDARD_MEAN as IMAGENET_STANDARD_MEAN, IMAGENET_STANDARD_STD as IMAGENET_STANDARD_STD, ImageInput as ImageInput, PILImageResampling as PILImageResampling, get_image_size as get_image_size, infer_channel_dimension_format as infer_channel_dimension_format, is_batched as is_batched, to_numpy_array as to_numpy_array, valid_images as valid_images
from ...utils import logging as logging
from _typeshed import Incomplete
from transformers.utils import is_vision_available as is_vision_available
from transformers.utils.generic import TensorType as TensorType
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

logger: Incomplete

def max_across_indices(values: Iterable[Any]) -> List[Any]:
    """
    Return the maximum value across all indices of an iterable of values.
    """
def make_pixel_mask(image: np.ndarray, output_size: Tuple[int, int]) -> np.ndarray:
    """
    Make a pixel mask for the image, where 1 indicates a valid pixel and 0 indicates padding.

    Args:
        image (`np.ndarray`):
            Image to make the pixel mask for.
        output_size (`Tuple[int, int]`):
            Output size of the mask.
    """
def get_max_height_width(images: List[np.ndarray]) -> List[int]:
    """
    Get the maximum height and width across all images in a batch.
    """
def get_resize_output_image_size(input_image: np.ndarray, shorter: int = 800, longer: int = 1333, size_divisor: int = 32) -> Tuple[int, int]: ...

class ViltImageProcessor(BaseImageProcessor):
    '''
    Constructs a ViLT image processor.

    Args:
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the image\'s (height, width) dimensions to the specified `size`. Can be overridden by the
            `do_resize` parameter in the `preprocess` method.
        size (`Dict[str, int]` *optional*, defaults to `{"shortest_edge": 384}`):
            Resize the shorter side of the input to `size["shortest_edge"]`. The longer side will be limited to under
            `int((1333 / 800) * size["shortest_edge"])` while preserving the aspect ratio. Only has an effect if
            `do_resize` is set to `True`. Can be overridden by the `size` parameter in the `preprocess` method.
        size_divisor (`int`, *optional*, defaults to 32):
            The size by which to make sure both the height and width can be divided. Only has an effect if `do_resize`
            is set to `True`. Can be overridden by the `size_divisor` parameter in the `preprocess` method.
        resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BICUBIC`):
            Resampling filter to use if resizing the image. Only has an effect if `do_resize` is set to `True`. Can be
            overridden by the `resample` parameter in the `preprocess` method.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Wwhether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the
            `do_rescale` parameter in the `preprocess` method.
        rescale_factor (`int` or `float`, *optional*, defaults to `1/255`):
            Scale factor to use if rescaling the image. Only has an effect if `do_rescale` is set to `True`. Can be
            overridden by the `rescale_factor` parameter in the `preprocess` method.
        do_normalize (`bool`, *optional*, defaults to `True`):
            Whether to normalize the image. Can be overridden by the `do_normalize` parameter in the `preprocess`
            method. Can be overridden by the `do_normalize` parameter in the `preprocess` method.
        image_mean (`float` or `List[float]`, *optional*, defaults to `IMAGENET_STANDARD_MEAN`):
            Mean to use if normalizing the image. This is a float or list of floats the length of the number of
            channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method. Can be
            overridden by the `image_mean` parameter in the `preprocess` method.
        image_std (`float` or `List[float]`, *optional*, defaults to `IMAGENET_STANDARD_STD`):
            Standard deviation to use if normalizing the image. This is a float or list of floats the length of the
            number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method.
            Can be overridden by the `image_std` parameter in the `preprocess` method.
        do_pad (`bool`, *optional*, defaults to `True`):
            Whether to pad the image to the `(max_height, max_width)` of the images in the batch. Can be overridden by
            the `do_pad` parameter in the `preprocess` method.
    '''
    model_input_names: Incomplete
    do_resize: Incomplete
    size: Incomplete
    size_divisor: Incomplete
    resample: Incomplete
    do_rescale: Incomplete
    rescale_factor: Incomplete
    do_normalize: Incomplete
    image_mean: Incomplete
    image_std: Incomplete
    do_pad: Incomplete
    def __init__(self, do_resize: bool = True, size: Dict[str, int] = None, size_divisor: int = 32, resample: PILImageResampling = ..., do_rescale: bool = True, rescale_factor: Union[int, float] = ..., do_normalize: bool = True, image_mean: Optional[Union[float, List[float]]] = None, image_std: Optional[Union[float, List[float]]] = None, do_pad: bool = True, **kwargs) -> None: ...
    @classmethod
    def from_dict(cls, image_processor_dict: Dict[str, Any], **kwargs):
        """
        Overrides the `from_dict` method from the base class to make sure `reduce_labels` is updated if image processor
        is created using from_dict and kwargs e.g. `ViltImageProcessor.from_pretrained(checkpoint,
        pad_and_return_pixel_mask=False)`
        """
    def resize(self, image: np.ndarray, size: Dict[str, int], size_divisor: int = 32, resample: PILImageResampling = ..., data_format: Optional[Union[str, ChannelDimension]] = None, **kwargs) -> np.ndarray:
        '''
        Resize an image.

        Resizes the shorter side of the image to `size["shortest_edge"]` while preserving the aspect ratio. If the
        longer side is larger than the max size `(int(`size["shortest_edge"]` * 1333 / 800))`, the longer side is then
        resized to the max size while preserving the aspect ratio.

        Args:
            image (`np.ndarray`):
                Image to resize.
            size (`Dict[str, int]`):
                Controls the size of the output image. Should be of the form `{"shortest_edge": int}`.
            size_divisor (`int`, defaults to 32):
                The image is resized to a size that is a multiple of this value.
            resample (`PILImageResampling` filter, *optional*, defaults to `PILImageResampling.BICUBIC`):
                Resampling filter to use when resiizing the image.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
        '''
    def rescale(self, image: np.ndarray, scale: Union[int, float], data_format: Optional[Union[str, ChannelDimension]] = None, **kwargs):
        """
        Rescale an image by a scale factor. image = image * scale.

        Args:
            image (`np.ndarray`):
                Image to rescale.
            scale (`int` or `float`):
                Scale to apply to the image.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
        """
    def normalize(self, image: np.ndarray, mean: Union[float, List[float]], std: Union[float, List[float]], data_format: Optional[Union[str, ChannelDimension]] = None, **kwargs) -> np.ndarray:
        """
        Normalize an image. image = (image - image_mean) / image_std.

        Args:
            image (`np.ndarray`):
                Image to normalize.
            mean (`float` or `List[float]`):
                Image mean.
            std (`float` or `List[float]`):
                Image standard deviation.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
        """
    def pad(self, images: List[np.ndarray], return_pixel_mask: bool = True, return_tensors: Optional[Union[str, TensorType]] = None, data_format: Optional[ChannelDimension] = None) -> BatchFeature:
        """
        Pads a batch of images with zeros to the size of largest height and width in the batch and optionally returns
        their corresponding pixel mask.

        Args:
            images (`List[np.ndarray]`):
                Batch of images to pad.
            return_pixel_mask (`bool`, *optional*, defaults to `False`):
                Whether to return the pixel mask.
            return_tensors (`str` or `TensorType`, *optional*):
                The type of tensors to return. Can be one of:
                    - Unset: Return a list of `np.ndarray`.
                    - `TensorType.TENSORFLOW` or `'tf'`: Return a batch of type `tf.Tensor`.
                    - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`.
                    - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.
                    - `TensorType.JAX` or `'jax'`: Return a batch of type `jax.numpy.ndarray`.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
        """
    def pad_and_create_pixel_mask(self, pixel_values_list: List[ImageInput], return_tensors: Optional[Union[str, TensorType]] = None, data_format: Optional[ChannelDimension] = None) -> BatchFeature:
        """
        Pads a batch of images with zeros to the size of largest height and width in the batch and returns their
        corresponding pixel mask.

        Args:
            images (`List[np.ndarray]`):
                Batch of images to pad.
            return_tensors (`str` or `TensorType`, *optional*):
                The type of tensors to return. Can be one of:
                    - Unset: Return a list of `np.ndarray`.
                    - `TensorType.TENSORFLOW` or `'tf'`: Return a batch of type `tf.Tensor`.
                    - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`.
                    - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.
                    - `TensorType.JAX` or `'jax'`: Return a batch of type `jax.numpy.ndarray`.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
        """
    def preprocess(self, images: ImageInput, do_resize: Optional[bool] = None, size: Optional[Dict[str, int]] = None, size_divisor: Optional[int] = None, resample: PILImageResampling = None, do_rescale: Optional[bool] = None, rescale_factor: Optional[float] = None, do_normalize: Optional[bool] = None, image_mean: Optional[Union[float, List[float]]] = None, image_std: Optional[Union[float, List[float]]] = None, do_pad: Optional[bool] = None, return_tensors: Optional[Union[str, TensorType]] = None, data_format: ChannelDimension = ..., **kwargs) -> PIL.Image.Image:
        '''
        Preprocess an image or batch of images.

        Args:
            images (`ImageInput`):
                Image to preprocess.
            do_resize (`bool`, *optional*, defaults to `self.do_resize`):
                Whether to resize the image.
            size (`Dict[str, int]`, *optional*, defaults to `self.size`):
                Controls the size of the image after `resize`. The shortest edge of the image is resized to
                `size["shortest_edge"]` whilst preserving the aspect ratio. If the longest edge of this resized image
                is > `int(size["shortest_edge"] * (1333 / 800))`, then the image is resized again to make the longest
                edge equal to `int(size["shortest_edge"] * (1333 / 800))`.
            size_divisor (`int`, *optional*, defaults to `self.size_divisor`):
                The image is resized to a size that is a multiple of this value.
            resample (`PILImageResampling`, *optional*, defaults to `self.resample`):
                Resampling filter to use if resizing the image. Only has an effect if `do_resize` is set to `True`.
            do_rescale (`bool`, *optional*, defaults to `self.do_rescale`):
                Whether to rescale the image values between [0 - 1].
            rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`):
                Rescale factor to rescale the image by if `do_rescale` is set to `True`.
            do_normalize (`bool`, *optional*, defaults to `self.do_normalize`):
                Whether to normalize the image.
            image_mean (`float` or `List[float]`, *optional*, defaults to `self.image_mean`):
                Image mean to normalize the image by if `do_normalize` is set to `True`.
            image_std (`float` or `List[float]`, *optional*, defaults to `self.image_std`):
                Image standard deviation to normalize the image by if `do_normalize` is set to `True`.
            do_pad (`bool`, *optional*, defaults to `self.do_pad`):
                Whether to pad the image to the (max_height, max_width) in the batch. If `True`, a pixel mask is also
                created and returned.
            return_tensors (`str` or `TensorType`, *optional*):
                The type of tensors to return. Can be one of:
                    - Unset: Return a list of `np.ndarray`.
                    - `TensorType.TENSORFLOW` or `\'tf\'`: Return a batch of type `tf.Tensor`.
                    - `TensorType.PYTORCH` or `\'pt\'`: Return a batch of type `torch.Tensor`.
                    - `TensorType.NUMPY` or `\'np\'`: Return a batch of type `np.ndarray`.
                    - `TensorType.JAX` or `\'jax\'`: Return a batch of type `jax.numpy.ndarray`.
            data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`):
                The channel dimension format for the output image. Can be one of:
                    - `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                    - `ChannelDimension.LAST`: image in (height, width, num_channels) format.
        '''
