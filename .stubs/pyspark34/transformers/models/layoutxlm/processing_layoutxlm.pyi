from ...processing_utils import ProcessorMixin as ProcessorMixin
from ...tokenization_utils_base import BatchEncoding as BatchEncoding, PaddingStrategy as PaddingStrategy, PreTokenizedInput as PreTokenizedInput, TextInput as TextInput, TruncationStrategy as TruncationStrategy
from ...utils import TensorType as TensorType
from _typeshed import Incomplete
from typing import List, Optional, Union

class LayoutXLMProcessor(ProcessorMixin):
    """
    Constructs a LayoutXLM processor which combines a LayoutXLM feature extractor and a LayoutXLM tokenizer into a
    single processor.

    [`LayoutXLMProcessor`] offers all the functionalities you need to prepare data for the model.

    It first uses [`LayoutLMv2FeatureExtractor`] to resize document images to a fixed size, and optionally applies OCR
    to get words and normalized bounding boxes. These are then provided to [`LayoutXLMTokenizer`] or
    [`LayoutXLMTokenizerFast`], which turns the words and bounding boxes into token-level `input_ids`,
    `attention_mask`, `token_type_ids`, `bbox`. Optionally, one can provide integer `word_labels`, which are turned
    into token-level `labels` for token classification tasks (such as FUNSD, CORD).

    Args:
        feature_extractor (`LayoutLMv2FeatureExtractor`):
            An instance of [`LayoutLMv2FeatureExtractor`]. The feature extractor is a required input.
        tokenizer (`LayoutXLMTokenizer` or `LayoutXLMTokenizerFast`):
            An instance of [`LayoutXLMTokenizer`] or [`LayoutXLMTokenizerFast`]. The tokenizer is a required input.
    """
    feature_extractor_class: str
    tokenizer_class: Incomplete
    def __call__(self, images, text: Union[TextInput, PreTokenizedInput, List[TextInput], List[PreTokenizedInput]] = None, text_pair: Optional[Union[PreTokenizedInput, List[PreTokenizedInput]]] = None, boxes: Union[List[List[int]], List[List[List[int]]]] = None, word_labels: Optional[Union[List[int], List[List[int]]]] = None, add_special_tokens: bool = True, padding: Union[bool, str, PaddingStrategy] = False, truncation: Union[bool, str, TruncationStrategy] = None, max_length: Optional[int] = None, stride: int = 0, pad_to_multiple_of: Optional[int] = None, return_token_type_ids: Optional[bool] = None, return_attention_mask: Optional[bool] = None, return_overflowing_tokens: bool = False, return_special_tokens_mask: bool = False, return_offsets_mapping: bool = False, return_length: bool = False, verbose: bool = True, return_tensors: Optional[Union[str, TensorType]] = None, **kwargs) -> BatchEncoding:
        """
        This method first forwards the `images` argument to [`~LayoutLMv2FeatureExtractor.__call__`]. In case
        [`LayoutLMv2FeatureExtractor`] was initialized with `apply_ocr` set to `True`, it passes the obtained words and
        bounding boxes along with the additional arguments to [`~LayoutXLMTokenizer.__call__`] and returns the output,
        together with resized `images`. In case [`LayoutLMv2FeatureExtractor`] was initialized with `apply_ocr` set to
        `False`, it passes the words (`text`/``text_pair`) and `boxes` specified by the user along with the additional
        arguments to [`~LayoutXLMTokenizer.__call__`] and returns the output, together with resized `images``.

        Please refer to the docstring of the above two methods for more information.
        """
    def get_overflowing_images(self, images, overflow_to_sample_mapping): ...
    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to PreTrainedTokenizer's [`~PreTrainedTokenizer.batch_decode`]. Please
        refer to the docstring of this method for more information.
        """
    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to PreTrainedTokenizer's [`~PreTrainedTokenizer.decode`]. Please refer
        to the docstring of this method for more information.
        """
    @property
    def model_input_names(self): ...
