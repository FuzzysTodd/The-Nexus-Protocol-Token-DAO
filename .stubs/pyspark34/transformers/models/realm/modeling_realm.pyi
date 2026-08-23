import torch
from ...activations import ACT2FN as ACT2FN
from ...modeling_outputs import BaseModelOutputWithPastAndCrossAttentions as BaseModelOutputWithPastAndCrossAttentions, BaseModelOutputWithPoolingAndCrossAttentions as BaseModelOutputWithPoolingAndCrossAttentions, MaskedLMOutput as MaskedLMOutput, ModelOutput as ModelOutput
from ...modeling_utils import PreTrainedModel as PreTrainedModel
from ...pytorch_utils import apply_chunking_to_forward as apply_chunking_to_forward, find_pruneable_heads_and_indices as find_pruneable_heads_and_indices, prune_linear_layer as prune_linear_layer
from ...utils import add_start_docstrings as add_start_docstrings, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_realm import RealmConfig as RealmConfig
from _typeshed import Incomplete
from dataclasses import dataclass
from torch import nn
from typing import Optional, Tuple, Union

logger: Incomplete
REALM_PRETRAINED_MODEL_ARCHIVE_LIST: Incomplete

def load_tf_weights_in_realm(model, config, tf_checkpoint_path):
    """Load tf checkpoints in a pytorch model."""

class RealmEmbeddings(nn.Module):
    """Construct the embeddings from word, position and token_type embeddings."""
    word_embeddings: Incomplete
    position_embeddings: Incomplete
    token_type_embeddings: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, past_key_values_length: int = 0) -> torch.Tensor: ...

class RealmSelfAttention(nn.Module):
    num_attention_heads: Incomplete
    attention_head_size: Incomplete
    all_head_size: Incomplete
    query: Incomplete
    key: Incomplete
    value: Incomplete
    dropout: Incomplete
    position_embedding_type: Incomplete
    max_position_embeddings: Incomplete
    distance_embedding: Incomplete
    is_decoder: Incomplete
    def __init__(self, config, position_embedding_type: Incomplete | None = None) -> None: ...
    def transpose_for_scores(self, x: torch.Tensor) -> torch.Tensor: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, encoder_hidden_states: Optional[torch.FloatTensor] = None, encoder_attention_mask: Optional[torch.FloatTensor] = None, past_key_value: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class RealmSelfOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class RealmAttention(nn.Module):
    self: Incomplete
    output: Incomplete
    pruned_heads: Incomplete
    def __init__(self, config, position_embedding_type: Incomplete | None = None) -> None: ...
    def prune_heads(self, heads) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, encoder_hidden_states: Optional[torch.FloatTensor] = None, encoder_attention_mask: Optional[torch.FloatTensor] = None, past_key_value: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...

class RealmIntermediate(nn.Module):
    dense: Incomplete
    intermediate_act_fn: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

class RealmOutput(nn.Module):
    dense: Incomplete
    LayerNorm: Incomplete
    dropout: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, input_tensor: torch.Tensor) -> torch.Tensor: ...

class RealmLayer(nn.Module):
    chunk_size_feed_forward: Incomplete
    seq_len_dim: int
    attention: Incomplete
    is_decoder: Incomplete
    add_cross_attention: Incomplete
    crossattention: Incomplete
    intermediate: Incomplete
    output: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, encoder_hidden_states: Optional[torch.FloatTensor] = None, encoder_attention_mask: Optional[torch.FloatTensor] = None, past_key_value: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, output_attentions: Optional[bool] = False) -> Tuple[torch.Tensor]: ...
    def feed_forward_chunk(self, attention_output): ...

class RealmEncoder(nn.Module):
    config: Incomplete
    layer: Incomplete
    gradient_checkpointing: bool
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor, attention_mask: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, encoder_hidden_states: Optional[torch.FloatTensor] = None, encoder_attention_mask: Optional[torch.FloatTensor] = None, past_key_values: Optional[Tuple[Tuple[torch.FloatTensor]]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = False, output_hidden_states: Optional[bool] = False, return_dict: Optional[bool] = True) -> Union[Tuple[torch.Tensor], BaseModelOutputWithPastAndCrossAttentions]: ...

