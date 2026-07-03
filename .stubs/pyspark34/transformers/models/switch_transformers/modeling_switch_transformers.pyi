import torch
import torch.nn as nn
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import MoEModelOutput as MoEModelOutput, MoEModelOutputWithPastAndCrossAttentions as MoEModelOutputWithPastAndCrossAttentions, Seq2SeqMoEModelOutput as Seq2SeqMoEModelOutput, Seq2SeqMoEOutput as Seq2SeqMoEOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import ALL_LAYERNORM_LAYERS as ALL_LAYERNORM_LAYERS, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import DUMMY_INPUTS as DUMMY_INPUTS, DUMMY_MASK as DUMMY_MASK, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, is_torch_fx_proxy as is_torch_fx_proxy, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_switch_transformers import SwitchTransformersConfig as SwitchTransformersConfig
from _typeshed import Incomplete
from typing import Optional, Tuple, Union

logger: Incomplete
SWITCH_TRANSFORMERS_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def router_z_loss_func(router_logits: torch.Tensor) -> float:
    """
    Compute the router z-loss implemented in PyTorch.

    The router z-loss was introduced in [Designing Effective Sparse Expert Models](https://arxiv.org/abs/2202.08906).
    It encourages router logits to remain small in an effort to improve stability.

    Args:
        router_logits (`float`):
            Input logits of shape [batch_size, sequence_length, num_experts]

    Returns:
        Scalar router z-loss.
    """
def load_balancing_loss_func(router_probs: torch.Tensor, expert_indices: torch.Tensor) -> float:
    """
    Computes auxiliary load balancing loss as in Switch Transformer - implemented in Pytorch.

    See Switch Transformer (https://arxiv.org/abs/2101.03961) for more details. This function implements the loss
    function presented in equations (4) - (6) of the paper. It aims at penalizing cases where the routing between
    experts is too unbalanced.

    Args:
        router_probs (`torch.Tensor`):
            Probability assigned to each expert per token. Shape: [batch_size, seqeunce_length, num_experts].
        expert_indices (`torch.Tensor`):
            Indices tensor of shape [batch_size, seqeunce_length] identifying the selected expert for a given token.

    Returns:
        The auxiliary loss.
    """

class SwitchTransformersTop1Router(nn.Module):
    """
    Router using tokens choose top-1 experts assignment.

    This router uses the same mechanism as in Switch Transformer (https://arxiv.org/abs/2101.03961) and V-MoE
    (https://arxiv.org/abs/2106.05974): tokens choose their top experts. Items are sorted by router_probs and then
    routed to their choice of expert until the expert's expert_capacity is reached. **There is no guarantee that each
    token is processed by an expert**, or that each expert receives at least one token.

    """
    num_experts: Incomplete
    expert_capacity: Incomplete
    classifier: Incomplete
    jitter_noise: Incomplete
    ignore_padding_tokens: Incomplete
    dtype: Incomplete
    def __init__(self, config: SwitchTransformersConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> Tuple:
        """
        Generic forward function for every Router class. Each Router expects to have the same input hidden states
        (`hidden_states`) corresponding to the hidden states for each token, the `expert_capacity` corresponding to the
        number of tokens the Router will send to each expert, some Routers can send up to few tokens to each expert.

        Each Router works as the following: it expects the hidden states for each token, gets the `router_probs` and
        `router_logits` from the `router_weights`. This will assign for each token, the raw probability to be assigned
        to an expert. Then each Router class will have to define its own `_compute_routing_instructions`.

        Args:
            hidden_states (`torch.Tensor`) :
                [num_groups, tokens_per_group, hidden_dim] inputs to send to experts.
        Returns:
            Tuple[`torch.Tensor`, `torch.Tensor`, `torch.Tensor`] Tuple containing the expert index, the router probs
            and the router logits. The router probabilities and logits are required to compute the loss.
        """

class SwitchTransformersLayerNorm(nn.Module):
    weight: Incomplete
    variance_epsilon: Incomplete
    def __init__(self, hidden_size, eps: float = 1e-06) -> None:
        """
        Construct a layernorm module in the SwitchTransformers style. No bias and no subtraction of mean.
        """
    def forward(self, hidden_states): ...

class SwitchTransformersDenseActDense(nn.Module):
    wi: Incomplete
    wo: Incomplete
    dropout: Incomplete
    act: Incomplete
    def __init__(self, config: SwitchTransformersConfig) -> None: ...
    def forward(self, hidden_states): ...

class SwitchTransformersDenseGatedActDense(nn.Module):
    wi_0: Incomplete
    wi_1: Incomplete
    wo: Incomplete
    dropout: Incomplete
    act: Incomplete
    def __init__(self, config: SwitchTransformersConfig) -> None: ...
    def forward(self, hidden_states): ...

class SwitchTransformersSparseMLP(nn.Module):
    """
    Implementation of the Switch Transformers Sparse MLP module.
    """
    router: Incomplete
    experts: Incomplete
    def __init__(self, config: SwitchTransformersConfig, expert_class: nn.Module = ...) -> None: ...
    def forward(self, hidden_states):
        """
        Hold on, this will be slightly tricky to understand In the correct order, a MoE layer does the following:

        1- Gets the `router_mask` from the router. The shape of the mask is `(batch_size, sequence_length, num_expert)`
        and corresponds to the argmax of the `router_probs`. The probabilities are needed in the computation of the
        hidden states : they are broadcasted to the hidden states values (can be interpreted as a scaling factor).

        2- Dispatch the tokens to its associated experts. We do a classic for loop over the experts and assign for each
        expert the corresponding hidden states.

        """

class SwitchTransformersLayerFF(nn.Module):
    """
    Switch Transformers Feed Forward layer module. This is a wrapper around the Mixture of Experts module.

    Parameters:
        config : ([`SwitchTransformersConfig`]): Model configuration class with all the parameters of the model.
            Initializing with a config file does not load the weights associated with the model, only the
            configuration. Check out the [`~PreTrainedModel.from_pretrained`] method to load the model weights.
        is_sparse (`bool`):
            Whether the MLP layer is a `Sparse` layer (contains a Mixture of Experts) or not
    """
    is_sparse: Incomplete
    mlp: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config: SwitchTransformersConfig, is_sparse: bool = False) -> None: ...
    def forward(self, hidden_states, output_router_logits): ...

