import PIL
import numpy as np
from ...image_processing_utils import BaseImageProcessor as BaseImageProcessor, BatchFeature as BatchFeature, get_size_dict as get_size_dict
from ...image_transforms import center_crop as center_crop, get_resize_output_image_size as get_resize_output_image_size, rescale as rescale, resize as resize, to_channel_dimension_format as to_channel_dimension_format
from ...image_utils import ChannelDimension as ChannelDimension, ImageInput as ImageInput, PILImageResampling as PILImageResampling, infer_channel_dimension_format as infer_channel_dimension_format, is_batched as is_batched, to_numpy_array as to_numpy_array, valid_images as valid_images
from ...utils import logging as logging
from _typeshed import Incomplete
from transformers.utils import is_torch_available as is_torch_available, is_torch_tensor as is_torch_tensor, is_vision_available as is_vision_available
from transformers.utils.generic import TensorType as TensorType
from typing import Dict, List, Optional, Tuple, Union

logger: Incomplete

def flip_channel_order(image: np.ndarray, data_format: Optional[ChannelDimension]) -> np.ndarray:
    """
    Flip the color channels from RGB to BGR or vice versa.

    Args:
        image (`np.ndarray`):
            The image, represented as a numpy array.
        data_format (`ChannelDimension`, *`optional`*):
            The channel dimension format of the image. If not provided, it will be the same as the input image.

    Returns:
        `np.ndarray`: The image with the flipped color channels.
    """

class MobileViTImageProcessor(BaseImageProcessor):
    '''
    Constructs a MobileViT image processor.

    Args:
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the image\'s (height, width) dimensions to the specified `size`. Can be overridden by the
            `do_resize` parameter in the `preprocess` method.
        size (`Dict[str, int]` *optional*, defaults to `{"shortest_edge": 224}`):
            Controls the size of the output image after resizing. Can be overridden by the `size` parameter in the
            `preprocess` method.
        resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BILINEAR`):
            Defines the resampling filter to use if resizing the image. Can be overridden by the `resample` parameter
            in the `preprocess` method.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the `do_rescale`
            parameter in the `preprocess` method.
        rescale_factor (`int` or `float`, *optional*, defaults to `1/255`):
            Scale factor to use if rescaling the image. Can be overridden by the `rescale_factor` parameter in the
            `preprocess` method.
        do_center_crop (`bool`, *optional*, defaults to `True`):
            Whether to crop the input at the center. If the input size is smaller than `crop_size` along any edge, the
            image is padded with 0\'s and then center cropped. Can be overridden by the `do_center_crop` parameter in
            the `preprocess` method.
        crop_size (`Dict[str, int]`, *optional*, defaults to `{"height": 256, "width": 256}`):
            Desired output size `(size["height"], size["width"])` when applying center-cropping. Can be overridden by
            the `crop_size` parameter in the `preprocess` method.
        do_flip_channel_order (`bool`, *optional*, defaults to `True`):
            Whether to flip the color channels from RGB to BGR. Can be overridden by the `do_flip_channel_order`
            parameter in the `preprocess` method.
    '''
    model_input_names: Incomplete
    do_resize: Incomplete
    size: Incomplete
    resample: Incomplete
    do_rescale: Incomplete
    rescale_factor: Incomplete
    do_center_crop: Incomplete
    crop_size: Incomplete
    do_flip_channel_order: Incomplete
    def __init__(self, do_resize: bool = True, size: Dict[str, int] = None, resample: PILImageResampling = ..., do_rescale: bool = True, rescale_factor: Union[int, float] = ..., do_center_crop: bool = True, crop_size: Dict[str, int] = None, do_flip_channel_order: bool = True, **kwargs) -> None: ...
    def resize(self, image: np.ndarray, size: Dict[str, int], resample: PILImageResampling = ..., data_format: Optional[Union[str, ChannelDimension]] = None, **kwargs) -> np.ndarray:
        '''
        Resize an image.

        Args:
            image (`np.ndarray`):
                Image to resize.
            size (`Dict[str, int]`):
                Controls the size of the output image. The shortest edge of the image will be resized to
                `size["shortest_edge"]` while maintaining the aspect ratio.
            resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BILINEAR`):
                Resampling filter to use when resiizing the image.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
        '''
    def center_crop(self, image: np.ndarray, size: Dict[str, int], data_format: Optional[Union[str, ChannelDimension]] = None, **kwargs) -> np.ndarray:
        '''
        Center crop an image to size `(size["height], size["width"])`. If the input size is smaller than `size` along
        any edge, the image is padded with 0\'s and then center cropped.

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
    def flip_channel_order(self, image: np.ndarray, data_format: Optional[Union[str, ChannelDimension]] = None) -> np.ndarray:
        """
        Flip the color channels from RGB to BGR or vice versa.

        Args:
            image (`np.ndarray`):
                The image, represented as a numpy array.
            data_format (`ChannelDimension` or `str`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
        """
    def preprocess(self, images: ImageInput, do_resize: bool = None, size: Dict[str, int] = None, resample: PILImageResampling = None, do_rescale: bool = None, rescale_factor: float = None, do_center_crop: bool = None, crop_size: Dict[str, int] = None, do_flip_channel_order: bool = None, return_tensors: Optional[Union[str, TensorType]] = None, data_format: ChannelDimension = ..., **kwargs) -> PIL.Image.Image:
        """
        Preprocess an image or batch of images.

        Args:
            images (`ImageInput`):
                Image to preprocess.
            do_resize (`bool`, *optional*, defaults to `self.do_resize`):
                Whether to resize the image.
            size (`Dict[str, int]`, *optional*, defaults to `self.size`):
                Size of the image after resizing.
            resample (`int`, *optional*, defaults to `self.resample`):
                Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`, Only
                has an effect if `do_resize` is set to `True`.
            do_rescale (`bool`, *optional*, defaults to `self.do_rescale`):
                Whether to rescale the image by rescale factor.
            rescale_factor (`float`, *optional*, defaults to `self.rescale_factor`):
                Rescale factor to rescale the image by if `do_rescale` is set to `True`.
            do_center_crop (`bool`, *optional*, defaults to `self.do_center_crop`):
                Whether to center crop the image.
            crop_size (`Dict[str, int]`, *optional*, defaults to `self.crop_size`):
                Size of the center crop if `do_center_crop` is set to `True`.
            do_flip_channel_order (`bool`, *optional*, defaults to `self.do_flip_channel_order`):
                Whether to flip the channel order of the image.
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
        """
    def post_process_semantic_segmentation(self, outputs, target_sizes: List[Tuple] = None):
        """
        Converts the output of [`MobileViTForSemanticSegmentation`] into semantic segmentation maps. Only supports
        PyTorch.

        Args:
            outputs ([`MobileViTForSemanticSegmentation`]):
                Raw outputs of the model.
            target_sizes (`List[Tuple]`, *optional*):
                A list of length `batch_size`, where each item is a `Tuple[int, int]` corresponding to the requested
                final size (height, width) of each prediction. If left to None, predictions will not be resized.

        Returns:
            `List[torch.Tensor]`:
                A list of length `batch_size`, where each item is a semantic segmentation map of shape (height, width)
                corresponding to the target_sizes entry (if `target_sizes` is specified). Each entry of each
                `torch.Tensor` correspond to a semantic class id.
        """
