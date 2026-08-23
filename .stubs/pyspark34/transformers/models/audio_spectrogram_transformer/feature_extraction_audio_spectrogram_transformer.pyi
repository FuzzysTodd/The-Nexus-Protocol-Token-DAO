import numpy as np
from ...feature_extraction_sequence_utils import SequenceFeatureExtractor as SequenceFeatureExtractor
from ...feature_extraction_utils import BatchFeature as BatchFeature
from ...utils import TensorType as TensorType, logging as logging
from _typeshed import Incomplete
from typing import List, Optional, Union

logger: Incomplete

class ASTFeatureExtractor(SequenceFeatureExtractor):
    """
    Constructs a Audio Spectrogram Transformer (AST) feature extractor.

    This feature extractor inherits from [`~feature_extraction_sequence_utils.SequenceFeatureExtractor`] which contains
    most of the main methods. Users should refer to this superclass for more information regarding those methods.

    This class extracts mel-filter bank features from raw speech using TorchAudio, pads/truncates them to a fixed
    length and normalizes them using a mean and standard deviation.

    Args:
        feature_size (`int`, *optional*, defaults to 1):
            The feature dimension of the extracted features.
        sampling_rate (`int`, *optional*, defaults to 16000):
            The sampling rate at which the audio files should be digitalized expressed in hertz (Hz).
        num_mel_bins (`int`, *optional*, defaults to 128):
            Number of Mel-frequency bins.
        max_length (`int`, *optional*, defaults to 1024):
            Maximum length to which to pad/truncate the extracted features.
        do_normalize (`bool`, *optional*, defaults to `True`):
            Whether or not to normalize the log-Mel features using `mean` and `std`.
        mean (`float`, *optional*, defaults to -4.2677393):
            The mean value used to normalize the log-Mel features. Uses the AudioSet mean by default.
        std (`float`, *optional*, defaults to 4.5689974):
            The standard deviation value used to normalize the log-Mel features. Uses the AudioSet standard deviation
            by default.
        return_attention_mask (`bool`, *optional*, defaults to `False`):
            Whether or not [`~ASTFeatureExtractor.__call__`] should return `attention_mask`.
    """
    model_input_names: Incomplete
    num_mel_bins: Incomplete
    max_length: Incomplete
    do_normalize: Incomplete
    mean: Incomplete
    std: Incomplete
    return_attention_mask: Incomplete
    def __init__(self, feature_size: int = 1, sampling_rate: int = 16000, num_mel_bins: int = 128, max_length: int = 1024, padding_value: float = 0.0, do_normalize: bool = True, mean: float = -4.2677393, std: float = 4.5689974, return_attention_mask: bool = False, **kwargs) -> None: ...
    def normalize(self, input_values: np.ndarray) -> np.ndarray: ...
    def __call__(self, raw_speech: Union[np.ndarray, List[float], List[np.ndarray], List[List[float]]], sampling_rate: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, **kwargs) -> BatchFeature:
        """
        Main method to featurize and prepare for the model one or several sequence(s).

        Args:
            raw_speech (`np.ndarray`, `List[float]`, `List[np.ndarray]`, `List[List[float]]`):
                The sequence or batch of sequences to be padded. Each sequence can be a numpy array, a list of float
                values, a list of numpy arrays or a list of list of float values.
            sampling_rate (`int`, *optional*):
                The sampling rate at which the `raw_speech` input was sampled. It is strongly recommended to pass
                `sampling_rate` at the forward call to prevent silent errors.
            return_tensors (`str` or [`~utils.TensorType`], *optional*):
                If set, will return tensors instead of list of python integers. Acceptable values are:

                - `'tf'`: Return TensorFlow `tf.constant` objects.
                - `'pt'`: Return PyTorch `torch.Tensor` objects.
                - `'np'`: Return Numpy `np.ndarray` objects.
        """
