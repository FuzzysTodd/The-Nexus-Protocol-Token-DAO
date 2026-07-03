import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import add_start_docstrings as add_start_docstrings, logging as logging
from ...utils.logging import tqdm as tqdm
from .configuration_jukebox import ATTENTION_PATTERNS as ATTENTION_PATTERNS, JukeboxConfig as JukeboxConfig, JukeboxPriorConfig as JukeboxPriorConfig, JukeboxVQVAEConfig as JukeboxVQVAEConfig
from _typeshed import Incomplete
from torch import nn
from torch.nn import LayerNorm as FusedLayerNorm
from typing import List, Optional, Tuple

logger: Incomplete
JUKEBOX_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def filter_logits(logits, top_k: int = 0, top_p: float = 0.0, filter_value=...):
    """
    Filter a distribution of logits using top-k and/or nucleus (top-p) filtering

    Args:
        logits (`torch.Tensor`):
            logits distribution shape (vocabulary size)
        top_k (`int`, *optional*, defaults to 0):
            When `top_k >0` keep only top key tokens with highest probability (top-k filtering).
        top_p (`int`, *optional*, defaults to 0):
            When `top_p>0.0` keep the top tokens with cumulative probability >= `top_p` (nucleus filtering).
    """
def get_relevant_lyric_tokens(full_tokens, max_n_lyric_tokens, total_length, offset, duration):
    """
    Extract only the relevant tokens based on the character position. A total of `max_n_lyric_tokens` tokens will be
    returned. If the provided token sequence is smaller, it will be padded, otherwise, only characters ranging from the
    midpoint - `max_n_lyric_tokens//2` to the midpoint + `max_n_lyric_tokens//2` will be returned. This *focuses* on
    the most relevant tokens (in time) for the sequence.

    Args:
        full_tokens (`List[int]`):
            List containing the token ids of the entire lyrics.
        total_length (`int`):
            Total expected length of the music (not all of it is generated, see duration), in samples.
        offset (`int`):
            Starting sample in the music. If the offset is greater than 0, the lyrics will be shifted take that into
            account
        duration (`int`):
            Expected duration of the generated music, in samples. The duration has to be smaller than the total length,
            which represent the overall length of the signal,
    """
def get_starts(total_length, n_ctx, hop_length): ...
def get_alignment(music_tokens, labels, prior, config): ...
def save_temp_audio(fname, lvl, metas, aud) -> None: ...
def get_mask(mask, query_length, key_value_length, blocks, spread, device, sample, sample_t): ...

class JukeboxConv1D(nn.Module):
    input_width: Incomplete
    output_width: Incomplete
    weight: Incomplete
    bias: Incomplete
    def __init__(self, input_width, output_width) -> None: ...
    def forward(self, hidden_states): ...

class JukeboxResConv1DBlock(nn.Module):
    res_scale: Incomplete
    activation: Incomplete
    conv1d_1: Incomplete
    conv1d_2: Incomplete
    def __init__(self, config, conv_width, depth: int = 1, res_scale: float = 1.0) -> None: ...
    def forward(self, hidden_states): ...

class JukeboxResnet1D(nn.Module):
    dilation_cycle: Incomplete
    resnet_block: Incomplete
    def __init__(self, config, conv_width, n_depth, reverse_dilation: bool = False) -> None: ...
    def forward(self, hidden_states): ...

class JukeboxEncoderConvBlock(nn.Module):
    proj_out: Incomplete
    downsample_block: Incomplete
    def __init__(self, config, embed_dim, hidden_dim, depth, down_t, stride_t) -> None: ...
    def forward(self, hidden_states): ...

class JukeboxEncoder(nn.Module):
    levels: Incomplete
    level_blocks: Incomplete
    def __init__(self, config, width, depth, levels, downs_t, strides_t) -> None: ...
    def forward(self, hidden_states): ...