class RealmPooler(nn.Module):
    dense: Incomplete
    activation: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor: ...

@dataclass
class RealmEmbedderOutput(ModelOutput):
    """
    Outputs of [`RealmEmbedder`] models.

    Args:
        projected_score (`torch.FloatTensor` of shape `(batch_size, config.retriever_proj_size)`):

            Projected score.
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
    projected_score: torch.FloatTensor = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, projected_score, hidden_states, attentions) -> None: ...

@dataclass
class RealmScorerOutput(ModelOutput):
    """
    Outputs of [`RealmScorer`] models.

    Args:
        relevance_score (`torch.FloatTensor` of shape `(batch_size, config.num_candidates)`):
            The relevance score of document candidates (before softmax).
        query_score (`torch.FloatTensor` of shape `(batch_size, config.retriever_proj_size)`):
            Query score derived from the query embedder.
        candidate_score (`torch.FloatTensor` of shape `(batch_size, config.num_candidates, config.retriever_proj_size)`):
            Candidate score derived from the embedder.
    """
    relevance_score: torch.FloatTensor = ...
    query_score: torch.FloatTensor = ...
    candidate_score: torch.FloatTensor = ...
    def __init__(self, relevance_score, query_score, candidate_score) -> None: ...

@dataclass
class RealmReaderOutput(ModelOutput):
    """
    Outputs of [`RealmReader`] models.

    Args:
        loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `start_positions`, `end_positions`, `has_answers` are provided):
            Total loss.
        retriever_loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `start_positions`, `end_positions`, `has_answers` are provided):
            Retriever loss.
        reader_loss (`torch.FloatTensor` of shape `(1,)`, *optional*, returned when `start_positions`, `end_positions`, `has_answers` are provided):
            Reader loss.
        retriever_correct (`torch.BoolTensor` of shape `(config.searcher_beam_size,)`, *optional*):
            Whether or not an evidence block contains answer.
        reader_correct (`torch.BoolTensor` of shape `(config.reader_beam_size, num_candidates)`, *optional*):
            Whether or not a span candidate contains answer.
        block_idx (`torch.LongTensor` of shape `()`):
            The index of the retrieved evidence block in which the predicted answer is most likely.
        candidate (`torch.LongTensor` of shape `()`):
            The index of the retrieved span candidates in which the predicted answer is most likely.
        start_pos (`torch.IntTensor` of shape `()`):
            Predicted answer starting position in *RealmReader*'s inputs.
        end_pos: (`torch.IntTensor` of shape `()`):
            Predicted answer ending position in *RealmReader*'s inputs.
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
    loss: torch.FloatTensor = ...
    retriever_loss: torch.FloatTensor = ...
    reader_loss: torch.FloatTensor = ...
    retriever_correct: torch.BoolTensor = ...
    reader_correct: torch.BoolTensor = ...
    block_idx: torch.LongTensor = ...
    candidate: torch.LongTensor = ...
    start_pos: torch.int32 = ...
    end_pos: torch.int32 = ...
    hidden_states: Optional[Tuple[torch.FloatTensor]] = ...
    attentions: Optional[Tuple[torch.FloatTensor]] = ...
    def __init__(self, loss, retriever_loss, reader_loss, retriever_correct, reader_correct, block_idx, candidate, start_pos, end_pos, hidden_states, attentions) -> None: ...

@dataclass
class RealmForOpenQAOutput(ModelOutput):
    """

    Outputs of [`RealmForOpenQA`] models.

    Args:
        reader_output (`dict`):
            Reader output.
        predicted_answer_ids (`torch.LongTensor` of shape `(answer_sequence_length)`):
            Predicted answer ids.
    """
    reader_output: dict = ...
    predicted_answer_ids: torch.LongTensor = ...
    def __init__(self, reader_output, predicted_answer_ids) -> None: ...

