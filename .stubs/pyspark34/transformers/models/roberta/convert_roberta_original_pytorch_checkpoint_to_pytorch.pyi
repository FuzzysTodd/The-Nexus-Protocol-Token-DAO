from _typeshed import Incomplete
from fairseq.modules import TransformerSentenceEncoderLayer as TransformerSentenceEncoderLayer
from transformers import RobertaConfig as RobertaConfig, RobertaForMaskedLM as RobertaForMaskedLM, RobertaForSequenceClassification as RobertaForSequenceClassification
from transformers.models.bert.modeling_bert import BertIntermediate as BertIntermediate, BertLayer as BertLayer, BertOutput as BertOutput, BertSelfAttention as BertSelfAttention, BertSelfOutput as BertSelfOutput
from transformers.utils import logging as logging

logger: Incomplete
SAMPLE_TEXT: str

def convert_roberta_checkpoint_to_pytorch(roberta_checkpoint_path: str, pytorch_dump_folder_path: str, classification_head: bool):
    """
    Copy/paste/tweak roberta's weights to our BERT structure.
    """
