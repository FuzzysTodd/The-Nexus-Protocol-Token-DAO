import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutputWithPastAndCrossAttentions as BaseModelOutputWithPastAndCrossAttentions, CausalLMOutputWithCrossAttentions as CausalLMOutputWithCrossAttentions, SequenceClassifierOutputWithPast as SequenceClassifierOutputWithPast
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import Conv1D as Conv1D, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_conv1d_layer as prune_conv1d_layer
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_imagegpt import ImageGPTConfig as ImageGPTConfig
from _typeshed import Incomplete
from torch import nn
from typing import Any, Optional, Tuple, Union

logger: Incomplete
IMAGEGPT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def load_tf_weights_in_imagegpt(model, config, imagegpt_checkpoint_path):
    """
    Load tf checkpoints in a pytorch model
    """

class ImageGPTLayerNorm(nn.Module):
    eps: Incomplete
    weight: Incomplete
    def __init__(self, hidden_size: Tuple[int], eps: float = 1e-05) -> None: ...
    def forward(self, tensor: torch.Tensor) -> tuple: ...

class ImageGPTAttention(nn.Module):
    embed_dim: Incomplete
    num_heads: Incomplete
    head_dim: Incomplete
    split_size: Incomplete
    scale_attn_weights: Incomplete
    is_cross_attention: Incomplete
    scale_attn_by_inverse_layer_idx: Incomplete
    layer_idx: Incomplete
    reorder_and_upcast_attn: Incomplete
    c_attn: Incomplete
    q_attn: Incomplete
    c_proj: Incomplete
    attn_dropout: Incomplete
    resid_dropout: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config, is_cross_attention: Optional[bool] = False, layer_idx: Optional[int] = None) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states: torch.Tensor, layer_past: Optional[bool] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, encoder_hidden_states: Optional[torch.Tensor] = None, encoder_attention_mask: Optional[torch.Tensor] = None, use_cache: Optional[bool] = False, output_attentions: Optional[bool] = False) -> tuple: ...

class ImageGPTMLP(nn.Module):
    c_fc: Incomplete
    c_proj: Incomplete
    act: Incomplete
    dropout: Incomplete
    def __init__(self, intermediate_size, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class ImageGPTBlock(nn.Module):
    ln_1: Incomplete
    attn: Incomplete
    ln_2: Incomplete
    crossattention: Incomplete
    ln_cross_attn: Incomplete
    mlp: Incomplete
    def __init__(self, config, layer_idx: Incomplete | None = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor, layer_past: Optional[bool] = None, attention_mask: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, encoder_hidden_states: Optional[torch.Tensor] = None, encoder_attention_mask: Optional[torch.Tensor] = None, use_cache: Optional[bool] = False, output_attentions: Optional[bool] = False) -> tuple: ...

class ImageGPTPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = ImageGPTConfig
    load_tf_weights = load_tf_weights_in_imagegpt
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool
    def __init__(self, *inputs, **kwargs) -> None: ...

IMAGEGPT_START_DOCSTRING: str
IMAGEGPT_INPUTS_DOCSTRING: str

class ImageGPTModel(ImageGPTPreTrainedModel):
    embed_dim: Incomplete
    wte: Incomplete
    wpe: Incomplete
    drop: Incomplete
    h: Incomplete
    ln_f: Incomplete
    model_parallel: bool
    device_map: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: ImageGPTConfig) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, encoder_hidden_states: Optional[torch.Tensor] = None, encoder_attention_mask: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **kwargs: Any) -> Union[Tuple, BaseModelOutputWithPastAndCrossAttentions]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
            `labels = input_ids` Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100`
            are ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, ImageGPTModel
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("openai/imagegpt-small")
        >>> model = ImageGPTModel.from_pretrained("openai/imagegpt-small")

        >>> inputs = image_processor(images=image, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> last_hidden_states = outputs.last_hidden_state
        ```'''

class ImageGPTForCausalImageModeling(ImageGPTPreTrainedModel):
    transformer: Incomplete
    lm_head: Incomplete
    model_parallel: bool
    device_map: Incomplete
    def __init__(self, config: ImageGPTConfig) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def prepare_inputs_for_generation(self, input_ids: torch.Tensor, past_key_values: Optional[bool] = None, **kwargs): ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, encoder_hidden_states: Optional[torch.Tensor] = None, encoder_attention_mask: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **kwargs: Any) -> Union[Tuple, CausalLMOutputWithCrossAttentions]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for language modeling. Note that the labels **are shifted** inside the model, i.e. you can set
            `labels = input_ids` Indices are selected in `[-100, 0, ..., config.vocab_size]` All labels set to `-100`
            are ignored (masked), the loss is only computed for labels in `[0, ..., config.vocab_size]`

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, ImageGPTForCausalImageModeling
        >>> import torch
        >>> import matplotlib.pyplot as plt
        >>> import numpy as np

        >>> image_processor = AutoImageProcessor.from_pretrained("openai/imagegpt-small")
        >>> model = ImageGPTForCausalImageModeling.from_pretrained("openai/imagegpt-small")
        >>> device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        >>> model.to(device)

        >>> # unconditional generation of 8 images
        >>> batch_size = 8
        >>> context = torch.full((batch_size, 1), model.config.vocab_size - 1)  # initialize with SOS token
        >>> context = torch.tensor(context).to(device)
        >>> output = model.generate(
        ...     input_ids=context, max_length=model.config.n_positions + 1, temperature=1.0, do_sample=True, top_k=40
        ... )

        >>> clusters = image_processor.clusters
        >>> height = image_processor.size["height"]
        >>> width = image_processor.size["width"]

        >>> samples = output[:, 1:].cpu().detach().numpy()
        >>> samples_img = [
        ...     np.reshape(np.rint(127.5 * (clusters[s] + 1.0)), [height, width, 3]).astype(np.uint8) for s in samples
        ... ]  # convert color cluster tokens back to pixels
        >>> f, axes = plt.subplots(1, batch_size, dpi=300)

        >>> for img, ax in zip(samples_img, axes):
        ...     ax.axis("off")
        ...     ax.imshow(img)
        ```'''

class ImageGPTForImageClassification(ImageGPTPreTrainedModel):
    num_labels: Incomplete
    transformer: Incomplete
    score: Incomplete
    def __init__(self, config: ImageGPTConfig) -> None: ...
    def forward(self, input_ids: Optional[torch.Tensor] = None, past_key_values: Optional[Tuple[Tuple[torch.Tensor]]] = None, attention_mask: Optional[torch.Tensor] = None, token_type_ids: Optional[torch.Tensor] = None, position_ids: Optional[torch.Tensor] = None, head_mask: Optional[torch.Tensor] = None, inputs_embeds: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, **kwargs: Any) -> Union[Tuple, SequenceClassifierOutputWithPast]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from transformers import AutoImageProcessor, ImageGPTForImageClassification
        >>> from PIL import Image
        >>> import requests

        >>> url = "http://images.cocodataset.org/val2017/000000039769.jpg"
        >>> image = Image.open(requests.get(url, stream=True).raw)

        >>> image_processor = AutoImageProcessor.from_pretrained("openai/imagegpt-small")
        >>> model = ImageGPTForImageClassification.from_pretrained("openai/imagegpt-small")

        >>> inputs = image_processor(images=image, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> logits = outputs.logits
        ```'''
