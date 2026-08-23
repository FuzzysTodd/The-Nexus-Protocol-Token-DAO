import torch
import torch.nn as nn
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutputWithNoAttention as BaseModelOutputWithNoAttention, SequenceClassifierOutput as SequenceClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import logging as logging
from .configuration_graphormer import GraphormerConfig as GraphormerConfig
from _typeshed import Incomplete
from typing import Optional, Tuple, Union

logger: Incomplete
GRAPHORMER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def quant_noise(module, p, block_size):
    '''
    From:
    https://github.com/facebookresearch/fairseq/blob/dd0079bde7f678b0cd0715cbd0ae68d661b7226d/fairseq/modules/quant_noise.py

    Wraps modules and applies quantization noise to the weights for subsequent quantization with Iterative Product
    Quantization as described in "Training with Quantization Noise for Extreme Model Compression"

    Args:
        - module: nn.Module
        - p: amount of Quantization Noise
        - block_size: size of the blocks for subsequent quantization with iPQ

    Remarks:
        - Module weights must have the right sizes wrt the block size
        - Only Linear, Embedding and Conv2d modules are supported for the moment
        - For more detail on how to quantize by blocks with convolutional weights, see "And the Bit Goes Down:
          Revisiting the Quantization of Neural Networks"
        - We implement the simplest form of noise here as stated in the paper which consists in randomly dropping
          blocks
    '''

class LayerDropModuleList(nn.ModuleList):
    """
    From:
    https://github.com/facebookresearch/fairseq/blob/dd0079bde7f678b0cd0715cbd0ae68d661b7226d/fairseq/modules/layer_drop.py
    A LayerDrop implementation based on [`torch.nn.ModuleList`]. LayerDrop as described in
    https://arxiv.org/abs/1909.11556.

    We refresh the choice of which layers to drop every time we iterate over the LayerDropModuleList instance. During
    evaluation we always iterate over all layers.

    Usage:

    ```python
    layers = LayerDropList(p=0.5, modules=[layer1, layer2, layer3])
    for layer in layers:  # this might iterate over layers 1 and 3
        x = layer(x)
    for layer in layers:  # this might iterate over all layers
        x = layer(x)
    for layer in layers:  # this might not iterate over any layers
        x = layer(x)
    ```

    Args:
        p (float): probability of dropping out each layer
        modules (iterable, optional): an iterable of modules to add
    """
    p: Incomplete
    def __init__(self, p, modules: Incomplete | None = None) -> None: ...
    def __iter__(self): ...

class GraphormerGraphNodeFeature(nn.Module):
    """
    Compute node features for each node in the graph.
    """
    num_heads: Incomplete
    num_atoms: Incomplete
    atom_encoder: Incomplete
    in_degree_encoder: Incomplete
    out_degree_encoder: Incomplete
    graph_token: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_nodes, in_degree, out_degree): ...

class GraphormerGraphAttnBias(nn.Module):
    """
    Compute attention bias for each head.
    """
    num_heads: Incomplete
    multi_hop_max_dist: Incomplete
    edge_encoder: Incomplete
    edge_type: Incomplete
    edge_dis_encoder: Incomplete
    spatial_pos_encoder: Incomplete
    graph_token_virtual_distance: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_nodes, attn_bias, spatial_pos, input_edges, attn_edge_type): ...

class GraphormerMultiheadAttention(nn.Module):
    '''Multi-headed attention.

    See "Attention Is All You Need" for more details.
    '''
    embedding_dim: Incomplete
    kdim: Incomplete
    vdim: Incomplete
    qkv_same_dim: Incomplete
    num_heads: Incomplete
    dropout_module: Incomplete
    head_dim: Incomplete
    scaling: Incomplete
    self_attention: bool
    k_proj: Incomplete
    v_proj: Incomplete
    q_proj: Incomplete
    out_proj: Incomplete
    onnx_trace: bool
    def __init__(self, config) -> None: ...
    def reset_parameters(self) -> None: ...
    def forward(self, query, key: Optional[torch.Tensor], value: Optional[torch.Tensor], attn_bias: Optional[torch.Tensor], key_padding_mask: Optional[torch.Tensor] = None, need_weights: bool = True, attn_mask: Optional[torch.Tensor] = None, before_softmax: bool = False, need_head_weights: bool = False) -> Tuple[torch.Tensor, Optional[torch.Tensor]]:
        """
        Args:
            key_padding_mask (Bytetorch.Tensor, optional): mask to exclude
                keys that are pads, of shape `(batch, src_len)`, where padding elements are indicated by 1s.
            need_weights (bool, optional): return the attention weights,
                averaged over heads (default: False).
            attn_mask (Bytetorch.Tensor, optional): typically used to
                implement causal attention, where the mask prevents the attention from looking forward in time
                (default: None).
            before_softmax (bool, optional): return the raw attention
                weights and values before the attention softmax.
            need_head_weights (bool, optional): return the attention
                weights for each head. Implies *need_weights*. Default: return the average attention weights over all
                heads.
        """
    def apply_sparse_mask(self, attn_weights, tgt_len: int, src_len: int, bsz: int): ...

