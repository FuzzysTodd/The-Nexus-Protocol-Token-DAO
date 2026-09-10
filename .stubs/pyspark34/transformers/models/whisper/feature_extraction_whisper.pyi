import numpy as np
from ...feature_extraction_sequence_utils import SequenceFeatureExtractor as SequenceFeatureExtractor
from ...feature_extraction_utils import BatchFeature as BatchFeature
from ...utils import TensorType as TensorType, logging as logging
from _typeshed import Incomplete
from typing import List, Optional, Union

logger: Incomplete

class WhisperFeatureExtractor(SequenceFeatureExtractor):
    """
    Constructs a Whisper feature extractor.

    This feature extractor inherits from [`WhisperFeatureExtractor`] which contains most of the main methods. Users
    should refer to this superclass for more information regarding those methods.

    This class extracts mel-filter bank features from raw speech using a custom numpy implementation of the `Short Time
    Fourier Transform` which should match pytorch's `torch.stft` equivalent.

    Args:
        feature_size (`int`, defaults to 80):
            The feature dimension of the extracted features.
        sampling_rate (`int`, defaults to 16000):
            The sampling rate at which the audio files should be digitalized expressed in hertz (Hz).
        hop_length (`int`, defaults to 160):
            Length of the overlaping windows for the STFT used to obtain the Mel Frequency coefficients.
        chunk_length (`int`, defaults to 30):
            The maximum number of chuncks of `sampling_rate` samples used to trim and pad longer or shorter audio
            sequences.
        n_fft (`int`, defaults to 400):
            Size of the Fourier transform.
        padding_value (`float`, *optional*, defaults to 0.0):
            Padding value used to pad the audio. Should correspond to silences.
    """
    model_input_names: Incomplete
    n_fft: Incomplete
    hop_length: Incomplete
    chunk_length: Incomplete
    n_samples: Incomplete
    nb_max_frames: Incomplete
    sampling_rate: Incomplete
    mel_filters: Incomplete
    def __init__(self, feature_size: int = 80, sampling_rate: int = 16000, hop_length: int = 160, chunk_length: int = 30, n_fft: int = 400, padding_value: float = 0.0, return_attention_mask: bool = False, **kwargs) -> None: ...
    def get_mel_filters(self, sr, n_fft, n_mels: int = 128, dtype=...): ...
    def fram_wave(self, waveform, center: bool = True):
        """
        Transform a raw waveform into a list of smaller waveforms. The window length defines how much of the signal is
        contain in each frame (smalle waveform), while the hope length defines the step between the beginning of each
        new frame.

        Centering is done by reflecting the waveform which is first centered around `frame_idx * hop_length`.
        """
    def stft(self, frames, window):
        """
        Calculates the complex Short-Time Fourier Transform (STFT) of the given framed signal. Should give the same
        results as `torch.stft`.
        """
    def __call__(self, raw_speech: Union[np.ndarray, List[float], List[np.ndarray], List[List[float]]], truncation: bool = True, pad_to_multiple_of: Optional[int] = None, return_tensors: Optional[Union[str, TensorType]] = None, return_attention_mask: Optional[bool] = None, padding: Optional[str] = 'max_length', max_length: Optional[int] = None, sampling_rate: Optional[int] = None, **kwargs) -> BatchFeature:
        """
        Main method to featurize and prepare for the model one or several sequence(s).

        Args:
            raw_speech (`np.ndarray`, `List[float]`, `List[np.ndarray]`, `List[List[float]]`):
                The sequence or batch of sequences to be padded. Each sequence can be a numpy array, a list of float
                values, a list of numpy arrays or a list of list of float values.
            truncation (`bool`, *optional*, default to `True`):
                Activates truncation to cut input sequences longer than *max_length* to *max_length*.
            pad_to_multiple_of (`int`, *optional*, defaults to None):
                If set will pad the sequence to a multiple of the provided value.

                This is especially useful to enable the use of Tensor Cores on NVIDIA hardware with compute capability
                `>= 7.5` (Volta), or on TPUs which benefit from having sequence lengths be a multiple of 128.
            return_attention_mask (`bool`, *optional*):
                Whether to return the attention mask. If left to the default, will return the attention mask according
                to the specific feature_extractor's default.

                [What are attention masks?](../glossary#attention-mask)

                <Tip>

                For Whisper models, `attention_mask` should always be passed for batched inference, to avoid subtle
                bugs.

                </Tip>

            return_tensors (`str` or [`~utils.TensorType`], *optional*):
                If set, will return tensors instead of list of python integers. Acceptable values are:

                - `'tf'`: Return TensorFlow `tf.constant` objects.
                - `'pt'`: Return PyTorch `torch.Tensor` objects.
                - `'np'`: Return Numpy `np.ndarray` objects.
            sampling_rate (`int`, *optional*):
                The sampling rate at which the `raw_speech` input was sampled. It is strongly recommended to pass
                `sampling_rate` at the forward call to prevent silent errors and allow automatic speech recognition
                pipeline.
            padding_value (`float`, defaults to 0.0):
                The value that is used to fill the padding values / vectors.
        """
