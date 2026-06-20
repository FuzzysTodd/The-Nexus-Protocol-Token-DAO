from transformers import BertConfig as BertConfig, BertForMaskedLM as BertForMaskedLM
from transformers.models.bert.modeling_bert import BertIntermediate as BertIntermediate, BertLayer as BertLayer, BertOutput as BertOutput, BertPooler as BertPooler, BertSelfAttention as BertSelfAttention, BertSelfOutput as BertSelfOutput
from transformers.utils import logging as logging

def convert_checkpoint_to_pytorch(tf_checkpoint_path: str, config_path: str, pytorch_dump_path: str): ...