class JukeboxDecoderConvBock(nn.Module):
    embed_dim: Incomplete
    hidden_dim: Incomplete
    proj_in: Incomplete
    upsample_block: Incomplete
    def __init__(self, config, embed_dim, hidden_dim, depth, down_t, stride_t, reverse_dilation: bool = True) -> None: ...
    def forward(self, hidden_states): ...

class JukeboxDecoder(nn.Module):
    levels: Incomplete
    level_blocks: Incomplete
    out: Incomplete
    def __init__(self, config, hidden_dim, depth, levels, downs_t, strides_t) -> None: ...
    def forward(self, hidden_states, all_levels: bool = True): ...

class JukeboxBottleneckBlock(nn.Module):
    nb_discrete_codes: Incomplete
    codebook_width: Incomplete
    mu: Incomplete
    threshold: float
    init: bool
    codebook_sum: Incomplete
    codebook_elem: Incomplete
    def __init__(self, config: JukeboxVQVAEConfig) -> None: ...
    codebook: Incomplete
    def init_codebook(self, hidden_states) -> None: ...
    def update_codebook(self, hidden_states, latent_states): ...
    def preprocess(self, hidden_states): ...
    def postprocess(self, latent_states, dequantised_states, x_shape): ...
    def quantise(self, latent_states): ...
    def dequantise(self, music_tokens): ...
    def encode(self, latent_states): ...
    def decode(self, music_tokens): ...
    def forward(self, hidden_states, update_codebook: bool = True): ...

class JukeboxBottleneck(nn.Module):
    levels: Incomplete
    level_blocks: Incomplete
    def __init__(self, config, levels) -> None: ...
    def encode(self, raw_audio): ...
    def decode(self, music_tokens, start_level: int = 0, end_level: Incomplete | None = None): ...
    def forward(self, input_audio): ...

JUKEBOX_START_DOCSTRING: str

class JukeboxVQVAE(PreTrainedModel):
    config_class = JukeboxVQVAEConfig
    base_model_prefix: str
    nb_discrete_codes: Incomplete
    commit: Incomplete
    sample_length: Incomplete
    downsamples: Incomplete
    hop_lengths: Incomplete
    levels: Incomplete
    music_tokens_shapes: Incomplete
    multipliers: Incomplete
    encoders: Incomplete
    decoders: Incomplete
    bottleneck: Incomplete
    def __init__(self, config: JukeboxVQVAEConfig) -> None: ...
    def decode(self, music_tokens, start_level: int = 0, end_level: Incomplete | None = None, bs_chunks: int = 1) -> torch.Tensor:
        """
        Transforms the input `music_tokens` to their `raw_audio` representation.

        Args:
            music_tokens (`torch.LongTensor`):
                Tensor of music tokens which will be decoded to raw audio by using the codebook. Each music token
                should be an index to a corresponding `code` vector in the codebook.
            start_level (`int`, *optional*):
                Level at which the decoding process will start. Default to 0.
            end_level (`int`, *optional*):
                Level at which the decoding process will start. Default to None.
            bs_chunks (int, *optional*):
                Number of chunks to process at the same time.
        """
    def encode(self, input_audio, start_level: int = 0, end_level: Incomplete | None = None, bs_chunks: int = 1):
        """
        Transforms the `input_audio` to a discrete representation made out of `music_tokens`.

        Args:
            input_audio (`torch.Tensor`):
                Raw audio which will be encoded to its discrete representation using the codebook. The closest `code`
                form the codebook will be computed for each sequence of samples.
            start_level (`int`, *optional*, defaults to 0):
                Level at which the encoding process will start. Default to 0.
            end_level (`int`, *optional*):
                Level at which the encoding process will start. Default to None.
            bs_chunks (int, *optional*, defaults to 1):
                Number of chunks of raw audio to process at the same time.
        """
    def sample(self, n_samples): ...
    def forward(self, raw_audio: torch.FloatTensor) -> Tuple[torch.Tensor, torch.Tensor]:
        '''
        Forward pass of the VQ-VAE, encodes the `raw_audio` to latent states, which are then decoded for each level.
        The commit loss, which ensure that the encoder\'s computed embeddings are close to the codebook vectors, is
        computed.

        Args:
            raw_audio (`torch.FloatTensor`):
                Audio input which will be encoded and decoded.

        Returns:
            `Tuple[torch.Tensor, torch.Tensor]`


        Example:
        ```python
        >>> from transformers import JukeboxVQVAE, set_seed
        >>> import torch

        >>> model = JukeboxVQVAE.from_pretrained("openai/jukebox-1b-lyrics").eval()
        >>> set_seed(0)
        >>> zs = [torch.randint(100, (4, 1))]
        >>> model.decode(zs).shape
        torch.Size([4, 8, 1])
        ```
        '''

