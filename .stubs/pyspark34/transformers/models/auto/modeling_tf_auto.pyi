from ...utils import logging as logging
from .auto_factory import _BaseAutoModelClass, auto_class_update as auto_class_update
from .configuration_auto import CONFIG_MAPPING_NAMES as CONFIG_MAPPING_NAMES
from _typeshed import Incomplete

logger: Incomplete
TF_MODEL_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_PRETRAINING_MAPPING_NAMES: Incomplete
TF_MODEL_WITH_LM_HEAD_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_CAUSAL_LM_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_MASKED_IMAGE_MODELING_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_IMAGE_CLASSIFICATION_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_SEMANTIC_SEGMENTATION_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_VISION_2_SEQ_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_MASKED_LM_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_SPEECH_SEQ_2_SEQ_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_SEQUENCE_CLASSIFICATION_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_QUESTION_ANSWERING_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_DOCUMENT_QUESTION_ANSWERING_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_TABLE_QUESTION_ANSWERING_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_TOKEN_CLASSIFICATION_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_MULTIPLE_CHOICE_MAPPING_NAMES: Incomplete
TF_MODEL_FOR_NEXT_SENTENCE_PREDICTION_MAPPING_NAMES: Incomplete
TF_MODEL_MAPPING: Incomplete
TF_MODEL_FOR_PRETRAINING_MAPPING: Incomplete
TF_MODEL_WITH_LM_HEAD_MAPPING: Incomplete
TF_MODEL_FOR_CAUSAL_LM_MAPPING: Incomplete
TF_MODEL_FOR_MASKED_IMAGE_MODELING_MAPPING: Incomplete
TF_MODEL_FOR_IMAGE_CLASSIFICATION_MAPPING: Incomplete
TF_MODEL_FOR_SEMANTIC_SEGMENTATION_MAPPING: Incomplete
TF_MODEL_FOR_VISION_2_SEQ_MAPPING: Incomplete
TF_MODEL_FOR_MASKED_LM_MAPPING: Incomplete
TF_MODEL_FOR_SEQ_TO_SEQ_CAUSAL_LM_MAPPING: Incomplete
TF_MODEL_FOR_SEQUENCE_CLASSIFICATION_MAPPING: Incomplete
TF_MODEL_FOR_SPEECH_SEQ_2_SEQ_MAPPING: Incomplete
TF_MODEL_FOR_QUESTION_ANSWERING_MAPPING: Incomplete
TF_MODEL_FOR_DOCUMENT_QUESTION_ANSWERING_MAPPING: Incomplete
TF_MODEL_FOR_TABLE_QUESTION_ANSWERING_MAPPING: Incomplete
TF_MODEL_FOR_TOKEN_CLASSIFICATION_MAPPING: Incomplete
TF_MODEL_FOR_MULTIPLE_CHOICE_MAPPING: Incomplete
TF_MODEL_FOR_NEXT_SENTENCE_PREDICTION_MAPPING: Incomplete

class TFAutoModel(_BaseAutoModelClass): ...
class TFAutoModelForPreTraining(_BaseAutoModelClass): ...
class _TFAutoModelWithLMHead(_BaseAutoModelClass): ...
class TFAutoModelForCausalLM(_BaseAutoModelClass): ...
class TFAutoModelForMaskedImageModeling(_BaseAutoModelClass): ...
class TFAutoModelForImageClassification(_BaseAutoModelClass): ...
class TFAutoModelForSemanticSegmentation(_BaseAutoModelClass): ...

TF_AutoModelForSemanticSegmentation: Incomplete

class TFAutoModelForVision2Seq(_BaseAutoModelClass): ...
class TFAutoModelForMaskedLM(_BaseAutoModelClass): ...
class TFAutoModelForSeq2SeqLM(_BaseAutoModelClass): ...
class TFAutoModelForSequenceClassification(_BaseAutoModelClass): ...
class TFAutoModelForQuestionAnswering(_BaseAutoModelClass): ...
class TFAutoModelForDocumentQuestionAnswering(_BaseAutoModelClass): ...
class TFAutoModelForTableQuestionAnswering(_BaseAutoModelClass): ...
class TFAutoModelForTokenClassification(_BaseAutoModelClass): ...
class TFAutoModelForMultipleChoice(_BaseAutoModelClass): ...
class TFAutoModelForNextSentencePrediction(_BaseAutoModelClass): ...
class TFAutoModelForSpeechSeq2Seq(_BaseAutoModelClass): ...

class TFAutoModelWithLMHead(_TFAutoModelWithLMHead):
    @classmethod
    def from_config(cls, config): ...
    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs): ...
