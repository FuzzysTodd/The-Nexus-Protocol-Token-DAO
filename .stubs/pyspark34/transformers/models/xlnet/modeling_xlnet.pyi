import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_utils import PoolerAnswerClass as PoolerAnswerClass, PoolerEndLogits as PoolerEndLogits, PoolerStartLogits as PoolerStartLogits, PreTrainedModel as PreTrainedModel, SequenceSummary as SequenceSummary
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_xlnet import XLNetConfig as XLNetConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import List, Optional, Tuple, Union

logger: Incomplete
XLNET_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def build_tf_xlnet_to_pytorch_map(model, config, tf_weights: Incomplete | None = None):
    """
    A map of modules from TF to PyTorch. I use a map to keep the PyTorch model as identical to the original PyTorch
    model as possible.
    """
def load_tf_weights_in_xlnet(model, config, tf_path):
    """Load tf checkpoints in a pytorch model"""

class XLNetRelativeAttention(nn.Module):
    n_head: Incomplete
    d_head: Incomplete
    d_model: Incomplete
    scale: Incomplete
    q: Incomplete
    k: Incomplete
    v: Incomplete
    o: Incomplete
    r: Incomplete
    r_r_bias: Incomplete
    r_s_bias: Incomplete
    r_w_bias: Incomplete
    seg_embed: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def prune_heads(self, heads) -> None: ...
    @staticmethod
    def rel_shift(x, klen: int = -1):
        """perform relative shift to form the relative attention score."""
    @staticmethod
    def rel_shift_bnij(x, klen: int = -1): ...
    def rel_attn_core(self, q_head, k_head_h, v_head_h, k_head_r, seg_mat: Incomplete | None = None, attn_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False):
        """Core relative positional attention operations."""
    def post_attention(self, h, attn_vec, residual: bool = True):
        """Post-attention processing."""
    def forward(self, h, g, attn_mask_h, attn_mask_g, r, seg_mat, mems: Incomplete | None = None, target_mapping: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class XLNetFeedForward(nn.Module):
    layer_norm: Incomplete
    layer_1: Incomplete
    layer_2: Incomplete
    dropout: Incomplete
    activation_function: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, inp): ...

