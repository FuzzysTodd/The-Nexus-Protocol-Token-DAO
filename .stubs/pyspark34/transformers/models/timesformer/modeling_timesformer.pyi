import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, ImageClassifierOutput as ImageClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_timesformer import TimesformerConfig as TimesformerConfig
from _typeshed import Incomplete
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
TIMESFORMER_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class TimesformerPatchEmbeddings(nn.Module):
    """Image to Patch Embedding"""
    image_size: Incomplete
    patch_size: Incomplete
    num_patches: Incomplete
    projection: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values): ...

class TimesformerEmbeddings(nn.Module):
    """
    Construct the patch and position embeddings.
    """
    attention_type: Incomplete
    patch_embeddings: Incomplete
    num_patches: Incomplete
    cls_token: Incomplete
    position_embeddings: Incomplete
    pos_drop: Incomplete
    time_embeddings: Incomplete
    time_drop: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values): ...

def drop_path(input: torch.Tensor, drop_prob: float = 0.0, training: bool = False) -> torch.Tensor:
    """
    Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks).

    Comment by Ross Wightman: This is the same as the DropConnect impl I created for EfficientNet, etc networks,
    however, the original name is misleading as 'Drop Connect' is a different form of dropout in a separate paper...
    See discussion: https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956 ... I've opted for changing the
    layer and argument names to 'drop path' rather than mix DropConnect as a layer name and use 'survival rate' as the
    argument.
    """

class TimeSformerDropPath(nn.Module):
    """Drop paths (Stochastic Depth) per sample (when applied in main path of residual blocks)."""
    drop_prob: Incomplete
    def __init__(self, drop_prob: Optional[float] = None) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...
    def extra_repr(self) -> str: ...

class TimesformerSelfAttention(nn.Module):
    num_heads: Incomplete
    scale: Incomplete
    qkv: Incomplete
    attn_drop: Incomplete
    def __init__(self, config: TimesformerConfig) -> None: ...
    def forward(self, hidden_states, output_attentions: bool = False): ...

class TimesformerSelfOutput(nn.Module):
    """
    The residual connection is defined in TimesformerLayer instead of here (as is the case with other models), due to
    the layernorm applied before each block.
    """
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: TimesformerConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class TimeSformerAttention(nn.Module):
    attention: Incomplete
    output: Incomplete
    def __init__(self, config: TimesformerConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, output_attentions: bool = False) -> Union[Tuple[torch.Tensor, torch.Tensor], Tuple[torch.Tensor]]: ...