class SwitchTransformersAttention(nn.Module):
    is_decoder: Incomplete
    has_relative_attention_bias: Incomplete
    relative_attention_num_buckets: Incomplete
    relative_attention_max_distance: Incomplete
    d_model: Incomplete
    key_value_proj_dim: Incomplete
    n_heads: Incomplete
    dropout: Incomplete
    inner_dim: Incomplete
    q: Incomplete
    k: Incomplete
    v: Incomplete
    o: Incomplete
    relative_attention_bias: Incomplete
    pruned_heads: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: SwitchTransformersConfig, has_relative_attention_bias: bool = False) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def compute_bias(self, query_length, key_length, device: Incomplete | None = None):
        """Compute binned relative position bias"""
    def forward(self, hidden_states, mask: Incomplete | None = None, key_value_states: Incomplete | None = None, position_bias: Incomplete | None = None, past_key_value: Incomplete | None = None, layer_head_mask: Incomplete | None = None, query_length: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False):
        """
        Self-attention (if key_value_states is None) or attention over source sentence (provided by key_value_states).
        """

class SwitchTransformersLayerSelfAttention(nn.Module):
    SelfAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config, has_relative_attention_bias: bool = False) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False): ...

class SwitchTransformersLayerCrossAttention(nn.Module):
    EncDecAttention: Incomplete
    layer_norm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, key_value_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, use_cache: bool = False, query_length: Incomplete | None = None, output_attentions: bool = False): ...

class SwitchTransformersBlock(nn.Module):
    is_decoder: Incomplete
    is_sparse: Incomplete
    layer: Incomplete
    def __init__(self, config, has_relative_attention_bias: bool = False, is_sparse: bool = False) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, position_bias: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, encoder_decoder_position_bias: Incomplete | None = None, layer_head_mask: Incomplete | None = None, cross_attn_layer_head_mask: Incomplete | None = None, past_key_value: Incomplete | None = None, use_cache: bool = False, output_attentions: bool = False, output_router_logits: bool = True, return_dict: bool = True): ...

class SwitchTransformersPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = SwitchTransformersConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool
    @property
    def dummy_inputs(self): ...

class SwitchTransformersStack(SwitchTransformersPreTrainedModel):
    embed_tokens: Incomplete
    is_decoder: Incomplete
    block: Incomplete
    final_layer_norm: Incomplete
    dropout: Incomplete
    device_map: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config, embed_tokens: Incomplete | None = None) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, output_router_logits: bool = True, return_dict: Incomplete | None = None): ...

SWITCH_TRANSFORMERS_START_DOCSTRING: str
SWITCH_TRANSFORMERS_INPUTS_DOCSTRING: str
SWITCH_TRANSFORMERS_ENCODER_INPUTS_DOCSTRING: str

