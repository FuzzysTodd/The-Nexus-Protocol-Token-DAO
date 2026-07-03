import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutput as BaseModelOutput, BaseModelOutputWithPooling as BaseModelOutputWithPooling, MultipleChoiceModelOutput as MultipleChoiceModelOutput, SequenceClassifierOutput as SequenceClassifierOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import ModelOutput as ModelOutput, add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_visual_bert import VisualBertConfig as VisualBertConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
VISUAL_BERT_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

class VisualBertEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings and visual embeddings."""
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    visual_token_type_embeddings: Incomplete
    visual_position_embeddings: Incomplete
    visual_projection: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, inputs_embeds: Incomplete | None = None, visual_embeds: Incomplete | None = None, visual_token_type_ids: Incomplete | None = None, image_text_alignment: Incomplete | None = None): ...

class VisualBertSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def transpose_for_scores(self, x): ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class VisualBertSelfOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class VisualBertAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...

class VisualBertIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class VisualBertOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class VisualBertLayer(nn.Module):
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False): ...
    def feed_forward_chunk(self, attention_output): ...

class VisualBertEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, attention_mask: Incomplete | None = None, head_mask: Incomplete | None = None, output_attentions: bool = False, output_hidden_states: bool = False, return_dict: bool = True): ...

class VisualBertPooler(nn.Module):
    dense: Incomplete
    activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class VisualBertPredictionHeadTransform(nn.Module):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class VisualBertLMPredictionHead(nn.Module):
    transform: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class VisualBertPreTrainingHeads(nn.Module):
    predictions: Incomplete
    seq_relationship: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, sequence_output, pooled_output): ...

class VisualBertPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = VisualBertConfig
    base_model_prefix: str
    supports_gradient_checkpointing: bool

@dataclass
class VisualBertForPreTrainingOutput(ModelOutput):
    """
    Output type of [`VisualBertForPreTraining`].

    Args:
        loss (*optional*, returned when `labels` is provided, `torch.FloatTensor` of shape `(1,)`):
            Total loss as the sum of the masked language modeling loss and the sentence-image prediction
            (classification) loss.
        prediction_logits (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
        seq_relationship_logits (`torch.FloatTensor` of shape `(batch_size, 2)`):
            Prediction scores of the sentence-image prediction (classification) head (scores of True/False continuation
            before SoftMax).
        hidden_states (`tuple(torch.FloatTensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `torch.FloatTensor` (one for the output of the embeddings + one for the output of each layer) of
            shape `(batch_size, sequence_length, hidden_size)`.

            Hidden-states of the model at the output of each layer plus the initial embedding outputs.
        attentions (`tuple(torch.FloatTensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `torch.FloatTensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights after the attention softmax, used to compute the weighted average in the self-attention
            heads.
    """
    loss: Optional[torch.FloatTensor] = ...
    prediction_logits: torch.FloatTensor = ...
    seq_relationship_logits: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, prediction_logits, seq_relationship_logits, hidden_states, attentions) -> None: ...

VISUAL_BERT_START_DOCSTRING: str
VISUAL_BERT_INPUTS_DOCSTRING: str

class VisualBertModel(VisualBertPreTrainedModel):
    """

    The model can behave as an encoder (with only self-attention) following the architecture described in [Attention is
    all you need](https://arxiv.org/abs/1706.03762) by Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit,
    Llion Jones, Aidan N. Gomez, Lukasz Kaiser and Illia Polosukhin.
    """
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    bypass_transformer: Incomplete
    additional_layer: Incomplete
    def __init__(self, config, add_pooling_layer: bool = True) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.LongTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, visual_embeds: Optional[torch.FloatTensor] = None, visual_attention_mask: Optional[torch.LongTensor] = None, visual_token_type_ids: Optional[torch.LongTensor] = None, image_text_alignment: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple[torch.Tensor], BaseModelOutputWithPooling]:
        '''

        Returns:

        Example:

        ```python
        # Assumption: *get_visual_embeddings(image)* gets the visual embeddings of the image.
        from transformers import AutoTokenizer, VisualBertModel
        import torch

        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        model = VisualBertModel.from_pretrained("uclanlp/visualbert-vqa-coco-pre")

        inputs = tokenizer("The capital of France is Paris.", return_tensors="pt")
        visual_embeds = get_visual_embeddings(image).unsqueeze(0)
        visual_token_type_ids = torch.ones(visual_embeds.shape[:-1], dtype=torch.long)
        visual_attention_mask = torch.ones(visual_embeds.shape[:-1], dtype=torch.float)

        inputs.update(
            {
                "visual_embeds": visual_embeds,
                "visual_token_type_ids": visual_token_type_ids,
                "visual_attention_mask": visual_attention_mask,
            }
        )

        outputs = model(**inputs)

        last_hidden_states = outputs.last_hidden_state
        ```'''

class VisualBertForPreTraining(VisualBertPreTrainedModel):
    visual_bert: Incomplete
    cls: Incomplete
    def __init__(self, config) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.LongTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, visual_embeds: Optional[torch.FloatTensor] = None, visual_attention_mask: Optional[torch.LongTensor] = None, visual_token_type_ids: Optional[torch.LongTensor] = None, image_text_alignment: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[torch.LongTensor] = None, sentence_image_labels: Optional[torch.LongTensor] = None) -> Union[Tuple[torch.Tensor], VisualBertForPreTrainingOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, total_sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`
        sentence_image_labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sentence-image prediction (classification) loss. Input should be a sequence pair
            (see `input_ids` docstring) Indices should be in `[0, 1]`:

            - 0 indicates sequence B is a matching pair of sequence A for the given image,
            - 1 indicates sequence B is a random sequence w.r.t A for the given image.

        Returns:

        Example:

        ```python
        # Assumption: *get_visual_embeddings(image)* gets the visual embeddings of the image in the batch.
        from transformers import AutoTokenizer, VisualBertForPreTraining

        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        model = VisualBertForPreTraining.from_pretrained("uclanlp/visualbert-vqa-coco-pre")

        inputs = tokenizer("The capital of France is [MASK].", return_tensors="pt")
        visual_embeds = get_visual_embeddings(image).unsqueeze(0)
        visual_token_type_ids = torch.ones(visual_embeds.shape[:-1], dtype=torch.long)
        visual_attention_mask = torch.ones(visual_embeds.shape[:-1], dtype=torch.float)

        inputs.update(
            {
                "visual_embeds": visual_embeds,
                "visual_token_type_ids": visual_token_type_ids,
                "visual_attention_mask": visual_attention_mask,
            }
        )
        max_length = inputs["input_ids"].shape[-1] + visual_embeds.shape[-2]
        labels = tokenizer(
            "The capital of France is Paris.", return_tensors="pt", padding="max_length", max_length=max_length
        )["input_ids"]
        sentence_image_labels = torch.tensor(1).unsqueeze(0)  # Batch_size


        outputs = model(**inputs, labels=labels, sentence_image_labels=sentence_image_labels)
        loss = outputs.loss
        prediction_logits = outputs.prediction_logits
        seq_relationship_logits = outputs.seq_relationship_logits
        ```'''

class VisualBertForMultipleChoice(VisualBertPreTrainedModel):
    visual_bert: Incomplete
    dropout: Incomplete
    cls: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.LongTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, visual_embeds: Optional[torch.FloatTensor] = None, visual_attention_mask: Optional[torch.LongTensor] = None, visual_token_type_ids: Optional[torch.LongTensor] = None, image_text_alignment: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[torch.LongTensor] = None) -> Union[Tuple[torch.Tensor], MultipleChoiceModelOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the multiple choice classification loss. Indices should be in `[0, ...,
            num_choices-1]` where `num_choices` is the size of the second dimension of the input tensors. (See
            `input_ids` above)

        Returns:

        Example:

        ```python
        # Assumption: *get_visual_embeddings(image)* gets the visual embeddings of the image in the batch.
        from transformers import AutoTokenizer, VisualBertForMultipleChoice
        import torch

        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        model = VisualBertForMultipleChoice.from_pretrained("uclanlp/visualbert-vcr")

        prompt = "In Italy, pizza served in formal settings, such as at a restaurant, is presented unsliced."
        choice0 = "It is eaten with a fork and a knife."
        choice1 = "It is eaten while held in the hand."

        visual_embeds = get_visual_embeddings(image)
        # (batch_size, num_choices, visual_seq_length, visual_embedding_dim)
        visual_embeds = visual_embeds.expand(1, 2, *visual_embeds.shape)
        visual_token_type_ids = torch.ones(visual_embeds.shape[:-1], dtype=torch.long)
        visual_attention_mask = torch.ones(visual_embeds.shape[:-1], dtype=torch.float)

        labels = torch.tensor(0).unsqueeze(0)  # choice0 is correct (according to Wikipedia ;)), batch size 1

        encoding = tokenizer([[prompt, prompt], [choice0, choice1]], return_tensors="pt", padding=True)
        # batch size is 1
        inputs_dict = {k: v.unsqueeze(0) for k, v in encoding.items()}
        inputs_dict.update(
            {
                "visual_embeds": visual_embeds,
                "visual_attention_mask": visual_attention_mask,
                "visual_token_type_ids": visual_token_type_ids,
                "labels": labels,
            }
        )
        outputs = model(**inputs_dict)

        loss = outputs.loss
        logits = outputs.logits
        ```'''

class VisualBertForQuestionAnswering(VisualBertPreTrainedModel):
    num_labels: Incomplete
    visual_bert: Incomplete
    dropout: Incomplete
    cls: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.LongTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, visual_embeds: Optional[torch.FloatTensor] = None, visual_attention_mask: Optional[torch.LongTensor] = None, visual_token_type_ids: Optional[torch.LongTensor] = None, image_text_alignment: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[torch.LongTensor] = None) -> Union[Tuple[torch.Tensor], SequenceClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size, total_sequence_length)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. A KLDivLoss is computed between the labels and the returned logits.

        Returns:

        Example:

        ```python
        # Assumption: *get_visual_embeddings(image)* gets the visual embeddings of the image in the batch.
        from transformers import AutoTokenizer, VisualBertForQuestionAnswering
        import torch

        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        model = VisualBertForQuestionAnswering.from_pretrained("uclanlp/visualbert-vqa")

        text = "Who is eating the apple?"
        inputs = tokenizer(text, return_tensors="pt")
        visual_embeds = get_visual_embeddings(image).unsqueeze(0)
        visual_token_type_ids = torch.ones(visual_embeds.shape[:-1], dtype=torch.long)
        visual_attention_mask = torch.ones(visual_embeds.shape[:-1], dtype=torch.float)

        inputs.update(
            {
                "visual_embeds": visual_embeds,
                "visual_token_type_ids": visual_token_type_ids,
                "visual_attention_mask": visual_attention_mask,
            }
        )

        labels = torch.tensor([[0.0, 1.0]]).unsqueeze(0)  # Batch size 1, Num labels 2

        outputs = model(**inputs, labels=labels)
        loss = outputs.loss
        scores = outputs.logits
        ```'''

class VisualBertForVisualReasoning(VisualBertPreTrainedModel):
    num_labels: Incomplete
    visual_bert: Incomplete
    dropout: Incomplete
    cls: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.LongTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, visual_embeds: Optional[torch.FloatTensor] = None, visual_attention_mask: Optional[torch.LongTensor] = None, visual_token_type_ids: Optional[torch.LongTensor] = None, image_text_alignment: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, labels: Optional[torch.LongTensor] = None) -> Union[Tuple[torch.Tensor], SequenceClassifierOutput]:
        '''
        labels (`torch.LongTensor` of shape `(batch_size,)`, *optional*):
            Labels for computing the sequence classification/regression loss. Indices should be in `[0, ...,
            config.num_labels - 1]`. A classification loss is computed (Cross-Entropy) against these labels.

        Returns:

        Example:

        ```python
        # Assumption: *get_visual_embeddings(image)* gets the visual embeddings of the image in the batch.
        from transformers import AutoTokenizer, VisualBertForVisualReasoning
        import torch

        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        model = VisualBertForVisualReasoning.from_pretrained("uclanlp/visualbert-nlvr2")

        text = "Who is eating the apple?"
        inputs = tokenizer(text, return_tensors="pt")
        visual_embeds = get_visual_embeddings(image).unsqueeze(0)
        visual_token_type_ids = torch.ones(visual_embeds.shape[:-1], dtype=torch.long)
        visual_attention_mask = torch.ones(visual_embeds.shape[:-1], dtype=torch.float)

        inputs.update(
            {
                "visual_embeds": visual_embeds,
                "visual_token_type_ids": visual_token_type_ids,
                "visual_attention_mask": visual_attention_mask,
            }
        )

        labels = torch.tensor(1).unsqueeze(0)  # Batch size 1, Num choices 2

        outputs = model(**inputs, labels=labels)
        loss = outputs.loss
        scores = outputs.logits
        ```'''

class VisualBertRegionToPhraseAttention(nn.Module):
    num_attention_heads: int
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def transpose_for_scores(self, x): ...
    def forward(self, query, key, attention_mask): ...

class VisualBertForRegionToPhraseAlignment(VisualBertPreTrainedModel):
    visual_bert: Incomplete
    dropout: Incomplete
    cls: Incomplete
    attention: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.LongTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, visual_embeds: Optional[torch.FloatTensor] = None, visual_attention_mask: Optional[torch.LongTensor] = None, visual_token_type_ids: Optional[torch.LongTensor] = None, image_text_alignment: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None, region_to_phrase_position: Optional[torch.LongTensor] = None, labels: Optional[torch.LongTensor] = None) -> Union[Tuple[torch.Tensor], SequenceClassifierOutput]:
        '''
        region_to_phrase_position (`torch.LongTensor` of shape `(batch_size, total_sequence_length)`, *optional*):
            The positions depicting the position of the image embedding corresponding to the textual tokens.

        labels (`torch.LongTensor` of shape `(batch_size, total_sequence_length, visual_sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. KLDivLoss is computed against these labels and the
            outputs from the attention layer.

        Returns:

        Example:

        ```python
        # Assumption: *get_visual_embeddings(image)* gets the visual embeddings of the image in the batch.
        from transformers import AutoTokenizer, VisualBertForRegionToPhraseAlignment
        import torch

        tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        model = VisualBertForRegionToPhraseAlignment.from_pretrained("uclanlp/visualbert-vqa-coco-pre")

        text = "Who is eating the apple?"
        inputs = tokenizer(text, return_tensors="pt")
        visual_embeds = get_visual_embeddings(image).unsqueeze(0)
        visual_token_type_ids = torch.ones(visual_embeds.shape[:-1], dtype=torch.long)
        visual_attention_mask = torch.ones(visual_embeds.shape[:-1], dtype=torch.float)
        region_to_phrase_position = torch.ones((1, inputs["input_ids"].shape[-1] + visual_embeds.shape[-2]))

        inputs.update(
            {
                "region_to_phrase_position": region_to_phrase_position,
                "visual_embeds": visual_embeds,
                "visual_token_type_ids": visual_token_type_ids,
                "visual_attention_mask": visual_attention_mask,
            }
        )

        labels = torch.ones(
            (1, inputs["input_ids"].shape[-1] + visual_embeds.shape[-2], visual_embeds.shape[-2])
        )  # Batch size 1

        outputs = model(**inputs, labels=labels)
        loss = outputs.loss
        scores = outputs.logits
        ```'''
