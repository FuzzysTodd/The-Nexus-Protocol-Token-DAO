import tensorflow as tf
from ..modeling_tf_outputs import TFCausalLMOutputWithPast as TFCausalLMOutputWithPast, TFSeq2SeqLMOutput as TFSeq2SeqLMOutput
from ..models.auto import TF_MODEL_FOR_CAUSAL_LM_MAPPING as TF_MODEL_FOR_CAUSAL_LM_MAPPING, TF_MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING as TF_MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING, TF_MODEL_FOR_SPEECH_SEQ_2_SEQ_MAPPING as TF_MODEL_FOR_SPEECH_SEQ_2_SEQ_MAPPING, TF_MODEL_FOR_VISION_2_SEQ_MAPPING as TF_MODEL_FOR_VISION_2_SEQ_MAPPING
from ..tf_utils import shape_list as shape_list, stable_softmax as stable_softmax
from ..utils import ModelOutput as ModelOutput, logging as logging
from .configuration_utils import GenerationConfig as GenerationConfig
from .tf_logits_process import TFForceTokensLogitsProcessor as TFForceTokensLogitsProcessor, TFForcedBOSTokenLogitsProcessor as TFForcedBOSTokenLogitsProcessor, TFForcedEOSTokenLogitsProcessor as TFForcedEOSTokenLogitsProcessor, TFLogitsProcessorList as TFLogitsProcessorList, TFMinLengthLogitsProcessor as TFMinLengthLogitsProcessor, TFNoBadWordsLogitsProcessor as TFNoBadWordsLogitsProcessor, TFNoRepeatNGramLogitsProcessor as TFNoRepeatNGramLogitsProcessor, TFRepetitionPenaltyLogitsProcessor as TFRepetitionPenaltyLogitsProcessor, TFSuppressTokensAtBeginLogitsProcessor as TFSuppressTokensAtBeginLogitsProcessor, TFSuppressTokensLogitsProcessor as TFSuppressTokensLogitsProcessor, TFTemperatureLogitsWarper as TFTemperatureLogitsWarper, TFTopKLogitsWarper as TFTopKLogitsWarper, TFTopPLogitsWarper as TFTopPLogitsWarper
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Optional, Tuple, Union

logger: Incomplete

@dataclass
class TFGreedySearchDecoderOnlyOutput(ModelOutput):
    """
    Base class for outputs of decoder-only generation models using greedy search.


    Args:
        sequences (`tf.Tensor` of shape `(batch_size, sequence_length)`):
            The generated sequences. The second dimension (sequence_length) is either equal to `max_length` or shorter
            if all batches finished early due to the `eos_token_id`.
        scores (`tuple(tf.Tensor)` *optional*, returned when `output_scores=True` is passed or when `config.output_scores=True`):
            Processed prediction scores of the language modeling head (scores for each vocabulary token before SoftMax)
            at each generation step. Tuple of `tf.Tensor` with up to `max_new_tokens` elements (one element for each
            generated token), with each tensor of shape `(batch_size, config.vocab_size)`.
        attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size, num_heads, generated_length, sequence_length)`.
        hidden_states (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size, generated_length, hidden_size)`.
    """
    sequences: tf.Tensor = ...
    scores: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    hidden_states: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    def __init__(self, sequences, scores, attentions, hidden_states) -> None: ...

@dataclass
class TFGreedySearchEncoderDecoderOutput(ModelOutput):
    """
    Base class for outputs of encoder-decoder generation models using greedy search. Hidden states and attention
    weights of the decoder (respectively the encoder) can be accessed via the encoder_attentions and the
    encoder_hidden_states attributes (respectively the decoder_attentions and the decoder_hidden_states attributes)


    Args:
        sequences (`tf.Tensor` of shape `(batch_size, sequence_length)`):
            The generated sequences. The second dimension (sequence_length) is either equal to `max_length` or shorter
            if all batches finished early due to the `eos_token_id`.
        scores (`tuple(tf.Tensor)` *optional*, returned when `output_scores=True` is passed or when `config.output_scores=True`):
            Processed prediction scores of the language modeling head (scores for each vocabulary token before SoftMax)
            at each generation step. Tuple of `tf.Tensor` with up to `max_new_tokens` elements (one element for each
            generated token), with each tensor of shape `(batch_size, config.vocab_size)`.
        encoder_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer of the decoder) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.
        encoder_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.
        decoder_attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size, num_heads, generated_length, sequence_length)`.
        cross_attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size, num_heads, generated_length, sequence_length)`.
        decoder_hidden_states (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size, generated_length, hidden_size)`.
    """
    sequences: tf.Tensor = ...
    scores: Optional[Tuple[tf.Tensor]] = ...
    encoder_attentions: Optional[Tuple[tf.Tensor]] = ...
    encoder_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    decoder_attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    cross_attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    decoder_hidden_states: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    def __init__(self, sequences, scores, encoder_attentions, encoder_hidden_states, decoder_attentions, cross_attentions, decoder_hidden_states) -> None: ...