class JukeboxMLP(nn.Module):
    c_fc: Incomplete
    c_proj: Incomplete
    act: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class JukeboxLayerNorm(FusedLayerNorm):
    width: Incomplete
    max_numel: Incomplete
    def __init__(self, normalized_shape, eps: float = 1e-05, elementwise_affine: bool = True) -> None: ...
    def forward(self, input): ...

class JukeboxAttention(nn.Module):
    embed_dim: Incomplete
    n_heads: Incomplete
    dropout: Incomplete
    head_dim: Incomplete
    n_ctx: Incomplete
    hidden_dim: Incomplete
    scale: Incomplete
    mask: Incomplete
    c_attn: Incomplete
    c_enc_kv: Incomplete
    c_proj: Incomplete
    attn_dropout: Incomplete
    resid_dropout: Incomplete
    attn_func: Incomplete
    qkv: Incomplete
    blocks: Incomplete
    spread: Incomplete
    block_ctx: Incomplete
    sample_t: int
    cache: Incomplete
    encoder_len: Incomplete
    record_attn: bool
    def __init__(self, config, n_ctx, attn_func: str = 'dense_attn') -> None: ...
    def merge_heads(self, hidden_states): ...
    def split_heads(self, hidden_states, is_key: bool = False): ...
    def dense_attn(self, query, key, value, sample): ...
    def block_attn(self, query, key, value, sample): ...
    def transpose_block_attn(self, query, key, value, sample): ...
    def prev_block_attn(self, query, key, value, sample): ...
    def summary_attn(self, query, key, value, sample): ...
    def summary_spread_attn(self, query, key, value, sample): ...
    def prime_attn(self, query, key, value, sample): ...
    def factored_qkv(self, hidden_states, last_encoder_hidden_states: Incomplete | None = None, sample: bool = False): ...
    def prime_qkv(self, hidden_states, last_encoder_hidden_states: Incomplete | None = None, sample: bool = False): ...
    def decode_qkv(self, hidden_states, last_encoder_hidden_states: Incomplete | None = None, sample: bool = False): ...
    def forward(self, hidden_states, last_encoder_hidden_states: Incomplete | None = None, sample: bool = False): ...
    def del_cache(self) -> None: ...

class JukeboxBlock(nn.Module):
    width: Incomplete
    attn: Incomplete
    layer_norm_0: Incomplete
    mlp: Incomplete
    layer_norm_1: Incomplete
    res_scale: Incomplete
    attn_func: Incomplete
    def __init__(self, config, n_ctx, attn_func: str = 'dense_attn') -> None: ...
    def forward(self, hidden_states, last_encoder_hidden_states, sample: bool = False): ...

class JukeboxLayerStack(nn.Module):
    n_ctx: Incomplete
    width: Incomplete
    num_layers: Incomplete
    blocks: Incomplete
    attention_pattern: Incomplete
    block_ctx: Incomplete
    encoder_len: Incomplete
    n_heads: Incomplete
    saved_attn_weights: Incomplete
    def __init__(self, config, n_ctx) -> None: ...
    def set_record_attn(self, record_attn):
        """
        Makes forward prop dump self-attention softmaxes to self.saved_attn_weights.

        Args:
            record_attn (`Union[bool,set]`):
                Either a set of layer indices indicating which layers to store, or a boolean value indicating Whether
                to dump all.
        """
    def forward(self, hidden_states, last_encoder_hidden_states: Incomplete | None = None, sample: bool = False): ...
    def del_cache(self) -> None: ...

