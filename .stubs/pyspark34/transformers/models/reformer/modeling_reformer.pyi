import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import CausalLMOutput as CausalLMOutput, MaskedLMOutput as MaskedLMOutput, QuestionAnsweringModelOutput as QuestionAnsweringModelOutput, SequenceClassifierOutput as SequenceClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward
from ...utils import DUMMY_INPUTS as DUMMY_INPUTS, DUMMY_MASK as DUMMY_MASK, ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_reformer import ReformerConfig as ReformerConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from torch.autograd.function import Function
from typing import List, NamedTuple, Optional, Tuple, Union

logger: Incomplete
REFORMER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class LSHSelfAttentionOutput(NamedTuple):
    hidden_states: Incomplete
    attention_probs: Incomplete
    buckets: Incomplete

class LocalSelfAttentionOutput(NamedTuple):
    hidden_states: Incomplete
    attention_probs: Incomplete

class AttentionOutput(NamedTuple):
    hidden_states: Incomplete
    attention_probs: Incomplete
    buckets: Incomplete

class ReformerOutput(NamedTuple):
    hidden_states: Incomplete
    attn_output: Incomplete
    attention_probs: Incomplete
    buckets: Incomplete

class ReformerBackwardOutput(NamedTuple):
    attn_output: Incomplete
    hidden_states: Incomplete
    grad_attn_output: Incomplete
    grad_hidden_states: Incomplete

class ReformerEncoderOutput(NamedTuple):
    hidden_states: Incomplete
    all_hidden_states: Incomplete
    all_attentions: Incomplete
    past_buckets_states: Incomplete

class AxialPositionEmbeddings(nn.Module):
    """
    Constructs axial position embeddings. Useful for very long input sequences to save memory and time.
    """
    axial_pos_shape: Incomplete
    axial_pos_embds_dim: Incomplete
    dropout: Incomplete
    least_common_mult_chunk_length: Incomplete
    weights: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, position_ids): ...

class PositionEmbeddings(nn.Module):
    """Constructs conventional position embeddings of shape `[max_pos_embeddings, hidden_size]`."""
    dropout: Incomplete
    embedding: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, position_ids): ...

class ReformerEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    max_position_embeddings: Incomplete
    dropout: Incomplete
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, start_idx_pos_encodings: int = 0): ...

class EfficientAttentionMixin:
    """
    A few utilities for nn.Modules in Reformer, to be used as a mixin.
    """

class LSHSelfAttention(nn.Module, EfficientAttentionMixin):
    config: Incomplete
    chunk_length: Incomplete
    num_hashes: Incomplete
    num_buckets: Incomplete
    num_chunks_before: Incomplete
    num_chunks_after: Incomplete
    hash_seed: Incomplete
    is_decoder: Incomplete
    max_position_embeddings: Incomplete
    dropout: Incomplete
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    hidden_size: Incomplete
    query_key: Incomplete
    value: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, num_hashes: Incomplete | None = None, buckets: Incomplete | None = None, past_buckets_states: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False, **kwargs): ...

class ReverseSort(Function):
    """
    After chunked attention is applied which sorted clusters, original ordering has to be restored. Since customized
    backward function is used for Reformer, the gradients of the output vectors have to be explicitly sorted here.
    """
    @staticmethod
    def forward(ctx, out_vectors, logits, sorted_bucket_idx, undo_sorted_bucket_idx): ...
    @staticmethod
    def backward(ctx, grad_out_vectors, grad_logits): ...

class LocalSelfAttention(nn.Module, EfficientAttentionMixin):
    num_attention_heads: Incomplete
    chunk_length: Incomplete
    num_chunks_before: Incomplete
    num_chunks_after: Incomplete
    is_decoder: Incomplete
    pad_token_id: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    hidden_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, past_buckets_states: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False, **kwargs): ...

class ReformerSelfOutput(nn.Module):
    dropout: Incomplete
    dense: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class ReformerAttention(nn.Module):
    layer_id: Incomplete
    attn_layers: Incomplete
    layer_norm: Incomplete
    self_attention: Incomplete
    output: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, num_hashes: Incomplete | None = None, past_buckets_states: Incomplete | None = None, use_cache: bool = False, orig_sequence_length: Incomplete | None = None, output_attentions: bool = False, buckets: Incomplete | None = None): ...

class ReformerFeedForwardDense(nn.Module):
    dropout: Incomplete
    act_fn: Incomplete
    dense: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class ReformerFeedForwardOutput(nn.Module):
    dropout: Incomplete
    dense: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class ChunkReformerFeedForward(nn.Module):
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    layer_norm: Incomplete
    dense: Incomplete
    output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, attention_output): ...
    def forward_chunk(self, hidden_states): ...

