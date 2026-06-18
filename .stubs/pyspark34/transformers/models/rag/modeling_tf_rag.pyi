import numpy as np
import tensorflow as tf
from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...modeling_tf_utils import TFCausalLanguageModelingLoss as TFCausalLanguageModelingLoss, TFModelInputType as TFModelInputType, TFPreTrainedModel as TFPreTrainedModel, shape_list as shape_list, unpack_inputs as unpack_inputs
from ...utils import ModelOutput as ModelOutput, add_start_docstrings_to_model_forward as add_start_docstrings_to_model_forward, logging as logging, replace_return_docstrings as replace_return_docstrings
from .configuration_rag import RagConfig as RagConfig
from .retrieval_rag import RagRetriever as RagRetriever
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import List, Optional, Tuple, Union

logger: Incomplete

@dataclass
class TFRetrievAugLMMarginOutput(ModelOutput):
    """
    Base class for retriever augmented marginalized models outputs.

    Args:
        loss (`tf.Tensor` of shape `(1,)`, *optional*, returned when `labels` is provided):
            Language modeling loss.
        logits (`tf.Tensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head. The score is possibly marginalized over all documents for
            each vocabulary token.
        past_key_values (`List[tf.Tensor]`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            List of `tf.Tensor` of length `config.n_layers`, with each tensor of shape `(2, batch_size, num_heads,
            sequence_length, embed_size_per_head)`).

            Contains precomputed hidden-states (key and values in the attention blocks) of the decoder that can be used
            (see `past_key_values` input) to speed up sequential decoding.
        doc_scores (`tf.Tensor` of shape `(batch_size, config.n_docs)`):
            Score between each retrieved document embeddings (see `retrieved_doc_embeds`) and
            `question_encoder_last_hidden_state`.
        retrieved_doc_embeds (`tf.Tensor` of shape `(batch_size, config.n_docs, hidden_size)`, *optional*, returned when *output_retrieved=True*):
            Embedded documents retrieved by the retriever. Is used with `question_encoder_last_hidden_state` to compute
            the `doc_scores`.
        retrieved_doc_ids (`tf.Tensor` (int32) of shape `(batch_size, config.n_docs)`, *optional*, returned when *output_retrieved=True*):
            The indexes of the embedded documents retrieved by the retriever.
        context_input_ids (`tf.Tensor`(int32) of shape `(batch_size * config.n_docs, config.max_combined_length)`, *optional*, returned when *output_retrieved=True*):
            Input ids post-processed from the retrieved documents and the question encoder input_ids by the retriever.
        context_attention_mask (`tf.Tensor` (int32) of shape `(batch_size * config.n_docs, config.max_combined_length)`, *optional*, returned when *output_retrieved=True*):
            Attention mask post-processed from the retrieved documents and the question encoder `input_ids` by the
            retriever.
        question_encoder_last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden states at the output of the last layer of the question encoder pooled output of the
            model.
        question_enc_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings and one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden states of the question encoder at the output of each layer plus the initial embedding outputs.
        question_enc_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the question encoder, after the attention softmax, used to compute the weighted
            average in the self-attention heads.
        generator_enc_last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the generator encoder of the model.
        generator_enc_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings and one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden states of the generator encoder at the output of each layer plus the initial embedding outputs.
        generator_enc_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the generator encoder, after the attention softmax, used to compute the weighted
            average in the self-attention heads.
        generator_dec_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings and one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden states of the generator decoder at the output of each layer plus the initial embedding outputs.
        generator_dec_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the generator decoder, after the attention softmax, used to compute the weighted
            average in the self-attention heads.
    """
    loss: Optional[tf.Tensor] = ...
    logits: tf.Tensor = ...
    past_key_values: Optional[List[tf.Tensor]] = ...
    doc_scores: Optional[tf.Tensor] = ...
    retrieved_doc_embeds: Optional[tf.Tensor] = ...
    retrieved_doc_ids: Optional[tf.Tensor] = ...
    context_input_ids: Optional[tf.Tensor] = ...
    context_attention_mask: Optional[tf.Tensor] = ...
    question_encoder_last_hidden_state: Optional[tf.Tensor] = ...
    question_enc_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    question_enc_attentions: Optional[Tuple[tf.Tensor]] = ...
    generator_enc_last_hidden_state: Optional[tf.Tensor] = ...
    generator_enc_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    generator_enc_attentions: Optional[Tuple[tf.Tensor]] = ...
    generator_dec_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    generator_dec_attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, loss, logits, past_key_values, doc_scores, retrieved_doc_embeds, retrieved_doc_ids, context_input_ids, context_attention_mask, question_encoder_last_hidden_state, question_enc_hidden_states, question_enc_attentions, generator_enc_last_hidden_state, generator_enc_hidden_states, generator_enc_attentions, generator_dec_hidden_states, generator_dec_attentions) -> None: ...

