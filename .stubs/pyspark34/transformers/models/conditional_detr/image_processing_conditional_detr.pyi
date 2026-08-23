import numpy as np
import pathlib
from _typeshed import Incomplete
from transformers.feature_extraction_utils import BatchFeature as BatchFeature
from transformers.image_processing_utils import BaseImageProcessor as BaseImageProcessor, get_size_dict as get_size_dict
from transformers.image_transforms import PaddingMode as PaddingMode, center_to_corners_format as center_to_corners_format, corners_to_center_format as corners_to_center_format, id_to_rgb as id_to_rgb, normalize as normalize, pad as pad, rescale as rescale, resize as resize, rgb_to_id as rgb_to_id, to_channel_dimension_format as to_channel_dimension_format
from transformers.image_utils import ChannelDimension as ChannelDimension, IMAGENET_DEFAULT_MEAN as IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD as IMAGENET_DEFAULT_STD, ImageInput as ImageInput, PILImageResampling as PILImageResampling, get_image_size as get_image_size, infer_channel_dimension_format as infer_channel_dimension_format, is_batched as is_batched, to_numpy_array as to_numpy_array, valid_coco_detection_annotations as valid_coco_detection_annotations, valid_coco_panoptic_annotations as valid_coco_panoptic_annotations, valid_images as valid_images
from transformers.utils import is_flax_available as is_flax_available, is_jax_tensor as is_jax_tensor, is_scipy_available as is_scipy_available, is_tf_available as is_tf_available, is_tf_tensor as is_tf_tensor, is_torch_available as is_torch_available, is_torch_tensor as is_torch_tensor, is_vision_available as is_vision_available
from transformers.utils.generic import ExplicitEnum as ExplicitEnum, TensorType as TensorType
from typing import Any, Callable, Dict, Iterable, List, Optional, Set, Tuple, Union

class AnnotionFormat(ExplicitEnum):
    COCO_DETECTION: str
    COCO_PANOPTIC: str

SUPPORTED_ANNOTATION_FORMATS: Incomplete

def get_size_with_aspect_ratio(image_size, size, max_size: Incomplete | None = None) -> Tuple[int, int]:
    """
    Computes the output image size given the input image size and the desired output size.

    Args:
        image_size (`Tuple[int, int]`):
            The input image size.
        size (`int`):
            The desired output size.
        max_size (`int`, *optional*):
            The maximum allowed output size.
    """
def get_resize_output_image_size(input_image: np.ndarray, size: Union[int, Tuple[int, int], List[int]], max_size: Optional[int] = None) -> Tuple[int, int]:
    """
    Computes the output image size given the input image size and the desired output size. If the desired output size
    is a tuple or list, the output image size is returned as is. If the desired output size is an integer, the output
    image size is computed by keeping the aspect ratio of the input image size.

    Args:
        image_size (`Tuple[int, int]`):
            The input image size.
        size (`int`):
            The desired output size.
        max_size (`int`, *optional*):
            The maximum allowed output size.
    """
def get_numpy_to_framework_fn(arr) -> Callable:
    """
    Returns a function that converts a numpy array to the framework of the input array.

    Args:
        arr (`np.ndarray`): The array to convert.
    """
def safe_squeeze(arr: np.ndarray, axis: Optional[int] = None) -> np.ndarray:
    """
    Squeezes an array, but only if the axis specified has dim 1.
    """
def normalize_annotation(annotation: Dict, image_size: Tuple[int, int]) -> Dict: ...
def max_across_indices(values: Iterable[Any]) -> List[Any]:
    """
    Return the maximum value across all indices of an iterable of values.
    """