@dataclass
class TFSampleDecoderOnlyOutput(ModelOutput):
    """
    Base class for outputs of decoder-only generation models using sampling.


    Args:
        sequences (`tf.Tensor` of shape `(batch_size*num_return_sequences, sequence_length)`):
            The generated sequences. The second dimension (sequence_length) is either equal to `max_length` or shorter
            if all batches finished early due to the `eos_token_id`.
        scores (`tuple(tf.Tensor)` *optional*, returned when `output_scores=True` is passed or when `config.output_scores=True`):
            Processed prediction scores of the language modeling head (scores for each vocabulary token before SoftMax)
            at each generation step. Tuple of `tf.Tensor` with up to `max_new_tokens` elements (one element for each
            generated token), with each tensor of shape `(batch_size*num_return_sequences, config.vocab_size)`.
        attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(num_return_sequences*batch_size, num_heads, generated_length, sequence_length)`.
        hidden_states (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(num_return_sequences*batch_size, generated_length, hidden_size)`.
    """
    sequences: tf.Tensor = ...
    scores: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    hidden_states: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    def __init__(self, sequences, scores, attentions, hidden_states) -> None: ...

@dataclass
class TFSampleEncoderDecoderOutput(ModelOutput):
    """
    Base class for outputs of encoder-decoder generation models using sampling. Hidden states and attention weights of
    the decoder (respectively the encoder) can be accessed via the encoder_attentions and the encoder_hidden_states
    attributes (respectively the decoder_attentions and the decoder_hidden_states attributes)


    Args:
        sequences (`tf.Tensor` of shape `(batch_size*num_return_sequences, sequence_length)`):
            The generated sequences. The second dimension (sequence_length) is either equal to `max_length` or shorter
            if all batches finished early due to the `eos_token_id`.
        scores (`tuple(tf.Tensor)` *optional*, returned when `output_scores=True` is passed or when `config.output_scores=True`):
            Processed prediction scores of the language modeling head (scores for each vocabulary token before SoftMax)
            at each generation step. Tuple of `tf.Tensor` with up to `max_new_tokens` elements (one element for each
            generated token), with each tensor of shape `(batch_size*num_return_sequences, config.vocab_size)`.
        encoder_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer of the decoder) of shape `(batch_size*num_return_sequences,
            num_heads, sequence_length, sequence_length)`.
        encoder_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size*num_return_sequences, sequence_length, hidden_size)`.
        decoder_attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size*num_return_sequences, num_heads, generated_length, sequence_length)`.
        cross_attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size, num_heads, generated_length, sequence_length)`.
        decoder_hidden_states (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size*num_return_sequences, generated_length, hidden_size)`.
    """
    sequences: tf.Tensor = ...
    scores: Optional[Tuple[tf.Tensor]] = ...
    encoder_attentions: Optional[Tuple[tf.Tensor]] = ...
    encoder_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    decoder_attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    cross_attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    decoder_hidden_states: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    def __init__(self, sequences, scores, encoder_attentions, encoder_hidden_states, decoder_attentions, cross_attentions, decoder_hidden_states) -> None: ...

@dataclass
class TFBeamSearchDecoderOnlyOutput(ModelOutput):
    """
    Base class for outputs of decoder-only generation models using beam search.

    Args:
        sequences (`tf.Tensor` of shape `(batch_size*num_return_sequences, sequence_length)`):
            The generated sequences. The second dimension (sequence_length) is either equal to `max_length` or shorter
            if all batches finished early due to the `eos_token_id`.
        sequences_scores (`tf.Tensor` of shape `(batch_size*num_return_sequences)`, *optional*, returned when `output_scores=True` is passed or when `config.output_scores=True`):
            Final beam scores of the generated `sequences`.
        scores (`tuple(tf.Tensor)` *optional*, returned when `output_scores=True` is passed or when `config.output_scores=True`):
            Processed beam scores for each vocabulary token at each generation step. Beam scores consisting of log
            softmax scores for each vocabulary token and sum of log softmax of previously generated tokens in this
            beam. Tuple of `tf.Tensor` with up to `max_new_tokens` elements (one element for each generated token),
            with each tensor of shape `(batch_size*num_beams*num_return_sequences, config.vocab_size)`.
        attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size*num_beams, num_heads, generated_length, sequence_length)`.
        hidden_states (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size*num_beams*num_return_sequences, generated_length, hidden_size)`.
    """
    sequences: tf.Tensor = ...
    sequences_scores: Optional[tf.Tensor] = ...
    scores: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    hidden_states: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    def __init__(self, sequences, sequences_scores, scores, attentions, hidden_states) -> None: ...