class RealmPredictionHeadTransform(nn.Module):
    dense: Incomplete
    transform_act_fn: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class RealmLMPredictionHead(nn.Module):
    transform: Incomplete
    decoder: Incomplete
    bias: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class RealmOnlyMLMHead(nn.Module):
    predictions: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, sequence_output): ...

class RealmScorerProjection(nn.Module):
    predictions: Incomplete
    dense: Incomplete
    LayerNorm: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states): ...

class RealmReaderProjection(nn.Module):
    config: Incomplete
    dense_intermediate: Incomplete
    dense_output: Incomplete
    layer_normalization: Incomplete
    relu: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, hidden_states, block_mask): ...

REALM_START_DOCSTRING: str
REALM_INPUTS_DOCSTRING: str

class RealmPreTrainedModel(PreTrainedModel):
    """
    An abstract class to handle weights initialization and a simple interface for downloading and loading pretrained
    models.
    """
    config_class = RealmConfig
    load_tf_weights = load_tf_weights_in_realm
    base_model_prefix: str

class RealmBertModel(RealmPreTrainedModel):
    """
    Same as the original BertModel but remove docstrings.
    """
    config: Incomplete
    embeddings: Incomplete
    encoder: Incomplete
    pooler: Incomplete
    def __init__(self, config, add_pooling_layer: bool = True) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Incomplete | None = None, attention_mask: Incomplete | None = None, token_type_ids: Incomplete | None = None, position_ids: Incomplete | None = None, head_mask: Incomplete | None = None, inputs_embeds: Incomplete | None = None, encoder_hidden_states: Incomplete | None = None, encoder_attention_mask: Incomplete | None = None, past_key_values: Incomplete | None = None, use_cache: Incomplete | None = None, output_attentions: Incomplete | None = None, output_hidden_states: Incomplete | None = None, return_dict: Incomplete | None = None): ...

