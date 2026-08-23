from ..image_utils import load_image as load_image
from ..models.auto.modeling_auto import MODEL_FOR_IMAGE_CLASSIFICATION_MAPPING as MODEL_FOR_IMAGE_CLASSIFICATION_MAPPING
from ..models.auto.modeling_tf_auto import TF_MODEL_FOR_IMAGE_CLASSIFICATION_MAPPING as TF_MODEL_FOR_IMAGE_CLASSIFICATION_MAPPING
from ..tf_utils import stable_softmax as stable_softmax
from ..utils import add_end_docstrings as add_end_docstrings, is_tf_available as is_tf_available, is_torch_available as is_torch_available, is_vision_available as is_vision_available, logging as logging, requires_backends as requires_backends
from .base import PIPELINE_INIT_ARGS as PIPELINE_INIT_ARGS, Pipeline as Pipeline
from PIL import Image as Image
from _typeshed import Incomplete
from typing import List, Union

logger: Incomplete

class ImageClassificationPipeline(Pipeline):
    '''
    Image classification pipeline using any `AutoModelForImageClassification`. This pipeline predicts the class of an
    image.

    Example:

    ```python
    >>> from transformers import pipeline

    >>> classifier = pipeline(model="microsoft/beit-base-patch16-224-pt22k-ft22k")
    >>> classifier("https://huggingface.co/datasets/Narsil/image_dummy/raw/main/parrots.png")
    [{\'score\': 0.442, \'label\': \'macaw\'}, {\'score\': 0.088, \'label\': \'popinjay\'}, {\'score\': 0.075, \'label\': \'parrot\'}, {\'score\': 0.073, \'label\': \'parodist, lampooner\'}, {\'score\': 0.046, \'label\': \'poll, poll_parrot\'}]
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

    This image classification pipeline can currently be loaded from [`pipeline`] using the following task identifier:
    `"image-classification"`.

    See the list of available models on
    [huggingface.co/models](https://huggingface.co/models?filter=image-classification).
    '''
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, images: Union[str, List[str], 'Image.Image', List['Image.Image']], **kwargs):
        """
        Assign labels to the image(s) passed as inputs.

        Args:
            images (`str`, `List[str]`, `PIL.Image` or `List[PIL.Image]`):
                The pipeline handles three types of images:

                - A string containing a http link pointing to an image
                - A string containing a local path to an image
                - An image loaded in PIL directly

                The pipeline accepts either a single image or a batch of images, which must then be passed as a string.
                Images in a batch must all be in the same format: all as http links, all as local paths, or all as PIL
                images.
            top_k (`int`, *optional*, defaults to 5):
                The number of top labels that will be returned by the pipeline. If the provided number is higher than
                the number of labels available in the model configuration, it will default to the number of labels.

        Return:
            A dictionary or a list of dictionaries containing result. If the input is a single image, will return a
            dictionary, if the input is a list of several images, will return a list of dictionaries corresponding to
            the images.

            The dictionaries contain the following keys:

            - **label** (`str`) -- The label identified by the model.
            - **score** (`int`) -- The score attributed by the model for that label.
        """
    def preprocess(self, image): ...
    def postprocess(self, model_outputs, top_k: int = 5): ...
