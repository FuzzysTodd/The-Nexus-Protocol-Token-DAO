import numpy as np
import tensorflow as tf
import torch
from ...tokenization_utils import PreTrainedTokenizer as PreTrainedTokenizer
from ...tokenization_utils_base import AddedToken as AddedToken, BatchEncoding as BatchEncoding
from ...utils import ModelOutput as ModelOutput, PaddingStrategy as PaddingStrategy, TensorType as TensorType, add_end_docstrings as add_end_docstrings, is_flax_available as is_flax_available, is_tf_available as is_tf_available, is_torch_available as is_torch_available, logging as logging, to_py_obj as to_py_obj
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Union

logger: Incomplete
VOCAB_FILES_NAMES: Incomplete
PRETRAINED_VOCAB_FILES_MAP: Incomplete
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Incomplete
WAV2VEC2_KWARGS_DOCSTRING: str
ListOfDict = List[Dict[str, Union[int, str]]]

@dataclass
class Wav2Vec2CTCTokenizerOutput(ModelOutput):
    """
    Output type of [` Wav2Vec2CTCTokenizer`], with transcription.

    Args:
        text (list of `str` or `str`):
            Decoded logits in text from. Usually the speech transcription.
        char_offsets (list of `List[Dict[str, Union[int, str]]]` or `List[Dict[str, Union[int, str]]]`):
            Offsets of the decoded characters. In combination with sampling rate and model downsampling rate char
            offsets can be used to compute time stamps for each charater. Total logit score of the beam associated with
            produced text.
        word_offsets (list of `List[Dict[str, Union[int, str]]]` or `List[Dict[str, Union[int, str]]]`):
            Offsets of the decoded words. In combination with sampling rate and model downsampling rate word offsets
            can be used to compute time stamps for each word.
    """
    text: Union[List[str], str]
    char_offsets: Union[List[ListOfDict], ListOfDict] = ...
    word_offsets: Union[List[ListOfDict], ListOfDict] = ...
    def __init__(self, text, char_offsets, word_offsets) -> None: ...

