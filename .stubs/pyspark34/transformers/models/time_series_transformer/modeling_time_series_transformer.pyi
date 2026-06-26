import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPastAndCrossAttentions as BaseModelOutputWithPastAndCrossAttentions, ModelOutput as ModelOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_time_series_transformer import TimeSeriesTransformerConfig as TimeSeriesTransformerConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from torch.distributions import Distribution as Distribution, TransformedDistribution
from typing import Callable, Dict, List, Optional, Tuple, Union

logger: Incomplete
TIME_SERIES_TRANSFORMER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class AffineTransformed(TransformedDistribution):
    scale: Incomplete
    loc: Incomplete
    def __init__(self, base_distribution: Distribution, loc: Incomplete | None = None, scale: Incomplete | None = None, event_dim: int = 0) -> None: ...
    @property
    def mean(self):
        """
        Returns the mean of the distribution.
        """
    @property
    def variance(self):
        """
        Returns the variance of the distribution.
        """
    @property
    def stddev(self):
        """
        Returns the standard deviation of the distribution.
        """

class ParameterProjection(nn.Module):
    args_dim: Incomplete
    proj: Incomplete
    domain_map: Incomplete
    def __init__(self, in_features: int, args_dim: Dict[str, int], domain_map: Callable[..., Tuple[torch.Tensor]], **kwargs) -> None: ...
    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor]: ...

class LambdaLayer(nn.Module):
    function: Incomplete
    def __init__(self, function) -> None: ...
    def forward(self, x, *args): ...

class DistributionOutput:
    distribution_class: type
    in_features: int
    args_dim: Dict[str, int]
    dim: Incomplete
    def __init__(self, dim: int = 1) -> None: ...
    def distribution(self, distr_args, loc: Optional[torch.Tensor] = None, scale: Optional[torch.Tensor] = None) -> Distribution: ...
    @property
    def event_shape(self) -> Tuple:
        """
        Shape of each individual event contemplated by the distributions that this object constructs.
        """
    @property
    def event_dim(self) -> int:
        """
        Number of event dimensions, i.e., length of the `event_shape` tuple, of the distributions that this object
        constructs.
        """
    @property
    def value_in_support(self) -> float:
        """
        A float that will have a valid numeric value when computing the log-loss of the corresponding distribution. By
        default 0.0. This value will be used when padding data series.
        """
    def get_parameter_projection(self, in_features: int) -> nn.Module:
        """
        Return the parameter projection layer that maps the input to the appropriate parameters of the distribution.
        """
    def domain_map(self, *args: torch.Tensor):
        """
        Converts arguments to the right shape and domain. The domain depends on the type of distribution, while the
        correct shape is obtained by reshaping the trailing axis in such a way that the returned tensors define a
        distribution of the right event_shape.
        """
    @classmethod
    def squareplus(cls, x: torch.Tensor) -> torch.Tensor:
        """
        Helper to map inputs to the positive orthant by applying the square-plus operation. Reference:
        https://twitter.com/jon_barron/status/1387167648669048833
        """

class StudentTOutput(DistributionOutput):
    args_dim: Dict[str, int]
    distribution_class: type
    @classmethod
    def domain_map(cls, df: torch.Tensor, loc: torch.Tensor, scale: torch.Tensor): ...

class NormalOutput(DistributionOutput):
    args_dim: Dict[str, int]
    distribution_class: type
    @classmethod
    def domain_map(cls, loc: torch.Tensor, scale: torch.Tensor): ...

class NegativeBinomialOutput(DistributionOutput):
    args_dim: Dict[str, int]
    distribution_class: type
    @classmethod
    def domain_map(cls, total_count: torch.Tensor, logits: torch.Tensor): ...
    def distribution(self, distr_args, loc: Optional[torch.Tensor] = None, scale: Optional[torch.Tensor] = None) -> Distribution: ...

class FeatureEmbedder(nn.Module):
    num_features: Incomplete
    embedders: Incomplete
    def __init__(self, cardinalities: List[int], embedding_dims: List[int]) -> None: ...
    def forward(self, features: torch.Tensor) -> torch.Tensor: ...

