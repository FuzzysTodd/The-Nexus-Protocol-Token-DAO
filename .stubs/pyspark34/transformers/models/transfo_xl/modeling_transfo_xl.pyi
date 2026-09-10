import torch
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_transfo_xl import TransfoXLConfig as TransfoXLConfig
from .modeling_transfo_xl_utilities import ProjectedAdaptiveLogSoftmax as ProjectedAdaptiveLogSoftmax
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import List, Optional, Tuple, Union

logger: Incomplete
TRANSFO_XL_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def build_tf_to_pytorch_map(model, config):
    """
    A map of modules from TF to PyTorch. This time I use a map to keep the PyTorch model as identical to the original
    PyTorch model as possible.
    """
def load_tf_weights_in_transfo_xl(model, config, tf_path):
    """Load tf checkpoints in a pytorch model"""

class PositionalEmbedding(nn.Module):
    demb: Incomplete
    def __init__(self, demb) -> None: ...
    def forward(self, pos_seq, bsz: Incomplete | None = None): ...

class PositionwiseFF(nn.Module):
    d_model: Incomplete
    d_inner: Incomplete
    dropout: Incomplete
    CoreNet: Incomplete
    layer_norm: Incomplete
    pre_lnorm: Incomplete
    def __init__(self, d_model, d_inner, dropout, pre_lnorm: bool = False, layer_norm_epsilon: float = 1e-05) -> None: ...
    def forward(self, inp): ...