class Wav2Vec2CTCTokenizer(PreTrainedTokenizer):
    '''
    Constructs a Wav2Vec2CTC tokenizer.

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains some of the main methods. Users should refer to
    the superclass for more information regarding such methods.

    Args:
        vocab_file (`str`):
            File containing the vocabulary.
        bos_token (`str`, *optional*, defaults to `"<s>"`):
            The beginning of sentence token.
        eos_token (`str`, *optional*, defaults to `"</s>"`):
            The end of sentence token.
        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        pad_token (`str`, *optional*, defaults to `"<pad>"`):
            The token used for padding, for example when batching sequences of different lengths.
        word_delimiter_token (`str`, *optional*, defaults to `"|"`):
            The token used for defining the end of a word.
        do_lower_case (`bool`, *optional*, defaults to `False`):
            Whether or not to accept lowercase input and lowercase the output when decoding.

        **kwargs
            Additional keyword arguments passed along to [`PreTrainedTokenizer`]
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    model_input_names: Incomplete
    do_lower_case: Incomplete
    replace_word_delimiter_char: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, vocab_file, bos_token: str = '<s>', eos_token: str = '</s>', unk_token: str = '<unk>', pad_token: str = '<pad>', word_delimiter_token: str = '|', replace_word_delimiter_char: str = ' ', do_lower_case: bool = False, **kwargs) -> None: ...
    @property
    def word_delimiter_token(self) -> str:
        """
        `str`: Word delimiter token. Log an error if used while not having been set.
        """
    @property
    def word_delimiter_token_id(self) -> Optional[int]:
        """
        `Optional[int]`: Id of the word_delimiter_token in the vocabulary. Returns `None` if the token has not been
        set.
        """
    @word_delimiter_token.setter
    def word_delimiter_token(self, value) -> None: ...
    @word_delimiter_token_id.setter
    def word_delimiter_token_id(self, value) -> None: ...
    @property
    def vocab_size(self) -> int: ...
    def get_vocab(self) -> Dict: ...
    def convert_tokens_to_string(self, tokens: List[str], group_tokens: bool = True, spaces_between_special_tokens: bool = False, output_char_offsets: bool = False, output_word_offsets: bool = False) -> Dict[str, Union[str, float]]:
        """
        Converts a connectionist-temporal-classification (CTC) output tokens into a single string.
        """
    def prepare_for_tokenization(self, text, is_split_into_words: bool = False, **kwargs): ...
    def batch_decode(self, sequences: Union[List[int], List[List[int]], 'np.ndarray', 'torch.Tensor', 'tf.Tensor'], skip_special_tokens: bool = False, clean_up_tokenization_spaces: bool = True, output_char_offsets: bool = False, output_word_offsets: bool = False, **kwargs) -> List[str]:
        """
        Convert a list of lists of token ids into a list of strings by calling decode.

        Args:
            sequences (`Union[List[int], List[List[int]], np.ndarray, torch.Tensor, tf.Tensor]`):
                List of tokenized input ids. Can be obtained using the `__call__` method.
            skip_special_tokens (`bool`, *optional*, defaults to `False`):
                Whether or not to remove special tokens in the decoding.
            clean_up_tokenization_spaces (`bool`, *optional*, defaults to `True`):
                Whether or not to clean up the tokenization spaces.
            output_char_offsets (`bool`, *optional*, defaults to `False`):
                Whether or not to output character offsets. Character offsets can be used in combination with the
                sampling rate and model downsampling rate to compute the time-stamps of transcribed characters.

                <Tip>

                Please take a look at the Example of [`~Wav2Vec2CTCTokenizer.decode`] to better understand how to make
                use of `output_char_offsets`. [`~Wav2Vec2CTCTokenizer.batch_decode`] works the same way with batched
                output.

                </Tip>

            output_word_offsets (`bool`, *optional*, defaults to `False`):
                Whether or not to output word offsets. Word offsets can be used in combination with the sampling rate
                and model downsampling rate to compute the time-stamps of transcribed words.

                <Tip>

                Please take a look at the Example of [`~Wav2Vec2CTCTokenizer.decode`] to better understand how to make
                use of `output_word_offsets`. [`~Wav2Vec2CTCTokenizer.batch_decode`] works the same way with batched
                output.

                </Tip>

            kwargs (additional keyword arguments, *optional*):
                Will be passed to the underlying model specific decode method.

        Returns:
            `List[str]` or [`~models.wav2vec2.tokenization_wav2vec2.Wav2Vec2CTCTokenizerOutput`]: The list of decoded
            sentences. Will be a [`~models.wav2vec2.tokenization_wav2vec2.Wav2Vec2CTCTokenizerOutput`] when
            `output_char_offsets == True` or `output_word_offsets == True`.
        """
    def decode(self, token_ids: Union[int, List[int], 'np.ndarray', 'torch.Tensor', 'tf.Tensor'], skip_special_tokens: bool = False, clean_up_tokenization_spaces: bool = True, output_char_offsets: bool = False, output_word_offsets: bool = False, **kwargs) -> str:
        '''
        Converts a sequence of ids in a string, using the tokenizer and vocabulary with options to remove special
        tokens and clean up tokenization spaces.

        Similar to doing `self.convert_tokens_to_string(self.convert_ids_to_tokens(token_ids))`.

        Args:
            token_ids (`Union[int, List[int], np.ndarray, torch.Tensor, tf.Tensor]`):
                List of tokenized input ids. Can be obtained using the `__call__` method.
            skip_special_tokens (`bool`, *optional*, defaults to `False`):
                Whether or not to remove special tokens in the decoding.
            clean_up_tokenization_spaces (`bool`, *optional*, defaults to `True`):
                Whether or not to clean up the tokenization spaces.
            output_char_offsets (`bool`, *optional*, defaults to `False`):
                Whether or not to output character offsets. Character offsets can be used in combination with the
                sampling rate and model downsampling rate to compute the time-stamps of transcribed characters.

                <Tip>

                Please take a look at the example below to better understand how to make use of `output_char_offsets`.

                </Tip>

            output_word_offsets (`bool`, *optional*, defaults to `False`):
                Whether or not to output word offsets. Word offsets can be used in combination with the sampling rate
                and model downsampling rate to compute the time-stamps of transcribed words.

                <Tip>

                Please take a look at the example below to better understand how to make use of `output_word_offsets`.

                </Tip>

            kwargs (additional keyword arguments, *optional*):
                Will be passed to the underlying model specific decode method.

        Returns:
            `str` or [`~models.wav2vec2.tokenization_wav2vec2.Wav2Vec2CTCTokenizerOutput`]: The list of decoded
            sentences. Will be a [`~models.wav2vec2.tokenization_wav2vec2.Wav2Vec2CTCTokenizerOutput`] when
            `output_char_offsets == True` or `output_word_offsets == True`.

        Example:

        ```python
        >>> # Let\'s see how to retrieve time steps for a model
        >>> from transformers import AutoTokenizer, AutoFeatureExtractor, AutoModelForCTC
        >>> from datasets import load_dataset
        >>> import datasets
        >>> import torch

        >>> # import model, feature extractor, tokenizer
        >>> model = AutoModelForCTC.from_pretrained("facebook/wav2vec2-base-960h")
        >>> tokenizer = AutoTokenizer.from_pretrained("facebook/wav2vec2-base-960h")
        >>> feature_extractor = AutoFeatureExtractor.from_pretrained("facebook/wav2vec2-base-960h")

        >>> # load first sample of English common_voice
        >>> dataset = load_dataset("common_voice", "en", split="train", streaming=True)
        >>> dataset = dataset.cast_column("audio", datasets.Audio(sampling_rate=16_000))
        >>> dataset_iter = iter(dataset)
        >>> sample = next(dataset_iter)

        >>> # forward sample through model to get greedily predicted transcription ids
        >>> input_values = feature_extractor(sample["audio"]["array"], return_tensors="pt").input_values
        >>> logits = model(input_values).logits[0]
        >>> pred_ids = torch.argmax(logits, axis=-1)

        >>> # retrieve word stamps (analogous commands for `output_char_offsets`)
        >>> outputs = tokenizer.decode(pred_ids, output_word_offsets=True)
        >>> # compute `time_offset` in seconds as product of downsampling ratio and sampling_rate
        >>> time_offset = model.config.inputs_to_logits_ratio / feature_extractor.sampling_rate

        >>> word_offsets = [
        ...     {
        ...         "word": d["word"],
        ...         "start_time": round(d["start_offset"] * time_offset, 2),
        ...         "end_time": round(d["end_offset"] * time_offset, 2),
        ...     }
        ...     for d in outputs.word_offsets
        ... ]
        >>> # compare word offsets with audio `common_voice_en_100038.mp3` online on the dataset viewer:
        >>> # https://huggingface.co/datasets/common_voice/viewer/en/train
        >>> word_offsets[:3]
        [{\'word\': \'WHY\', \'start_time\': 1.42, \'end_time\': 1.54}, {\'word\': \'DOES\', \'start_time\': 1.64, \'end_time\': 1.9}, {\'word\': \'MILISANDRA\', \'start_time\': 2.26, \'end_time\': 2.9}]
        ```'''
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...

class Wav2Vec2Tokenizer(PreTrainedTokenizer):
    '''
    Constructs a Wav2Vec2 tokenizer.

    This tokenizer inherits from [`PreTrainedTokenizer`] which contains some of the main methods. Users should refer to
    the superclass for more information regarding such methods.

    Args:
        vocab_file (`str`):
            File containing the vocabulary.
        bos_token (`str`, *optional*, defaults to `"<s>"`):
            The beginning of sentence token.
        eos_token (`str`, *optional*, defaults to `"</s>"`):
            The end of sentence token.
        unk_token (`str`, *optional*, defaults to `"<unk>"`):
            The unknown token. A token that is not in the vocabulary cannot be converted to an ID and is set to be this
            token instead.
        pad_token (`str`, *optional*, defaults to `"<pad>"`):
            The token used for padding, for example when batching sequences of different lengths.
        word_delimiter_token (`str`, *optional*, defaults to `"|"`):
            The token used for defining the end of a word.
        do_lower_case (`bool`, *optional*, defaults to `False`):
            Whether or not to lowercase the output when decoding.
        do_normalize (`bool`, *optional*, defaults to `False`):
            Whether or not to zero-mean unit-variance normalize the input. Normalizing can help to significantly
            improve the performance for some models, *e.g.*,
            [wav2vec2-lv60](https://huggingface.co/models?search=lv60).
        return_attention_mask (`bool`, *optional*, defaults to `False`):
            Whether or not [`~Wav2Vec2Tokenizer.__call__`] should return `attention_mask`.

            <Tip>

            Wav2Vec2 models that have set `config.feat_extract_norm == "group"`, such as
            [wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base-960h), have **not** been trained using
            `attention_mask`. For such models, `input_values` should simply be padded with 0 and no `attention_mask`
            should be passed.

            For Wav2Vec2 models that have set `config.feat_extract_norm == "layer"`, such as
            [wav2vec2-lv60](https://huggingface.co/facebook/wav2vec2-large-960h-lv60-self), `attention_mask` should be
            passed for batched inference.

            </Tip>

        **kwargs
            Additional keyword arguments passed along to [`PreTrainedTokenizer`]
    '''
    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map: Incomplete
    model_input_names: Incomplete
    do_lower_case: Incomplete
    return_attention_mask: Incomplete
    do_normalize: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, vocab_file, bos_token: str = '<s>', eos_token: str = '</s>', unk_token: str = '<unk>', pad_token: str = '<pad>', word_delimiter_token: str = '|', do_lower_case: bool = False, do_normalize: bool = False, return_attention_mask: bool = False, **kwargs) -> None: ...
    @property
    def word_delimiter_token(self) -> str:
        """
        `str`: Padding token. Log an error if used while not having been set.
        """
    @property
    def word_delimiter_token_id(self) -> Optional[int]:
        """
        `Optional[int]`: Id of the word_delimiter_token in the vocabulary. Returns `None` if the token has not been
        set.
        """
    @word_delimiter_token.setter
    def word_delimiter_token(self, value) -> None: ...
    @word_delimiter_token_id.setter
    def word_delimiter_token_id(self, value) -> None: ...
    def __call__(self, raw_speech: Union[np.ndarray, List[float], List[np.ndarray], List[List[float]]], padding: Union[bool, str, PaddingStrategy] = False, max_length: Optional[int] = None, pad_to_multiple_of: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, verbose: bool = True, **kwargs) -> BatchEncoding:
        """
        Main method to tokenize and prepare for the model one or several sequence(s) or one or several pair(s) of
        sequences.

        Args:
            raw_speech (`np.ndarray`, `List[float]`, `List[np.ndarray]`, `List[List[float]]`):
                The sequence or batch of sequences to be padded. Each sequence can be a numpy array, a list of float
                values, a list of numpy arrayr or a list of list of float values.
        """
    @property
    def vocab_size(self) -> int: ...
    def get_vocab(self) -> Dict: ...
    def convert_tokens_to_string(self, tokens: List[str]) -> str:
        """
        Converts a connectionist-temporal-classification (CTC) output tokens into a single string.
        """
    def save_vocabulary(self, save_directory: str, filename_prefix: Optional[str] = None) -> Tuple[str]: ...
