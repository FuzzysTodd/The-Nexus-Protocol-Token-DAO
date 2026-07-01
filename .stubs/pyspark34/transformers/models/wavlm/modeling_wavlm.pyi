import torch
from ...activations import ACT2FN as ACT2FN
from ...deepspeed import is_deepspeed_zero3_enabled as is_deepspeed_zero3_enabled
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, CausalLMOutput as CausalLMOutput, SequenceClassifierOutput as SequenceClassifierOutput, TokenClassifierOutput as TokenClassifierOutput, Wav2Vec2BaseModelOutput as Wav2Vec2BaseModelOutput, XVectorOutput as XVectorOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import torch_int_div as torch_int_div
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging
from .configuration_wavlm import WavLMConfig as WavLMConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
WAVLM_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class WavLMNoLayerNormConvLayer(nn.Module):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    activation: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states): ...

class WavLMLayerNormConvLayer(nn.Module):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    layer_norm: Incomplete
    activation: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states): ...

class WavLMGroupNormConvLayer(nn.Module):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    activation: Incomplete
    layer_norm: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states): ...

class WavLMPositionalConvEmbedding(nn.Module):
    conv: Incomplete
    padding: Incomplete
    activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class WavLMSamePadLayer(nn.Module):
    num_pad_remove: Incomplete
    def __init__(self, num_conv_pos_embeddings) -> None: ...
    def forward(self, hidden_states): ...

class WavLMFeatureEncoder(nn.Module):
    """Construct the features from raw audio waveform"""
    conv_layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, input_values): ...

class WavLMFeatureExtractor(WavLMFeatureEncoder):
    def __init__(self, config) -> None: ...

class WavLMFeatureProjection(nn.Module):
    layer_norm: Incomplete
    projection: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class WavLMAttention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    embed_dim: Incomplete
    num_heads: Incomplete
    dropout: Incomplete
    head_dim: Incomplete
    scaling: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    q_proj: Incomplete
    out_proj: Incomplete
    num_buckets: Incomplete
    max_distance: Incomplete
    gru_rel_pos_const: Incomplete
    gru_rel_pos_linear: Incomplete
    rel_attn_embed: Incomplete
    def __init__(self, embed_dim: int, num_heads: int, dropout: float = 0.0, num_buckets: int = 320, max_distance: int = 800, has_relative_position_bias: bool = True) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, position_bias: Optional[torch.Tensor] = None, output_attentions: bool = False, index: int = 0) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        """Attention layer with relative attention"""
    def torch_multi_head_self_attention(self, hidden_states: torch.FloatTensor, attention_mask: Union[torch.LongTensor, torch.BoolTensor], gated_position_bias: torch.FloatTensor, output_attentions: bool) -> tuple[torch.FloatTensor, torch.FloatTensor]:
        """simple wrapper around torch's multi_head_attention_forward function"""
    def compute_bias(self, query_length: int, key_length: int) -> torch.FloatTensor: ...

class WavLMFeedForward(nn.Module):
    intermediate_dropout: Incomplete
    intermediate_dense: Incomplete
    intermediate_act_fn: Incomplete
    output_dense: Incomplete
    output_dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class WavLMEncoderLayer(nn.Module):
    attention: Incomplete
    dropout: Incomplete
    layer_norm: Incomplete
    feed_forward: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: WavLMConfig, has_relative_position_bias: bool = True) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, output_attentions: bool = False, index: int = 0): ...

class WavLMEncoderLayerStableLayerNorm(nn.Module):
    attention: Incomplete
    dropout: Incomplete
    layer_norm: Incomplete
    feed_forward: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: WavLMConfig, has_relative_position_bias: bool = True) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, output_attentions: bool = False): ...

class WavLMEncoder(nn.Module):
    config: Incomplete
    pos_conv_embed: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class WavLMEncoderStableLayerNorm(nn.Module):
    config: Incomplete
    pos_conv_embed: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class WavLMGumbelVectorQuantizer(nn.Module):
    """
    Vector quantization using gumbel softmax. See [CATEGORICAL REPARAMETERIZATION WITH
    GUMBEL-SOFTMAX](https://arxiv.org/pdf/1611.01144.pdf) for more information.
    """
    num_groups: Incomplete
    num_vars: Incomplete
    codevectors: Incomplete
    weight_proj: Incomplete
    temperature: int
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class WavLMAdapter(nn.Module):
    proj: Incomplete
    proj_layer_norm: Incomplete
    layers: Incomplete
    layerdrop: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class WavLMAdapterLayer(nn.Module):
    conv: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class WavLMPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = WavLMConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

WAVLM_START_DOCSTRING: str
WAVLM_INPUTS_DOCSTRING: str

class WavLMModel(WavLMPreTrainedModel):
    config: Incomplete
    feature_extractor: Incomplete
    feature_projection: Incomplete
    masked_spec_embed: Incomplete
    encoder: Incomplete
    adapter: Incomplete
    def __init__(self, config: WavLMConfig) -> None: ...
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
    def forward(self, input_values: Optional[torch.Tensor], attention_mask: Optional[torch.Tensor] = None, mask_time_indices: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, Wav2Vec2BaseModelOutput]: ...

class WavLMForCTC(WavLMPreTrainedModel):
    wavlm: Incomplete
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

class WavLMForSequenceClassification(WavLMPreTrainedModel):
    wavlm: Incomplete
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

class WavLMForAudioFrameClassification(WavLMPreTrainedModel):
    wavlm: Incomplete
    layer_weights: Incomplete
    classifier: Incomplete
    num_labels: Incomplete
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
    def freeze_base_model(self) -> None:
        """
        Calling this function will disable the gradient computation for the base model so that its parameters will not
        be updated during training. Only the classification head will be updated.
        """
    def forward(self, input_values: Optional[torch.Tensor], attention_mask: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, TokenClassifierOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """

class AMSoftmaxLoss(nn.Module):
    scale: Incomplete
    margin: Incomplete
    num_labels: Incomplete
    weight: Incomplete
    loss: Incomplete
    def __init__(self, input_dim, num_labels, scale: float = 30.0, margin: float = 0.4) -> None: ...
    def forward(self, hidden_states, labels): ...

class TDNNLayer(nn.Module):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    kernel_size: Incomplete
    dilation: Incomplete
    kernel: Incomplete
    activation: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states): ...

class WavLMForXVector(WavLMPreTrainedModel):
    wavlm: Incomplete
    layer_weights: Incomplete
    projector: Incomplete
    tdnn: Incomplete
    feature_extractor: Incomplete
    classifier: Incomplete
    objective: Incomplete
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
    def freeze_base_model(self) -> None:
        """
        Calling this function will disable the gradient computation for the base model so that its parameters will not
        be updated during training. Only the classification head will be updated.
        """
    def forward(self, input_values: Optional[torch.Tensor], attention_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[torch.Tensor] = None) -> Union[Tuple, XVectorOutput]:
        """
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).
        """
