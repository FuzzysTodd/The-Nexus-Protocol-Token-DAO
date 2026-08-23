from _typeshed import Incomplete
from transformers import BertConfig as BertConfig, BertForMaskedLM as BertForMaskedLM, BertModel as BertModel, RobertaTokenizer as RobertaTokenizer
from transformers.models.bert.modeling_bert import BertIntermediate as BertIntermediate, BertLayer as BertLayer, BertOutput as BertOutput, BertSelfAttention as BertSelfAttention, BertSelfOutput as BertSelfOutput
from transformers.utils import logging as logging

logger: Incomplete
SAMPLE_TEXT: str

def convert_bort_checkpoint_to_pytorch(bort_checkpoint_path: str, pytorch_dump_folder_path: str):
    """
    Convert the original Bort checkpoint (based on MXNET and Gluonnlp) to our BERT structure-
    """