class RelPartialLearnableMultiHeadAttn(nn.Module):
    n_head: Incomplete
    d_model: Incomplete
    d_head: Incomplete
    dropout: Incomplete
    qkv_net: Incomplete
    drop: Incomplete
    dropatt: Incomplete
    o_net: Incomplete
    layer_norm: Incomplete
    scale: Incomplete
    pre_lnorm: Incomplete
    r_r_bias: Incomplete
    r_w_bias: Incomplete
    r_net: Incomplete
    def __init__(self, n_head, d_model, d_head, dropout, dropatt: int = 0, pre_lnorm: bool = False, r_r_bias: Incomplete | None = None, r_w_bias: Incomplete | None = None, layer_norm_epsilon: float = 1e-05) -> None: ...
    def forward(self, w, r, attn_mask: Incomplete | None = None, mems: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class RelPartialLearnableDecoderLayer(nn.Module):
    dec_attn: Incomplete
    pos_ff: Incomplete
    def __init__(self, n_head, d_model, d_head, d_inner, dropout, layer_norm_epsilon: float = 1e-05, **kwargs) -> None: ...
    def forward(self, dec_inp, r, dec_attn_mask: Incomplete | None = None, mems: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class AdaptiveEmbedding(nn.Module):
    n_token: Incomplete
    d_embed: Incomplete
    cutoffs: Incomplete
    div_val: Incomplete
    d_proj: Incomplete
    emb_scale: Incomplete
    cutoff_ends: Incomplete
    emb_layers: Incomplete
    emb_projs: Incomplete
    def __init__(self, n_token, d_embed, d_proj, cutoffs, div_val: int = 1, sample_softmax: bool = False) -> None: ...
    def forward(self, inp): ...

class TransfoXLPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = TransfoXLConfig
    load_tf_weights = load_tf_weights_in_transfo_xl
    base_model_prefix: str
    def resize_token_embeddings(self, new_num_tokens: Optional[int] = None, layer: Optional[int] = -1):
        """
        Resize input token embeddings matrix of the model if new_num_tokens != config.vocab_size. Take care of tying
        weights embeddings afterwards if the model class has a *tie_weights()* method.

        Arguments:
            new_num_tokens: (*optional*) int:
                New number of tokens in the embedding matrix. Increasing the size will add newly initialized vectors at
                the end. Reducing the size will remove vectors from the end. If not provided or None: does nothing and
                just returns a pointer to the input tokens `torch.nn.Embeddings` Module of the model.
            layer: (*optional*) int:
                Layer of the *AdaptiveEmbedding* where the resizing should be done. Per default the last layer will be
                resized. Be aware that when resizing other than the last layer, you have to ensure that the new
                token(s) in the tokenizer are at the corresponding position.

        Return: `torch.nn.Embeddings` Pointer to the input tokens Embeddings Module of the model
        """

@dataclass
class TransfoXLModelOutput(ModelOutput):
    """
    Base class for model's outputs that may also contain a past key/values (to speed up sequential decoding).

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        mems (`List[torch.FloatTensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states (key and values in the attention blocks). Can be used (see `mems`
            input) to speed up sequential decoding. The token ids which have their past given to this model should not
            be passed as input ids as they have already been computed.
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
    mems: List[torch.FloatTensor] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, last_hidden_state, mems, hidden_states, attentions) -> None: ...

@dataclass
class TransfoXLSequenceClassifierOutputWithPast(ModelOutput):
    """
    Base class for outputs of sentence classification models.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Classification (or regression if config.num_labels==1) loss.
        logits (`torch.FloatTensor` of shape `(batch_size, config.num_labels)`):
            Classification (or regression if config.num_labels==1) scores (before SoftMax).
        mems (`List[torch.FloatTensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states (key and values in the attention blocks). Can be used (see `mems`
            input) to speed up sequential decoding. The token ids which have their past given to this model should not
            be passed as input ids as they have already been computed.
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
    mems: List[torch.FloatTensor] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, logits, mems, hidden_states, attentions) -> None: ...

@dataclass
class TransfoXLLMHeadModelOutput(ModelOutput):
    """
    Base class for model's outputs that may also contain a past key/values (to speed up sequential decoding).

    Args:
        losses (`torch.FloatTensor` of shape *(batch_size, sequence_length-1)*, *optional*, returned when `labels` is provided):
            Language modeling losses (not reduced).
        prediction_scores (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token after SoftMax).
        mems (`List[torch.FloatTensor]` of length `config.n_layers`):
            Contains pre-computed hidden-states (key and values in the attention blocks). Can be used (see `mems`
            input) to speed up sequential decoding. The token ids which have their past given to this model should not
            be passed as input ids as they have already been computed.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
        loss (`torch.FloatTensor` of shape `()`, *optional*, returned when `labels` is provided)
            Reduced language modeling loss.
    """
    losses: Optional[torch.FloatTensor] = ...
    prediction_scores: torch.FloatTensor = ...
    mems: List[torch.FloatTensor] = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    loss: Optional[torch.FloatTensor] = ...
    @property
    def logits(self): ...
    def __init__(self, losses, prediction_scores, mems, hidden_states, attentions, loss) -> None: ...

TRANSFO_XL_START_DOCSTRING: str
TRANSFO_XL_INPUTS_DOCSTRING: str

class TransfoXLModel(TransfoXLPreTrainedModel):
    n_token: Incomplete
    d_embed: Incomplete
    d_model: Incomplete
    n_head: Incomplete
    d_head: Incomplete
    word_emb: Incomplete
    drop: Incomplete
    n_layer: Incomplete
    mem_len: Incomplete
    attn_type: Incomplete
    r_w_bias: Incomplete
    r_r_bias: Incomplete
    layers: Incomplete
    same_length: Incomplete
    clamp_len: Incomplete
    pos_emb: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    sample_softmax: int
    def backward_compatible(self) -> None: ...
    def reset_memory_length(self, mem_len) -> None: ...
    def init_mems(self, bsz): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, mems: Optional[List[torch.FloatTensor]] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, TransfoXLModelOutput]: ...

class TransfoXLLMHeadModel(TransfoXLPreTrainedModel):
    transformer: Incomplete
    sample_softmax: Incomplete
    trainer_compatible: Incomplete
    crit: Incomplete
    def __init__(self, config) -> None: ...
    def tie_weights(self) -> None:
        """
        Run this to be sure output and input (adaptive) softmax weights are tied
        """
    def reset_memory_length(self, mem_len) -> None: ...
    def init_mems(self, bsz): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, mems: Optional[List[torch.FloatTensor]] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, TransfoXLLMHeadModelOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
            `labels = input_ids` Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100`
            are ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`
        """
    def get_output_embeddings(self):
        """Double-check if you are using adaptive softmax."""
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, **model_kwargs): ...

class TransfoXLForSequenceClassification(TransfoXLPreTrainedModel):
    num_labels: Incomplete
    transformer: Incomplete
    score: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, mems: Optional[List[torch.FloatTensor]] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, TransfoXLSequenceClassifierOutputWithPast]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
