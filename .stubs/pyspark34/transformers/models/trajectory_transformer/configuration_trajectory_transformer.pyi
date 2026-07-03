from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
TRAJECTORY_TRANSFORMER_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class TrajectoryTransformerConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`TrajectoryTransformerModel`]. It is used to
    instantiate an TrajectoryTransformer model according to the specified arguments, defining the model architecture.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the
    TrajectoryTransformer
    [CarlCochet/trajectory-transformer-halfcheetah-medium-v2](https://huggingface.co/CarlCochet/trajectory-transformer-halfcheetah-medium-v2)
    architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 100):
            Vocabulary size of the TrajectoryTransformer model. Defines the number of different tokens that can be
            represented by the `trajectories` passed when calling [`TrajectoryTransformerModel`]
        action_weight (`int`, *optional*, defaults to 5):
            Weight of the action in the loss function
        reward_weight (`int`, *optional*, defaults to 1):
            Weight of the reward in the loss function
        value_weight (`int`, *optional*, defaults to 1):
            Weight of the value in the loss function
        block_size (`int`, *optional*, defaults to 249):
            Size of the blocks in the trajectory transformer.
        action_dim (`int`, *optional*, defaults to 6):
            Dimension of the action space.
        observation_dim (`int`, *optional*, defaults to 17):
            Dimension of the observation space.
        transition_dim (`int`, *optional*, defaults to 25):
            Dimension of the transition space.
        n_layer (`int`, *optional*, defaults to 4):
            Number of hidden layers in the Transformer encoder.
        n_head (`int`, *optional*, defaults to 4):
            Number of attention heads for each attention layer in the Transformer encoder.
        n_embd (`int`, *optional*, defaults to 128):
            Dimensionality of the embeddings and hidden states.
        resid_pdrop (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        embd_pdrop (`int`, *optional*, defaults to 0.1):
            The dropout ratio for the embeddings.
        attn_pdrop (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the `token_type_ids` passed when calling [`TrajectoryTransformerModel`]
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        kaiming_initializer_range (`float, *optional*, defaults to 1):
            A coefficient scaling the negative slope of the kaiming initializer rectifier for EinLinear layers.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.
        Example:

    ```python
    >>> from transformers import TrajectoryTransformerConfig, TrajectoryTransformerModel

    >>> # Initializing a TrajectoryTransformer CarlCochet/trajectory-transformer-halfcheetah-medium-v2 style configuration
    >>> configuration = TrajectoryTransformerConfig()

    >>> # Initializing a model (with random weights) from the CarlCochet/trajectory-transformer-halfcheetah-medium-v2 style configuration
    >>> model = TrajectoryTransformerModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    keys_to_ignore_at_inference: Incomplete
    attribute_map: Incomplete
    vocab_size: Incomplete
    action_weight: Incomplete
    reward_weight: Incomplete
    value_weight: Incomplete
    max_position_embeddings: Incomplete
    block_size: Incomplete
    action_dim: Incomplete
    observation_dim: Incomplete
    transition_dim: Incomplete
    learning_rate: Incomplete
    n_layer: Incomplete
    n_head: Incomplete
    n_embd: Incomplete
    embd_pdrop: Incomplete
    attn_pdrop: Incomplete
    resid_pdrop: Incomplete
    initializer_range: Incomplete
    type_vocab_size: Incomplete
    layer_norm_eps: Incomplete
    kaiming_initializer_range: Incomplete
    use_cache: Incomplete
    def __init__(self, vocab_size: int = 100, action_weight: int = 5, reward_weight: int = 1, value_weight: int = 1, block_size: int = 249, action_dim: int = 6, observation_dim: int = 17, transition_dim: int = 25, n_layer: int = 4, n_head: int = 4, n_embd: int = 128, embd_pdrop: float = 0.1, attn_pdrop: float = 0.1, resid_pdrop: float = 0.1, learning_rate: float = 0.0006, max_position_embeddings: int = 512, type_vocab_size: int = 2, initializer_range: float = 0.02, layer_norm_eps: float = 1e-12, kaiming_initializer_range: int = 1, use_cache: bool = True, pad_token_id: int = 1, bos_token_id: int = 50256, eos_token_id: int = 50256, **kwargs) -> None: ...