@dataclass
class TFBeamSearchEncoderDecoderOutput(ModelOutput):
    """
    Base class for outputs of encoder-decoder generation models using beam search. Hidden states and attention weights
    of the decoder (respectively the encoder) can be accessed via the encoder_attentions and the encoder_hidden_states
    attributes (respectively the decoder_attentions and the decoder_hidden_states attributes)

    Args:
        sequences (`tf.Tensor` of shape `(batch_size*num_return_sequences, sequence_length)`):
            The generated sequences. The second dimension (sequence_length) is either equal to `max_length` or shorter
            if all batches finished early due to the `eos_token_id`.
        sequences_scores (`tf.Tensor` of shape `(batch_size*num_return_sequences)`, *optional*, returned when `output_scores=True` is passed or when `config.output_scores=True`):
            Final beam scores of the generated `sequences`.
        scores (`tuple(tf.Tensor)` *optional*, returned when `output_scores=True` is passed or when `config.output_scores=True`):
            Processed beam scores for each vocabulary token at each generation step. Beam scores consisting of log
            softmax scores for each vocabulary token and sum of log softmax of previously generated tokens in this
            beam. `Tuple of `tf.Tensor` with up to `max_new_tokens` elements (one element for each generated token),
            with each tensor of shape `(batch_size*num_beams, config.vocab_size)`.
        attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
        encoder_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer of the decoder) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.
        encoder_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size*num_beams*num_return_sequences, sequence_length, hidden_size)`.
        decoder_attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size*num_beams*num_return_sequences, num_heads, generated_length,
            sequence_length)`.
        cross_attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size, num_heads, generated_length, sequence_length)`.
        decoder_hidden_states (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size*num_beams*num_return_sequences, generated_length, hidden_size)`.
    """
    sequences: tf.Tensor = ...
    sequences_scores: Optional[tf.Tensor] = ...
    scores: Optional[Tuple[tf.Tensor]] = ...
    encoder_attentions: Optional[Tuple[tf.Tensor]] = ...
    encoder_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    decoder_attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    cross_attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    decoder_hidden_states: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    def __init__(self, sequences, sequences_scores, scores, encoder_attentions, encoder_hidden_states, decoder_attentions, cross_attentions, decoder_hidden_states) -> None: ...

@dataclass
class TFBeamSampleDecoderOnlyOutput(ModelOutput):
    """
    Base class for outputs of decoder-only generation models using beam sample.

    Args:
        sequences (`tf.Tensor` of shape `(batch_size*num_return_sequences, sequence_length)`):
            The generated sequences. The second dimension (sequence_length) is either equal to `max_length` or shorter
            if all batches finished early due to the `eos_token_id`.
        sequences_scores (`tf.Tensor` of shape `(batch_size * num_return_sequence)`, *optional*, returned when `output_scores=True` is passed or when `config.output_scores=True`):
            Final beam scores of the generated `sequences`.
        scores (`tuple(tf.Tensor)` *optional*, returned when `output_scores=True` is passed or when `config.output_scores=True`):
            Processed beam scores for each vocabulary token at each generation step. Beam scores consisting of log
            softmax scores for each vocabulary token and sum of log softmax of previously generated tokens in this
            beam. Tuple of `tf.Tensor` with up to `max_new_tokens` elements (one element for each generated token),
            with each tensor of shape `(batch_size*num_beams*num_return_sequences, config.vocab_size)`.
        attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size*num_beams, num_heads, generated_length, sequence_length)`.
        hidden_states (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size*num_beams, generated_length, hidden_size)`.
    """
    sequences: tf.Tensor = ...
    sequences_scores: Optional[tf.Tensor] = ...
    scores: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    hidden_states: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    def __init__(self, sequences, sequences_scores, scores, attentions, hidden_states) -> None: ...

@dataclass
class TFBeamSampleEncoderDecoderOutput(ModelOutput):
    """
    Base class for outputs of encoder-decoder generation models using beam sampling. Hidden states and attention
    weights of the decoder (respectively the encoder) can be accessed via the encoder_attentions and the
    encoder_hidden_states attributes (respectively the decoder_attentions and the decoder_hidden_states attributes)

    Args:
        sequences (`tf.Tensor` of shape `(batch_size*num_beams, sequence_length)`):
            The generated sequences. The second dimension (sequence_length) is either equal to `max_length` or shorter
            if all batches finished early due to the `eos_token_id`.
        sequences_scores (`tf.Tensor` of shape `(batch_size * num_return_sequence)`, *optional*, returned when `output_scores=True` is passed or when `config.output_scores=True`):
            Final beam scores of the generated `sequences`.
        scores (`tuple(tf.Tensor)` *optional*, returned when `output_scores=True` is passed or when `config.output_scores=True`):
            Processed beam scores for each vocabulary token at each generation step. Beam scores consisting of log
            softmax scores for each vocabulary token and sum of log softmax of previously generated tokens in this
            beam. Tuple of `tf.Tensor` with up to `max_new_tokens` elements (one element for each generated token),
            with each tensor of shape `(batch_size*num_beams, config.vocab_size)`.
        encoder_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer of the decoder) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.
        encoder_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size*num_beams, sequence_length, hidden_size)`.
        decoder_attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size*num_beams, num_heads, generated_length, sequence_length)`.
        cross_attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size, num_heads, generated_length, sequence_length)`.
        decoder_hidden_states (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size*num_beams, generated_length, hidden_size)`.
    """
    sequences: tf.Tensor = ...
    sequences_scores: Optional[tf.Tensor] = ...
    scores: Optional[Tuple[tf.Tensor]] = ...
    encoder_attentions: Optional[Tuple[tf.Tensor]] = ...
    encoder_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    decoder_attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    cross_attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    decoder_hidden_states: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    def __init__(self, sequences, sequences_scores, scores, encoder_attentions, encoder_hidden_states, decoder_attentions, cross_attentions, decoder_hidden_states) -> None: ...

