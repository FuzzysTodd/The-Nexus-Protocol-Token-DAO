from ...utils import is_tf_available as is_tf_available, is_torch_available as is_torch_available, logging as logging
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import List, Optional, Union

logger: Incomplete

@dataclass
class InputExample:
    """
    A single training/test example for simple sequence classification.

    Args:
        guid: Unique id for the example.
        text_a: string. The untokenized text of the first sequence. For single
            sequence tasks, only this sequence must be specified.
        text_b: (Optional) string. The untokenized text of the second sequence.
            Only must be specified for sequence pair tasks.
        label: (Optional) string. The label of the example. This should be
            specified for train and dev examples, but not for test examples.
    """
    guid: str
    text_a: str
    text_b: Optional[str] = ...
    label: Optional[str] = ...
    def to_json_string(self):
        """Serializes this instance to a JSON string."""
    def __init__(self, guid, text_a, text_b, label) -> None: ...

@dataclass(frozen=True)
class InputFeatures:
    """
    A single set of features of data. Property names are the same names as the corresponding inputs to a model.

    Args:
        input_ids: Indices of input sequence tokens in the vocabulary.
        attention_mask: Mask to avoid performing attention on padding token indices.
            Mask values selected in `[0, 1]`: Usually `1` for tokens that are NOT MASKED, `0` for MASKED (padded)
            tokens.
        token_type_ids: (Optional) Segment token indices to indicate first and second
            portions of the inputs. Only some models use them.
        label: (Optional) Label corresponding to the input. Int for classification problems,
            float for regression problems.
    """
    input_ids: List[int]
    attention_mask: Optional[List[int]] = ...
    token_type_ids: Optional[List[int]] = ...
    label: Optional[Union[int, float]] = ...
    def to_json_string(self):
        """Serializes this instance to a JSON string."""
    def __init__(self, input_ids, attention_mask, token_type_ids, label) -> None: ...

class DataProcessor:
    """Base class for data converters for sequence classification data sets."""
    def get_example_from_tensor_dict(self, tensor_dict) -> None:
        """
        Gets an example from a dict with tensorflow tensors.

        Args:
            tensor_dict: Keys and values should match the corresponding Glue
                tensorflow_dataset examples.
        """
    def get_train_examples(self, data_dir) -> None:
        """Gets a collection of [`InputExample`] for the train set."""
    def get_dev_examples(self, data_dir) -> None:
        """Gets a collection of [`InputExample`] for the dev set."""
    def get_test_examples(self, data_dir) -> None:
        """Gets a collection of [`InputExample`] for the test set."""
    def get_labels(self) -> None:
        """Gets the list of labels for this data set."""
    def tfds_map(self, example):
        """
        Some tensorflow_datasets datasets are not formatted the same way the GLUE datasets are. This method converts
        examples to the correct format.
        """

class SingleSentenceClassificationProcessor(DataProcessor):
    """Generic processor for a single sentence classification data set."""
    labels: Incomplete
    examples: Incomplete
    mode: Incomplete
    verbose: Incomplete
    def __init__(self, labels: Incomplete | None = None, examples: Incomplete | None = None, mode: str = 'classification', verbose: bool = False) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, idx): ...
    @classmethod
    def create_from_csv(cls, file_name, split_name: str = '', column_label: int = 0, column_text: int = 1, column_id: Incomplete | None = None, skip_first_row: bool = False, **kwargs): ...
    @classmethod
    def create_from_examples(cls, texts_or_text_and_labels, labels: Incomplete | None = None, **kwargs): ...
    def add_examples_from_csv(self, file_name, split_name: str = '', column_label: int = 0, column_text: int = 1, column_id: Incomplete | None = None, skip_first_row: bool = False, overwrite_labels: bool = False, overwrite_examples: bool = False): ...
    def add_examples(self, texts_or_text_and_labels, labels: Incomplete | None = None, ids: Incomplete | None = None, overwrite_labels: bool = False, overwrite_examples: bool = False): ...
    def get_features(self, tokenizer, max_length: Incomplete | None = None, pad_on_left: bool = False, pad_token: int = 0, mask_padding_with_zero: bool = True, return_tensors: Incomplete | None = None):
        """
        Convert examples in a list of `InputFeatures`

        Args:
            tokenizer: Instance of a tokenizer that will tokenize the examples
            max_length: Maximum example length
            pad_on_left: If set to `True`, the examples will be padded on the left rather than on the right (default)
            pad_token: Padding token
            mask_padding_with_zero: If set to `True`, the attention mask will be filled by `1` for actual values
                and by `0` for padded values. If set to `False`, inverts it (`1` for padded values, `0` for actual
                values)

        Returns:
            If the `examples` input is a `tf.data.Dataset`, will return a `tf.data.Dataset` containing the
            task-specific features. If the input is a list of `InputExamples`, will return a list of task-specific
            `InputFeatures` which can be fed to the model.

        """
