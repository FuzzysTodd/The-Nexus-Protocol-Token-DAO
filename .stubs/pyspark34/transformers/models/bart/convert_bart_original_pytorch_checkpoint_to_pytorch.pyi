from _typeshed import Incomplete
from transformers import BartConfig as BartConfig, BartForConditionalGeneration as BartForConditionalGeneration, BartForSequenceClassification as BartForSequenceClassification, BartModel as BartModel, BartTokenizer as BartTokenizer
from transformers.utils import logging as logging

FAIRSEQ_MODELS: Incomplete
extra_arch: Incomplete
logger: Incomplete
SAMPLE_TEXT: str
mnli_rename_keys: Incomplete

def remove_ignore_keys_(state_dict) -> None: ...
def rename_key(dct, old, new) -> None: ...
def load_xsum_checkpoint(checkpoint_path):
    """Checkpoint path should end in model.pt"""
def make_linear_from_emb(emb): ...
def convert_bart_checkpoint(checkpoint_path, pytorch_dump_folder_path, hf_checkpoint_name: Incomplete | None = None) -> None:
    """
    Copy/paste/tweak model's weights to our BERT structure.
    """
