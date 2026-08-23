from ...file_utils import TensorType as TensorType
from ...processing_utils import ProcessorMixin as ProcessorMixin
from ...tokenization_utils_base import BatchEncoding as BatchEncoding, PaddingStrategy as PaddingStrategy, TruncationStrategy as TruncationStrategy
from _typeshed import Incomplete
from typing import Optional, Union

class MarkupLMProcessor(ProcessorMixin):
    """
    Constructs a MarkupLM processor which combines a MarkupLM feature extractor and a MarkupLM tokenizer into a single
    processor.

    [`MarkupLMProcessor`] offers all the functionalities you need to prepare data for the model.

    It first uses [`MarkupLMFeatureExtractor`] to extract nodes and corresponding xpaths from one or more HTML strings.
    Next, these are provided to [`MarkupLMTokenizer`] or [`MarkupLMTokenizerFast`], which turns them into token-level
    `input_ids`, `attention_mask`, `token_type_ids`, `xpath_tags_seq` and `xpath_subs_seq`.

    Args:
        feature_extractor (`MarkupLMFeatureExtractor`):
            An instance of [`MarkupLMFeatureExtractor`]. The feature extractor is a required input.
        tokenizer (`MarkupLMTokenizer` or `MarkupLMTokenizerFast`):
            An instance of [`MarkupLMTokenizer`] or [`MarkupLMTokenizerFast`]. The tokenizer is a required input.
        parse_html (`bool`, *optional*, defaults to `True`):
            Whether or not to use `MarkupLMFeatureExtractor` to parse HTML strings into nodes and corresponding xpaths.
    """
    feature_extractor_class: str
    tokenizer_class: Incomplete
    parse_html: bool
    def __call__(self, html_strings: Incomplete | None = None, nodes: Incomplete | None = None, xpaths: Incomplete | None = None, node_labels: Incomplete | None = None, questions: Incomplete | None = None, add_special_tokens: bool = True, padding: Union[bool, str, PaddingStrategy] = False, truncation: Union[bool, str, TruncationStrategy] = None, max_length: Optional[int] = None, stride: int = 0, pad_to_multiple_of: Optional[int] = None, return_token_type_ids: Optional[bool] = None, return_attention_mask: Optional[bool] = None, return_overflowing_tokens: bool = False, return_special_tokens_mask: bool = False, return_offsets_mapping: bool = False, return_length: bool = False, verbose: bool = True, return_tensors: Optional[Union[str, TensorType]] = None, **kwargs) -> BatchEncoding:
        """
        This method first forwards the `html_strings` argument to [`~MarkupLMFeatureExtractor.__call__`]. Next, it
        passes the `nodes` and `xpaths` along with the additional arguments to [`~MarkupLMTokenizer.__call__`] and
        returns the output.

        Optionally, one can also provide a `text` argument which is passed along as first sequence.

        Please refer to the docstring of the above two methods for more information.
        """
    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to TrOCRTokenizer's [`~PreTrainedTokenizer.batch_decode`]. Please refer
        to the docstring of this method for more information.
        """
    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to TrOCRTokenizer's [`~PreTrainedTokenizer.decode`]. Please refer to the
        docstring of this method for more information.
        """
    @property
    def model_input_names(self): ...
