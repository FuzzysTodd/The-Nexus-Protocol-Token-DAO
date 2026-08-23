from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete

logger: Incomplete
WAV2VEC2_CONFORMER_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

class Wav2Vec2ConformerConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`Wav2Vec2ConformerModel`]. It is used to
    instantiate an Wav2Vec2Conformer model according to the specified arguments, defining the model architecture.
    Instantiating a configuration with the defaults will yield a similar configuration to that of the Wav2Vec2Conformer
    [facebook/wav2vec2-conformer-rel-pos-large](https://huggingface.co/facebook/wav2vec2-conformer-rel-pos-large)
    architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*):
            Vocabulary size of the Wav2Vec2Conformer model. Defines the number of different tokens that can be
            represented by the `inputs_ids` passed when calling [`Wav2Vec2ConformerModel`]. Vocabulary size of the
            model. Defines the different tokens that can be represented by the *inputs_ids* passed to the forward
            method of [`Wav2Vec2ConformerModel`].
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_dropout (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        final_dropout (`float`, *optional*, defaults to 0.1):
            The dropout probability for the final projection layer of [`Wav2Vec2ConformerForCTC`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        feat_extract_norm (`str`, *optional*, defaults to `"group"`):
            The norm to be applied to 1D convolutional layers in feature encoder. One of `"group"` for group
            normalization of only the first 1D convolutional layer or `"layer"` for layer normalization of all 1D
            convolutional layers.
        feat_proj_dropout (`float`, *optional*, defaults to 0.0):
            The dropout probability for output of the feature encoder.
        feat_extract_activation (`str, `optional`, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the 1D convolutional layers of the feature
            extractor. If string, `"gelu"`, `"relu"`, `"selu"` and `"gelu_new"` are supported.
        feat_quantizer_dropout (`float`, *optional*, defaults to 0.0):
            The dropout probabilitiy for quantized feature encoder states.
        conv_dim (`Tuple[int]` or `List[int]`, *optional*, defaults to `(512, 512, 512, 512, 512, 512, 512)`):
            A tuple of integers defining the number of input and output channels of each 1D convolutional layer in the
            feature encoder. The length of *conv_dim* defines the number of 1D convolutional layers.
        conv_stride (`Tuple[int]` or `List[int]`, *optional*, defaults to `(5, 2, 2, 2, 2, 2, 2)`):
            A tuple of integers defining the stride of each 1D convolutional layer in the feature encoder. The length
            of *conv_stride* defines the number of convolutional layers and has to match the length of *conv_dim*.
        conv_kernel (`Tuple[int]` or `List[int]`, *optional*, defaults to `(10, 3, 3, 3, 3, 3, 3)`):
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
        num_codevectors_per_group (`int`, *optional*, defaults to 320):
            Number of entries in each quantization codebook (group).
        num_codevector_groups (`int`, *optional*, defaults to 2):
            Number of codevector groups for product codevector quantization.
        contrastive_logits_temperature (`float`, *optional*, defaults to 0.1):
            The temperature *kappa* in the contrastive loss.
        feat_quantizer_dropout (`float`, *optional*, defaults to 0.0):
            The dropout probabilitiy for the output of the feature encoder that\'s used by the quantizer.
        num_negatives (`int`, *optional*, defaults to 100):
            Number of negative samples for the contrastive loss.
        codevector_dim (`int`, *optional*, defaults to 256):
            Dimensionality of the quantized feature vectors.
        proj_codevector_dim (`int`, *optional*, defaults to 256):
            Dimensionality of the final projection of both the quantized and the transformer features.
        diversity_loss_weight (`int`, *optional*, defaults to 0.1):
            The weight of the codebook diversity loss component.
        ctc_loss_reduction (`str`, *optional*, defaults to `"sum"`):
            Specifies the reduction to apply to the output of `torch.nn.CTCLoss`. Only relevant when training an
            instance of [`Wav2Vec2ConformerForCTC`].
        ctc_zero_infinity (`bool`, *optional*, defaults to `False`):
            Whether to zero infinite losses and the associated gradients of `torch.nn.CTCLoss`. Infinite losses mainly
            occur when the inputs are too short to be aligned to the targets. Only relevant when training an instance
            of [`Wav2Vec2ConformerForCTC`].
        use_weighted_layer_sum (`bool`, *optional*, defaults to `False`):
            Whether to use a weighted average of layer outputs with learned weights. Only relevant when using an
            instance of [`Wav2Vec2ConformerForSequenceClassification`].
        classifier_proj_size (`int`, *optional*, defaults to 256):
            Dimensionality of the projection before token mean-pooling for classification.
        tdnn_dim (`Tuple[int]` or `List[int]`, *optional*, defaults to `(512, 512, 512, 512, 1500)`):
            A tuple of integers defining the number of output channels of each 1D convolutional layer in the *TDNN*
            module of the *XVector* model. The length of *tdnn_dim* defines the number of *TDNN* layers.
        tdnn_kernel (`Tuple[int]` or `List[int]`, *optional*, defaults to `(5, 3, 3, 1, 1)`):
            A tuple of integers defining the kernel size of each 1D convolutional layer in the *TDNN* module of the
            *XVector* model. The length of *tdnn_kernel* has to match the length of *tdnn_dim*.
        tdnn_dilation (`Tuple[int]` or `List[int]`, *optional*, defaults to `(1, 2, 3, 1, 1)`):
            A tuple of integers defining the dilation factor of each 1D convolutional layer in *TDNN* module of the
            *XVector* model. The length of *tdnn_dilation* has to match the length of *tdnn_dim*.
        xvector_output_dim (`int`, *optional*, defaults to 512):
            Dimensionality of the *XVector* embedding vectors.
        add_adapter (`bool`, *optional*, defaults to `False`):
            Whether a convolutional network should be stacked on top of the Wav2Vec2Conformer Encoder. Can be very
            useful for warm-starting Wav2Vec2Conformer for SpeechEncoderDecoder models.
        adapter_kernel_size (`int`, *optional*, defaults to 3):
            Kernel size of the convolutional layers in the adapter network. Only relevant if `add_adapter is True`.
        adapter_stride (`int`, *optional*, defaults to 2):
            Stride of the convolutional layers in the adapter network. Only relevant if `add_adapter is True`.
        num_adapter_layers (`int`, *optional*, defaults to 3):
            Number of convolutional layers that should be used in the adapter network. Only relevant if `add_adapter is
            True`.
        output_hidden_size (`int`, *optional*):
            Dimensionality of the encoder output layer. If not defined, this defaults to *hidden-size*. Only relevant
            if `add_adapter is True`.
        position_embeddings_type (`str`, *optional*, defaults to `"relative"`):
            Can be specified to `relative` or `rotary` for relative or rotary position embeddings respectively. If left
            `None` no relative position embedding is applied.
        rotary_embedding_base (`int`, *optional*, defaults to 10000):
            If `"rotary"` position embeddings are used, defines the size of the embedding base.
        max_source_positions (`int`, *optional*, defaults to 5000):
            if `"relative"` position embeddings are used, defines the maximum source input positions.
        conv_depthwise_kernel_size (`int`, defaults to 31):
            Kernel size of convolutional depthwise 1D layer in Conformer blocks.
        conformer_conv_dropout (`float`, defaults to 0.1):
            The dropout probability for all convolutional layers in Conformer blocks.

    Example:

    ```python
    >>> from transformers import Wav2Vec2ConformerConfig, Wav2Vec2ConformerModel

    >>> # Initializing a Wav2Vec2Conformer facebook/wav2vec2-conformer-rel-pos-large style configuration
    >>> configuration = Wav2Vec2ConformerConfig()

    >>> # Initializing a model (with random weights) from the facebook/wav2vec2-conformer-rel-pos-large style configuration
    >>> model = Wav2Vec2ConformerModel(configuration)

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
    hidden_act: Incomplete
    num_attention_heads: Incomplete
    hidden_dropout: Incomplete
    attention_dropout: Incomplete
    activation_dropout: Incomplete
    feat_proj_dropout: Incomplete
    final_dropout: Incomplete
    layerdrop: Incomplete
    layer_norm_eps: Incomplete
    initializer_range: Incomplete
    vocab_size: Incomplete
    use_weighted_layer_sum: Incomplete
    max_source_positions: Incomplete
    position_embeddings_type: Incomplete
    rotary_embedding_base: Incomplete
    conv_depthwise_kernel_size: Incomplete
    conformer_conv_dropout: Incomplete
    apply_spec_augment: Incomplete
    mask_time_prob: Incomplete
    mask_time_length: Incomplete
    mask_time_min_masks: Incomplete
    mask_feature_prob: Incomplete
    mask_feature_length: Incomplete
    mask_feature_min_masks: Incomplete
    num_codevectors_per_group: Incomplete
    num_codevector_groups: Incomplete
    contrastive_logits_temperature: Incomplete
    feat_quantizer_dropout: Incomplete
    num_negatives: Incomplete
    codevector_dim: Incomplete
    proj_codevector_dim: Incomplete
    diversity_loss_weight: Incomplete
    ctc_loss_reduction: Incomplete
    ctc_zero_infinity: Incomplete
    add_adapter: Incomplete
    adapter_kernel_size: Incomplete
    adapter_stride: Incomplete
    num_adapter_layers: Incomplete
    output_hidden_size: Incomplete
    classifier_proj_size: Incomplete
    tdnn_dim: Incomplete
    tdnn_kernel: Incomplete
    tdnn_dilation: Incomplete
    xvector_output_dim: Incomplete
    def __init__(self, vocab_size: Incomplete | None = None, hidden_size: int = 768, num_hidden_layers: int = 12, num_attention_heads: int = 12, intermediate_size: int = 3072, hidden_act: str = 'gelu', hidden_dropout: float = 0.1, activation_dropout: float = 0.1, attention_dropout: float = 0.1, feat_proj_dropout: float = 0.0, feat_quantizer_dropout: float = 0.0, final_dropout: float = 0.1, layerdrop: float = 0.1, initializer_range: float = 0.02, layer_norm_eps: float = 1e-05, feat_extract_norm: str = 'group', feat_extract_activation: str = 'gelu', conv_dim=(512, 512, 512, 512, 512, 512, 512), conv_stride=(5, 2, 2, 2, 2, 2, 2), conv_kernel=(10, 3, 3, 3, 3, 2, 2), conv_bias: bool = False, num_conv_pos_embeddings: int = 128, num_conv_pos_embedding_groups: int = 16, apply_spec_augment: bool = True, mask_time_prob: float = 0.05, mask_time_length: int = 10, mask_time_min_masks: int = 2, mask_feature_prob: float = 0.0, mask_feature_length: int = 10, mask_feature_min_masks: int = 0, num_codevectors_per_group: int = 320, num_codevector_groups: int = 2, contrastive_logits_temperature: float = 0.1, num_negatives: int = 100, codevector_dim: int = 256, proj_codevector_dim: int = 256, diversity_loss_weight: float = 0.1, ctc_loss_reduction: str = 'sum', ctc_zero_infinity: bool = False, use_weighted_layer_sum: bool = False, classifier_proj_size: int = 256, tdnn_dim=(512, 512, 512, 512, 1500), tdnn_kernel=(5, 3, 3, 1, 1), tdnn_dilation=(1, 2, 3, 1, 1), xvector_output_dim: int = 512, pad_token_id: int = 0, bos_token_id: int = 1, eos_token_id: int = 2, add_adapter: bool = False, adapter_kernel_size: int = 3, adapter_stride: int = 2, num_adapter_layers: int = 3, output_hidden_size: Incomplete | None = None, position_embeddings_type: str = 'relative', rotary_embedding_base: int = 10000, max_source_positions: int = 5000, conv_depthwise_kernel_size: int = 31, conformer_conv_dropout: float = 0.1, **kwargs) -> None: ...
    @property
    def inputs_to_logits_ratio(self): ...