@dataclass
class TFRetrievAugLMOutput(ModelOutput):
    """
    Args:
        logits (`tf.Tensor` of shape `(batch_size, sequence_length, config.vocab_size)`):
            Prediction scores of the language modeling head. The score is possibly marginalized over all documents for
            each vocabulary token.
        past_key_values (`List[tf.Tensor]`, *optional*, returned when `use_cache=True` is passed or when `config.use_cache=True`):
            List of `tf.Tensor` of length `config.n_layers`, with each tensor of shape `(2, batch_size, num_heads,
            sequence_length, embed_size_per_head)`).

            Contains precomputed hidden-states (key and values in the attention blocks) of the decoder that can be used
            (see `past_key_values` input) to speed up sequential decoding.
        doc_scores (`tf.Tensor` of shape `(batch_size, config.n_docs)`):
            Score between each retrieved document embeddings (see `retrieved_doc_embeds`) and
            `question_encoder_last_hidden_state`.
        retrieved_doc_embeds (`tf.Tensor` of shape `(batch_size, config.n_docs, hidden_size)`, *optional*, returned when *output_retrieved=True*):
            Embedded documents retrieved by the retriever. Is used with `question_encoder_last_hidden_state` to compute
            the `doc_scores`.
        retrieved_doc_ids (`tf.Tensor` of shape `(batch_size, config.n_docs)`, *optional*, returned when *output_retrieved=True*):
            The indexes of the embedded documents retrieved by the retriever.
        context_input_ids (`tf.Tensor` of shape `(batch_size * config.n_docs, config.max_combined_length)`, *optional*, returned when *output_retrieved=True*):
            Input ids post-processed from the retrieved documents and the question encoder input_ids by the retriever.
        context_attention_mask (`tf.Tensor` of shape `(batch_size * config.n_docs, config.max_combined_length)`, *optional*, returned when *output_retrieved=True*):
            Attention mask post-processed from the retrieved documents and the question encoder `input_ids` by the
            retriever.
        question_encoder_last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden states at the output of the last layer of the question encoder pooled output of the
            model.
        question_enc_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings and one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden states of the question encoder at the output of each layer plus the initial embedding outputs.
        question_enc_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the question encoder, after the attention softmax, used to compute the weighted
            average in the self-attention heads.
        generator_enc_last_hidden_state (`tf.Tensor` of shape `(batch_size, sequence_length, hidden_size)`, *optional*):
            Sequence of hidden-states at the output of the last layer of the generator encoder of the model.
        generator_enc_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings and one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden states of the generator encoder at the output of each layer plus the initial embedding outputs.
        generator_enc_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the generator encoder, after the attention softmax, used to compute the weighted
            average in the self-attention heads.
        generator_dec_hidden_states (`tuple(tf.Tensor)`, *optional*, returned when `output_hidden_states=True` is passed or when `config.output_hidden_states=True`):
            Tuple of `tf.Tensor` (one for the output of the embeddings and one for the output of each layer) of shape
            `(batch_size, sequence_length, hidden_size)`.

            Hidden states of the generator decoder at the output of each layer plus the initial embedding outputs.
        generator_dec_attentions (`tuple(tf.Tensor)`, *optional*, returned when `output_attentions=True` is passed or when `config.output_attentions=True`):
            Tuple of `tf.Tensor` (one for each layer) of shape `(batch_size, num_heads, sequence_length,
            sequence_length)`.

            Attentions weights of the generator decoder, after the attention softmax, used to compute the weighted
            average in the self-attention heads.
    """
    logits: tf.Tensor = ...
    past_key_values: Optional[List[tf.Tensor]] = ...
    doc_scores: Optional[tf.Tensor] = ...
    retrieved_doc_embeds: Optional[tf.Tensor] = ...
    retrieved_doc_ids: Optional[tf.Tensor] = ...
    context_input_ids: Optional[tf.Tensor] = ...
    context_attention_mask: Optional[tf.Tensor] = ...
    question_encoder_last_hidden_state: Optional[tf.Tensor] = ...
    question_enc_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    question_enc_attentions: Optional[Tuple[tf.Tensor]] = ...
    generator_enc_last_hidden_state: Optional[tf.Tensor] = ...
    generator_enc_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    generator_enc_attentions: Optional[Tuple[tf.Tensor]] = ...
    generator_dec_hidden_states: Optional[Tuple[tf.Tensor]] = ...
    generator_dec_attentions: Optional[Tuple[tf.Tensor]] = ...
    def __init__(self, logits, past_key_values, doc_scores, retrieved_doc_embeds, retrieved_doc_ids, context_input_ids, context_attention_mask, question_encoder_last_hidden_state, question_enc_hidden_states, question_enc_attentions, generator_enc_last_hidden_state, generator_enc_hidden_states, generator_enc_attentions, generator_dec_hidden_states, generator_dec_attentions) -> None: ...