@dataclass
class TFContrastiveSearchDecoderOnlyOutput(ModelOutput):
    """
    Base class for outputs of decoder-only generation models using contrastive search.

    Args:
        sequences (`tf.Tensor` of shape `(batch_size, sequence_length)`):
            The generated sequences. The second dimension (sequence_length) is either equal to `max_length` or shorter
            if all batches finished early due to the `eos_token_id`.
        scores (`tuple(tf.Tensor)` *optional*, returned when `output_scores=True` is passed or when `config.output_scores=True`):
            Processed prediction scores of the language modeling head (scores for each vocabulary token before SoftMax)
            at each generation step. Tuple of `tf.Tensor` with up to `max_new_tokens` elements (one element for each
            generated token), with each tensor of shape `(batch_size, config.vocab_size)`.
        attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size, num_heads, generated_length, sequence_length)`.
        hidden_states (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size, generated_length, hidden_size)`.
    """
    sequences: tf.Tensor = ...
    scores: Optional[Tuple[tf.Tensor]] = ...
    attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    hidden_states: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    def __init__(self, sequences, scores, attentions, hidden_states) -> None: ...

@dataclass
class TFContrastiveSearchEncoderDecoderOutput(ModelOutput):
    """
    Base class for outputs of encoder-decoder generation models using contrastive search. Hidden states and attention
    weights of the decoder (respectively the encoder) can be accessed via the encoder_attentions and the
    encoder_hidden_states attributes (respectively the decoder_attentions and the decoder_hidden_states attributes)

    Args:
        sequences (`tf.Tensor` of shape `(batch_size, sequence_length)`):
            The generated sequences. The second dimension (sequence_length) is either equal to `max_length` or shorter
            if all batches finished early due to the `eos_token_id`.
        scores (`tuple(tf.Tensor)` *optional*, returned when `output_scores=True` is passed or when `config.output_scores=True`):
            Processed prediction scores of the language modeling head (scores for each vocabulary token before SoftMax)
            at each generation step. Tuple of `tf.Tensor` with up to `max_new_tokens` elements (one element for each
            generated token), with each tensor of shape `(batch_size, config.vocab_size)`.
        encoder_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer of the decoder) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.
        encoder_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings + one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.
        decoder_attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size, num_heads, generated_length, sequence_length)`.
        cross_attentions (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_attentions=True` is passed or `config.output_attentions=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size, num_heads, generated_length, sequence_length)`.
        decoder_hidden_states (`tuple(tuple(tf.Tensor))`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple (one element for each generated token) of tuples (one element for each layer of the decoder) of
            `tf.Tensor` of shape `(batch_size, generated_length, hidden_size)`.
    """
    sequences: tf.Tensor = ...
    scores: Optional[Tuple[tf.Tensor]] = ...
    encoder_attentions: Optional[Tuple[tf.Tensor]] = ...
    encoder_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    decoder_attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    cross_attentions: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    decoder_hidden_states: Optional[Tuple[Tuple[tf.Tensor]]] = ...
    def __init__(self, sequences, scores, encoder_attentions, encoder_hidden_states, decoder_attentions, cross_attentions, decoder_hidden_states) -> None: ...
TFGreedySearchOutput = Union[TFGreedySearchEncoderDecoderOutput, TFGreedySearchDecoderOnlyOutput]
TFSampleOutput = Union[TFSampleEncoderDecoderOutput, TFSampleDecoderOnlyOutput]
TFBeamSearchOutput = Union[TFBeamSearchEncoderDecoderOutput, TFBeamSearchDecoderOnlyOutput]
TFBeamSampleOutput = Union[TFBeamSampleEncoderDecoderOutput, TFBeamSampleDecoderOnlyOutput]
TFContrastiveSearchOutput = Union[TFContrastiveSearchEncoderDecoderOutput, TFContrastiveSearchDecoderOnlyOutput]
TFGenerateOutput = Union[TFGreedySearchOutput, TFSampleOutput, TFBeamSearchOutput, TFBeamSampleOutput, TFContrastiveSearchOutput]