def get_max_height_width(images: List[np.ndarray]) -> List[int]:
    """
    Get the maximum height and width across all images in a batch.
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
def convert_coco_poly_to_mask(segmentations, height: int, width: int) -> np.ndarray:
    """
    Convert a COCO polygon annotation to a mask.

    Args:
        segmentations (`List[List[float]]`):
            List of polygons, each polygon represented by a list of x-y coordinates.
        height (`int`):
            Height of the mask.
        width (`int`):
            Width of the mask.
    """
def prepare_coco_detection_annotation(image, target, return_segmentation_masks: bool = False):
    """
    Convert the target in COCO format into the format expected by ConditionalDetr.
    """
def masks_to_boxes(masks: np.ndarray) -> np.ndarray:
    """
    Compute the bounding boxes around the provided panoptic segmentation masks.

    Args:
        masks: masks in format `[number_masks, height, width]` where N is the number of masks

    Returns:
        boxes: bounding boxes in format `[number_masks, 4]` in xyxy format
    """
def prepare_coco_panoptic_annotation(image: np.ndarray, target: Dict, masks_path: Union[str, pathlib.Path], return_masks: bool = True) -> Dict:
    """
    Prepare a coco panoptic annotation for ConditionalDetr.
    """
def get_segmentation_image(masks: np.ndarray, input_size: Tuple, target_size: Tuple, stuff_equiv_classes, deduplicate: bool = False): ...
def get_mask_area(seg_img: np.ndarray, target_size: Tuple[int, int], n_classes: int) -> np.ndarray: ...
def score_labels_from_class_probabilities(logits: np.ndarray) -> Tuple[np.ndarray, np.ndarray]: ...
def post_process_panoptic_sample(out_logits: np.ndarray, masks: np.ndarray, boxes: np.ndarray, processed_size: Tuple[int, int], target_size: Tuple[int, int], is_thing_map: Dict, threshold: float = 0.85) -> Dict:
    """
    Converts the output of [`ConditionalDetrForSegmentation`] into panoptic segmentation predictions for a single
    sample.

    Args:
        out_logits (`torch.Tensor`):
            The logits for this sample.
        masks (`torch.Tensor`):
            The predicted segmentation masks for this sample.
        boxes (`torch.Tensor`):
            The prediced bounding boxes for this sample. The boxes are in the normalized format `(center_x, center_y,
            width, height)` and values between `[0, 1]`, relative to the size the image (disregarding padding).
        processed_size (`Tuple[int, int]`):
            The processed size of the image `(height, width)`, as returned by the preprocessing step i.e. the size
            after data augmentation but before batching.
        target_size (`Tuple[int, int]`):
            The target size of the image, `(height, width)` corresponding to the requested final size of the
            prediction.
        is_thing_map (`Dict`):
            A dictionary mapping class indices to a boolean value indicating whether the class is a thing or not.
        threshold (`float`, *optional*, defaults to 0.85):
            The threshold used to binarize the segmentation masks.
    """
def resize_annotation(annotation: Dict[str, Any], orig_size: Tuple[int, int], target_size: Tuple[int, int], threshold: float = 0.5, resample: PILImageResampling = ...):
    """
    Resizes an annotation to a target size.

    Args:
        annotation (`Dict[str, Any]`):
            The annotation dictionary.
        orig_size (`Tuple[int, int]`):
            The original size of the input image.
        target_size (`Tuple[int, int]`):
            The target size of the image, as returned by the preprocessing `resize` step.
        threshold (`float`, *optional*, defaults to 0.5):
            The threshold used to binarize the segmentation masks.
        resample (`PILImageResampling`, defaults to `PILImageResampling.NEAREST`):
            The resampling filter to use when resizing the masks.
    """
def binary_mask_to_rle(mask):
    """
    Converts given binary mask of shape `(height, width)` to the run-length encoding (RLE) format.

    Args:
        mask (`torch.Tensor` or `numpy.array`):
            A binary mask tensor of shape `(height, width)` where 0 denotes background and 1 denotes the target
            segment_id or class_id.
    Returns:
        `List`: Run-length encoded list of the binary mask. Refer to COCO API for more information about the RLE
        format.
    """
def convert_segmentation_to_rle(segmentation):
    """
    Converts given segmentation map of shape `(height, width)` to the run-length encoding (RLE) format.

    Args:
        segmentation (`torch.Tensor` or `numpy.array`):
            A segmentation map of shape `(height, width)` where each value denotes a segment or class id.
    Returns:
        `List[List]`: A list of lists, where each list is the run-length encoding of a segment / class id.
    """
def remove_low_and_no_objects(masks, scores, labels, object_mask_threshold, num_labels):
    """
    Binarize the given masks using `object_mask_threshold`, it returns the associated values of `masks`, `scores` and
    `labels`.

    Args:
        masks (`torch.Tensor`):
            A tensor of shape `(num_queries, height, width)`.
        scores (`torch.Tensor`):
            A tensor of shape `(num_queries)`.
        labels (`torch.Tensor`):
            A tensor of shape `(num_queries)`.
        object_mask_threshold (`float`):
            A number between 0 and 1 used to binarize the masks.
    Raises:
        `ValueError`: Raised when the first dimension doesn't match in all input tensors.
    Returns:
        `Tuple[`torch.Tensor`, `torch.Tensor`, `torch.Tensor`]`: The `masks`, `scores` and `labels` without the region
        < `object_mask_threshold`.
    """
def check_segment_validity(mask_labels, mask_probs, k, mask_threshold: float = 0.5, overlap_mask_area_threshold: float = 0.8): ...
def compute_segments(mask_probs, pred_scores, pred_labels, mask_threshold: float = 0.5, overlap_mask_area_threshold: float = 0.8, label_ids_to_fuse: Optional[Set[int]] = None, target_size: Tuple[int, int] = None): ...

class ConditionalDetrImageProcessor(BaseImageProcessor):
    '''
    Constructs a Conditional Detr image processor.

    Args:
        format (`str`, *optional*, defaults to `"coco_detection"`):
            Data format of the annotations. One of "coco_detection" or "coco_panoptic".
        do_resize (`bool`, *optional*, defaults to `True`):
            Controls whether to resize the image\'s (height, width) dimensions to the specified `size`. Can be
            overridden by the `do_resize` parameter in the `preprocess` method.
        size (`Dict[str, int]` *optional*, defaults to `{"shortest_edge": 800, "longest_edge": 1333}`):
            Size of the image\'s (height, width) dimensions after resizing. Can be overridden by the `size` parameter in
            the `preprocess` method.
        resample (`PILImageResampling`, *optional*, defaults to `PILImageResampling.BILINEAR`):
            Resampling filter to use if resizing the image.
        do_rescale (`bool`, *optional*, defaults to `True`):
            Controls whether to rescale the image by the specified scale `rescale_factor`. Can be overridden by the
            `do_rescale` parameter in the `preprocess` method.
        rescale_factor (`int` or `float`, *optional*, defaults to `1/255`):
            Scale factor to use if rescaling the image. Can be overridden by the `rescale_factor` parameter in the
            `preprocess` method.
        do_normalize:
            Controls whether to normalize the image. Can be overridden by the `do_normalize` parameter in the
            `preprocess` method.
        image_mean (`float` or `List[float]`, *optional*, defaults to `IMAGENET_DEFAULT_MEAN`):
            Mean values to use when normalizing the image. Can be a single value or a list of values, one for each
            channel. Can be overridden by the `image_mean` parameter in the `preprocess` method.
        image_std (`float` or `List[float]`, *optional*, defaults to `IMAGENET_DEFAULT_STD`):
            Standard deviation values to use when normalizing the image. Can be a single value or a list of values, one
            for each channel. Can be overridden by the `image_std` parameter in the `preprocess` method.
        do_pad (`bool`, *optional*, defaults to `True`):
            Controls whether to pad the image to the largest image in a batch and create a pixel mask. Can be
            overridden by the `do_pad` parameter in the `preprocess` method.
    '''
    model_input_names: Incomplete
    format: Incomplete
    do_resize: Incomplete
    size: Incomplete
    resample: Incomplete
    do_rescale: Incomplete
    rescale_factor: Incomplete
    do_normalize: Incomplete
    image_mean: Incomplete
    image_std: Incomplete
    do_pad: Incomplete
    def __init__(self, format: Union[str, AnnotionFormat] = ..., do_resize: bool = True, size: Dict[str, int] = None, resample: PILImageResampling = ..., do_rescale: bool = True, rescale_factor: Union[int, float] = ..., do_normalize: bool = True, image_mean: Union[float, List[float]] = None, image_std: Union[float, List[float]] = None, do_pad: bool = True, **kwargs) -> None: ...
    @property
    def max_size(self): ...
    @classmethod
    def from_dict(cls, image_processor_dict: Dict[str, Any], **kwargs):
        """
        Overrides the `from_dict` method from the base class to make sure parameters are updated if image processor is
        created using from_dict and kwargs e.g. `ConditionalDetrImageProcessor.from_pretrained(checkpoint, size=600,
        max_size=800)`
        """
    def prepare_annotation(self, image: np.ndarray, target: Dict, format: Optional[AnnotionFormat] = None, return_segmentation_masks: bool = None, masks_path: Optional[Union[str, pathlib.Path]] = None) -> Dict:
        """
        Prepare an annotation for feeding into ConditionalDetr model.
        """
    def prepare(self, image, target, return_segmentation_masks: bool = False, masks_path: Incomplete | None = None): ...
    def convert_coco_poly_to_mask(self, *args, **kwargs): ...
    def prepare_coco_detection(self, *args, **kwargs): ...
    def prepare_coco_panoptic(self, *args, **kwargs): ...
    def resize(self, image: np.ndarray, size: Dict[str, int], resample: PILImageResampling = ..., data_format: Optional[ChannelDimension] = None, **kwargs) -> np.ndarray:
        """
        Resize the image to the given size. Size can be `min_size` (scalar) or `(height, width)` tuple. If size is an
        int, smaller edge of the image will be matched to this number.
        """
    def resize_annotation(self, annotation, orig_size, size, resample: PILImageResampling = ...) -> Dict:
        """
        Resize the annotation to match the resized image. If size is an int, smaller edge of the mask will be matched
        to this number.
        """
    def rescale(self, image: np.ndarray, rescale_factor: Union[float, int], data_format: Optional[ChannelDimension] = None) -> np.ndarray:
        """
        Rescale the image by the given factor.
        """
    def normalize(self, image: np.ndarray, mean: Union[float, Iterable[float]], std: Union[float, Iterable[float]], data_format: Optional[ChannelDimension] = None) -> np.ndarray:
        """
        Normalize the image with the given mean and standard deviation.
        """
    def normalize_annotation(self, annotation: Dict, image_size: Tuple[int, int]) -> Dict:
        """
        Normalize the boxes in the annotation from `[top_left_x, top_left_y, bottom_right_x, bottom_right_y]` to
        `[center_x, center_y, width, height]` format.
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
    def pad(self, images: List[np.ndarray], constant_values: Union[float, Iterable[float]] = 0, return_pixel_mask: bool = True, return_tensors: Optional[Union[str, TensorType]] = None, data_format: Optional[ChannelDimension] = None) -> np.ndarray:
        '''
        Pads a batch of images to the bottom and right of the image with zeros to the size of largest height and width
        in the batch and optionally returns their corresponding pixel mask.

        Args:
            image (`np.ndarray`):
                Image to pad.
            constant_values (`float` or `Iterable[float]`, *optional*):
                The value to use for the padding if `mode` is `"constant"`.
            return_pixel_mask (`bool`, *optional*, defaults to `True`):
                Whether to return a pixel mask.
            input_channel_dimension (`ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be inferred from the input image.
            data_format (`str` or `ChannelDimension`, *optional*):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
        '''
    def preprocess(self, images: ImageInput, annotations: Optional[Union[List[Dict], List[List[Dict]]]] = None, return_segmentation_masks: bool = None, masks_path: Optional[Union[str, pathlib.Path]] = None, do_resize: Optional[bool] = None, size: Optional[Dict[str, int]] = None, resample: Incomplete | None = None, do_rescale: Optional[bool] = None, rescale_factor: Optional[Union[int, float]] = None, do_normalize: Optional[bool] = None, image_mean: Optional[Union[float, List[float]]] = None, image_std: Optional[Union[float, List[float]]] = None, do_pad: Optional[bool] = None, format: Optional[Union[str, AnnotionFormat]] = None, return_tensors: Optional[Union[TensorType, str]] = None, data_format: Union[str, ChannelDimension] = ..., **kwargs) -> BatchFeature:
        '''
        Preprocess an image or a batch of images so that it can be used by the model.

        Args:
            images (`ImageInput`):
                Image or batch of images to preprocess.
            annotations (`List[Dict]` or `List[List[Dict]]`, *optional*):
                List of annotations associated with the image or batch of images. If annotionation is for object
                detection, the annotations should be a dictionary with the following keys:
                - "image_id" (`int`): The image id.
                - "annotations" (`List[Dict]`): List of annotations for an image. Each annotation should be a
                  dictionary. An image can have no annotations, in which case the list should be empty.
                If annotionation is for segmentation, the annotations should be a dictionary with the following keys:
                - "image_id" (`int`): The image id.
                - "segments_info" (`List[Dict]`): List of segments for an image. Each segment should be a dictionary.
                  An image can have no segments, in which case the list should be empty.
                - "file_name" (`str`): The file name of the image.
            return_segmentation_masks (`bool`, *optional*, defaults to self.return_segmentation_masks):
                Whether to return segmentation masks.
            masks_path (`str` or `pathlib.Path`, *optional*):
                Path to the directory containing the segmentation masks.
            do_resize (`bool`, *optional*, defaults to self.do_resize):
                Whether to resize the image.
            size (`Dict[str, int]`, *optional*, defaults to self.size):
                Size of the image after resizing.
            resample (`PILImageResampling`, *optional*, defaults to self.resample):
                Resampling filter to use when resizing the image.
            do_rescale (`bool`, *optional*, defaults to self.do_rescale):
                Whether to rescale the image.
            rescale_factor (`float`, *optional*, defaults to self.rescale_factor):
                Rescale factor to use when rescaling the image.
            do_normalize (`bool`, *optional*, defaults to self.do_normalize):
                Whether to normalize the image.
            image_mean (`float` or `List[float]`, *optional*, defaults to self.image_mean):
                Mean to use when normalizing the image.
            image_std (`float` or `List[float]`, *optional*, defaults to self.image_std):
                Standard deviation to use when normalizing the image.
            do_pad (`bool`, *optional*, defaults to self.do_pad):
                Whether to pad the image.
            format (`str` or `AnnotionFormat`, *optional*, defaults to self.format):
                Format of the annotations.
            return_tensors (`str` or `TensorType`, *optional*, defaults to self.return_tensors):
                Type of tensors to return. If `None`, will return the list of images.
            data_format (`str` or `ChannelDimension`, *optional*, defaults to self.data_format):
                The channel dimension format of the image. If not provided, it will be the same as the input image.
        '''
    def post_process(self, outputs, target_sizes):
        """
        Converts the output of [`ConditionalDetrForObjectDetection`] into the format expected by the COCO api. Only
        supports PyTorch.

        Args:
            outputs ([`ConditionalDetrObjectDetectionOutput`]):
                Raw outputs of the model.
            target_sizes (`torch.Tensor` of shape `(batch_size, 2)`):
                Tensor containing the size (h, w) of each image of the batch. For evaluation, this must be the original
                image size (before any data augmentation). For visualization, this should be the image size after data
                augment, but before padding.
        Returns:
            `List[Dict]`: A list of dictionaries, each dictionary containing the scores, labels and boxes for an image
            in the batch as predicted by the model.
        """
    def post_process_object_detection(self, outputs, threshold: float = 0.5, target_sizes: Union[TensorType, List[Tuple]] = None):
        """
        Converts the raw output of [`ConditionalDetrForObjectDetection`] into final bounding boxes in (top_left_x,
        top_left_y, bottom_right_x, bottom_right_y) format. Only supports PyTorch.

        Args:
            outputs ([`DetrObjectDetectionOutput`]):
                Raw outputs of the model.
            threshold (`float`, *optional*):
                Score threshold to keep object detection predictions.
            target_sizes (`torch.Tensor` or `List[Tuple[int, int]]`, *optional*):
                Tensor of shape `(batch_size, 2)` or list of tuples (`Tuple[int, int]`) containing the target size
                (height, width) of each image in the batch. If left to None, predictions will not be resized.

        Returns:
            `List[Dict]`: A list of dictionaries, each dictionary containing the scores, labels and boxes for an image
            in the batch as predicted by the model.
        """
    def post_process_semantic_segmentation(self, outputs, target_sizes: List[Tuple[int, int]] = None):
        """
        Converts the output of [`ConditionalDetrForSegmentation`] into semantic segmentation maps. Only supports
        PyTorch.

        Args:
            outputs ([`ConditionalDetrForSegmentation`]):
                Raw outputs of the model.
            target_sizes (`List[Tuple[int, int]]`, *optional*):
                A list of tuples (`Tuple[int, int]`) containing the target size (height, width) of each image in the
                batch. If unset, predictions will not be resized.
        Returns:
            `List[torch.Tensor]`:
                A list of length `batch_size`, where each item is a semantic segmentation map of shape (height, width)
                corresponding to the target_sizes entry (if `target_sizes` is specified). Each entry of each
                `torch.Tensor` correspond to a semantic class id.
        """
    def post_process_instance_segmentation(self, outputs, threshold: float = 0.5, mask_threshold: float = 0.5, overlap_mask_area_threshold: float = 0.8, target_sizes: Optional[List[Tuple[int, int]]] = None, return_coco_annotation: Optional[bool] = False) -> List[Dict]:
        """
        Converts the output of [`ConditionalDetrForSegmentation`] into instance segmentation predictions. Only supports
        PyTorch.

        Args:
            outputs ([`ConditionalDetrForSegmentation`]):
                Raw outputs of the model.
            threshold (`float`, *optional*, defaults to 0.5):
                The probability score threshold to keep predicted instance masks.
            mask_threshold (`float`, *optional*, defaults to 0.5):
                Threshold to use when turning the predicted masks into binary values.
            overlap_mask_area_threshold (`float`, *optional*, defaults to 0.8):
                The overlap mask area threshold to merge or discard small disconnected parts within each binary
                instance mask.
            target_sizes (`List[Tuple]`, *optional*):
                List of length (batch_size), where each list item (`Tuple[int, int]]`) corresponds to the requested
                final size (height, width) of each prediction. If unset, predictions will not be resized.
            return_coco_annotation (`bool`, *optional*):
                Defaults to `False`. If set to `True`, segmentation maps are returned in COCO run-length encoding (RLE)
                format.
        Returns:
            `List[Dict]`: A list of dictionaries, one per image, each dictionary containing two keys:
            - **segmentation** -- A tensor of shape `(height, width)` where each pixel represents a `segment_id` or
              `List[List]` run-length encoding (RLE) of the segmentation map if return_coco_annotation is set to
              `True`. Set to `None` if no mask if found above `threshold`.
            - **segments_info** -- A dictionary that contains additional information on each segment.
                - **id** -- An integer representing the `segment_id`.
                - **label_id** -- An integer representing the label / semantic class id corresponding to `segment_id`.
                - **score** -- Prediction score of segment with `segment_id`.
        """
    def post_process_panoptic_segmentation(self, outputs, threshold: float = 0.5, mask_threshold: float = 0.5, overlap_mask_area_threshold: float = 0.8, label_ids_to_fuse: Optional[Set[int]] = None, target_sizes: Optional[List[Tuple[int, int]]] = None) -> List[Dict]:
        """
        Converts the output of [`ConditionalDetrForSegmentation`] into image panoptic segmentation predictions. Only
        supports PyTorch.

        Args:
            outputs ([`ConditionalDetrForSegmentation`]):
                The outputs from [`ConditionalDetrForSegmentation`].
            threshold (`float`, *optional*, defaults to 0.5):
                The probability score threshold to keep predicted instance masks.
            mask_threshold (`float`, *optional*, defaults to 0.5):
                Threshold to use when turning the predicted masks into binary values.
            overlap_mask_area_threshold (`float`, *optional*, defaults to 0.8):
                The overlap mask area threshold to merge or discard small disconnected parts within each binary
                instance mask.
            label_ids_to_fuse (`Set[int]`, *optional*):
                The labels in this state will have all their instances be fused together. For instance we could say
                there can only be one sky in an image, but several persons, so the label ID for sky would be in that
                set, but not the one for person.
            target_sizes (`List[Tuple]`, *optional*):
                List of length (batch_size), where each list item (`Tuple[int, int]]`) corresponds to the requested
                final size (height, width) of each prediction in batch. If unset, predictions will not be resized.
        Returns:
            `List[Dict]`: A list of dictionaries, one per image, each dictionary containing two keys:
            - **segmentation** -- a tensor of shape `(height, width)` where each pixel represents a `segment_id` or
              `None` if no mask if found above `threshold`. If `target_sizes` is specified, segmentation is resized to
              the corresponding `target_sizes` entry.
            - **segments_info** -- A dictionary that contains additional information on each segment.
                - **id** -- an integer representing the `segment_id`.
                - **label_id** -- An integer representing the label / semantic class id corresponding to `segment_id`.
                - **was_fused** -- a boolean, `True` if `label_id` was in `label_ids_to_fuse`, `False` otherwise.
                  Multiple instances of the same class / label were fused and assigned a single `segment_id`.
                - **score** -- Prediction score of segment with `segment_id`.
        """