class XLNetLayer(nn.Module):
    rel_attn: Incomplete
    ff: Incomplete
    dropout: Incomplete
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    def __init__(self, config) -> None: ...
    def forward(self, output_h, output_g, attn_mask_h, attn_mask_g, r, seg_mat, mems: Incomplete | None = None, target_mapping: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...
    def ff_chunk(self, output_x): ...

class XLNetPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = XLNetConfig
    load_tf_weights = load_tf_weights_in_xlnet
    base_model_prefix: str

@dataclass
class XLNetModelOutput(ModelOutput):
    """
    Output type of [`XLNetModel`].

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, num_predict, hidden_size)`):
            Sequence of hidden-states at the last layer of the model.

            `num_predict` corresponds to `target_mapping.shape[1]`. If `target_mapping` is `None`, then `num_predict`
            corresponds to `sequence_length`.
        mems (`List[torch.FloatTensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states. Can be used (see `mems` input) to speed up sequential decoding. The
            token ids which have their past given to this model should not be passed as `input_ids` as they have
            already been computed.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    last_hidden_state: torch.FloatTensor
    mems: Optional[List[torch.FloatTensor]] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, mems, hidden_states, attentions) -> None: ...

@dataclass
class XLNetLMHeadModelOutput(ModelOutput):
    """
    Output type of [`XLNetLMHeadModel`].

    Args:
        loss (`torch.FloatTensor` of shape *(1,)*, *optional*, returned when `labels` is provided)
            Language modeling loss (for next-token prediction).
        logits (`torch.FloatTensor` of shape `(batch_size, num_predict, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).

            `num_predict` corresponds to `target_mapping.shape[1]`. If `target_mapping` is `None`, then `num_predict`
            corresponds to `sequence_length`.
        mems (`List[torch.FloatTensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states. Can be used (see `mems` input) to speed up sequential decoding. The
            token ids which have their past given to this model should not be passed as `input_ids` as they have
            already been computed.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    mems: Optional[List[torch.FloatTensor]] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, mems, hidden_states, attentions) -> None: ...

@dataclass
class XLNetForSequenceClassificationOutput(ModelOutput):
    """
    Output type of [`XLNetForSequenceClassification`].

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `label` is provided):
            Classification (or regression if config.num_labels==1) loss.
        logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels)`):
            Classification (or regression if config.num_labels==1) scores (before SoftMax).
        mems (`List[torch.FloatTensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states. Can be used (see `mems` input) to speed up sequential decoding. The
            token ids which have their past given to this model should not be passed as `input_ids` as they have
            already been computed.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    mems: Optional[List[torch.FloatTensor]] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, mems, hidden_states, attentions) -> None: ...

@dataclass
class XLNetForTokenClassificationOutput(ModelOutput):
    """
    Output type of [`XLNetForTokenClassificationOutput`].

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided) :
            Classification loss.
        logits (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.num_labels)`):
            Classification scores (before SoftMax).
        mems (`List[torch.FloatTensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states. Can be used (see `mems` input) to speed up sequential decoding. The
            token ids which have their past given to this model should not be passed as `input_ids` as they have
            already been computed.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    mems: Optional[List[torch.FloatTensor]] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, mems, hidden_states, attentions) -> None: ...

@dataclass
class XLNetForMultipleChoiceOutput(ModelOutput):
    """
    Output type of [`XLNetForMultipleChoice`].

    Args:
        loss (`torch.FloatTensor` of shape *(1,)*, *optional*, returned when `labels` is provided):
            Classification loss.
        logits (`torch.FloatTensor` of shape `(batch_size, num_choices)`):
            *num_choices* is the second dimension of the input tensors. (see *input_ids* above).

            Classification scores (before SoftMax).
        mems (`List[torch.FloatTensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states. Can be used (see `mems` input) to speed up sequential decoding. The
            token ids which have their past given to this model should not be passed as `input_ids` as they have
            already been computed.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    logits: torch.FloatTensor = ...
    mems: Optional[List[torch.FloatTensor]] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, mems, hidden_states, attentions) -> None: ...

@dataclass
class XLNetForQuestionAnsweringSimpleOutput(ModelOutput):
    """
    Output type of [`XLNetForQuestionAnsweringSimple`].

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Total span extraction loss is the sum of a Cross-Entropy for the start and end positions.
        start_logits (`torch.FloatTensor` of shape `(batch_size, sequence_length,)`):
            Span-start scores (before SoftMax).
        end_logits (`torch.FloatTensor` of shape `(batch_size, sequence_length,)`):
            Span-end scores (before SoftMax).
        mems (`List[torch.FloatTensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states. Can be used (see `mems` input) to speed up sequential decoding. The
            token ids which have their past given to this model should not be passed as `input_ids` as they have
            already been computed.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    start_logits: torch.FloatTensor = ...
    end_logits: torch.FloatTensor = ...
    mems: Optional[List[torch.FloatTensor]] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, start_logits, end_logits, mems, hidden_states, attentions) -> None: ...

@dataclass
class XLNetForQuestionAnsweringOutput(ModelOutput):
    """
    Output type of [`XLNetForQuestionAnswering`].

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned if both `start_positions` and `end_positions` are provided):
            Classification loss as the sum of start token, end token (and is_impossible if provided) classification
            losses.
        start_top_log_probs (`torch.FloatTensor` of shape `(batch_size, config.start_n_top)`, *optional*, returned if `start_positions` or `end_positions` is not provided):
            Log probabilities for the top config.start_n_top start token possibilities (beam-search).
        start_top_index (`torch.LongTensor` of shape `(batch_size, config.start_n_top)`, *optional*, returned if `start_positions` or `end_positions` is not provided):
            Indices for the top config.start_n_top start token possibilities (beam-search).
        end_top_log_probs (`torch.FloatTensor` of shape `(batch_size, config.start_n_top * config.end_n_top)`, *optional*, returned if `start_positions` or `end_positions` is not provided):
            Log probabilities for the top `config.start_n_top * config.end_n_top` end token possibilities
            (beam-search).
        end_top_index (`torch.LongTensor` of shape `(batch_size, config.start_n_top * config.end_n_top)`, *optional*, returned if `start_positions` or `end_positions` is not provided):
            Indices for the top `config.start_n_top * config.end_n_top` end token possibilities (beam-search).
        cls_logits (`torch.FloatTensor` of shape `(batch_size,)`, *optional*, returned if `start_positions` or `end_positions` is not provided):
            Log probabilities for the `is_impossible` label of the answers.
        mems (`List[torch.FloatTensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states. Can be used (see `mems` input) to speed up sequential decoding. The
            token ids which have their past given to this model should not be passed as `input_ids` as they have
            already been computed.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    start_top_log_probs: Optional[torch.FloatTensor] = ...
    start_top_index: Optional[torch.LongTensor] = ...
    end_top_log_probs: Optional[torch.FloatTensor] = ...
    end_top_index: Optional[torch.LongTensor] = ...
    cls_logits: Optional[torch.FloatTensor] = ...
    mems: Optional[List[torch.FloatTensor]] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, start_top_log_probs, start_top_index, end_top_log_probs, end_top_index, cls_logits, mems, hidden_states, attentions) -> None: ...

XLNET_START_DOCSTRING: str
XLNET_INPUTS_DOCSTRING: str

class XLNetModel(XLNetPreTrainedModel):
    mem_len: Incomplete
    reuse_len: Incomplete
    d_model: Incomplete
    same_length: Incomplete
    attn_type: Incomplete
    bi_data: Incomplete
    clamp_len: Incomplete
    n_layer: Incomplete
    word_embedding: Incomplete
    mask_emb: Incomplete
    layer: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def create_mask(self, qlen, mlen):
        """
        Creates causal attention mask. Float mask where 1.0 indicates masked, 0.0 indicates not-masked.

        Args:
            qlen: Sequence length
            mlen: Mask length

        ::

                  same_length=False: same_length=True: <mlen > < qlen > <mlen > < qlen >
               ^ [0 0 0 0 0 1 1 1 1] [0 0 0 0 0 1 1 1 1]
                 [0 0 0 0 0 0 1 1 1] [1 0 0 0 0 0 1 1 1]
            qlen [0 0 0 0 0 0 0 1 1] [1 1 0 0 0 0 0 1 1]
                 [0 0 0 0 0 0 0 0 1] [1 1 1 0 0 0 0 0 1]
               v [0 0 0 0 0 0 0 0 0] [1 1 1 1 0 0 0 0 0]

        """
    def cache_mem(self, curr_out, prev_mem): ...
    @staticmethod
    def positional_embedding(pos_seq, inv_freq, bsz: Incomplete | None = None): ...
    def relative_positional_encoding(self, qlen, klen, bsz: Incomplete | None = None): ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, mems: Optional[torch.Tensor] = None, perm_mask: Optional[torch.Tensor] = None, target_mapping: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, input_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, use_mems: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **kwargs) -> Union[Tuple, XLNetModelOutput]: ...

class XLNetLMHeadModel(XLNetPreTrainedModel):
    attn_type: Incomplete
    same_length: Incomplete
    transformer: Incomplete
    lm_loss: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, use_mems: Incomplete | None = None, **kwargs): ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, mems: Optional[torch.Tensor] = None, perm_mask: Optional[torch.Tensor] = None, target_mapping: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, input_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, use_mems: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **kwargs) -> Union[Tuple, XLNetLMHeadModelOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, num_predict)`, *optional*):
            Labels for masked language modeling. `num_predict` corresponds to `target_mapping.shape[1]`. If
            `target_mapping` is `None`, then `num_predict` corresponds to `sequence_length`.

            The labels should correspond to the masked input words that should be predicted and depends on
            `target_mapping`. Note in order to perform standard auto-regressive language modeling a *<mask>* token has
            to be added to the `input_ids` (see the `prepare_inputs_for_generation` function and examples below)

            Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100` are ignored, the loss
            is only computed for labels in `[0, ..., config.vocab_size]`

        Return:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, XLNetLMHeadModel
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("xlnet-large-cased")
        >>> model = XLNetLMHeadModel.from_pretrained("xlnet-large-cased")

        >>> # We show how to setup inputs to predict a next token using a bi-directional context.
        >>> input_ids = torch.tensor(
        ...     tokenizer.encode("Hello, my dog is very <mask>", add_special_tokens=False)
        ... ).unsqueeze(
        ...     0
        ... )  # We will predict the masked token
        >>> perm_mask = torch.zeros((1, input_ids.shape[1], input_ids.shape[1]), dtype=torch.float)
        >>> perm_mask[:, :, -1] = 1.0  # Previous tokens don\'t see last token
        >>> target_mapping = torch.zeros(
        ...     (1, 1, input_ids.shape[1]), dtype=torch.float
        ... )  # Shape [1, 1, seq_length] => let\'s predict one token
        >>> target_mapping[
        ...     0, 0, -1
        ... ] = 1.0  # Our first (and only) prediction will be the last token of the sequence (the masked token)

        >>> outputs = model(input_ids, perm_mask=perm_mask, target_mapping=target_mapping)
        >>> next_token_logits = outputs[
        ...     0
        ... ]  # Output has shape [target_mapping.size(0), target_mapping.size(1), config.vocab_size]

        >>> # The same way can the XLNetLMHeadModel be used to be trained by standard auto-regressive language modeling.
        >>> input_ids = torch.tensor(
        ...     tokenizer.encode("Hello, my dog is very <mask>", add_special_tokens=False)
        ... ).unsqueeze(
        ...     0
        ... )  # We will predict the masked token
        >>> labels = torch.tensor(tokenizer.encode("cute", add_special_tokens=False)).unsqueeze(0)
        >>> assert labels.shape[0] == 1, "only one word will be predicted"
        >>> perm_mask = torch.zeros((1, input_ids.shape[1], input_ids.shape[1]), dtype=torch.float)
        >>> perm_mask[
        ...     :, :, -1
        ... ] = 1.0  # Previous tokens don\'t see last token as is done in standard auto-regressive lm training
        >>> target_mapping = torch.zeros(
        ...     (1, 1, input_ids.shape[1]), dtype=torch.float
        ... )  # Shape [1, 1, seq_length] => let\'s predict one token
        >>> target_mapping[
        ...     0, 0, -1
        ... ] = 1.0  # Our first (and only) prediction will be the last token of the sequence (the masked token)

        >>> outputs = model(input_ids, perm_mask=perm_mask, target_mapping=target_mapping, labels=labels)
        >>> loss = outputs.loss
        >>> next_token_logits = (
        ...     outputs.logits
        ... )  # Logits have shape [target_mapping.size(0), target_mapping.size(1), config.vocab_size]
        ```'''

class XLNetForSequenceClassification(XLNetPreTrainedModel):
    num_labels: Incomplete
    config: Incomplete
    transformer: Incomplete
    sequence_summary: Incomplete
    logits_proj: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, mems: Optional[torch.Tensor] = None, perm_mask: Optional[torch.Tensor] = None, target_mapping: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, input_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, use_mems: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **kwargs) -> Union[Tuple, XLNetForSequenceClassificationOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class XLNetForTokenClassification(XLNetPreTrainedModel):
    num_labels: Incomplete
    transformer: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, mems: Optional[torch.Tensor] = None, perm_mask: Optional[torch.Tensor] = None, target_mapping: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, input_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, use_mems: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **kwargs) -> Union[Tuple, XLNetForTokenClassificationOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ..., num_choices]`
            where *num_choices* is the size of the second dimension of the input tensors. (see *input_ids* above)
        """

class XLNetForMultipleChoice(XLNetPreTrainedModel):
    transformer: Incomplete
    sequence_summary: Incomplete
    logits_proj: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, input_mask: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, mems: Optional[torch.Tensor] = None, perm_mask: Optional[torch.Tensor] = None, target_mapping: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, use_mems: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **kwargs) -> Union[Tuple, XLNetForMultipleChoiceOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ...,
            num_choices-1]` where `num_choices` is the size of the second dimension of the input tensors. (See
            `input_ids` above)
        """

