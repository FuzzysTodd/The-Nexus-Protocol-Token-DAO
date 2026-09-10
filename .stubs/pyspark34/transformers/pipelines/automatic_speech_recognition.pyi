import numpy as np
from ...feature_extraction_sequence_utils import SequenceFeatureExtractor as SequenceFeatureExtractor
from ..models.auto.modeling_auto import MODEL_FOR_CTC_MAPPING as MODEL_FOR_CTC_MAPPING, MODEL_FOR_SPEECH_SEQ_2_SEQ_MAPPING as MODEL_FOR_SPEECH_SEQ_2_SEQ_MAPPING
from ..utils import is_torch_available as is_torch_available, logging as logging
from .audio_utils import ffmpeg_read as ffmpeg_read
from .base import ChunkPipeline as ChunkPipeline
from _typeshed import Incomplete
from collections.abc import Generator
from pyctcdecode import BeamSearchDecoderCTC as BeamSearchDecoderCTC
from transformers.generation.logits_process import WhisperTimeStampLogitsProcessor as WhisperTimeStampLogitsProcessor
from typing import Dict, Optional, Union

logger: Incomplete

def rescale_stride(stride, ratio):
    """
    Rescales the stride values from audio space to tokens/logits space.

    (160_000, 16_000, 16_000) -> (2000, 200, 200) for instance.
    """
