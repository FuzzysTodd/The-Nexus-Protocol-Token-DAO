import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, MaskedLMOutput as MaskedLMOutput, QuestionAnsweringModelOutput as QuestionAnsweringModelOutput, SequenceClassifierOutput as SequenceClassifierOutput, TokenClassifierOutput as TokenClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import softmax_backward_data as softmax_backward_data
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_deberta import DebertaConfig as DebertaConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
DEBERTA_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class ContextPooler(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    config: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...
    @property
    def output_dim(self): ...

class XSoftmax(torch.autograd.Function):
    """
    Masked Softmax which is optimized for saving memory

    Args:
        input (`torch.tensor`): The input tensor that will apply softmax.
        mask (`torch.IntTensor`):
            The mask matrix where 0 indicate that element will be ignored in the softmax calculation.
        dim (int): The dimension that will apply softmax

    Example:

    ```python
    >>> import torch
    >>> from transformers.models.deberta.modeling_deberta import XSoftmax

    >>> # Make a tensor
    >>> x = torch.randn([4, 20, 100])

    >>> # Create a mask
    >>> mask = (x > 0).int()

    >>> # Specify the dimension to apply softmax
    >>> dim = -1

    >>> y = XSoftmax.apply(x, mask, dim)
    ```"""
    dim: Incomplete
    @staticmethod
    def forward(self, input, mask, dim): ...
    @staticmethod
    def backward(self, grad_output): ...
    @staticmethod
    def symbolic(g, self, mask, dim): ...

class DropoutContext:
    dropout: int
    mask: Incomplete
    scale: int
    reuse_mask: bool
    def __init__(self) -> None: ...

def get_mask(input, local_context): ...

class XDropout(torch.autograd.Function):
    """Optimized dropout function to save computation and memory by using mask operation instead of multiplication."""
    @staticmethod
    def forward(ctx, input, local_ctx): ...
    @staticmethod
    def backward(ctx, grad_output): ...
    @staticmethod
    def symbolic(g: torch._C.Graph, input: torch._C.Value, local_ctx: Union[float, DropoutContext]) -> torch._C.Value: ...

class StableDropout(nn.Module):
    """
    Optimized dropout module for stabilizing the training

    Args:
        drop_prob (float): the dropout probabilities
    """
    drop_prob: Incomplete
    count: int
    context_stack: Incomplete
    def __init__(self, drop_prob) -> None: ...
    def forward(self, x):
        """
        Call the module

        Args:
            x (`torch.tensor`): The input tensor to apply dropout
        """
    def clear_context(self) -> None: ...
    def init_context(self, reuse_mask: bool = True, scale: int = 1) -> None: ...
    def get_context(self): ...

class DebertaLayerNorm(nn.Module):
    """LayerNorm module in the TF style (epsilon inside the square root)."""
    weight: Incomplete
    bias: Incomplete
    variance_epsilon: Incomplete
    def __init__(self, size, eps: float = 1e-12) -> None: ...
    def forward(self, hidden_states): ...

class DebertaSelfOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, input_tensor): ...

class DebertaAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    config: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask, output_attentions: bool = False, query_states: Incomplete | None = None, relative_pos: Incomplete | None = None, rel_embeddings: Incomplete | None = None): ...

class DebertaIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class DebertaOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    config: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, input_tensor): ...

class DebertaLayer(nn.Module):
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask, query_states: Incomplete | None = None, relative_pos: Incomplete | None = None, rel_embeddings: Incomplete | None = None, output_attentions: bool = False): ...

class DebertaEncoder(nn.Module):
    """Modified BertEncoder with relative position bias support"""
    layer: Incomplete
    relative_attention: Incomplete
    max_relative_positions: Incomplete
    rel_embeddings: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def get_rel_embedding(self): ...
    def get_attention_mask(self, attention_mask): ...
    def get_rel_pos(self, hidden_states, query_states: Incomplete | None = None, relative_pos: Incomplete | None = None): ...
    def forward(self, hidden_states, attention_mask, output_hidden_states: bool = True, output_attentions: bool = False, query_states: Incomplete | None = None, relative_pos: Incomplete | None = None, return_dict: bool = True): ...

