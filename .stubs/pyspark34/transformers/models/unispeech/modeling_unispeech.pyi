import torch
from ...activations import ACT2FN as ACT2FN
from ...deepspeed import is_deepspeed_zero3_enabled as is_deepspeed_zero3_enabled
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, CausalLMOutput as CausalLMOutput, SequenceClassifierOutput as SequenceClassifierOutput, Wav2Vec2BaseModelOutput as Wav2Vec2BaseModelOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import torch_int_div as torch_int_div
from ...utils import ModelOutput as ModelOutput, add_code_sample_docstrings as add_code_sample_docstrings, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_unispeech import UniSpeechConfig as UniSpeechConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
UNISPEECH_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class UniSpeechForPreTrainingOutput(ModelOutput):
    """
    Output type of [`UniSpeechForPreTrainingOutput`], with potential hidden states and attentions.

    Args:
        loss (*optional*, returned when model is in train mode, `torch.FloatTensor` of shape `(1,)`):
            Total loss as the sum of the contrastive loss (L_m) and the diversity loss (L_d) as stated in the [official
            paper](https://arxiv.org/pdf/2006.11477.pdf) . (classification) loss.
        projected_states (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.proj_codevector_dim)`):
            Hidden-states of the model projected to *config.proj_codevector_dim* that can be used to predict the masked
            projected quantized states.
        projected_quantized_states (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.proj_codevector_dim)`):
            Quantized extracted feature vectors projected to *config.proj_codevector_dim* representing the positive
            target vectors for contrastive loss.
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
    projected_states: torch.FloatTensor = ...
    projected_quantized_states: torch.FloatTensor = ...
    codevector_perplexity: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, projected_states, projected_quantized_states, codevector_perplexity, hidden_states, attentions) -> None: ...

class UniSpeechNoLayerNormConvLayer(nn.Module):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    activation: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states): ...

class UniSpeechLayerNormConvLayer(nn.Module):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    layer_norm: Incomplete
    activation: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states): ...

class UniSpeechGroupNormConvLayer(nn.Module):
    in_conv_dim: Incomplete
    out_conv_dim: Incomplete
    conv: Incomplete
    activation: Incomplete
    layer_norm: Incomplete
    def __init__(self, config, layer_id: int = 0) -> None: ...
    def forward(self, hidden_states): ...

class UniSpeechPositionalConvEmbedding(nn.Module):
    conv: Incomplete
    padding: Incomplete
    activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class UniSpeechSamePadLayer(nn.Module):
    num_pad_remove: Incomplete
    def __init__(self, num_conv_pos_embeddings) -> None: ...
    def forward(self, hidden_states): ...

class UniSpeechFeatureEncoder(nn.Module):
    """Construct the features from raw audio waveform"""
    conv_layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, input_values): ...

class UniSpeechFeatureExtractor(UniSpeechFeatureEncoder):
    def __init__(self, config) -> None: ...

class UniSpeechFeatureProjection(nn.Module):
    layer_norm: Incomplete
    projection: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class UniSpeechAttention(nn.Module):
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

class UniSpeechFeedForward(nn.Module):
    intermediate_dropout: Incomplete
    intermediate_dense: Incomplete
    intermediate_act_fn: Incomplete
    output_dense: Incomplete
    output_dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class UniSpeechEncoderLayer(nn.Module):
    attention: Incomplete
    dropout: Incomplete
    layer_norm: Incomplete
    feed_forward: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, output_attentions: bool = False): ...

class UniSpeechEncoderLayerStableLayerNorm(nn.Module):
    attention: Incomplete
    dropout: Incomplete
    layer_norm: Incomplete
    feed_forward: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, output_attentions: bool = False): ...

class UniSpeechEncoder(nn.Module):
    config: Incomplete
    pos_conv_embed: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.tensor, attention_mask: Optional[torch.Tensor] = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class UniSpeechEncoderStableLayerNorm(nn.Module):
    config: Incomplete
    pos_conv_embed: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class UniSpeechGumbelVectorQuantizer(nn.Module):
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

class UniSpeechPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = UniSpeechConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

UNISPEECH_START_DOCSTRING: str
UNISPEECH_INPUTS_DOCSTRING: str

class UniSpeechModel(UniSpeechPreTrainedModel):
    config: Incomplete
    feature_extractor: Incomplete
    feature_projection: Incomplete
    masked_spec_embed: Incomplete
    encoder: Incomplete
    def __init__(self, config: UniSpeechConfig) -> None: ...
    def forward(self, input_values: Optional[torch.Tensor], attention_mask: Optional[torch.Tensor] = None, mask_time_indices: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, Wav2Vec2BaseModelOutput]: ...

class UniSpeechForPreTraining(UniSpeechPreTrainedModel):
    unispeech: Incomplete
    dropout_features: Incomplete
    quantizer: Incomplete
    project_q: Incomplete
    project_hid: Incomplete
    ctc_proj: Incomplete
    dropout: Incomplete
    def __init__(self, config: UniSpeechConfig) -> None: ...
    def set_gumbel_temperature(self, temperature: int):
        """
        Set the Gumbel softmax temperature to a given value. Only necessary for training
        """
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
    @staticmethod
    def compute_contrastive_logits(target_features: torch.FloatTensor, negative_features: torch.FloatTensor, predicted_features: torch.FloatTensor, temperature: int = 1):
        """
        Compute logits for contrastive loss based using cosine similarity as the distance measure between
        `[positive_feature, negative_features]` and `[predicted_features]`. Additionally, temperature can be applied.
        """
    def forward(self, input_values: Optional[torch.Tensor], attention_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, UniSpeechForPreTrainingOutput]:
        '''
        mask_time_indices (`torch.BoolTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Indices to mask extracted features for contrastive loss. When in training mode, model learns to predict
            masked extracted features in *config.proj_codevector_dim* space.
        sampled_negative_indices (`torch.BoolTensor` of shape `(batch_size, sequence_length, num_negatives)`, *optional*):
            Indices indicating which quantized target vectors are used as negative sampled vectors in contrastive loss.
            Required input for pre-training.

        Returns:

        Example:

        ```python
        >>> import torch
        >>> from transformers import AutoFeatureExtractor, UniSpeechForPreTraining

        >>> feature_extractor = AutoFeatureExtractor.from_pretrained("microsoft/unispeech-large-1500h-cv")
        >>> model = UniSpeechForPreTraining.from_pretrained("microsoft/unispeech-large-1500h-cv")
        >>> # TODO: Add full pretraining example
        ```'''

class UniSpeechForCTC(UniSpeechPreTrainedModel):
    unispeech: Incomplete
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

class UniSpeechForSequenceClassification(UniSpeechPreTrainedModel):
    unispeech: Incomplete
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
