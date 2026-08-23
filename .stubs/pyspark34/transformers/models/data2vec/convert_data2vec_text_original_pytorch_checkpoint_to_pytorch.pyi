from _typeshed import Incomplete
from fairseq.modules import TransformerSentenceEncoderLayer as TransformerSentenceEncoderLayer
from transformers import Data2VecTextConfig as Data2VecTextConfig, Data2VecTextForMaskedLM as Data2VecTextForMaskedLM, Data2VecTextForSequenceClassification as Data2VecTextForSequenceClassification
from transformers.models.bert.modeling_bert import BertIntermediate as BertIntermediate, BertLayer as BertLayer, BertOutput as BertOutput, BertSelfAttention as BertSelfAttention, BertSelfOutput as BertSelfOutput
from transformers.models.data2vec.data2vec_text import Data2VecTextModel as Data2VecTextModel
from transformers.utils import logging as logging

logger: Incomplete
SAMPLE_TEXT: str

def convert_data2vec_checkpoint_to_pytorch(data2vec_checkpoint_path: str, pytorch_dump_folder_path: str, classification_head: bool):
    """
    Copy/paste/tweak data2vec's weights to our BERT structure.
    """
