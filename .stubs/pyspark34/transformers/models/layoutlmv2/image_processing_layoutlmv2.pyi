import PIL
import numpy as np
from ...image_processing_utils import BaseImageProcessor as BaseImageProcessor, BatchFeature as BatchFeature, get_size_dict as get_size_dict
from ...image_transforms import resize as resize, to_channel_dimension_format as to_channel_dimension_format, to_pil_image as to_pil_image
from ...image_utils import ChannelDimension as ChannelDimension, ImageInput as ImageInput, PILImageResampling as PILImageResampling, infer_channel_dimension_format as infer_channel_dimension_format, is_batched as is_batched, to_numpy_array as to_numpy_array, valid_images as valid_images
from ...utils import is_pytesseract_available as is_pytesseract_available, logging as logging, requires_backends as requires_backends
from _typeshed import Incomplete
from transformers.utils import is_vision_available as is_vision_available
from transformers.utils.generic import TensorType as TensorType
from typing import Dict, Optional, Union

logger: Incomplete

def normalize_box(box, width, height): ...
def apply_tesseract(image: np.ndarray, lang: Optional[str], tesseract_config: Optional[str] = None):
    """Applies Tesseract OCR on a document image, and returns recognized words + normalized bounding boxes."""
def flip_channel_order(image: np.ndarray, data_format: Optional[ChannelDimension] = None) -> np.ndarray: ...

class LayoutLMv2ImageProcessor(BaseImageProcessor):
    '''
    Constructs a LayoutLMv2 image processor.

    Args:
        do_resize (`bool`, *optional*, defaults to `True`):
            Whether to resize the image\'s (height, width) dimensions to `(size["height"], size["width"])`. Can be
            overridden by `do_resize` in `preprocess`.
        size (`Dict[str, int]` *optional*, defaults to `{"height": 224, "width": 224}`):
            Size of the image after resizing. Can be overridden by `size` in `preprocess`.
        resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BILINEAR`):
            Resampling filter to use if resizing the image. Can be overridden by the `resample` parameter in the
            `preprocess` method.
        apply_ocr (`bool`, *optional*, defaults to `True`):
            Whether to apply the Tesseract OCR engine to get words + normalized bounding boxes. Can be overridden by
            `apply_ocr` in `preprocess`.
        ocr_lang (`str`, *optional*):
            The language, specified by its ISO code, to be used by the Tesseract OCR engine. By default, English is
            used. Can be overridden by `ocr_lang` in `preprocess`.
        tesseract_config (`str`, *optional*):
            Any additional custom configuration flags that are forwarded to the `config` parameter when calling
            Tesseract. For example: \'--psm 6\'. Can be overridden by `tesseract_config` in `preprocess`.
    '''
    model_input_names: Incomplete
    do_resize: Incomplete
    size: Incomplete
    resample: Incomplete
    apply_ocr: Incomplete
    ocr_lang: Incomplete
    tesseract_config: Incomplete
    def __init__(self, do_resize: bool = True, size: Dict[str, int] = None, resample: PILImageResampling = ..., apply_ocr: bool = True, ocr_lang: Optional[str] = None, tesseract_config: Optional[str] = '', **kwargs) -> None: ...
    def resize(self, image: np.ndarray, size: Dict[str, int], resample: PILImageResampling = ..., data_format: Optional[Union[str, ChannelDimension]] = None, **kwargs) -> np.ndarray:
        '''
        Resize an image to `(size["height"], size["width"])`.

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
    def preprocess(self, images: ImageInput, do_resize: bool = None, size: Dict[str, int] = None, resample: PILImageResampling = None, apply_ocr: bool = None, ocr_lang: Optional[str] = None, tesseract_config: Optional[str] = None, return_tensors: Optional[Union[str, TensorType]] = None, data_format: ChannelDimension = ..., **kwargs) -> PIL.Image.Image:
        """
        Preprocess an image or batch of images.

        Args:
            images (`ImageInput`):
                Image to preprocess.
            do_resize (`bool`, *optional*, defaults to `self.do_resize`):
                Whether to resize the image.
            size (`Dict[str, int]`, *optional*, defaults to `self.size`):
                Desired size of the output image after resizing.
            resample (`PILImageResampling`, *optional*, defaults to `self.resample`):
                Resampling filter to use if resizing the image. This can be one of the enum `PIL.Image` resampling
                filter. Only has an effect if `do_resize` is set to `True`.
            apply_ocr (`bool`, *optional*, defaults to `self.apply_ocr`):
                Whether to apply the Tesseract OCR engine to get words + normalized bounding boxes.
            ocr_lang (`str`, *optional*, defaults to `self.ocr_lang`):
                The language, specified by its ISO code, to be used by the Tesseract OCR engine. By default, English is
                used.
            tesseract_config (`str`, *optional*, defaults to `self.tesseract_config`):
                Any additional custom configuration flags that are forwarded to the `config` parameter when calling
                Tesseract.
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
