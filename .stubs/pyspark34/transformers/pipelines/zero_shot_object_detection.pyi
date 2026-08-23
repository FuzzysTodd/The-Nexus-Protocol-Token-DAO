from ..image_utils import load_image as load_image
from ..models.auto.modeling_auto import MODEL_FOR_ZERO_SHOT_OBJECT_DETECTION_MAPPING as MODEL_FOR_ZERO_SHOT_OBJECT_DETECTION_MAPPING
from ..utils import add_end_docstrings as add_end_docstrings, is_torch_available as is_torch_available, is_vision_available as is_vision_available, logging as logging, requires_backends as requires_backends
from .base import ChunkPipeline as ChunkPipeline, PIPELINE_INIT_ARGS as PIPELINE_INIT_ARGS
from PIL import Image
from _typeshed import Incomplete
from collections.abc import Generator
from transformers.modeling_outputs import BaseModelOutput as BaseModelOutput
from typing import Any, Dict, List, Union

logger: Incomplete

class ZeroShotObjectDetectionPipeline(ChunkPipeline):
    '''
    Zero shot object detection pipeline using `OwlViTForObjectDetection`. This pipeline predicts bounding boxes of
    objects when you provide an image and a set of `candidate_labels`.

    Example:

    ```python
    >>> from transformers import pipeline

    >>> detector = pipeline(model="google/owlvit-base-patch32", task="zero-shot-object-detection")
    >>> detector(
    ...     "http://images.cocodataset.org/val2017/000000039769.jpg",
    ...     candidate_labels=["cat", "couch"],
    ... )
    [{\'score\': 0.287, \'label\': \'cat\', \'box\': {\'xmin\': 324, \'ymin\': 20, \'xmax\': 640, \'ymax\': 373}}, {\'score\': 0.254, \'label\': \'cat\', \'box\': {\'xmin\': 1, \'ymin\': 55, \'xmax\': 315, \'ymax\': 472}}, {\'score\': 0.121, \'label\': \'couch\', \'box\': {\'xmin\': 4, \'ymin\': 0, \'xmax\': 642, \'ymax\': 476}}]

    >>> detector(
    ...     "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png",
    ...     candidate_labels=["head", "bird"],
    ... )
    [{\'score\': 0.119, \'label\': \'bird\', \'box\': {\'xmin\': 71, \'ymin\': 170, \'xmax\': 410, \'ymax\': 508}}]
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

    This object detection pipeline can currently be loaded from [`pipeline`] using the following task identifier:
    `"zero-shot-object-detection"`.

    See the list of available models on
    [huggingface.co/models](https://huggingface.co/models?filter=zero-shot-object-detection).
    '''
    def __init__(self, **kwargs) -> None: ...
    def __call__(self, image: Union[str, 'Image.Image', List[Dict[str, Any]]], candidate_labels: Union[str, List[str]] = None, **kwargs):
        '''
        Detect objects (bounding boxes & classes) in the image(s) passed as inputs.

        Args:
            image (`str`, `PIL.Image` or `List[Dict[str, Any]]`):
                The pipeline handles three types of images:

                - A string containing an http url pointing to an image
                - A string containing a local path to an image
                - An image loaded in PIL directly

                You can use this parameter to send directly a list of images, or a dataset or a generator like so:

                ```python
                >>> from transformers import pipeline

                >>> detector = pipeline(model="google/owlvit-base-patch32", task="zero-shot-object-detection")
                >>> detector(
                ...     [
                ...         {
                ...             "image": "http://images.cocodataset.org/val2017/000000039769.jpg",
                ...             "candidate_labels": ["cat", "couch"],
                ...         },
                ...         {
                ...             "image": "http://images.cocodataset.org/val2017/000000039769.jpg",
                ...             "candidate_labels": ["cat", "couch"],
                ...         },
                ...     ]
                ... )
                [[{\'score\': 0.287, \'label\': \'cat\', \'box\': {\'xmin\': 324, \'ymin\': 20, \'xmax\': 640, \'ymax\': 373}}, {\'score\': 0.25, \'label\': \'cat\', \'box\': {\'xmin\': 1, \'ymin\': 55, \'xmax\': 315, \'ymax\': 472}}, {\'score\': 0.121, \'label\': \'couch\', \'box\': {\'xmin\': 4, \'ymin\': 0, \'xmax\': 642, \'ymax\': 476}}], [{\'score\': 0.287, \'label\': \'cat\', \'box\': {\'xmin\': 324, \'ymin\': 20, \'xmax\': 640, \'ymax\': 373}}, {\'score\': 0.254, \'label\': \'cat\', \'box\': {\'xmin\': 1, \'ymin\': 55, \'xmax\': 315, \'ymax\': 472}}, {\'score\': 0.121, \'label\': \'couch\', \'box\': {\'xmin\': 4, \'ymin\': 0, \'xmax\': 642, \'ymax\': 476}}]]
                ```


            candidate_labels (`str` or `List[str]` or `List[List[str]]`):
                What the model should recognize in the image.

            threshold (`float`, *optional*, defaults to 0.1):
                The probability necessary to make a prediction.

            top_k (`int`, *optional*, defaults to None):
                The number of top predictions that will be returned by the pipeline. If the provided number is `None`
                or higher than the number of predictions available, it will default to the number of predictions.


        Return:
            A list of lists containing prediction results, one list per input image. Each list contains dictionaries
            with the following keys:

            - **label** (`str`) -- Text query corresponding to the found object.
            - **score** (`float`) -- Score corresponding to the object (between 0 and 1).
            - **box** (`Dict[str,int]`) -- Bounding box of the detected object in image\'s original size. It is a
              dictionary with `x_min`, `x_max`, `y_min`, `y_max` keys.
        '''
    def preprocess(self, inputs) -> Generator[Incomplete, None, None]: ...
    def postprocess(self, model_outputs, threshold: float = 0.1, top_k: Incomplete | None = None): ...
