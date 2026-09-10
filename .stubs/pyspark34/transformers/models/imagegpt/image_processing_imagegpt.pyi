import PIL
import numpy as np
from ...image_processing_utils import BaseImageProcessor as BaseImageProcessor, BatchFeature as BatchFeature, get_size_dict as get_size_dict
from ...image_transforms import rescale as rescale, resize as resize, to_channel_dimension_format as to_channel_dimension_format
from ...image_utils import ChannelDimension as ChannelDimension, ImageInput as ImageInput, PILImageResampling as PILImageResampling, is_batched as is_batched, to_numpy_array as to_numpy_array, valid_images as valid_images
from ...utils import logging as logging
from _typeshed import Incomplete
from transformers.utils import is_vision_available as is_vision_available
from transformers.utils.generic import TensorType as TensorType
from typing import Dict, List, Optional, Union

logger: Incomplete

def squared_euclidean_distance(a, b): ...
def color_quantize(x, clusters): ...

class ImageGPTImageProcessor(BaseImageProcessor):
    '''
    Constructs a ImageGPT image processor. This image processor can be used to resize images to a smaller resolution
    (such as 32x32 or 64x64), normalize them and finally color quantize them to obtain sequences of "pixel values"
    (color clusters).

    Args:
        clusters (`np.ndarray`, *optional*):
            The color clusters to use, as a `np.ndarray` of shape `(n_clusters, 3)` when color quantizing. Can be
            overriden by `clusters` in `preprocess`.
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the image\'s dimensions to `(size["height"], size["width"])`. Can be overridden by
            `do_resize` in `preprocess`.
        size (`Dict[str, int]` *optional*, defaults to `{"height": 256, "width": 256}`):
            Size of the image after resizing. Can be overridden by `size` in `preprocess`.
        resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BICUBIC`):
            Resampling filter to use if resizing the image. Can be overridden by `resample` in `preprocess`.
        do_normalize (`bool`, *optional*, defaults to `True`):
            Whether to normalize the image pixel value to between [-1, 1]. Can be overridden by `do_normalize` in
            `preprocess`.
        do_color_quantize (`bool`, *optional*, defaults to `True`):
            Whether to color quantize the image. Can be overridden by `do_color_quantize` in `preprocess`.
    '''
    model_input_names: Incomplete
    clusters: Incomplete
    do_resize: Incomplete
    size: Incomplete
    resample: Incomplete
    do_normalize: Incomplete
    do_color_quantize: Incomplete
    def __init__(self, clusters: Optional[np.ndarray] = None, do_resize: bool = True, size: Dict[str, int] = None, resample: PILImageResampling = ..., do_normalize: bool = True, do_color_quantize: bool = True, **kwargs) -> None: ...
    def resize(self, image: np.ndarray, size: Dict[str, int], resample: PILImageResampling = ..., data_format: Optional[Union[str, ChannelDimension]] = None, **kwargs) -> np.ndarray:
        '''
        Resize an image to (size["height"], size["width"]).

        Args:
            image (`np.ndarray`):
                Image to resize.
            size (`Dict[str, int]`):
                Size of the output image.
            resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BILINEAR`):
                Resampling filter to use when resizing the image.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
        '''
    def normalize(self, image: np.ndarray, data_format: Optional[Union[str, ChannelDimension]] = None) -> np.ndarray:
        """
        Normalizes an images' pixel values to between [-1, 1].

        Args:
            image (`np.ndarray`):
                Image to normalize.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
        """
    def preprocess(self, images: ImageInput, do_resize: bool = None, size: Dict[str, int] = None, resample: PILImageResampling = None, do_normalize: bool = None, do_color_quantize: Optional[bool] = None, clusters: Optional[Union[int, List[int]]] = None, return_tensors: Optional[Union[str, TensorType]] = None, data_format: Optional[Union[str, ChannelDimension]] = ..., **kwargs) -> PIL.Image.Image:
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
            do_normalize (`bool`, *optional*, defaults to `self.do_normalize`):
                Whether to normalize the image
            do_color_quantize (`bool`, *optional*, defaults to `self.do_color_quantize`):
                Whether to color quantize the image.
            clusters (`np.ndarray`, *optional*, defaults to `self.clusters`):
                Clusters used to quantize the image of shape `(n_clusters, 3)`. Only has an effect if
                `do_color_quantize` is set to `True`.
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
                Only has an effect if `do_color_quantize` is set to `False`.
        """