class MeanScaler(nn.Module):
    """
    Computes a scaling factor as the weighted average absolute value along dimension `dim`, and scales the data
    accordingly.

    Args:
        dim (`int`):
            Dimension along which to compute the scale.
        keepdim (`bool`, *optional*, defaults to `False`):
            Controls whether to retain dimension `dim` (of length 1) in the scale tensor, or suppress it.
        minimum_scale (`float`, *optional*, defaults to 1e-10):
            Default scale that is used for elements that are constantly zero along dimension `dim`.
    """
    dim: Incomplete
    keepdim: Incomplete
    def __init__(self, dim: int, keepdim: bool = False, minimum_scale: float = 1e-10) -> None: ...
    def forward(self, data: torch.Tensor, weights: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]: ...

class NOPScaler(nn.Module):
    """
    Assigns a scaling factor equal to 1 along dimension `dim`, and therefore applies no scaling to the input data.

    Args:
        dim (`int`):
            Dimension along which to compute the scale.
        keepdim (`bool`, *optional*, defaults to `False`):
            Controls whether to retain dimension `dim` (of length 1) in the scale tensor, or suppress it.
    """
    dim: Incomplete
    keepdim: Incomplete
    def __init__(self, dim: int, keepdim: bool = False) -> None: ...
    def forward(self, data: torch.Tensor, observed_indicator: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]: ...

def weighted_average(input_tensor: torch.Tensor, weights: Optional[torch.Tensor] = None, dim: Incomplete | None = None) -> torch.Tensor:
    """
    Computes the weighted average of a given tensor across a given `dim`, masking values associated with weight zero,
    meaning instead of `nan * 0 = nan` you will get `0 * 0 = 0`.

    Args:
        input_tensor (`torch.FloatTensor`):
            Input tensor, of which the average must be computed.
        weights (`torch.FloatTensor`, *optional*):
            Weights tensor, of the same shape as `input_tensor`.
        dim (`int`, *optional*):
            The dim along which to average `input_tensor`.

    Returns:
        `torch.FloatTensor`: The tensor with values averaged along the specified `dim`.
    """

class NegativeLogLikelihood:
    """
    Computes the negative log likelihood loss from input distribution with respect to target.
    """
    def __call__(self, input: torch.distributions.Distribution, target: torch.Tensor) -> torch.Tensor: ...

@dataclass
class Seq2SeqTimeSeriesModelOutput(ModelOutput):
    """
    Base class for model encoder's outputs that also contains pre-computed hidden states that can speed up sequential
    decoding.

    Args:
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the decoder of the model.

            If `past_key_values` is used only the last hidden-state of the sequences of shape `(batch_size, 1,
            hidden_size)` is output.
        past_key_values (`tuple(tuple(torch.FloatTensor))`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            Tuple of `tuple(torch.FloatTensor)` of length `config.n_layers`, with each tuple having 2 tensors of shape
            `(batch_size, num_heads, sequence_length, embed_size_per_head)`) and 2 additional tensors of shape
            `(batch_size, num_heads, encoder_sequence_length, embed_size_per_head)`.

            Contains pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
            blocks) that can be used (see `past_key_values` input) to speed up sequential decoding.
        decoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the decoder at the output of each layer plus the optional initial embedding outputs.
        decoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the decoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        cross_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the decoder's cross-attention layer, after the attention softmax, used to compute the
            weighted average in the cross-attention heads.
        encoder_last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the encoder of the model.
        encoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the encoder at the output of each layer plus the optional initial embedding outputs.
        encoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the encoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        scale: (`torch.FloatTensor` of shape `(batch_size,)`, *optional*):
            Scaling values of each time series' context window which is used to give the model inputs of the same
            magnitude and then used to rescale to the original scale.
        static_features: (`torch.FloatTensor` of shape `(batch_size, feature size)`, *optional*):
            Static features of each time series' in a batch which are copied to the covariates at inference time.
    """
    last_hidden_state: torch.FloatTensor = ...
    past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = ...
    decoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    cross_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_last_hidden_state: Optional[torch.FloatTensor] = ...
    encoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    scale: Optional[torch.FloatTensor] = ...
    static_features: Optional[torch.FloatTensor] = ...
    def __init__(self, last_hidden_state, past_key_values, decoder_hidden_states, decoder_attentions, cross_attentions, encoder_last_hidden_state, encoder_hidden_states, encoder_attentions, scale, static_features) -> None: ...

