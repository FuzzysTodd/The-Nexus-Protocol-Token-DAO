from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
CTRL_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class CTRLConfig(PretrainedConfig):
    """
    This is the configuration class to store the configuration of a [`CTRLModel`] or a [`TFCTRLModel`]. It is used to
    instantiate a CTRL model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the
    [ctrl](https://huggingface.co/ctrl) architecture from SalesForce.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        vocab_size (`int`, *optional*, defaults to 246534):
            Vocabulary size of the CTRL model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`CTRLModel`] or [`TFCTRLModel`].
        n_positions (`int`, *optional*, defaults to 256):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        n_embd (`int`, *optional*, defaults to 1280):
            Dimensionality of the embeddings and hidden states.
        dff (`int`, *optional*, defaults to 8192):
            Dimensionality of the inner dimension of the feed forward networks (FFN).
        n_layer (`int`, *optional*, defaults to 48):
            Number of hidden layers in the Transformer encoder.
        n_head (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer encoder.
        resid_pdrop (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        embd_pdrop (`int`, *optional*, defaults to 0.1):
            The dropout ratio for the embeddings.
        layer_norm_epsilon (`float`, *optional*, defaults to 1e-6):
            The epsilon to use in the layer normalization layers
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models).


    Examples:

    ```python
    >>> from transformers import CTRLConfig, CTRLModel

    >>> # Initializing a CTRL configuration
    >>> configuration = CTRLConfig()

    >>> # Initializing a model (with random weights) from the configuration
    >>> model = CTRLModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type: str
    keys_to_ignore_at_inference: Incomplete
    attribute_map: Incomplete
    vocab_size: Incomplete
    n_positions: Incomplete
    n_embd: Incomplete
    n_layer: Incomplete
    n_head: Incomplete
    dff: Incomplete
    resid_pdrop: Incomplete
    embd_pdrop: Incomplete
    layer_norm_epsilon: Incomplete
    initializer_range: Incomplete
    summary_type: Incomplete
    summary_use_proj: Incomplete
    summary_activation: Incomplete
    summary_first_dropout: Incomplete
    summary_proj_to_labels: Incomplete
    use_cache: Incomplete
    def __init__(self, vocab_size: int = 246534, n_positions: int = 256, n_embd: int = 1280, dff: int = 8192, n_layer: int = 48, n_head: int = 16, resid_pdrop: float = 0.1, embd_pdrop: float = 0.1, layer_norm_epsilon: float = 1e-06, initializer_range: float = 0.02, summary_type: str = 'cls_index', summary_use_proj: bool = True, summary_activation: Incomplete | None = None, summary_proj_to_labels: bool = True, summary_first_dropout: float = 0.1, use_cache: bool = True, **kwargs) -> None: ...