class TFRagPreTrainedModel(TFPreTrainedModel):
    """
    RAG models were released with the paper [Retrieval-Augmented Generation for Knowledge-Intensive NLP
    Tasks](https://arxiv.org/abs/2005.11401) by Patrick Lewis, Ethan Perez, Aleksandra Piktus et al.

    RAG is a retriever augmented model and encapsulate three components: a question encoder, a dataset retriever and a
    generator, the encoder and generator are trainable while the retriever is just an indexed dataset.

    """
    config_class = RagConfig
    base_model_prefix: str
    @classmethod
    def from_pretrained_question_encoder_generator(cls, question_encoder_pretrained_model_name_or_path: str = None, generator_pretrained_model_name_or_path: str = None, retriever: RagRetriever = None, *model_args, **kwargs) -> TFPreTrainedModel:
        '''
        Instantiates an question encoder and a generator from one or two base classes of the library from pretrained
        model checkpoints.

        Params:
            question_encoder_pretrained_model_name_or_path (`str`, *optional*):
                Information necessary to initiate the question encoder. Can be either:

                    - A string with the *shortcut name* of a pretrained model to load from cache or download, e.g.,
                      `bert-base-uncased`.
                    - A string with the *identifier name* of a pretrained model that was user-uploaded to our S3, e.g.,
                      `dbmdz/bert-base-german-cased`.
                    - A path to a *directory* containing model weights saved using
                      [`~TFPreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.
                    - A path or url to a *pytorch index checkpoint file* (e.g, `./pt_model/`). In this case,
                      `question_encoder_from_pt` should be set to `True`.

            generator_pretrained_model_name_or_path (`str`, *optional*, defaults to `None`):
                Information necessary to initiate the generator. Can be either:

                    - A string with the *shortcut name* of a pretrained model to load from cache or download, e.g.,
                      `t5-small`.
                    - A string with the *identifier name* of a pretrained model that was user-uploaded to our S3, e.g.,
                      `facebook/bart-base`.
                    - A path to a *directory* containing model weights saved using
                      [`~TFPreTrainedModel.save_pretrained`], e.g., `./my_model_directory/`.
                    - A path or url to a *pytorch checkpoint file* (e.g, `./pt_model/`). In this case,
                      `generator_from_pt` should be set to `True`.

            model_args (remaining positional arguments, *optional*):
                All remaining positional arguments will be passed to the underlying model\'s `__init__` method.
            retriever ([`RagRetriever`], *optional*):
                The retriever to use.
            kwargs (remaining dictionary of keyword arguments, *optional*):
                Can be used to update the configuration object (after it being loaded) and initiate the model (e.g.,
                `output_attentions=True`).

                - To update the question_encoder configuration, use the prefix *question_encoder_* for each
                  configuration parameter.
                - To update the generator configuration, use the prefix *generator_* for each configuration parameter.
                - To update the parent model configuration, do not use a prefix for each configuration parameter.

                Behaves differently depending on whether a `config` is provided or automatically loaded.

        Example:

        ```python
        >>> from transformers import RagRetriever, TFRagModel

        >>> # initialize a RAG from two pretrained models.
        >>> model = TFRagModel.from_pretrained_question_encoder_generator(
        ...     "facebook/dpr-question_encoder-single-nq-base", "t5-small"
        ... )
        >>> # alternatively, initialize from pytorch pretrained models can also be done
        >>> model = TFRagModel.from_pretrained_question_encoder_generator(
        ...     "facebook/dpr-question_encoder-single-nq-base",
        ...     "facebook/bart-base",
        ...     generator_from_pt=True,
        ...     question_encoder_from_pt=True,
        ... )

        >>> # saving model after fine-tuning
        >>> model.save_pretrained("./rag")

        >>> # load retriever
        >>> retriever = RagRetriever.from_pretrained(
        ...     "facebook/rag-token-base", index_name="exact", use_dummy_dataset=True
        ... )
        >>> # load fine-tuned model with retriever
        >>> model = TFRagModel.from_pretrained("./rag", retriever=retriever)
        ```'''

