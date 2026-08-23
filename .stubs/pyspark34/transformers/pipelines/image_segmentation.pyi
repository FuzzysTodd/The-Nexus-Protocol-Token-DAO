from ..image_utils import load_image as load_image
from ..models.auto.modeling_auto import MODEL_FOR_IMAGE_SEGMENTATION_MAPPING as MODEL_FOR_IMAGE_SEGMENTATION_MAPPING, MODEL_FOR_INSTANCE_SEGMENTATION_MAPPING as MODEL_FOR_INSTANCE_SEGMENTATION_MAPPING, MODEL_FOR_SEMANTIC_SEGMENTATION_MAPPING as MODEL_FOR_SEMANTIC_SEGMENTATION_MAPPING, MODEL_FOR_UNIVERSAL_SEGMENTATION_MAPPING as MODEL_FOR_UNIVERSAL_SEGMENTATION_MAPPING
from ..utils import add_end_docstrings as add_end_docstrings, is_torch_available as is_torch_available, is_vision_available as is_vision_available, logging as logging, requires_backends as requires_backends
from .base import PIPELINE_INIT_ARGS as PIPELINE_INIT_ARGS, Pipeline as Pipeline
from _typeshed import Incomplete
from typing import Any, Dict, List, Union

logger: Incomplete
Prediction = Dict[str, Any]
Predictions = List[Prediction]

class ImageSegmentationPipeline(Pipeline):
    '''
    Image segmentation pipeline using any `AutoModelForXXXSegmentation`. This pipeline predicts masks of objects and
    their classes.

    Example:

    ```python
    >>> from transformers import pipeline

    >>> segmenter = pipeline(model="facebook/detr-resnet-50-panoptic")
    >>> segments = segmenter("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png")
    >>> len(segments)
    2

    >>> segments[0]["label"]
    \'bird\'

    >>> segments[1]["label"]
    \'bird\'

    >>> type(segments[0]["mask"])  # This is a black and white mask showing where is the bird on the original image.
    <class \'PIL.Image.Image\'>

    >>> segments[0]["mask"].size
    (768, 512)
    ```


    This image segmentation pipeline can currently be loaded from [`pipeline`] using the following task identifier:
    `"image-segmentation"`.

    See the list of available models on
    [huggingface.co/models](https://huggingface.co/models?filter=image-segmentation).
    '''
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, images, **kwargs) -> Union[Predictions, List[Prediction]]:
        '''
        Perform segmentation (detect masks & classes) in the image(s) passed as inputs.

        Args:
            images (`str`, `List[str]`, `PIL.Image` or `List[PIL.Image]`):
                The pipeline handles three types of images:

                - A string containing an HTTP(S) link pointing to an image
                - A string containing a local path to an image
                - An image loaded in PIL directly

                The pipeline accepts either a single image or a batch of images. Images in a batch must all be in the
                same format: all as HTTP(S) links, all as local paths, or all as PIL images.
            subtask (`str`, *optional*):
                Segmentation task to be performed, choose [`semantic`, `instance` and `panoptic`] depending on model
                capabilities. If not set, the pipeline will attempt tp resolve in the following order:
                  `panoptic`, `instance`, `semantic`.
            threshold (`float`, *optional*, defaults to 0.9):
                Probability threshold to filter out predicted masks.
            mask_threshold (`float`, *optional*, defaults to 0.5):
                Threshold to use when turning the predicted masks into binary values.
            overlap_mask_area_threshold (`float`, *optional*, defaults to 0.5):
                Mask overlap threshold to eliminate small, disconnected segments.

        Return:
            A dictionary or a list of dictionaries containing the result. If the input is a single image, will return a
            list of dictionaries, if the input is a list of several images, will return a list of list of dictionaries
            corresponding to each image.

            The dictionaries contain the mask, label and score (where applicable) of each detected object and contains
            the following keys:

            - **label** (`str`) -- The class label identified by the model.
            - **mask** (`PIL.Image`) -- A binary mask of the detected object as a Pil Image of shape (width, height) of
              the original image. Returns a mask filled with zeros if no object is found.
            - **score** (*optional* `float`) -- Optionally, when the model is capable of estimating a confidence of the
              "object" described by the label and the mask.
        '''
    def preprocess(self, image): ...
    def postprocess(self, model_outputs, subtask: Incomplete | None = None, threshold: float = 0.9, mask_threshold: float = 0.5, overlap_mask_area_threshold: float = 0.5): ...