class SwitchTransformersModel(SwitchTransformersPreTrainedModel):
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    device_map: Incomplete
    def __init__(self, config: SwitchTransformersConfig) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.BoolTensor] = None, head_mask: Optional[torch.FloatTensor] = None, decoder_head_mask: Optional[torch.FloatTensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, inputs_embeds: Optional[torch.Tensor] = None, decoder_inputs_embeds: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_router_logits: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.FloatTensor], Seq2SeqMoEModelOutput]:
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, SwitchTransformersModel

        >>> tokenizer = AutoTokenizer.from_pretrained("google/switch-base-8")
        >>> model = SwitchTransformersModel.from_pretrained("google/switch-base-8")

        >>> input_ids = tokenizer(
        ...     "Studies have been shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> decoder_input_ids = tokenizer("Studies show that", return_tensors="pt").input_ids  # Batch size 1

        >>> # preprocess: Prepend decoder_input_ids with start token which is pad token for SwitchTransformersModel.
        >>> # This is not needed for torch\'s SwitchTransformersForConditionalGeneration as it does this internally using labels arg.
        >>> decoder_input_ids = model._shift_right(decoder_input_ids)

        >>> # forward pass
        >>> outputs = model(input_ids=input_ids, decoder_input_ids=decoder_input_ids)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''

class SwitchTransformersForConditionalGeneration(SwitchTransformersPreTrainedModel):
    model_dim: Incomplete
    shared: Incomplete
    encoder: Incomplete
    decoder: Incomplete
    lm_head: Incomplete
    router_z_loss_coef: Incomplete
    router_aux_loss_coef: Incomplete
    device_map: Incomplete
    def __init__(self, config: SwitchTransformersConfig) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def get_output_embeddings(self): ...
    def get_encoder(self): ...
    def get_decoder(self): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, decoder_input_ids: Optional[torch.LongTensor] = None, decoder_attention_mask: Optional[torch.BoolTensor] = None, head_mask: Optional[torch.FloatTensor] = None, decoder_head_mask: Optional[torch.FloatTensor] = None, cross_attn_head_mask: Optional[torch.Tensor] = None, encoder_outputs: Optional[Tuple[Tuple[torch.Tensor]]] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None, inputs_embeds: Optional[torch.FloatTensor] = None, decoder_inputs_embeds: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_router_logits: Optional[bool] = True, return_dict: Optional[bool] = None) -> Union[Tuple[torch.FloatTensor], Seq2SeqMoEOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[-100, 0, ...,
            config.vocab_size - 1]`. All labels set to `-100` are ignored (masked), the loss is only computed for
            labels in `[0, ..., config.vocab_size]`

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoTokenizer, SwitchTransformersForConditionalGeneration

        >>> tokenizer = AutoTokenizer.from_pretrained("google/switch-base-8")
        >>> model = SwitchTransformersForConditionalGeneration.from_pretrained("google/switch-base-8")

        >>> # training
        >>> input_ids = tokenizer("The <extra_id_0> walks in <extra_id_1> park", return_tensors="pt").input_ids
        >>> labels = tokenizer("<extra_id_0> cute dog <extra_id_1> the <extra_id_2>", return_tensors="pt").input_ids
        >>> outputs = model(input_ids=input_ids, labels=labels)
        >>> loss = outputs.loss
        >>> logits = outputs.logits

        >>> # inference
        >>> input_ids = tokenizer(
        ...     "summarize: studies have shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> outputs = model.generate(input_ids)
        >>> # . To, let’s say you have a dog. To summarize:
        >>> # Since the model has been trained on MLM, this will output gibberish
        ```'''
    def prepare_inputs_for_generation(self, input_ids, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, decoder_head_mask: Incomplete | None = None, cross_attn_head_mask: Incomplete | None = None, use_cache: Incomplete | None = None, encoder_outputs: Incomplete | None = None, **kwargs): ...
    def prepare_decoder_input_ids_from_labels(self, labels: torch.Tensor): ...

class SwitchTransformersEncoderModel(SwitchTransformersPreTrainedModel):
    shared: Incomplete
    encoder: Incomplete
    device_map: Incomplete
    def __init__(self, config: SwitchTransformersConfig) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def get_encoder(self): ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_router_logits: Optional[bool] = True, return_dict: Optional[bool] = None) -> Union[Tuple[torch.FloatTensor], MoEModelOutput]:
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, SwitchTransformersEncoderModel

        >>> tokenizer = AutoTokenizer.from_pretrained("google/switch-base-8")
        >>> model = SwitchTransformersEncoderModel.from_pretrained("google/switch-base-8")
        >>> input_ids = tokenizer(
        ...     "Studies have been shown that owning a dog is good for you", return_tensors="pt"
        ... ).input_ids  # Batch size 1
        >>> outputs = model(input_ids=input_ids)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''
