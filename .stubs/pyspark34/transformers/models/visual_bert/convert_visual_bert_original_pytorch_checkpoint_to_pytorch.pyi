from _typeshed import Incomplete
from transformers import VisualBertConfig as VisualBertConfig, VisualBertForMultipleChoice as VisualBertForMultipleChoice, VisualBertForPreTraining as VisualBertForPreTraining, VisualBertForQuestionAnswering as VisualBertForQuestionAnswering, VisualBertForVisualReasoning as VisualBertForVisualReasoning
from transformers.utils import logging as logging

logger: Incomplete
rename_keys_prefix: Incomplete
ACCEPTABLE_CHECKPOINTS: Incomplete

def load_state_dict(checkpoint_path): ...
def get_new_dict(d, config, rename_keys_prefix=...): ...
def convert_visual_bert_checkpoint(checkpoint_path, pytorch_dump_folder_path) -> None:
    """
    Copy/paste/tweak model's weights to our VisualBERT structure.
    """
