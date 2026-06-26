from ..image_utils import load_image as load_image
from ..models.auto.modeling_auto import MODEL_FOR_VISUAL_QUESTION_ANSWERING_MAPPING as MODEL_FOR_VISUAL_QUESTION_ANSWERING_MAPPING
from ..utils import add_end_docstrings as add_end_docstrings, is_torch_available as is_torch_available, is_vision_available as is_vision_available, logging as logging
from .base import PIPELINE_INIT_ARGS as PIPELINE_INIT_ARGS, Pipeline as Pipeline
from PIL import Image
from _typeshed import Incomplete
from typing import Union

logger: Incomplete

class VisualQuestionAnsweringPipeline(Pipeline):
    '''
    Visual Question Answering pipeline using a `AutoModelForVisualQuestionAnswering`. This pipeline is currently only
    available in PyTorch.

    Example:

    ```python
    >>> from transformers import pipeline

    >>> oracle = pipeline(model="dandelin/vilt-b32-finetuned-vqa")
    >>> image_url = "https://huggingface.co/datasets/Narsil/image_dummy/raw/main/lena.png"
    >>> oracle(question="What is she wearing ?", image=image_url)
    [{\'score\': 0.948, \'answer\': \'hat\'}, {\'score\': 0.009, \'answer\': \'fedora\'}, {\'score\': 0.003, \'answer\': \'clothes\'}, {\'score\': 0.003, \'answer\': \'sun hat\'}, {\'score\': 0.002, \'answer\': \'nothing\'}]

    >>> oracle(question="What is she wearing ?", image=image_url, top_k=1)
    [{\'score\': 0.948, \'answer\': \'hat\'}]

    >>> oracle(question="Is this a person ?", image=image_url, top_k=1)
    [{\'score\': 0.993, \'answer\': \'yes\'}]

    >>> oracle(question="Is this a man ?", image=image_url, top_k=1)
    [{\'score\': 0.996, \'answer\': \'no\'}]
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

    This visual question answering pipeline can currently be loaded from [`pipeline`] using the following task
    identifiers: `"visual-question-answering", "vqa"`.

    The models that this pipeline can use are models that have been fine-tuned on a visual question answering task. See
    the up-to-date list of available models on
    [huggingface.co/models](https://huggingface.co/models?filter=visual-question-answering).
    '''
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, image: Union['Image.Image', str], question: str = None, **kwargs):
        '''
        Answers open-ended questions about images. The pipeline accepts several types of inputs which are detailed
        below:

        - `pipeline(image=image, question=question)`
        - `pipeline({"image": image, "question": question})`
        - `pipeline([{"image": image, "question": question}])`
        - `pipeline([{"image": image, "question": question}, {"image": image, "question": question}])`

        Args:
            image (`str`, `List[str]`, `PIL.Image` or `List[PIL.Image]`):
                The pipeline handles three types of images:

                - A string containing a http link pointing to an image
                - A string containing a local path to an image
                - An image loaded in PIL directly

                The pipeline accepts either a single image or a batch of images. If given a single image, it can be
                broadcasted to multiple questions.
            question (`str`, `List[str]`):
                The question(s) asked. If given a single question, it can be broadcasted to multiple images.
            top_k (`int`, *optional*, defaults to 5):
                The number of top labels that will be returned by the pipeline. If the provided number is higher than
                the number of labels available in the model configuration, it will default to the number of labels.
        Return:
            A dictionary or a list of dictionaries containing the result. The dictionaries contain the following keys:

            - **label** (`str`) -- The label identified by the model.
            - **score** (`int`) -- The score attributed by the model for that label.
        '''
    def preprocess(self, inputs, padding: bool = False, truncation: bool = False): ...
    def postprocess(self, model_outputs, top_k: int = 5): ...
