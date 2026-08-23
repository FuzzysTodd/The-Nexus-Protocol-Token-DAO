from ..image_utils import load_image as load_image
from ..models.auto.modeling_auto import MODEL_FOR_DOCUMENT_QUESTION_ANSWERING_MAPPING as MODEL_FOR_DOCUMENT_QUESTION_ANSWERING_MAPPING
from ..utils import ExplicitEnum as ExplicitEnum, add_end_docstrings as add_end_docstrings, is_pytesseract_available as is_pytesseract_available, is_torch_available as is_torch_available, is_vision_available as is_vision_available, logging as logging
from .base import ChunkPipeline as ChunkPipeline, PIPELINE_INIT_ARGS as PIPELINE_INIT_ARGS
from .question_answering import select_starts_ends as select_starts_ends
from PIL import Image as Image
from _typeshed import Incomplete
from typing import List, Optional, Tuple, Union

TESSERACT_LOADED: bool
logger: Incomplete

def normalize_box(box, width, height): ...
def apply_tesseract(image: Image.Image, lang: Optional[str], tesseract_config: Optional[str]):
    """Applies Tesseract OCR on a document image, and returns recognized words + normalized bounding boxes."""

class ModelType(ExplicitEnum):
    LayoutLM: str
    LayoutLMv2andv3: str
    VisionEncoderDecoder: str

class DocumentQuestionAnsweringPipeline(ChunkPipeline):
    '''
    Document Question Answering pipeline using any `AutoModelForDocumentQuestionAnswering`. The inputs/outputs are
    similar to the (extractive) question answering pipeline; however, the pipeline takes an image (and optional OCR\'d
    words/boxes) as input instead of text context.

    Example:

    ```python
    >>> from transformers import pipeline

    >>> document_qa = pipeline(model="impira/layoutlm-document-qa")
    >>> document_qa(
    ...     image="https://huggingface.co/spaces/impira/docquery/resolve/2359223c1837a7587402bda0f2643382a6eefeab/invoice.png",
    ...     question="What is the invoice number?",
    ... )
    [{\'score\': 0.425, \'answer\': \'us-001\', \'start\': 16, \'end\': 16}]
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

    This document question answering pipeline can currently be loaded from [`pipeline`] using the following task
    identifier: `"document-question-answering"`.

    The models that this pipeline can use are models that have been fine-tuned on a document question answering task.
    See the up-to-date list of available models on
    [huggingface.co/models](https://huggingface.co/models?filter=document-question-answering).
    '''
    model_type: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, image: Union['Image.Image', str], question: Optional[str] = None, word_boxes: Tuple[str, List[float]] = None, **kwargs):
        '''
        Answer the question(s) given as inputs by using the document(s). A document is defined as an image and an
        optional list of (word, box) tuples which represent the text in the document. If the `word_boxes` are not
        provided, it will use the Tesseract OCR engine (if available) to extract the words and boxes automatically for
        LayoutLM-like models which require them as input. For Donut, no OCR is run.

        You can invoke the pipeline several ways:

        - `pipeline(image=image, question=question)`
        - `pipeline(image=image, question=question, word_boxes=word_boxes)`
        - `pipeline([{"image": image, "question": question}])`
        - `pipeline([{"image": image, "question": question, "word_boxes": word_boxes}])`

        Args:
            image (`str` or `PIL.Image`):
                The pipeline handles three types of images:

                - A string containing a http link pointing to an image
                - A string containing a local path to an image
                - An image loaded in PIL directly

                The pipeline accepts either a single image or a batch of images. If given a single image, it can be
                broadcasted to multiple questions.
            question (`str`):
                A question to ask of the document.
            word_boxes (`List[str, Tuple[float, float, float, float]]`, *optional*):
                A list of words and bounding boxes (normalized 0->1000). If you provide this optional input, then the
                pipeline will use these words and boxes instead of running OCR on the image to derive them for models
                that need them (e.g. LayoutLM). This allows you to reuse OCR\'d results across many invocations of the
                pipeline without having to re-run it each time.
            top_k (`int`, *optional*, defaults to 1):
                The number of answers to return (will be chosen by order of likelihood). Note that we return less than
                top_k answers if there are not enough options available within the context.
            doc_stride (`int`, *optional*, defaults to 128):
                If the words in the document are too long to fit with the question for the model, it will be split in
                several chunks with some overlap. This argument controls the size of that overlap.
            max_answer_len (`int`, *optional*, defaults to 15):
                The maximum length of predicted answers (e.g., only answers with a shorter length are considered).
            max_seq_len (`int`, *optional*, defaults to 384):
                The maximum length of the total sentence (context + question) in tokens of each chunk passed to the
                model. The context will be split in several chunks (using `doc_stride` as overlap) if needed.
            max_question_len (`int`, *optional*, defaults to 64):
                The maximum length of the question after tokenization. It will be truncated if needed.
            handle_impossible_answer (`bool`, *optional*, defaults to `False`):
                Whether or not we accept impossible as an answer.
            lang (`str`, *optional*):
                Language to use while running OCR. Defaults to english.
            tesseract_config (`str`, *optional*):
                Additional flags to pass to tesseract while running OCR.

        Return:
            A `dict` or a list of `dict`: Each result comes as a dictionary with the following keys:

            - **score** (`float`) -- The probability associated to the answer.
            - **start** (`int`) -- The start word index of the answer (in the OCR\'d version of the input or provided
              `word_boxes`).
            - **end** (`int`) -- The end word index of the answer (in the OCR\'d version of the input or provided
              `word_boxes`).
            - **answer** (`str`) -- The answer to the question.
            - **words** (`list[int]`) -- The index of each word/box pair that is in the answer
        '''
    def preprocess(self, input, padding: str = 'do_not_pad', doc_stride: Incomplete | None = None, max_seq_len: Incomplete | None = None, word_boxes: Tuple[str, List[float]] = None, lang: Incomplete | None = None, tesseract_config: str = ''): ...
    def postprocess(self, model_outputs, top_k: int = 1, **kwargs): ...
    def postprocess_encoder_decoder_single(self, model_outputs, **kwargs): ...
    def postprocess_extractive_qa(self, model_outputs, top_k: int = 1, handle_impossible_answer: bool = False, max_answer_len: int = 15, **kwargs): ...
