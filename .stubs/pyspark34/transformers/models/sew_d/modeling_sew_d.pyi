import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, CausalLMOutput as CausalLMOutput, SequenceClassifierOutput as SequenceClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import softmax_backward_data as softmax_backward_data, torch_int_div as torch_int_div
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_sew_d import SEWDConfig as SEWDConfig
from _typeshed import Incomplete
from torch import nn
from transformers.deepspeed import is_deepspeed_zero3_enabled as is_deepspeed_zero3_enabled
from typing import Optional, Tuple, Union

logger: Incomplete
SEW_D_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def make_log_bucket_position(relative_pos, bucket_size, max_position): ...
def build_relative_position(query_size, key_size, bucket_size: int = -1, max_position: int = -1, device: Incomplete | None = None):
    """
    Build relative position according to the query and key

    We assume the absolute position of query \\(P_q\\) is range from (0, query_size) and the absolute position of key
    \\(P_k\\) is range from (0, key_size), The relative positions from query to key is \\(R_{q \\rightarrow k} = P_q -
    P_k\\)

    Args:
        query_size (int): the length of query
        key_size (int): the length of key
        bucket_size (int): the size of position bucket
        max_position (int): the maximum allowed absolute position
        device (`torch.device`): the device on which tensors will be created.

    Return:
        `torch.LongTensor`: A tensor with shape [1, query_size, key_size]
    """
def c2p_dynamic_expand(c2p_pos, query_layer, relative_pos): ...
def p2c_dynamic_expand(c2p_pos, query_layer, key_layer): ...
def pos_dynamic_expand(pos_index, p2c_att, key_layer): ...
def get_mask(input, local_context): ...

class SEWDNoLayerNormConvLayer(nn.Module):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    activation: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states): ...

class SEWDLayerNormConvLayer(nn.Module):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    layer_norm: Incomplete
    activation: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states): ...

class SEWDGroupNormConvLayer(nn.Module):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    activation: Incomplete
    layer_norm: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states): ...

class SEWDPositionalConvEmbedding(nn.Module):
    conv: Incomplete
    padding: Incomplete
    activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class SEWDSamePadLayer(nn.Module):
    num_pad_remove: Incomplete
    def __init__(self, num_conv_pos_embeddings) -> None: ...
    def forward(self, hidden_states): ...

class SEWDUpsampling(nn.Module):
    projection: Incomplete
    activation: Incomplete
    squeeze_factor: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class SEWDFeatureEncoder(nn.Module):
    """Construct the features from raw audio waveform"""
    conv_layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, input_values): ...

class SEWDFeatureExtractor(SEWDFeatureEncoder):
    def __init__(self, config) -> None: ...

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
    >>> from transformers.models.deberta_v2.modeling_deberta_v2 import XSoftmax

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

class SEWDSelfOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, input_tensor): ...

class DisentangledSelfAttention(nn.Module):
    """
    Disentangled self-attention module

    Parameters:
        config (`DebertaV2Config`):
            A model config class instance with the configuration to build a new model. The schema is similar to
            *BertConfig*, for more details, please refer [`DebertaV2Config`]

    """
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query_proj: Incomplete
    key_proj: Incomplete
    value_proj: Incomplete
    share_att_key: Incomplete
    pos_att_type: Incomplete
    relative_attention: Incomplete
    position_buckets: Incomplete
    max_relative_positions: Incomplete
    pos_ebd_size: Incomplete
    pos_dropout: Incomplete
    pos_key_proj: Incomplete
    pos_query_proj: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def transpose_for_scores(self, x, attention_heads): ...
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
    def disentangled_attention_bias(self, query_layer, key_layer, relative_pos, rel_embeddings, scale_factor): ...

class SEWDAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    config: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask, output_attentions: bool = False, query_states: Incomplete | None = None, relative_pos: Incomplete | None = None, rel_embeddings: Incomplete | None = None): ...

class SEWDIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class SEWDOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    config: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, input_tensor): ...

class SEWDLayer(nn.Module):
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask, query_states: Incomplete | None = None, relative_pos: Incomplete | None = None, rel_embeddings: Incomplete | None = None, output_attentions: bool = False): ...

class ConvLayer(nn.Module):
    conv_act: Incomplete
    conv: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    config: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, residual_states, input_mask): ...

class SEWDTransformerEncoder(nn.Module):
    """Modified BertEncoder with relative position bias support"""
    layer: Incomplete
    relative_attention: Incomplete
    max_relative_positions: Incomplete
    position_buckets: Incomplete
    rel_embeddings: Incomplete
    norm_rel_ebd: Incomplete
    LayerNorm: Incomplete
    conv: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def get_rel_embedding(self): ...
    def get_attention_mask(self, attention_mask): ...
    def get_rel_pos(self, hidden_states, query_states: Incomplete | None = None, relative_pos: Incomplete | None = None): ...
    def forward(self, hidden_states, attention_mask, output_hidden_states: bool = True, output_attentions: bool = False, query_states: Incomplete | None = None, relative_pos: Incomplete | None = None, return_dict: bool = True): ...

class SEWDEncoder(nn.Module):
    config: Incomplete
    pos_conv_embed: Incomplete
    pool: Incomplete
    encoder: Incomplete
    upsample: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.tensor, attention_mask: Optional[torch.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class SEWDPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = SEWDConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

SEWD_START_DOCSTRING: str
SEWD_INPUTS_DOCSTRING: str

class SEWDModel(SEWDPreTrainedModel):
    config: Incomplete
    feature_extractor: Incomplete
    layer_norm: Incomplete
    project_features: Incomplete
    feature_projection: Incomplete
    feature_dropout: Incomplete
    masked_spec_embed: Incomplete
    encoder: Incomplete
    def __init__(self, config: SEWDConfig) -> None: ...
    def forward(self, input_values: Optional[torch.Tensor], attention_mask: Optional[torch.Tensor] = None, mask_time_indices: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]: ...

class SEWDForCTC(SEWDPreTrainedModel):
    sew_d: Incomplete
    dropout: Incomplete
    lm_head: Incomplete
    def __init__(self, config) -> None: ...
    def freeze_feature_extractor(self) -> None:
        """
        Calling this function will disable the gradient computation for the feature encoder so that its parameter will
        not be updated during training.
        """
    def freeze_feature_encoder(self) -> None:
        """
        Calling this function will disable the gradient computation for the feature encoder so that its parameter will
        not be updated during training.
        """
    def forward(self, input_values: Optional[torch.Tensor], attention_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[torch.Tensor] = None) -> Union[Tuple, CausalLMOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size, target_length)`, *optional*):
            Labels for connectionist temporal classification. Note that `target_length` has to be smaller or equal to
            the sequence length of the output logits. Indices are selected in `[-100, 0, ..., config.vocab_size - 1]`.
            All labels set to `-100` are ignored (masked), the loss is only computed for labels in `[0, ...,
            config.vocab_size - 1]`.
        """

class SEWDForSequenceClassification(SEWDPreTrainedModel):
    sew_d: Incomplete
    layer_weights: Incomplete
    projector: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def freeze_feature_extractor(self) -> None:
        """
        Calling this function will disable the gradient computation for the feature encoder so that its parameters will
        not be updated during training.
        """
    def freeze_feature_encoder(self) -> None:
        """
        Calling this function will disable the gradient computation for the feature encoder so that its parameter will
        not be updated during training.
        """
    def freeze_base_model(self) -> None:
        """
        Calling this function will disable the gradient computation for the base model so that its parameters will not
        be updated during training. Only the classification head will be updated.
        """
    def forward(self, input_values: Optional[torch.Tensor], attention_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[torch.Tensor] = None) -> Union[Tuple, SequenceClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
