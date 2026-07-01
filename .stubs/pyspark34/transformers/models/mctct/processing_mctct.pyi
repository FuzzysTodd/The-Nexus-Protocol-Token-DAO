from ...processing_utils import ProcessorMixin as ProcessorMixin
from _typeshed import Incomplete
from collections.abc import Generator

class MCTCTProcessor(ProcessorMixin):
    """
    Constructs a MCTCT processor which wraps a MCTCT feature extractor and a MCTCT tokenizer into a single processor.

    [`MCTCTProcessor`] offers all the functionalities of [`MCTCTFeatureExtractor`] and [`AutoTokenizer`]. See the
    [`~MCTCTProcessor.__call__`] and [`~MCTCTProcessor.decode`] for more information.

    Args:
        feature_extractor (`MCTCTFeatureExtractor`):
            An instance of [`MCTCTFeatureExtractor`]. The feature extractor is a required input.
        tokenizer (`AutoTokenizer`):
            An instance of [`AutoTokenizer`]. The tokenizer is a required input.
    """
    feature_extractor_class: str
    tokenizer_class: str
    current_processor: Incomplete
    def __init__(self, feature_extractor, tokenizer) -> None: ...
    def __call__(self, *args, **kwargs):
        """
        When used in normal mode, this method forwards all its arguments to MCTCTFeatureExtractor's
        [`~MCTCTFeatureExtractor.__call__`] and returns its output. If used in the context
        [`~MCTCTProcessor.as_target_processor`] this method forwards all its arguments to AutoTokenizer's
        [`~AutoTokenizer.__call__`]. Please refer to the doctsring of the above two methods for more information.
        """
    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to AutoTokenizer's [`~PreTrainedTokenizer.batch_decode`]. Please refer
        to the docstring of this method for more information.
        """
    def pad(self, *args, **kwargs):
        """
        When used in normal mode, this method forwards all its arguments to MCTCTFeatureExtractor's
        [`~MCTCTFeatureExtractor.pad`] and returns its output. If used in the context
        [`~MCTCTProcessor.as_target_processor`] this method forwards all its arguments to PreTrainedTokenizer's
        [`~PreTrainedTokenizer.pad`]. Please refer to the docstring of the above two methods for more information.
        """
    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to AutoTokenizer's [`~PreTrainedTokenizer.decode`]. Please refer to the
        docstring of this method for more information.
        """
    def as_target_processor(self) -> Generator[None, None, None]:
        """
        Temporarily sets the tokenizer for processing the input. Useful for encoding the labels when fine-tuning MCTCT.
        """
