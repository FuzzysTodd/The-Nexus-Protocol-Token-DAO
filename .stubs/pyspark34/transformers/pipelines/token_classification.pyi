import numpy as np
from ..models.auto.modeling_auto import MODEL_FOR_TOKEN_CLASSIFICATION_MAPPING as MODEL_FOR_TOKEN_CLASSIFICATION_MAPPING
from ..models.auto.modeling_tf_auto import TF_MODEL_FOR_TOKEN_CLASSIFICATION_MAPPING as TF_MODEL_FOR_TOKEN_CLASSIFICATION_MAPPING
from ..models.bert.tokenization_bert import BasicTokenizer as BasicTokenizer
from ..utils import ExplicitEnum as ExplicitEnum, add_end_docstrings as add_end_docstrings, is_tf_available as is_tf_available, is_torch_available as is_torch_available
from .base import ArgumentHandler as ArgumentHandler, Dataset as Dataset, PIPELINE_INIT_ARGS as PIPELINE_INIT_ARGS, Pipeline as Pipeline
from _typeshed import Incomplete
from typing import List, Optional, Tuple, Union

class TokenClassificationArgumentHandler(ArgumentHandler):
    """
    Handles arguments for token classification.
    """
    def __call__(self, inputs: Union[str, List[str]], **kwargs): ...

class AggregationStrategy(ExplicitEnum):
    """All the valid aggregation strategies for TokenClassificationPipeline"""
    NONE: str
    SIMPLE: str
    FIRST: str
    AVERAGE: str
    MAX: str

class TokenClassificationPipeline(Pipeline):
    '''
    Named Entity Recognition pipeline using any `ModelForTokenClassification`. See the [named entity recognition
    examples](../task_summary#named-entity-recognition) for more information.

    Example:

    ```python
    >>> from transformers import pipeline

    >>> token_classifier = pipeline(model="Jean-Baptiste/camembert-ner", aggregation_strategy="simple")
    >>> sentence = "Je m\'appelle jean-baptiste et je vis à montréal"
    >>> tokens = token_classifier(sentence)
    >>> tokens
    [{\'entity_group\': \'PER\', \'score\': 0.9931, \'word\': \'jean-baptiste\', \'start\': 12, \'end\': 26}, {\'entity_group\': \'LOC\', \'score\': 0.998, \'word\': \'montréal\', \'start\': 38, \'end\': 47}]

    >>> token = tokens[0]
    >>> # Start and end provide an easy way to highlight words in the original text.
    >>> sentence[token["start"] : token["end"]]
    \' jean-baptiste\'

    >>> # Some models use the same idea to do part of speech.
    >>> syntaxer = pipeline(model="vblagoje/bert-english-uncased-finetuned-pos", aggregation_strategy="simple")
    >>> syntaxer("My name is Sarah and I live in London")
    [{\'entity_group\': \'PRON\', \'score\': 0.999, \'word\': \'my\', \'start\': 0, \'end\': 2}, {\'entity_group\': \'NOUN\', \'score\': 0.997, \'word\': \'name\', \'start\': 3, \'end\': 7}, {\'entity_group\': \'AUX\', \'score\': 0.994, \'word\': \'is\', \'start\': 8, \'end\': 10}, {\'entity_group\': \'PROPN\', \'score\': 0.999, \'word\': \'sarah\', \'start\': 11, \'end\': 16}, {\'entity_group\': \'CCONJ\', \'score\': 0.999, \'word\': \'and\', \'start\': 17, \'end\': 20}, {\'entity_group\': \'PRON\', \'score\': 0.999, \'word\': \'i\', \'start\': 21, \'end\': 22}, {\'entity_group\': \'VERB\', \'score\': 0.998, \'word\': \'live\', \'start\': 23, \'end\': 27}, {\'entity_group\': \'ADP\', \'score\': 0.999, \'word\': \'in\', \'start\': 28, \'end\': 30}, {\'entity_group\': \'PROPN\', \'score\': 0.999, \'word\': \'london\', \'start\': 31, \'end\': 37}]
    ```

    Learn more about the basics of using a pipeline in the [pipeline tutorial](../pipeline_tutorial)

    This token recognition pipeline can currently be loaded from [`pipeline`] using the following task identifier:
    `"ner"` (for predicting the classes of tokens in a sequence: person, organisation, location or miscellaneous).

    The models that this pipeline can use are models that have been fine-tuned on a token classification task. See the
    up-to-date list of available models on
    [huggingface.co/models](https://huggingface.co/models?filter=token-classification).
    '''
    default_input_names: str
    def __init__(self, args_parser=..., *args, **kwargs) -> None: ...
    def __call__(self, inputs: Union[str, List[str]], **kwargs):
        '''
        Classify each token of the text(s) given as inputs.

        Args:
            inputs (`str` or `List[str]`):
                One or several texts (or one list of texts) for token classification.

        Return:
            A list or a list of list of `dict`: Each result comes as a list of dictionaries (one for each token in the
            corresponding input, or each entity if this pipeline was instantiated with an aggregation_strategy) with
            the following keys:

            - **word** (`str`) -- The token/word classified. This is obtained by decoding the selected tokens. If you
              want to have the exact string in the original sentence, use `start` and `end`.
            - **score** (`float`) -- The corresponding probability for `entity`.
            - **entity** (`str`) -- The entity predicted for that token/word (it is named *entity_group* when
              *aggregation_strategy* is not `"none"`.
            - **index** (`int`, only present when `aggregation_strategy="none"`) -- The index of the corresponding
              token in the sentence.
            - **start** (`int`, *optional*) -- The index of the start of the corresponding entity in the sentence. Only
              exists if the offsets are available within the tokenizer
            - **end** (`int`, *optional*) -- The index of the end of the corresponding entity in the sentence. Only
              exists if the offsets are available within the tokenizer
        '''
    def preprocess(self, sentence, offset_mapping: Incomplete | None = None): ...
    def postprocess(self, model_outputs, aggregation_strategy=..., ignore_labels: Incomplete | None = None): ...
    def gather_pre_entities(self, sentence: str, input_ids: np.ndarray, scores: np.ndarray, offset_mapping: Optional[List[Tuple[int, int]]], special_tokens_mask: np.ndarray, aggregation_strategy: AggregationStrategy) -> List[dict]:
        """Fuse various numpy arrays into dicts with all the information needed for aggregation"""
    def aggregate(self, pre_entities: List[dict], aggregation_strategy: AggregationStrategy) -> List[dict]: ...
    def aggregate_word(self, entities: List[dict], aggregation_strategy: AggregationStrategy) -> dict: ...
    def aggregate_words(self, entities: List[dict], aggregation_strategy: AggregationStrategy) -> List[dict]:
        """
        Override tokens from a given word that disagree to force agreement on word boundaries.

        Example: micro|soft| com|pany| B-ENT I-NAME I-ENT I-ENT will be rewritten with first strategy as microsoft|
        company| B-ENT I-ENT
        """
    def group_sub_entities(self, entities: List[dict]) -> dict:
        """
        Group together the adjacent tokens with the same entity predicted.

        Args:
            entities (`dict`): The entities predicted by the pipeline.
        """
    def get_tag(self, entity_name: str) -> Tuple[str, str]: ...
    def group_entities(self, entities: List[dict]) -> List[dict]:
        """
        Find and group together the adjacent tokens with the same entity predicted.

        Args:
            entities (`dict`): The entities predicted by the pipeline.
        """
NerPipeline = TokenClassificationPipeline