RAG_START_DOCSTRING: str
RAG_FORWARD_INPUTS_DOCSTRING: str

class TFRagModel(TFRagPreTrainedModel):
    load_weight_prefix: str
    retriever: Incomplete
    question_encoder: Incomplete
    generator: Incomplete
    def __init__(self, config: Optional[PretrainedConfig] = None, question_encoder: Optional[TFPreTrainedModel] = None, generator: Optional[TFPreTrainedModel] = None, retriever: Optional[RagRetriever] = None, load_weight_prefix: Optional[str] = None, **kwargs) -> None: ...
    def set_retriever(self, retriever: RagRetriever): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_outputs: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_input_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, doc_scores: Optional[Union[np.ndarray, tf.Tensor]] = None, context_input_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, context_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_retrieved: Optional[bool] = None, n_docs: Optional[int] = None, return_dict: Optional[bool] = None, training: bool = False, **kwargs):
        '''
        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, RagRetriever, TFRagModel
        >>> import torch

        >>> tokenizer = AutoTokenizer.from_pretrained("facebook/rag-token-base")
        >>> retriever = RagRetriever.from_pretrained(
        ...     "facebook/rag-token-base", index_name="exact", use_dummy_dataset=True
        ... )
        >>> # initialize with RagRetriever to do everything in one forward call
        >>> model = TFRagModel.from_pretrained("facebook/rag-token-base", retriever=retriever, from_pt=True)

        >>> input_dict = tokenizer.prepare_seq2seq_batch(
        ...     "How many people live in Paris?", "In Paris, there are 10 million people.", return_tensors="tf"
        ... )
        >>> input_ids = input_dict["input_ids"]
        >>> outputs = model(input_ids)
        ```'''

