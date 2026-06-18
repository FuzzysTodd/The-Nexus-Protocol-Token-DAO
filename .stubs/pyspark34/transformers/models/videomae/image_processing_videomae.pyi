import PIL
import numpy as np
from ...image_processing_utils import BaseImageProcessor as BaseImageProcessor, BatchFeature as BatchFeature, get_size_dict as get_size_dict
from ...image_transforms import center_crop as center_crop, get_resize_output_image_size as get_resize_output_image_size, normalize as normalize, rescale as rescale, resize as resize, to_channel_dimension_format as to_channel_dimension_format
from ...image_utils import ChannelDimension as ChannelDimension, IMAGENET_STANDARD_MEAN as IMAGENET_STANDARD_MEAN, IMAGENET_STANDARD_STD as IMAGENET_STANDARD_STD, ImageInput as ImageInput, PILImageResampling as PILImageResampling, is_valid_image as is_valid_image, to_numpy_array as to_numpy_array, valid_images as valid_images
from ...utils import logging as logging
from _typeshed import Incomplete
from transformers.utils import is_vision_available as is_vision_available
from transformers.utils.generic import TensorType as TensorType
from typing import Dict, List, Optional, Union

logger: Incomplete

def make_batched(videos) -> List[List[ImageInput]]: ...