@dataclass
class Seq2SeqTimeSeriesPredictionOutput(ModelOutput):
    """
    Base class for model's predictions outputs that also contain the loss as well parameters of the chosen
    distribution.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when a `future_values` is provided):
            Distributional loss.
        params (`torch.FloatTensor` of shape `(batch_size, num_samples, num_params)`):
            Parameters of the chosen distribution.
        past_key_values (`tuple(tuple(torch.FloatTensor))`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            Tuple of `tuple(torch.FloatTensor)` of length `config.n_layers`, with each tuple having 2 tensors of shape
            `(batch_size, num_heads, sequence_length, embed_size_per_head)`) and 2 additional tensors of shape
            `(batch_size, num_heads, encoder_sequence_length, embed_size_per_head)`.

            Contains pre-computed hidden-states (key and values in the self-attention blocks and in the cross-attention
            blocks) that can be used (see `past_key_values` input) to speed up sequential decoding.
        decoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the decoder at the output of each layer plus the initial embedding outputs.
        decoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the decoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        cross_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the decoder's cross-attention layer, after the attention softmax, used to compute the
            weighted average in the cross-attention heads.
        encoder_last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the encoder of the model.
        encoder_hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the encoder at the output of each layer plus the initial embedding outputs.
        encoder_attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the encoder, after the attention softmax, used to compute the weighted average in the
            self-attention heads.
        scale: (`torch.FloatTensor` of shape `(batch_size,)`, *optional*):
            Scaling values of each time series' context window which is used to give the model inputs of the same
            magnitude and then used to rescale to the original scale.
        static_features: (`torch.FloatTensor` of shape `(batch_size, feature size)`, *optional*):
            Static features of each time series' in a batch which are copied to the covariates at inference time.
    """
    loss: Optional[torch.FloatTensor] = ...
    params: Optional[Tuple[torch.FloatTensor]] = ...
    past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = ...
    decoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    decoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    cross_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_last_hidden_state: Optional[torch.FloatTensor] = ...
    encoder_hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    encoder_attentions: Optional[Tuple[torch.FloatTensor]] = ...
    scale: Optional[torch.FloatTensor] = ...
    static_features: Optional[torch.FloatTensor] = ...
    def __init__(self, loss, params, past_key_values, decoder_hidden_states, decoder_attentions, cross_attentions, encoder_last_hidden_state, encoder_hidden_states, encoder_attentions, scale, static_features) -> None: ...

@dataclass
class SampleTimeSeriesPredictionOutput(ModelOutput):
    sequences: torch.FloatTensor = ...
    def __init__(self, sequences) -> None: ...

class TimeSeriesTransformerAttention(nn.Module):
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

class TimeSeriesTransformerEncoderLayer(nn.Module):
    embed_dim: Incomplete
    self_attn: Incomplete
    self_attn_layer_norm: Incomplete
    dropout: Incomplete
    activation_fn: Incomplete
    activation_dropout: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: TimeSeriesTransformerConfig) -> None: ...
    def forward(self, hidden_states: torch.FloatTensor, attention_mask: torch.FloatTensor, layer_head_mask: torch.FloatTensor, output_attentions: Optional[bool] = False) -> Tuple[torch.FloatTensor, Optional[torch.FloatTensor]]:
        """
        Args:
            hidden_states (`torch.FloatTensor`): input to the layer of shape `(seq_len, batch, embed_dim)`
            attention_mask (`torch.FloatTensor`): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            layer_head_mask (`torch.FloatTensor`): mask for attention heads in a given layer of size
                `(encoder_attention_heads,)`.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
        """