def chunk_iter(inputs, feature_extractor, chunk_len, stride_left, stride_right, rescale: bool = True, dtype: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...

class AutomaticSpeechRecognitionPipeline(ChunkPipeline):
    '''
    Pipeline that aims at extracting spoken text contained within some audio.

    The input can be either a raw waveform or a audio file. In case of the audio file, ffmpeg should be installed for
    to support multiple audio formats

    Example:

    ```python
    >>> from transformers import pipeline

    >>> transcriber = pipeline(model="openai/whisper-base")
    >>> transcriber("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/1.flac")
    {\'text\': \' He hoped there would be stew for dinner, turnips and carrots and bruised potatoes and fat mutton pieces to be ladled out in thick, peppered flour-fatten sauce.\'}
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

    Arguments:
        model ([`PreTrainedModel`] or [`TFPreTrainedModel`]):
            The model that will be used by the pipeline to make predictions. This needs to be a model inheriting from
            [`PreTrainedModel`] for PyTorch and [`TFPreTrainedModel`] for TensorFlow.
        tokenizer ([`PreTrainedTokenizer`]):
            The tokenizer that will be used by the pipeline to encode data for the model. This object inherits from
            [`PreTrainedTokenizer`].
        feature_extractor ([`SequenceFeatureExtractor`]):
            The feature extractor that will be used by the pipeline to encode waveform for the model.
        chunk_length_s (`float`, *optional*, defaults to 0):
            The input length for in each chunk. If `chunk_length_s = 0` then chunking is disabled (default). Only
            available for CTC models, e.g. [`Wav2Vec2ForCTC`].

            <Tip>

            For more information on how to effectively use `chunk_length_s`, please have a look at the [ASR chunking
            blog post](https://huggingface.co/blog/asr-chunking).

            </Tip>

        stride_length_s (`float`, *optional*, defaults to `chunk_length_s / 6`):
            The length of stride on the left and right of each chunk. Used only with `chunk_length_s > 0`. This enables
            the model to *see* more context and infer letters better than without this context but the pipeline
            discards the stride bits at the end to make the final reconstitution as perfect as possible.

            <Tip>

            For more information on how to effectively use `stride_length_s`, please have a look at the [ASR chunking
            blog post](https://huggingface.co/blog/asr-chunking).

            </Tip>

        framework (`str`, *optional*):
            The framework to use, either `"pt"` for PyTorch or `"tf"` for TensorFlow. The specified framework must be
            installed. If no framework is specified, will default to the one currently installed. If no framework is
            specified and both frameworks are installed, will default to the framework of the `model`, or to PyTorch if
            no model is provided.
        device (`int`, *optional*, defaults to -1):
            Device ordinal for CPU/GPU supports. Setting this to -1 will leverage CPU, a positive will run the model on
            the associated CUDA device id.
        decoder (`pyctcdecode.BeamSearchDecoderCTC`, *optional*):
            [PyCTCDecode\'s
            BeamSearchDecoderCTC](https://github.com/kensho-technologies/pyctcdecode/blob/2fd33dc37c4111417e08d89ccd23d28e9b308d19/pyctcdecode/decoder.py#L180)
            can be passed for language model boosted decoding. See [`Wav2Vec2ProcessorWithLM`] for more information.

    '''
    feature_extractor: Incomplete
    type: str
    decoder: Incomplete
    def __init__(self, feature_extractor: Union['SequenceFeatureExtractor', str], *, decoder: Optional[Union['BeamSearchDecoderCTC', str]] = None, **kwargs) -> None: ...
    def __call__(self, inputs: Union[np.ndarray, bytes, str], **kwargs):
        '''
        Transcribe the audio sequence(s) given as inputs to text. See the [`AutomaticSpeechRecognitionPipeline`]
        documentation for more information.

        Args:
            inputs (`np.ndarray` or `bytes` or `str` or `dict`):
                The inputs is either :
                    - `str` that is the filename of the audio file, the file will be read at the correct sampling rate
                      to get the waveform using *ffmpeg*. This requires *ffmpeg* to be installed on the system.
                    - `bytes` it is supposed to be the content of an audio file and is interpreted by *ffmpeg* in the
                      same way.
                    - (`np.ndarray` of shape (n, ) of type `np.float32` or `np.float64`)
                        Raw audio at the correct sampling rate (no further check will be done)
                    - `dict` form can be used to pass raw audio sampled at arbitrary `sampling_rate` and let this
                      pipeline do the resampling. The dict must be in the format `{"sampling_rate": int, "raw":
                      np.array}` with optionally a `"stride": (left: int, right: int)` than can ask the pipeline to
                      treat the first `left` samples and last `right` samples to be ignored in decoding (but used at
                      inference to provide more context to the model). Only use `stride` with CTC models.
            return_timestamps (*optional*, `str`):
                Only available for pure CTC models. If set to `"char"`, the pipeline will return `timestamps` along the
                text for every character in the text. For instance if you get `[{"text": "h", "timestamps": (0.5,0.6),
                {"text": "i", "timestamps": (0.7, .9)}]`, then it means the model predicts that the letter "h" was
                pronounced after `0.5` and before `0.6` seconds. If set to `"word"`, the pipeline will return
                `timestamps` along the text for every word in the text. For instance if you get `[{"text": "hi ",
                "timestamps": (0.5,0.9), {"text": "there", "timestamps": (1.0, .1.5)}]`, then it means the model
                predicts that the word "hi" was pronounced after `0.5` and before `0.9` seconds.
            generate_kwargs (`dict`, *optional*):
                The dictionary of ad-hoc parametrization of `generate_config` to be used for the generation call. For a
                complete overview of generate, check the [following
                guide](https://huggingface.co/docs/transformers/en/main_classes/text_generation).
            max_new_tokens (`int`, *optional*):
                The maximum numbers of tokens to generate, ignoring the number of tokens in the prompt.

        Return:
            `Dict`: A dictionary with the following keys:
                - **text** (`str` ) -- The recognized text.
                - **chunks** (*optional(, `List[Dict]`)
                        When using `return_timestamps`, the `chunks` will become a list containing all the various text
                        chunks identified by the model, *e.g.* `[{"text": "hi ", "timestamps": (0.5,0.9), {"text":
                        "there", "timestamps": (1.0, 1.5)}]`. The original full text can roughly be recovered by doing
                        `"".join(chunk["text"] for chunk in output["chunks"])`.
        '''
    def preprocess(self, inputs, chunk_length_s: int = 0, stride_length_s: Incomplete | None = None, ignore_warning: bool = False) -> Generator[Incomplete, None, None]: ...
    def postprocess(self, model_outputs, decoder_kwargs: Optional[Dict] = None, return_timestamps: Incomplete | None = None): ...
