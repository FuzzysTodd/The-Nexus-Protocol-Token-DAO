import PIL
import numpy as np
from ...image_processing_utils import BaseImageProcessor as BaseImageProcessor, BatchFeature as BatchFeature, get_size_dict as get_size_dict
from ...image_transforms import center_crop as center_crop, normalize as normalize, rescale as rescale, resize as resize, to_channel_dimension_format as to_channel_dimension_format
from ...image_utils import ChannelDimension as ChannelDimension, ImageInput as ImageInput, PILImageResampling as PILImageResampling, is_batched as is_batched, to_numpy_array as to_numpy_array, valid_images as valid_images
from ...utils import logging as logging
from _typeshed import Incomplete
from transformers.utils import is_vision_available as is_vision_available
from transformers.utils.generic import TensorType as TensorType
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

logger: Incomplete
FLAVA_IMAGE_MEAN: Incomplete
FLAVA_IMAGE_STD: Incomplete
FLAVA_CODEBOOK_MEAN: Incomplete
FLAVA_CODEBOOK_STD: Incomplete
LOGIT_LAPLACE_EPS: float

class FlavaMaskingGenerator:
    num_patches: Incomplete
    total_mask_patches: Incomplete
    mask_group_min_patches: Incomplete
    mask_group_max_patches: Incomplete
    log_aspect_ratio: Incomplete
    def __init__(self, input_size: Union[int, Tuple[int, int]] = 14, total_mask_patches: int = 75, mask_group_max_patches: Optional[int] = None, mask_group_min_patches: int = 16, mask_group_min_aspect_ratio: Optional[float] = 0.3, mask_group_max_aspect_ratio: float = None) -> None: ...
    def get_shape(self): ...
    def __call__(self): ...