class JukeboxPositionalEmbedding(nn.Module):
    pos_emb: Incomplete
    def __init__(self, embed_dim, width) -> None: ...
    def forward(self): ...

class JukeboxConditionalAutoregressive(nn.Module):
    width: Incomplete
    num_layers: Incomplete
    n_ctx: Incomplete
    embed_dim: Incomplete
    embed_tokens: Incomplete
    embed_tokens_dropout: Incomplete
    metadata_conditioning: Incomplete
    audio_conditioning: Incomplete
    start_token: Incomplete
    pos_emb: Incomplete
    pos_emb_dropout: Incomplete
    transformer: Incomplete
    is_encoder: Incomplete
    encoder_len: Incomplete
    add_cond_after_transformer: bool
    share_embed_tokens_fc_proj_out: bool
    fc_proj_out: Incomplete
    loss: Incomplete
    def __init__(self, config, n_ctx: Incomplete | None = None, embed_dim: Incomplete | None = None, audio_conditioning: bool = False, metadata_conditioning: bool = False, is_encoder: bool = False) -> None:
        """
        Autoregressive model on either lyric tokens or music tokens, or both. The attention pattern should be properly
        set fro each configuration.

        Args:
            config (`JukeboxPriorConfig`):
                Model configuration class with all the parameters of the model. Initializing with a config file does
                not load the weights associated with the model, only the configuration. Check out the
                [`~PreTrainedModel.from_pretrained`] method to load the model weights.
            n_ctx (`int`, *optional*):
                Number of tokens or lyrics tokens provided in a single pass.
            embed_dim (`int`, *optional*):
                Either equals to the dimension of the codebook, or the sum of n_vocab (lyrics) and codeboook dimension,
                if the model combines lyrics and music tokens, or simply n_vocab if the model is a seperate encoder
            audio_conditioning (`bool`, *optional*, defaults to `False`):
                Whether or not the prior supports conditionning on audio.
            metadata_conditioning (`bool`, *optional*, defaults to `False`):
                Whether or not the prior supports conditionning on artitst, genres, lyrics and timing.
            is_encoder (`bool`, *optional*, defaults to `False`):
                Whether the model is an encoder only model.
        """
    def forward(self, tokens, audio_conditioning: Incomplete | None = None, metadata_conditioning: Incomplete | None = None, last_encoder_hidden_states: Incomplete | None = None, get_preds: bool = False, get_acts: bool = False, get_sep_loss: bool = False):
        """
        Args:
            tokens (`torch.tensor`):
                Can represent music tokens, lyrics tokens or both, depending on the configuration.
        """
    def get_emb(self, sample_t, n_samples, tokens, audio_conditioning, metadata_conditioning): ...
    def sample(self, n_samples, audio_conditioning: Incomplete | None = None, metadata_conditioning: Incomplete | None = None, last_encoder_hidden_states: Incomplete | None = None, temp: float = 1.0, top_k: int = 0, top_p: float = 0.0, get_preds: bool = False, sample_tokens: Incomplete | None = None): ...
    def split_chunks(self, length, chunk_size): ...
    def primed_sample(self, n_samples, lyric_and_music_tokens, audio_conditioning: Incomplete | None = None, metadata_conditioning: Incomplete | None = None, last_encoder_hidden_states: Incomplete | None = None, temp: float = 1.0, top_k: int = 0, top_p: float = 0.0, get_preds: bool = False, chunk_size: Incomplete | None = None, sample_tokens: Incomplete | None = None): ...