class XLNetForQuestionAnsweringSimple(XLNetPreTrainedModel):
    num_labels: Incomplete
    transformer: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, mems: Optional[torch.Tensor] = None, perm_mask: Optional[torch.Tensor] = None, target_mapping: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, input_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, start_positions: Optional[torch.Tensor] = None, end_positions: Optional[torch.Tensor] = None, use_mems: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **kwargs) -> Union[Tuple, XLNetForQuestionAnsweringSimpleOutput]:
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

class XLNetForQuestionAnswering(XLNetPreTrainedModel):
    start_n_top: Incomplete
    end_n_top: Incomplete
    transformer: Incomplete
    start_logits: Incomplete
    end_logits: Incomplete
    answer_class: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, mems: Optional[torch.Tensor] = None, perm_mask: Optional[torch.Tensor] = None, target_mapping: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, input_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, start_positions: Optional[torch.Tensor] = None, end_positions: Optional[torch.Tensor] = None, is_impossible: Optional[torch.Tensor] = None, cls_index: Optional[torch.Tensor] = None, p_mask: Optional[torch.Tensor] = None, use_mems: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **kwargs) -> Union[Tuple, XLNetForQuestionAnsweringOutput]:
        '''
        start_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        is_impossible (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels whether a question has an answer or no answer (SQuAD 2.0)
        cls_index (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for position (index) of the classification token to use as input for computing plausibility of the
            answer.
        p_mask (`torch.FloatTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Optional mask of tokens which can\'t be in answers (e.g. [CLS], [PAD], ...). 1.0 means token should be
            masked. 0.0 mean token is not masked.

        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, XLNetForQuestionAnswering
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("xlnet-base-cased")
        >>> model = XLNetForQuestionAnswering.from_pretrained("xlnet-base-cased")

        >>> input_ids = torch.tensor(tokenizer.encode("Hello, my dog is cute", add_special_tokens=True)).unsqueeze(
        ...     0
        ... )  # Batch size 1
        >>> start_positions = torch.tensor([1])
        >>> end_positions = torch.tensor([3])
        >>> outputs = model(input_ids, start_positions=start_positions, end_positions=end_positions)

        >>> loss = outputs.loss
        ```'''
