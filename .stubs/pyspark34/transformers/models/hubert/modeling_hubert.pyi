import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, CausalLMOutput as CausalLMOutput, SequenceClassifierOutput as SequenceClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import torch_int_div as torch_int_div
from ...utils import add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_hubert import HubertConfig as HubertConfig
from _typeshed import Incomplete
from torch import nn
from transformers.deepspeed import is_deepspeed_zero3_enabled as is_deepspeed_zero3_enabled
from typing import Optional, Tuple, Union

logger: Incomplete
HUBERT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class HubertNoLayerNormConvLayer(nn.Module):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    activation: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states): ...

class HubertLayerNormConvLayer(nn.Module):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    layer_norm: Incomplete
    activation: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states): ...

class HubertGroupNormConvLayer(nn.Module):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    activation: Incomplete
    layer_norm: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states): ...

class HubertPositionalConvEmbedding(nn.Module):
    conv: Incomplete
    padding: Incomplete
    activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class HubertSamePadLayer(nn.Module):
    num_pad_remove: Incomplete
    def __init__(self, num_conv_pos_embeddings) -> None: ...
    def forward(self, hidden_states): ...

class HubertFeatureEncoder(nn.Module):
    """Construct the features from raw audio waveform"""
    conv_layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, input_values): ...

class HubertFeatureExtractor(HubertFeatureEncoder):
    def __init__(self, config) -> None: ...

class HubertFeatureProjection(nn.Module):
    feat_proj_layer_norm: Incomplete
    layer_norm: Incomplete
    projection: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class HubertAttention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    embed_dim: Incomplete
    num_heads: Incomplete
    dropout: Incomplete
    head_dim: Incomplete
    scaling: Incomplete
    is_decoder: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    q_proj: Incomplete
    out_proj: Incomplete
    def __init__(self, embed_dim: int, num_heads: int, dropout: float = 0.0, is_decoder: bool = False, bias: bool = True) -> None: ...
    def forward(self, hidden_states: torch.Tensor, key_value_states: Optional[torch.Tensor] = None, past_key_value: Optional[Tuple[torch.Tensor]] = None, attention_mask: Optional[torch.Tensor] = None, layer_head_mask: Optional[torch.Tensor] = None, output_attentions: bool = False) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        """Input shape: Batch x Time x Channel"""

class HubertFeedForward(nn.Module):
    intermediate_dropout: Incomplete
    intermediate_dense: Incomplete
    intermediate_act_fn: Incomplete
    output_dense: Incomplete
    output_dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class HubertEncoderLayer(nn.Module):
    attention: Incomplete
    dropout: Incomplete
    layer_norm: Incomplete
    feed_forward: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, output_attentions: bool = False): ...

class HubertEncoderLayerStableLayerNorm(nn.Module):
    attention: Incomplete
    dropout: Incomplete
    layer_norm: Incomplete
    feed_forward: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, output_attentions: bool = False): ...

class HubertEncoder(nn.Module):
    config: Incomplete
    pos_conv_embed: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.tensor, attention_mask: Optional[torch.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class HubertEncoderStableLayerNorm(nn.Module):
    config: Incomplete
    pos_conv_embed: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class HubertPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = HubertConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

HUBERT_START_DOCSTRING: str
HUBERT_INPUTS_DOCSTRING: str

class HubertModel(HubertPreTrainedModel):
    config: Incomplete
    feature_extractor: Incomplete
    feature_projection: Incomplete
    masked_spec_embed: Incomplete
    encoder: Incomplete
    def __init__(self, config: HubertConfig) -> None: ...
    def forward(self, input_values: Optional[torch.Tensor], attention_mask: Optional[torch.Tensor] = None, mask_time_indices: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]:
        '''

        Returns:

        Example:

        ```python
        >>> from transformers import AutoProcessor, HubertModel
        >>> from datasets import load_dataset
        >>> import soundfile as sf

        >>> processor = AutoProcessor.from_pretrained("facebook/hubert-large-ls960-ft")
        >>> model = HubertModel.from_pretrained("facebook/hubert-large-ls960-ft")


        >>> def map_to_array(batch):
        ...     speech, _ = sf.read(batch["file"])
        ...     batch["speech"] = speech
        ...     return batch


        >>> ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
        >>> ds = ds.map(map_to_array)

        >>> input_values = processor(ds["speech"][0], return_tensors="pt").input_values  # Batch size 1
        >>> hidden_states = model(input_values).last_hidden_state
        ```'''

class HubertForCTC(HubertPreTrainedModel):
    hubert: Incomplete
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

class HubertForSequenceClassification(HubertPreTrainedModel):
    hubert: Incomplete
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
