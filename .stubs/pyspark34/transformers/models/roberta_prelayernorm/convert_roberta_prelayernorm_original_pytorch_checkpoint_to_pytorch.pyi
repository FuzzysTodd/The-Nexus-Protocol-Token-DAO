from _typeshed import Incomplete
from transformers import AutoTokenizer as AutoTokenizer, RobertaPreLayerNormConfig as RobertaPreLayerNormConfig, RobertaPreLayerNormForMaskedLM as RobertaPreLayerNormForMaskedLM
from transformers.utils import logging as logging

logger: Incomplete

def convert_roberta_prelayernorm_checkpoint_to_pytorch(checkpoint_repo: str, pytorch_dump_folder_path: str):
    """
    Copy/paste/tweak roberta_prelayernorm's weights to our BERT structure.
    """