class TimeSeriesTransformerDecoderLayer(nn.Module):
    embed_dim: Incomplete
    self_attn: Incomplete
    dropout: Incomplete
    activation_fn: Incomplete
    activation_dropout: Incomplete
    self_attn_layer_norm: Incomplete
    encoder_attn: Incomplete
    encoder_attn_layer_norm: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config: TimeSeriesTransformerConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, encoder_hidden_states: Optional[torch.Tensor] = None, encoder_attention_mask: Optional[torch.Tensor] = None, layer_head_mask: Optional[torch.Tensor] = None, cross_attn_layer_head_mask: Optional[torch.Tensor] = None, past_key_value: Optional[Tuple[torch.Tensor]] = None, output_attentions: Optional[bool] = False, use_cache: Optional[bool] = True) -> Tuple[torch.FloatTensor, Optional[Tuple[torch.FloatTensor, torch.FloatTensor]]]:
        """
        Args:
            hidden_states (`torch.FloatTensor`): input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`torch.FloatTensor`): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            encoder_hidden_states (`torch.FloatTensor`):
                cross attention input to the layer of shape `(batch, seq_len, embed_dim)`
            encoder_attention_mask (`torch.FloatTensor`): encoder attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
            layer_head_mask (`torch.FloatTensor`): mask for attention heads in a given layer of size
                `(encoder_attention_heads,)`.
            cross_attn_layer_head_mask (`torch.FloatTensor`): mask for cross-attention heads in a given layer of
                size `(decoder_attention_heads,)`.
            past_key_value (`Tuple(torch.FloatTensor)`): cached past key and value projection states
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
        """

class TimeSeriesTransformerPreTrainedModel(PreTrainedModel):
    config_class = TimeSeriesTransformerConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

TIME_SERIES_TRANSFORMER_START_DOCSTRING: str
TIME_SERIES_TRANSFORMER_INPUTS_DOCSTRING: str

class TimeSeriesTransformerEncoder(TimeSeriesTransformerPreTrainedModel):
    """
    Transformer encoder consisting of *config.encoder_layers* self attention layers. Each layer is a
    [`TimeSeriesTransformerEncoderLayer`].

    Args:
        config: TimeSeriesTransformerConfig
    """
    dropout: Incomplete
    layerdrop: Incomplete
    layers: Incomplete
    layernorm_embedding: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: TimeSeriesTransformerConfig) -> None: ...
    def forward(self, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]:
        """
        Args:
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            head_mask (`torch.Tensor` of shape `(encoder_layers, encoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
                Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation.
                This is useful if you want more control over how to convert `input_ids` indices into associated vectors
                than the model's internal embedding lookup matrix.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """

