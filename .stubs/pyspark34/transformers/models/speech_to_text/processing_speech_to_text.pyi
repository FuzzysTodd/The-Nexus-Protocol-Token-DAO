from ...processing_utils import ProcessorMixin as ProcessorMixin
from _typeshed import Incomplete
from collections.abc import Generator

class Speech2TextProcessor(ProcessorMixin):
    """
    Constructs a Speech2Text processor which wraps a Speech2Text feature extractor and a Speech2Text tokenizer into a
    single processor.

    [`Speech2TextProcessor`] offers all the functionalities of [`Speech2TextFeatureExtractor`] and
    [`Speech2TextTokenizer`]. See the [`~Speech2TextProcessor.__call__`] and [`~Speech2TextProcessor.decode`] for more
    information.

    Args:
        feature_extractor (`Speech2TextFeatureExtractor`):
            An instance of [`Speech2TextFeatureExtractor`]. The feature extractor is a required input.
        tokenizer (`Speech2TextTokenizer`):
            An instance of [`Speech2TextTokenizer`]. The tokenizer is a required input.
    """
    feature_extractor_class: str
    tokenizer_class: str
    current_processor: Incomplete
    def __init__(self, feature_extractor, tokenizer) -> None: ...
    def __call__(self, *args, **kwargs):
        """
        When used in normal mode, this method forwards all its arguments to Speech2TextFeatureExtractor's
        [`~Speech2TextFeatureExtractor.__call__`] and returns its output. If used in the context
        [`~Speech2TextProcessor.as_target_processor`] this method forwards all its arguments to Speech2TextTokenizer's
        [`~Speech2TextTokenizer.__call__`]. Please refer to the doctsring of the above two methods for more
        information.
        """
    def batch_decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to Speech2TextTokenizer's [`~PreTrainedTokenizer.batch_decode`]. Please
        refer to the docstring of this method for more information.
        """
    def decode(self, *args, **kwargs):
        """
        This method forwards all its arguments to Speech2TextTokenizer's [`~PreTrainedTokenizer.decode`]. Please refer
        to the docstring of this method for more information.
        """
    def as_target_processor(self) -> Generator[None, None, None]:
        """
        Temporarily sets the tokenizer for processing the input. Useful for encoding the labels when fine-tuning
        Speech2Text.
        """