class ReformerLayer(nn.Module):
    attention: Incomplete
    attention_seed: Incomplete
    feed_forward_seed: Incomplete
    feed_forward: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, prev_attn_output, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, num_hashes: Incomplete | None = None, past_buckets_states: Incomplete | None = None, use_cache: bool = False, orig_sequence_length: Incomplete | None = None, output_attentions: bool = False): ...
    def backward_pass(self, next_attn_output, hidden_states, grad_attn_output, grad_hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, buckets: Incomplete | None = None): ...

class _ReversibleFunction(Function):
    """
    To prevent PyTorch from performing the usual backpropagation, a customized backward function is implemented here.
    This way it is made sure that no memory expensive activations are saved during the forward pass. This function is
    heavily inspired by https://github.com/lucidrains/reformer-pytorch/blob/master/reformer_pytorch/reversible.py
    """
    @staticmethod
    def forward(ctx, hidden_states, layers, attention_mask, head_mask, num_hashes, all_hidden_states, all_attentions, past_buckets_states, use_cache, orig_sequence_length, output_hidden_states, output_attentions): ...
    @staticmethod
    def backward(ctx, grad_hidden_states): ...

class ReformerEncoder(nn.Module):
    dropout: Incomplete
    layers: Incomplete
    layer_norm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, num_hashes: Incomplete | None = None, past_buckets_states: Incomplete | None = None, use_cache: bool = False, orig_sequence_length: Incomplete | None = None, output_hidden_states: bool = False, output_attentions: bool = False): ...

class ReformerOnlyLMHead(nn.Module):
    seq_len_dim: int
    chunk_size_lm_head: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...
    def forward_chunk(self, hidden_states): ...

class ReformerPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ReformerConfig
    base_model_prefix: str
    @property
    def dummy_inputs(self): ...