class TimeSeriesTransformerDecoder(TimeSeriesTransformerPreTrainedModel):
    """
    Transformer decoder consisting of *config.decoder_layers* layers. Each layer is a
    [`TimeSeriesTransformerDecoderLayer`]

    Args:
        config: TimeSeriesTransformerConfig
    """
    dropout: Incomplete
    layerdrop: Incomplete
    layers: Incomplete
    layernorm_embedding: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: TimeSeriesTransformerConfig) -> None: ...
    def forward(self, attention_mask: Optional[torch.Tensor] = None, encoder_hidden_states: Optional[torch.FloatTensor] = None, encoder_attention_mask: Optional[torch.LongTensor] = None, head_mask: Optional[torch.Tensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, past_key_values: Optional[List[torch.FloatTensor]] = None, inputs_embeds: Optional[torch.FloatTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutputWithPastAndCrossAttentions]:
        """
        Args:
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            encoder_hidden_states (`torch.FloatTensor` of shape `(batch_size, encoder_sequence_length, hidden_size)`, *optional*):
                Sequence of hidden-states at the output of the last layer of the encoder. Used in the cross-attention
                of the decoder.
            encoder_attention_mask (`torch.LongTensor` of shape `(batch_size, encoder_sequence_length)`, *optional*):
                Mask to avoid performing cross-attention on padding tokens indices of encoder input_ids. Mask values
                selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            head_mask (`torch.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the attention modules. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            cross_attn_head_mask (`torch.Tensor` of shape `(decoder_layers, decoder_attention_heads)`, *optional*):
                Mask to nullify selected heads of the cross-attention modules in the decoder to avoid performing
                cross-attention on hidden heads. Mask values selected in `[0, 1]`:

                - 1 indicates the head is **not masked**,
                - 0 indicates the head is **masked**.

            past_key_values (`tuple(tuple(torch.FloatTensor))`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
                Tuple of `tuple(torch.FloatTensor)` of length `config.n_layers`, with each tuple having 2 tensors of
                shape `(batch_size, num_heads, sequence_length, embed_size_per_head)`) and 2 additional tensors of
                shape `(batch_size, num_heads, encoder_sequence_length, embed_size_per_head)`.

                Contains pre-computed hidden-states (key and values in the self-attention blocks and in the
                cross-attention blocks) that can be used (see `past_key_values` input) to speed up sequential decoding.

                If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those
                that don't have their past key value states given to this model) of shape `(batch_size, 1)` instead of
                all `decoder_input_ids` of shape `(batch_size, sequence_length)`.

            inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
                Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation.
                This is useful if you want more control over how to convert `input_ids` indices into associated vectors
                than the model's internal embedding lookup matrix.

            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.

            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.

            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """

class TimeSeriesTransformerModel(TimeSeriesTransformerPreTrainedModel):
    scaler: Incomplete
    embedder: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    def __init__(self, config: TimeSeriesTransformerConfig) -> None: ...
    def get_lagged_subsequences(self, sequence: torch.Tensor, subsequences_length: int, shift: int = 0) -> torch.Tensor:
        """
        Returns lagged subsequences of a given sequence. Returns a tensor of shape (N, S, C, I),
            where S = subsequences_length and I = len(indices), containing lagged subsequences. Specifically, lagged[i,
            j, :, k] = sequence[i, -indices[k]-S+j, :].

        Args:
            sequence: Tensor
                The sequence from which lagged subsequences should be extracted. Shape: (N, T, C).
            subsequences_length : int
                Length of the subsequences to be extracted.
            shift: int
                Shift the lags by this amount back.
        """
    def create_network_inputs(self, past_values: torch.Tensor, past_time_features: torch.Tensor, static_categorical_features: torch.Tensor, static_real_features: torch.Tensor, past_observed_mask: Optional[torch.Tensor] = None, future_values: Optional[torch.Tensor] = None, future_time_features: Optional[torch.Tensor] = None): ...
    def enc_dec_outputs(self, transformer_inputs): ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def forward(self, past_values: torch.Tensor, past_time_features: torch.Tensor, past_observed_mask: torch.Tensor, static_categorical_features: torch.Tensor, static_real_features: torch.Tensor, future_values: Optional[torch.Tensor] = None, future_time_features: Optional[torch.Tensor] = None, decoder_attention_mask: Optional[torch.LongTensor] = None, head_mask: Optional[torch.Tensor] = None, decoder_head_mask: Optional[torch.Tensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[List[torch.FloatTensor]] = None, past_key_values: Optional[List[torch.FloatTensor]] = None, output_hidden_states: Optional[bool] = None, output_attentions: Optional[bool] = None, use_cache: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Seq2SeqTimeSeriesModelOutput, Tuple]:
        '''
        Returns:

        Examples:

        ```python
        >>> from huggingface_hub import hf_hub_download
        >>> import torch
        >>> from transformers import TimeSeriesTransformerModel

        >>> file = hf_hub_download(
        ...     repo_id="kashif/tourism-monthly-batch", filename="train-batch.pt", repo_type="dataset"
        ... )
        >>> batch = torch.load(file)

        >>> model = TimeSeriesTransformerModel.from_pretrained("huggingface/time-series-transformer-tourism-monthly")

        >>> # during training, one provides both past and future values
        >>> # as well as possible additional features
        >>> outputs = model(
        ...     past_values=batch["past_values"],
        ...     past_time_features=batch["past_time_features"],
        ...     past_observed_mask=batch["past_observed_mask"],
        ...     static_categorical_features=batch["static_categorical_features"],
        ...     static_real_features=batch["static_real_features"],
        ...     future_values=batch["future_values"],
        ...     future_time_features=batch["future_time_features"],
        ... )

        >>> last_hidden_state = outputs.last_hidden_state
        ```'''

class TimeSeriesTransformerForPrediction(TimeSeriesTransformerPreTrainedModel):
    model: Incomplete
    distribution_output: Incomplete
    parameter_projection: Incomplete
    target_shape: Incomplete
    loss: Incomplete
    def __init__(self, config: TimeSeriesTransformerConfig) -> None: ...
    def output_params(self, dec_output): ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def output_distribution(self, params, scale: Incomplete | None = None, trailing_n: Incomplete | None = None) -> torch.distributions.Distribution: ...
    def forward(self, past_values: torch.Tensor, past_time_features: torch.Tensor, past_observed_mask: torch.Tensor, static_categorical_features: torch.Tensor, static_real_features: torch.Tensor, future_values: Optional[torch.Tensor] = None, future_time_features: Optional[torch.Tensor] = None, future_observed_mask: Optional[torch.Tensor] = None, decoder_attention_mask: Optional[torch.LongTensor] = None, head_mask: Optional[torch.Tensor] = None, decoder_head_mask: Optional[torch.Tensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[List[torch.FloatTensor]] = None, past_key_values: Optional[List[torch.FloatTensor]] = None, output_hidden_states: Optional[bool] = None, output_attentions: Optional[bool] = None, use_cache: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Seq2SeqTimeSeriesModelOutput, Tuple]:
        '''
        Returns:

        future_observed_mask (`torch.BoolTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Boolean mask to indicate which `future_values` were observed and which were missing. Mask values selected
            in `[0, 1]`:

            - 1 for values that are **observed**,
            - 0 for values that are **missing** (i.e. NaNs that were replaced by zeros).

            This mask is used to filter out missing values for the final loss calculation.

        Examples:

        ```python
        >>> from huggingface_hub import hf_hub_download
        >>> import torch
        >>> from transformers import TimeSeriesTransformerForPrediction

        >>> file = hf_hub_download(
        ...     repo_id="kashif/tourism-monthly-batch", filename="train-batch.pt", repo_type="dataset"
        ... )
        >>> batch = torch.load(file)

        >>> model = TimeSeriesTransformerForPrediction.from_pretrained(
        ...     "huggingface/time-series-transformer-tourism-monthly"
        ... )

        >>> # during training, one provides both past and future values
        >>> # as well as possible additional features
        >>> outputs = model(
        ...     past_values=batch["past_values"],
        ...     past_time_features=batch["past_time_features"],
        ...     past_observed_mask=batch["past_observed_mask"],
        ...     static_categorical_features=batch["static_categorical_features"],
        ...     static_real_features=batch["static_real_features"],
        ...     future_values=batch["future_values"],
        ...     future_time_features=batch["future_time_features"],
        ... )

        >>> loss = outputs.loss
        >>> loss.backward()

        >>> # during inference, one only provides past values
        >>> # as well as possible additional features
        >>> # the model autoregressively generates future values
        >>> outputs = model.generate(
        ...     past_values=batch["past_values"],
        ...     past_time_features=batch["past_time_features"],
        ...     past_observed_mask=batch["past_observed_mask"],
        ...     static_categorical_features=batch["static_categorical_features"],
        ...     static_real_features=batch["static_real_features"],
        ...     future_time_features=batch["future_time_features"],
        ... )

        >>> mean_prediction = outputs.sequences.mean(dim=1)
        ```'''
    def generate(self, static_categorical_features: torch.Tensor, static_real_features: torch.Tensor, past_time_features: torch.Tensor, past_values: torch.Tensor, past_observed_mask: torch.Tensor, future_time_features: Optional[torch.Tensor], output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None) -> torch.Tensor: ...