class TimesformerIntermediate(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config: TimesformerConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class TimesformerOutput(nn.Module):
    dense: Incomplete
    dropout: Incomplete
    def __init__(self, config: TimesformerConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class TimesformerLayer(nn.Module):
    drop_path: Incomplete
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    layernorm_before: Incomplete
    layernorm_after: Incomplete
    config: Incomplete
    attention_type: Incomplete
    temporal_layernorm: Incomplete
    temporal_attention: Incomplete
    temporal_dense: Incomplete
    def __init__(self, config: TimesformerConfig, layer_index: int) -> None: ...
    def forward(self, hidden_states: torch.Tensor, output_attentions: bool = False): ...

class TimesformerEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config: TimesformerConfig) -> None: ...
    def forward(self, hidden_states: torch.Tensor, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True) -> Union[tuple, BaseModelOutput]: ...

class TimesformerPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = TimesformerConfig
    base_model_prefix: str
    main_input_name: str
    supports_gradient_checkpointing: bool

TIMESFORMER_START_DOCSTRING: str
TIMESFORMER_INPUTS_DOCSTRING: str

class TimesformerModel(TimesformerPreTrainedModel):
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    layernorm: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def forward(self, pixel_values, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None):
        '''
        Returns:

        Examples:

        ```python
        >>> from decord import VideoReader, cpu
        >>> import numpy as np

        >>> from transformers import AutoFeatureExtractor, TimesformerModel
        >>> from huggingface_hub import hf_hub_download


        >>> def sample_frame_indices(clip_len, frame_sample_rate, seg_len):
        ...     converted_len = int(clip_len * frame_sample_rate)
        ...     end_idx = np.random.randint(converted_len, seg_len)
        ...     start_idx = end_idx - converted_len
        ...     indices = np.linspace(start_idx, end_idx, num=clip_len)
        ...     indices = np.clip(indices, start_idx, end_idx - 1).astype(np.int64)
        ...     return indices


        >>> # video clip consists of 300 frames (10 seconds at 30 FPS)
        >>> file_path = hf_hub_download(
        ...     repo_id="nielsr/video-demo", filename="eating_spaghetti.mp4", repo_type="dataset"
        ... )
        >>> videoreader = VideoReader(file_path, num_threads=1, ctx=cpu(0))

        >>> # sample 8 frames
        >>> videoreader.seek(0)
        >>> indices = sample_frame_indices(clip_len=8, frame_sample_rate=4, seg_len=len(videoreader))
        >>> video = videoreader.get_batch(indices).asnumpy()

        >>> feature_extractor = AutoFeatureExtractor.from_pretrained("MCG-NJU/videomae-base")
        >>> model = TimesformerModel.from_pretrained("facebook/timesformer-base-finetuned-k400")

        >>> # prepare video for the model
        >>> inputs = feature_extractor(list(video), return_tensors="pt")

        >>> # forward pass
        >>> outputs = model(**inputs)
        >>> last_hidden_states = outputs.last_hidden_state
        >>> list(last_hidden_states.shape)
        [1, 1568, 768]
        ```'''

class TimesformerForVideoClassification(TimesformerPreTrainedModel):
    num_labels: Incomplete
    timesformer: Incomplete
    classifier: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, pixel_values: Optional[torch.Tensor] = None, labels: Optional[torch.Tensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, ImageClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the image classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. If `config.num_labels == 1` a regression loss is computed (Mean-Square loss), If
            `config.num_labels > 1` a classification loss is computed (Cross-Entropy).

        Returns:

        Examples:

        ```python
        >>> from decord import VideoReader, cpu
        >>> import torch
        >>> import numpy as np

        >>> from transformers import AutoFeatureExtractor, TimesformerForVideoClassification
        >>> from huggingface_hub import hf_hub_download

        >>> np.random.seed(0)


        >>> def sample_frame_indices(clip_len, frame_sample_rate, seg_len):
        ...     converted_len = int(clip_len * frame_sample_rate)
        ...     end_idx = np.random.randint(converted_len, seg_len)
        ...     start_idx = end_idx - converted_len
        ...     indices = np.linspace(start_idx, end_idx, num=clip_len)
        ...     indices = np.clip(indices, start_idx, end_idx - 1).astype(np.int64)
        ...     return indices


        >>> # video clip consists of 300 frames (10 seconds at 30 FPS)
        >>> file_path = hf_hub_download(
        ...     repo_id="nielsr/video-demo", filename="eating_spaghetti.mp4", repo_type="dataset"
        ... )
        >>> videoreader = VideoReader(file_path, num_threads=1, ctx=cpu(0))

        >>> # sample 8 frames
        >>> videoreader.seek(0)
        >>> indices = sample_frame_indices(clip_len=8, frame_sample_rate=4, seg_len=len(videoreader))
        >>> video = videoreader.get_batch(indices).asnumpy()

        >>> feature_extractor = AutoFeatureExtractor.from_pretrained("MCG-NJU/videomae-base-finetuned-kinetics")
        >>> model = TimesformerForVideoClassification.from_pretrained("facebook/timesformer-base-finetuned-k400")

        >>> inputs = feature_extractor(list(video), return_tensors="pt")

        >>> with torch.no_grad():
        ...     outputs = model(**inputs)
        ...     logits = outputs.logits

        >>> # model predicts one of the 400 Kinetics-400 classes
        >>> predicted_label = logits.argmax(-1).item()
        >>> print(model.config.id2label[predicted_label])
        eating spaghetti
        ```'''
