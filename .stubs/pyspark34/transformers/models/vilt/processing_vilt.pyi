from ...processing_utils import ProcessorMixin as ProcessorMixin
from ...tokenization_utils_base import BatchEncoding as BatchEncoding, PaddingStrategy as PaddingStrategy, PreTokenizedInput as PreTokenizedInput, TextInput as TextInput, TruncationStrategy as TruncationStrategy
from ...utils import TensorType as TensorType
from _typeshed import Incomplete
from typing import List, Optional, Union

class ViltProcessor(ProcessorMixin):
    """
    Constructs a ViLT processor which wraps a BERT tokenizer and ViLT image processor into a single processor.

    [`ViltProcessor`] offers all the functionalities of [`ViltImageProcessor`] and [`BertTokenizerFast`]. See the
    docstring of [`~ViltProcessor.__call__`] and [`~ViltProcessor.decode`] for more information.

    Args:
        image_processor (`ViltImageProcessor`):
            An instance of [`ViltImageProcessor`]. The image processor is a required input.
        tokenizer (`BertTokenizerFast`):
            An instance of ['BertTokenizerFast`]. The tokenizer is a required input.
    """
    attributes: Incomplete
    image_processor_class: str
    tokenizer_class: Incomplete
    current_processor: Incomplete
    def __init__(self, image_processor: Incomplete | None = None, tokenizer: Incomplete | None = None, **kwargs) -> None: ...
    def __call__(self, images, text: Union[TextInput, PreTokenizedInput, List[TextInput], List[PreTokenizedInput]] = None, add_special_tokens: bool = True, padding: Union[bool, str, PaddingStrategy] = False, truncation: Union[bool, str, TruncationStrategy] = None, max_length: Optional[int] = None, stride: int = 0, pad_to_multiple_of: Optional[int] = None, return_token_type_ids: Optional[bool] = None, return_attention_mask: Optional[bool] = None, return_overflowing_tokens: bool = False, return_special_tokens_mask: bool = False, return_offsets_mapping: bool = False, return_length: bool = False, verbose: bool = True, return_tensors: Optional[Union[str, TensorType]] = None, **kwargs) -> BatchEncoding:
        """
        This method uses [`ViltImageProcessor.__call__`] method to prepare image(s) for the model, and
        [`BertTokenizerFast.__call__`] to prepare text for the model.

        Please refer to the docstring of the above two methods for more information.
        """
    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to BertTokenizerFast's [`~PreTrainedTokenizer.batch_decode`]. Please
        refer to the docstring of this method for more information.
        """
    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to BertTokenizerFast's [`~PreTrainedTokenizer.decode`]. Please refer to
        the docstring of this method for more information.
        """
    @property
    def model_input_names(self): ...
    @property
    def feature_extractor_class(self): ...
    @property
    def feature_extractor(self): ...