class JukeboxMusicTokenConditioner(nn.Module):
    """
    The `JukeboxMusicTokenConditioner` takes music tokens as an input (coresponding to the codes of the VQVAE's
    codebook) and upsamples it using a single layer of decoder convolution block (the same is used in the VQVAE).
    """
    embed_tokens: Incomplete
    upsampler: Incomplete
    layer_norm: Incomplete
    def __init__(self, config, level) -> None: ...
    def forward(self, music_tokens, raw_audio_conditionning: Incomplete | None = None):
        """
        Args:
            music_tokens (`torch.LongTensor`):
                Music tokens form the uper level in range(nb_discrete_codes)
            raw_audio_conditionning (`torch.LongTensor`, *optional*):
                Audio used when primed sampling, raw audio information that conditions the generation
        """

class JukeboxRangeEmbedding(nn.Module):
    """
    The `JukeboxRangeEmbedding` interpolate the given [pos_start, pos_end] to obtain an equivalent of time positional
    embedding of length `n_ctx`.

    Binning process : For each pos in position tensor, find its bin [start,end) mapped to [0,1,...,bins-1] [start,end)
    -> [0,1) -> [0, bins) -> floor -> [0,...,bins-1] NOTE: Open ended interval on right, so start <= pos < end, not <=
    end
    """
    n_time: Incomplete
    embed_dim: Incomplete
    emb: Incomplete
    clamp: Incomplete
    def __init__(self, n_time, embed_dim, range, out_width, clamp: bool = False) -> None: ...
    def forward(self, pos_start, pos_end: Incomplete | None = None): ...

class JukeboxLabelConditioner(nn.Module):
    max_nb_genres: Incomplete
    bow_genre_emb: Incomplete
    artist_emb: Incomplete
    include_time_signal: Incomplete
    total_length_emb: Incomplete
    absolute_pos_emb: Incomplete
    relative_pos_emb: Incomplete
    def __init__(self, config, include_time_signal) -> None: ...
    def forward(self, metadata): ...

