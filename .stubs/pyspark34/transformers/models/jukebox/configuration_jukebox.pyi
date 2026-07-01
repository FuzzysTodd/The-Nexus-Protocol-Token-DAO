import os
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import logging as logging
from _typeshed import Incomplete
from typing import List, Union

logger: Incomplete
JUKEBOX_PRETRAINED_CONFIG_ARCHIVE_MAP: Incomplete

def full_dense_attention(layer): ...
def raw_column_previous_row_attention(layer): ...
def large_separated_enc_dec_w_lyrics(layer): ...
def enc_dec_with_lyrics(layer): ...

ATTENTION_PATTERNS: Incomplete

class JukeboxPriorConfig(PretrainedConfig):
    '''
        This is the configuration class to store the configuration of a [`JukeboxPrior`]. It is used to instantiate a
        `JukeboxPrior` according to the specified arguments, defining the model architecture. Instantiating a
        configuration with the defaults will yield a similar configuration to that of the top level prior from the
        [openai/jukebox-1b-lyrics](https://huggingface.co/openai/jukebox
    -1b-lyrics) architecture.

        Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
        documentation from [`PretrainedConfig`] for more information.



    Args:
        act_fn (`str`, *optional*, defaults to `"quick_gelu"`):
            Activation function.
        alignment_head (`int`, *optional*, defaults to 2):
            Head that is responsible of the alignment between lyrics and music. Only used to compute the lyric to audio
            alignment
        alignment_layer (`int`, *optional*, defaults to 68):
            Index of the layer that is responsible of the alignment between lyrics and music. Only used to compute the
            lyric to audio alignment
        attention_multiplier (`float`, *optional*, defaults to 0.25):
            Multiplier coefficient used to define the hidden dimension of the attention layers. 0.25 means that
            0.25*width of the model will be used.
        attention_pattern (`str`, *optional*, defaults to `"enc_dec_with_lyrics"`):
            Which attention pattern to use for the decoder/
        attn_dropout (`int`, *optional*, defaults to 0):
            Dropout probability for the post-attention layer dropout in the decoder.
        attn_res_scale (`bool`, *optional*, defaults to `False`):
            Whether or not to scale the residuals in the attention conditioner block.
        blocks (`int`, *optional*, defaults to 64):
            Number of blocks used in the `block_attn`. A sequence of length seq_len is factored as `[blocks, seq_len //
            blocks]` in the `JukeboxAttention` layer.
        conv_res_scale (`int`, *optional*):
            Whether or not to scale the residuals in the conditioner block. Since the top level prior does not have a
            conditioner, the default value is to None and should not be modified.
        num_layers (`int`, *optional*, defaults to 72):
            Number of layers of the transformer architecture.
        emb_dropout (`int`, *optional*, defaults to 0):
            Embedding dropout used in the lyric decoder.
        encoder_config (`JukeboxPriorConfig`, *optional*) :
            Configuration of the encoder which models the prior on the lyrics.
        encoder_loss_fraction (`float`, *optional*, defaults to 0.4):
            Multiplication factor used in front of the lyric encoder loss.
        hidden_size (`int`, *optional*, defaults to 2048):
            Hidden dimension of the attention layers.
        init_scale (`float`, *optional*, defaults to 0.2):
            Initialization scales for the prior modules.
        is_encoder_decoder (`bool`, *optional*, defaults to `True`):
            Whether or not the prior is an encoder-decoder model. In case it is not, and `nb_relevant_lyric_tokens` is
            greater than 0, the `encoder` args should be specified for the lyric encoding.
        mask (`bool`, *optional*, defaults to `False`):
            Whether or not to mask the previous positions in the attention.
        max_duration (`int`, *optional*, defaults to 600):
            Maximum supported duration of the generated song in seconds.
        max_nb_genres (`int`, *optional*, defaults to 1):
            Maximum number of genres that can be used to condition the model.
        merged_decoder (`bool`, *optional*, defaults to `True`):
            Whether or not the decoder and the encoder inputs are merged. This is used for the separated
            encoder-decoder architecture
        metadata_conditioning (`bool`, *optional*, defaults to `True)`:
            Whether or not to condition on the artist and genre metadata.
        metadata_dims (`List[int]`, *optional*, defaults to `[604, 7898]`):
            Number of genres and the number of artists that were used to train the embedding layers of the prior
            models.
        min_duration (`int`, *optional*, defaults to 0):
            Minimum duration of the generated audio on which the model was trained.
        mlp_multiplier (`float`, *optional*, defaults to 1.0):
            Multiplier coefficient used to define the hidden dimension of the MLP layers. 0.25 means that 0.25*width of
            the model will be used.
        music_vocab_size (`int`, *optional*, defaults to 2048):
            Number of different music tokens. Should be similar to the `JukeboxVQVAEConfig.nb_discrete_codes`.
        n_ctx (`int`, *optional*, defaults to 6144):
            Number of context tokens for each prior. The context tokens are the music tokens that are attended to when
            generating music tokens.
        n_heads (`int`, *optional*, defaults to 2):
                Number of attention heads.
        nb_relevant_lyric_tokens (`int`, *optional*, defaults to 384):
            Number of lyric tokens that are used when sampling a single window of length `n_ctx`
        res_conv_depth (`int`, *optional*, defaults to 3):
            Depth of the `JukeboxDecoderConvBock` used to upsample the previously sampled audio in the
            `JukeboxMusicTokenConditioner`.
        res_conv_width (`int`, *optional*, defaults to 128):
            Width of the `JukeboxDecoderConvBock` used to upsample the previously sampled audio in the
            `JukeboxMusicTokenConditioner`.
        res_convolution_multiplier (`int`, *optional*, defaults to 1):
            Multiplier used to scale the `hidden_dim` of the `JukeboxResConv1DBlock`.
        res_dilation_cycle (`int`, *optional*):
            Dilation cycle used to define the `JukeboxMusicTokenConditioner`. Usually similar to the ones used in the
            corresponding level of the VQVAE. The first prior does not use it as it is not conditioned on upper level
            tokens.
        res_dilation_growth_rate (`int`, *optional*, defaults to 1):
            Dilation grow rate used between each convolutionnal block of the `JukeboxMusicTokenConditioner`
        res_downs_t (`List[int]`, *optional*, defaults to `[3, 2, 2]`):
            Downsampling rates used in the audio conditioning network
        res_strides_t (`List[int]`, *optional*, defaults to `[2, 2, 2]`):
            Striding used in the audio conditioning network
        resid_dropout (`int`, *optional*, defaults to 0):
            Residual dropout used in the attention pattern.
        sampling_rate (`int`, *optional*, defaults to 44100):
            Sampling rate used for training.
        spread (`int`, *optional*):
            Spread used in the `summary_spread_attention` pattern
        timing_dims (`int`, *optional*, defaults to 64):
            Dimension of the timing embedding.
        zero_out (`bool`, *optional*, defaults to `False`):
            Whether or not to zero out convolution weights when initializing.
    '''
    model_type: str
    attribute_map: Incomplete
    act_fn: Incomplete
    alignment_head: Incomplete
    alignment_layer: Incomplete
    attention_multiplier: Incomplete
    attention_pattern: Incomplete
    attn_dropout: Incomplete
    attn_res_scale: Incomplete
    blocks: Incomplete
    conv_res_scale: Incomplete
    num_layers: Incomplete
    emb_dropout: Incomplete
    music_vocab_size: Incomplete
    encoder_config: Incomplete
    encoder_loss_fraction: Incomplete
    init_scale: Incomplete
    is_encoder_decoder: Incomplete
    lyric_vocab_size: Incomplete
    level: Incomplete
    mask: Incomplete
    max_duration: Incomplete
    max_nb_genres: Incomplete
    merged_decoder: Incomplete
    metadata_conditioning: Incomplete
    metadata_dims: Incomplete
    min_duration: Incomplete
    mlp_multiplier: Incomplete
    n_ctx: Incomplete
    n_heads: Incomplete
    nb_relevant_lyric_tokens: Incomplete
    res_conv_depth: Incomplete
    res_conv_width: Incomplete
    res_convolution_multiplier: Incomplete
    res_dilation_cycle: Incomplete
    res_dilation_growth_rate: Incomplete
    res_downs_t: Incomplete
    res_strides_t: Incomplete
    resid_dropout: Incomplete
    sampling_rate: Incomplete
    spread: Incomplete
    timing_dims: Incomplete
    hidden_size: Incomplete
    zero_out: Incomplete
    def __init__(self, act_fn: str = 'quick_gelu', level: int = 0, alignment_head: int = 2, alignment_layer: int = 68, attention_multiplier: float = 0.25, attention_pattern: str = 'enc_dec_with_lyrics', attn_dropout: int = 0, attn_res_scale: bool = False, blocks: int = 64, conv_res_scale: Incomplete | None = None, num_layers: int = 72, emb_dropout: int = 0, encoder_config: Incomplete | None = None, encoder_loss_fraction: float = 0.4, hidden_size: int = 2048, init_scale: float = 0.2, is_encoder_decoder: bool = True, lyric_vocab_size: int = 80, mask: bool = False, max_duration: int = 600, max_nb_genres: int = 1, merged_decoder: bool = True, metadata_conditioning: bool = True, metadata_dims=[604, 7898], min_duration: int = 0, mlp_multiplier: float = 1.0, music_vocab_size: int = 2048, n_ctx: int = 6144, n_heads: int = 2, nb_relevant_lyric_tokens: int = 384, res_conv_depth: int = 3, res_conv_width: int = 128, res_convolution_multiplier: int = 1, res_dilation_cycle: Incomplete | None = None, res_dilation_growth_rate: int = 1, res_downs_t=[3, 2, 2], res_strides_t=[2, 2, 2], resid_dropout: int = 0, sampling_rate: int = 44100, spread: Incomplete | None = None, timing_dims: int = 64, zero_out: bool = False, **kwargs) -> None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], level: int = 0, **kwargs) -> PretrainedConfig: ...
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """

class JukeboxVQVAEConfig(PretrainedConfig):
    '''
    This is the configuration class to store the configuration of a [`JukeboxVQVAE`]. It is used to instantiate a
    `JukeboxVQVAE` according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the VQVAE from
    [openai/jukebox-1b-lyrics](https://huggingface.co/openai/jukebox-1b-lyrics) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        act_fn (`str`, *optional*, defaults to `"relu"`):
            Activation function of the model.
        nb_discrete_codes (`int`, *optional*, defaults to 2048):
            Number of codes of the VQVAE.
        commit (`float`, *optional*, defaults to 0.02):
            Commit loss multiplier.
        conv_input_shape (`int`, *optional*, defaults to 1):
            Number of audio channels.
        conv_res_scale (`bool`, *optional*, defaults to `False`):
            Whether or not to scale the residuals of the `JukeboxResConv1DBlock`.
        embed_dim (`int`, *optional*, defaults to 64):
            Embedding dimension of the codebook vectors.
        hop_fraction (`List[int]`, *optional*, defaults to `[0.125, 0.5, 0.5]`):
            Fraction of non-intersecting window used when continuing the sampling process.
        levels (`int`, *optional*, defaults to 3):
            Number of hierarchical levels that used in the VQVAE.
        lmu (`float`, *optional*, defaults to 0.99):
            Used in the codebook update, exponential moving average coefficient. For more detail refer to Appendix A.1
            of the original [VQVAE paper](https://arxiv.org/pdf/1711.00937v2.pdf)
        multipliers (`List[int]`, *optional*, defaults to `[2, 1, 1]`):
            Depth and width multipliers used for each level. Used on the `res_conv_width` and `res_conv_depth`
        res_conv_depth (`int`, *optional*, defaults to 4):
            Depth of the encoder and decoder block. If no `multipliers` are used, this is the same for each level.
        res_conv_width (`int`, *optional*, defaults to 32):
            Width of the encoder and decoder block. If no `multipliers` are used, this is the same for each level.
        res_convolution_multiplier (`int`, *optional*, defaults to 1):
            Scaling factor of the hidden dimension used in the `JukeboxResConv1DBlock`.
        res_dilation_cycle (`int`, *optional*):
            Dilation cycle value used in the `JukeboxResnet`. If an int is used, each new Conv1 block will have a depth
            reduced by a power of `res_dilation_cycle`.
        res_dilation_growth_rate (`int`, *optional*, defaults to 3):
            Resnet dilation growth rate used in the VQVAE (dilation_growth_rate ** depth)
        res_downs_t (`List[int]`, *optional*, defaults to `[3, 2, 2]`):
            Downsampling rate for each level of the hierarchical VQ-VAE.
        res_strides_t (`List[int]`, *optional*, defaults to `[2, 2, 2]`):
            Stride used for each level of the hierarchical VQ-VAE.
        sample_length (`int`, *optional*, defaults to 1058304):
            Provides the max input shape of the VQVAE. Is used to compute the input shape of each level.
        init_scale (`float`, *optional*, defaults to 0.2):
            Initialization scale.
        zero_out (`bool`, *optional*, defaults to `False`):
            Whether or not to zero out convolution weights when initializing.
    '''
    model_type: str
    hop_fraction: Incomplete
    conv_input_shape: Incomplete
    sample_length: Incomplete
    levels: Incomplete
    embed_dim: Incomplete
    nb_discrete_codes: Incomplete
    res_conv_width: Incomplete
    res_conv_depth: Incomplete
    res_convolution_multiplier: Incomplete
    res_dilation_growth_rate: Incomplete
    res_dilation_cycle: Incomplete
    multipliers: Incomplete
    res_downs_t: Incomplete
    res_strides_t: Incomplete
    lmu: Incomplete
    commit: Incomplete
    conv_res_scale: Incomplete
    act_fn: Incomplete
    init_scale: Incomplete
    zero_out: Incomplete
    def __init__(self, act_fn: str = 'relu', nb_discrete_codes: int = 2048, commit: float = 0.02, conv_input_shape: int = 1, conv_res_scale: bool = False, embed_dim: int = 64, hop_fraction=[0.125, 0.5, 0.5], levels: int = 3, lmu: float = 0.99, multipliers=[2, 1, 1], res_conv_depth: int = 4, res_conv_width: int = 32, res_convolution_multiplier: int = 1, res_dilation_cycle: Incomplete | None = None, res_dilation_growth_rate: int = 3, res_downs_t=[3, 2, 2], res_strides_t=[2, 2, 2], sample_length: int = 1058304, init_scale: float = 0.2, zero_out: bool = False, **kwargs) -> None: ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path: Union[str, os.PathLike], **kwargs) -> PretrainedConfig: ...

class JukeboxConfig(PretrainedConfig):
    """
    This is the configuration class to store the configuration of a [`JukeboxModel`].

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information. Instantiating a configuration with the defaults will
    yield a similar configuration to that of
    [openai/jukebox-1b-lyrics](https://huggingface.co/openai/jukebox-1b-lyrics) architecture.


    The downsampling and stride are used to determine downsampling of the input sequence. For example, downsampling =
    (5,3), and strides = (2, 2) will downsample the audio by 2^5 = 32 to get the first level of codes, and 2**8 = 256
    to get the second level codes. This is mostly true for training the top level prior and the upsamplers.

    Args:
        vqvae_config (`JukeboxVQVAEConfig`, *optional*):
            Configuration for the `JukeboxVQVAE` model.
        prior_config_list (`List[JukeboxPriorConfig]`, *optional*):
            List of the configs for each of the `JukeboxPrior` of the model. The original architecture uses 3 priors.
        nb_priors (`int`, *optional*, defaults to 3):
            Number of prior models that will sequentially sample tokens. Each prior is conditional auto regressive
            (decoder) model, apart from the top prior, which can include a lyric encoder. The available models were
            trained using a top prior and 2 upsampler priors.
        sampling_rate (`int`, *optional*, defaults to 44100):
            Sampling rate of the raw audio.
        timing_dims (`int`, *optional*, defaults to 64):
            Dimensions of the JukeboxRangeEmbedding layer which is equivalent to traditional positional embedding
            layer. The timing embedding layer converts the absolute and relative position in the currently sampled
            audio to a tensor of length `timing_dims` that will be added to the music tokens.
        min_duration (`int`, *optional*, defaults to 0):
            Minimum duration of the audios to generate
        max_duration (`float`, *optional*, defaults to 600.0):
            Maximum duration of the audios to generate
        max_nb_genres (`int`, *optional*, defaults to 5):
            Maximum number of genres that can be used to condition a single sample.
        metadata_conditioning (`bool`, *optional*, defaults to `True`):
            Whether or not to use metadata conditioning, corresponding to the artist, the genre and the min/maximum
            duration.
        init_std (`float`, *optional*, defaults to 0.2):
            Standard deviation used to initial the model.

    Example:

    ```python
    >>> from transformers import JukeboxModel, JukeboxConfig

    >>> # Initializing a Jukebox configuration
    >>> configuration = JukeboxConfig()

    >>> # Initializing a model from the configuration
    >>> model = JukeboxModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```
    """
    model_type: str
    is_composition: bool
    vqvae_config: Incomplete
    prior_configs: Incomplete
    hop_fraction: Incomplete
    init_std: Incomplete
    nb_priors: Incomplete
    max_nb_genres: Incomplete
    sampling_rate: Incomplete
    timing_dims: Incomplete
    min_duration: Incomplete
    max_duration: Incomplete
    metadata_conditioning: Incomplete
    def __init__(self, vqvae_config: Incomplete | None = None, prior_config_list: Incomplete | None = None, nb_priors: int = 3, sampling_rate: int = 44100, timing_dims: int = 64, min_duration: int = 0, max_duration: float = 600.0, max_nb_genres: int = 5, metadata_conditioning: bool = True, init_std: float = 0.2, **kwargs) -> None: ...
    @classmethod
    def from_configs(cls, prior_configs: List[JukeboxPriorConfig], vqvae_config: JukeboxVQVAEConfig, **kwargs):
        """
        Instantiate a [`JukeboxConfig`] (or a derived class) from clip text model configuration and clip vision model
        configuration.

        Returns:
            [`JukeboxConfig`]: An instance of a configuration object
        """
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
