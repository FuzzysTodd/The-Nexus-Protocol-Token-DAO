from ...image_utils import ImageInput as ImageInput
from ...processing_utils import ProcessorMixin as ProcessorMixin
from ...tokenization_utils_base import BatchEncoding as BatchEncoding, PaddingStrategy as PaddingStrategy, PreTokenizedInput as PreTokenizedInput, TextInput as TextInput, TruncationStrategy as TruncationStrategy
from ...utils import TensorType as TensorType
from _typeshed import Incomplete
from typing import List, Optional, Union

class FlavaProcessor(ProcessorMixin):
    """
    Constructs a FLAVA processor which wraps a FLAVA image processor and a FLAVA tokenizer into a single processor.

    [`FlavaProcessor`] offers all the functionalities of [`FlavaImageProcessor`] and [`BertTokenizerFast`]. See the
    [`~FlavaProcessor.__call__`] and [`~FlavaProcessor.decode`] for more information.

    Args:
        image_processor ([`FlavaImageProcessor`]): The image processor is a required input.
        tokenizer ([`BertTokenizerFast`]): The tokenizer is a required input.
    """
    attributes: Incomplete
    image_processor_class: str
    tokenizer_class: Incomplete
    current_processor: Incomplete
    def __init__(self, image_processor: Incomplete | None = None, tokenizer: Incomplete | None = None, **kwargs) -> None: ...
    def __call__(self, images: Optional[ImageInput] = None, text: Optional[Union[TextInput, PreTokenizedInput, List[TextInput], List[PreTokenizedInput]]] = None, add_special_tokens: bool = True, padding: Union[bool, str, PaddingStrategy] = False, truncation: Union[bool, str, TruncationStrategy] = False, max_length: Optional[int] = None, stride: int = 0, pad_to_multiple_of: Optional[int] = None, return_image_mask: Optional[bool] = None, return_codebook_pixels: Optional[bool] = None, return_token_type_ids: Optional[bool] = None, return_attention_mask: Optional[bool] = None, return_overflowing_tokens: bool = False, return_special_tokens_mask: bool = False, return_offsets_mapping: bool = False, return_length: bool = False, verbose: bool = True, return_tensors: Optional[Union[str, TensorType]] = None, **kwargs):
        """
        This method uses [`FlavaImageProcessor.__call__`] method to prepare image(s) for the model, and
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