class TFGenerationMixin:
    """
    A class containing all of the functions supporting generation, to be used as a mixin in [`TFPreTrainedModel`].

    The class exposes [`~generation.TFGenerationMixin.generate`], which can be used for:
        - *greedy decoding* by calling [`~generation.TFGenerationMixin.greedy_search`] if `num_beams=1` and
          `do_sample=False`
        - *contrastive search* by calling [`~generation.TFGenerationMixin.contrastive_search`] if `penalty_alpha>0` and
          `top_k>1`
        - *multinomial sampling* by calling [`~generation.TFGenerationMixin.sample`] if `num_beams=1` and
          `do_sample=True`
        - *beam-search decoding* by calling [`~generation.TFGenerationMixin.beam_search`] if `num_beams>1`

    You do not need to call any of the above methods directly. Pass custom parameter values to 'generate' instead. To
    learn more about decoding strategies refer to the [text generation strategies guide](./generation_strategies).
    """
    @property
    def seed_generator(self): ...
    supports_xla_generation: bool
    def prepare_inputs_for_generation(self, *args, **kwargs) -> None: ...
    def adjust_logits_during_generation(self, logits, cur_len, max_length, forced_bos_token_id, forced_eos_token_id, **kwargs):
        """
        Implement in subclasses of [`PreTrainedModel`] for custom behavior to adjust the logits in the generate method.
        """
    generation_config: Incomplete
    def generate(self, input_ids: Optional[tf.Tensor] = None, generation_config: Optional[GenerationConfig] = None, seed: Incomplete | None = None, **kwargs) -> Union[TFGenerateOutput, tf.Tensor]:
        """
        Generates sequences of token ids for models with a language modeling head.

        <Tip warning={true}>

        Most generation-controlling parameters are set in `generation_config` which, if not passed, will be set to the
        model's default generation configuration. You can override any `generation_config` by passing the corresponding
        parameters to generate, e.g. `.generate(inputs, num_beams=4, do_sample=True)`.

        For an overview of generation strategies and code examples, check out the [following
        guide](./generation_strategies).

        </Tip>

        Parameters:
            input_ids (`tf.Tensor` of `dtype=tf.int32` and shape `(batch_size, sequence_length)`, *optional*):
                The sequence used as a prompt for the generation. If `None` the method initializes it with
                `bos_token_id` and a batch size of 1.
            generation_config (`~generation.GenerationConfig`, *optional*):
                The generation configuration to be used as base parametrization for the generation call. `**kwargs`
                passed to generate matching the attributes of `generation_config` will override them. If
                `generation_config` is not provided, the default will be used, which had the following loading
                priority: 1) from the `generation_config.json` model file, if it exists; 2) from the model
                configuration. Please note that unspecified parameters will inherit [`~generation.GenerationConfig`]'s
                default values, whose documentation should be checked to parameterize generation.
            seed (`List[int]`, *optional*):
                Random seed to control sampling, containing two integers, used when `do_sample` is `True`. See the
                `seed` argument from stateless functions in `tf.random`.
            kwargs:
                Ad hoc parametrization of `generate_config` and/or additional model-specific kwargs that will be
                forwarded to the `forward` function of the model. If the model is an encoder-decoder model, encoder
                specific kwargs should not be prefixed and decoder specific kwargs should be prefixed with *decoder_*.

        Return:
            [`~utils.ModelOutput`] or `tf.Tensor`: A [`~utils.ModelOutput`] (if `return_dict_in_generate=True` or when
            `config.return_dict_in_generate=True`) or a `tf.Tensor`.

                If the model is *not* an encoder-decoder model (`model.config.is_encoder_decoder=False`), the possible
                [`~utils.ModelOutput`] types are:

                    - [`~generation.TFGreedySearchDecoderOnlyOutput`],
                    - [`~generation.TFSampleDecoderOnlyOutput`],
                    - [`~generation.TFBeamSearchDecoderOnlyOutput`],
                    - [`~generation.TFBeamSampleDecoderOnlyOutput`]

                If the model is an encoder-decoder model (`model.config.is_encoder_decoder=True`), the possible
                [`~utils.ModelOutput`] types are:

                    - [`~generation.TFGreedySearchEncoderDecoderOutput`],
                    - [`~generation.TFSampleEncoderDecoderOutput`],
                    - [`~generation.TFBeamSearchEncoderDecoderOutput`],
                    - [`~generation.TFBeamSampleEncoderDecoderOutput`]

        """
    def greedy_search(self, input_ids: tf.Tensor, max_length: Optional[int] = None, pad_token_id: Optional[int] = None, eos_token_id: Optional[int] = None, logits_processor: Optional[TFLogitsProcessorList] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_scores: Optional[bool] = None, return_dict_in_generate: Optional[bool] = None, **model_kwargs) -> Union[TFGreedySearchOutput, tf.Tensor]:
        '''
        Generates sequences for models with a language modeling head using greedy decoding.

        Parameters:
            input_ids (`tf.Tensor` of shape `(batch_size, sequence_length)`):
                The sequence used as a prompt for the generation.
            logits_processor (`TFLogitsProcessorList`, *optional*):
                An instance of [`TFLogitsProcessorList`]. List of instances of class derived from [`TFLogitsProcessor`]
                used to modify the prediction scores of the language modeling head applied at each generation step.
            max_length (`int`, *optional*, defaults to 20):
                The maximum length of the sequence to be generated.
            pad_token_id (`int`, *optional*):
                The id of the *padding* token.
            eos_token_id (`int`, *optional*):
                The id of the *end-of-sequence* token.
            output_attentions (`bool`, *optional*, defaults to `False`):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more details.
            output_hidden_states (`bool`, *optional*, defaults to `False`):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more details.
            output_scores (`bool`, *optional*, defaults to `False`):
                Whether or not to return the prediction scores. See `scores` under returned tensors for more details.
            return_dict_in_generate (`bool`, *optional*, defaults to `False`):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
            model_kwargs:
                Additional model specific keyword arguments will be forwarded to the `call` function of the model. If
                model is an encoder-decoder model the kwargs should include `encoder_outputs`.

        Return:
            [`~generation.TFGreedySearchDecoderOnlyOutput`], [`~generation.TFGreedySearchEncoderDecoderOutput`] or
            `tf.Tensor`: A `tf.Tensor` containing the generated tokens (default behaviour) or a
            [`~generation.TFGreedySearchDecoderOnlyOutput`] if `model.config.is_encoder_decoder=False` and
            `return_dict_in_generate=True` or a [`~generation.TFGreedySearchEncoderDecoderOutput`] if
            `model.config.is_encoder_decoder=True`.

        Examples:

        ```python
        >>> from transformers import (
        ...     AutoTokenizer,
        ...     TFAutoModelForCausalLM,
        ...     TFLogitsProcessorList,
        ...     TFMinLengthLogitsProcessor,
        ... )

        >>> tokenizer = AutoTokenizer.from_pretrained("gpt2")
        >>> model = TFAutoModelForCausalLM.from_pretrained("gpt2")

        >>> # set pad_token_id to eos_token_id because GPT2 does not have a PAD token
        >>> model.generation_config.pad_token_id = model.generation_config.eos_token_id

        >>> input_prompt = "Today is a beautiful day, and"
        >>> input_ids = tokenizer(input_prompt, return_tensors="tf").input_ids

        >>> # instantiate logits processors
        >>> logits_processor = TFLogitsProcessorList(
        ...     [
        ...         TFMinLengthLogitsProcessor(15, eos_token_id=model.generation_config.eos_token_id),
        ...     ]
        ... )

        >>> outputs = model.greedy_search(input_ids, logits_processor=logits_processor)
        >>> tokenizer.batch_decode(outputs, skip_special_tokens=True)
        ["Today is a beautiful day, and I\'m so happy to be here. I\'m so happy to"]
        ```'''
    def sample(self, input_ids: tf.Tensor, logits_processor: Optional[TFLogitsProcessorList] = None, logits_warper: Optional[TFLogitsProcessorList] = None, max_length: Optional[int] = None, pad_token_id: Optional[int] = None, eos_token_id: Optional[int] = None, seed: Optional[Tuple[int, int]] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_scores: Optional[bool] = None, return_dict_in_generate: Optional[bool] = None, **model_kwargs) -> Union[TFSampleOutput, tf.Tensor]:
        '''
        Generates sequences for models with a language modeling head using multinomial sampling.

        Parameters:
            input_ids (`tf.Tensor` of shape `(batch_size, sequence_length)`):
                The sequence used as a prompt for the generation.
            logits_processor (`TFLogitsProcessorList`, *optional*):
                An instance of [`TFLogitsProcessorList`]. List of instances of class derived from [`TFLogitsProcessor`]
                used to modify the prediction scores of the language modeling head applied at each generation step.
            logits_warper (`TFLogitsProcessorList`, *optional*):
                An instance of [`TFLogitsProcessorList`]. List of instances of class derived from [`TFLogitsWarper`]
                used to warp the prediction score distribution of the language modeling head applied before multinomial
                sampling at each generation step.
            max_length (`int`, *optional*, defaults to 20):
                The maximum length of the sequence to be generated.
            pad_token_id (`int`, *optional*):
                The id of the *padding* token.
            eos_token_id (`int`, *optional*):
                The id of the *end-of-sequence* token.
            seed (`List[int]`, *optional*):
                Random seed to control sampling, containing two integers, used when `do_sample` is `True`. See the
                `seed` argument from stateless functions in `tf.random`.
            output_attentions (`bool`, *optional*, defaults to `False`):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more details.
            output_hidden_states (`bool`, *optional*, defaults to `False`):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more details.
            output_scores (`bool`, *optional*, defaults to `False`):
                Whether or not to return the prediction scores. See `scores` under returned tensors for more details.
            return_dict_in_generate (`bool`, *optional*, defaults to `False`):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
            model_kwargs:
                Additional model specific kwargs will be forwarded to the `call` function of the model. If model is an
                encoder-decoder model the kwargs should include `encoder_outputs`.

        Return:
            [`~generation.TFSampleDecoderOnlyOutput`], [`~generation.TFSampleEncoderDecoderOutput`] or `tf.Tensor`: A
            `tf.Tensor` containing the generated tokens (default behaviour) or a
            [`~generation.TFSampleDecoderOnlyOutput`] if `model.config.is_encoder_decoder=False` and
            `return_dict_in_generate=True` or a [`~generation.TFSampleEncoderDecoderOutput`] if
            `model.config.is_encoder_decoder=True`.

        Examples:

        ```python
        >>> import tensorflow as tf
        >>> from transformers import (
        ...     AutoTokenizer,
        ...     TFAutoModelForCausalLM,
        ...     TFLogitsProcessorList,
        ...     TFMinLengthLogitsProcessor,
        ...     TFTopKLogitsWarper,
        ...     TFTemperatureLogitsWarper,
        ... )

        >>> tokenizer = AutoTokenizer.from_pretrained("gpt2")
        >>> model = TFAutoModelForCausalLM.from_pretrained("gpt2")

        >>> # set pad_token_id to eos_token_id because GPT2 does not have a EOS token
        >>> model.generation_config.pad_token_id = model.generation_config.eos_token_id

        >>> input_prompt = "Today is a beautiful day, and"
        >>> input_ids = tokenizer(input_prompt, return_tensors="tf").input_ids

        >>> # instantiate logits processors
        >>> logits_processor = TFLogitsProcessorList(
        ...     [
        ...         TFMinLengthLogitsProcessor(15, eos_token_id=model.generation_config.eos_token_id),
        ...     ]
        ... )
        >>> # instantiate logits processors
        >>> logits_warper = TFLogitsProcessorList(
        ...     [
        ...         TFTopKLogitsWarper(50),
        ...         TFTemperatureLogitsWarper(0.7),
        ...     ]
        ... )

        >>> tf.random.set_seed(0)
        >>> outputs = model.sample(input_ids, logits_processor=logits_processor, logits_warper=logits_warper)

        >>> tokenizer.batch_decode(outputs, skip_special_tokens=True)
        [\'Today is a beautiful day, and I love my country. But when I look at Donald Trump,\']
        ```'''
    def beam_search(self, input_ids: tf.Tensor, do_sample: bool = False, max_length: Optional[int] = None, pad_token_id: Optional[int] = None, eos_token_id: Optional[int] = None, length_penalty: Optional[float] = None, early_stopping: Optional[bool] = None, logits_processor: Optional[TFLogitsProcessorList] = None, logits_warper: Optional[TFLogitsProcessorList] = None, num_return_sequences: Optional[int] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_scores: Optional[bool] = None, return_dict_in_generate: Optional[bool] = None, **model_kwargs) -> Union[TFBeamSearchOutput, TFBeamSampleOutput, tf.Tensor]:
        '''
        Generates sequences for models with a language modeling head using beam search. If `do_sample` is `False`, uses
        a greedy approach, otherwise does multinomial sampling without replacement.

        Parameters:
            input_ids (`tf.Tensor` of shape `(batch_size, sequence_length)`):
                The sequence used as a prompt for the generation.
            do_sample (`bool`, *optional*, defaults to `False`):
                Whether or not to use sampling ; use greedy decoding otherwise.
            max_length (`int`, *optional*, defaults to 20):
                The maximum length of the sequence to be generated.
            pad_token_id (`int`, *optional*):
                The id of the *padding* token.
            eos_token_id (`int`, *optional*):
                The id of the *end-of-sequence* token.
            length_penalty (`float`, *optional*, defaults to 1.0):
                Exponential penalty to the length that is used with beam-based generation. It is applied as an exponent
                to the sequence length, which in turn is used to divide the score of the sequence. Since the score is
                the log likelihood of the sequence (i.e. negative), `length_penalty` > 0.0 promotes longer sequences,
                while `length_penalty` < 0.0 encourages shorter sequences.
            early_stopping (`bool`, *optional*, defaults to `False`):
                Whether to stop the beam search when at least `num_beams` sentences are finished per batch or not.
            logits_processor (`[TFLogitsProcessorList]`, *optional*):
                An instance of [`TFLogitsProcessorList`]. List of instances of class derived from [`TFLogitsProcessor`]
                used to modify the prediction scores of the language modeling head applied at each generation step.
            logits_warper (`TFLogitsProcessorList`, *optional*):
                An instance of [`TFLogitsProcessorList`]. List of instances of class derived from [`TFLogitsWarper`]
                used to warp the prediction score distribution of the language modeling head applied before multinomial
                sampling at each generation step.
            num_return_sequences(`int`, *optional*, defaults to 1):
                The number of independently computed returned sequences for each element in the batch.
            output_attentions (`bool`, *optional*, defaults to `False`):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more details.
            output_hidden_states (`bool`, *optional*, defaults to `False`):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more details.
            return_dict_in_generate (`bool`, *optional*, defaults to `False`):
                Whether or not to return a [`~file_utils.ModelOutput`] instead of a plain tuple.
            model_kwargs:
                Additional model specific kwargs will be forwarded to the `call` function of the model. If model is an
                encoder-decoder model the kwargs should include `encoder_outputs`.

        Return:
            [`~generation.TFBeamSearchDecoderOnlyOutput`], [`~generation.TFBeamSearchEncoderDecoderOutput`] or
            `tf.Tensor`: A `tf.Tensor` containing the generated tokens (default behaviour) or a
            [`~generation.TFBeamSearchDecoderOnlyOutput`] if `model.config.is_encoder_decoder=False` and
            `return_dict_in_generate=True` or a [`~generation.TFBeamSearchEncoderDecoderOutput`] if
            `model.config.is_encoder_decoder=True`.

        Examples:

        ```python
        >>> from transformers import (
        ...     AutoTokenizer,
        ...     TFAutoModelForSeq2SeqLM,
        ...     TFLogitsProcessorList,
        ...     TFMinLengthLogitsProcessor,
        ... )
        >>> import tensorflow as tf

        >>> tokenizer = AutoTokenizer.from_pretrained("t5-base")
        >>> model = TFAutoModelForSeq2SeqLM.from_pretrained("t5-base")

        >>> encoder_input_str = "translate English to German: How old are you?"
        >>> encoder_input_ids = tokenizer(encoder_input_str, return_tensors="tf").input_ids

        >>> # lets run beam search using 3 beams
        >>> num_beams = 3
        >>> # define decoder start token ids
        >>> input_ids = tf.ones((1, num_beams, 1), dtype=tf.int32)
        >>> input_ids = input_ids * model.generation_config.decoder_start_token_id

        >>> # add encoder_outputs to model keyword arguments
        >>> encoder_outputs = model.get_encoder()(encoder_input_ids, return_dict=True)
        >>> encoder_outputs.last_hidden_state = tf.repeat(
        ...     tf.expand_dims(encoder_outputs.last_hidden_state, axis=0), num_beams, axis=1
        ... )
        >>> model_kwargs = {"encoder_outputs": encoder_outputs}

        >>> # instantiate logits processors
        >>> logits_processor = TFLogitsProcessorList(
        ...     [TFMinLengthLogitsProcessor(5, eos_token_id=model.generation_config.eos_token_id)]
        ... )

        >>> outputs = model.beam_search(input_ids, logits_processor=logits_processor, **model_kwargs)
        >>> tokenizer.batch_decode(outputs, skip_special_tokens=True)
        [\'Wie alt bist du?\']
        ```'''
    def contrastive_search(self, input_ids: tf.Tensor, top_k: Optional[int] = 1, penalty_alpha: Optional[float] = 0, logits_processor: Optional[TFLogitsProcessorList] = None, logits_warper: Optional[TFLogitsProcessorList] = None, max_length: Optional[int] = None, pad_token_id: Optional[int] = None, eos_token_id: Optional[int] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_scores: Optional[bool] = None, return_dict_in_generate: Optional[bool] = None, **model_kwargs) -> Union[TFContrastiveSearchOutput, tf.Tensor]:
        '''
        Generates sequences of token ids for models with a language modeling head using **contrastive search** and can
        be used for text-decoder, text-to-text, speech-to-text, and vision-to-text models.

        Parameters:
            input_ids (`tf.Tensor` of shape `(batch_size, sequence_length)`):
                The sequence used as a prompt for the generation.
            top_k (`int`, *optional*, defaults to 1):
                The size of the candidate set that is used to re-rank for contrastive search
            penalty_alpha (`float`, *optional*, defaults to 0):
                The degeneration penalty for contrastive search; activate when it is larger than 0
            logits_processor (`TFLogitsProcessorList`, *optional*):
                An instance of [`TFLogitsProcessorList`]. List of instances of class derived from [`TFLogitsProcessor`]
                used to modify the prediction scores of the language modeling head applied at each generation step.
            logits_warper (`TFLogitsProcessorList`, *optional*):
                An instance of [`TFLogitsProcessorList`]. List of instances of class derived from [`TFLogitsWarper`]
                used to warp the prediction score distribution of the language modeling head applied before multinomial
                sampling at each generation step.
            max_length (`int`, *optional*, defaults to 20):
                The maximum length of the sequence to be generated.
            pad_token_id (`int`, *optional*):
                The id of the *padding* token.
            eos_token_id (`int`, *optional*):
                The id of the *end-of-sequence* token.
            output_attentions (`bool`, *optional*, defaults to `False`):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more details.
            output_hidden_states (`bool`, *optional*, defaults to `False`):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more details.
            output_scores (`bool`, *optional*, defaults to `False`):
                Whether or not to return the prediction scores. See `scores` under returned tensors for more details.
            return_dict_in_generate (`bool`, *optional*, defaults to `False`):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
            model_kwargs:
                Additional model specific keyword arguments will be forwarded to the `call` function of the model. If
                model is an encoder-decoder model the kwargs should include `encoder_outputs`.
        Return:
            [`~generation.TFContrastiveSearchDecoderOnlyOutput`],
            [`~generation.TFContrastiveSearchEncoderDecoderOutput`] or `tf.Tensor`: A `tf.Tensor` containing the
            generated tokens (default behaviour) or a [`~generation.TFContrastiveySearchDecoderOnlyOutput`] if
            `model.config.is_encoder_decoder=False` and `return_dict_in_generate=True` or a
            [`~generation.TFContrastiveSearchEncoderDecoderOutput`] if `model.config.is_encoder_decoder=True`.
        Examples:
        ```python
        >>> from transformers import AutoTokenizer, TFAutoModelForCausalLM

        >>> tokenizer = AutoTokenizer.from_pretrained("facebook/opt-125m")
        >>> model = TFAutoModelForCausalLM.from_pretrained("facebook/opt-125m")
        >>> # set pad_token_id to eos_token_id because OPT does not have a PAD token
        >>> model.config.pad_token_id = model.config.eos_token_id
        >>> input_prompt = "DeepMind Company is"
        >>> input_ids = tokenizer(input_prompt, return_tensors="tf")
        >>> outputs = model.contrastive_search(**input_ids, penalty_alpha=0.6, top_k=4, max_length=64)
        >>> tokenizer.batch_decode(outputs, skip_special_tokens=True)
        [\'DeepMind Company is a company that focuses on the development and commercialization of artificial intelligence (AI). DeepMind’s mission is to help people understand and solve problems that are difficult to solve in the world today.\\n\\nIn this post, we talk about the benefits of deep learning in business and how it\']
        ```'''

def tf_top_k_top_p_filtering(logits, top_k: int = 0, top_p: float = 1.0, filter_value=..., min_tokens_to_keep: int = 1):
    """
    Filter a distribution of logits using top-k and/or nucleus (top-p) filtering

    Args:
        logits: logits distribution shape (batch size, vocabulary size)
        top_k (`int`, *optional*, defaults to 0):
            If > 0, only keep the top k tokens with highest probability (top-k filtering)
        top_p (`float`, *optional*, defaults to 1.0):
            If < 1.0, only keep the top tokens with cumulative probability >= top_p (nucleus filtering). Nucleus
            filtering is described in Holtzman et al. (http://arxiv.org/abs/1904.09751)
        min_tokens_to_keep (`int`, *optional*, defaults to 1):
            Minimumber of tokens we keep per batch example in the output.

    From: https://gist.github.com/thomwolf/1a5a29f6962089e871b94cbd09daf317
    """
def scatter_values_on_batch_indices(values, batch_indices): ...
def sample_without_replacement(logits, num_samples):
    """
    categorical sampling without replacement is currently not implemented the gumbel-max trick will do for now see
    https://github.com/tensorflow/tensorflow/issues/9260 for more info
    """
