import torch
from ...activations import ACT2FN as ACT2FN
from ...file_utils import ModelOutput as ModelOutput
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPast as BaseModelOutputWithPast, BaseModelOutputWithPooling as BaseModelOutputWithPooling, CausalLMOutputWithPast as CausalLMOutputWithPast
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_git import GitConfig as GitConfig, GitVisionConfig as GitVisionConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import List, Optional, Tuple, Union

logger: Incomplete
GIT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

@dataclass
class GitVisionModelOutput(ModelOutput):
    """
    Base class for vision model's outputs that also contains image embeddings of the pooling of the last hidden states.

    Args:
        image_embeds (`torch.FloatTensor` of shape `(batch_size, output_dim)` *optional* returned when model is initialized with `with_projection=True`):
            The image embeddings obtained by applying the projection layer to the pooler_output.
        last_hidden_state (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
            Sequence of hidden-states at the output of the last layer of the model.
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings, if the model has an embedding layer, +
            one for the output of each layer) of shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the optional initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    image_embeds: Optional[torch.FloatTensor] = ...
    last_hidden_state: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, image_embeds, last_hidden_state, hidden_states, attentions) -> None: ...

class GitEmbeddings(nn.Module):
    """Construct the embeddings from word and position embeddings."""
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, past_key_values_length: int = 0) -> torch.Tensor: ...

class GitSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    image_patch_tokens: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    max_position_embeddings: Incomplete
    distance_embedding: Incomplete
    def __init__(self, config, position_embedding_type: Incomplete | None = None) -> None: ...
    def transpose_for_scores(self, x: torch.Tensor) -> torch.Tensor: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, past_key_value: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, output_attentions: Optional[bool] = False, pixel_values_present: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class GitSelfOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class GitAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config, position_embedding_type: Incomplete | None = None) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, past_key_value: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, output_attentions: Optional[bool] = False, pixel_values_present: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class GitIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class GitOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class GitLayer(nn.Module):
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, past_key_value: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, output_attentions: Optional[bool] = False, pixel_values_present: Optional[bool] = False) -> Tuple[torch.Tensor]: ...
    def feed_forward_chunk(self, attention_output): ...

class GitEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = False, output_hidden_states: Optional[bool] = False, pixel_values_present: Optional[bool] = False, return_dict: Optional[bool] = True) -> Union[Tuple[torch.Tensor], BaseModelOutputWithPast]: ...

class GitPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = GitConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool

GIT_START_DOCSTRING: str
GIT_INPUTS_DOCSTRING: str

class GitVisionEmbeddings(nn.Module):
    config: Incomplete
    embed_dim: Incomplete
    image_size: Incomplete
    patch_size: Incomplete
    class_embedding: Incomplete
    patch_embedding: Incomplete
    num_patches: Incomplete
    num_positions: Incomplete
    position_embedding: Incomplete
    def __init__(self, config: GitVisionConfig) -> None: ...
    def forward(self, pixel_values: torch.FloatTensor) -> torch.Tensor: ...

class GitVisionMLP(nn.Module):
    config: Incomplete
    activation_fn: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class GitVisionAttention(nn.Module):
    """Multi-headed attention from 'Attention Is All You Need' paper"""
    config: Incomplete
    embed_dim: Incomplete
    num_heads: Incomplete
    head_dim: Incomplete
    scale: Incomplete
    dropout: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    q_proj: Incomplete
    out_proj: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, causal_attention_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor, Optional[torch.Tensor], Optional[Tuple[torch.Tensor]]]:
        """Input shape: Batch x Time x Channel"""

class GitVisionEncoderLayer(nn.Module):
    embed_dim: Incomplete
    self_attn: Incomplete
    layer_norm1: Incomplete
    mlp: Incomplete
    layer_norm2: Incomplete
    def __init__(self, config: GitVisionConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: torch.Tensor, causal_attention_mask: torch.Tensor, output_attentions: Optional[bool] = False) -> Tuple[torch.FloatTensor]:
        """
        Args:
            hidden_states (`torch.FloatTensor`): input to the layer of shape `(batch, seq_len, embed_dim)`
            attention_mask (`torch.FloatTensor`): attention mask of size
                `(batch, 1, tgt_len, src_len)` where padding elements are indicated by very large negative values.
                `(config.encoder_attention_heads,)`.
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
        """

class GitVisionEncoder(nn.Module):
    """
    Transformer encoder consisting of `config.num_hidden_layers` self attention layers. Each layer is a
    [`GitVisionEncoderLayer`].

    Args:
        config: GitVisionConfig
    """
    config: Incomplete
    layers: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: GitVisionConfig) -> None: ...
    def forward(self, inputs_embeds, attention_mask: Optional[torch.Tensor] = None, causal_attention_mask: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]:
        """
        Args:
            inputs_embeds (`torch.FloatTensor` of shape `(batch_size, sequence_length, hidden_size)`):
                Optionally, instead of passing `input_ids` you can choose to directly pass an embedded representation.
                This is useful if you want more control over how to convert `input_ids` indices into associated vectors
                than the model's internal embedding lookup matrix.
            attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            causal_attention_mask (`torch.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Causal mask for the text model. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            output_attentions (`bool`, *optional*):
                Whether or not to return the attentions tensors of all attention layers. See `attentions` under
                returned tensors for more detail.
            output_hidden_states (`bool`, *optional*):
                Whether or not to return the hidden states of all layers. See `hidden_states` under returned tensors
                for more detail.
            return_dict (`bool`, *optional*):
                Whether or not to return a [`~utils.ModelOutput`] instead of a plain tuple.
        """

GIT_VISION_INPUTS_DOCSTRING: str

class GitVisionTransformer(nn.Module):
    config: Incomplete
    embeddings: Incomplete
    pre_layrnorm: Incomplete
    encoder: Incomplete
    post_layernorm: Incomplete
    def __init__(self, config: GitVisionConfig) -> None: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]:
        """
        Returns:

        """

class GitVisionModel(GitPreTrainedModel):
    config_class = GitVisionConfig
    main_input_name: str
    vision_model: Incomplete
    def __init__(self, config: GitVisionConfig) -> None: ...
    def get_input_embeddings(self) -> nn.Module: ...
    def forward(self, pixel_values: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, BaseModelOutput]:
        '''
        Returns:

        Examples:

        ```python
        >>> from PIL import Image
        >>> import requests
        >>> from transformers import AutoProcessor, GitVisionModel

        >>> processor = AutoProcessor.from_pretrained("microsoft/git-base")
        >>> model = GitVisionModel.from_pretrained("microsoft/git-base")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> inputs = processor(images=image, return_tensors="pt")

        >>> outputs = model(**inputs)
        >>> last_hidden_state = outputs.last_hidden_state
        ```'''

class GitProjection(nn.Module):
    config: Incomplete
    visual_projection: Incomplete
    def __init__(self, config: GitConfig) -> None: ...
    def forward(self, embeddings: torch.Tensor) -> torch.Tensor: ...

class GitModel(GitPreTrainedModel):
    config: Incomplete
    embeddings: Incomplete
    image_encoder: Incomplete
    encoder: Incomplete
    visual_projection: Incomplete
    img_temperal_embedding: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def create_attention_mask(self, tgt, memory, tgt_mask, past_key_values_length, memory_key_padding_mask: Incomplete | None = None): ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, pixel_values: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, past_key_values: Optional[List[torch.FloatTensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], BaseModelOutputWithPooling]:
        '''
        past_key_values (`tuple(tuple(torch.FloatTensor))` of length `config.n_layers` with each tuple having 4 tensors of shape `(batch_size, num_heads, sequence_length - 1, embed_size_per_head)`):
            Contains precomputed key and value hidden states of the attention blocks. Can be used to speed up decoding.

            If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those that
            don\'t have their past key value states given to this model) of shape `(batch_size, 1)` instead of all
            `decoder_input_ids` of shape `(batch_size, sequence_length)`.
        use_cache (`bool`, *optional*):
            If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
            `past_key_values`).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoProcessor, AutoModel
        >>> import requests
        >>> from PIL import Image

        >>> processor = AutoProcessor.from_pretrained("microsoft/git-base")
        >>> model = AutoModel.from_pretrained("microsoft/git-base")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> text = "this is an image of two cats"

        >>> inputs = processor(text, images=image, return_tensors="pt")

        >>> outputs = model(**inputs)
        >>> last_hidden_state = outputs.last_hidden_state
        ```'''

class GitForCausalLM(GitPreTrainedModel):
    git: Incomplete
    output: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, attention_mask: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, pixel_values: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, past_key_values: Optional[List[torch.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], CausalLMOutputWithPast]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the left-to-right language modeling loss (next word prediction). Indices should be in
            `[-100, 0, ..., config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are
            ignored (masked), the loss is only computed for the tokens with labels n `[0, ..., config.vocab_size]`
        past_key_values (`tuple(tuple(torch.FloatTensor))` of length `config.n_layers` with each tuple having 4 tensors of shape `(batch_size, num_heads, sequence_length - 1, embed_size_per_head)`):
            Contains precomputed key and value hidden states of the attention blocks. Can be used to speed up decoding.

            If `past_key_values` are used, the user can optionally input only the last `decoder_input_ids` (those that
            don\'t have their past key value states given to this model) of shape `(batch_size, 1)` instead of all
            `decoder_input_ids` of shape `(batch_size, sequence_length)`.
        use_cache (`bool`, *optional*):
            If set to `True`, `past_key_values` key value states are returned and can be used to speed up decoding (see
            `past_key_values`).

        Returns:

        Examples:

        Image captioning example:

        ```python
        >>> from transformers import AutoProcessor, AutoModelForCausalLM
        >>> import requests
        >>> from PIL import Image

        >>> processor = AutoProcessor.from_pretrained("microsoft/git-base-coco")
        >>> model = AutoModelForCausalLM.from_pretrained("microsoft/git-base-coco")

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> pixel_values = processor(images=image, return_tensors="pt").pixel_values

        >>> generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
        >>> generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        >>> print(generated_caption)
        two cats sleeping on a pink blanket next to remotes.
        ```

        Visual question answering (VQA) example:

        ```python
        >>> from transformers import AutoProcessor, AutoModelForCausalLM
        >>> from huggingface_hub import hf_hub_download
        >>> from PIL import Image

        >>> processor = AutoProcessor.from_pretrained("microsoft/git-base-textvqa")
        >>> model = AutoModelForCausalLM.from_pretrained("microsoft/git-base-textvqa")

        >>> file_path = hf_hub_download(repo_id="nielsr/textvqa-sample", filename="bus.png", repo_type="dataset")
        >>> image = Image.open(file_path).convert("RGB")

        >>> pixel_values = processor(images=image, return_tensors="pt").pixel_values

        >>> question = "what does the front of the bus say at the top?"

        >>> input_ids = processor(text=question, add_special_tokens=False).input_ids
        >>> input_ids = [processor.tokenizer.cls_token_id] + input_ids
        >>> input_ids = torch.tensor(input_ids).unsqueeze(0)

        >>> generated_ids = model.generate(pixel_values=pixel_values, input_ids=input_ids, max_length=50)
        >>> print(processor.batch_decode(generated_ids, skip_special_tokens=True))
        [\'what does the front of the bus say at the top? special\']
        ```

        Video captioning example:

        ```python
        >>> from transformers import AutoProcessor, AutoModelForCausalLM
        >>> from PIL import Image
        >>> import numpy as np
        >>> from huggingface_hub import hf_hub_download
        >>> from decord import VideoReader, cpu

        >>> processor = AutoProcessor.from_pretrained("microsoft/git-base-vatex")
        >>> model = AutoModelForCausalLM.from_pretrained("microsoft/git-base-vatex")

        >>> # set seed for reproducability
        >>> np.random.seed(45)


        >>> def sample_frame_indices(clip_len, frame_sample_rate, seg_len):
        ...     converted_len = int(clip_len * frame_sample_rate)
        ...     end_idx = np.random.randint(converted_len, seg_len)
        ...     start_idx = end_idx - converted_len
        ...     indices = np.linspace(start_idx, end_idx, num=clip_len)
        ...     indices = np.clip(indices, start_idx, end_idx - 1).astype(np.int64)
        ...     return indices


        >>> def sample_frames(file_path, num_frames):
        ...     videoreader = VideoReader(file_path, num_threads=1, ctx=cpu(0))
        ...     videoreader.seek(0)
        ...     indices = sample_frame_indices(clip_len=num_frames, frame_sample_rate=4, seg_len=len(videoreader))
        ...     frames = videoreader.get_batch(indices).asnumpy()
        ...     return list(frames)


        >>> # load video
        >>> file_path = hf_hub_download(
        ...     repo_id="nielsr/video-demo", filename="eating_spaghetti.mp4", repo_type="dataset"
        ... )

        >>> # sample frames
        >>> num_frames = model.config.num_image_with_embedding
        >>> frames = sample_frames(file_path, num_frames)

        >>> pixel_values = processor(images=frames, return_tensors="pt").pixel_values

        >>> generated_ids = model.generate(pixel_values=pixel_values, max_length=50)

        >>> print("Generated caption:", processor.batch_decode(generated_ids, skip_special_tokens=True))
        Generated caption: [\'a woman is sitting at a table and she is talking about the food she is holding.\']
        ```
        '''
    def prepare_inputs_for_generation(self, input_ids, past: Incomplete | None = None, attention_mask: Incomplete | None = None, use_cache: bool = True, **kwargs): ...