class VideoMAEImageProcessor(BaseImageProcessor):
    '''
    Constructs a VideoMAE image processor.

    Args:
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the image\'s (height, width) dimensions to the specified `size`. Can be overridden by the
            `do_resize` parameter in the `preprocess` method.
        size (`Dict[str, int]` *optional*, defaults to `{"shortest_edge": 224}`):
            Size of the output image after resizing. The shortest edge of the image will be resized to
            `size["shortest_edge"]` while maintaining the aspect ratio of the original image. Can be overriden by
            `size` in the `preprocess` method.
        resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BILINEAR`):
            Resampling filter to use if resizing the image. Can be overridden by the `resample` parameter in the
            `preprocess` method.
        do_center_crop (`bool`, *optional*, defaults to `True`):
            Whether to center crop the image to the specified `crop_size`. Can be overridden by the `do_center_crop`
            parameter in the `preprocess` method.
        crop_size (`Dict[str, int]`, *optional*, defaults to `{"height": 224, "width": 224}`):
            Size of the image after applying the center crop. Can be overridden by the `crop_size` parameter in the
            `preprocess` method.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the `do_rescale`
            parameter in the `preprocess` method.
        rescale_factor (`int` or `float`, *optional*, defaults to `1/255`):
            Defines the scale factor to use if rescaling the image. Can be overridden by the `rescale_factor` parameter
            in the `preprocess` method.
        do_normalize (`bool`, *optional*, defaults to `True`):
            Whether to normalize the image. Can be overridden by the `do_normalize` parameter in the `preprocess`
            method.
        image_mean (`float` or `List[float]`, *optional*, defaults to `IMAGENET_STANDARD_MEAN`):
            Mean to use if normalizing the image. This is a float or list of floats the length of the number of
            channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method.
        image_std (`float` or `List[float]`, *optional*, defaults to `IMAGENET_STANDARD_STD`):
            Standard deviation to use if normalizing the image. This is a float or list of floats the length of the
            number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method.
    '''
    model_input_names: Incomplete
    do_resize: Incomplete
    size: Incomplete
    do_center_crop: Incomplete
    crop_size: Incomplete
    resample: Incomplete
    do_rescale: Incomplete
    rescale_factor: Incomplete
    do_normalize: Incomplete
    image_mean: Incomplete
    image_std: Incomplete
    def __init__(self, do_resize: bool = True, size: Dict[str, int] = None, resample: PILImageResampling = ..., do_center_crop: bool = True, crop_size: Dict[str, int] = None, do_rescale: bool = True, rescale_factor: Union[int, float] = ..., do_normalize: bool = True, image_mean: Optional[Union[float, List[float]]] = None, image_std: Optional[Union[float, List[float]]] = None, **kwargs) -> None: ...
    def resize(self, image: np.ndarray, size: Dict[str, int], resample: PILImageResampling = ..., data_format: Optional[Union[str, ChannelDimension]] = None, **kwargs) -> np.ndarray:
        '''
        Resize an image.

        Args:
            image (`np.ndarray`):
                Image to resize.
            size (`Dict[str, int]`):
                Size of the output image. If `size` is of the form `{"height": h, "width": w}`, the output image will
                have the size `(h, w)`. If `size` is of the form `{"shortest_edge": s}`, the output image will have its
                shortest edge of length `s` while keeping the aspect ratio of the original image.
            resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BILINEAR`):
                Resampling filter to use when resiizing the image.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
        '''
    def center_crop(self, image: np.ndarray, size: Dict[str, int], data_format: Optional[Union[str, ChannelDimension]] = None, **kwargs) -> np.ndarray:
        '''
        Center crop an image to `(size["height"], size["width"])`. If the input size is smaller than `size` along any
        edge, the image is padded with 0\'s and then center cropped.

        Args:
            image (`np.ndarray`):
                Image to center crop.
            size (`Dict[str, int]`):
                Size of the output image.
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
            image_mean (`float` or `List[float]`):
                Image mean.
            image_std (`float` or `List[float]`):
                Image standard deviation.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
        """
    def preprocess(self, videos: ImageInput, do_resize: bool = None, size: Dict[str, int] = None, resample: PILImageResampling = None, do_center_crop: bool = None, crop_size: Dict[str, int] = None, do_rescale: bool = None, rescale_factor: float = None, do_normalize: bool = None, image_mean: Optional[Union[float, List[float]]] = None, image_std: Optional[Union[float, List[float]]] = None, return_tensors: Optional[Union[str, TensorType]] = None, data_format: ChannelDimension = ..., **kwargs) -> PIL.Image.Image:
        """
        Preprocess an image or batch of images.

        Args:
            images (`ImageInput`):
                Image to preprocess.
            do_resize (`bool`, *optional*, defaults to `self.do_resize`):
                Whether to resize the image.
            size (`Dict[str, int]`, *optional*, defaults to `self.size`):
                Size of the image after applying resize.
            resample (`PILImageResampling`, *optional*, defaults to `self.resample`):
                Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`, Only
                has an effect if `do_resize` is set to `True`.
            do_center_crop (`bool`, *optional*, defaults to `self.do_centre_crop`):
                Whether to centre crop the image.
            crop_size (`Dict[str, int]`, *optional*, defaults to `self.crop_size`):
                Size of the image after applying the centre crop.
            do_rescale (`bool`, *optional*, defaults to `self.do_rescale`):
                Whether to rescale the image values between [0 - 1].
            rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`):
                Rescale factor to rescale the image by if `do_rescale` is set to `True`.
            do_normalize (`bool`, *optional*, defaults to `self.do_normalize`):
                Whether to normalize the image.
            image_mean (`float` or `List[float]`, *optional*, defaults to `self.image_mean`):
                Image mean.
            image_std (`float` or `List[float]`, *optional*, defaults to `self.image_std`):
                Image standard deviation.
            return_tensors (`str` or `TensorType`, *optional*):
                The type of tensors to return. Can be one of:
                    - Unset: Return a list of `np.ndarray`.
                    - `TensorType.TENSORFLOW` or `'tf'`: Return a batch of type `tf.Tensor`.
                    - `TensorType.PYTORCH` or `'pt'`: Return a batch of type `torch.Tensor`.
                    - `TensorType.NUMPY` or `'np'`: Return a batch of type `np.ndarray`.
                    - `TensorType.JAX` or `'jax'`: Return a batch of type `jax.numpy.ndarray`.
            data_format (`ChannelDimension` or `str`, *optional*, defaults to `ChannelDimension.FIRST`):
                The channel dimension format for the output image. Can be one of:
                    - `ChannelDimension.FIRST`: image in (num_channels, height, width) format.
                    - `ChannelDimension.LAST`: image in (height, width, num_channels) format.
                    - Unset: Use the inferred channel dimension format of the input image.
        """