class GraphormerGraphEncoderLayer(nn.Module):
    embedding_dim: Incomplete
    num_attention_heads: Incomplete
    attention_dropout: Incomplete
    q_noise: Incomplete
    qn_block_size: Incomplete
    pre_layernorm: Incomplete
    dropout_module: Incomplete
    activation_dropout_module: Incomplete
    activation_fn: Incomplete
    self_attn: Incomplete
    self_attn_layer_norm: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    final_layer_norm: Incomplete
    def __init__(self, config) -> None: ...
    def build_fc(self, input_dim, output_dim, q_noise, qn_block_size): ...
    def forward(self, input_nodes: torch.Tensor, self_attn_bias: Optional[torch.Tensor] = None, self_attn_mask: Optional[torch.Tensor] = None, self_attn_padding_mask: Optional[torch.Tensor] = None):
        """
        nn.LayerNorm is applied either before or after the self-attention/ffn modules similar to the original
        Transformer implementation.
        """

class GraphormerGraphEncoder(nn.Module):
    dropout_module: Incomplete
    layerdrop: Incomplete
    embedding_dim: Incomplete
    apply_graphormer_init: Incomplete
    traceable: Incomplete
    graph_node_feature: Incomplete
    graph_attn_bias: Incomplete
    embed_scale: Incomplete
    quant_noise: Incomplete
    emb_layer_norm: Incomplete
    final_layer_norm: Incomplete
    layers: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_nodes, input_edges, attn_bias, in_degree, out_degree, spatial_pos, attn_edge_type, perturb: Incomplete | None = None, last_state_only: bool = False, token_embeddings: Optional[torch.Tensor] = None, attn_mask: Optional[torch.Tensor] = None) -> Tuple[torch.torch.Tensor, torch.Tensor]: ...

class GraphormerDecoderHead(nn.Module):
    lm_output_learned_bias: Incomplete
    classifier: Incomplete
    num_classes: Incomplete
    def __init__(self, embedding_dim, num_classes) -> None: ...
    def forward(self, input_nodes, **unused): ...

class GraphormerPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = GraphormerConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool
    main_input_name_nodes: str
    main_input_name_edges: str
    def normal_(self, data) -> None: ...
    def init_graphormer_params(self, module) -> None:
        """
        Initialize the weights specific to the Graphormer Model.
        """

class GraphormerModel(GraphormerPreTrainedModel):
    """The Graphormer model is a graph-encoder model.

    It goes from a graph to its representation. If you want to use the model for a downstream classification task, use
    GraphormerForGraphClassification instead. For any other downstream task, feel free to add a new class, or combine
    this model with a downstream model of your choice, following the example in GraphormerForGraphClassification.
    """
    graph_encoder: Incomplete
    share_input_output_embed: Incomplete
    lm_output_learned_bias: Incomplete
    load_softmax: Incomplete
    lm_head_transform_weight: Incomplete
    activation_fn: Incomplete
    layer_norm: Incomplete
    def __init__(self, config) -> None: ...
    def reset_output_layer_parameters(self) -> None: ...
    def forward(self, input_nodes, input_edges, attn_bias, in_degree, out_degree, spatial_pos, attn_edge_type, perturb: Incomplete | None = None, masked_tokens: Incomplete | None = None, return_dict: Optional[bool] = True, **unused): ...
    def max_nodes(self):
        """Maximum output length supported by the encoder."""

class GraphormerForGraphClassification(GraphormerPreTrainedModel):
    """
    This model can be used for graph-level classification or regression tasks.

    It can be trained on
    - regression (by setting config.num_classes to 1); there should be one float-type label per graph
    - one task classification (by setting config.num_classes to the number of classes); there should be one integer
      label per graph
    - binary multi-task classification (by setting config.num_classes to the number of labels); there should be a list
      of integer labels for each graph.
    """
    encoder: Incomplete
    embedding_dim: Incomplete
    num_classes: Incomplete
    classifier: Incomplete
    is_encoder_decoder: bool
    def __init__(self, config) -> None: ...
    def forward(self, input_nodes, input_edges, attn_bias, in_degree, out_degree, spatial_pos, attn_edge_type, labels: Optional[torch.LongTensor] = None, return_dict: Optional[bool] = True, **unused) -> Union[Tuple[torch.Tensor], SequenceClassifierOutput]: ...