class JukeboxPrior(PreTrainedModel):
    """
    The JukeboxPrior class, which is a wrapper around the various conditioning and the transformer. JukeboxPrior can be
    seen as language models trained on music. They model the next `music token` prediction task. If a (lyric) `encoderù
    is defined, it also models the `next character` prediction on the lyrics. Can be conditionned on timing, artist,
    genre, lyrics and codes from lower-levels Priors.

    Args:
        config (`JukeboxPriorConfig`):
            Model configuration class with all the parameters of the model. Initializing with a config file does not
            load the weights associated with the model, only the configuration. Check out the
            [`~PreTrainedModel.from_pretrained`] method to load the model weights.
        level (`int`, *optional*):
            Current level of the Prior. Should be in range `[0,nb_priors]`.
        nb_priors (`int`, *optional*, defaults to 3):
            Total number of priors.
        vqvae_encoder (`Callable`, *optional*):
            Encoding method of the VQVAE encoder used in the forward pass of the model. Passing functions instead of
            the vqvae module to avoid getting the parameters.
        vqvae_decoder (`Callable`, *optional*):
            Decoding method of the VQVAE decoder used in the forward pass of the model. Passing functions instead of
            the vqvae module to avoid getting the parameters.
    """
    config_class = JukeboxPriorConfig
    vqvae_encoder: Incomplete
    vqvae_decoder: Incomplete
    levels: Incomplete
    level: Incomplete
    base_model_prefix: Incomplete
    n_ctx: Incomplete
    lyric_conditioning: Incomplete
    nb_relevant_lyric_tokens: Incomplete
    encoder_loss_fraction: Incomplete
    audio_conditioning: Incomplete
    cond_level: Incomplete
    conditioner_blocks: Incomplete
    metadata_conditioning: Incomplete
    metadata_embedding: Incomplete
    is_encoder_decoder: Incomplete
    input_shapes: Incomplete
    embed_dim_shift: Incomplete
    width: Incomplete
    prior: Incomplete
    lyric_acts_width: Incomplete
    encoder_width: Incomplete
    encoder_dim: Incomplete
    encoder: Incomplete
    next_token_prediction_loss_dims: Incomplete
    total_loss_dims: Incomplete
    downsamples: Incomplete
    cond_downsample: Incomplete
    raw_to_tokens: Incomplete
    sample_length: Incomplete
    def __init__(self, config: JukeboxPriorConfig, level: Incomplete | None = None, nb_priors: int = 3, vqvae_encoder: Incomplete | None = None, vqvae_decoder: Incomplete | None = None) -> None: ...
    def get_metadata(self, labels, start, total_length, offset, get_indices: bool = False): ...
    def set_metadata_lyric_tokens(self, labels):
        """
        Processes the full labels to only retreive the relevant lyric tokens and keep the metadata conditioning tokens.
        """
    def get_music_tokens_conds(self, music_tokens, start, end):
        """
        Extracts current level's conditioning music tokens.
        """
    def prior_preprocess(self, tokens, conds):
        """
        Shifts the input tokens to account for the dictionary merge. The embed_dim_shift give by how much the music
        tokens should be shifted by. It is equal to `lyric_vocab_size`.
        """
    def prior_postprocess(self, tokens):
        """
        Shifts back the input tokens if the model uses an encoder decoder architecture. As the embedding layer is
        shared, `prior_embed_dim_shift` shifts the music token ids by `lyric_vocab_size`. Only returns the music
        tokens.
        """
    def embed_tokens(self, music_tokens_conds):
        """
        Embeds the upper level music tokens and upsamples them to provide as audio conditioning.
        """
    def encode(self, hidden_states, start_level: Incomplete | None = None, end_level: Incomplete | None = None, bs_chunks: int = 1):
        """
        Encodes the hidden states (raw audio) using the VQVAE's encoder. Returns latent_states.
        """
    def decode(self, music_tokens, start_level: Incomplete | None = None, end_level: Incomplete | None = None, bs_chunks: int = 1):
        """
        Usamples the sequence of codebook vectors to a raw audio.
        """
    def get_cond(self, music_tokens_conds, metadata):
        """
        Converts the input tokens to input_embeddings. Splits the lyrics form the rest of the metadata. Lyric tokens
        can be None.
        """
    def sample(self, n_samples, music_tokens: Incomplete | None = None, music_tokens_conds: Incomplete | None = None, metadata: Incomplete | None = None, temp: float = 1.0, top_k: int = 0, top_p: float = 0.0, chunk_size: Incomplete | None = None, sample_tokens: Incomplete | None = None):
        """
        Ancestral/Prime sampling a window of tokens using the provided conditioning and metadatas.

        Args:
            n_samples (`int`):
                Number of samples to generate.
            music_tokens (`List[torch.LongTensor]`, *optional*):
                Previously gemerated tokens at the current level. Used as context for the generation.
            music_tokens_conds (`List[torch.FloatTensor]`, *optional*):
                Upper-level music tokens generated by the previous prior model. Is `None` if the generation is not
                conditionned on the upper-level tokens.
            metadata (`List[torch.LongTensor]`, *optional*):
                List containing the metatdata tensor with the artist, genre and the lyric tokens.
            temp (`float`, *optional*, defaults to 1.0):
                Sampling temperature.
            top_k (`int`, *optional*, defaults to 0):
                Top k probabilities used for filtering.
            top_p (`float`, *optional*, defaults to 0.0):
                Top p probabilities used for filtering.
            chunk_size (`int`, *optional*):
                Size of the chunks used to prepare the cache of the transformer.
            sample_tokens (`int`, *optional*):
                Number of tokens to sample.

        """
    def get_encoder_states(self, lyric_tokens, sample: bool = False):
        """
        Retreive the last hidden_states of the lyric encoder that will be attended to by the decoder. Forwards through
        the lyric encoder.
        """
    def get_encoder_loss(self, last_encoder_hidden_states, target_lyrics):
        """
        Computes the loss for the lyric encoder: next lyric token prediction.
        """
    def forward_tokens(self, music_tokens, music_tokens_conds=[], metadata: Incomplete | None = None, get_preds: bool = False, get_attn_weights: bool = False):
        """
        Applies a forward pass using the conditioning tokens. Different from the classic forward as it does not use the
        vqvae's encoding layers.
        """
    def forward(self, hidden_states: torch.Tensor, metadata: Optional[List[torch.LongTensor]], decode: Optional[bool] = False, get_preds: Optional[bool] = False) -> List[torch.Tensor]:
        """
        Encode the hidden states using the `vqvae` encoder, and then predicts the next token in the `forward_tokens`
        function. The loss is the sum of the `encoder` loss and the `decoder` loss.

        Args:
            hidden_states (`torch.Tensor`):
                Hidden states which should be raw audio
            metadata (`List[torch.LongTensor]`, *optional*):
                List containing the metadata conditioning tensorwith the lyric and the metadata tokens.
            decode (`bool`, *optional*, defaults to `False`):
                Whether or not to decode the encoded to tokens.
            get_preds (`bool`, *optional*, defaults to `False`):
                Whether or not to return the actual predicitons of the model.
        """

class JukeboxPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = JukeboxConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool
    def __init__(self, *inputs, **kwargs) -> None: ...

JUKEBOX_SAMPLING_INPUT_DOCSTRING: str

class JukeboxModel(JukeboxPreTrainedModel):
    vqvae: Incomplete
    priors: Incomplete
    def __init__(self, config) -> None: ...
    def set_shared_params(self, model_config) -> None:
        """
        Initialises the parameters that are shared. This has to be done here because the list of `JukeboxPriorConfig`
        is nest, and is thus unreachable in the `from_dict` function
        """
    def decode(self, music_tokens, start_level: int = 0, end_level: Incomplete | None = None, bs_chunks: int = 1): ...
    def encode(self, input_audio, start_level: int = 0, end_level: Incomplete | None = None, bs_chunks: int = 1): ...
    def split_batch(self, obj, n_samples, split_size): ...
    def sample_partial_window(self, music_tokens, labels, offset, sampling_kwargs, level, tokens_to_sample, max_batch_size): ...
    def sample_single_window(self, music_tokens, labels, offset, sampling_kwargs, level, start, max_batch_size): ...
    def sample_level(self, music_tokens, labels, offset, sampling_kwargs, level, total_length, hop_length, max_batch_size): ...
    def ancestral_sample(self, labels, n_samples: int = 1, **sampling_kwargs) -> List[torch.LongTensor]:
        '''
        Example:

        ```python
        >>> from transformers import AutoTokenizer, JukeboxModel, set_seed

        >>> model = JukeboxModel.from_pretrained("openai/jukebox-1b-lyrics", min_duration=0).eval()
        >>> tokenizer = AutoTokenizer.from_pretrained("openai/jukebox-1b-lyrics")

        >>> lyrics = "Hey, are you awake? Can you talk to me?"
        >>> artist = "Zac Brown Band"
        >>> genre = "Country"
        >>> metas = tokenizer(artist=artist, genres=genre, lyrics=lyrics)
        >>> set_seed(0)
        >>> music_tokens = model.ancestral_sample(metas.input_ids, sample_length=400)

        >>> with torch.no_grad():
        ...     model.decode(music_tokens)[:, :10].squeeze(-1)
        tensor([[-0.0219, -0.0679, -0.1050, -0.1203, -0.1271, -0.0936, -0.0396, -0.0405,
            -0.0818, -0.0697]])
        ```
        '''
    def continue_sample(self, music_tokens, labels, **sampling_kwargs) -> List[torch.LongTensor]: ...
    def upsample(self, music_tokens, labels, **sampling_kwargs) -> List[torch.LongTensor]: ...
    def primed_sample(self, raw_audio, labels, **sampling_kwargs) -> List[torch.LongTensor]: ...