class TFRagTokenForGeneration(TFRagPreTrainedModel, TFCausalLanguageModelingLoss):
    load_weight_prefix: str
    rag: Incomplete
    def __init__(self, config: Optional[PretrainedConfig] = None, question_encoder: Optional[TFPreTrainedModel] = None, generator: Optional[TFPreTrainedModel] = None, retriever: Optional[RagRetriever] = None, **kwargs) -> None: ...
    def set_retriever(self, retriever: RagRetriever): ...
    def prepare_inputs_for_generation(self, decoder_input_ids, past_key_values: Incomplete | None = None, attention_mask: Incomplete | None = None, use_cache: Incomplete | None = None, encoder_outputs: Incomplete | None = None, doc_scores: Incomplete | None = None, n_docs: Incomplete | None = None, **kwargs): ...
    @property
    def retriever(self): ...
    @property
    def generator(self): ...
    @property
    def question_encoder(self): ...
    def marginalize(self, seq_logits, doc_scores, n_docs: Incomplete | None = None): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_input_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_outputs: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, doc_scores: Optional[Union[np.ndarray, tf.Tensor]] = None, context_input_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, context_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_retrieved: Optional[bool] = None, n_docs: Optional[int] = None, do_marginalize: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, reduce_loss: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False, **kwargs):
        '''
        do_marginalize (`bool`, *optional*):
            If `True`, the logits are marginalized over all documents by making use of
            `torch.nn.functional.log_softmax`.
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the cross entropy classification loss according to Rag-Token model formulation See
            https://arxiv.org/pdf/2005.11401.pdf Section 2.1 for details about Rag-Token formulation. Indices should be
            in `[0, ..., config.vocab_size - 1]`.
        reduce_loss (`bool`, *optional*):
            Only relevant if `labels` is passed. If `True`, the NLL loss is reduced using the `tf.Tensor.sum`
            operation.
        kwargs (`Dict[str, any]`, optional, defaults to *{}*):
            Legacy dictionary, which is required so that model can use *generate()* function.

        Returns:

        Example:

        ```python
        >>> import tensorflow as tf
        >>> from transformers import AutoTokenizer, RagRetriever, TFRagTokenForGeneration

        >>> tokenizer = AutoTokenizer.from_pretrained("facebook/rag-token-nq")
        >>> retriever = RagRetriever.from_pretrained(
        ...     "facebook/rag-token-nq", index_name="exact", use_dummy_dataset=True
        ... )
        >>> # initialize with RagRetriever to do everything in one forward call
        >>> model = TFRagTokenForGeneration.from_pretrained("facebook/rag-token-nq", retriever=retriever, from_pt=True)

        >>> input_dict = tokenizer.prepare_seq2seq_batch(
        ...     "How many people live in Paris?", "In Paris, there are 10 million people.", return_tensors="tf"
        ... )
        >>> outputs = model(input_dict, output_retrieved=True)

        >>> # or use retriever separately
        >>> # 1. Encode
        >>> input_ids = input_dict["input_ids"]
        >>> question_hidden_states = model.question_encoder(input_ids)[0]
        >>> # 2. Retrieve
        >>> docs_dict = retriever(input_ids.numpy(), question_hidden_states.numpy(), return_tensors="tf")
        >>> doc_scores = tf.squeeze(
        ...     tf.matmul(
        ...         tf.expand_dims(question_hidden_states, axis=1), docs_dict["retrieved_doc_embeds"], transpose_b=True
        ...     ),
        ...     axis=1,
        ... )
        >>> # 3. Forward to generator
        >>> outputs = model(
        ...     inputs=None,
        ...     context_input_ids=docs_dict["context_input_ids"],
        ...     context_attention_mask=docs_dict["context_attention_mask"],
        ...     doc_scores=doc_scores,
        ...     decoder_input_ids=input_dict["labels"],
        ... )

        >>> # or directly generate
        >>> generated = model.generate(
        ...     context_input_ids=docs_dict["context_input_ids"],
        ...     context_attention_mask=docs_dict["context_attention_mask"],
        ...     doc_scores=doc_scores,
        ... )
        >>> generated_string = tokenizer.batch_decode(generated, skip_special_tokens=True)
        ```'''
    def generate(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[tf.Tensor] = None, context_input_ids: Incomplete | None = None, context_attention_mask: Incomplete | None = None, doc_scores: Incomplete | None = None, n_docs: Incomplete | None = None, generation_config: Incomplete | None = None, **kwargs):
        """
        Implements TFRAG token decoding.

        Args:
            input_ids (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                The sequence used as a prompt for the generation. If `input_ids` is not passed, then
                `context_input_ids` has to be provided.
            attention_mask (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`:

                - 1 for tokens that are **not masked**,
                - 0 for tokens that are **masked**.

                [What are attention masks?](../glossary#attention-mask)
            context_input_ids (`tf.Tensor` of shape `(batch_size * config.n_docs, config.max_combined_length)`, *optional*, returned when *output_retrieved=True*):
                Input IDs post-processed from the retrieved documents and the question encoder `input_ids` by the
                retriever.

                If the model has is not initialized with a `retriever`, `context_input_ids` has to be provided to the
                forward pass. `context_input_ids` are returned by [`~RagRetriever.__call__`].
            context_attention_mask (`tf.Tensor` of shape `(batch_size * config.n_docs, config.max_combined_length)`, *optional*, returned when *output_retrieved=True*):
                Attention mask post-processed from the retrieved documents and the question encoder `input_ids` by the
                retriever.

                If the model has is not initialized with a `retriever`, `context_input_ids` has to be provided to the
                forward pass. `context_input_ids` are returned by [`~RagRetriever.__call__`].
            doc_scores (`tf.Tensor` of shape `(batch_size, config.n_docs)`):
                Score between each retrieved document embeddings (see `retrieved_doc_embeds`) and
                `question_encoder_last_hidden_state`.

                If the model has is not initialized with a `retriever`, `context_input_ids` has to be provided to the
                forward pass. `context_input_ids` are returned by [`~RagRetriever.__call__`].
            n_docs (`int`, *optional*, defaults to `config.n_docs`)
                Number of documents to retrieve and/or number of documents for which to generate an answer.
            generation_config (`~generation.GenerationConfig`, *optional*):
                The generation configuration to be used as base parametrization for the generation call. `**kwargs`
                passed to generate matching the attributes of `generation_config` will override them. If
                `generation_config` is not provided, the default will be used, which had the following loading
                priority: 1) from the `generation_config.json` model file, if it exists; 2) from the model
                configuration. Please note that unspecified parameters will inherit [`~generation.GenerationConfig`]'s
                default values, whose documentation should be checked to parameterize generation.
            kwargs:
                Ad hoc parametrization of `generate_config` and/or additional model-specific kwargs that will be
                forwarded to the `forward` function of the model.

        Return:
            `tf.Tensor` of shape `(batch_size * num_return_sequences, sequence_length)`: The generated sequences. The
            second dimension (sequence_length) is either equal to `max_length` or shorter if all batches finished early
            due to the `eos_token_id`.
        """
    def get_input_embeddings(self): ...
    def get_output_embeddings(self): ...
    def shift_tokens_right(self, input_ids, start_token_id: Incomplete | None = None):
        """Shift input ids one token to the right, and pad with start_token_id"""
    def get_nll(self, seq_logits, doc_scores, target, reduce_loss: bool = False, epsilon: float = 0.0, n_docs: Incomplete | None = None): ...
    def hf_compute_loss(self, labels, y_pred, smooth_epsilon: float = 0.0, from_logits: bool = True, reduce_loss: bool = False):
        """CrossEntropyLoss that ignores pad tokens"""