@dataclass
class ReformerModelOutput(ModelOutput):
    """
    Output type of [`ReformerModel`].

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, num_predict, hidden_size)`):
            Sequence of hidden-states at the last layer of the model.

            `num_predict` corresponds to `target_mapping.shape[1]`. If `target_mapping` is `None`, then `num_predict`
            corresponds to `sequence_length`.
        past_buckets_states (`List[Tuple(torch.LongTensor, torch.FloatTensor)]`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            List of `Tuple(torch.LongTensor, torch.FloatTensor` of length `config.n_layers`, with the first element
            being the previous *buckets* of shape `(batch_size, num_heads, num_hashes, sequence_length)`) and the
            second being the previous *hidden_states* of shape `(batch_size, sequence_length, hidden_size)`).

            Contains precomputed buckets and hidden-states that can be used (see `past_buckets_states` input) to speed
            up sequential decoding.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings and one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    last_hidden_state: torch.FloatTensor
    past_buckets_states: Optional[List[Tuple[torch.LongTensor, torch.FloatTensor]]] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, past_buckets_states, hidden_states, attentions) -> None: ...

@dataclass
class ReformerModelWithLMHeadOutput(ModelOutput):
    """
    Output type of [`ReformerModelWithLMHead`].

    Args:
        loss (`torch.FloatTensor` of shape *(1,)*, *optional*, returned when `labels` is provided)
            Language modeling loss (for next-token prediction).
        logits (`torch.FloatTensor` of shape `(batch_size, num_predict, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).

            `num_predict` corresponds to `target_mapping.shape[1]`. If `target_mapping` is `None`, then `num_predict`
            corresponds to `sequence_length`.
        past_buckets_states (`List[Tuple(torch.LongTensor, torch.FloatTensor)]`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            List of `Tuple(torch.LongTensor, torch.FloatTensor` of length `config.n_layers`, with the first element
            being the previous *buckets* of shape `(batch_size, num_heads, num_hashes, sequence_length)`) and the
            second being the previous *hidden_states* of shape `(batch_size, sequence_length, hidden_size)`).

            Contains precomputed buckets and hidden-states that can be used (see `past_buckets_states` input) to speed
            up sequential decoding.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            TTuple of `torch.FloatTensor` (one for the output of the embeddings and one for the output of each layer)
            of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    past_buckets_states: Optional[List[Tuple[torch.LongTensor, torch.FloatTensor]]] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, past_buckets_states, hidden_states, attentions) -> None: ...

REFORMER_START_DOCSTRING: str
REFORMER_INPUTS_DOCSTRING: str

class ReformerModel(ReformerPreTrainedModel):
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, num_hashes: Optional[int] = None, past_buckets_states: Optional[List[Tuple[torch.Tensor]]] = None, use_cache: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_attentions: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, ReformerModelOutput]: ...

class ReformerModelWithLMHead(ReformerPreTrainedModel):
    reformer: Incomplete
    lm_head: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, num_hashes: Optional[int] = None, past_buckets_states: Optional[List[Tuple[torch.Tensor]]] = None, use_cache: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_attentions: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[torch.Tensor] = None) -> Union[Tuple, CausalLMOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
                Labels for computing the sequence classification/regression loss. Indices should be in `[-100, 0, ...,
                config.vocab_size - 1]`. All labels set to `-100` are ignored (masked), the loss is only computed for
                labels in `[0, ..., config.vocab_size]`
        """
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, num_hashes: Incomplete | None = None, **kwargs): ...

class ReformerForMaskedLM(ReformerPreTrainedModel):
    reformer: Incomplete
    lm_head: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, num_hashes: Optional[int] = None, labels: Optional[torch.Tensor] = None, output_hidden_states: Optional[bool] = None, output_attentions: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, MaskedLMOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
                Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
                config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked),
                the loss is only computed for the tokens with labels

        Returns:

        <Tip warning={true}>

        This example uses a false checkpoint since we don\'t have any available pretrained model for the masked language
        modeling task with the Reformer architecture.

        </Tip>

        Example:

        ```python
        >>> import torch
        >>> from transformers import AutoTokenizer, ReformerForMaskedLM

        >>> tokenizer = AutoTokenizer.from_pretrained("hf-internal-testing/tiny-random-reformer")
        >>> model = ReformerForMaskedLM.from_pretrained("hf-internal-testing/tiny-random-reformer")

        >>> # add mask_token
        >>> tokenizer.add_special_tokens({"mask_token": "[MASK]"})  # doctest: +IGNORE_RESULT
        >>> inputs = tokenizer("The capital of France is [MASK].", return_tensors="pt")

        >>> # resize model\'s embedding matrix
        >>> model.resize_token_embeddings(new_num_tokens=model.config.vocab_size + 1)  # doctest: +IGNORE_RESULT

        >>> with torch.no_grad():
        ...     logits = model(**inputs).logits

        >>> # retrieve index of [MASK]
        >>> mask_token_index = (inputs.input_ids == tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]

        >>> predicted_token_id = logits[0, mask_token_index].argmax(axis=-1)
        >>> predicted_token = tokenizer.decode(predicted_token_id)
        ```

        ```python
        >>> labels = tokenizer("The capital of France is Paris.", return_tensors="pt")["input_ids"]
        >>> # mask labels of non-[MASK] tokens
        >>> labels = torch.where(
        ...     inputs.input_ids == tokenizer.mask_token_id, labels[:, : inputs["input_ids"].shape[-1]], -100
        ... )

        >>> outputs = model(**inputs, labels=labels)
        >>> loss = round(outputs.loss.item(), 2)
        ```
        '''

class ReformerForSequenceClassification(ReformerPreTrainedModel):
    num_labels: Incomplete
    config: Incomplete
    reformer: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, num_hashes: Optional[int] = None, labels: Optional[torch.Tensor] = None, output_hidden_states: Optional[bool] = None, output_attentions: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, SequenceClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Example of single-label classification:

        ```python
        >>> import torch
        >>> from transformers import AutoTokenizer, ReformerForSequenceClassification

        >>> tokenizer = AutoTokenizer.from_pretrained("google/reformer-crime-and-punishment")
        >>> model = ReformerForSequenceClassification.from_pretrained("google/reformer-crime-and-punishment")

        >>> inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")

        >>> with torch.no_grad():
        ...     logits = model(**inputs).logits

        >>> predicted_class_id = logits.argmax().item()
        >>> label = model.config.id2label[predicted_class_id]
        ```

        ```python
        >>> # To train a model on `num_labels` classes, you can pass `num_labels=num_labels` to `.from_pretrained(...)`
        >>> num_labels = len(model.config.id2label)
        >>> model = ReformerForSequenceClassification.from_pretrained(
        ...     "google/reformer-crime-and-punishment", num_labels=num_labels
        ... )

        >>> labels = torch.tensor(1)
        >>> loss = model(**inputs, labels=labels).loss
        ```
        '''

class ReformerClassificationHead(nn.Module):
    """Head for sentence-level classification tasks."""
    dense: Incomplete
    dropout: Incomplete
    out_proj: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, **kwargs): ...

class ReformerForQuestionAnswering(ReformerPreTrainedModel):
    num_labels: Incomplete
    reformer: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, num_hashes: Optional[int] = None, start_positions: Optional[torch.Tensor] = None, end_positions: Optional[torch.Tensor] = None, output_hidden_states: Optional[bool] = None, output_attentions: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, QuestionAnsweringModelOutput]:
        """
        start_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        """