def build_relative_position(query_size, key_size, device):
    """
    Build relative position according to the query and key

    We assume the absolute position of query \\(P_q\\) is range from (0, query_size) and the absolute position of key
    \\(P_k\\) is range from (0, key_size), The relative positions from query to key is \\(R_{q \\rightarrow k} = P_q -
    P_k\\)

    Args:
        query_size (int): the length of query
        key_size (int): the length of key

    Return:
        `torch.LongTensor`: A tensor with shape [1, query_size, key_size]

    """
def c2p_dynamic_expand(c2p_pos, query_layer, relative_pos): ...
def p2c_dynamic_expand(c2p_pos, query_layer, key_layer): ...
def pos_dynamic_expand(pos_index, p2c_att, key_layer): ...

class DisentangledSelfAttention(nn.Module):
    """
    Disentangled self-attention module

    Parameters:
        config (`str`):
            A model config class instance with the configuration to build a new model. The schema is similar to
            *BertConfig*, for more details, please refer [`DebertaConfig`]

    """
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    in_proj: Incomplete
    q_bias: Incomplete
    v_bias: Incomplete
    pos_att_type: Incomplete
    relative_attention: Incomplete
    talking_head: Incomplete
    head_logits_proj: Incomplete
    head_weights_proj: Incomplete
    max_relative_positions: Incomplete
    pos_dropout: Incomplete
    pos_proj: Incomplete
    pos_q_proj: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def transpose_for_scores(self, x): ...
    def forward(self, hidden_states, attention_mask, output_attentions: bool = False, query_states: Incomplete | None = None, relative_pos: Incomplete | None = None, rel_embeddings: Incomplete | None = None):
        """
        Call the module

        Args:
            hidden_states (`torch.FloatTensor`):
                Input states to the module usually the output from previous layer, it will be the Q,K and V in
                *Attention(Q,K,V)*

            attention_mask (`torch.ByteTensor`):
                An attention mask matrix of shape [*B*, *N*, *N*] where *B* is the batch size, *N* is the maximum
                sequence length in which element [i,j] = *1* means the *i* th token in the input can attend to the *j*
                th token.

            output_attentions (`bool`, optional):
                Whether return the attention matrix.

            query_states (`torch.FloatTensor`, optional):
                The *Q* state in *Attention(Q,K,V)*.

            relative_pos (`torch.LongTensor`):
                The relative position encoding between the tokens in the sequence. It's of shape [*B*, *N*, *N*] with
                values ranging in [*-max_relative_positions*, *max_relative_positions*].

            rel_embeddings (`torch.FloatTensor`):
                The embedding of relative distances. It's a tensor of shape [\\(2 \\times
                \\text{max_relative_positions}\\), *hidden_size*].


        """
    def disentangled_att_bias(self, query_layer, key_layer, relative_pos, rel_embeddings, scale_factor): ...

class DebertaEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    embedding_size: Incomplete
    word_embeddings: Incomplete
    position_biased_input: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    embed_proj: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    config: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None): ...

class DebertaPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = DebertaConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool

DEBERTA_START_DOCSTRING: str
DEBERTA_INPUTS_DOCSTRING: str

class DebertaModel(DebertaPreTrainedModel):
    embeddings: Incomplete
    encoder: Incomplete
    z_steps: int
    config: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]: ...

class DebertaForMaskedLM(DebertaPreTrainedModel):
    deberta: Incomplete
    cls: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, MaskedLMOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        """

class DebertaPredictionHeadTransform(nn.Module):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class DebertaLMPredictionHead(nn.Module):
    transform: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class DebertaOnlyMLMHead(nn.Module):
    predictions: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, sequence_output): ...

class DebertaForSequenceClassification(DebertaPreTrainedModel):
    num_labels: Incomplete
    deberta: Incomplete
    pooler: Incomplete
    classifier: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, SequenceClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class DebertaForTokenClassification(DebertaPreTrainedModel):
    num_labels: Incomplete
    deberta: Incomplete
    dropout: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, TokenClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the token classification loss. Indices should be in `[0, ..., config.num_labels - 1]`.
        """

class DebertaForQuestionAnswering(DebertaPreTrainedModel):
    num_labels: Incomplete
    deberta: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, start_positions: Optional[torch.Tensor] = None, end_positions: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, QuestionAnsweringModelOutput]:
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