class TFRagSequenceForGeneration(TFRagPreTrainedModel, TFCausalLanguageModelingLoss):
    load_weight_prefix: str
    rag: Incomplete
    def __init__(self, config: Optional[PretrainedConfig] = None, question_encoder: Optional[TFPreTrainedModel] = None, generator: Optional[TFPreTrainedModel] = None, retriever: Optional[RagRetriever] = None, **kwargs) -> None: ...
    def set_retriever(self, retriever: RagRetriever): ...
    @property
    def retriever(self): ...
    @property
    def generator(self): ...
    @property
    def question_encoder(self): ...
    def call(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_input_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, decoder_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, encoder_outputs: Optional[Union[np.ndarray, tf.Tensor]] = None, past_key_values: Optional[Tuple[Tuple[Union[np.ndarray, tf.Tensor]]]] = None, doc_scores: Optional[Union[np.ndarray, tf.Tensor]] = None, context_input_ids: Optional[Union[np.ndarray, tf.Tensor]] = None, context_attention_mask: Optional[Union[np.ndarray, tf.Tensor]] = None, use_cache: Optional[bool] = None, output_attentions: Optional[bool] = None, output_hidden_states: Optional[bool] = None, output_retrieved: Optional[bool] = None, n_docs: Optional[int] = None, exclude_bos_score: Optional[bool] = None, labels: Optional[Union[np.ndarray, tf.Tensor]] = None, reduce_loss: Optional[bool] = None, return_dict: Optional[bool] = None, training: bool = False, **kwargs) -> Union[Tuple[tf.Tensor], TFRetrievAugLMMarginOutput]:
        '''
        exclude_bos_score (`bool`, *optional*):
            Only relevant if `labels` is passed. If `True`, the score of the BOS token is disregarded when computing
            the loss.
        labels (`tf.Tensor` or `np.ndarray` of shape `(batch_size, sequence_length)`, *optional*):
            Labels for computing the cross entropy classification loss according to Rag-Sequence model formulation See
            https://arxiv.org/pdf/2005.11401.pdf Section 2.1 for details about Rag-Sequence formulation. Indices should
            be in `[0, ..., config.vocab_size - 1]`.
        reduce_loss (`bool`, *optional*):
            Only relevant if `labels` is passed. If `True`, the NLL loss is reduced using the `tf.Tensor.sum`
            operation.
        kwargs (`Dict[str, any]`, optional, defaults to *{}*):
            Legacy dictionary, which is required so that model can use *generate()* function.

        Returns:

        Example:

        ```python
        >>> from transformers import AutoTokenizer, RagRetriever, TFRagSequenceForGeneration

        >>> tokenizer = AutoTokenizer.from_pretrained("facebook/rag-sequence-nq")
        >>> retriever = RagRetriever.from_pretrained(
        ...     "facebook/rag-sequence-nq", index_name="exact", use_dummy_dataset=True
        ... )
        >>> # initialize with RagRetriever to do everything in one forward call
        >>> model = TFRagSequenceForGeneration.from_pretrained(
        ...     "facebook/rag-sequence-nq", retriever=retriever, from_pt=True
        ... )

        >>> input_dict = tokenizer.prepare_seq2seq_batch(
        ...     "How many people live in Paris?", "In Paris, there are 10 million people.", return_tensors="tf"
        ... )
        >>> outputs = model(input_dict, output_retrieved=True)

        >>> # or use retriever separately
        >>> # 1. Encode
        >>> input_ids = input_dict["input_ids"]
        >>> question_hidden_states = model.question_encoder(input_ids)[0]
        >>> # 2. Retrieve
        >>> docs_dict = retriever(input_ids.numpy(), question_hidden_states.numpy(), return_tensors="tf")
        >>> doc_scores = tf.squeeze(
        ...     tf.matmul(
        ...         tf.expand_dims(question_hidden_states, axis=1), docs_dict["retrieved_doc_embeds"], transpose_b=True
        ...     ),
        ...     axis=1,
        ... )
        >>> # 3. Forward to generator
        >>> outputs = model(
        ...     inputs=None,
        ...     context_input_ids=docs_dict["context_input_ids"],
        ...     context_attention_mask=docs_dict["context_attention_mask"],
        ...     doc_scores=doc_scores,
        ...     decoder_input_ids=input_dict["labels"],
        ... )

        >>> # or directly generate
        >>> generated = model.generate(
        ...     context_input_ids=docs_dict["context_input_ids"],
        ...     context_attention_mask=docs_dict["context_attention_mask"],
        ...     doc_scores=doc_scores,
        ... )
        >>> generated_string = tokenizer.batch_decode(generated, skip_special_tokens=True)
        ```'''
    def get_nll(self, seq_logits, doc_scores, target, reduce_loss: bool = False, epsilon: float = 0.0, exclude_bos_score: bool = False, n_docs: Incomplete | None = None): ...
    def generate(self, input_ids: Optional[TFModelInputType] = None, attention_mask: Optional[tf.Tensor] = None, context_input_ids: Incomplete | None = None, context_attention_mask: Incomplete | None = None, doc_scores: Incomplete | None = None, do_deduplication: Incomplete | None = None, num_return_sequences: Incomplete | None = None, num_beams: Incomplete | None = None, n_docs: Incomplete | None = None, **model_kwargs):
        '''
        Implements RAG sequence "thorough" decoding. Read the [`~generation.GenerationMixin.generate`]` documentation
        for more information on how to set other generate input parameters

        Args:
            input_ids (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                The sequence used as a prompt for the generation. If `input_ids` is not passed, then
                `context_input_ids` has to be provided.
            attention_mask (`tf.Tensor` of shape `(batch_size, sequence_length)`, *optional*):
                Mask to avoid performing attention on padding token indices. Mask values selected in `[0, 1]`: - 1 for
                tokens that are **not masked**, - 0 for tokens that are **masked**. [What are attention
                masks?](../glossary#attention-mask)
            context_input_ids (`tf.Tensor` of shape `(batch_size * config.n_docs, config.max_combined_length)`, *optional*, returned when *output_retrieved=True*):
                Input IDs post-processed from the retrieved documents and the question encoder input_ids by the
                retriever.
            context_attention_mask (`tf.Tensor` of shape `(batch_size * config.n_docs, config.max_combined_length)`, *optional*, returned when *output_retrieved=True*):
                Attention mask post-processed from the retrieved documents and the question encoder `input_ids` by the
                retriever. If the model has is not initialized with a `retriever` or `input_ids` is not given,
                `context_input_ids` and `context_attention_mask` have to be provided to the forward pass. They are
                returned by [`~RagRetriever.__call__`].
            doc_scores (`tf.Tensor` of shape `(batch_size, config.n_docs)`):
                Score between each retrieved document embeddings (see `retrieved_doc_embeds`) and
                `question_encoder_last_hidden_state`. If the model has is not initialized with a `retriever` or
                `input_ids` is not given, `doc_scores` has to be provided to the forward pass. `doc_scores` are
                returned by [`~RagRetriever.__call__`].
            do_deduplication (`bool`, *optional*):
                Whether or not to deduplicate the generations from different context documents for a given input. Has
                to be set to `False` if used while training with distributed backend.
            num_return_sequences(`int`, *optional*, defaults to 1):
                The number of independently computed returned sequences for each element in the batch. Note that this
                is not the value we pass to the `generator`\'s `[`~generation.GenerationMixin.generate`]` function,
                where we set `num_return_sequences` to `num_beams`.
            num_beams (`int`, *optional*, defaults to 1):
                Number of beams for beam search. 1 means no beam search.
            n_docs (`int`, *optional*, defaults to `config.n_docs`)
                Number of documents to retrieve and/or number of documents for which to generate an answer.
            kwargs:
                Additional kwargs will be passed to [`~generation.GenerationMixin.generate`]

        Return:
            `tf.Tensor` of shape `(batch_size * num_return_sequences, sequence_length)`: The generated sequences. The
            second dimension (sequence length) is either equal to `max_length` or shorter if all batches finished early
            due to the `eos_token_id`.
        '''
