from ...configuration_utils import PretrainedConfig as PretrainedConfig
from ...utils import add_start_docstrings as add_start_docstrings
from _typeshed import Incomplete

RAG_CONFIG_DOC: str

class RagConfig(PretrainedConfig):
    model_type: str
    is_composition: bool
    question_encoder: Incomplete
    generator: Incomplete
    reduce_loss: Incomplete
    label_smoothing: Incomplete
    exclude_bos_score: Incomplete
    do_marginalize: Incomplete
    title_sep: Incomplete
    doc_sep: Incomplete
    n_docs: Incomplete
    max_combined_length: Incomplete
    dataset: Incomplete
    dataset_split: Incomplete
    index_name: Incomplete
    retrieval_vector_size: Incomplete
    retrieval_batch_size: Incomplete
    passages_path: Incomplete
    index_path: Incomplete
    use_dummy_dataset: Incomplete
    output_retrieved: Incomplete
    do_deduplication: Incomplete
    use_cache: Incomplete
    forced_eos_token_id: Incomplete
    def __init__(self, vocab_size: Incomplete | None = None, is_encoder_decoder: bool = True, prefix: Incomplete | None = None, bos_token_id: Incomplete | None = None, pad_token_id: Incomplete | None = None, eos_token_id: Incomplete | None = None, decoder_start_token_id: Incomplete | None = None, title_sep: str = ' / ', doc_sep: str = ' // ', n_docs: int = 5, max_combined_length: int = 300, retrieval_vector_size: int = 768, retrieval_batch_size: int = 8, dataset: str = 'wiki_dpr', dataset_split: str = 'train', index_name: str = 'compressed', index_path: Incomplete | None = None, passages_path: Incomplete | None = None, use_dummy_dataset: bool = False, reduce_loss: bool = False, label_smoothing: float = 0.0, do_deduplication: bool = True, exclude_bos_score: bool = False, do_marginalize: bool = False, output_retrieved: bool = False, use_cache: bool = True, forced_eos_token_id: Incomplete | None = None, **kwargs) -> None: ...
    @classmethod
    def from_question_encoder_generator_configs(cls, question_encoder_config: PretrainedConfig, generator_config: PretrainedConfig, **kwargs) -> PretrainedConfig:
        """
        Instantiate a [`EncoderDecoderConfig`] (or a derived class) from a pre-trained encoder model configuration and
        decoder model configuration.

        Returns:
            [`EncoderDecoderConfig`]: An instance of a configuration object
        """
    def to_dict(self):
        """
        Serializes this instance to a Python dictionary. Override the default [`~PretrainedConfig.to_dict`].

        Returns:
            `Dict[str, any]`: Dictionary of all the attributes that make up this configuration instance,
        """
