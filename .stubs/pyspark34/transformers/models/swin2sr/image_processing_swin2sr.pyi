import numpy as np
from ...image_processing_utils import BaseImageProcessor as BaseImageProcessor, BatchFeature as BatchFeature
from ...image_transforms import get_image_size as get_image_size, pad as pad, rescale as rescale, to_channel_dimension_format as to_channel_dimension_format
from ...image_utils import ChannelDimension as ChannelDimension, ImageInput as ImageInput, is_batched as is_batched, to_numpy_array as to_numpy_array, valid_images as valid_images
from ...utils import logging as logging
from _typeshed import Incomplete
from transformers.utils.generic import TensorType as TensorType
from typing import Optional, Union

logger: Incomplete

class Swin2SRImageProcessor(BaseImageProcessor):
    """
    Constructs a Swin2SR image processor.

    Args:
        do_rescale (`bool`, *optional*, defaults to `True`):
            Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the `do_rescale`
            parameter in the `preprocess` method.
        rescale_factor (`int` or `float`, *optional*, defaults to `1/255`):
            Scale factor to use if rescaling the image. Can be overridden by the `rescale_factor` parameter in the
            `preprocess` method.
    """
    model_input_names: Incomplete
    do_rescale: Incomplete
    rescale_factor: Incomplete
    do_pad: Incomplete
    pad_size: Incomplete
    def __init__(self, do_rescale: bool = True, rescale_factor: Union[int, float] = ..., do_pad: bool = True, pad_size: int = 8, **kwargs) -> None: ...
    def rescale(self, image: np.ndarray, scale: float, data_format: Optional[Union[str, ChannelDimension]] = None, **kwargs) -> np.ndarray:
        '''
        Rescale an image by a scale factor. image = image * scale.

        Args:
            image (`np.ndarray`):
                Image to rescale.
            scale (`float`):
                The scaling factor to rescale pixel values by.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format for the output image. If unset, the channel dimension format of the input
                image is used. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.

        Returns:
            `np.ndarray`: The rescaled image.
        '''
    def pad(self, image: np.ndarray, size: int, data_format: Optional[Union[str, ChannelDimension]] = None):
        '''
        Pad an image to make the height and width divisible by `size`.

        Args:
            image (`np.ndarray`):
                Image to pad.
            size (`int`):
                The size to make the height and width divisible by.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format for the output image. If unset, the channel dimension format of the input
                image is used. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.

        Returns:
            `np.ndarray`: The padded image.
        '''
    def preprocess(self, images: ImageInput, do_rescale: Optional[bool] = None, rescale_factor: Optional[float] = None, do_pad: Optional[bool] = None, pad_size: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, data_format: Union[str, ChannelDimension] = ..., **kwargs):
        '''
        Preprocess an image or batch of images.

        Args:
            images (`ImageInput`):
                Image to preprocess.
            do_rescale (`bool`, *optional*, defaults to `self.do_rescale`):
                Whether to rescale the image values between [0 - 1].
            rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`):
                Rescale factor to rescale the image by if `do_rescale` is set to `True`.
            do_pad (`bool`, *optional*, defaults to `True`):
                Whether to pad the image to make the height and width divisible by `window_size`.
            pad_size (`int`, *optional*, defaults to `32`):
                The size of the sliding window for the local attention.
            return_tensors (`str` or `TensorType`, *optional*):
                The type of tensors to return. Can be one of:
                - Unset: Return a list of `np.ndarray`.
                - `TensorType.TENSORFLOW` or `\'tf\'`: Return a batch of type `tf.Tensor`.
                - `TensorType.PYTORCH` or `\'pt\'`: Return a batch of type `torch.Tensor`.
                - `TensorType.NUMPY` or `\'np\'`: Return a batch of type `np.ndarray`.
                - `TensorType.JAX` or `\'jax\'`: Return a batch of type `jax.numpy.ndarray`.
            data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`):
                The channel dimension format for the output image. Can be one of:
                - `"channels_first"` or `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                - `"channels_last"` or `ChannelDimension.LAST`: image in (height, width, num_channels) format.
                - Unset: Use the channel dimension format of the input image.
        '''
