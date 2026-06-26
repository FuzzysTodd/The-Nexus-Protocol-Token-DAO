from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Optional

logger: Incomplete
ESM_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class EsmConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`ESMModel`]. It is used to instantiate a ESM model
    according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the ESM
    [facebook/esm-1b](https://huggingface.co/facebook/esm-1b) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*):
            Vocabulary size of the ESM model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`ESMModel`].
        mask_token_id (`int`, *optional*):
            The index of the mask token in the vocabulary. This must be included in the config because of the
            "mask-dropout" scaling trick, which will scale the inputs depending on the number of masked tokens.
        pad_token_id (`int`, *optional*):
            The index of the padding token in the vocabulary. This must be included in the config because certain parts
            of the ESM code use this instead of the attention mask.
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimensionality of the "intermediate" (often named feed-forward) layer in the Transformer encoder.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 1026):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        position_embedding_type (`str`, *optional*, defaults to `"absolute"`):
            Type of position embedding. Choose one of `"absolute"`, `"relative_key"`, `"relative_key_query", "rotary"`.
            For positional embeddings use `"absolute"`. For more information on `"relative_key"`, please refer to
            [Self-Attention with Relative Position Representations (Shaw et al.)](https://arxiv.org/abs/1803.02155).
            For more information on `"relative_key_query"`, please refer to *Method 4* in [Improve Transformer Models
            with Better Relative Position Embeddings (Huang et al.)](https://arxiv.org/abs/2009.13658).
        is_decoder (`bool`, *optional*, defaults to `False`):
            Whether the model is used as a decoder or not. If `False`, the model is used as an encoder.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.
        classifier_dropout (`float`, *optional*):
            The dropout ratio for the classification head.
        emb_layer_norm_before (`bool`, *optional*):
            Whether to apply layer normalization after embeddings but before the main stem of the network.
        token_dropout (`bool`, defaults to `False`):
            When this is enabled, masked tokens are treated as if they had been dropped out by input dropout.

    Examples:

    ```python
    >>> from transformers import EsmModel, EsmConfig

    >>> # Initializing a ESM facebook/esm-1b style configuration >>> configuration = EsmConfig()

    >>> # Initializing a model from the configuration >>> model = ESMModel(configuration)

    >>> # Accessing the model configuration >>> configuration = model.config
    ```'''
    model_type: str
    vocab_size: Incomplete
    hidden_size: Incomplete
    num_hidden_layers: Incomplete
    num_attention_heads: Incomplete
    intermediate_size: Incomplete
    hidden_dropout_prob: Incomplete
    attention_probs_dropout_prob: Incomplete
    max_position_embeddings: Incomplete
    initializer_range: Incomplete
    layer_norm_eps: Incomplete
    position_embedding_type: Incomplete
    use_cache: Incomplete
    classifier_dropout: Incomplete
    emb_layer_norm_before: Incomplete
    token_dropout: Incomplete
    is_folding_model: Incomplete
    esmfold_config: Incomplete
    vocab_list: Incomplete
    def __init__(self, vocab_size: Incomplete | None = None, mask_token_id: Incomplete | None = None, pad_token_id: Incomplete | None = None, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, hidden_dropout_prob: float = 0.1, attention_probs_dropout_prob: float = 0.1, max_position_embeddings: int = 1026, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, position_embedding_type: str = 'absolute', use_cache: bool = True, classifier_dropout: Incomplete | None = None, emb_layer_norm_before: Incomplete | None = None, token_dropout: bool = False, is_folding_model: bool = False, esmfold_config: Incomplete | None = None, vocab_list: Incomplete | None = None, **kwargs) -> None: ...
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """

@dataclass
class EsmFoldConfig:
    esm_type: str = ...
    fp16_esm: bool = ...
    use_esm_attn_map: bool = ...
    esm_ablate_pairwise: bool = ...
    esm_ablate_sequence: bool = ...
    esm_input_dropout: float = ...
    embed_aa: bool = ...
    bypass_lm: bool = ...
    lddt_head_hid_dim: int = ...
    trunk: TrunkConfig = ...
    def __post_init__(self) -> None: ...
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
    def __init__(self, esm_type, fp16_esm, use_esm_attn_map, esm_ablate_pairwise, esm_ablate_sequence, esm_input_dropout, embed_aa, bypass_lm, lddt_head_hid_dim, trunk) -> None: ...

@dataclass
class TrunkConfig:
    num_blocks: int = ...
    sequence_state_dim: int = ...
    pairwise_state_dim: int = ...
    sequence_head_width: int = ...
    pairwise_head_width: int = ...
    position_bins: int = ...
    dropout: float = ...
    layer_drop: float = ...
    cpu_grad_checkpoint: bool = ...
    max_recycles: int = ...
    chunk_size: Optional[int] = ...
    structure_module: StructureModuleConfig = ...
    def __post_init__(self) -> None: ...
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
    def __init__(self, num_blocks, sequence_state_dim, pairwise_state_dim, sequence_head_width, pairwise_head_width, position_bins, dropout, layer_drop, cpu_grad_checkpoint, max_recycles, chunk_size, structure_module) -> None: ...

@dataclass
class StructureModuleConfig:
    """
    Args:
        sequence_dim:
            Single representation channel dimension
        pairwise_dim:
            Pair representation channel dimension
        ipa_dim:
            IPA hidden channel dimension
        resnet_dim:
            Angle resnet (Alg. 23 lines 11-14) hidden channel dimension
        num_heads_ipa:
            Number of IPA heads
        num_qk_points:
            Number of query/key points to generate during IPA
        num_v_points:
            Number of value points to generate during IPA
        dropout_rate:
            Dropout rate used throughout the layer
        num_blocks:
            Number of structure module blocks
        num_transition_layers:
            Number of layers in the single representation transition (Alg. 23 lines 8-9)
        num_resnet_blocks:
            Number of blocks in the angle resnet
        num_angles:
            Number of angles to generate in the angle resnet
        trans_scale_factor:
            Scale of single representation transition hidden dimension
        epsilon:
            Small number used in angle resnet normalization
        inf:
            Large number used for attention masking
    """
    sequence_dim: int = ...
    pairwise_dim: int = ...
    ipa_dim: int = ...
    resnet_dim: int = ...
    num_heads_ipa: int = ...
    num_qk_points: int = ...
    num_v_points: int = ...
    dropout_rate: float = ...
    num_blocks: int = ...
    num_transition_layers: int = ...
    num_resnet_blocks: int = ...
    num_angles: int = ...
    trans_scale_factor: int = ...
    epsilon: float = ...
    inf: float = ...
    def to_dict(self): ...
    def __init__(self, sequence_dim, pairwise_dim, ipa_dim, resnet_dim, num_heads_ipa, num_qk_points, num_v_points, dropout_rate, num_blocks, num_transition_layers, num_resnet_blocks, num_angles, trans_scale_factor, epsilon, inf) -> None: ...

def get_default_vocab_list(): ...
