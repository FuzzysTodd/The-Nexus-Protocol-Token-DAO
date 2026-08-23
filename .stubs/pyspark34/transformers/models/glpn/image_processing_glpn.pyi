import PIL.Image
import numpy as np
from ...image_processing_utils import BaseImageProcessor as BaseImageProcessor, BatchFeature as BatchFeature
from ...image_transforms import rescale as rescale, resize as resize, to_channel_dimension_format as to_channel_dimension_format
from ...image_utils import ChannelDimension as ChannelDimension, get_image_size as get_image_size, is_batched as is_batched, to_numpy_array as to_numpy_array, valid_images as valid_images
from ...utils import logging as logging
from _typeshed import Incomplete
from transformers.image_utils import PILImageResampling as PILImageResampling
from transformers.utils.generic import TensorType as TensorType
from typing import List, Optional, Union

logger: Incomplete

class GLPNImageProcessor(BaseImageProcessor):
    """
    Constructs a GLPN image processor.

    Args:
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the image's (height, width) dimensions, rounding them down to the closest multiple of
            `size_divisor`. Can be overridden by `do_resize` in `preprocess`.
        size_divisor (`int`, *optional*, defaults to 32):
            When `do_resize` is `True`, images are resized so their height and width are rounded down to the closest
            multiple of `size_divisor`. Can be overridden by `size_divisor` in `preprocess`.
        resample (`PIL.Image` resampling filter, *optional*, defaults to `PILImageResampling.BILINEAR`):
            Resampling filter to use if resizing the image. Can be overridden by `resample` in `preprocess`.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Whether or not to apply the scaling factor (to make pixel values floats between 0. and 1.). Can be
            overridden by `do_rescale` in `preprocess`.
    """
    model_input_names: Incomplete
    do_resize: Incomplete
    do_rescale: Incomplete
    size_divisor: Incomplete
    resample: Incomplete
    def __init__(self, do_resize: bool = True, size_divisor: int = 32, resample=..., do_rescale: bool = True, **kwargs) -> None: ...
    def resize(self, image: np.ndarray, size_divisor: int, resample, data_format: Optional[ChannelDimension] = None, **kwargs) -> np.ndarray:
        """
        Resize the image, rounding the (height, width) dimensions down to the closest multiple of size_divisor.

        If the image is of dimension (3, 260, 170) and size_divisor is 32, the image will be resized to (3, 256, 160).

        Args:
            image (`np.ndarray`):
                The image to resize.
            size_divisor (`int`):
                The image is resized so its height and width are rounded down to the closest multiple of
                `size_divisor`.
            resample:
                `PIL.Image` resampling filter to use when resizing the image e.g. `PILImageResampling.BILINEAR`.
            data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format for the output image. If `None`, the channel dimension format of the input
                image is used. Can be one of:
                - `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `ChannelDimension.LAST`: image in (height, width, num_channels) format.

        Returns:
            `np.ndarray`: The resized image.
        """
    def rescale(self, image: np.ndarray, scale: float, data_format: Optional[ChannelDimension] = None, **kwargs) -> np.ndarray:
        """
        Rescale the image by the given scaling factor `scale`.

        Args:
            image (`np.ndarray`):
                The image to rescale.
            scale (`float`):
                The scaling factor to rescale pixel values by.
            data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format for the output image. If `None`, the channel dimension format of the input
                image is used. Can be one of:
                - `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `ChannelDimension.LAST`: image in (height, width, num_channels) format.

        Returns:
            `np.ndarray`: The rescaled image.
        """
    def preprocess(self, images: Union['PIL.Image.Image', TensorType, List['PIL.Image.Image'], List[TensorType]], do_resize: Optional[bool] = None, size_divisor: Optional[int] = None, resample: Incomplete | None = None, do_rescale: Optional[bool] = None, return_tensors: Optional[Union[TensorType, str]] = None, data_format: ChannelDimension = ..., **kwargs) -> BatchFeature:
        """
        Preprocess the given images.

        Args:
            images (`PIL.Image.Image` or `TensorType` or `List[np.ndarray]` or `List[TensorType]`):
                The image or images to preprocess.
            do_resize (`bool`, *optional*, defaults to `self.do_resize`):
                Whether to resize the input such that the (height, width) dimensions are a multiple of `size_divisor`.
            size_divisor (`int`, *optional*, defaults to `self.size_divisor`):
                When `do_resize` is `True`, images are resized so their height and width are rounded down to the
                closest multiple of `size_divisor`.
            resample (`PIL.Image` resampling filter, *optional*, defaults to `self.resample`):
                `PIL.Image` resampling filter to use if resizing the image e.g. `PILImageResampling.BILINEAR`. Only has
                an effect if `do_resize` is set to `True`.
            do_rescale (`bool`, *optional*, defaults to `self.do_rescale`):
                Whether or not to apply the scaling factor (to make pixel values floats between 0. and 1.).
            return_tensors (`str` or `TensorType`, *optional*):
                The type of tensors to return. Can be one of:
                    - `None`: Return a list of `np.ndarray`.
                    - `TensorType.TENSORFLOW` or `'tf'`: Return a batch of type `tf.Tensor`.
                    - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`.
                    - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.
                    - `TensorType.JAX` or `'jax'`: Return a batch of type `jax.numpy.ndarray`.
            data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`):
                The channel dimension format for the output image. Can be one of:
                    - `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                    - `ChannelDimension.LAST`: image in (height, width, num_channels) format.
        """
