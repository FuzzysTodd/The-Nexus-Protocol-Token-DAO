from ..image_utils import load_image as load_image
from ..models.auto.modeling_auto import MODEL_FOR_OBJECT_DETECTION_MAPPING as MODEL_FOR_OBJECT_DETECTION_MAPPING, MODEL_FOR_TOKEN_CLASSIFICATION_MAPPING as MODEL_FOR_TOKEN_CLASSIFICATION_MAPPING
from ..utils import add_end_docstrings as add_end_docstrings, is_torch_available as is_torch_available, is_vision_available as is_vision_available, logging as logging, requires_backends as requires_backends
from .base import PIPELINE_INIT_ARGS as PIPELINE_INIT_ARGS, Pipeline as Pipeline
from _typeshed import Incomplete
from typing import Any, Dict, List, Union

logger: Incomplete
Prediction = Dict[str, Any]
Predictions = List[Prediction]

class ObjectDetectionPipeline(Pipeline):
    '''
    Object detection pipeline using any `AutoModelForObjectDetection`. This pipeline predicts bounding boxes of objects
    and their classes.

    Example:

    ```python
    >>> from transformers import pipeline

    >>> detector = pipeline(model="facebook/detr-resnet-50")
    >>> detector("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png")
    [{\'score\': 0.997, \'label\': \'bird\', \'box\': {\'xmin\': 69, \'ymin\': 171, \'xmax\': 396, \'ymax\': 507}}, {\'score\': 0.999, \'label\': \'bird\', \'box\': {\'xmin\': 398, \'ymin\': 105, \'xmax\': 767, \'ymax\': 507}}]

    >>> # x, y  are expressed relative to the top left hand corner.
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

    This object detection pipeline can currently be loaded from [`pipeline`] using the following task identifier:
    `"object-detection"`.

    See the list of available models on [huggingface.co/models](https://huggingface.co/models?filter=object-detection).
    '''
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, *args, **kwargs) -> Union[Predictions, List[Prediction]]:
        """
        Detect objects (bounding boxes & classes) in the image(s) passed as inputs.

        Args:
            images (`str`, `List[str]`, `PIL.Image` or `List[PIL.Image]`):
                The pipeline handles three types of images:

                - A string containing an HTTP(S) link pointing to an image
                - A string containing a local path to an image
                - An image loaded in PIL directly

                The pipeline accepts either a single image or a batch of images. Images in a batch must all be in the
                same format: all as HTTP(S) links, all as local paths, or all as PIL images.
            threshold (`float`, *optional*, defaults to 0.9):
                The probability necessary to make a prediction.

        Return:
            A list of dictionaries or a list of list of dictionaries containing the result. If the input is a single
            image, will return a list of dictionaries, if the input is a list of several images, will return a list of
            list of dictionaries corresponding to each image.

            The dictionaries contain the following keys:

            - **label** (`str`) -- The class label identified by the model.
            - **score** (`float`) -- The score attributed by the model for that label.
            - **box** (`List[Dict[str, int]]`) -- The bounding box of detected object in image's original size.
        """
    def preprocess(self, image): ...
    def postprocess(self, model_outputs, threshold: float = 0.9): ...