class FlavaImageProcessor(BaseImageProcessor):
    '''
    Constructs a Flava image processor.

    Args:
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the image\'s (height, width) dimensions to the specified `size`. Can be overridden by the
            `do_resize` parameter in `preprocess`.
        size (`Dict[str, int]` *optional*, defaults to `{"height": 224, "width": 224}`):
            Size of the image after resizing. Can be overridden by the `size` parameter in `preprocess`.
        resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BICUBIC`):
            Resampling filter to use if resizing the image. Can be overridden by the `resample` parameter in
            `preprocess`.
        do_center_crop (`bool`, *optional*, defaults to `True`):
            Whether to center crop the images. Can be overridden by the `do_center_crop` parameter in `preprocess`.
        crop_size (`Dict[str, int]` *optional*, defaults to `{"height": 224, "width": 224}`):
            Size of image after the center crop `(crop_size["height"], crop_size["width"])`. Can be overridden by the
            `crop_size` parameter in `preprocess`.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the `do_rescale`
            parameter in `preprocess`.
        rescale_factor (`int` or `float`, *optional*, defaults to `1/255`):
            Scale factor to use if rescaling the image. Can be overridden by the `rescale_factor` parameter in
            `preprocess`.
        do_normalize (`bool`, *optional*, defaults to `True`):
            Whether to normalize the image. Can be overridden by the `do_normalize` parameter in `preprocess`.
        image_mean (`float` or `List[float]`, *optional*, defaults to `IMAGENET_STANDARD_MEAN`):
            Mean to use if normalizing the image. This is a float or list of floats the length of the number of
            channels in the image. Can be overridden by the `image_mean` parameter in the `preprocess` method.
        image_std (`float` or `List[float]`, *optional*, defaults to `IMAGENET_STANDARD_STD`):
            Standard deviation to use if normalizing the image. This is a float or list of floats the length of the
            number of channels in the image. Can be overridden by the `image_std` parameter in the `preprocess` method.
        return_image_mask (`bool`, *optional*, defaults to `False`):
            Whether to return the image mask. Can be overridden by the `return_image_mask` parameter in `preprocess`.
        input_size_patches (`int`, *optional*, defaults to 14):
            Number of patches in the image in height and width direction. 14x14 = 196 total patches. Can be overridden
            by the `input_size_patches` parameter in `preprocess`.
        total_mask_patches (`int`, *optional*, defaults to 75):
            Total number of patches that should be masked. Can be overridden by the `total_mask_patches` parameter in
            `preprocess`.
        mask_group_min_patches (`int`, *optional*, defaults to 16):
            Minimum number of patches that should be masked. Can be overridden by the `mask_group_min_patches`
            parameter in `preprocess`.
        mask_group_max_patches (`int`, *optional*):
            Maximum number of patches that should be masked. Can be overridden by the `mask_group_max_patches`
            parameter in `preprocess`.
        mask_group_min_aspect_ratio (`float`, *optional*, defaults to 0.3):
            Minimum aspect ratio of the mask window. Can be overridden by the `mask_group_min_aspect_ratio` parameter
            in `preprocess`.
        mask_group_max_aspect_ratio (`float`, *optional*):
            Maximum aspect ratio of the mask window. Can be overridden by the `mask_group_max_aspect_ratio` parameter
            in `preprocess`.
        codebook_do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the input for codebook to a certain. Can be overridden by the `codebook_do_resize`
            parameter in `preprocess`. `codebook_size`.
        codebook_size (`Dict[str, int]`, *optional*, defaults to `{"height": 224, "width": 224}`):
            Resize the input for codebook to the given size. Can be overridden by the `codebook_size` parameter in
            `preprocess`.
        codebook_resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.LANCZOS`):
            Resampling filter to use if resizing the codebook image. Can be overridden by the `codebook_resample`
            parameter in `preprocess`.
        codebook_do_center_crop (`bool`, *optional*, defaults to `True`):
            Whether to crop the input for codebook at the center. If the input size is smaller than
            `codebook_crop_size` along any edge, the image is padded with 0\'s and then center cropped. Can be
            overridden by the `codebook_do_center_crop` parameter in `preprocess`.
        codebook_crop_size (`Dict[str, int]`, *optional*, defaults to `{"height": 224, "width": 224}`):
            Desired output size for codebook input when applying center-cropping. Can be overridden by the
            `codebook_crop_size` parameter in `preprocess`.
        codebook_do_rescale (`bool`, *optional*, defaults to `True`):
            Whether to rescale the input for codebook by the specified scale `codebook_rescale_factor`. Can be
            overridden by the `codebook_do_rescale` parameter in `preprocess`.
        codebook_rescale_factor (`int` or `float`, *optional*, defaults to `1/255`):
            Defines the scale factor to use if rescaling the codebook image. Can be overridden by the
            `codebook_rescale_factor` parameter in `preprocess`.
        codebook_do_map_pixels (`bool`, *optional*, defaults to `True`):
            Whether to map the pixel values of the codebook input to (1 - 2e)x + e. Can be overridden by the
            `codebook_do_map_pixels` parameter in `preprocess`.
        codebook_do_normalize (`bool`, *optional*, defaults to `True`):
            Whether or not to normalize the input for codebook with `codebook_image_mean` and `codebook_image_std`. Can
            be overridden by the `codebook_do_normalize` parameter in `preprocess`.
        codebook_image_mean (`Optional[Union[float, Iterable[float]]]`, *optional*, defaults to `[0, 0, 0]`):
            The sequence of means for each channel, to be used when normalizing images for codebook. Can be overridden
            by the `codebook_image_mean` parameter in `preprocess`.
        codebook_image_std (`Optional[Union[float, Iterable[float]]]`, *optional*, defaults to `[0.5, 0.5, 0.5]`):
            The sequence of standard deviations for each channel, to be used when normalizing images for codebook. Can
            be overridden by the `codebook_image_std` parameter in `preprocess`.
    '''
    model_input_names: Incomplete
    do_resize: Incomplete
    size: Incomplete
    resample: Incomplete
    do_rescale: Incomplete
    rescale_factor: Incomplete
    do_center_crop: Incomplete
    crop_size: Incomplete
    do_normalize: Incomplete
    image_mean: Incomplete
    image_std: Incomplete
    return_image_mask: Incomplete
    input_size_patches: Incomplete
    total_mask_patches: Incomplete
    mask_group_min_patches: Incomplete
    mask_group_max_patches: Incomplete
    mask_group_min_aspect_ratio: Incomplete
    mask_group_max_aspect_ratio: Incomplete
    return_codebook_pixels: Incomplete
    codebook_do_resize: Incomplete
    codebook_size: Incomplete
    codebook_resample: Incomplete
    codebook_do_center_crop: Incomplete
    codebook_crop_size: Incomplete
    codebook_do_rescale: Incomplete
    codebook_rescale_factor: Incomplete
    codebook_do_map_pixels: Incomplete
    codebook_do_normalize: Incomplete
    codebook_image_mean: Incomplete
    codebook_image_std: Incomplete
    def __init__(self, do_resize: bool = True, size: Dict[str, int] = None, resample: PILImageResampling = ..., do_center_crop: bool = True, crop_size: Dict[str, int] = None, do_rescale: bool = True, rescale_factor: Union[int, float] = ..., do_normalize: bool = True, image_mean: Optional[Union[float, Iterable[float]]] = None, image_std: Optional[Union[float, Iterable[float]]] = None, return_image_mask: bool = False, input_size_patches: int = 14, total_mask_patches: int = 75, mask_group_min_patches: int = 16, mask_group_max_patches: Optional[int] = None, mask_group_min_aspect_ratio: float = 0.3, mask_group_max_aspect_ratio: Optional[float] = None, return_codebook_pixels: bool = False, codebook_do_resize: bool = True, codebook_size: bool = None, codebook_resample: int = ..., codebook_do_center_crop: bool = True, codebook_crop_size: int = None, codebook_do_rescale: bool = True, codebook_rescale_factor: Union[int, float] = ..., codebook_do_map_pixels: bool = True, codebook_do_normalize: bool = True, codebook_image_mean: Optional[Union[float, Iterable[float]]] = None, codebook_image_std: Optional[Union[float, Iterable[float]]] = None, **kwargs) -> None: ...
    @classmethod
    def from_dict(cls, image_processor_dict: Dict[str, Any], **kwargs):
        """
        Overrides the `from_dict` method from the base class to make sure parameters are updated if image processor is
        created using from_dict and kwargs e.g. `FlavaImageProcessor.from_pretrained(checkpoint, codebook_size=600)`
        """
    def masking_generator(self, input_size_patches, total_mask_patches, mask_group_min_patches, mask_group_max_patches, mask_group_min_aspect_ratio, mask_group_max_aspect_ratio) -> FlavaMaskingGenerator: ...
    def resize(self, image: np.ndarray, size: Dict[str, int], resample: PILImageResampling = ..., data_format: Optional[Union[str, ChannelDimension]] = None, **kwargs) -> np.ndarray:
        '''
        Resize an image to `(size["height"], size["width"])`.

        Args:
            image (`np.ndarray`):
                Image to resize.
            size (`Dict[str, int]`):
                Size of the output image.
            resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BICUBIC`):
                Resampling filter to use when resiizing the image.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
        '''
    def center_crop(self, image: np.ndarray, size: Dict[str, int], data_format: Optional[Union[str, ChannelDimension]] = None, **kwargs) -> np.ndarray:
        '''
        Center crop an image to `(size["height"], size["width"])`. If the input size is smaller than `crop_size` along
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
    def map_pixels(self, image: np.ndarray) -> np.ndarray: ...
    def preprocess(self, images: ImageInput, do_resize: Optional[bool] = None, size: Dict[str, int] = None, resample: PILImageResampling = None, do_center_crop: Optional[bool] = None, crop_size: Optional[Dict[str, int]] = None, do_rescale: Optional[bool] = None, rescale_factor: Optional[float] = None, do_normalize: Optional[bool] = None, image_mean: Optional[Union[float, List[float]]] = None, image_std: Optional[Union[float, List[float]]] = None, return_image_mask: Optional[bool] = None, input_size_patches: Optional[int] = None, total_mask_patches: Optional[int] = None, mask_group_min_patches: Optional[int] = None, mask_group_max_patches: Optional[int] = None, mask_group_min_aspect_ratio: Optional[float] = None, mask_group_max_aspect_ratio: Optional[float] = None, return_codebook_pixels: Optional[bool] = None, codebook_do_resize: Optional[bool] = None, codebook_size: Optional[Dict[str, int]] = None, codebook_resample: Optional[int] = None, codebook_do_center_crop: Optional[bool] = None, codebook_crop_size: Optional[Dict[str, int]] = None, codebook_do_rescale: Optional[bool] = None, codebook_rescale_factor: Optional[float] = None, codebook_do_map_pixels: Optional[bool] = None, codebook_do_normalize: Optional[bool] = None, codebook_image_mean: Optional[Iterable[float]] = None, codebook_image_std: Optional[Iterable[float]] = None, return_tensors: Optional[Union[str, TensorType]] = None, data_format: ChannelDimension = ..., **kwargs) -> PIL.Image.Image:
        """
        Preprocess an image or batch of images.

        Args:
            images (`ImageInput`):
                Image to preprocess.
            do_resize (`bool`, *optional*, defaults to `self.do_resize`):
                Whether to resize the image.
            size (`Dict[str, int]`, *optional*, defaults to `self.size`):
                Size of the image.
            resample (`int`, *optional*, defaults to `self.resample`):
                Resampling filter to use if resizing the image. This can be one of the enum `PILImageResampling`, Only
                has an effect if `do_resize` is set to `True`.
            do_center_crop (`bool`, *optional*, defaults to `self.do_center_crop`):
                Whether to center crop the image.
            crop_size (`Dict[str, int]`, *optional*, defaults to `self.crop_size`):
                Size of the center crop. Only has an effect if `do_center_crop` is set to `True`.
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
            return_image_mask (`bool`, *optional*, defaults to `self.return_image_mask`):
                Whether to return the image mask.
            input_size_patches (`int`, *optional*, defaults to `self.input_size_patches`):
                Size of the patches to extract from the image.
            total_mask_patches (`int`, *optional*, defaults to `self.total_mask_patches`):
                Total number of patches to extract from the image.
            mask_group_min_patches (`int`, *optional*, defaults to `self.mask_group_min_patches`):
                Minimum number of patches to extract from the image.
            mask_group_max_patches (`int`, *optional*, defaults to `self.mask_group_max_patches`):
                Maximum number of patches to extract from the image.
            mask_group_min_aspect_ratio (`float`, *optional*, defaults to `self.mask_group_min_aspect_ratio`):
                Minimum aspect ratio of the patches to extract from the image.
            mask_group_max_aspect_ratio (`float`, *optional*, defaults to `self.mask_group_max_aspect_ratio`):
                Maximum aspect ratio of the patches to extract from the image.
            return_codebook_pixels (`bool`, *optional*, defaults to `self.return_codebook_pixels`):
                Whether to return the codebook pixels.
            codebook_do_resize (`bool`, *optional*, defaults to `self.codebook_do_resize`):
                Whether to resize the codebook pixels.
            codebook_size (`Dict[str, int]`, *optional*, defaults to `self.codebook_size`):
                Size of the codebook pixels.
            codebook_resample (`int`, *optional*, defaults to `self.codebook_resample`):
                Resampling filter to use if resizing the codebook pixels. This can be one of the enum
                `PILImageResampling`, Only has an effect if `codebook_do_resize` is set to `True`.
            codebook_do_center_crop (`bool`, *optional*, defaults to `self.codebook_do_center_crop`):
                Whether to center crop the codebook pixels.
            codebook_crop_size (`Dict[str, int]`, *optional*, defaults to `self.codebook_crop_size`):
                Size of the center crop of the codebook pixels. Only has an effect if `codebook_do_center_crop` is set
                to `True`.
            codebook_do_rescale (`bool`, *optional*, defaults to `self.codebook_do_rescale`):
                Whether to rescale the codebook pixels values between [0 - 1].
            codebook_rescale_factor (`float`, *optional*, defaults to `self.codebook_rescale_factor`):
                Rescale factor to rescale the codebook pixels by if `codebook_do_rescale` is set to `True`.
            codebook_do_map_pixels (`bool`, *optional*, defaults to `self.codebook_do_map_pixels`):
                Whether to map the codebook pixels values.
            codebook_do_normalize (`bool`, *optional*, defaults to `self.codebook_do_normalize`):
                Whether to normalize the codebook pixels.
            codebook_image_mean (`float` or `List[float]`, *optional*, defaults to `self.codebook_image_mean`):
                Codebook pixels mean to normalize the codebook pixels by if `codebook_do_normalize` is set to `True`.
            codebook_image_std (`float` or `List[float]`, *optional*, defaults to `self.codebook_image_std`):
                Codebook pixels standard deviation to normalize the codebook pixels by if `codebook_do_normalize` is
                set to `True`.
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
