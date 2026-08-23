from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
SEW_D_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class SEWDConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`SEWDModel`]. It is used to instantiate a SEW-D
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the SEW-D
    [asapp/sew-d-tiny-100k](https://huggingface.co/asapp/sew-d-tiny-100k) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 32):
            Vocabulary size of the SEW-D model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`SEWD`].
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        squeeze_factor (`int`, *optional*, defaults to 2):
            Sequence length downsampling factor after the encoder and upsampling factor after the transformer.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        position_buckets (`int`, *optional*, defaults to 256):
            The maximum size of relative position embeddings.
        share_att_key (`bool`, *optional*, defaults to `True`):
            Whether to share attention key with c2p and p2c.
        relative_attention (`bool`, *optional*, defaults to `True`):
            Whether to use relative position encoding.
        pos_att_type (`Tuple[str]`, *optional*, defaults to `("p2c", "c2p")`):
            The type of relative position attention, it can be a combination of `("p2c", "c2p")`, e.g. `("p2c")`,
            `("p2c", "c2p")`, `("p2c", "c2p")`.
        norm_rel_ebd (`str`, *optional*, defaults to `"layer_norm"`):
            Whether to use layer norm in relative embedding (`"layer_norm"` if yes)
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu_python"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"`, `"gelu_python"` and `"gelu_new"` are supported.
        hidden_dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_dropout (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        final_dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for the final projection layer of [`SEWDForCTC`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-7):
            The epsilon used by the layer normalization layers in the transformer encoder.
        feature_layer_norm_eps (`float`, *optional*, defaults to 1e-5):
            The epsilon used by the layer normalization after the feature encoder.
        feat_extract_norm (`str`, *optional*, defaults to `"group"`):
            The norm to be applied to 1D convolutional layers in feature encoder. One of `"group"` for group
            normalization of only the first 1D convolutional layer or `"layer"` for layer normalization of all 1D
            convolutional layers.
        feat_proj_dropout (`float`, *optional*, defaults to 0.0):
            The dropout probability for output of the feature encoder.
        feat_extract_activation (`str, `optional`, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the 1D convolutional layers of the feature
            extractor. If string, `"gelu"`, `"relu"`, `"selu"` and `"gelu_new"` are supported.
        conv_dim (`Tuple[int]` or `List[int]`, *optional*, defaults to `(64, 128, 128, 128, 128, 256, 256, 256, 256, 512, 512, 512, 512)`):
            A tuple of integers defining the number of input and output channels of each 1D convolutional layer in the
            feature encoder. The length of *conv_dim* defines the number of 1D convolutional layers.
        conv_stride (`Tuple[int]` or `List[int]`, *optional*, defaults to `(5, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1)`):
            A tuple of integers defining the stride of each 1D convolutional layer in the feature encoder. The length
            of *conv_stride* defines the number of convolutional layers and has to match the length of *conv_dim*.
        conv_kernel (`Tuple[int]` or `List[int]`, *optional*, defaults to `(10, 3, 1, 3, 1, 3, 1, 3, 1, 2, 1, 2, 1)`):
            A tuple of integers defining the kernel size of each 1D convolutional layer in the feature encoder. The
            length of *conv_kernel* defines the number of convolutional layers and has to match the length of
            *conv_dim*.
        conv_bias (`bool`, *optional*, defaults to `False`):
            Whether the 1D convolutional layers have a bias.
        num_conv_pos_embeddings (`int`, *optional*, defaults to 128):
            Number of convolutional positional embeddings. Defines the kernel size of 1D convolutional positional
            embeddings layer.
        num_conv_pos_embedding_groups (`int`, *optional*, defaults to 16):
            Number of groups of 1D convolutional positional embeddings layer.
        apply_spec_augment (`bool`, *optional*, defaults to `True`):
            Whether to apply *SpecAugment* data augmentation to the outputs of the feature encoder. For reference see
            [SpecAugment: A Simple Data Augmentation Method for Automatic Speech
            Recognition](https://arxiv.org/abs/1904.08779).
        mask_time_prob (`float`, *optional*, defaults to 0.05):
            Percentage (between 0 and 1) of all feature vectors along the time axis which will be masked. The masking
            procecure generates \'\'mask_time_prob*len(time_axis)/mask_time_length\'\' independent masks over the axis. If
            reasoning from the propability of each feature vector to be chosen as the start of the vector span to be
            masked, *mask_time_prob* should be `prob_vector_start*mask_time_length`. Note that overlap may decrease the
            actual percentage of masked vectors. This is only relevant if `apply_spec_augment is True`.
        mask_time_length (`int`, *optional*, defaults to 10):
            Length of vector span along the time axis.
        mask_time_min_masks (`int`, *optional*, defaults to 2),:
            The minimum number of masks of length `mask_feature_length` generated along the time axis, each time step,
            irrespectively of `mask_feature_prob`. Only relevant if \'\'mask_time_prob*len(time_axis)/mask_time_length <
            mask_time_min_masks\'\'
        mask_feature_prob (`float`, *optional*, defaults to 0.0):
            Percentage (between 0 and 1) of all feature vectors along the feature axis which will be masked. The
            masking procecure generates \'\'mask_feature_prob*len(feature_axis)/mask_time_length\'\' independent masks over
            the axis. If reasoning from the propability of each feature vector to be chosen as the start of the vector
            span to be masked, *mask_feature_prob* should be `prob_vector_start*mask_feature_length`. Note that overlap
            may decrease the actual percentage of masked vectors. This is only relevant if `apply_spec_augment is
            True`.
        mask_feature_length (`int`, *optional*, defaults to 10):
            Length of vector span along the feature axis.
        mask_feature_min_masks (`int`, *optional*, defaults to 0),:
            The minimum number of masks of length `mask_feature_length` generated along the feature axis, each time
            step, irrespectively of `mask_feature_prob`. Only relevant if
            \'\'mask_feature_prob*len(feature_axis)/mask_feature_length < mask_feature_min_masks\'\'
        diversity_loss_weight (`int`, *optional*, defaults to 0.1):
            The weight of the codebook diversity loss component.
        ctc_loss_reduction (`str`, *optional*, defaults to `"sum"`):
            Specifies the reduction to apply to the output of `torch.nn.CTCLoss`. Only relevant when training an
            instance of [`SEWDForCTC`].
        ctc_zero_infinity (`bool`, *optional*, defaults to `False`):
            Whether to zero infinite losses and the associated gradients of `torch.nn.CTCLoss`. Infinite losses mainly
            occur when the inputs are too short to be aligned to the targets. Only relevant when training an instance
            of [`SEWDForCTC`].
        use_weighted_layer_sum (`bool`, *optional*, defaults to `False`):
            Whether to use a weighted average of layer outputs with learned weights. Only relevant when using an
            instance of [`Wav2Vec2ForSequenceClassification`].
        classifier_proj_size (`int`, *optional*, defaults to 256):
            Dimensionality of the projection before token mean-pooling for classification.

    Example:

    ```python
    >>> from transformers import SEWDConfig, SEWDModel

    >>> # Initializing a SEW-D asapp/sew-d-tiny-100k style configuration
    >>> configuration = SEWDConfig()

    >>> # Initializing a model (with random weights) from the asapp/sew-d-tiny-100k style configuration
    >>> model = SEWDModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```'''
    model_type: str
    hidden_size: Incomplete
    feat_extract_norm: Incomplete
    feat_extract_activation: Incomplete
    conv_dim: Incomplete
    conv_stride: Incomplete
    conv_kernel: Incomplete
    conv_bias: Incomplete
    num_conv_pos_embeddings: Incomplete
    num_conv_pos_embedding_groups: Incomplete
    num_feat_extract_layers: Incomplete
    num_hidden_layers: Incomplete
    intermediate_size: Incomplete
    squeeze_factor: Incomplete
    max_position_embeddings: Incomplete
    position_buckets: Incomplete
    share_att_key: Incomplete
    relative_attention: Incomplete
    norm_rel_ebd: Incomplete
    pos_att_type: Incomplete
    hidden_act: Incomplete
    num_attention_heads: Incomplete
    hidden_dropout: Incomplete
    attention_dropout: Incomplete
    activation_dropout: Incomplete
    feat_proj_dropout: Incomplete
    final_dropout: Incomplete
    layerdrop: Incomplete
    layer_norm_eps: Incomplete
    feature_layer_norm_eps: Incomplete
    initializer_range: Incomplete
    vocab_size: Incomplete
    apply_spec_augment: Incomplete
    mask_time_prob: Incomplete
    mask_time_length: Incomplete
    mask_time_min_masks: Incomplete
    mask_feature_prob: Incomplete
    mask_feature_length: Incomplete
    mask_feature_min_masks: Incomplete
    ctc_loss_reduction: Incomplete
    ctc_zero_infinity: Incomplete
    use_weighted_layer_sum: Incomplete
    classifier_proj_size: Incomplete
    def __init__(self, vocab_size: int = 32, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, squeeze_factor: int = 2, max_position_embeddings: int = 512, position_buckets: int = 256, share_att_key: bool = True, relative_attention: bool = True, pos_att_type=('p2c', 'c2p'), norm_rel_ebd: str = 'layer_norm', hidden_act: str = 'gelu_python', hidden_dropout: float = 0.1, activation_dropout: float = 0.1, attention_dropout: float = 0.1, feat_proj_dropout: float = 0.0, final_dropout: float = 0.1, layerdrop: float = 0.1, initializer_range: float = 0.02, layer_norm_eps: float = 1e-07, feature_layer_norm_eps: float = 1e-05, feat_extract_norm: str = 'group', feat_extract_activation: str = 'gelu', conv_dim=(64, 128, 128, 128, 128, 256, 256, 256, 256, 512, 512, 512, 512), conv_stride=(5, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1), conv_kernel=(10, 3, 1, 3, 1, 3, 1, 3, 1, 2, 1, 2, 1), conv_bias: bool = False, num_conv_pos_embeddings: int = 128, num_conv_pos_embedding_groups: int = 16, apply_spec_augment: bool = True, mask_time_prob: float = 0.05, mask_time_length: int = 10, mask_time_min_masks: int = 2, mask_feature_prob: float = 0.0, mask_feature_length: int = 10, mask_feature_min_masks: int = 0, ctc_loss_reduction: str = 'mean', ctc_zero_infinity: bool = False, use_weighted_layer_sum: bool = False, classifier_proj_size: int = 256, pad_token_id: int = 0, bos_token_id: int = 1, eos_token_id: int = 2, **kwargs) -> None: ...
    @property
    def inputs_to_logits_ratio(self): ...