class RealmEmbedder(RealmPreTrainedModel):
    realm: Incomplete
    cls: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, RealmEmbedderOutput]:
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, RealmEmbedder
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("google/realm-cc-news-pretrained-embedder")
        >>> model = RealmEmbedder.from_pretrained("google/realm-cc-news-pretrained-embedder")

        >>> inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
        >>> outputs = model(**inputs)

        >>> projected_score = outputs.projected_score
        ```
        '''

class RealmScorer(RealmPreTrainedModel):
    """
    Args:
        query_embedder ([`RealmEmbedder`]):
            Embedder for input sequences. If not specified, it will use the same embedder as candidate sequences.
    """
    embedder: Incomplete
    query_embedder: Incomplete
    def __init__(self, config, query_embedder: Incomplete | None = None) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, candidate_input_ids: Optional[torch.LongTensor] = None, candidate_attention_mask: Optional[torch.FloatTensor] = None, candidate_token_type_ids: Optional[torch.LongTensor] = None, candidate_inputs_embeds: Optional[torch.FloatTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, RealmScorerOutput]:
        '''
        candidate_input_ids (`torch.LongTensor` of shape `(batch_size, num_candidates, sequence_length)`):
            Indices of candidate input sequence tokens in the vocabulary.

            Indices can be obtained using [`AutoTokenizer`]. See [`PreTrainedTokenizer.encode`] and
            [`PreTrainedTokenizer.__call__`] for details.

            [What are input IDs?](../glossary#input-ids)
        candidate_attention_mask (`torch.FloatTensor` of shape `(batch_size, num_candidates, sequence_length)`, *optional*):
            Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

            - 1 for tokens that are **not masked**,
            - 0 for tokens that are **masked**.

            [What are attention masks?](../glossary#attention-mask)
        candidate_token_type_ids (`torch.LongTensor` of shape `(batch_size, num_candidates, sequence_length)`, *optional*):
            Segment token indices to indicate first and second portions of the inputs. Indices are selected in `[0,
            1]`:

            - 0 corresponds to a *sentence A* token,
            - 1 corresponds to a *sentence B* token.

            [What are token type IDs?](../glossary#token-type-ids)
        candidate_inputs_embeds (`torch.FloatTensor` of shape `(batch_size * num_candidates, sequence_length, hidden_size)`, *optional*):
            Optionally, instead of passing `candidate_input_ids` you can choose to directly pass an embedded
            representation. This is useful if you want more control over how to convert *candidate_input_ids* indices
            into associated vectors than the model\'s internal embedding lookup matrix.

        Returns:

        Example:

        ```python
        >>> import torch
        >>> from transformers import AutoTokenizer, RealmScorer

        >>> tokenizer = AutoTokenizer.from_pretrained("google/realm-cc-news-pretrained-scorer")
        >>> model = RealmScorer.from_pretrained("google/realm-cc-news-pretrained-scorer", num_candidates=2)

        >>> # batch_size = 2, num_candidates = 2
        >>> input_texts = ["How are you?", "What is the item in the picture?"]
        >>> candidates_texts = [["Hello world!", "Nice to meet you!"], ["A cute cat.", "An adorable dog."]]

        >>> inputs = tokenizer(input_texts, return_tensors="pt")
        >>> candidates_inputs = tokenizer.batch_encode_candidates(candidates_texts, max_length=10, return_tensors="pt")

        >>> outputs = model(
        ...     **inputs,
        ...     candidate_input_ids=candidates_inputs.input_ids,
        ...     candidate_attention_mask=candidates_inputs.attention_mask,
        ...     candidate_token_type_ids=candidates_inputs.token_type_ids,
        ... )
        >>> relevance_score = outputs.relevance_score
        ```'''

class RealmKnowledgeAugEncoder(RealmPreTrainedModel):
    realm: Incomplete
    cls: Incomplete
    def __init__(self, config) -> None: ...
    def get_input_embeddings(self): ...
    def set_input_embeddings(self, value) -> None: ...
    def get_output_embeddings(self): ...
    def set_output_embeddings(self, new_embeddings) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, relevance_score: Optional[torch.FloatTensor] = None, labels: Optional[torch.LongTensor] = None, mlm_mask: Optional[torch.LongTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, MaskedLMOutput]:
        '''
        relevance_score (`torch.FloatTensor` of shape `(batch_size, num_candidates)`, *optional*):
            Relevance score derived from RealmScorer, must be specified if you want to compute the masked language
            modeling loss.

        labels (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the masked language modeling loss. Indices should be in `[-100, 0, ...,
            config.vocab_size]` (see `input_ids` docstring) Tokens with indices set to `-100` are ignored (masked), the
            loss is only computed for the tokens with labels in `[0, ..., config.vocab_size]`

        mlm_mask (`torch.LongTensor` of shape `(batch_size, sequence_length)`, *optional*):
            Mask to avoid calculating joint loss on certain positions. If not specified, the loss will not be masked.
            Mask values selected in `[0, 1]`:

            - 1 for tokens that are **not masked**,
            - 0 for tokens that are **masked**.

        Returns:

        Example:

        ```python
        >>> import torch
        >>> from transformers import AutoTokenizer, RealmKnowledgeAugEncoder

        >>> tokenizer = AutoTokenizer.from_pretrained("google/realm-cc-news-pretrained-encoder")
        >>> model = RealmKnowledgeAugEncoder.from_pretrained(
        ...     "google/realm-cc-news-pretrained-encoder", num_candidates=2
        ... )

        >>> # batch_size = 2, num_candidates = 2
        >>> text = [["Hello world!", "Nice to meet you!"], ["The cute cat.", "The adorable dog."]]

        >>> inputs = tokenizer.batch_encode_candidates(text, max_length=10, return_tensors="pt")
        >>> outputs = model(**inputs)
        >>> logits = outputs.logits
        ```'''

class RealmReader(RealmPreTrainedModel):
    num_labels: Incomplete
    realm: Incomplete
    cls: Incomplete
    qa_outputs: Incomplete
    def __init__(self, config) -> None: ...
    def forward(self, input_ids: Optional[torch.LongTensor] = None, attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, position_ids: Optional[torch.LongTensor] = None, head_mask: Optional[torch.FloatTensor] = None, inputs_embeds: Optional[torch.FloatTensor] = None, relevance_score: Optional[torch.FloatTensor] = None, block_mask: Optional[torch.BoolTensor] = None, start_positions: Optional[torch.LongTensor] = None, end_positions: Optional[torch.LongTensor] = None, has_answers: Optional[torch.BoolTensor] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, return_dict: Optional[bool] = None) -> Union[Tuple, RealmReaderOutput]:
        """
        relevance_score (`torch.FloatTensor` of shape `(searcher_beam_size,)`, *optional*):
            Relevance score, which must be specified if you want to compute the logits and marginal log loss.
        block_mask (`torch.BoolTensor` of shape `(searcher_beam_size, sequence_length)`, *optional*):
            The mask of the evidence block, which must be specified if you want to compute the logits and marginal log
            loss.
        start_positions (`torch.LongTensor` of shape `(searcher_beam_size,)`, *optional*):
            Labels for position (index) of the start of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        end_positions (`torch.LongTensor` of shape `(searcher_beam_size,)`, *optional*):
            Labels for position (index) of the end of the labelled span for computing the token classification loss.
            Positions are clamped to the length of the sequence (`sequence_length`). Position outside of the sequence
            are not taken into account for computing the loss.
        has_answers (`torch.BoolTensor` of shape `(searcher_beam_size,)`, *optional*):
            Whether or not the evidence block has answer(s).

        Returns:
        """

REALM_FOR_OPEN_QA_DOCSTRING: str

class RealmForOpenQA(RealmPreTrainedModel):
    embedder: Incomplete
    reader: Incomplete
    retriever: Incomplete
    def __init__(self, config, retriever: Incomplete | None = None) -> None: ...
    @property
    def searcher_beam_size(self): ...
    block_emb: Incomplete
    def block_embedding_to(self, device) -> None:
        """Send `self.block_emb` to a specific device.

        Args:
            device (`str` or `torch.device`):
                The device to which `self.block_emb` will be sent.
        """
    def forward(self, input_ids: Optional[torch.LongTensor], attention_mask: Optional[torch.FloatTensor] = None, token_type_ids: Optional[torch.LongTensor] = None, answer_ids: Optional[torch.LongTensor] = None, return_dict: Optional[bool] = None) -> Union[Tuple, RealmForOpenQAOutput]:
        '''
        Returns:

        Example:

        ```python
        >>> import torch
        >>> from transformers import RealmForOpenQA, RealmRetriever, AutoTokenizer

        >>> retriever = RealmRetriever.from_pretrained("google/realm-orqa-nq-openqa")
        >>> tokenizer = AutoTokenizer.from_pretrained("google/realm-orqa-nq-openqa")
        >>> model = RealmForOpenQA.from_pretrained("google/realm-orqa-nq-openqa", retriever=retriever)

        >>> question = "Who is the pioneer in modern computer science?"
        >>> question_ids = tokenizer([question], return_tensors="pt")
        >>> answer_ids = tokenizer(
        ...     ["alan mathison turing"],
        ...     add_special_tokens=False,
        ...     return_token_type_ids=False,
        ...     return_attention_mask=False,
        ... ).input_ids

        >>> reader_output, predicted_answer_ids = model(**question_ids, answer_ids=answer_ids, return_dict=False)
        >>> predicted_answer = tokenizer.decode(predicted_answer_ids)
        >>> loss = reader_output.loss
        ```'''
